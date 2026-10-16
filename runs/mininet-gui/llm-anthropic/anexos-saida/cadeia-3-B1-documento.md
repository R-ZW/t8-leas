# Roteiro de execução — Mininet-GUI (SBRC 2025, selos F e R)

Oct 16, 2026 · @edu

## Escopo e regras

Este roteiro leva a execução do Mininet-GUI (commit `465648a4425a4457af0348ab951cf7f71d37a86f`) até uma decisão sobre F e R, com 28 passos, sendo 12 não documentados pelos autores e 3 com valores de entrada não documentados (P19–P21). Nada aqui foi executado: os resultados esperados são os declarados pelos autores ou derivados do código, com a fonte indicada.

- **Fonte dos procedimentos:** README.md do artefato (citado como `README.md:linha` em artefato.txt) e scripts `run.sh`/`setup.sh`. Passos fora disso levam a marca **\[NÃO DOCUMENTADO\]** e uma justificativa.
- **Caminho seguido:** a VM recomendada pelos autores (README.md:49–57). A instalação manual (README.md:60–78) fica como alternativa não coberta, pois os próprios autores alertam que ela altera o kernel (README.md:62).
- **Regra de R:** R é atribuído se C4 e C5 forem reproduzidas (reivindicacoes.md). C1, C2, C3 e C6 são verificadas para o relatório, mas não decidem R.
- **Evidências:** crie no hospedeiro a pasta `~/sbrc2025-mininet-gui/evidencias/` e, dentro da VM, `~/evidencias/`. Nomeie cada arquivo pelo passo (`P10_pingall.png`). Capturas de tela devem mostrar data e hora do sistema.
- **Interrupção global:** se a VM não importar ou não iniciar (P3–P4), ou se a interface não abrir (P7), pare: F e R ficam “Não atribuir” por falha de execução, a menos que os autores corrijam o problema no prazo de contato do comitê.
- **Fluxo:** P1–P7 preparam o ambiente; P8–P14 são o teste mínimo; P15–P28 são os blocos de R. Execute na ordem; os blocos de R reutilizam resultados do teste mínimo quando indicado.

## Requisitos do ambiente

O hospedeiro precisa do VirtualBox 7.1.6 e de memória para a VM; o README dá dois mínimos diferentes de RAM (8 GB e 2 GB), e o laptop dos autores tinha 8 GB no total.

| Item | Valor exigido | Fonte | Observação |
| --- | --- | --- | --- |
| Virtualizador | Oracle VirtualBox 7.1.6 r167084 | README.md:37 | Única dependência com versão no caminho da VM |
| RAM da VM | Mínimo 8 GB | README.md:38 | Conflita com a linha 103 |
| RAM e CPU da VM (experimentos) | Mínimo 2 GB e 1 núcleo reservado | README.md:103 | — |
| Hardware de referência | Intel i5-10300H 2,50 GHz, 8 GB RAM, Windows 11 Home 64 bits | README.md:26–31 | Hospedeiro da demonstração, não mínimo |
| Disco livre | Pelo menos 80 GB | README.md:32 | — |
| Imagem da VM | `Mininet-GUI-Desktop-VM-SBRC-2025.ova` | README.md:53–55 | Hospedada no Google Drive; sem hash de referência |
| Credenciais | usuário `mininet`, senha `mininet` | README.md:57 | Também usadas pelo `sudo` de run.sh |
| Navegador | Dentro da VM | README.md:86 | Versão não informada |
| Node.js (na VM) | 18.20.7 via nvm | setup.sh:15–19 | Selecionado por run.sh:20 |
| Backend (na VM) | fastapi, websockets, uvicorn, python-multipart | requirements.txt:1–4 | Sem versões fixadas |
| Mininet (na VM) | Versão não informada | README.md:66 | Clonado do branch padrão na instalação manual |
| Ryu (opcional, passo 8) | `ryu`, `eventlet==0.30.0`, `dnspython==1.16.0` | README.md:75–77 | Não se sabe se já vem na VM |

Dois pontos não estão nos anexos e precisam de decisão do avaliador:

- **\[NÃO DOCUMENTADO\] Virtualização por hardware (VT-x/AMD-V) habilitada na BIOS do hospedeiro.** É necessária para o VirtualBox iniciar uma VM de 64 bits; sem ela, P4 falha antes de qualquer teste do artefato.
- **\[NÃO DOCUMENTADO\] RAM a reservar.** Com hospedeiro de 8 GB, reservar 8 GB à VM é inviável. Use a memória que o `.ova` trouxer configurada, desde que ≥ 2 GB (README.md:103), e registre o valor em P3.

## Preparação do ambiente (P1–P7)

P1–P7 deixam a interface aberta no navegador da VM; só P5 não é documentado pelos autores.

### P1 — Conferir o hospedeiro

- **Selo / reivindicação:** F (pré-requisito).
- **Diretório:** hospedeiro, `~/sbrc2025-mininet-gui/`.
- **Comando:** `VBoxManage --version > evidencias/P1_vbox.txt; df -h . >> evidencias/P1_vbox.txt` (no Windows, `"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" --version`).
- **Esperado (autores):** VirtualBox 7.1.6 r167084 (README.md:37) e ≥ 80 GB livres (README.md:32).
- **Evidência:** `P1_vbox.txt`.
- **Sucesso:** saída `7.1.6r167084` e espaço suficiente.
- **Falha:** VirtualBox ausente ou disco insuficiente.
- **Interrupção:** não há como instalar o VirtualBox. Versão diferente não interrompe: registre a divergência e siga para P3.

### P2 — Baixar a imagem da VM

- **Selo / reivindicação:** F.
- **Diretório:** hospedeiro, `~/sbrc2025-mininet-gui/`.
- **Comando:** abrir no navegador `https://drive.google.com/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing` (README.md:53), baixar para este diretório e depois `ls -l *.ova > evidencias/P2_ova.txt; sha256sum Mininet-GUI-Desktop-VM-SBRC-2025.ova >> evidencias/P2_ova.txt`.
- **Esperado (autores):** arquivo `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (README.md:55).
- **Evidência:** `P2_ova.txt` com tamanho e SHA-256. Os autores não dão hash de referência; o registro serve para rastreabilidade.
- **Sucesso:** download completo com o nome indicado.
- **Falha:** link indisponível, acesso negado ou download truncado.
- **Interrupção:** link inacessível após duas tentativas em horários distintos. Pare (interrupção global) e registre a data e a mensagem do Google Drive.

### P3 — Importar a VM

- **Selo / reivindicação:** F.
- **Diretório:** hospedeiro, VirtualBox.
- **Comando:** abrir o `.ova` no VirtualBox (Arquivo → Importar Appliance → selecionar o arquivo → Importar), como em README.md:55. Depois: `VBoxManage showvminfo "<nome da VM importada>" > evidencias/P3_vminfo.txt`.
- **Esperado (autores):** a máquina virtual é importada (README.md:55).
- **Evidência:** `P3_vminfo.txt` (RAM, CPUs, rede) e captura `P3_import.png`.
- **Sucesso:** VM listada no VirtualBox sem erro de importação; RAM ≥ 2 GB e ≥ 1 CPU (README.md:103).
- **Falha:** erro de importação ou arquivo rejeitado.
- **Interrupção:** erro persiste após novo download (P2). Pare (interrupção global).

### P4 — Iniciar a VM e fazer login

- **Selo / reivindicação:** F (README, Teste mínimo, passo 1).
- **Diretório:** VirtualBox.
- **Comando:** iniciar a VM e entrar com usuário `mininet`, senha `mininet` (README.md:57 e 82).
- **Esperado (autores):** sessão gráfica com terminal acessível por Ctrl+Alt+T (README.md:84).
- **Evidência:** `P4_desktop.png`. Dentro da VM, criar `mkdir -p ~/evidencias`.
- **Sucesso:** área de trabalho carregada e terminal abre.
- **Falha:** VM não inicia (ex.: VT-x desabilitado), tela preta ou login recusado.
- **Interrupção:** falha que não se resolve habilitando VT-x/AMD-V. Pare (interrupção global).

### P5 — Conferir versão do código e das dependências \[NÃO DOCUMENTADO\]

- **Justificativa:** a avaliação se refere ao commit `465648a4…`, mas a VM é externa e sem hash; e as dependências do backend não têm versão (requirements.txt:1–4). Sem este passo, não se sabe o que foi executado.
- **Selo / reivindicação:** F e R (rastreabilidade).
- **Diretório:** VM, `/home/mininet/mininet-gui` (run.sh:7).
- **Comando:**

```bash
cd /home/mininet/mininet-gui
git rev-parse HEAD > ~/evidencias/P5_versao.txt 2>&1
sha256sum README.md run.sh setup.sh mininet-gui-backend/mininet_gui_backend/api.py mininet-gui-frontend/src/components/NetworkGraph.vue mininet-gui-frontend/src/components/Webshell.vue >> ~/evidencias/P5_versao.txt
mn --version >> ~/evidencias/P5_versao.txt 2>&1
python3 --version >> ~/evidencias/P5_versao.txt
python3 -m pip show fastapi uvicorn websockets python-multipart | grep -E '^(Name|Version)' >> ~/evidencias/P5_versao.txt
node --version >> ~/evidencias/P5_versao.txt 2>&1
which ryu-manager >> ~/evidencias/P5_versao.txt 2>&1
```

- **Esperado (índice de artefato.txt, não dos autores):** HEAD `465648a4425a4457af0348ab951cf7f71d37a86f`; SHA-256 de README.md `e424434f…3753`, run.sh `e1e2a1e8…d77f5`, setup.sh `9f7c7bf5…7246`, api.py `1ea14fe4…0d6e`, NetworkGraph.vue `c8272489…e345`, Webshell.vue `9758dc08…c5b84` (hashes completos no índice de artefato.txt).
- **Evidência:** `P5_versao.txt`.
- **Sucesso:** HEAD igual ao commit, ou todos os hashes iguais quando não houver `.git`.
- **Falha:** algum hash diverge. Não é falha do artefato: registre que a execução avaliou a versão da VM, e não o commit.
- **Interrupção:** nenhuma; prossiga com a ressalva no relatório.

### P6 — Iniciar o Mininet-GUI

- **Selo / reivindicação:** F (README, Teste mínimo, passo 2).
- **Diretório:** VM, `~` (o script usa caminhos absolutos).
- **Comando:** Ctrl+Alt+T e `mininet_gui` (alternativa: `/home/mininet/mininet-gui/run.sh`), conforme README.md:84. Se o `sudo` pedir senha, use `mininet`.
- **Esperado (autores):** uma URL na saída do terminal, por exemplo `http://10.0.2.15:5173` (README.md:86); o script imprime “Mininet-GUI bootstrap complete”, os caminhos dos logs e “Mininet-GUI is available at:” (run.sh:22–28).
- **Evidência:** captura `P6_run.png` do terminal inteiro. Não redirecione a saída com `| tee`: os processos em segundo plano mantêm o pipe aberto e alteram o comportamento do script.
- **Sucesso:** URL impressa sem erro fatal.
- **Falha:** script aborta ou não imprime a URL. A mensagem `nvm: command not found` (run.sh:20 chama `nvm` sem carregar `nvm.sh`) não é falha por si: anote e decida em P7.
- **Interrupção:** sem URL após duas execuções. Execute P14 (logs) e pare (interrupção global).

### P7 — Abrir a interface

- **Selo / reivindicação:** F (README, Teste mínimo, passo 3); base de C1.
- **Diretório:** VM, navegador.
- **Comando:** abrir no navegador da VM a URL impressa em P6 (README.md:86).
- **Esperado (autores):** interface com três áreas: barra lateral de controles, painel inferior WebShell em abas e área principal com o grafo (artigo, p. 7, Fig. 2).
- **Evidência:** `P7_interface.png`.
- **Sucesso:** barra lateral com “Generate Topology”, “Reset Topology”, “Create Link”, “Delete Selected”, “Run Pingall Test” e os botões de exportação/importação, além da paleta de nós.
- **Falha:** página não carrega, fica em branco ou sem a paleta de nós.
- **Interrupção:** página não carrega em 5 minutos, mesmo após repetir P6 uma vez. Execute P14 e pare (interrupção global).

## Teste mínimo — selo F (P8–P14)

F é atribuível se P6–P10 e P13 tiverem sucesso; P11 e P12 são opcionais para os autores, e falhas neles entram no relatório sem bloquear F. P8–P13 correspondem aos passos 4–9 do README.

### P8 — Criar o controlador c1 (passo 4)

- **Selo / reivindicação:** F; C1, C2.
- **Diretório:** VM, navegador.
- **Comando:** arrastar o ícone “Controller” da barra lateral esquerda para o centro da tela; na caixa de diálogo, selecionar “Default” e pressionar “Submit” (README.md:88).
- **Esperado (autores):** o controller é criado (README.md:88) e passa a ser selecionável como “c1” (README.md:90).
- **Evidência:** `P8_c1.png`.
- **Sucesso:** nó c1 visível no grafo.
- **Falha:** diálogo não abre, erro na tela ou nenhum nó criado.
- **Interrupção:** c1 não é criado em duas tentativas. Execute P14 e pare: o teste mínimo falhou.

### P9 — Gerar topologia Single com 2 hosts (passo 5)

- **Selo / reivindicação:** F; C1, C2, C4 (modelo Single).
- **Diretório:** VM, navegador.
- **Comando:** “Generate Topology”; no modal, “Topology Type” = Single, “Controller” = c1, “Hosts” = 2; “Submit” (README.md:90).
- **Esperado (autores):** topologia criada; dispositivos como ícones brancos, links verdes para conexões ativas e linha pontilhada cinza entre switch e controlador (artigo, p. 7). Pelo código, 1 switch e 2 hosts, cada host ligado ao switch (NetworkGraph.vue:512–522).
- **Evidência:** `P9_single.png`.
- **Sucesso:** s1, h1 e h2 no grafo, dois links verdes e associação pontilhada s1–c1.
- **Falha:** nós faltando, links cinza (a interface pinta de cinza quando a rede não está iniciada) ou erro.
- **Interrupção:** nenhum nó criado. Execute P14 e pare.

### P10 — Executar o pingall (passo 6)

- **Selo / reivindicação:** F; C2.
- **Diretório:** VM, navegador.
- **Comando:** “Run Pingall Test” e aguardar os resultados (README.md:92).
- **Esperado (autores):** os resultados aparecem (README.md:92). Pelo código, linhas no formato `h1->h2: 1/1, rtt min/avg/max/mdev … ms` (api.py:159).
- **Evidência:** `P10_pingall.png`.
- **Sucesso:** h1→h2 e h2→h1 com pacotes recebidos iguais aos enviados.
- **Falha:** recebidos = 0, mensagem “network must be started to run pingall” ou modal vazio. Repita uma vez antes de concluir falha, pois o primeiro pacote pode se perder enquanto o controlador instala as regras.
- **Interrupção:** modal não responde em 2 minutos. Execute P14 e pare.

### P11 — Teste com iperf (passo 7, opcional)

- **Selo / reivindicação:** F; C5 (apoio).
- **Diretório:** VM, painel WebShell.
- **Comando:** aba h1 → `iperf -s`; aba h2 → `iperf -c 10.0.0.1`; aguardar 1 minuto (README.md:94). Ao terminar, Ctrl+C na aba h1 para liberar o terminal.
- **Esperado (autores):** o teste se completa em cerca de 1 minuto (README.md:94). Os autores não descrevem a saída.
- **Evidência:** `P11_iperf_h1.png` e `P11_iperf_h2.png`.
- **Sucesso:** a aba h2 mostra o relatório do cliente com intervalo e taxa (Mbits/s ou Gbits/s); a aba h1 mostra a conexão aceita.
- **Falha:** `command not found`, `connection refused` ou aba sem saída.
- **Interrupção:** nenhuma (opcional). Registre e siga.

### P12 — Múltiplos controladores (passo 8, opcional)

- **Selo / reivindicação:** F; C3 (link criado com a emulação ativa).
- **Diretório:** VM, navegador e WebShell.
- **Comando:** seguir README.md:96 na ordem: arrastar novo “Controller” com type “Remote”, IP `127.0.0.1`, porta `6633`; “Generate Topology” Single, 2 hosts, controller c2; “Create Link” e arrastar de s1 para s2; aba c2 no WebShell → `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; “Run Pingall Test”.
- **Esperado (autores):** linha verde ligando s1 e s2 indica sucesso do link (README.md:96); o pingall testa a conexão.
- **Evidência:** `P12_c2.png`, `P12_link.png`, `P12_ryu.png`, `P12_pingall.png`.
- **Sucesso:** link s1–s2 verde sem reiniciar a rede; Ryu inicia; pingall entre h1–h4 com recebidos iguais aos enviados.
- **Falha:** link não fica verde; ou, com o Ryu ativo, pingall com perda entre as duas metades.
- **Interrupção:** a criação do controlador remoto pode travar a requisição por até 60 s enquanto o Mininet testa a porta (comentário em api.py:205); aguarde 90 s antes de julgar. Se `ryu-manager` não existir (ver P5), pare este passo após o link: instalar o Ryu (README.md:77) é instrução da instalação manual, não da VM. Se a interface travar, repita P6 e refaça P8–P9 antes de P13.

### P13 — Exportar a topologia (passo 9)

- **Selo / reivindicação:** F.
- **Diretório:** VM, navegador; depois `~/Downloads`.
- **Comando:** “Export Topology (JSON)” e “Export Mininet Script” (README.md:98); em seguida `ls -lt ~/Downloads | head -5` e copiar os dois arquivos mais recentes para `~/evidencias/` com os nomes `P13_topologia.json` e `P13_script.py`.
- **Esperado (autores):** um JSON com a configuração da topologia atual e um script Mininet para executar fora do Mininet-GUI (README.md:98).
- **Evidência:** `P13_topologia.json`, `P13_script.py`.
- **Sucesso:** o JSON tem as chaves `switches`, `hosts`, `controllers` e `links` com os nós do grafo (como example\_network\_export.json); o script contém `addController`, `addSwitch`, `addHost` e `addLink` (como example\_network\_export.py).
- **Falha:** nenhum download, arquivo vazio ou nós ausentes.
- **Interrupção:** nenhuma. Não execute o script exportado com a interface ativa: ele criaria uma segunda rede Mininet na mesma VM.

### P14 — Coletar logs \[NÃO DOCUMENTADO\]

- **Justificativa:** run.sh:23–24 informa onde ficam os logs, mas os autores não pedem para coletar. Os logs são a única evidência do lado do servidor para explicar qualquer falha de F ou R.
- **Selo / reivindicação:** F e R.
- **Diretório:** VM, `/home/mininet/mininet-gui`.
- **Comando:**

```bash
cd /home/mininet/mininet-gui
sudo cp mininet-gui-backend/nohup.out ~/evidencias/P14_backend.log
cp mininet-gui-frontend/nohup.out ~/evidencias/P14_frontend.log
cp mininet-gui-frontend/.env ~/evidencias/P14_env.txt
sudo chown mininet:mininet ~/evidencias/P14_*
grep -ciE 'error|traceback' ~/evidencias/P14_backend.log
```

- **Esperado:** arquivos de log existentes; `.env` com `VITE_BACKEND_URL` e `VITE_BACKEND_WS_URL` (run.sh:16–17).
- **Evidência:** os três arquivos `P14_*`.
- **Sucesso:** logs copiados; tracebacks, se houver, correlacionados aos passos.
- **Falha:** logs ausentes (o backend pode não ter iniciado).
- **Interrupção:** nenhuma. Repita este passo ao final de P28.

## Selo R — um bloco por reivindicação (P15–P28)

R é atribuído se C4 (P19–P22, os três modelos) e C5 (P23–P24) tiverem sucesso; qualquer falha nelas, confirmada após uma repetição, leva a “Não atribuir”. C1, C2, C3 e C6 são registradas para o relatório e para F, sem decidir R (reivindicacoes.md).

### C1 — Interface web com grafo interativo

Reutiliza P7, P8, P9 e o link de P12. C1 é reproduzida se os elementos criados aparecem no grafo (P8–P9) e respondem a uma ação (P15).

#### P15 — Mover um nó no grafo \[NÃO DOCUMENTADO\]

- **Justificativa:** o resultado esperado de C1 inclui elementos “respondendo às ações”, e o README só descreve criação. Arrastar é a interação básica do módulo Network Manipulation (artigo, p. 5).
- **Selo / reivindicação:** R (relatório); C1.
- **Diretório:** VM, navegador.
- **Comando:** clicar em s1, arrastar para outra posição e soltar.
- **Esperado (autores):** manipulação visual da topologia em grafo dinâmico (artigo, p. 3, §3).
- **Evidência:** `P15_antes.png`, `P15_depois.png`.
- **Sucesso:** o nó acompanha o mouse, os links o seguem e a posição se mantém após soltar.
- **Falha:** o nó não se move ou volta à posição anterior.
- **Interrupção:** nenhuma.

### C2 — Emulação integrada

Não há passo novo. C2 é reproduzida se P9 mostra os nós com links verdes (rede iniciada) e P10 exibe o pingall na interface sem perda. P11 e P12 reforçam, com tráfego real e um segundo controlador.

### C3 — Modificação da topologia em tempo real

A criação com a rede ativa é coberta por P12 (README.md:96, opcional). A remoção não está no README; P16–P17 a verificam. C3 é reproduzida se P12 e P16–P17 tiverem sucesso sem uso de “Reset Topology”.

#### P16 — Remover nó e link com a emulação ativa \[NÃO DOCUMENTADO\]

- **Justificativa:** C3 reivindica criar **e remover** nós e links sem reiniciar (artigo, p. 5, §3); o README só cobre criação. O botão “Delete Selected” aparece na interface (artigo, Fig. 2), mas seu uso não é descrito.
- **Selo / reivindicação:** R (relatório); C3.
- **Diretório:** VM, navegador e WebShell.
- **Comando:** na aba h1 do WebShell, `echo antes-remocao`. No grafo, selecionar h2 e clicar “Delete Selected”. Se P12 criou o link s1–s2, selecioná-lo e clicar “Delete Selected”.
- **Esperado (autores):** nós e links removidos em tempo de execução, sem interromper ou reiniciar a emulação (artigo, p. 5).
- **Evidência:** `P16_antes.png`, `P16_depois.png`.
- **Sucesso:** h2 e seu link somem do grafo; o link s1–s2 some, quando existir.
- **Falha:** o elemento permanece, aparece erro ou a interface recarrega a rede.
- **Interrupção:** a interface trava por mais de 2 minutos. Execute P14 e siga para P18.

#### P17 — Confirmar que a emulação seguiu ativa \[NÃO DOCUMENTADO\]

- **Justificativa:** o resultado esperado de C3 é “rede alterada enquanto a emulação continua ativa” (reivindicacoes.md), e o README não diz como verificar isso.
- **Selo / reivindicação:** R (relatório); C3.
- **Diretório:** VM, navegador e WebShell.
- **Comando:** “Run Pingall Test” sem usar “Reset Topology”; na aba h1, `echo depois-remocao`.
- **Esperado:** pingall sem linhas de h2. Se o link s1–s2 foi removido, os pares entre h1 e h3/h4 falham, e isso é o esperado.
- **Evidência:** `P17_pingall.png`, `P17_h1.png`.
- **Sucesso:** pingall executa e não lista h2; a aba h1 ainda mostra `antes-remocao` acima de `depois-remocao`, ou seja, a sessão não foi derrubada.
- **Falha:** h2 ainda listado, erro “network must be started” ou sessão h1 perdida.
- **Interrupção:** nenhuma.

### C4 — Geração automatizada (Single, Linear, Tree)

Procedimento dos autores: “Generate Topology”, tipo (Single, Linear ou Tree) e número de dispositivos (README.md:105–108). C4 é reproduzida somente se os três modelos tiverem as contagens esperadas em P22.

#### P18 — Limpar a topologia antes de cada modelo \[NÃO DOCUMENTADO\]

- **Justificativa:** o README não diz se cada modelo deve partir de grafo vazio. Sem limpar, os nós se acumulam e a contagem de P22 fica ambígua. O reset também apaga os controladores (api.py:134), por isso c1 é recriado.
- **Selo / reivindicação:** R; C4.
- **Diretório:** VM, navegador.
- **Comando:** se o Ryu de P12 estiver rodando, Ctrl+C na aba c2. “Reset Topology” → confirmar o diálogo “Are you sure you want to reset the topology?” → repetir P8 (c1 “Default”). Executar antes de P19, P20 e P21.
- **Esperado:** grafo vazio e, depois, apenas c1.
- **Evidência:** `P18_reset_<modelo>.png`.
- **Sucesso:** nenhum nó além de c1.
- **Falha:** nós remanescentes ou erro.
- **Interrupção:** reset falha duas vezes. Execute P14, repita P6 (run.sh:3 encerra o backend anterior) e P7–P8.

#### P19 — Gerar Single

- **Selo / reivindicação:** R; C4 (Single).
- **Diretório:** VM, navegador.
- **Comando:** “Generate Topology” → Single, Controller c1, “Hosts” = 4 → “Submit” (README.md:107–108). Depois “Export Topology (JSON)” (README.md:98) e copiar o arquivo para `~/evidencias/P19_single.json`.
- **Valores \[NÃO DOCUMENTADO\]:** o README não fixa quantidades. Usar 4, e não os 2 de P9, mostra que a contagem acompanha a entrada. O README fala em “OK”; o botão se chama “Submit” (TopologyForm.vue:43).
- **Esperado (autores):** topologia do tipo escolhido com o número de dispositivos escolhido (README.md:107–108). Derivado do código: 1 switch, 4 hosts, 4 links.
- **Evidência:** `P19_single.png`, `P19_single.json`.
- **Sucesso:** contagens confirmadas em P22.
- **Falha:** contagem diferente ou erro.
- **Interrupção:** geração não termina em 2 minutos. Execute P14, registre e siga para P18 do próximo modelo.

#### P20 — Gerar Linear

- **Selo / reivindicação:** R; C4 (Linear).
- **Diretório:** VM, navegador.
- **Comando:** após P18, “Generate Topology” → Linear, Controller c1, “Switches” = 3, “Hosts per switch” = 2 → “Submit”. Exportar o JSON como em P19 para `~/evidencias/P20_linear.json`.
- **Valores \[NÃO DOCUMENTADO\]:** o README fala em “número de dispositivos”, mas o formulário Linear pede dois campos (TopologyForm.vue:25–30).
- **Esperado (autores):** README.md:107–108. Derivado do código (NetworkGraph.vue:524–551): 3 switches em cadeia, 6 hosts, 8 links (6 host–switch e 2 switch–switch).
- **Evidência:** `P20_linear.png`, `P20_linear.json`.
- **Sucesso:** contagens confirmadas em P22.
- **Falha:** contagem diferente, cadeia quebrada ou erro.
- **Interrupção:** como em P19.

#### P21 — Gerar Tree

- **Selo / reivindicação:** R; C4 (Tree).
- **Diretório:** VM, navegador.
- **Comando:** após P18, “Generate Topology” → Tree, Controller c1, “Layers” = 2, “Fanout” = 2 → “Submit”. Exportar para `~/evidencias/P21_tree.json`.
- **Valores \[NÃO DOCUMENTADO\]:** o formulário Tree pede profundidade e fanout, não número de dispositivos (TopologyForm.vue:35–40).
- **Esperado (autores):** README.md:107–108. Derivado do código (NetworkGraph.vue:553–585): 3 switches (raiz e 2 filhos), 4 hosts, 6 links.
- **Evidência:** `P21_tree.png`, `P21_tree.json`.
- **Sucesso:** contagens confirmadas em P22. Mantenha esta topologia para C5 e C6.
- **Falha:** contagem diferente, hierarquia errada ou erro.
- **Interrupção:** como em P19.

#### P22 — Contar nós e links nos JSON exportados \[NÃO DOCUMENTADO\]

- **Justificativa:** contar no grafo a olho é sujeito a erro; a exportação JSON é documentada (README.md:98), mas a contagem não.
- **Selo / reivindicação:** R; C4.
- **Diretório:** VM, `~/evidencias`.
- **Comando:**

```bash
cd ~/evidencias
for f in P19_single.json P20_linear.json P21_tree.json; do
  python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(sys.argv[1], {k: len(d.get(k, [])) for k in ('controllers','switches','hosts','links')})" "$f"
done | tee P22_contagem.txt
```

- **Esperado (derivado do código):**

| Modelo | Entrada | controllers | switches | hosts | links |
| --- | --- | --- | --- | --- | --- |
| Single | Hosts = 4 | 1 | 1 | 4 | 4 |
| Linear | 3 switches, 2 hosts/switch | 1 | 3 | 6 | 8 |
| Tree | Layers = 2, Fanout = 2 | 1 | 3 | 4 | 6 |

- **Evidência:** `P22_contagem.txt`.
- **Sucesso:** as três linhas iguais à tabela e coerentes com as capturas de P19–P21.
- **Falha:** qualquer divergência. C4 não é reproduzida.
- **Interrupção:** nenhuma.

### C5 — Terminal dos nós via WebShell

Procedimento dos autores: criar ao menos um nó, abrir a aba dele no painel “Webshell” e executar comandos no namespace do nó (README.md:110–114). Usa a topologia Tree de P21. C5 é reproduzida se P23 e P24 tiverem sucesso; P25 e P11 são apoio.

#### P23 — Abrir o terminal de um host

- **Selo / reivindicação:** R; C5.
- **Diretório:** VM, painel WebShell.
- **Comando:** clicar na aba de um host (ex.: h1) e pressionar Enter (README.md:112–113).
- **Esperado (autores):** terminal bash daquele nó (README.md:114); a Fig. 2 do artigo mostra um prompt `root@…#`.
- **Evidência:** `P23_aba_h1.png`.
- **Sucesso:** prompt bash na aba do nó.
- **Falha:** aba sem prompt ou mensagem “Error: node … not found.” (api.py:470).
- **Interrupção:** sem prompt em 30 s, mesmo após trocar de aba e voltar. Execute P14; C5 não é reproduzida.

#### P24 — Executar um comando no namespace do nó \[NÃO DOCUMENTADO\]

- **Justificativa:** o README manda “executar comandos” sem citar nenhum. `ip addr show` é o comando exibido na Fig. 2 do artigo e distingue o namespace do host do da VM. Não use `hostname`: o Mininet não isola o nome de host, e a saída seria a mesma da VM.
- **Selo / reivindicação:** R; C5.
- **Diretório:** VM, painel WebShell.
- **Comando:** na aba h1, `ip addr show`; repetir na aba h2.
- **Esperado:** em cada aba, apenas `lo` e a interface do próprio nó (`h1-eth0`, `h2-eth0`) com endereço 10.0.0.x, como na Fig. 2.
- **Evidência:** `P24_h1.png`, `P24_h2.png`.
- **Sucesso:** saída exibida na aba do nó selecionado, com interfaces distintas entre h1 e h2.
- **Falha:** sem saída, ou interfaces da VM (ex.: `enp0s3`) em vez das do nó.
- **Interrupção:** nenhuma.

#### P25 — Comando de rede a partir do nó \[NÃO DOCUMENTADO\]

- **Justificativa:** confirma que o terminal opera na rede emulada, além de exibir saída. O único exemplo dos autores (iperf, P11) foi executado na topologia Single.
- **Selo / reivindicação:** R (apoio); C5.
- **Diretório:** VM, painel WebShell.
- **Comando:** na aba h1, `ping -c 3 <IP de h2 visto em P24>`.
- **Esperado:** 3 pacotes transmitidos e 3 recebidos.
- **Evidência:** `P25_ping.png`.
- **Sucesso:** 0% de perda.
- **Falha:** 100% de perda ou “Network is unreachable”.
- **Interrupção:** nenhuma.

### C6 — Regras de fluxo OpenFlow

O README não traz procedimento para C6, então todos os passos são \[NÃO DOCUMENTADO\]. C6 não decide R. A análise do código indica só leitura da tabela (api.py:363, `dump-flows`), sem criação ou remoção pela interface; estes passos confirmam ou refutam isso.

#### P26 — Visualizar a tabela de fluxo \[NÃO DOCUMENTADO\]

- **Justificativa:** o artigo reivindica visualização (p. 5, Flow Rule Editor), mas o README não diz como acessá-la. No código, o duplo clique abre os dados do nó (NetworkGraph.vue:277–279), com a aba “Flow Table”.
- **Selo / reivindicação:** relatório; C6.
- **Diretório:** VM, navegador.
- **Comando:** “Run Pingall Test” (para gerar fluxos); duplo clique em s1 → aba “Flow Table”.
- **Esperado (autores):** visualização das regras de fluxo do switch (artigo, p. 5).
- **Evidência:** `P26_flowtable.png`.
- **Sucesso:** tabela com linhas (cookie, duration, table, n\_packets, n\_bytes, idle\_timeout, priority, match fields).
- **Falha:** aba ausente ou vazia após o pingall.
- **Interrupção:** nenhuma.

#### P27 — Procurar criação e remoção de regras na interface \[NÃO DOCUMENTADO\]

- **Justificativa:** o artigo reivindica “criação e remoção de regras de fluxo OpenFlow nos switches” (p. 5), e o README não indica onde.
- **Selo / reivindicação:** relatório; C6.
- **Diretório:** VM, navegador.
- **Comando:** inspecionar barra lateral, modal “Node Info” de s1 (todas as abas) e clique direito sobre s1.
- **Esperado (autores):** editor que cria e remove regras.
- **Evidência:** `P27_modal.png`, `P27_barra.png`.
- **Sucesso:** opção encontrada; uma regra criada aparece na Flow Table e some ao ser removida.
- **Falha:** nenhuma opção encontrada. C6 fica “não reproduzível” quanto a criação e remoção.
- **Interrupção:** nenhuma.

#### P28 — Contraprova da visualização com regra inserida fora da interface \[NÃO DOCUMENTADO\]

- **Justificativa:** separa o que funciona (visualização) do que falta (editor). Não conta como reprodução da criação pela interface.
- **Selo / reivindicação:** relatório; C6.
- **Diretório:** VM, painel WebShell, aba s1.
- **Comando:** `ovs-ofctl add-flow s1 "priority=1,actions=normal"`; reabrir a Flow Table de s1; depois `ovs-ofctl --strict del-flows s1 "priority=1"` e reabrir. Se aparecer erro de negociação de versão, acrescente `-O OpenFlow13`.
- **Esperado:** a linha com priority 1 aparece após a inserção e some após a remoção.
- **Evidência:** `P28_add.png`, `P28_del.png`.
- **Sucesso:** a visualização reflete as duas mudanças.
- **Falha:** a tabela não muda.
- **Interrupção:** nenhuma. Ao final, repita P14.

## Tempo estimado

O roteiro completo leva de 1h45 a 3h25; o download do `.ova` é a maior incerteza, pois o README não informa o tamanho do arquivo.

| Fase | Passos | Tempo (min) |
| --- | --- | --- |
| Hospedeiro e download | P1–P2 | 20–65 |
| Importação, boot e login | P3–P4 | 7–20 |
| Versões e início da ferramenta | P5–P7 | 8–10 |
| Teste mínimo obrigatório | P8–P10, P13–P14 | 10–15 |
| Teste mínimo opcional | P11–P12 | 8–13 |
| C1 e C3 | P15–P17 | 7–12 |
| C4 (três modelos e contagem) | P18–P22 | 20–30 |
| C5 | P23–P25 | 5–10 |
| C6 | P26–P28 | 10–15 |
| Organização das evidências | — | 10–15 |

Não está incluído o tempo de contato com os autores em caso de falha.

## Tabela de todos os passos

São 28 passos: 16 seguem procedimentos dos autores e 12 são \[NÃO DOCUMENTADO\]; os obrigatórios para decidir F são P6–P10 e P13, e para R são P18–P24.

| Passo | Selo | Reivindicação | Ação | Fonte | Documentado | Decide |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | F | — | Conferir VirtualBox e disco | README.md:32, 37 | Sim | Pré-requisito |
| P2 | F | — | Baixar o `.ova` | README.md:53 | Sim | Pré-requisito |
| P3 | F | — | Importar a VM | README.md:55 | Sim | Pré-requisito |
| P4 | F | — | Iniciar e fazer login | README.md:57, 82 | Sim | Pré-requisito |
| P5 | F, R | — | Conferir versão e dependências | Índice de artefato.txt | Não | Ressalva |
| P6 | F | — | Executar `mininet_gui` | README.md:84 | Sim | F |
| P7 | F | C1 | Abrir a URL | README.md:86 | Sim | F |
| P8 | F | C1, C2 | Criar c1 Default | README.md:88 | Sim | F |
| P9 | F | C1, C2, C4 | Gerar Single com 2 hosts | README.md:90 | Sim | F |
| P10 | F | C2 | Pingall | README.md:92 | Sim | F |
| P11 | F | C5 | iperf h1↔h2 | README.md:94 | Sim (opcional) | Relatório |
| P12 | F | C3 | Segundo controlador e link s1–s2 | README.md:96 | Sim (opcional) | Relatório |
| P13 | F | — | Exportar JSON e script | README.md:98 | Sim | F |
| P14 | F, R | — | Coletar logs | run.sh:23–24 | Não | Evidência |
| P15 | R | C1 | Mover um nó | Artigo p. 3 e 5 | Não | Relatório |
| P16 | R | C3 | Remover h2 e link s1–s2 | Artigo p. 5; Fig. 2 | Não | Relatório |
| P17 | R | C3 | Pingall e sessão h1 após remoção | reivindicacoes.md | Não | Relatório |
| P18 | R | C4 | Reset e recriar c1 | api.py:134 | Não | R (preparo) |
| P19 | R | C4 | Gerar Single (4 hosts) | README.md:107–108 | Sim (valores não) | R |
| P20 | R | C4 | Gerar Linear (3 × 2) | README.md:107–108 | Sim (valores não) | R |
| P21 | R | C4 | Gerar Tree (2 camadas, fanout 2) | README.md:107–108 | Sim (valores não) | R |
| P22 | R | C4 | Contar nós e links nos JSON | README.md:98 (exportação) | Não | R |
| P23 | R | C5 | Abrir aba do host no WebShell | README.md:112–113 | Sim | R |
| P24 | R | C5 | `ip addr show` em h1 e h2 | Artigo, Fig. 2 | Não | R |
| P25 | R | C5 | `ping` a partir de h1 | — | Não | Apoio |
| P26 | — | C6 | Ver Flow Table de s1 | NetworkGraph.vue:277–279 | Não | Relatório |
| P27 | — | C6 | Procurar editor de regras | Artigo p. 5 | Não | Relatório |
| P28 | — | C6 | Inserir e remover regra via `ovs-ofctl` | — | Não | Relatório |
