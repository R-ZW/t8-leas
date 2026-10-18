# Roteiro A, P14 (parte Linux, comandos literais; diretório ~/aval).
# A instalação de ferramentas de A:P14 foi feita em P12. EVTX: amostra pública
# (python-evtx, tests/data/system.evtx, commit fixado) no lugar do export de Windows.
# Mach-O: as duas amostras sintéticas de G:P10, recortadas de c3_macho.img, no lugar das de macOS.
set -x
cd ~/aval
cp /bin/ls amostras/elf64_ls
printf '#include <stdio.h>\nint main(void){puts("ola");return 0;}\n' > /tmp/ola.c
gcc -m32 -o amostras/elf32_ola /tmp/ola.c
printf '#!/bin/bash\nfor i in 1 2 3; do\n  echo "linha $i"\ndone\n' > amostras/s_bash.sh
printf '#!/usr/bin/env python3\nimport sys\nprint("ola", sys.argv)\n' > amostras/s_py.py
printf '#!/usr/bin/env pwsh\nGet-ChildItem -Path . | ForEach-Object { $_.Name }\n' > amostras/s_ps.ps1
printf '#!/bin/sh\n# so comentario\n# outro comentario\n' > amostras/neg_comentario.sh
printf '#!/bin/sh\nls\n' > amostras/neg_curto.sh
# EVTX público (D3)
curl -fsSL -o amostras/evtx_system.evtx https://raw.githubusercontent.com/williballenthin/python-evtx/c0007441657899c39180de10a2be1a0e43dbeaf9/tests/data/system.evtx
# Mach-O sintéticos de G:P10 (thin: offset 8192, 4096 B; fat: offset 32768, 8192 B)
SRC=~/trabalho/foremost-ng-bb812a22/src
dd if=$SRC/c3_macho.img of=amostras/macho_thin bs=4096 skip=2 count=1 status=none
dd if=$SRC/c3_macho.img of=amostras/macho_fat bs=4096 skip=8 count=2 status=none
file amostras/* > evidencias/P14_file.txt; sha256sum amostras/* > evidencias/P14_amostras.txt
cat evidencias/P14_file.txt evidencias/P14_amostras.txt
stat -c '%n %s' amostras/*
