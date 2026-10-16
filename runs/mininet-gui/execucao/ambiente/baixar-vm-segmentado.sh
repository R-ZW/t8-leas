#!/bin/bash
# Baixa o ZIP da VM (release v0.0.1) em segmentos paralelos de bytes e concatena.
# Motivo: o CDN do GitHub limitou cada conexão a ~60-230 KiB/s em 15/10/2026.
# Uso no host (Git Bash): bash baixar-vm-segmentado.sh <pasta-destino> [n-segmentos]
# Se <pasta>/Mininet-GUI-VM-SBRC-2025.zip já existir parcial, os segmentos começam no fim dele.
set -u
URL="https://github.com/latarc/mininet-gui/releases/download/v0.0.1/Mininet-GUI-VM-SBRC-2025.zip"
TOTAL=1303516409   # tamanho informado pela API de releases (asset 238275228)
DEST="${1:?pasta de destino}"
N="${2:-12}"
ZIP="$DEST/Mininet-GUI-VM-SBRC-2025.zip"
SEG="$DEST/segmentos"
mkdir -p "$SEG"
INICIO=$( [ -f "$ZIP" ] && stat -c %s "$ZIP" || echo 0 )
RESTO=$(( TOTAL - INICIO ))
PASSO=$(( (RESTO + N - 1) / N ))
echo "inicio=$INICIO resto=$RESTO segmentos=$N passo=$PASSO $(date -u +%FT%TZ)"

baixa_segmento() {  # $1=indice $2=primeiro byte $3=ultimo byte
  local f="$SEG/parte-$(printf %03d "$1")" quer=$(( $3 - $2 + 1 )) tem
  for tentativa in $(seq 1 50); do
    tem=$( [ -f "$f" ] && stat -c %s "$f" || echo 0 )
    [ "$tem" -ge "$quer" ] && return 0
    curl -sSL --fail --connect-timeout 30 --speed-limit 1024 --speed-time 60 \
      -r "$(( $2 + tem ))-$3" "$URL" >> "$f" || sleep 5
  done
  return 1
}

for i in $(seq 0 $(( N - 1 ))); do
  a=$(( INICIO + i * PASSO )); b=$(( a + PASSO - 1 )); [ $b -ge $TOTAL ] && b=$(( TOTAL - 1 ))
  [ $a -gt $b ] && continue
  baixa_segmento "$i" "$a" "$b" &
done
wait

SOMA=$(cat "$SEG"/parte-* | wc -c)
if [ $(( INICIO + SOMA )) -ne $TOTAL ]; then
  echo "segmentos incompletos: $(( INICIO + SOMA )) de $TOTAL; rode de novo para retomar"; exit 1
fi
for i in $(seq 0 $(( N - 1 ))); do
  f="$SEG/parte-$(printf %03d "$i")"; [ -f "$f" ] && cat "$f" >> "$ZIP"
done
FINAL=$(stat -c %s "$ZIP")
echo "final=$FINAL esperado=$TOTAL $(date -u +%FT%TZ)"
[ "$FINAL" -eq "$TOTAL" ] && rm -rf "$SEG" && echo "tamanho confere"
