#!/bin/bash
# uso: vmcmd.sh <rotulo> 'comando' [timeout_s]
# Envia o comando ao bash gravado (FIFO) e espera o marcador de fim; imprime a saída nova.
S="/c/Users/eduar/AppData/Local/Temp/claude/D--Lab-artefatos-t8-leas/e5f6f2bc-804d-4a02-93e7-6fcf8f6d5c4b/scratchpad"
ID="$1"; CMD="$2"; TO="${3:-60}"
# o comando vai em base64 para não sofrer com aspas no ssh
B64=$(printf '%s' "$CMD" | base64 -w0)
timeout $((TO+20)) $S/vmssh.sh "ID='$ID' TO='$TO' B64='$B64' bash -s" <<'REMOTE'
OUT=/proc/$(pgrep -f "^script -q -t")/fd/1
START=$(wc -c < $OUT)
CMD=$(echo "$B64" | base64 -d)
printf 'echo "[passo=%s inicio=$(date -u +%%FT%%T.%%3NZ)]"; %s\necho "[passo=%s saida=$? fim=$(date -u +%%FT%%T.%%3NZ)]"\n' "$ID" "$CMD" "$ID" > ~/exec.fifo
for i in $(seq 1 $((TO*2))); do
  if tail -c +$((START+1)) $OUT | grep -aq "^\[passo=$ID saida="; then break; fi
  sleep 0.5
done
tail -c +$((START+1)) $OUT | sed 's/\r$//'
REMOTE
