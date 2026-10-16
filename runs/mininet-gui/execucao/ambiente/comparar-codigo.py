"""Compara o manifesto SHA-256 do código da VM com árvores de referência.

Uso no host (rodar com python -I):
  python -I comparar-codigo.py <identificacao-vm.txt> <rotulo>=<pasta> [<rotulo>=<pasta> ...]
Prefixo "lf:" no rótulo (ex.: lf:pacote=<pasta>) converte CRLF em LF na referência antes do hash,
para árvores extraídas no Windows, como o pacote/artefato.zip.

O manifesto é a seção "### Manifesto SHA-256" gerada por identificar-vm.sh.
Cada pasta de referência é uma árvore extraída (git archive ou artefato.zip).
São ignorados os mesmos caminhos excluídos na VM (.git, node_modules, venv, dist, __pycache__, *.pyc).
"""
import hashlib
import os
import re
import sys

IGNORAR_DIRS = {".git", "node_modules", "venv", ".venv", "dist", "__pycache__"}


def manifesto_vm(caminho):
    linhas = open(caminho, encoding="utf-8", errors="replace").read().splitlines()
    dentro, saida = False, {}
    for linha in linhas:
        if linha.startswith("### Manifesto SHA-256"):
            dentro = True
            continue
        if dentro:
            m = re.match(r"^([0-9a-f]{64})\s+\*?\./(.+)$", linha)
            if m:
                saida[m.group(2)] = m.group(1)
    return saida


def manifesto_pasta(raiz, lf=False):
    saida = {}
    for pasta, dirs, arquivos in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in IGNORAR_DIRS]
        for nome in arquivos:
            if nome.endswith(".pyc"):
                continue
            p = os.path.join(pasta, nome)
            rel = os.path.relpath(p, raiz).replace(os.sep, "/")
            with open(p, "rb") as f:
                dados = f.read()
            if lf and b"\0" not in dados:  # só texto; binários ficam intactos
                dados = dados.replace(b"\r\n", b"\n")
            saida[rel] = hashlib.sha256(dados).hexdigest()
    return saida


def main():
    vm = manifesto_vm(sys.argv[1])
    print(f"VM: {len(vm)} arquivos no manifesto")
    for arg in sys.argv[2:]:
        rotulo, pasta = arg.split("=", 1)
        lf = rotulo.startswith("lf:")
        ref = manifesto_pasta(pasta, lf)
        iguais = sorted(k for k in vm if k in ref and vm[k] == ref[k])
        difere = sorted(k for k in vm if k in ref and vm[k] != ref[k])
        so_vm = sorted(k for k in vm if k not in ref)
        so_ref = sorted(k for k in ref if k not in vm)
        print(f"\n## VM x {rotulo} ({len(ref)} arquivos)")
        print(f"iguais={len(iguais)} diferentes={len(difere)} so_na_vm={len(so_vm)} so_na_referencia={len(so_ref)}")
        for titulo, lista in (("diferentes", difere), ("só na VM", so_vm), ("só na referência", so_ref)):
            for k in lista:
                print(f"  {titulo}: {k}")


if __name__ == "__main__":
    main()
