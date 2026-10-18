# Conferência complementar (D2) das saídas dos testes de G: recorta da imagem de
# entrada os bytes originais (offset e tamanho conhecidos) e compara com o recuperado.
SRC=~/trabalho/foremost-ng-bb812a22/src
O=/execucao/evidencias/saidas
cd /tmp && rm -rf gcmp && mkdir gcmp && cd gcmp
cmpx() { # rotulo original recuperado
  a=$(stat -c %s "$2"); b=$(stat -c %s "$3" 2>/dev/null || echo ausente)
  if [ "$b" = ausente ]; then echo "$1: recuperado ausente ($3)"; return; fi
  if cmp -s "$2" "$3"; then r=IDENTICO
  elif [ "$b" -lt "$a" ] && cmp -s -n "$b" "$2" "$3"; then r="PREFIXO_IDENTICO (recuperado menor)"
  elif [ "$b" -gt "$a" ] && cmp -s -n "$a" "$2" "$3"; then r="ORIGINAL_E_PREFIXO (recuperado maior)"
  else r=DIFERENTE; fi
  echo "$1: original=$a B recuperado=$b B -> $r"
}
# P15b (disk.img): ELF = binário foremost-ng no offset 4096; script no offset 524288 (65 B)
cmpx "P15b ELF 4096" $SRC/foremost-ng $O/P15b/carved/elf/00000008.elf
dd if=$SRC/disk.img of=s_disk bs=1 skip=524288 count=65 status=none; cmpx "P15b script 524288" s_disk $O/P15b/carved/script/00001024.script
# P18b (c1_evtx.img): cabeçalho 4096 B + chunk 65536 B no offset 8192
dd if=$SRC/c1_evtx.img of=evtx_sint bs=1 skip=8192 count=69632 status=none; cmpx "P18b EVTX sintetico 8192 (cabecalho+chunk)" evtx_sint $O/P18b/out_c1/evtx/00000016.evtx
# P21b (c2_script.img): s1 76 B em 4096; s2 75 B em 16384; s4 62 B em 49152
dd if=$SRC/c2_script.img of=s1 bs=1 skip=4096 count=76 status=none; cmpx "P21b s1 bash 4096" s1 $O/P21b/out_c2/script/00000008.script
dd if=$SRC/c2_script.img of=s2 bs=1 skip=16384 count=75 status=none; cmpx "P21b s2 python 16384" s2 $O/P21b/out_c2/script/00000032.script
dd if=$SRC/c2_script.img of=s3 bs=1 skip=32768 count=18 status=none; cmpx "P21b s3 <32 B 32768" s3 $O/P21b/out_c2/script/00000064.script
dd if=$SRC/c2_script.img of=s4 bs=1 skip=49152 count=62 status=none; cmpx "P21b s4 so comentarios 49152" s4 $O/P21b/out_c2/script/00000096.script
# P24b (c3_macho.img): thin 4096 B em 8192; fat 8192 B em 32768
dd if=$SRC/c3_macho.img of=thin bs=1 skip=8192 count=4096 status=none; cmpx "P24b Mach-O thin 8192" thin $O/P24b/out_c3/macho/00000016.macho
dd if=$SRC/c3_macho.img of=fat bs=1 skip=32768 count=8192 status=none; cmpx "P24b Mach-O fat 32768" fat $O/P24b/out_c3/macho/00000064.macho
# P27b (memory.dump): ELF32 4096 B em 4096; ELF64 = foremost-ng em 65536
dd if=$SRC/memory.dump of=elf32 bs=1 skip=4096 count=4096 status=none; cmpx "P27b ELF32 4096" elf32 $O/P27b/out_c4/elf/00000008.elf
cmpx "P27b ELF64 65536" $SRC/foremost-ng $O/P27b/out_c4/elf/00000128.elf
cmpx "P29b ELF32 (sem chave)" elf32 $O/P29b/carved-files_nokey/elf/00000008.elf
cmpx "P29b ELF64 (sem chave)" $SRC/foremost-ng $O/P29b/carved-files_nokey/elf/00000128.elf
# Fim do ELF64 original x tabela de seções (readelf no binário original)
readelf -h $SRC/foremost-ng | grep -E "Start of section headers|Size of section headers|Number of section headers"
readelf -lW $SRC/foremost-ng | grep LOAD
