#!/usr/bin/env bash
# gravar-sessao.sh — registro da execução de referência (T8/LEAS, Foremost-NG).
#
# Uso, dentro do contêiner:
#   gravar-sessao.sh sessao DIR [COMANDO]
#       Grava a sessão de terminal com `script` (util-linux):
#         DIR/terminal.txt   saída bruta do terminal (cabeçalho com hora UTC)
#         DIR/tempo.txt      tempos para `scriptreplay -T DIR/tempo.txt DIR/terminal.txt`
#         DIR/historico.txt  histórico do bash com carimbo de hora
#       Sem COMANDO, abre um bash interativo cujo prompt mostra a hora; com
#       COMANDO, executa-o (útil para testes não interativos).
#       Dentro da sessão, REG_DIR=DIR e a função `passo` ficam disponíveis.
#
#   gravar-sessao.sh passo ID [-w DIR_OBSERVADO]... -- COMANDO [ARGS...]
#       Executa COMANDO no diretório atual e registra, em $REG_DIR (padrão: .):
#         passos.tsv              uma linha por passo: id, início e fim (UTC),
#                                 duração (s), código de saída, diretório, comando
#         passos/ID.saida.txt     stdout+stderr do comando (também vai à tela)
#         passos/ID.sha256        sha256sum dos arquivos criados/alterados
#                                 durante o passo nos diretórios observados
#                                 (padrão: o diretório atual)
#       O código de saída de `passo` é o do COMANDO.
#
# Os nomes não terminam em .log porque o .gitignore da raiz ignora *.log.

set -u

agora() { date -u +%Y-%m-%dT%H:%M:%S.%3NZ; }
segundos() { date +%s.%N; }

uso() { sed -n '2,25p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }

cmd_sessao() {
    [ $# -ge 1 ] || uso
    local dir; dir=$(mkdir -p "$1" && cd "$1" && pwd) || exit 1
    shift
    local eu; eu=$(readlink -f "$0")
    local rc="$dir/.bashrc-sessao"
    cat > "$rc" <<EOF
[ -f ~/.bashrc ] && . ~/.bashrc
export REG_DIR='$dir'
export HISTFILE="\$REG_DIR/historico.txt" HISTTIMEFORMAT='%Y-%m-%dT%H:%M:%S%z  '
shopt -s histappend
PROMPT_COMMAND='history -a'
PS1='[\D{%Y-%m-%dT%H:%M:%S%z}] \u@\h:\w (\$?)\\$ '
passo() { '$eu' passo "\$@"; }
EOF
    {
        echo "### sessao iniciada $(agora)"
        echo "### host=$(hostname) $(uname -srm)"
        [ -r /etc/os-release ] && . /etc/os-release && echo "### so=$PRETTY_NAME"
        echo "### usuario=$(id -un) diretorio=$PWD"
    } > "$dir/cabecalho.txt"
    local alvo
    if [ $# -gt 0 ]; then
        alvo="bash --rcfile '$rc' -i -c $(printf '%q' "$*")"
    else
        alvo="bash --rcfile '$rc' -i"
    fi
    SHELL=/bin/bash REG_DIR="$dir" script -q -f -a -E never -T "$dir/tempo.txt" \
        -c "cat '$dir/cabecalho.txt'; $alvo" "$dir/terminal.txt"
    local st=$?
    echo "### sessao encerrada $(agora) codigo=$st" | tee -a "$dir/terminal.txt"
    return $st
}

cmd_passo() {
    [ $# -ge 1 ] || uso
    local id=$1; shift
    local -a observados=()
    while [ $# -gt 0 ]; do
        case $1 in
            -w) observados+=("$(cd "$2" && pwd)") || exit 1; shift 2 ;;
            --) shift; break ;;
            *) break ;;
        esac
    done
    [ $# -ge 1 ] || uso
    [ ${#observados[@]} -gt 0 ] || observados=("$PWD")

    local reg; reg=$(mkdir -p "${REG_DIR:-.}/passos" && cd "${REG_DIR:-.}" && pwd) || exit 1
    local tsv="$reg/passos.tsv"
    [ -s "$tsv" ] || printf 'id\tinicio_utc\tfim_utc\tduracao_s\tcodigo_saida\tdiretorio\tcomando\n' > "$tsv"

    local comando; comando=$(printf '%q ' "$@"); comando=${comando% }
    local marca; marca=$(mktemp "$reg/passos/.marca-XXXXXX")
    local ini_h ini_s fim_h fim_s st
    ini_h=$(agora); ini_s=$(segundos)
    echo ">>> passo $id | $ini_h | $PWD | $comando"
    "$@" 2>&1 | tee "$reg/passos/$id.saida.txt"
    st=${PIPESTATUS[0]}
    fim_s=$(segundos); fim_h=$(agora)
    local dur; dur=$(awk -v a="$ini_s" -v b="$fim_s" 'BEGIN{printf "%.3f", b-a}')

    # Arquivos criados ou alterados durante o passo (ctime posterior à marca;
    # ctime não é preservado por cp -p/unzip/tar, ao contrário do mtime).
    : > "$reg/passos/$id.sha256"
    local d
    for d in "${observados[@]}"; do
        find "$d" -path "$reg" -prune -o -type f -cnewer "$marca" -print0 2>/dev/null \
            | sort -z | xargs -0 -r sha256sum >> "$reg/passos/$id.sha256"
    done
    rm -f "$marca"
    local n; n=$(wc -l < "$reg/passos/$id.sha256")

    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$id" "$ini_h" "$fim_h" "$dur" "$st" "$PWD" "$comando" >> "$tsv"
    echo "<<< passo $id | codigo=$st | ${dur}s | arquivos novos/alterados=$n | $fim_h"
    return "$st"
}

case ${1:-} in
    sessao) shift; cmd_sessao "$@" ;;
    passo)  shift; cmd_passo "$@" ;;
    *) uso ;;
esac
