#!/bin/bash
# Copia ~/evidencias da VM para o host por SCP (rede host-only) e confere SHA-256 nos dois lados.
# O guestcontrol do VirtualBox não funciona nesta VM: as Guest Additions são o pacote 6.1.6 do
# Ubuntu, sem o VBoxService (runlevel 1).
# Uso no host (Git Bash): bash transferir-evidencias.sh <pasta-destino> [ip] [known_hosts]
# Autenticação: senha padrão publicada pelos autores (mininet/mininet), fornecida por SSH_ASKPASS.
set -euo pipefail
DEST="${1:?pasta de destino no host}"
IP="${2:-192.168.56.101}"
KH="${3:-D:/Lab-artefatos/t8-mininet-vm/known_hosts-vm}"
ASK="$(mktemp)"; printf '#!/bin/sh\necho mininet\n' > "$ASK"; chmod +x "$ASK"
trap 'rm -f "$ASK"' EXIT
export SSH_ASKPASS="$ASK" SSH_ASKPASS_REQUIRE=force DISPLAY=:0
O=(-o UserKnownHostsFile="$KH" -o StrictHostKeyChecking=yes -o PubkeyAuthentication=no -o LogLevel=ERROR)

# 1) manifesto no convidado, no formato do sha256sum
ssh "${O[@]}" "mininet@$IP" 'cd ~/evidencias && find . -type f ! -name .bashrc-gravacao ! -name manifesto-convidado.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > manifesto-convidado.sha256 && cat manifesto-convidado.sha256' < /dev/null

# 2) cópia preservando datas
mkdir -p "$DEST"
scp -p -r "${O[@]}" "mininet@$IP:evidencias/." "$DEST/" < /dev/null

# 3) conferência no host
( cd "$DEST" && sha256sum -c manifesto-convidado.sha256 )
