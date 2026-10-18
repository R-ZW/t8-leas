# Fase 1 — passos dos autores sem entrada de dados (D0/D1). Roteiro: P01–P08.
# Executado com `source` dentro de `gravar-sessao.sh sessao /execucao ...`.
export REG_DIR=/execucao/evidencias
export COLUMNS=100
mkdir -p ~/trabalho && cd ~/trabalho

echo "=== P01 (artigo p.6, §4): git clone"
passo P01 -w ~/trabalho -- git clone https://github.com/cristianzsh/foremost-ng.git

echo "=== P02 (artigo p.6, §4): cd foremost-ng; make"
cd ~/trabalho/foremost-ng
passo P02 -- make

echo "=== P03 (README:23,27-28): obter o pacote e entrar em src (zip fixado no lugar do tar.gz: D1)"
cd ~/trabalho
passo P03 -w ~/trabalho -- unzip /pacote/artefato.zip -d ~/trabalho
cd ~/trabalho/foremost-ng-bb812a22/src && pwd && ls

echo "=== P04 (README:31-33): make"
passo P04 -- make

echo "=== P05 (README:34): sudo make install"
passo P05 -w /usr/local/bin -w /usr/share/man/man8 -w /usr/local/etc -- sudo make install
ls -l /usr/local/bin/foremost-ng /usr/share/man/man8/foremost-ng.8.gz /usr/local/etc/foremost.conf
which foremost-ng

echo "=== P06 (README:76-79): man foremost-ng"
cd ~
passo P06 -- env MANPAGER=cat MANWIDTH=100 man foremost-ng

echo "=== P07 (README:89-101): VT_API_KEY com chave valida -> bloqueado; verifica-se apenas se a variavel existe"
passo P07 -- sh -c 'if [ -n "${VT_API_KEY:-}" ]; then echo "VT_API_KEY definida"; else echo "VT_API_KEY nao definida (nenhuma chave disponivel)"; fi'

echo "=== P08 (artigo p.8, Fig. 2): ./foremost-ng -v -x evidence2.dd (arquivo indisponivel)"
cd ~/trabalho/foremost-ng-bb812a22/src
ls -l evidence2.dd 2>&1
passo P08 -w ~/trabalho/foremost-ng-bb812a22/src -- ./foremost-ng -v -x evidence2.dd
ls -la ~/trabalho/foremost-ng-bb812a22/src | grep -i output || echo "(nenhum diretorio output criado em src)"
echo "=== fim da fase 1"
