# Roteiro G, P4 (comandos literais; diretório <raiz>/src)
set -x
python3 -c '
with open("foremost-ng", "rb") as f:
    elf_data = f.read()
script_data = b"#!/bin/bash\n# Script de teste\necho \"Foremost-NG functional test\"\n"
img = bytearray(2 * 1024 * 1024)
img[4096:4096+len(elf_data)] = elf_data
img[524288:524288+len(script_data)] = script_data
with open("disk.img", "wb") as out:
    out.write(img)
'
mkdir -p /temp/output
rm -rf /temp/output/carved
ls -l disk.img
sha256sum disk.img foremost-ng
