# Roteiro A, P15 (comandos literais; diretório ~/aval)
cd ~/aval
IMG=teste.dd; GAP=1048576; off=$GAP
rm -f $IMG; truncate -s $off $IMG
: > evidencias/P15_offsets.txt
for f in amostras/*; do
  [ "$f" = amostras/min.sh ] && continue
  dd if="$f" of=$IMG bs=512 seek=$((off/512)) conv=notrunc status=none
  printf '%s %s %08d %s\n' "$f" "$off" "$((off/512))" "$(sha256sum < "$f" | cut -d' ' -f1)" >> evidencias/P15_offsets.txt
  sz=$(stat -c %s "$f")
  off=$(( (off + sz + GAP + 511) / 512 * 512 ))
done
truncate -s $((off + GAP)) $IMG
sha256sum $IMG >> evidencias/P15_offsets.txt
cat evidencias/P15_offsets.txt
stat -c '%n %s' $IMG
