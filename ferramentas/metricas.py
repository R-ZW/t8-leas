#!/usr/bin/env python3
"""Calcula as medidas do §8 do protocolo e gera analise/metricas.md (tabelas do §9).

Uso:
    python ferramentas/metricas.py <artefato> [--runs DIR] [--chave ARQ] [--cadeias 3]

Lê   runs/<artefato>/analise/decisoes.csv      (de extrair_decisoes.py)
     runs/<artefato>/analise/evidencias.csv    (opcional; de cegar.py + verificador)
Grava runs/<artefato>/analise/metricas.md

Regras fixadas (pré-registro):
- Decisão modal: decisão mais frequente nas cadeias de cada LLM x etapa x selo.
  Se duas ou mais decisões empatam no topo, a moda é "Empate" e é listada
  explicitamente; não há desempate.
- Estabilidade: nº de cadeias com a decisão modal / nº de cadeias ESPERADAS
  (--cadeias, padrão 3). Cadeia sem decisão extraída conta como não modal.
- Cobertura: decisões diferentes de Indeterminado / decisões extraídas.
- Consistente com o oficial (por LLM e selo): modal após execução (etapa B)
  igual ao oficial E estabilidade >= 2/3. Empate nunca é consistente.
- Consistentes entre si (por etapa e selo): as três LLMs com a mesma modal,
  sem empate.
- Transição A->B por cadeia: confirma (A = B), contradiz (Atribuir <-> Não
  atribuir), resolve incerteza (Indeterminado -> firme), introduz incerteza
  (firme -> Indeterminado). "Confirma" ainda exige conferir à mão se a
  evidência é coerente, como pede o §9.
- Calibração: confiança média quando a decisão coincide com o oficial versus
  quando não coincide (separando Indeterminado), e escore de Brier da confiança
  lida como probabilidade de o comitê ter atribuído o selo (Prompt A, item 5).
- Precisão das evidências: corretas / total citadas, por LLM. Com linhas ainda
  sem classe, o valor é marcado como parcial.

Todas as medidas são descritivas: com um artefato não há base para testes
estatísticos, e metricas.md diz isso.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extrair_decisoes import (  # noqa: E402
    DECISOES, PROVEDORES, RUNS_PADRAO, SELOS, chave_normalizada, console_seguro,
    normalizar_decisao,
)

NOMES = {"openai": "OpenAI", "anthropic": "Anthropic", "google": "Google", "humano": "Humano"}
ETAPAS = ("A", "B")
NOME_ETAPA = {"A": "Analítica (A)", "B": "Após execução (B)"}
ABREV = {"Atribuir": "Atribuir", "Não atribuir": "Não atribuir", "Indeterminado": "Indet."}
CLASSES_EVIDENCIA = ("correta", "mal_interpretada", "inexistente", "nao_verificavel")
PREENCHER = "_(preencher)_"
CAUSAS = (
    "Erro de julgamento da LLM", "Interpretação do critério",
    "Insumo indisponível publicamente", "Diferença de versão", "Ambiente",
    "Possível erro do comitê",
)


# --------------------------------------------------------------------------- #
# Leitura
# --------------------------------------------------------------------------- #
def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def nome(llm: str) -> str:
    return NOMES.get(llm, llm)


class Dados:
    def __init__(self, linhas: list[dict], n_cadeias: int):
        self.n_cadeias = n_cadeias
        self.avisos: list[str] = []
        # (llm, etapa, selo) -> {cadeia: linha}
        self.por_grupo: dict[tuple, dict[str, dict]] = defaultdict(dict)
        self.oficial: dict[str, str] = {}
        llms = set()
        for i, linha in enumerate(linhas, start=2):
            decisao = normalizar_decisao(linha.get("decisao", ""))
            etapa, selo = linha.get("etapa", "").strip().upper(), linha.get("selo", "").strip().upper()
            if decisao is None or etapa not in ETAPAS or selo not in SELOS:
                self.avisos.append(f"decisoes.csv, linha {i}: decisão/etapa/selo inválidos; ignorada")
                continue
            linha = dict(linha, decisao=decisao, etapa=etapa, selo=selo)
            chave = (linha["llm"], etapa, selo)
            if linha["cadeia"] in self.por_grupo[chave]:
                self.avisos.append(f"decisoes.csv, linha {i}: cadeia repetida; mantida a primeira")
                continue
            self.por_grupo[chave][linha["cadeia"]] = linha
            if linha["llm"] != "humano":
                llms.add(linha["llm"])
            oficial = normalizar_decisao(linha.get("oficial", ""))
            if oficial:
                if self.oficial.setdefault(selo, oficial) != oficial:
                    self.avisos.append(f"decisoes.csv: valores de \"oficial\" diferentes para {selo}")
        ordem = {p: i for i, p in enumerate(PROVEDORES)}
        self.llms = sorted(llms, key=lambda p: (ordem.get(p, 99), p))
        for selo in SELOS:
            if selo not in self.oficial:
                self.avisos.append(f"selo oficial {selo} ausente em decisoes.csv; comparações com o oficial ficam n.d.")

    def decisoes(self, llm, etapa, selo) -> list[str]:
        return [l["decisao"] for l in self.por_grupo.get((llm, etapa, selo), {}).values()]

    def linhas(self, llm, etapa, selo) -> dict[str, dict]:
        return self.por_grupo.get((llm, etapa, selo), {})


# --------------------------------------------------------------------------- #
# Medidas
# --------------------------------------------------------------------------- #
class Moda:
    def __init__(self, decisoes: list[str], esperadas: int):
        self.n = len(decisoes)
        self.esperadas = max(esperadas, self.n)
        contagem = Counter(decisoes)
        self.contagem = contagem
        topo = max(contagem.values()) if contagem else 0
        self.lideres = sorted((d for d, c in contagem.items() if c == topo), key=DECISOES.index)
        self.freq = topo

    @property
    def vazia(self) -> bool:
        return self.n == 0

    @property
    def empate(self) -> bool:
        return len(self.lideres) > 1

    @property
    def valor(self) -> str | None:
        """Decisão modal, ou None se vazia ou empatada."""
        return self.lideres[0] if len(self.lideres) == 1 else None

    @property
    def estabilidade(self) -> Fraction:
        return Fraction(self.freq, self.esperadas) if self.esperadas else Fraction(0)

    def texto(self) -> str:
        if self.vazia:
            return "sem decisões"
        if self.empate:
            return "Empate: " + " = ".join(ABREV[d] for d in self.lideres) + f" ({self.freq} cada)"
        return ABREV[self.valor]

    def estab_texto(self) -> str:
        if self.vazia:
            return "0/" + str(self.esperadas)
        sufixo = " (empate)" if self.empate else ""
        return f"{self.freq}/{self.esperadas}{sufixo}"

    def com_estab(self) -> str:
        return f"{self.texto()} ({self.estab_texto()})"


def cobertura(decisoes: list[str]) -> str:
    if not decisoes:
        return "n.d."
    firmes = sum(d != "Indeterminado" for d in decisoes)
    return f"{firmes}/{len(decisoes)} ({firmes / len(decisoes):.0%})"


def coincide(moda: Moda, oficial: str | None) -> str:
    if not oficial or moda.vazia:
        return "n.d."
    if moda.empate:
        return "n.d. (empate)"
    return "Sim" if moda.valor == oficial else "Não"


def relacao(a: str, b: str) -> str:
    if a == b:
        return "Confirma"
    if "Indeterminado" not in (a, b):
        return "Contradiz"
    if a == "Indeterminado":
        return "Resolve incerteza"
    return "Introduz incerteza"


def media(valores: list[float]) -> str:
    return f"{sum(valores) / len(valores):.1f} (n={len(valores)})" if valores else "n.d."


def tabela(cabecalho: list[str], linhas: list[list[str]]) -> list[str]:
    def celula(v):
        return str(v).replace("|", "\\|").replace("\n", " ")
    saida = ["| " + " | ".join(cabecalho) + " |", "|" + "---|" * len(cabecalho)]
    saida += ["| " + " | ".join(celula(c) for c in l) + " |" for l in linhas]
    return saida + [""]


# --------------------------------------------------------------------------- #
# Seções do relatório
# --------------------------------------------------------------------------- #
def secao_modal(d: Dados, modas) -> list[str]:
    out = ["## 1. Decisão modal, estabilidade e cobertura", "",
           "Estabilidade = cadeias com a decisão modal / cadeias esperadas "
           f"({d.n_cadeias}). Cobertura = decisões ≠ Indeterminado / decisões extraídas.", ""]
    linhas = []
    for llm in d.llms:
        for etapa in ETAPAS:
            for selo in SELOS:
                m = modas[(llm, etapa, selo)]
                por_cadeia = d.linhas(llm, etapa, selo)
                cadeias = sorted(set(por_cadeia) | {str(i) for i in range(1, d.n_cadeias + 1)},
                                 key=lambda c: (len(c), c))
                lista = ", ".join(f"c{c}: {ABREV[por_cadeia[c]['decisao']]}" if c in por_cadeia
                                  else f"c{c}: —" for c in cadeias)
                linhas.append([nome(llm), etapa, selo, lista, m.texto(), m.estab_texto(),
                               cobertura(d.decisoes(llm, etapa, selo)),
                               ABREV.get(d.oficial.get(selo), "n.d."),
                               coincide(m, d.oficial.get(selo))])
    out += tabela(["LLM", "Etapa", "Selo", "Decisões por cadeia", "Modal", "Estabilidade",
                   "Cobertura", "Oficial", "Coincide"], linhas)
    linhas = []
    for llm in d.llms:
        for etapa in ETAPAS:
            todas = [x for selo in SELOS for x in d.decisoes(llm, etapa, selo)]
            linhas.append([nome(llm), etapa, cobertura(todas)])
    out += ["Cobertura agregada (F e R):", ""]
    out += tabela(["LLM", "Etapa", "Cobertura"], linhas)
    return out


def secao_empates(d: Dados, modas) -> list[str]:
    out = ["## 2. Empates de moda", ""]
    empates = [(k, m) for k, m in modas.items() if m.empate]
    if not empates:
        return out + ["Nenhum empate de moda.", ""]
    out += ["Os grupos abaixo não têm decisão modal única. Nenhum desempate foi aplicado: "
            "eles aparecem como \"Empate\" nas tabelas, não contam como coincidentes nem "
            "como consistentes e devem ser discutidos no relatório.", ""]
    linhas = [[nome(llm), etapa, selo,
               ", ".join(f"{ABREV[x]}: {c}" for x, c in sorted(m.contagem.items(), key=lambda t: DECISOES.index(t[0]))),
               f"{m.n}/{d.n_cadeias}"]
              for (llm, etapa, selo), m in empates]
    return out + tabela(["LLM", "Etapa", "Selo", "Contagem", "Decisões extraídas"], linhas)


def secao_comparativa(d: Dados, modas, humano) -> list[str]:
    out = ["## 3. Tabela comparativa (§9, item 10)", "",
           "\"Causa da divergência\" e \"Evidência-chave\" são preenchidas à mão. Causas "
           "admitidas (§8): " + "; ".join(CAUSAS) + ". \"n.a.\" = modal A e B coincidem com o oficial.", ""]
    linhas = []
    for llm in d.llms + (["humano"] if humano else []):
        for selo in SELOS:
            ma, mb = modas[(llm, "A", selo)], modas[(llm, "B", selo)]
            oficial = d.oficial.get(selo)
            ca, cb = coincide(ma, oficial), coincide(mb, oficial)
            if ma.valor and mb.valor:
                mudou = "Sim" if ma.valor != mb.valor else "Não"
            elif ma.vazia or mb.vazia:
                mudou = "n.d."
            else:
                mudou = "n.d. (empate)"
            causa = "n.a." if ca == "Sim" and cb == "Sim" else PREENCHER
            linhas.append([nome(llm), selo, ABREV.get(oficial, "n.d."), ma.com_estab(),
                           mb.com_estab(), f"{ca} / {cb}", mudou, causa, PREENCHER])
    return out + tabela(["LLM", "Selo", "Oficial", "Analítica (modal, estabilidade)",
                         "Após execução (modal, estabilidade)", "Coincide (A / B)", "Mudou?",
                         "Causa da divergência", "Evidência-chave"], linhas)


def secao_consistencia(d: Dados, modas) -> list[str]:
    out = ["## 4. Critério pré-registrado de consistência", "",
           "Consistente com o oficial = modal após execução igual ao oficial e "
           "estabilidade ≥ 2/3. Consistentes entre si = as três LLMs com a mesma modal.", ""]
    linhas = []
    for llm in d.llms:
        for selo in SELOS:
            m = modas[(llm, "B", selo)]
            oficial = d.oficial.get(selo)
            if m.vazia or not oficial:
                veredito = "n.d."
            elif m.empate:
                veredito = "Não (empate)"
            else:
                ok = m.valor == oficial and m.estabilidade >= Fraction(2, 3)
                veredito = "Sim" if ok else "Não"
            linhas.append([nome(llm), selo, m.texto(), m.estab_texto(),
                           ABREV.get(oficial, "n.d."), veredito])
    out += tabela(["LLM", "Selo", "Modal B", "Estabilidade B", "Oficial",
                   "Consistente com o oficial?"], linhas)
    out += ["### Consistência e concordância entre LLMs", "",
            "Pares concordantes = pares de LLMs com a mesma modal, entre os pares "
            "comparáveis (sem empate e com decisões).", ""]
    linhas = []
    for etapa in ETAPAS:
        for selo in SELOS:
            ms = {llm: modas[(llm, etapa, selo)] for llm in d.llms}
            valores = [m.valor for m in ms.values()]
            if len(d.llms) < 3:
                entre = f"n.d. ({len(d.llms)} LLMs)"
            elif any(m.empate for m in ms.values()):
                entre = "Não (há empate)"
            elif any(v is None for v in valores):
                entre = "n.d."
            else:
                entre = "Sim" if len(set(valores)) == 1 else "Não"
            pares = list(combinations(d.llms, 2))
            comparaveis = [(a, b) for a, b in pares if ms[a].valor and ms[b].valor]
            iguais = sum(ms[a].valor == ms[b].valor for a, b in comparaveis)
            excluidos = len(pares) - len(comparaveis)
            prop = f"{iguais}/{len(comparaveis)}" if comparaveis else "n.d."
            if excluidos:
                prop += f" ({excluidos} par(es) excluído(s) por empate/ausência)"
            detalhe = "; ".join(f"{nome(a)}–{nome(b)}: " + (
                ("igual" if ms[a].valor == ms[b].valor else "diferente") if (a, b) in comparaveis else "n.d.")
                for a, b in pares)
            linhas.append([NOME_ETAPA[etapa], selo,
                           " / ".join(f"{nome(l)}: {ms[l].texto()}" for l in d.llms),
                           entre, prop, detalhe])
    return out + tabela(["Etapa", "Selo", "Modais", "Consistentes entre si?",
                         "Pares concordantes", "Pares"], linhas)


def secao_transicao(d: Dados) -> list[str]:
    out = ["## 5. Execução confirma ou contradiz (§9, item 12)", "",
           "Uma linha por cadeia com decisão nas duas etapas. \"Confirma\" ainda requer "
           "conferir se a evidência é coerente; \"Passo do registro que motivou\" é "
           "preenchido à mão.", ""]
    linhas, pares, sem_par = [], [], []
    for llm in d.llms + ["humano"]:
        for selo in SELOS:
            la, lb = d.linhas(llm, "A", selo), d.linhas(llm, "B", selo)
            for cadeia in sorted(set(la) | set(lb), key=lambda c: (len(c), c)):
                if cadeia in la and cadeia in lb:
                    a, b = la[cadeia]["decisao"], lb[cadeia]["decisao"]
                    rel = relacao(a, b)
                    pares.append((llm, selo, a, b, rel))
                    linhas.append([nome(llm), selo, cadeia, ABREV[a], ABREV[b], rel, PREENCHER])
                else:
                    sem_par.append(f"{nome(llm)}, {selo}, cadeia {cadeia}: falta a etapa "
                                   + ("B" if cadeia in la else "A"))
    out += tabela(["LLM", "Selo", "Cadeia", "Decisão A", "Decisão B", "Relação",
                   "Passo do registro que motivou"], linhas)
    if sem_par:
        out += ["Cadeias sem par A→B (fora da matriz):", ""] + [f"- {s}" for s in sem_par] + [""]

    llm_pares = [p for p in pares if p[0] != "humano"]
    for selo in SELOS:
        out += [f"### Matriz de transição A → B — selo {selo} (LLMs, todas as cadeias)", ""]
        cont = Counter((a, b) for _, s, a, b, _ in llm_pares if s == selo)
        linhas = [[f"A: {ABREV[a]}"] + [str(cont[(a, b)]) for b in DECISOES] + [str(sum(cont[(a, b)] for b in DECISOES))]
                  for a in DECISOES]
        out += tabela(["", *(f"B: {ABREV[b]}" for b in DECISOES), "Total"], linhas)
    categorias = ("Confirma", "Contradiz", "Resolve incerteza", "Introduz incerteza")
    out += ["### Relações por LLM", ""]
    linhas = []
    for llm in d.llms + ["humano"]:
        for selo in SELOS:
            cont = Counter(rel for l, s, _, _, rel in pares if l == llm and s == selo)
            if llm == "humano" and not cont:
                continue
            linhas.append([nome(llm), selo] + [str(cont[c]) for c in categorias])
    return out + tabela(["LLM", "Selo", *categorias], linhas)


def secao_calibracao(d: Dados) -> list[str]:
    out = ["## 6. Calibração", "",
           "Confiança média (0–100) quando a decisão coincide com o oficial versus quando não "
           "coincide. Brier = média de (confiança/100 − 1[oficial atribuiu])², lendo a confiança "
           "como a probabilidade de o comitê ter atribuído o selo (Prompt A, item 5); menor é melhor.", ""]
    linhas = []
    for llm in d.llms + ["humano"]:
        for etapa in ETAPAS:
            acerto, erro_firme, indet, brier, sem_conf = [], [], [], [], 0
            for selo in SELOS:
                oficial = d.oficial.get(selo)
                if not oficial:
                    continue
                for l in d.linhas(llm, etapa, selo).values():
                    try:
                        conf = float(l.get("confianca", ""))
                    except ValueError:
                        sem_conf += 1
                        continue
                    if l["decisao"] == oficial:
                        acerto.append(conf)
                    elif l["decisao"] == "Indeterminado":
                        indet.append(conf)
                    else:
                        erro_firme.append(conf)
                    brier.append((conf / 100 - (1.0 if oficial == "Atribuir" else 0.0)) ** 2)
            if not (acerto or erro_firme or indet or sem_conf):
                continue
            linhas.append([nome(llm), etapa, media(acerto), media(erro_firme + indet),
                           media(erro_firme), media(indet),
                           f"{sum(brier) / len(brier):.3f}" if brier else "n.d.", str(sem_conf)])
    return out + tabela(["LLM", "Etapa", "Coincide", "Não coincide (total)",
                         "…decisão firme oposta", "…Indeterminado", "Brier", "Sem confiança"], linhas)


def secao_humano(d: Dados, modas, humano) -> list[str]:
    out = ["## 7. Linha de base humana", ""]
    linhas = []
    for etapa in ETAPAS:
        for selo in SELOS:
            h = d.linhas("humano", etapa, selo)
            if not h:
                linhas.append([NOME_ETAPA[etapa], selo, "**ausente**", "n.d."]
                              + ["n.d."] * len(d.llms))
                continue
            dh = next(iter(h.values()))["decisao"]
            oficial = d.oficial.get(selo)
            vs_of = ("Sim" if dh == oficial else "Não") if oficial else "n.d."
            vs_llm = []
            for llm in d.llms:
                m = modas[(llm, etapa, selo)]
                vs_llm.append("n.d. (empate)" if m.empate else "n.d." if m.vazia
                              else ("igual" if m.valor == dh else f"diferente ({ABREV[m.valor]})"))
            linhas.append([NOME_ETAPA[etapa], selo, ABREV[dh], vs_of] + vs_llm)
    if not humano:
        out += ["**Nenhuma decisão humana em decisoes.csv** (arquivos `humano/` ausentes ou "
                "com pendência de extração). A comparação abaixo fica n.d.", ""]
    return out + tabela(["Etapa", "Selo", "Humano", "Coincide com oficial",
                         *(f"vs. modal {nome(l)}" for l in d.llms)], linhas)


def ler_chave(caminho: Path | None) -> dict[str, str]:
    if not caminho:
        return {}
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    return dados.get("mapeamento", {})


def secao_evidencias(caminho: Path, chave: dict[str, str]) -> list[str]:
    out = ["## 8. Precisão das evidências", ""]
    if not caminho.exists():
        return out + [f"`{caminho.name}` não encontrado; precisão n.d.", ""]
    linhas_csv = ler_csv(caminho)
    rotulos_cegos = {l.get("llm", "") for l in linhas_csv}
    if chave:
        out += ["Provedores revelados com a chave de cegamento informada em `--chave`.", ""]
    elif any(r.startswith("M") for r in rotulos_cegos):
        out += ["Rótulos cegos (M1–M3) mantidos: passe `--chave` depois da verificação para revelar.", ""]
    grupos: dict[str, Counter] = defaultdict(Counter)
    invalidas = []
    for i, l in enumerate(linhas_csv, start=2):
        llm = chave.get(l.get("llm", ""), l.get("llm", ""))
        classe = chave_normalizada(l.get("classe", "") or "")
        if not classe:
            grupos[llm]["pendente"] += 1
        elif classe in CLASSES_EVIDENCIA:
            grupos[llm][classe] += 1
        else:
            grupos[llm]["invalida"] += 1
            invalidas.append(f"linha {i}: classe \"{l.get('classe')}\" não reconhecida")
    ordem = {p: i for i, p in enumerate(PROVEDORES)}
    linhas = []
    for llm in sorted(grupos, key=lambda p: (ordem.get(p, 99), p)):
        c = grupos[llm]
        total = sum(c.values())
        classificadas = sum(c[k] for k in CLASSES_EVIDENCIA)
        if total and classificadas == total:
            precisao = f"{c['correta']}/{total} ({c['correta'] / total:.0%})"
        elif classificadas:
            precisao = (f"parcial: {c['correta']}/{classificadas} classificadas "
                        f"({c['pendente'] + c['invalida']} sem classe válida)")
        else:
            precisao = "n.d. (nenhuma classificada)"
        linhas.append([nome(llm), str(total), *(str(c[k]) for k in CLASSES_EVIDENCIA),
                       str(c["pendente"] + c["invalida"]), precisao])
    out += tabela(["LLM", "Citadas", "Correta", "Mal interpretada", "Inexistente",
                   "Não verificável", "Sem classe", "Precisão (corretas/citadas)"], linhas)
    if invalidas:
        out += ["Classes não reconhecidas:", ""] + [f"- {x}" for x in invalidas] + [""]
    return out


def gerar_relatorio(artefato: str, decisoes: Path, evidencias: Path, n_cadeias: int,
                    chave: dict[str, str]) -> tuple[str, Dados]:
    d = Dados(ler_csv(decisoes), n_cadeias)
    modas = {}
    for llm in d.llms + ["humano"]:
        esperadas = 1 if llm == "humano" else n_cadeias
        for etapa in ETAPAS:
            for selo in SELOS:
                modas[(llm, etapa, selo)] = Moda(d.decisoes(llm, etapa, selo), esperadas)
    humano = any(d.linhas("humano", e, s) for e in ETAPAS for s in SELOS)
    out = [f"# Métricas — {artefato}", "",
           f"Gerado por `ferramentas/metricas.py` a partir de `{decisoes.name}`. Todas as medidas "
           "são descritivas: com um único artefato não há base para testes estatísticos.", ""]
    if d.avisos:
        out += ["**Avisos:**", ""] + [f"- {a}" for a in d.avisos] + [""]
    out += secao_modal(d, modas)
    out += secao_empates(d, modas)
    out += secao_comparativa(d, modas, humano)
    out += secao_consistencia(d, modas)
    out += secao_transicao(d)
    out += secao_calibracao(d)
    out += secao_humano(d, modas, humano)
    out += secao_evidencias(evidencias, chave)
    return "\n".join(out).rstrip() + "\n", d


def main(argv=None) -> int:
    console_seguro()
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("artefato")
    ap.add_argument("--runs", type=Path, default=RUNS_PADRAO)
    ap.add_argument("--cadeias", type=int, default=3, help="cadeias esperadas por LLM (padrão 3)")
    ap.add_argument("--chave", type=Path, help="chave de cegamento (JSON de cegar.py) para revelar M1–M3")
    ap.add_argument("--evidencias", type=Path, help="padrão: analise/evidencias.csv")
    args = ap.parse_args(argv)

    analise = args.runs / args.artefato / "analise"
    decisoes = analise / "decisoes.csv"
    if not decisoes.exists():
        print(f"erro: {decisoes} não existe; rode extrair_decisoes.py antes", file=sys.stderr)
        return 2
    texto, d = gerar_relatorio(args.artefato, decisoes, args.evidencias or analise / "evidencias.csv",
                               args.cadeias, ler_chave(args.chave))
    (analise / "metricas.md").write_text(texto, encoding="utf-8")
    print(f"Relatório gravado em {analise / 'metricas.md'}")
    for a in d.avisos:
        print(f"  aviso: {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
