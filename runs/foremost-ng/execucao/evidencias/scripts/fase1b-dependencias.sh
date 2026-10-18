# Fase 1b — P04 falhou (ctype.h ausente): a imagem foi construída com
# --no-install-recommends e não tem libc6-dev, que o apt-get do Dockerfile dos
# autores (Dockerfile:3-6, sem essa opção) instalaria como recomendação do gcc.
export REG_DIR=/execucao/evidencias
export COLUMNS=100
cd ~/trabalho
echo "=== estado antes: libc6-dev"
dpkg -l libc6-dev 2>&1 | tail -1
echo "=== P00a (Dockerfile:3-6; roteiro A:P2, G:P1): instalar dependencias como no Dockerfile, com sudo"
passo P00a -- sh -c 'sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev'
dpkg -l libc6-dev 2>&1 | tail -1
echo "=== P00b (D1): instalar libc6-dev, recomendacao do gcc omitida na construcao da imagem"
passo P00b -- sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libc6-dev
dpkg -l libc6-dev | tail -1
echo "=== repeticao de P04-P06 e P08 no ambiente corrigido"
cd ~/trabalho/foremost-ng-bb812a22/src
passo P04-2 -- make
ls -l foremost-ng
passo P05-2 -w /usr/local/bin -w /usr/share/man/man8 -w /usr/local/etc -- sudo make install
ls -l /usr/local/bin/foremost-ng /usr/share/man/man8/foremost-ng.8.gz /usr/local/etc/foremost.conf
which foremost-ng
cd ~
passo P06-2 -- env MANPAGER=cat MANWIDTH=100 man foremost-ng
cd ~/trabalho/foremost-ng-bb812a22/src
ls -l evidence2.dd 2>&1
passo P08-2 -w ~/trabalho/foremost-ng-bb812a22/src -- ./foremost-ng -v -x evidence2.dd
ls -la ~/trabalho/foremost-ng-bb812a22/src | grep -i output || echo "(nenhum diretorio output criado em src)"
echo "=== fim da fase 1b"
