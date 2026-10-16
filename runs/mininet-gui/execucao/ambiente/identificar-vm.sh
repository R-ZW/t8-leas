#!/bin/sh
# Identificação do código e do ambiente dentro da VM do Mininet-GUI.
# Só lê: não inicia mininet_gui, mn (sem --version), pingall nem controladores.
# Uso dentro da VM: sh identificar-vm.sh [/home/mininet/mininet-gui] > identificacao-vm.txt 2>&1
P="${1:-/home/mininet/mininet-gui}"

secao() { printf '\n### %s\n' "$*"; }
rodar() { printf '$ %s\n' "$*"; sh -c "$*" 2>&1; printf '[saida=%s]\n' "$?"; }

secao "Data e identificação"
rodar 'date -u +%Y-%m-%dT%H:%M:%SZ'
rodar 'id; hostname'

secao "Sistema operacional e kernel"
rodar 'cat /etc/os-release'
rodar 'uname -a'

secao "Código em $P (versao.md, Como confirmar)"
rodar "git -C '$P' rev-parse HEAD"
rodar "git -C '$P' status --short"
rodar "git -C '$P' remote -v"
rodar "git -C '$P' log -1 --format='%H %ci %s'"
rodar "git -C '$P' describe --tags --always"
rodar "git -C '$P' branch -a"
rodar "git -C '$P' stash list"

secao "Lançador mininet_gui (sem executar)"
rodar 'command -v mininet_gui'
L=$(command -v mininet_gui 2>/dev/null)
if [ -n "$L" ]; then
  rodar "ls -l '$L'"
  rodar "readlink -f '$L'"
  rodar "file '$(readlink -f "$L")'"
  rodar "sha256sum '$(readlink -f "$L")'"
  rodar "head -n 40 '$(readlink -f "$L")'"
fi
rodar 'type mininet_gui'
rodar 'grep -n "mininet_gui" ~/.bashrc ~/.profile /etc/bash.bashrc /etc/profile 2>/dev/null'

secao "Versões"
rodar 'mn --version'
rodar 'ovs-vsctl --version'
rodar 'python3 --version'
rodar 'command -v python3'
rodar 'node --version'
rodar 'npm --version'
rodar 'git --version'
rodar "pip3 show mininet-gui-backend 2>/dev/null | head -n 12"

secao "Manifesto SHA-256 dos arquivos do projeto (sem .git, node_modules, venv, dist, __pycache__)"
if [ -d "$P" ]; then
  ( cd "$P" && find . -type f \
      -not -path './.git/*' -not -path '*/node_modules/*' -not -path '*/venv/*' \
      -not -path '*/.venv/*' -not -path '*/dist/*' -not -path '*/__pycache__/*' \
      -not -name '*.pyc' -print0 | LC_ALL=C sort -z | xargs -0 sha256sum )
fi
