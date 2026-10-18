# Roteiro A, conferências P18, P20, P21, P22, P24 sobre saida_todos/saida_tipos
# (comandos literais; nome do EVTX ajustado para evtx_system.evtx; diretório ~/aval)
cd ~/aval
echo "##### A:P18 (C1)"
nome=$(awk '$1 ~ /evtx/ {print $3}' evidencias/P15_offsets.txt)
grep evtx evidencias/P15_offsets.txt; grep -i evtx saida_todos/audit.txt saida_tipos/audit.txt; ls -l saida_todos/evtx saida_tipos/evtx; stat -c %s amostras/evtx_system.evtx; cmp amostras/evtx_system.evtx saida_todos/evtx/$nome.evtx && echo IDENTICO
echo "##### A:P20 (C2)"
ls -l saida_todos/script
while read f off nome h; do
  case "$f" in amostras/s_*)
    alvo=saida_todos/script/$nome.script
    echo "== $f -> $alvo"; head -1 "$alvo"; cmp "$f" "$alvo" && echo IDENTICO;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P20_scripts.txt
grep script saida_todos/audit.txt
echo "##### A:P21 (C2 negativos)"
while read f off nome h; do
  case "$f" in amostras/neg_*)
    if [ -e saida_todos/script/$nome.script ]; then echo "$f RECUPERADO"; else echo "$f descartado"; fi;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P21_negativos.txt
echo "##### A:P22 (C3)"
ls -l saida_todos/macho; grep macho saida_todos/audit.txt
while read f off nome h; do
  case "$f" in amostras/macho_*)
    alvo=saida_todos/macho/$nome.macho
    echo "== $f -> $alvo"; file "$alvo"; stat -c %s "$f" "$alvo"; cmp "$f" "$alvo" && echo IDENTICO;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P22_macho.txt
echo "##### A:P24 (C4)"
ls -l saida_todos/elf saida_tipos/elf
while read f off nome h; do
  case "$f" in amostras/elf*)
    for d in saida_todos saida_tipos; do
      alvo=$d/elf/$nome.elf
      echo "== $f -> $alvo"; file "$alvo"
      readelf -h -l "$alvo" 2>&1 | grep -iE 'error|warning' || echo "readelf -h -l sem erros"
      readelf -S "$alvo" 2>&1 | grep -iE 'error|warning' | head -3
      stat -c %s "$f" "$alvo"
      cmp -n $(stat -c %s "$alvo") "$f" "$alvo" && echo PREFIXO_IDENTICO
    done;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P24_elf.txt
echo "##### arquivos fora dos esperados (todas as saidas)"
find saida_todos saida_tipos -type f | sort
