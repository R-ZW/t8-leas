# Fase 3 — complementos D2 (P11-2, conferência das saídas de G) e testes externos D3 (DFTT).
export REG_DIR=/execucao/evidencias
export COLUMNS=100
E=/execucao/evidencias/scripts/entradas
OUT=/execucao/evidencias/saidas
DF=/execucao/evidencias/dftt

echo "################ Complementos D2"
cd ~/trabalho
passo P11-2 -- bash $E/P11-2-sem-cr.sh
passo P16-G-cmp -- bash $E/P-G-cmp.sh

echo "################ D3 — DFTT #11 e #12"
mkdir -p ~/dftt && cd ~/dftt
passo P39-prep -w ~/dftt -- sh -c 'cp /execucao/insumos/dftt-11/11-carve-fat/11-carve-fat.dd /execucao/insumos/dftt-12/12-carve-ext2/12-carve-ext2.dd . && md5sum 11-carve-fat.dd 12-carve-ext2.dd && sha256sum 11-carve-fat.dd 12-carve-ext2.dd && ls -l'

for t in 11 12; do
  img=$( [ $t = 11 ] && echo 11-carve-fat.dd || echo 12-carve-ext2.dd )
  id=$( [ $t = 11 ] && echo P39 || echo P41 )
  echo "=== $id (A3:P10): foremost-ng -v -i $img -o saida$t"
  passo $id -w ~/dftt -- foremost-ng -v -i $img -o ~/dftt/saida$t
  passo $id-conf -- sh -c "find saida$t -type f | sort; ls -l saida$t/recovery.log 2>&1; find saida$t -type f ! -name audit.txt -exec file {} +"
  passo $id-gabarito -- python3 $E/compara-gabarito.py $DF/gabarito-$t.tsv ~/dftt/saida$t
  echo "=== $id-t (A3:P11): foremost-ng -t evtx,elf,exe -i $img -o saida$t-t"
  passo $id-t -w ~/dftt -- foremost-ng -t evtx,elf,exe -i $img -o ~/dftt/saida$t-t
  passo $id-t-conf -- sh -c "find saida$t-t -mindepth 1 -type d | sort; find saida$t-t -type f | sort; cat saida$t-t/audit.txt"
  mkdir -p $DF/saida$t $DF/saida$t-t
  cp saida$t/audit.txt $DF/saida$t/; cp saida$t-t/audit.txt $DF/saida$t-t/
  (cd saida$t && find . -type f ! -name audit.txt -exec md5sum {} + | sort -k2) > $DF/saida$t/md5-recuperados.txt
  (cd saida$t && find . -type f ! -name audit.txt -exec sha256sum {} + | sort -k2) > $DF/saida$t/sha256-recuperados.txt
done
echo "=== fim da fase 3"
