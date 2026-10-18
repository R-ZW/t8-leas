# Roteiro G, P8 (comandos literais; diretório <raiz>/src)
set -x
python3 -c '
img = bytearray(128 * 1024)
# Script 1 válido (Bash, >= 32 bytes, com corpo executável) no offset 4096
s1 = b"#!/bin/bash\n# Valid bash script\necho \"Hello from carved bash script\"\nexit 0\n"
# Script 2 válido (Python, >= 32 bytes, com corpo executável) no offset 16384
s2 = b"#!/usr/bin/env python3\n# Valid python script\nimport sys\nprint(sys.version)\n"
# Script 3 inválido (< 32 bytes) no offset 32768
s3 = b"#!/bin/sh\necho ok\n"
# Script 4 inválido (>= 32 bytes, mas apenas comentários) no offset 49152
s4 = b"#!/bin/bash\n# apenas comentario 1\n# apenas comentario 2 longo\n"
img[4096:4096+len(s1)] = s1
img[16384:16384+len(s2)] = s2
img[32768:32768+len(s3)] = s3
img[49152:49152+len(s4)] = s4
with open("c2_script.img", "wb") as f:
    f.write(img)
'
rm -rf /tmp/out_c2
ls -l c2_script.img; sha256sum c2_script.img
