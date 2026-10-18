# Roteiro A, P11 (comandos literais; diretório ~/aval)
set -x
mkdir -p ~/aval/evidencias ~/aval/amostras && cd ~/aval
printf '#!/bin/bash\n# teste minimo\necho "foremost-ng teste minimo F"\nls -l /tmp\n' > amostras/min.sh
truncate -s 1M min.dd
dd if=amostras/min.sh of=min.dd bs=512 seek=1024 conv=notrunc
sha256sum amostras/min.sh min.dd > evidencias/P11_hashes.txt
cat evidencias/P11_hashes.txt
stat -c '%n %s' amostras/min.sh min.dd
