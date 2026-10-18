#!/bin/bash
# uso: vmssh.sh 'comando'   (ssh não interativo na VM, senha padrão dos autores via askpass)
ASK="/c/Users/eduar/AppData/Local/Temp/claude/D--Lab-artefatos-t8-leas/e5f6f2bc-804d-4a02-93e7-6fcf8f6d5c4b/scratchpad/ask.sh"
[ -f "$ASK" ] || { printf '#!/bin/sh\necho mininet\n' > "$ASK"; chmod +x "$ASK"; }
export SSH_ASKPASS="$ASK" SSH_ASKPASS_REQUIRE=force DISPLAY=:0
exec ssh -o UserKnownHostsFile=D:/Lab-artefatos/t8-mininet-vm/known_hosts-vm -o StrictHostKeyChecking=yes -o PubkeyAuthentication=no -o LogLevel=ERROR -o ConnectTimeout=10 mininet@192.168.56.101 "$@"
