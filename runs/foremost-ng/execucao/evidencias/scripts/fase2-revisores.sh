# Fase 2 — passos [NÃO DOCUMENTADO] propostos pelos revisores (D2). Roteiro: P09–P38.
# Executado com `source` dentro de `gravar-sessao.sh sessao /execucao ...`.
export REG_DIR=/execucao/evidencias
export COLUMNS=100
E=/execucao/evidencias/scripts/entradas
OUT=/execucao/evidencias/saidas
SRC=~/trabalho/foremost-ng-bb812a22/src
mkdir -p $OUT
guarda() { mkdir -p "$OUT/$1"; cp -a "$2" "$OUT/$1/"; }

echo "################ Preparação e verificação"
cd ~/trabalho
echo "=== P09 (A:P3): registrar versões"
passo P09 -- sh -c '{ cat /etc/os-release; uname -m; gcc --version | head -1; make --version | head -1; openssl version; curl --version | head -1; dpkg -l libssl-dev libcurl4-openssl-dev | tail -2; } 2>&1'
passo P09-amb -- bash /execucao/evidencias/scripts/entradas/P09-ambiente.sh

echo "=== P10 (A:P5): fixar o commit no clone"
cd ~/trabalho/foremost-ng
passo P10 -- sh -c 'git checkout bb812a22cb06ef87b5a2d877dfb6f40eb12d460d && git rev-parse HEAD && git status --short && git log -1 --format="%H %cI %s"'

echo "=== P11 (A:P4 alternativa; A2:P6): integridade do pacote e comparação clone x zip"
cd ~/trabalho
passo P11 -w /tmp -- bash /execucao/evidencias/scripts/entradas/P11-integridade.sh

echo "=== P12 (A:P14/P19; G:P1): ferramentas de verificação"
passo P12 -- sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-multilib file binutils python3 python3-evtx curl jq
passo P12-versoes -- sh -c 'file --version | head -1; readelf --version | head -1; python3 --version; dpkg -l python3-evtx gcc-multilib file jq curl | tail -5; ls /usr/bin | grep -i evtx'

echo "=== P13a (A:P10): foremost-ng -h"
cd ~
passo P13a -- foremost-ng -h
echo "=== P13b (G:P3): ./foremost-ng -V; ./foremost-ng -h; man | head"
cd $SRC
passo P13b -- sh -c './foremost-ng -V; echo "exit -V=$?"; ./foremost-ng -h; echo "exit -h=$?"; MANPAGER=cat man foremost-ng | head -n 30'

echo "################ Teste mínimo (F)"
echo "=== P14a (A:P11): min.dd"
cd ~
passo P14a -w ~ -- bash $E/P14a-A-min.sh
echo "=== P14b (G:P4): disk.img e /temp/output"
cd $SRC
passo P14b -w $SRC -- bash $E/P14b-G-disk.sh
echo "=== P15a (A:P12): foremost-ng -i min.dd -o ~/aval/saida_min"
cd ~/aval
passo P15a -w ~/aval -- foremost-ng -i min.dd -o ~/aval/saida_min
echo "=== P16a (A:P13): conferir saída mínima"
passo P16a -- sh -c 'cat saida_min/audit.txt; ls -R saida_min; cmp amostras/min.sh saida_min/script/00001024.script && echo IDENTICO; find ~/aval/saida_min -type f | sort > evidencias/P12_arquivos.txt; cat evidencias/P12_arquivos.txt'
guarda P15a ~/aval/saida_min
echo "=== P15b (G:P5): ./foremost-ng -i disk.img -o /temp/output/carved"
cd $SRC
passo P15b -w /tmp -- ./foremost-ng -i disk.img -o /temp/output/carved
if [ ! -d /temp/output/carved ]; then
  echo "=== P14b-2 (D2): /temp/output não existe (mkdir -p de G:P4 sem root); criado com sudo e entregue ao usuário"
  passo P14b-2 -- sh -c 'sudo mkdir -p /temp/output && sudo chown revisor:revisor /temp/output && ls -ld /temp/output'
  passo P15b-2 -w /temp/output -- ./foremost-ng -i disk.img -o /temp/output/carved
fi
echo "=== P16b (G:P5): conferir saída"
passo P16b -- sh -c 'cat /temp/output/carved/audit.txt; ls -la /temp/output/carved/*'
[ -d /temp/output/carved ] && guarda P15b /temp/output/carved

echo "################ C1 — EVTX (sintético de G)"
cd $SRC
passo P17b -w $SRC -- bash $E/P17b-G-evtx.sh
passo P18b -w /tmp -- ./foremost-ng -v -t evtx -i c1_evtx.img -o /tmp/out_c1
passo P18b-conf -- bash $E/P18b-G-conf.sh
passo P19b -- sh -c 'for f in /tmp/out_c1/evtx/*.evtx; do echo "== $f"; evtx_dump.py "$f"; echo "exit=$?"; done'
[ -d /tmp/out_c1 ] && guarda P18b /tmp/out_c1

echo "################ C2 — scripts (G)"
passo P20b -w $SRC -- bash $E/P20b-G-script.sh
passo P21b -w /tmp -- ./foremost-ng -v -t script -i c2_script.img -o /tmp/out_c2
passo P21b-conf -- sh -c 'cat /tmp/out_c2/audit.txt; ls -l /tmp/out_c2/script/; head -n 20 /tmp/out_c2/script/*'
[ -d /tmp/out_c2 ] && guarda P21b /tmp/out_c2

echo "################ C3 — Mach-O (G)"
passo P23b -w $SRC -- bash $E/P23b-G-macho.sh
passo P24b -w /tmp -- ./foremost-ng -v -t macho -i c3_macho.img -o /tmp/out_c3
passo P24b-conf -- sh -c 'cat /tmp/out_c3/audit.txt; file /tmp/out_c3/macho/*.macho; ls -l /tmp/out_c3/macho/*.macho'
[ -d /tmp/out_c3 ] && guarda P24b /tmp/out_c3

echo "################ C4 — ELF (G)"
passo P26b -w $SRC -- bash $E/P26b-G-elf.sh
passo P27b -w /tmp -- ./foremost-ng -v -t elf -i memory.dump -o /tmp/out_c4
passo P27b-conf -- sh -c 'cat /tmp/out_c4/audit.txt; file /tmp/out_c4/elf/*.elf; ls -l /tmp/out_c4/elf/; for f in /tmp/out_c4/elf/*.elf; do echo "=== Analisando $f ==="; readelf -h -l "$f"; done'
[ -d /tmp/out_c4 ] && guarda P27b /tmp/out_c4

echo "################ Amostras de A e imagem combinada (C1–C4)"
cd ~/aval
passo P20a -w ~/aval -- bash $E/P20a-A-amostras.sh
passo P28a -w ~/aval -- bash $E/P28a-A-teste-dd.sh
passo P28b -w ~/aval -- foremost-ng -i teste.dd -o ~/aval/saida_todos
passo P28c -w ~/aval -- foremost-ng -t evtx,elf,exe -i teste.dd -o ~/aval/saida_tipos
passo P28d -- bash $E/P28d-A-conferencias.sh
passo P19a -- bash $E/P19a-A-evtx-dump.sh
guarda P28b ~/aval/saida_todos; guarda P28c ~/aval/saida_tipos

echo "################ C5 — VirusTotal sem chave"
cd $SRC
passo P29b -w $SRC -- sh -c 'rm -rf ./carved-files_nokey; env -u VT_API_KEY ./foremost-ng -x -t elf -i memory.dump -o ./carved-files_nokey; echo "exit foremost-ng=$?"; cat ./carved-files_nokey/audit.txt; ls -la ./carved-files_nokey/elf/'
[ -d ./carved-files_nokey ] && guarda P29b ./carved-files_nokey
cd ~/aval
passo P29a -w ~/aval -- bash -c 'unset VT_API_KEY; foremost-ng -x -t elf -i teste.dd -o ~/aval/saida_vt_semchave 2>&1 | tee evidencias/P25_semchave.txt; echo "exit foremost-ng=${PIPESTATUS[0]}"; cat saida_vt_semchave/audit.txt'
[ -d ~/aval/saida_vt_semchave ] && guarda P29a ~/aval/saida_vt_semchave

echo "################ C6 — busca de evidence2.dd (G:P16)"
cd $SRC
passo P34 -- sh -c 'find .. -name "evidence2.dd"; echo "find exit=$? (sem linhas = nenhum arquivo)"; find / -xdev -name "evidence2.dd" 2>/dev/null; echo "busca em / concluida"'

echo "################ C7 — inspeção (A:P33; G:P17)"
cd $SRC
passo P38a -- bash $E/P38a-A-grep.sh
passo P38b -- sh -c 'grep -n "typedef struct s_spec" -A 19 main.h; grep -n "void init_all" -A 82 state.c; grep -n "unsigned char \*extract_file" -A 69 extract.c'

echo "################ cópia das entradas e evidências de A"
mkdir -p $OUT/entradas
cp -a ~/aval/evidencias $OUT/entradas/A-evidencias
cp -a ~/aval/amostras $OUT/entradas/A-amostras
cp -a ~/aval/min.dd $SRC/disk.img $SRC/c1_evtx.img $SRC/c2_script.img $SRC/c3_macho.img $SRC/memory.dump $OUT/entradas/
gzip -n -c ~/aval/teste.dd > $OUT/entradas/teste.dd.gz
(cd $OUT/entradas && sha256sum min.dd disk.img c1_evtx.img c2_script.img c3_macho.img memory.dump teste.dd.gz; sha256sum ~/aval/teste.dd)
echo "=== fim da fase 2"
