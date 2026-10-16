"""Gera a apresentação em arquivo único (artefato.txt) a partir de pacote/artefato.zip.

Motivo: o app do Claude não lista ZIP entre os anexos aceitos e o Gemini lê no
máximo dez arquivos por ZIP. Pelo §4.6 do protocolo, se uma interface não lê o
ZIP, as três recebem a mesma apresentação extraída. Este script produz essa
apresentação de forma determinística:

- cabeçalho com origem (hash do ZIP, comentário com o SHA) e índice de todas as
  entradas, com tamanho e SHA-256;
- cada arquivo de texto na íntegra, com o número da linha original, para que as
  evidências possam ser citadas como caminho:linha;
- arquivos binários (imagens, DLLs, .gz, .ico) apenas listados no índice.

Uso: python ferramentas/achatar_artefato.py runs/<artefato>/pacote
"""
import hashlib
import sys
import zipfile
from pathlib import Path

BINARIO = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".dll", ".gz", ".zip", ".pdf", ".exe", ".so"}


def eh_texto(nome, dados):
    if Path(nome).suffix.lower() in BINARIO or b"\x00" in dados:
        return False
    try:
        dados.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def main(pasta):
    pasta = Path(pasta)
    zpath = pasta / "artefato.zip"
    zbytes = zpath.read_bytes()
    z = zipfile.ZipFile(zpath)
    entradas = [i for i in z.infolist() if not i.is_dir()]
    # remove o prefixo de diretório gerado pelo git archive (ex.: foremost-ng-bb812a22/)
    prefixo = entradas[0].filename.split("/", 1)[0] + "/"
    comentario = z.comment.decode("utf-8", "replace").strip()

    linhas = [
        "ARTEFATO EM ARQUIVO ÚNICO",
        f"Origem: artefato.zip (SHA-256 {hashlib.sha256(zbytes).hexdigest()}), gerado por git archive.",
        f"Commit (comentário do ZIP): {comentario}",
        f"Diretório raiz no ZIP: {prefixo}",
        "Conteúdo: todos os arquivos do commit. Arquivos de texto aparecem na íntegra, com o número",
        "da linha original à esquerda (LINHA| texto). Arquivos binários aparecem só no índice.",
        "Para citar evidência use caminho:linha, por exemplo README.md:12.",
        "",
        "ÍNDICE (caminho | bytes | tipo | sha256)",
    ]
    corpo = []
    for i in entradas:
        dados = z.read(i)
        caminho = i.filename[len(prefixo):] if i.filename.startswith(prefixo) else i.filename
        texto = eh_texto(caminho, dados)
        h = hashlib.sha256(dados).hexdigest()
        linhas.append(f"{caminho} | {len(dados)} | {'texto' if texto else 'binário (omitido)'} | {h}")
        if not texto:
            continue
        conteudo = dados.decode("utf-8").replace("\r\n", "\n").split("\n")
        if conteudo and conteudo[-1] == "":
            conteudo.pop()
        largura = len(str(len(conteudo)))
        corpo.append("")
        corpo.append(f"===== INÍCIO DO ARQUIVO: {caminho} ({len(conteudo)} linhas) =====")
        corpo.extend(f"{n:>{largura}}| {t}" for n, t in enumerate(conteudo, 1))
        corpo.append(f"===== FIM DO ARQUIVO: {caminho} =====")

    saida = pasta / "artefato.txt"
    saida.write_text("\n".join(linhas + corpo) + "\n", encoding="utf-8", newline="\n")
    print(saida, hashlib.sha256(saida.read_bytes()).hexdigest(), saida.stat().st_size)


if __name__ == "__main__":
    main(sys.argv[1])
