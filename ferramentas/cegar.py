#!/usr/bin/env python3
"""Prepara a verificação cega das evidências (§7 do protocolo).

Uso:
    python ferramentas/cegar.py <artefato> [--runs DIR] [--saida DIR] [--chave ARQ]
                                [--evidencias ARQ] [--remover NOME ...] [--semente N] [--forcar]

1. Sorteia um mapeamento provedor -> M1/M2/M3 (random.SystemRandom, salvo --semente).
2. Copia runs/<artefato>/llm-<provedor>/cadeia-N.md para <saida>/M<k>/cadeia-N.md
   (padrão de <saida>: runs/<artefato>/verificacao-cega/), substituindo por
   [REMOVIDO] os nomes de modelo/provedor (GPT*, ChatGPT, OpenAI, Claude,
   Anthropic, Gemini, Google, Bard, DeepMind, Opus, Sonnet, Haiku, Codex, mais
   --remover) e os valores de provedor/modelo/versão/esforço/interface do
   cabeçalho (só antes da primeira seção "## Prompt/Resposta").
3. Grava a chave (JSON) FORA do Git. Padrão: ~/t8-leas-chaves/<artefato>-chave.json.
   Um caminho dentro do repositório só é aceito se `git check-ignore` confirmar
   que ele é ignorado. Chave existente não é sobrescrita sem --forcar.
4. Gera evidencias.csv (padrão: runs/<artefato>/analise/evidencias.csv) com as
   evidências citadas nos JSON das respostas A e B2, a afirmação (linha do texto
   da resposta que cita a evidência, quando encontrada) e "classe" vazia.

Depois da classificação cega, revele os provedores só no cálculo:
    python ferramentas/metricas.py <artefato> --chave <arquivo da chave>
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extrair_decisoes import (  # noqa: E402
    PROVEDORES, RAIZ, RE_CABECALHO, RUNS_PADRAO, SELOS, Registro, chave_normalizada,
    console_seguro, ler_blocos_cadeia, listar_cadeias, sem_acentos,
)

COLUNAS_EVIDENCIAS = ["id_cego", "llm", "cadeia", "etapa", "selo", "evidencia_citada",
                      "afirmacao", "classe", "nota_verificador"]
NOMES_OBVIOS = ["chat[ -]?gpt", "gpt", "openai", "claude", "anthropic", "gemini", "google",
                "bard", "deepmind", "opus", "sonnet", "haiku", "codex"]
CAMPOS_CABECALHO = ("provedor", "modelo", "modelo_exibido", "model", "versao", "version",
                    "esforco", "nivel_de_raciocinio", "raciocinio", "nivel_de_esforco",
                    "interface")
SUBSTITUTO = "[REMOVIDO]"


def compilar_remocao(extras: list[str]) -> re.Pattern:
    """Nome + variantes coladas: 'GPT-5.1', 'gpt4o', 'Claude.ai', 'gemini-cli'.

    O nome não pode ser seguido de letra ('geminiano' fica intacto); dígitos e
    sufixos com '-', '_' ou '.' fazem parte do nome removido.
    """
    nomes = NOMES_OBVIOS + [re.escape(e) for e in extras if e.strip()]
    return re.compile(r"\b(?:" + "|".join(nomes) + r")(?![^\W\d_])(?:\d\w*)?(?:[-_.]\w+)*",
                      re.IGNORECASE)


def cegar_texto(texto: str, padrao: re.Pattern, literais: list[str],
                cabecalho: bool = False) -> tuple[str, int]:
    """Remove nomes. Com cabecalho=True, também zera Modelo/Versão/Esforço/Interface
    nas linhas anteriores à primeira seção "## Prompt/Resposta"."""
    total = 0
    linhas = []
    em_cabecalho = cabecalho
    for linha in texto.splitlines(keepends=True):
        if em_cabecalho and RE_CABECALHO.match(sem_acentos(linha.strip()).lower()):
            em_cabecalho = False
        limpa = linha.strip().lstrip("-*+ ").replace("**", "").replace("__", "")
        if em_cabecalho and ":" in limpa and not limpa.startswith("#") \
                and chave_normalizada(limpa.split(":", 1)[0]) in CAMPOS_CABECALHO:
            rotulo = linha.split(":", 1)[0]
            fim = "\n" if linha.endswith("\n") else ""
            linha = f"{rotulo}: {SUBSTITUTO}{fim}"
            total += 1
        linhas.append(linha)
    texto = "".join(linhas)
    for literal in sorted({l for l in literais if len(l) >= 3}, key=len, reverse=True):
        texto, n = re.subn(r"(?<!\w)" + re.escape(literal) + r"(?!\w)", SUBSTITUTO, texto,
                           flags=re.IGNORECASE)
        total += n
    texto, n = padrao.subn(SUBSTITUTO, texto)
    return texto, total + n


def dentro(caminho: Path, pasta: Path) -> bool:
    try:
        caminho.resolve().relative_to(pasta.resolve())
        return True
    except ValueError:
        return False


def chave_ignorada_pelo_git(caminho: Path) -> bool:
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), "check-ignore", "-q", str(caminho.resolve())],
                           capture_output=True)
    except OSError:
        return False
    return r.returncode == 0


def afirmacao_para(evidencia: str, texto: str) -> str:
    """Primeira linha da resposta (fora do bloco JSON) que contém a evidência."""
    alvo = evidencia.strip().strip("[]").strip()
    if len(alvo) < 3:
        return ""
    for linha in texto.splitlines():
        s = linha.strip()
        if alvo in s and not s.startswith(("{", "\"", "[\"", "}")) and "\"evidencias\"" not in s:
            return s[:400]
    return ""


def main(argv=None) -> int:
    console_seguro()
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("artefato")
    ap.add_argument("--runs", type=Path, default=RUNS_PADRAO)
    ap.add_argument("--saida", type=Path, help="padrão: runs/<artefato>/verificacao-cega")
    ap.add_argument("--chave", type=Path, help="padrão: ~/t8-leas-chaves/<artefato>-chave.json")
    ap.add_argument("--evidencias", type=Path, help="padrão: runs/<artefato>/analise/evidencias.csv")
    ap.add_argument("--remover", nargs="*", default=[], help="nomes extras a remover (p. ex. o3)")
    ap.add_argument("--semente", type=int, help="semente fixa (só para testes)")
    ap.add_argument("--forcar", action="store_true", help="sobrescreve saída, chave e evidencias.csv")
    args = ap.parse_args(argv)

    dir_artefato = args.runs / args.artefato
    if not dir_artefato.is_dir():
        print(f"erro: pasta do artefato não encontrada: {dir_artefato}", file=sys.stderr)
        return 2
    saida = args.saida or dir_artefato / "verificacao-cega"
    chave = args.chave or Path.home() / "t8-leas-chaves" / f"{args.artefato}-chave.json"
    evid = args.evidencias or dir_artefato / "analise" / "evidencias.csv"

    if dentro(chave, saida):
        print("erro: a chave não pode ficar dentro da pasta cega", file=sys.stderr)
        return 2
    if dentro(chave, RAIZ) and not chave_ignorada_pelo_git(chave):
        print(f"erro: {chave} está no repositório e não é ignorado pelo Git; "
              "escolha um caminho fora do repositório", file=sys.stderr)
        return 2
    bloqueios = [p for p in (chave, evid) if p.exists()]
    if saida.exists() and any(saida.iterdir()):
        bloqueios.append(saida)
    if bloqueios and not args.forcar:
        for p in bloqueios:
            print(f"erro: {p} já existe (use --forcar para sobrescrever)", file=sys.stderr)
        return 2

    reg = Registro(args.runs.resolve().parent)
    cadeias = listar_cadeias(dir_artefato, reg)
    provedores = [p for p in PROVEDORES if any(c[0] == p for c in cadeias)]
    provedores += sorted({c[0] for c in cadeias} - set(provedores))
    rotulos = [f"M{i}" for i in range(1, len(provedores) + 1)]
    sorteio = random.Random(args.semente) if args.semente is not None else random.SystemRandom()
    embaralhados = provedores[:]
    sorteio.shuffle(embaralhados)
    mapa = dict(zip(rotulos, embaralhados))
    rotulo_de = {p: m for m, p in mapa.items()}

    padrao = compilar_remocao(args.remover)
    linhas_evid, remocoes = [], 0
    for provedor, cadeia, caminho in cadeias:
        rotulo = rotulo_de[provedor]
        meta, por_etapa, textos = ler_blocos_cadeia(caminho, reg.rel(caminho), reg)
        literais = [meta.get("modelo", ""), meta.get("versao", "")]
        texto, n = cegar_texto(caminho.read_text(encoding="utf-8-sig"), padrao, literais,
                               cabecalho=True)
        remocoes += n
        destino = saida / rotulo / caminho.name
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        for etapa in ("A", "B"):
            resposta = textos.get(etapa, "")
            for selo in SELOS:
                dados = por_etapa.get(etapa, {}).get(selo)
                if not dados:
                    continue
                for i, ev in enumerate(dados["evidencias"], start=1):
                    bruto = ev if isinstance(ev, str) else json.dumps(ev, ensure_ascii=False)
                    citada, _ = cegar_texto(bruto, padrao, literais)
                    afirmacao, _ = cegar_texto(afirmacao_para(bruto, resposta), padrao, literais)
                    linhas_evid.append({
                        "id_cego": f"{rotulo}-c{cadeia}-{etapa}-{selo}-{i:02d}",
                        "llm": rotulo, "cadeia": str(cadeia), "etapa": etapa, "selo": selo,
                        "evidencia_citada": citada, "afirmacao": afirmacao,
                        "classe": "", "nota_verificador": "",
                    })

    ordem = {m: i for i, m in enumerate(rotulos)}
    linhas_evid.sort(key=lambda l: (ordem[l["llm"]], int(l["cadeia"]), l["etapa"], l["selo"], l["id_cego"]))
    evid.parent.mkdir(parents=True, exist_ok=True)
    with evid.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS_EVIDENCIAS)
        escritor.writeheader()
        escritor.writerows(linhas_evid)

    chave.parent.mkdir(parents=True, exist_ok=True)
    chave.write_text(json.dumps({
        "artefato": args.artefato,
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mapeamento": mapa,
        "aviso": "Não versionar. Revelar só depois de classificar evidencias.csv.",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"{len(cadeias)} cadeias copiadas para {saida} ({remocoes} trechos removidos)")
    print(f"{len(linhas_evid)} evidências em {evid} (coluna classe vazia)")
    print(f"Chave gravada em {chave} — mantenha fora do Git e longe do verificador")
    for p in reg.pendencias:
        print(f"  PENDENTE: {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
