#!/usr/bin/env python3
"""Extrai as decisões F/R das conversas exportadas e grava analise/decisoes.csv.

Uso:
    python ferramentas/extrair_decisoes.py <artefato> [--runs DIR]

Lê   runs/<artefato>/llm-<provedor>/cadeia-<N>.md
     runs/<artefato>/humano/decisao-analitica.md   (etapa A do humano)
     runs/<artefato>/humano/decisao-final.md       (etapa B do humano)
     runs/<artefato>/referencia/selos-oficiais.md  (coluna "oficial")
Grava runs/<artefato>/analise/decisoes.csv           (esquema do §11 do protocolo)
      runs/<artefato>/analise/por-reivindicacao.csv
      runs/<artefato>/analise/pendencias-extracao.md

CONVENÇÃO DAS TRANSCRIÇÕES (exigida pelo guia de exportação)
-----------------------------------------------------------
1. Bloco de metadados antes da primeira seção, como em runs/MODELO-cadeia.md:
   lista "- chave: valor" com provedor, modelo_exibido, versao, esforco,
   interface, data_hora_A, data_hora_B1, data_hora_B2, anexos_A, anexo_B2,
   metodo_exportacao e desvios. O script usa modelo_exibido (ou "Modelo:"),
   versao, esforco, data_hora_A e data_hora_B2 (ou só "data_hora:") e confere
   provedor com a pasta llm-<provedor> (divergência vira aviso); as demais são
   ignoradas. Negrito, acentos e caixa nas chaves não importam; valores "<...>"
   contam como não preenchidos.
2. Seis seções delimitadas por cabeçalhos de nível 2, exatamente nesta forma
   (texto extra depois do rótulo é permitido, p. ex. "## Resposta A — 10:12"):
       ## Prompt A      ## Resposta A
       ## Prompt B1     ## Resposta B1
       ## Prompt B2     ## Resposta B2
   Uma seção vai do seu cabeçalho até o próximo cabeçalho desta lista. Títulos
   que a própria LLM escreveu ("## B. Selo F", "### ...") não encerram a seção.
3. A decisão da etapa A é o ÚLTIMO bloco JSON com chave "F" e/ou "R" dentro de
   "## Resposta A"; a da etapa B é o último bloco desse tipo dentro de
   "## Resposta B2". A mesma regra vale para as duas etapas. A resposta B1
   (plano) não é lida.
4. Arquivos humanos: não têm seções; usa-se o último bloco JSON do arquivo
   inteiro, no mesmo formato do Prompt A (por_reivindicacao é opcional).

Tolerâncias: cercas de código (``` / ~~~), aspas tipográficas, acentos/caixa/
separadores na decisão ("NAO ATRIBUIR", "não_atribuir"), confiança "80%".
Nada além disso é corrigido. Seção ausente ou duplicada, JSON inválido, selo
ausente ou decisão fora das três categorias NÃO geram linha no CSV: vão para
pendencias-extracao.md e para a saída do terminal.

Colunas calculadas: "oficial" vem de selos-oficiais.md ("F atribuído" ->
Atribuir; não atribuído -> Não atribuir); "coincide" = decisao == oficial;
"mudou" (só etapa B) = decisão B2 != decisão A da mesma cadeia, calculada a
partir das decisões extraídas. O "mudou" declarado pela LLM é só conferido:
divergência vira aviso.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUNS_PADRAO = RAIZ / "runs"

PROVEDORES = ("openai", "anthropic", "google")
CADEIAS_ESPERADAS = (1, 2, 3)
SELOS = ("F", "R")
DECISOES = ("Atribuir", "Não atribuir", "Indeterminado")
CLASSES_REIVINDICACAO = ("reproduzivel", "nao_reproduzivel", "depende_execucao")

COLUNAS_DECISOES = [
    "llm", "modelo", "versao", "esforco", "cadeia", "etapa", "selo", "decisao",
    "confianca", "oficial", "coincide", "mudou", "data_hora", "arquivo_conversa",
]
COLUNAS_REIVINDICACAO = [
    "llm", "cadeia", "etapa", "reivindicacao", "classificacao", "valor_original",
    "arquivo_conversa",
]

# Etapa do CSV -> seção da transcrição que contém a decisão.
SECAO_DA_ETAPA = {"A": "resposta a", "B": "resposta b2"}

RE_CABECALHO = re.compile(r"^##[ \t]+(prompt|resposta)[ \t]+(a|b1|b2)\b.*$")
RE_CERCA = re.compile(r"^[ \t]*(```|~~~).*$", re.MULTILINE)
RE_INICIO_BLOCO = re.compile(r'\{\s*"(?:[FfRr])"\s*:')
TROCAS_ASPAS = str.maketrans({
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    " ": " ",
})


# --------------------------------------------------------------------------- #
# Normalização
# --------------------------------------------------------------------------- #
def sem_acentos(texto: str) -> str:
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def chave_normalizada(texto: str) -> str:
    """'Data/hora B2' -> 'data_hora_b2'; 'Esforço' -> 'esforco'."""
    t = sem_acentos(texto).lower()
    return re.sub(r"[^a-z0-9]+", "_", t).strip("_")


def normalizar_decisao(valor) -> str | None:
    """Devolve uma das três decisões canônicas ou None (nunca adivinha)."""
    if not isinstance(valor, str):
        return None
    t = chave_normalizada(valor)
    return {
        "atribuir": "Atribuir",
        "nao_atribuir": "Não atribuir",
        "indeterminado": "Indeterminado",
    }.get(t)


def normalizar_classe_reivindicacao(valor) -> str | None:
    if not isinstance(valor, str):
        return None
    t = chave_normalizada(valor)
    t = {"depende_de_execucao": "depende_execucao"}.get(t, t)
    return t if t in CLASSES_REIVINDICACAO else None


def normalizar_confianca(valor) -> str | None:
    if isinstance(valor, bool):
        return None
    if isinstance(valor, (int, float)):
        numero = float(valor)
    elif isinstance(valor, str):
        m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*%?\s*", valor)
        if not m:
            return None
        numero = float(m.group(1).replace(",", "."))
    else:
        return None
    if not 0 <= numero <= 100:
        return None
    return str(int(numero)) if numero.is_integer() else str(numero)


def normalizar_booleano(valor) -> bool | None:
    if isinstance(valor, bool):
        return valor
    if isinstance(valor, str):
        t = chave_normalizada(valor)
        if t in ("true", "sim", "yes"):
            return True
        if t in ("false", "nao", "no"):
            return False
    return None


def oficial_para_decisao(atribuido: bool) -> str:
    return "Atribuir" if atribuido else "Não atribuir"


# --------------------------------------------------------------------------- #
# Leitura da transcrição
# --------------------------------------------------------------------------- #
def ler_texto(caminho: Path) -> str:
    return caminho.read_text(encoding="utf-8-sig")


def separar_secoes(texto: str):
    """Devolve (cabecalho, {rotulo: [conteudo, ...]}) segundo a convenção."""
    secoes: dict[str, list[str]] = {}
    cabecalho: list[str] = []
    atual: str | None = None
    buffer: list[str] = []
    for linha in texto.splitlines():
        m = RE_CABECALHO.match(sem_acentos(linha.strip()).lower())
        if m:
            if atual is not None:
                secoes.setdefault(atual, []).append("\n".join(buffer))
            atual = f"{m.group(1)} {m.group(2)}"
            buffer = []
        elif atual is None:
            cabecalho.append(linha)
        else:
            buffer.append(linha)
    if atual is not None:
        secoes.setdefault(atual, []).append("\n".join(buffer))
    return "\n".join(cabecalho), secoes


def ler_metadados(cabecalho: str) -> dict[str, str]:
    """Linhas 'chave: valor' do cabeçalho -> dicionário com chaves canônicas."""
    apelidos = {
        "modelo": "modelo", "model": "modelo", "modelo_exibido": "modelo",
        "versao": "versao", "version": "versao",
        "esforco": "esforco", "nivel_de_raciocinio": "esforco",
        "raciocinio": "esforco", "nivel_de_esforco": "esforco",
        "data_hora": "data_hora", "data": "data_hora",
        "data_hora_a": "data_hora_a", "data_hora_b2": "data_hora_b2",
        "data_hora_b": "data_hora_b2", "interface": "interface", "provedor": "provedor",
    }
    meta: dict[str, str] = {}
    for linha in cabecalho.splitlines():
        limpa = linha.strip().lstrip("-*+ ").replace("**", "").replace("__", "")
        if ":" not in limpa or limpa.startswith("#"):
            continue
        chave, valor = limpa.split(":", 1)
        canonica = apelidos.get(chave_normalizada(chave))
        valor = valor.strip()
        if valor.startswith("<") and valor.endswith(">"):
            continue  # campo do modelo ainda não preenchido
        if canonica and valor and canonica not in meta:
            meta[canonica] = valor
    return meta


def extrair_json(texto: str):
    """Procura o último objeto JSON com chave F/R.

    Devolve (objeto | None, erro | None, n_blocos_validos_distintos).
    """
    limpo = RE_CERCA.sub("", texto.translate(TROCAS_ASPAS))
    decodificador = json.JSONDecoder()
    candidatos = []
    i = 0
    while True:
        i = limpo.find("{", i)
        if i < 0:
            break
        try:
            obj, fim = decodificador.raw_decode(limpo, i)
        except json.JSONDecodeError:
            i += 1
            continue
        if isinstance(obj, dict) and any(str(k).upper() in SELOS for k in obj):
            candidatos.append(obj)
            i = fim
        else:
            i += 1
    if candidatos:
        distintos = {json.dumps(c, sort_keys=True, ensure_ascii=False) for c in candidatos}
        return candidatos[-1], None, len(distintos)
    inicios = list(RE_INICIO_BLOCO.finditer(limpo))
    if not inicios:
        return None, "bloco JSON com chaves F/R ausente", 0
    pos = inicios[-1].start()
    try:
        decodificador.raw_decode(limpo, pos)
        erro = "bloco JSON sem formato de objeto válido"
    except json.JSONDecodeError as exc:
        linha = limpo.count("\n", 0, pos) + exc.lineno
        erro = f"JSON inválido ({exc.msg}, linha {linha} da seção)"
    return None, erro, 0


def chaves_canonicas(d: dict) -> dict:
    return {chave_normalizada(str(k)): v for k, v in d.items()}


def obter_selo(obj: dict, selo: str):
    for k, v in obj.items():
        if str(k).strip().upper() == selo:
            return v
    return None


def ler_selos_oficiais(caminho: Path) -> dict[str, str]:
    """Lê 'F atribuído' / 'R não atribuído' de referencia/selos-oficiais.md."""
    if not caminho.exists():
        return {}
    texto = sem_acentos(ler_texto(caminho)).lower()
    oficiais: dict[str, str] = {}
    for m in re.finditer(r"(?<![a-z0-9])([fr])\s+(nao\s+)?atribuido", texto):
        selo = m.group(1).upper()
        valor = oficial_para_decisao(m.group(2) is None)
        if oficiais.get(selo, valor) != valor:
            oficiais[selo] = "CONFLITO"
        else:
            oficiais[selo] = valor
    return oficiais


# --------------------------------------------------------------------------- #
# Extração
# --------------------------------------------------------------------------- #
class Registro:
    """Acumula linhas, pendências (bloqueiam uma decisão) e avisos."""

    def __init__(self, raiz_relativa: Path):
        self.raiz_relativa = raiz_relativa
        self.linhas: list[dict] = []
        self.reivindicacoes: list[dict] = []
        self.pendencias: list[str] = []
        self.avisos: list[str] = []

    def rel(self, caminho: Path) -> str:
        try:
            return caminho.resolve().relative_to(self.raiz_relativa).as_posix()
        except ValueError:
            return caminho.as_posix()


def decisoes_do_bloco(obj: dict, contexto: str, reg: Registro):
    """Valida o JSON e devolve {selo: dados} só com o que foi lido de fato."""
    saida = {}
    mudou_raiz = obter_selo_raiz_mudou(obj)
    for selo in SELOS:
        bruto = obter_selo(obj, selo)
        if not isinstance(bruto, dict):
            reg.pendencias.append(f"{contexto}, selo {selo}: objeto do selo ausente no JSON")
            continue
        campos = chaves_canonicas(bruto)
        decisao = normalizar_decisao(campos.get("decisao"))
        if decisao is None:
            reg.pendencias.append(
                f"{contexto}, selo {selo}: decisão ausente ou fora das categorias "
                f"(valor lido: {json.dumps(campos.get('decisao'), ensure_ascii=False)})")
            continue
        confianca = normalizar_confianca(campos.get("confianca"))
        if confianca is None:
            reg.pendencias.append(
                f"{contexto}, selo {selo}: confiança ausente ou fora de 0-100 "
                f"(valor lido: {json.dumps(campos.get('confianca'), ensure_ascii=False)}); "
                "decisão registrada com confiança vazia")
        evidencias = campos.get("evidencias")
        if not isinstance(evidencias, list):
            evidencias = []
        mudou = normalizar_booleano(campos.get("mudou"))
        if mudou is None and isinstance(mudou_raiz, dict):
            mudou = normalizar_booleano(obter_selo(mudou_raiz, selo))
        saida[selo] = {
            "decisao": decisao, "confianca": confianca or "",
            "evidencias": evidencias, "mudou_declarado": mudou,
            "por_reivindicacao": campos.get("por_reivindicacao"),
        }
    return saida


def obter_selo_raiz_mudou(obj: dict):
    for k, v in obj.items():
        if chave_normalizada(str(k)) == "mudou":
            return v
    return None


def ler_blocos_cadeia(caminho: Path, contexto: str, reg: Registro):
    """Devolve (metadados, {etapa: {selo: dados}}, {etapa: texto_da_resposta})."""
    cabecalho, secoes = separar_secoes(ler_texto(caminho))
    meta = ler_metadados(cabecalho)
    por_etapa, textos = {}, {}
    for etapa, rotulo in SECAO_DA_ETAPA.items():
        ctx = f"{contexto}, etapa {etapa} (## {rotulo.title()})"
        partes = secoes.get(rotulo, [])
        if not partes:
            reg.pendencias.append(f"{ctx}: seção ausente")
            continue
        if len(partes) > 1:
            reg.pendencias.append(f"{ctx}: seção duplicada ({len(partes)} vezes); resolver à mão")
            continue
        obj, erro, n_distintos = extrair_json(partes[0])
        if obj is None:
            reg.pendencias.append(f"{ctx}: {erro}")
            continue
        if n_distintos > 1:
            reg.avisos.append(f"{ctx}: {n_distintos} blocos JSON distintos; usado o último")
        por_etapa[etapa] = decisoes_do_bloco(obj, ctx, reg)
        textos[etapa] = partes[0]
    return meta, por_etapa, textos


def ler_bloco_humano(caminho: Path, contexto: str, reg: Registro):
    texto = ler_texto(caminho)
    cabecalho, _ = separar_secoes(texto)
    obj, erro, n_distintos = extrair_json(texto)
    if obj is None:
        reg.pendencias.append(f"{contexto}: {erro}")
        return ler_metadados(cabecalho), None
    if n_distintos > 1:
        reg.avisos.append(f"{contexto}: {n_distintos} blocos JSON distintos; usado o último")
    return ler_metadados(cabecalho), decisoes_do_bloco(obj, contexto, reg)


def adicionar_linhas(reg, llm, cadeia, meta, por_etapa, oficiais, arquivos):
    for etapa in ("A", "B"):
        for selo in SELOS:
            dados = por_etapa.get(etapa, {}).get(selo)
            if not dados:
                continue
            oficial = oficiais.get(selo, "")
            if oficial == "CONFLITO":
                oficial = ""
            mudou = ""
            if etapa == "B":
                anterior = por_etapa.get("A", {}).get(selo)
                if anterior:
                    mudou = "sim" if anterior["decisao"] != dados["decisao"] else "nao"
                declarado = dados["mudou_declarado"]
                if declarado is not None and mudou and declarado != (mudou == "sim"):
                    reg.avisos.append(
                        f"{arquivos[etapa]}, selo {selo}: \"mudou\" declarado = "
                        f"{str(declarado).lower()}, mas A={anterior['decisao']} e "
                        f"B={dados['decisao']} (CSV usa o valor calculado)")
            data_hora = meta.get("data_hora_a" if etapa == "A" else "data_hora_b2") \
                or meta.get("data_hora", "")
            reg.linhas.append({
                "llm": llm, "modelo": meta.get("modelo", ""),
                "versao": meta.get("versao", ""), "esforco": meta.get("esforco", ""),
                "cadeia": str(cadeia), "etapa": etapa, "selo": selo,
                "decisao": dados["decisao"], "confianca": dados["confianca"],
                "oficial": oficial,
                "coincide": ("sim" if dados["decisao"] == oficial else "nao") if oficial else "",
                "mudou": mudou, "data_hora": data_hora,
                "arquivo_conversa": arquivos[etapa],
            })
            if selo == "R":
                adicionar_reivindicacoes(reg, llm, cadeia, etapa, dados, arquivos[etapa])


def adicionar_reivindicacoes(reg, llm, cadeia, etapa, dados, arquivo):
    por_reiv = dados.get("por_reivindicacao")
    if por_reiv is None:
        if llm != "humano":
            reg.avisos.append(f"{arquivo}, etapa {etapa}: \"por_reivindicacao\" ausente em R")
        return
    if not isinstance(por_reiv, dict):
        reg.pendencias.append(f"{arquivo}, etapa {etapa}: \"por_reivindicacao\" não é objeto")
        return
    for chave, valor in por_reiv.items():
        classe = normalizar_classe_reivindicacao(valor)
        if classe is None:
            reg.pendencias.append(
                f"{arquivo}, etapa {etapa}, {chave}: classificação fora das categorias "
                f"(valor lido: {json.dumps(valor, ensure_ascii=False)})")
        reg.reivindicacoes.append({
            "llm": llm, "cadeia": str(cadeia), "etapa": etapa,
            "reivindicacao": str(chave).strip().upper(), "classificacao": classe or "",
            "valor_original": valor if isinstance(valor, str) else json.dumps(valor, ensure_ascii=False),
            "arquivo_conversa": arquivo,
        })


def caminho_cadeia(dir_artefato: Path, provedor: str, cadeia: int) -> Path:
    return dir_artefato / f"llm-{provedor}" / f"cadeia-{cadeia}.md"


def listar_cadeias(dir_artefato: Path, reg: Registro):
    """Cadeias esperadas (3x3) + extras encontradas; ausentes viram pendência."""
    encontradas = []
    for caminho in sorted(dir_artefato.glob("llm-*/cadeia-*.md")):
        m = re.fullmatch(r"cadeia-(\d+)\.md", caminho.name)
        provedor = caminho.parent.name[len("llm-"):]
        if not m:
            reg.avisos.append(f"{reg.rel(caminho)}: nome fora do padrão cadeia-<N>.md; ignorado")
            continue
        encontradas.append((provedor, int(m.group(1)), caminho))
    chaves = {(p, n) for p, n, _ in encontradas}
    for provedor in PROVEDORES:
        for n in CADEIAS_ESPERADAS:
            if (provedor, n) not in chaves:
                reg.pendencias.append(
                    f"{reg.rel(caminho_cadeia(dir_artefato, provedor, n))}: cadeia ausente")
    ordem = {p: i for i, p in enumerate(PROVEDORES)}
    return sorted(encontradas, key=lambda t: (ordem.get(t[0], 99), t[0], t[1]))


def extrair_artefato(dir_artefato: Path, raiz_relativa: Path | None = None) -> Registro:
    reg = Registro((raiz_relativa or RAIZ).resolve())
    caminho_oficial = dir_artefato / "referencia" / "selos-oficiais.md"
    oficiais = ler_selos_oficiais(caminho_oficial)
    for selo in SELOS:
        if oficiais.get(selo) in (None, "CONFLITO"):
            motivo = "registros conflitantes" if oficiais.get(selo) else "não encontrado"
            reg.pendencias.append(
                f"{reg.rel(caminho_oficial)}: selo oficial {selo} {motivo}; coluna \"oficial\" vazia")

    for provedor, cadeia, caminho in listar_cadeias(dir_artefato, reg):
        rel = reg.rel(caminho)
        meta, por_etapa, _ = ler_blocos_cadeia(caminho, rel, reg)
        declarado = chave_normalizada(meta.get("provedor", ""))
        if declarado and declarado != provedor:
            reg.avisos.append(f"{rel}: cabeçalho diz provedor \"{meta['provedor']}\", "
                              f"mas a pasta é llm-{provedor} (CSV usa a pasta)")
        adicionar_linhas(reg, provedor, cadeia, meta, por_etapa, oficiais, {"A": rel, "B": rel})

    # Humano: um arquivo por etapa; metadados de cada arquivo valem para a sua etapa.
    por_etapa, meta_humano, arquivos = {}, {}, {}
    for etapa, nome in (("A", "decisao-analitica.md"), ("B", "decisao-final.md")):
        caminho = dir_artefato / "humano" / nome
        arquivos[etapa] = reg.rel(caminho)
        if not caminho.exists():
            reg.pendencias.append(f"{arquivos[etapa]}: decisão humana da etapa {etapa} ausente")
            continue
        meta, blocos = ler_bloco_humano(caminho, f"{arquivos[etapa]} (humano, etapa {etapa})", reg)
        meta_humano["data_hora_a" if etapa == "A" else "data_hora_b2"] = meta.get("data_hora", "")
        if blocos:
            por_etapa[etapa] = blocos
    adicionar_linhas(reg, "humano", 1, meta_humano, por_etapa, oficiais, arquivos)
    return reg


# --------------------------------------------------------------------------- #
# Saída
# --------------------------------------------------------------------------- #
def gravar_csv(caminho: Path, colunas, linhas):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(linhas)


def texto_pendencias(artefato: str, reg: Registro) -> str:
    partes = [
        f"# Pendências de extração — {artefato}",
        "",
        "Gerado por `ferramentas/extrair_decisoes.py`. Uma pendência significa que "
        "a decisão correspondente **não** foi gravada em `decisoes.csv` (ou foi gravada "
        "incompleta, quando indicado). Corrija a transcrição seguindo a convenção do "
        "script — sem alterar o conteúdo das respostas — e rode de novo.",
        "",
        f"## Pendências ({len(reg.pendencias)})",
        "",
    ]
    partes += [f"- {p}" for p in reg.pendencias] or ["Nenhuma."]
    partes += ["", f"## Avisos ({len(reg.avisos)})", ""]
    partes += [f"- {a}" for a in reg.avisos] or ["Nenhum."]
    return "\n".join(partes) + "\n"


def console_seguro():
    """Evita UnicodeEncodeError em consoles cp1252 do Windows."""
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(errors="replace")


def main(argv=None) -> int:
    console_seguro()
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("artefato", help="nome da pasta em runs/, p. ex. foremost-ng")
    ap.add_argument("--runs", type=Path, default=RUNS_PADRAO, help="pasta runs/ (padrão: a do repositório)")
    args = ap.parse_args(argv)

    dir_artefato = args.runs / args.artefato
    if not dir_artefato.is_dir():
        print(f"erro: pasta do artefato não encontrada: {dir_artefato}", file=sys.stderr)
        return 2
    reg = extrair_artefato(dir_artefato, raiz_relativa=args.runs.resolve().parent)
    analise = dir_artefato / "analise"
    gravar_csv(analise / "decisoes.csv", COLUNAS_DECISOES, reg.linhas)
    gravar_csv(analise / "por-reivindicacao.csv", COLUNAS_REIVINDICACAO, reg.reivindicacoes)
    (analise / "pendencias-extracao.md").write_text(texto_pendencias(args.artefato, reg), encoding="utf-8")

    print(f"{len(reg.linhas)} decisões gravadas em {analise / 'decisoes.csv'}")
    print(f"{len(reg.reivindicacoes)} classificações por reivindicação em {analise / 'por-reivindicacao.csv'}")
    print(f"Pendências: {len(reg.pendencias)}  Avisos: {len(reg.avisos)}  "
          f"(detalhes em {analise / 'pendencias-extracao.md'})")
    for p in reg.pendencias:
        print(f"  PENDENTE: {p}")
    for a in reg.avisos:
        print(f"  aviso: {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
