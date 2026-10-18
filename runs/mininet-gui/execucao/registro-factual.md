# Registro factual da execução de referência — Mininet-GUI (SBRC 2025)

**Data da execução:** 2026-10-17, das 18:34:47Z (restauração do snapshot) às 19:03:35Z (VM desligada). Todas as horas estão em UTC. **Execução:** única, feita pelo aluno, com a operação automatizada por um agente de software autorizado por ele (ver "Modo de operação").
**Roteiro executado:** união dos planos de execução de três revisores, com cada passo marcado como documentado pelos autores (com a fonte) ou [NÃO DOCUMENTADO]. Os passos [NÃO DOCUMENTADO] foram executados como desvios declarados (D2) e aparecem em seção separada.
**Documentação avaliada:** `README.md` do commit `465648a4425a4457af0348ab951cf7f71d37a86f`. As citações "README:N" usam a numeração de linhas desse arquivo.

Este registro descreve fatos observados. Ele não contém avaliação dos selos.

## 1. Ambiente

### 1.1 Host

| Item | Valor |
|---|---|
| Sistema | Windows 11 Home, build 26300, 64 bits |
| CPU | Intel Core i5-13450HX, 10 núcleos e 16 threads |
| RAM | 16.069 MB no total. Antes de ligar a VM havia cerca de 753 MB livres; o `VBox.log` registrou "Host RAM: 16068MB (15.6GB) total, 725MB available". Outros programas estavam abertos, entre eles contêineres Docker de outra tarefa. |
| Disco | 660 GB livres no volume da VM |
| Hipervisor | Oracle VirtualBox **7.1.6 r167084**, a mesma versão pedida em README:37 |
| Motor de execução | O Hyper-V do Windows está ativo e o VT-x não fica disponível para o VirtualBox. O `VBox.log` registra "HM: HMR3Init: Attempting fall back to NEM: VT-x is not available" e "NEM: NEMR3Init: Snail execution mode is active!". A VM rodou sobre a API do Hyper-V (NEM), não em VT-x nativo. |
| Navegador | Microsoft Edge 155.0.4283.45 no host, em modo headless, com janela de 1600×1000 |

### 1.2 Máquina virtual

| Item | Valor |
|---|---|
| Origem | release `v0.0.1` "VM SBRC 2025" do repositório dos autores (`Mininet-GUI-VM-SBRC-2025.zip`, 1.303.516.409 bytes, SHA-256 `3a484c2d…5364e4bc`; OVA SHA-256 `9018352d…99fc7455`, cujo manifesto SHA-1 interno confere). O link do Google Drive em README:53 abria a página "O arquivo que você solicitou não existe" quando foi consultado em 15/10/2026. |
| Nome da imagem | `Mininet-GUI-VM-SBRC-2025.ova`. README:55 cita outro nome, `Mininet-GUI-Desktop-VM-SBRC-2025.ova`. |
| Estado inicial | snapshot `02-apos-identificacao` (VM importada, ajustada e já iniciada uma vez só para identificação, sem ter executado `mininet_gui`) |
| Recursos | **8192 MB de RAM**, 2 vCPUs, disco de 8 GiB (3,2 GB livres), rede host-only (`192.168.56.101`), sem acesso à Internet. A OVA vinha com 1536 MB e 1 vCPU. |
| SO | Ubuntu 20.04.1 LTS, kernel `5.4.0-42-generic #46-Ubuntu`, x86_64 |
| Interface gráfica | não há; a VM inicia em console texto (tty1). O acesso foi por SSH com o usuário e a senha publicados pelos autores (`mininet`/`mininet`). |
| Versões | Mininet 2.3.0; Open vSwitch 2.13.1; Python 3.8.5; Node v18.20.7 e npm 10.8.2 (via nvm, em shell interativo); vite 4.5.9; iperf 2.0.13; `ryu-manager` **ausente** (não há módulo `ryu`) |
| Pico de memória da VM | 257 MB usados de 7962 MB (`free -m` às 19:02:53Z) |
| Código na VM | `/home/mininet/mininet-gui` em **`be68302a9d3e17acf740d002090f7191098ac03d`** (`v0.0.1-2-gbe68302`, branch `sbrc2025`), com a árvore limpa |

### 1.3 Commit da VM × documentação avaliada

O commit da VM (`be68302`) é ancestral do commit da documentação avaliada (`465648a4`), com 16 commits entre os dois.

- Os 41 arquivos do projeto na VM são idênticos aos de `be68302`.
- Entre `be68302` e `465648a4` mudam apenas `README.md`, `run.sh` e dois arquivos de exemplo (`example_network_export.json` e `.py`, que não existem na VM).
- **Nenhum arquivo de `mininet-gui-backend/` ou `mininet-gui-frontend/` difere.**
- No `run.sh`, a versão `465648a4` acrescenta `nvm use 18.20.7 ;` antes de `nohup npm run dev &`. Na VM, o Node 18 já vem do `~/.bashrc` em shell interativo.

### 1.4 Requisitos do README × ambiente usado

| Requisito | Fonte | Valor usado |
|---|---|---|
| VirtualBox 7.1.6 r167084 | README:37 | 7.1.6 r167084 |
| RAM da VM: "Mínimo de 8GB" | README:38 | 8192 MB |
| RAM da VM: "no mínimo 2GB" e "um core de CPU" | README:103 | 8192 MB, 2 vCPUs |
| Host de demonstração: i5-10300H, 8 GB, Windows 11 Home, 80 GB livres | README:26-32 | i5-13450HX, 16 GB, Windows 11 Home, 660 GB livres; Hyper-V ativo (NEM). O README não fala de Hyper-V. |
| VM `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (Google Drive) | README:53-55 | `Mininet-GUI-VM-SBRC-2025.ova` da release `v0.0.1` (link do Drive inativo) |
| Navegador "dentro da VM" | README:86 | navegador do host via rede host-only. A VM da release não tem ambiente gráfico; o texto da release manda abrir a URL "em um navegador", com o exemplo `http://192.168.56.101:5173`. |
| Terminal com Ctrl+Alt+T | README:84 | sessão SSH com bash interativo (carrega o alias `mininet_gui` e o nvm do `~/.bashrc`) |

### 1.5 Modo de operação e registro

- **Terminal da VM:** uma única sessão bash interativa gravada com `script -t`, pelo script `gravar-sessao.sh`, das 18:36:48Z às 19:02:5xZ. Arquivos: [`terminal.txt`](terminal.txt) (SHA-256 `6ffa9cc8…12865`) e [`tempo.txt`](tempo.txt) (`fa7c8e50…a2976`), que podem ser reproduzidos com `scriptreplay -t tempo.txt terminal.txt`. Os comandos foram enviados à sessão por um FIFO. Cada comando é cercado por marcadores `[passo=… inicio=…]` e `[passo=… saida=<código> fim=…]`.
- **Interface web:** operada no Edge headless do host pelo Chrome DevTools Protocol (script `evidencias/ferramentas/cdp.mjs`).
  - Cliques, arrastes (inclusive o arraste HTML5 da paleta), roda do mouse e teclas foram enviados como eventos de entrada do navegador (`Input.dispatch*`).
  - Nos campos `<select>`, o valor foi atribuído por JavaScript, com o disparo dos eventos `input` e `change`.
  - As posições dos nós e as listas de nós e arestas foram lidas do componente Vue da página, só para leitura.
  - Cada captura recebeu, só no momento da captura, um carimbo com a hora UTC e o rótulo do passo, no canto inferior direito.
- **Evidências:** [`evidencias/telas/`](evidencias/telas/) (65 PNG, SHA-256 em `telas.sha256`), [`evidencias/saidas-interface.txt`](evidencias/saidas-interface.txt) (texto lido da página em cada passo), [`evidencias/exportados/`](evidencias/exportados/), [`evidencias/vm/`](evidencias/vm/) (gravação, logs `nohup.out` do backend e do frontend, conferidos por SHA-256 após a transferência) e [`evidencias/host/`](evidencias/host/) (comandos do VirtualBox, trechos do `VBox.log`, dados do host).

## 2. Tabela de passos — procedimento documentado pelos autores

Status: **sucesso** (esperado observado), **falha** (esperado não observado), **inconclusivo**, **bloqueado**. "Esperado" é o texto dos autores; quando eles não o fixam, a tabela diz isso.

| Passo | Origem | Ação | Esperado | Observado | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| E02 | autores (README:53; release `v0.0.1`) | Obter a VM | arquivo `.ova` da VM | link do README inativo; ZIP/OVA da release dos autores obtido e íntegro (CRC e manifesto conferem) | `ambiente/ambiente.md` (preparação) | sucesso | D1: fonte alternativa dos próprios autores |
| E04 | autores (README:55) | Importar a OVA | VM importada | importada sem erro | idem | sucesso | D0 |
| E06 | autores (README:57, 82) | Iniciar a VM e entrar | sessão aberta | boot até o login em ~95 s (18:34:48Z → SSH às 18:36:23Z); console texto, sem área de trabalho; login por SSH | `telas/20261017T183635Z-E06-console-boot.png`; `evidencias/host/vbox-comandos.txt` | sucesso | D1: SSH em vez de terminal gráfico |
| E09 | autores (README:84) | `mininet_gui` | "mostrará … uma URL" (README:86) | código de saída 0 em 0,2 s (18:41:10.720–.942Z); imprimiu "Mininet-GUI bootstrap complete" e `http://192.168.56.101:5173`; uvicorn em :8000 e vite em :5173 ("VITE v4.5.9 ready in 4713 ms") às 18:41:32Z | `terminal.txt` (passos E09, E09-verif); `vm/frontend-nohup.txt`, `vm/backend-nohup.txt` | sucesso | D0 |
| E10 | autores (README:86; release, Teste mínimo passo 3) | Abrir a URL impressa | interface web | página "Mininet-GUI" com barra lateral (Topology Controls, Actions, Export/Import, Nodes Palette), área do grafo e painel "WebShell" | `telas/…184317Z-E10-interface-1600x1000.png` | sucesso | D1: navegador do host |
| E11 | autores (README:88) | Arrastar "Controller", "Default", "Submit" | controlador criado | formulário "Controller Type: Default/Remote"; nó `c1` no grafo e aba `C1` no WebShell (18:43:26–18:43:42Z) | `telas/…184332Z-E11-dialogo-controller.png`, `…184341Z-E11-c1-criado.png` | sucesso | D0 |
| E12 | autores (README:90) | "Generate Topology": Single, c1, Hosts 2, "Submit" | topologia gerada | `s1`, `h1`, `h2`; links `s1`–`h1` e `s1`–`h2` em verde; `s1`–`c1` cinza tracejado; abas C1 S1 H1 H2; rede iniciada (18:43:51–18:44:11Z) | `telas/…184355Z-E12-formulario-single.png`, `…184411Z-E12-topologia-single.png` | sucesso | D0 |
| E13 | autores (README:92) | "Run Pingall Test" | "aguarde os resultados aparecerem" | em menos de 2 s, tabela "Pingall Results": h1→h2 e h2→h1, 1 enviado/1 recebido cada (RTT 24,340 e 4,674 ms) | `telas/…184422Z-E13-pingall.png`; `saidas-interface.txt` | sucesso | D0 |
| E14 | autores (README:94, opcional) | aba `h1`: `iperf -s`; aba `h2`: `iperf -c 10.0.0.1`; aguardar 1 min | teste completa em 1 min | `h2`: "0.0-10.0 sec 7.71 GBytes 6.62 Gbits/sec"; `h1` registrou a conexão de 10.0.0.2 com o mesmo valor; servidor encerrado com Ctrl+C (18:46:25–18:47:49Z). Uma tentativa anterior (18:44:37–18:46:00Z) não digitou nada porque o modal do Pingall continuava aberto sobre a página; ver Limitações. | `telas/…184629Z-E14-iperf-servidor-h1.png`, `…184738Z-E14-iperf-cliente-h2.png`, `…184742Z-E14-iperf-servidor-h1-relatorio.png` | sucesso | D0 |
| E16 | autores (README:96, opcional) | Controller Remote 127.0.0.1:6633 (`c2`); Single, 2 hosts, c2; "Create Link" `s1`→`s2`; na aba `c2`, `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; Pingall | "linha verde conectando os dois nós"; Ryu iniciado; teste de conexão | `c2 <127.0.0.1:6633>` criado em 3 s; `s2`, `h3`, `h4` gerados **nas mesmas coordenadas de tela** de `s1`, `h1`, `h2`, sobrepostos; os três nós foram afastados arrastando-os no grafo; link `s1`–`s2` criado em verde (`#00aa00ff`); na aba `c2`, "Command 'ryu-manager' not found, but can be installed with: apt install python3-ryu"; Pingall (~30 s): h1↔h2 com 1/1, os outros 10 pares com 0 recebidos | `telas/…184824Z-E16-single-c2.png`, `…184844Z-E16-nos-afastados.png`, `…184928Z-E16-link-s1-s2.png`, `…184945Z-E16-ryu-c2.png`, `…185024Z-E16-pingall-resultado.png` | falha (Ryu ausente na VM; sem conectividade entre as duas topologias) | D1: nós afastados à mão para permitir o arraste |
| E17 | autores (README:98) | "Export Topology (JSON)" e "Export Mininet Script" | JSON da topologia e script do Mininet | `network_export.json` (2514 bytes; 2 switches, 4 hosts, 2 controladores, 5 links) e `network_export.py` (1105 bytes; `Mininet(...)`, `addController` c1 e `c2` RemoteController 127.0.0.1:6633, 4 hosts com IP/MAC, 5 `addLink`, `CLI(net)`); o `.py` passa em `ast.parse` | `exportados/network_export.json` SHA-256 `b188381b6952ee5f901ac337a2e0a9d4a902bcc73b60da9dbf53fe29ea116866`; `exportados/network_export.py` SHA-256 `66eccd22d0d99459719eb298f4b14c54701ff0a3cb4e49e2b83bd6860a458b9d`; `telas/…185112Z-E17-apos-exportar.png` | sucesso | D0 (validação do JSON e da sintaxe: D2) |
| E19 | autores (README:107-108); quantidade escolhida pelos revisores | Single, c1, Hosts = 3 | topologia Single "com o número de dispositivos" escolhido | grafo: `s1`, `h1`–`h3`, 3 links host–switch + associação `s1`–`c1`; API: 1 switch, 3 hosts, 3 links (18:51:58–18:52:18Z) | `telas/…185210Z-E19-single3-formulario.png`, `…185217Z-E19-single3-grafo.png`; `terminal.txt` (E19-api) | sucesso | D0 (valor: D2) |
| E20 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 3, Hosts per switch 2 | topologia Linear com a quantidade escolhida | grafo: `s1`–`s2`–`s3` em cadeia, 2 hosts por switch (`h1`–`h6`), 8 links; API: 3 switches, 6 hosts, 8 links (18:52:35–18:52:55Z). Os hosts de cada switch aparecem empilhados e encobrem os rótulos `h1`, `h3`, `h5`. | `telas/…185248Z-E20-linear3x2-formulario.png`, `…185255Z-E20-linear3x2-grafo.png`; `terminal.txt` (E20-api) | sucesso | D0 (valores: D2) |
| E21 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 2, Hosts per switch 1 | idem | grafo e API: 2 switches, 2 hosts, 3 links (`s1`–`h1`, `s2`–`h2`, `s1`–`s2`) (18:53:13–18:53:34Z) | `telas/…185327Z-E21-…`, `…185334Z-E21-linear2x1-grafo.png`; `terminal.txt` (E21-api) | sucesso | D0 (valores: D2) |
| E22 | autores (README:107-108); quantidades escolhidas pelos revisores | Tree, c1, Layers 2, Fanout 2 | topologia Tree com a quantidade escolhida | grafo: raiz `s3`, filhos `s1` e `s2`, 2 hosts em cada (`h1`–`h4`), 6 links; API: 3 switches, 4 hosts, 6 links (18:53:44–18:54:05Z). Os hosts ficaram abaixo da área visível; a vista foi deslocada arrastando o fundo do grafo. | `telas/…185357Z-E22-tree2x2-formulario.png`, `…185404Z-E22-tree2x2-grafo.png`, `…185432Z-E22-tree2x2-grafo-deslocado.png`; `terminal.txt` (E22-api) | sucesso | D0 (valores: D2) |
| E24 | autores (README:112-114); comando escolhido pelos revisores (artigo p. 7, Fig. 2) | aba `h1` do WebShell: `ip addr show` | saída "no namespace daquele nó" | na aba `h1`: `lo` 127.0.0.1/8 e `h1-eth0@if40` 10.0.0.1/8, MAC 00:00:00:00:00:01 (18:54:41–18:54:48Z) | `telas/…185448Z-E24-h1-ip-addr.png`; `saidas-interface.txt` | sucesso | D0 (comando: D2) |

Tempo do teste mínimo (E09–E17): 18:41:10Z → 18:51:12Z. Tempo de C4 (E18–E23): 18:51:29Z → 18:54:32Z. Nenhum bloco chegou perto do limite de 2 h.

## 3. Passos [NÃO DOCUMENTADO] (desvios declarados, D2)

Todos foram propostos pelos revisores e não constam da documentação dos autores. São evidência complementar.

| Passo | Origem | Reivindicação | Ação | Esperado (revisores) | Observado | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|---|
| E01 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Registrar host, VirtualBox e recursos | requisitos registrados | ver seção 1 | `evidencias/host/host.txt`, `vbox-comandos.txt`, `vbox-execucao-trechos.txt` | sucesso | D2 |
| E03 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | SHA-256 da OVA | hash registrado | `9018352deec76c1ef47b15c0d6b7155fbd7ed090d34e8f97a0a302d299fc7455`; os autores não publicam hash | preparação | sucesso | D2 |
| E05 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Conferir e ajustar RAM/CPU | ≥ 8 GB | OVA com 1536 MB e 1 vCPU; ajustada para 8192 MB e 2 vCPUs | `vbox-comandos.txt` | sucesso | D2 |
| E07 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | `git rev-parse HEAD`, `status --short`, `describe` | commit registrado | `be68302a9d3e17acf740d002090f7191098ac03d`, árvore limpa, `v0.0.1-2-gbe68302`, ≠ `465648a4` (ver 1.3). O `git log` abriu o paginador e consumiu o caractere seguinte; o marcador de fim deste passo não foi gravado. | `terminal.txt` (E07) | sucesso | D2 |
| E08 | [NÃO DOCUMENTADO] proposto pelos revisores | pré-condição | Inspecionar `api.js` (linha 299) e o carregamento do nvm, sem corrigir | registrar | linha 299 de `mininet-gui-frontend/src/core/api.js` contém `}i`; nada foi corrigido; o frontend compilou e funcionou (E09–E32). `~/.bashrc` (linhas 120–122) carrega o nvm. | `terminal.txt` (E08) | sucesso | D2 |
| E15 | [NÃO DOCUMENTADO] proposto pelos revisores | apoio a C3 | `command -v ryu-manager`; `python3 -c "import ryu"` | caminho do Ryu | código 1, sem caminho; `ModuleNotFoundError: No module named 'ryu'` | `terminal.txt` (E15) | falha | D2 |
| E18 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | "Reset Topology" (diálogo confirmado) antes de cada modelo; recriar `c1` Default | grafo e API vazios | 5 resets (18:51:37Z, 18:52:26Z, 18:53:0xZ, 18:53:3xZ, 19:01:40Z); depois de cada um, grafo vazio e API com 0 controllers/switches/hosts/links | `telas/…185144Z-E18-reset-1.png`; `terminal.txt` (E18-*) | sucesso | D2 |
| E23 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | Contar nós e links pela API após cada modelo | contagens iguais às escolhidas | iguais nos 4 casos (ver E19–E22) | `terminal.txt` (E19-api … E22-api) | sucesso | D2 |
| E25 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h2`: `ip addr show` | `h2-eth0` com IP diferente do de `h1` | `h2-eth0@if41` 10.0.0.2/8, MAC 00:00:00:00:00:02 | `telas/…185455Z-E25-h2-ip-addr.png` | sucesso | D2 |
| E26 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h1`: `ping -c 2 10.0.0.2` | respostas | 2 transmitidos, 2 recebidos, 0% de perda | `telas/…185511Z-E26-h1-ping.png` | sucesso | D2 |
| E27 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | Comparar com o terminal da VM; nas abas, `readlink /proc/$$/ns/net` | namespaces distintos dos da VM | shell da aba `h1` no `net:[4026532228]`, o mesmo do processo `mininet:h1` (pid 3801); aba `h2` no `net:[4026532269]`, o mesmo de `mininet:h2` (pid 3803); shell da VM no `net:[4026531992]`. `ip -br addr` da VM mostra `eth0` 192.168.56.101 e as portas dos switches, sem `h1-eth0`/`h2-eth0`. | `telas/…185535Z-E27-h2-netns.png`, `…185537Z-E27-h1-netns.png`; `terminal.txt` (E27-vm, E27-ps) | sucesso | D2 |
| E28a | [NÃO DOCUMENTADO] proposto pelos revisores | C1 | Arrastar `h1` e recarregar a página | posição mantida | canvas: (50, 450) → (−205, 389); API `/hosts` gravou (−204,73; 388,86); após recarregar, (−204, 388). Uma tentativa anterior (18:55:49Z) partiu de coordenada errada da automação e não moveu o nó. | `telas/…185629Z-E28-depois-mover.png`, `…185640Z-E28-apos-reload.png`; `terminal.txt` (E28-api) | sucesso | D2 |
| E28b | [NÃO DOCUMENTADO] proposto pelos revisores | C1 (e adição para C3) | Soltar "Switch" e "Host" da paleta no grafo; "Create Link" `h5`→`s4`, `s4`→`s1`, `s4`→`c1`, com a rede em execução | nós e links aparecem | `s4` e `h5` criados sem formulário; links `h5`–`s4` e `s4`–`s1` em verde; associação `s4`–`c1` tracejada; API: 4 switches, 5 hosts, 8 links, `start=true`. O ponto em que o nó aparece fica ~250 px à direita do ponto onde foi solto. | `telas/…185658Z-E28-paleta-nos.png`, `…185723Z-E28-links-paleta.png`; `terminal.txt` (E28-api2) | sucesso | D2 |
| E29 | [NÃO DOCUMENTADO] proposto pelos revisores | C2 (e C3) | `curl /api/mininet/start` e `/hosts`; "Run Pingall Test" | `true`, hosts iguais aos do grafo; tabela | `true`; hosts h1–h5 (10.0.0.1–.5/8); Pingall: **20/20 pares** com 1/1, incluindo `h5`, criado com a rede em execução | `telas/…185739Z-E29-pingall.png`; `saidas-interface.txt` | sucesso | D2 |
| E30a | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o link `h2`–`s1`, "Delete Selected" | link some do grafo e da API | some do grafo e de `/links` (7 links); `start=true`; log: `DELETE /api/mininet/delete_link/h2/s1` 200 OK | `telas/…185805Z-E30-link-selecionado.png`, `…185808Z-E30-link-removido.png` | sucesso | D2 |
| E30b | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o nó `h4`, "Delete Selected" | nó some do grafo e da API | `h4` some do grafo, da lista de abas e de `/hosts` (4 hosts); `/links` **continua listando `['h4','s2']`**; log: `DELETE /api/mininet/delete_node/h4` 200 OK | `telas/…185819Z-E30-no-selecionado.png`, `…185830Z-E30-no-removido.png`; `terminal.txt` (E30-api-no) | sucesso (com resíduo em `/links`) | D2 |
| E30c | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | "Run Pingall Test" após as remoções | Pingall sem o nó removido | alerta "Network Error"; modal "No ping results available."; backend `POST /api/mininet/pingall` **500 Internal Server Error**, `AttributeError: 'NoneType' object has no attribute 'IP'` em `pingFull()` (api.py:157) | `telas/…190107Z-E30-pingall-apos-remocao.png`; `vm/backend-nohup.txt` (linhas 2517–2574) | falha | D2 |
| E30d | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Confirmar a emulação ativa: `/start`, reinícios no log, `ping -c 2 10.0.0.3` na aba `h1` | emulação ativa, sem reinício | `start=true`; "Creating network" aparece 10 vezes no log antes e depois das remoções (2 na partida + 2 por reset × 4 resets anteriores; nenhuma nova); `h1` alcança 10.0.0.3 com 0% de perda e mantém a interface `h1-eth0@if40` vista em E24 | `telas/…190130Z-E30-h1-ping-h3-apos-remocao.png`; `terminal.txt` (E30-depois) | sucesso | D2 |
| E31 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Reset; `c1`; Single 2 hosts; Pingall; duplo clique em `s1`; aba "Flow Table" | tabela com ao menos uma regra | modal "Node Info: s1" com abas Details e Flow Table; Flow Table com **5 regras** (prioridade 65535, idle timeout 60, campos de match ARP e ICMP entre 10.0.0.1 e 10.0.0.2), lidas cerca de 5 s após o Pingall | `telas/…190214Z-E31-node-info-s1.png`, `…190225Z-E31-flow-table-s1.png`; `saidas-interface.txt` | sucesso | D2 |
| E32 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Procurar no modal e na página um controle para inserir ou remover regra | controle presente, ou ausência registrada | controles do modal: "X", "Details", "Flow Table"; da página: Generate/Reset Topology, Create Link, Delete Selected, Run Pingall Test, Export/Import, ocultar barra, abas do WebShell. **Nenhum controle para criar ou remover regra de fluxo.** | `saidas-interface.txt` (E32); `telas/…190237Z-E32-modal-details.png` | falha (controle não encontrado) | D2 |

## 4. Resultados por reivindicação

Os resultados esperados vêm da lista de reivindicações entregue aos revisores. Nenhuma reivindicação tem valor numérico publicado pelos autores. Por isso não há diferenças absolutas nem relativas a calcular.

| ID | Resultado esperado | Passos | Observado |
|---|---|---|---|
| C1 | elementos criados pelo usuário representados no grafo e respondendo às ações | E10–E12 (autores); E28a–E28b (D2) | Controlador, switch, hosts e links criados pela interface aparecem no grafo e nas abas do WebShell. Um nó arrastado mantém a posição após recarregar a página. Nós soltos da paleta aparecem e podem ser ligados. Duas gerações sucessivas sem reset (E16) produziram nós sobrepostos nas mesmas coordenadas. |
| C2 | nós emulados e resultado de `pingall` exibido na interface | E12–E13 (autores); E29, E31 (D2) | Pingall exibido na interface: 2/2 pares (E13), 20/20 pares com 5 hosts (E29) e 2/2 pares (E31). A API informa `start=true`, e os hosts têm interfaces e IPs próprios. |
| C3 | rede alterada enquanto a emulação continua ativa | E16 (autores, opcional); E28b, E29, E30a–E30d (D2) | **Adição com a rede ativa:** segunda topologia, link `s1`–`s2` (E16) e `s4`/`h5` com links (E28b), sem reinício; `h5` respondeu no Pingall (20/20). **Remoção com a rede ativa:** link e nó removidos do grafo e do Mininet sem reinício (o log não tem novo "Creating network", e `h1` segue alcançando `h3`). Depois das remoções, o Pingall da interface falhou com HTTP 500 e `/links` manteve a entrada do nó removido. O passo 8 do README não se completou: `ryu-manager` não existe na VM, e não houve conectividade entre as duas topologias. |
| C4 | topologia de cada modelo gerada com a quantidade de dispositivos escolhida | E19–E22 (autores; quantidades escolhidas pelos revisores); E18, E23 (D2) | Single (3 hosts), Linear (3×2 e 2×1) e Tree (2 níveis, fanout 2) gerados. Contagens de switches, hosts e links iguais às escolhidas no grafo e na API, nos quatro casos. |
| C5 | saída do comando exibida na aba do nó selecionado | E14, E24 (autores); E25–E27 (D2) | `ip addr show` na aba `h1` mostra `h1-eth0` 10.0.0.1/8; na aba `h2`, `h2-eth0` 10.0.0.2/8. O shell de cada aba está no namespace de rede do respectivo nó, diferente do namespace da VM. O `iperf` entre as abas `h1` e `h2` mediu 6,62 Gbit/s. |
| C6 | tabela de fluxo exibida, com a regra inserida ou removida no switch | E31–E32 (D2; os autores não documentam procedimento) | A tabela de fluxo de `s1` é exibida (5 regras instaladas pelo controlador após o Pingall). A interface não oferece controle para inserir ou remover regras. |

**Teste mínimo do README (passos 1–9):** passos 1–6 e 9 com o resultado descrito pelos autores; passo 7 (opcional, iperf) concluído; passo 8 (opcional) com a criação do controlador remoto, da segunda topologia e do link verde, mas sem o Ryu (ausente na VM) e sem conectividade entre as topologias no Pingall.

## 5. Insumos ausentes e respostas dos autores

- **Ryu:** não está instalado na VM da release `v0.0.1`. README:75-78 documenta a instalação do Ryu só para a instalação manual. A VM não tem Internet (rede host-only), e nada foi instalado.
- **Link da VM no README** (README:53): inativo na consulta de 15/10/2026. Foi usada a OVA da release `v0.0.1` dos autores.
- **VM "Desktop" com navegador interno** (README:55, 86): não disponível; a VM da release não tem ambiente gráfico.
- **Valores esperados:** os autores não publicam contagens, saídas de referência, tempos nem vazão. As quantidades de C4 e os comandos de C5 foram escolhidos pelos revisores antes da execução.
- **Contato com os autores:** nenhum foi feito; não há respostas.

## 6. Limitações e incidentes

- **Execução única**, em um único host. Os tempos e as vazões dependem do modo NEM sobre o Hyper-V e da memória livre do host (~725 MB no início).
- **Software × documentação:** a VM roda o commit `be68302`. A documentação avaliada é do commit `465648a4`. Backend e frontend são idênticos; mudam `README.md`, `run.sh` (linha `nvm use 18.20.7`) e dois arquivos de exemplo.
- **Navegador:** a interface foi usada pelo navegador do host, não por um navegador dentro da VM. A interação foi automatizada por eventos de entrada do navegador (CDP), não por uma pessoa com mouse e teclado. Os valores dos `<select>` foram atribuídos por script, com o evento `change`.
- **Incidentes da automação** (as capturas e os textos estão preservados):
  - A primeira captura de E10 saiu em 500×320; foi refeita em 1600×1000.
  - Em E13/E14 e E16/E17, o primeiro clique automático no "X" do modal "Pingall Results" não fechou o modal. Os cliques seguintes caíram na máscara do modal: as teclas do primeiro iperf não chegaram ao terminal, e a primeira tentativa de exportar não baixou nada. Em E14, a aba `h1` chegou a ser ativada uma vez por `click()` em JavaScript, sem efeito nos resultados. Tudo foi repetido depois de fechar o modal.
  - Em E16 e E28a, uma leitura de coordenadas errada fez um arraste começar fora do nó; os arrastes foram repetidos.
  - No fim de E32, três cliques automáticos no modal "Node Info" não o fecharam (`…190243Z-E32-barra-lateral.png`); a barra lateral está registrada em E10.
- **Modal do Pingall:** logo após o clique, o modal mostra "No ping results available." até chegar a resposta. Em E16, a resposta levou cerca de 30 s.
- **Limpeza do Mininet:** ao iniciar, o backend apagou `/tmp/*.out`, onde estava a cópia da saída ao vivo da sessão gravada. A gravação em `~/evidencias` (o `terminal.txt`) não foi afetada.
- **Processos:** havia processos `bash` defuntos (`<defunct>`) filhos do uvicorn depois dos resets (`terminal.txt`, E27-ps).
- **Estado da VM:** o snapshot `02-apos-identificacao` não foi alterado. Depois da execução, a VM foi desligada por ACPI às 19:03:35Z, e foi criado o snapshot `03-apos-execucao-referencia`.
