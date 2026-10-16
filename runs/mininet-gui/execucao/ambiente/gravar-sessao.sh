#!/bin/sh
# Grava uma sessão de terminal dentro da VM com tempos (script -t), para a execução futura.
# Uso dentro da VM: sh gravar-sessao.sh <rotulo>   (ex.: teste-minimo, R1)
# Gera em ~/evidencias/: <UTC>-<rotulo>.terminal, <UTC>-<rotulo>.tempo e <UTC>-<rotulo>.sha256.
# Os nomes não terminam em .log porque o .gitignore da raiz do repositório ignora *.log.
# Reprodução: scriptreplay -t <arquivo>.tempo <arquivo>.terminal
set -eu
ROTULO="${1:?informe um rótulo, ex.: teste-minimo}"
DIR="$HOME/evidencias"
mkdir -p "$DIR"
BASE="$DIR/$(date -u +%Y%m%dT%H%M%SZ)-$ROTULO"
# rcfile: carrega o ~/.bashrc normal (aliases/PATH do lançador) e só troca o prompt por um datado.
RC="$DIR/.bashrc-gravacao"
cat > "$RC" <<'EOF'
[ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"
PS1='[\D{%Y-%m-%dT%H:%M:%S%z}] \u@\h:\w\$ '
EOF
echo "Gravando em $BASE.terminal (saia com 'exit')."
script -q -t"$BASE.tempo" -c "bash --rcfile '$RC' -i" "$BASE.terminal"
sha256sum "$BASE.terminal" "$BASE.tempo" > "$BASE.sha256"
cat "$BASE.sha256"
