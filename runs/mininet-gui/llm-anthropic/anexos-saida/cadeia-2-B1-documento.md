# Roteiro de execução — Mininet-GUI (SBRC 2025, selos F e R)

Oct 16, 2026 · @edu

Este roteiro leva o revisor da VM dos autores até as decisões de F e R em 24 passos (P1–P24), entre 2 h 45 min e 3 h 50 min. Nenhum passo foi executado na sua preparação: os resultados esperados vêm do README dos autores ou, quando os autores não os declaram, são derivações do código, sempre identificadas.

## Escopo e convenções

**Fontes.** Somente os anexos: `artefato.txt` (commit `465648a4425a4457af0348ab951cf7f71d37a86f`), `artigo.pdf`, `instrucoes-oficiais.md` e `reivindicacoes.md`. Citações no formato `[arquivo:linha]`; arquivos do repositório são citados pelo caminho dentro de `artefato.txt`.

**Caminho seguido.** Apenas a máquina virtual, que é o caminho recomendado pelos autores: "recomenda-se a utilização da VM do Mininet-GUI" \[README.md:44\]. A instalação manual é descrita como invasiva \[README.md:43, 62\] e fica fora deste roteiro.

**Marca \[NÃO DOCUMENTADO\].** Indica passo, comando ou resultado esperado que os autores não descrevem. Cada ocorrência traz a justificativa de por que é necessária. Quando o README dá a ação mas não o resultado, o resultado esperado aparece como "derivado do código", com a linha que o sustenta.

**Campos de cada passo.** Selo e reivindicação; diretório; comando exato; resultado esperado segundo os autores; evidência a salvar; critério de sucesso; critério de falha; critério de interrupção.

**Evidências.** No hospedeiro, guarde tudo em `~/sbrc25-mininet-gui/`; dentro da VM, em `/home/mininet/evidencias/`. Nomeie cada arquivo com o identificador do passo (`P10_grafo.png`, `P18_single.json`). Capturas de tela da VM podem ser feitas pelo menu do VirtualBox (Exibir → Capturar Tela) e salvas no hospedeiro.

**Regra de dependência.** Se o teste mínimo (P9–P11) falhar, F não é atribuído e os blocos de R não têm base para continuar. R segue a regra de `reivindicacoes.md`: é atribuído se C4 (nos três modelos) e C5 forem reproduzidas. C1, C2, C3 e C6 são verificadas para registro e para F.

## Requisitos do ambiente

Os autores pedem VirtualBox 7.1.6 e uma VM com 8 GB de RAM; o restante vem pronto na VM. A tabela separa o que os autores declaram do que é inferência deste roteiro.

| Item | Valor | Origem |
| --- | --- | --- |
| Virtualizador | Oracle VirtualBox versão 7.1.6 r167084 | \[README.md:37\] "requer o Oracle VirtualBox (versão 7.1.6 r167084)" |
| RAM da VM | 8 GB (valor adotado) | \[README.md:38\] "Mínimo de 8GB para a máquina virtual". Conflita com \[README.md:103\] "no mínimo 2GB de RAM"; adota-se o maior. |
| CPU da VM | Pelo menos 1 núcleo reservado | \[README.md:103\] "um core de CPU reservado à VM" |
| RAM do hospedeiro | Mais de 8 GB livres para a VM; sugestão de 12–16 GB no total | \[NÃO DOCUMENTADO\] Inferência: a VM sozinha pede 8 GB. A máquina dos autores tinha 8 GB \[README.md:29\], o que não é declarado como mínimo. |
| Disco do hospedeiro | Pelo menos 80 GB livres | \[README.md:32\] "Pelo menos 80GB livres" (configuração da máquina de demonstração) |
| Hospedeiro de referência | Intel i5-10300H, 8 GB, Windows 11 Home 64 bits | \[README.md:26-31\]; descreve a máquina usada na demonstração, não um requisito |
| Imagem da VM | `Mininet-GUI-Desktop-VM-SBRC-2025.ova` | \[README.md:53, 55\]; link do Google Drive, sem hash publicado |
| Software na VM | Mininet-GUI, Mininet, Node e Ryu pré-instalados (presumido) | \[README.md:44, 84\]. Versões dentro da VM não declaradas; o `setup.sh` instala Node 18.20.7 \[setup.sh:19\]. |
| Navegador | Navegador dentro da VM | \[README.md:86\] "Acesse essa URL em um navegador dentro da VM" |
| Credenciais | usuário `mininet`, senha `mininet` | \[README.md:57, 82\] |
| Rede | Acesso à internet no hospedeiro para baixar a `.ova` | \[README.md:53\]; também na VM caso o Ryu precise ser instalado (P15) |

Se a VM não puder ser obtida, a alternativa dos autores é a instalação manual em Ubuntu 20.04 \[README.md:63-73\]. Ela modifica o sistema e usa caminhos fixos em `/home/mininet` \[setup.sh:5; run.sh:7\], por isso deve ser feita numa VM Ubuntu descartável com usuário `mininet`. Registre essa troca de caminho como desvio.

## Preparação do ambiente (P1–P8)

A preparação termina quando a interface abre no navegador da VM (P8). Três passos aqui não são dos autores: registrar o hospedeiro, conferir os recursos da VM e conferir a versão do código.

### P1 — Registrar o hospedeiro \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F (ambiente); todas.
- **Justificativa:** as instruções oficiais exigem que o ambiente satisfaça os requisitos mínimos; sem registro, a revisão não tem como mostrar isso.
- **Diretório:** `~/sbrc25-mininet-gui/` no hospedeiro.
- **Comando:** `VBoxManage --version > P1_host.txt` e, em Linux, `lscpu >> P1_host.txt; free -h >> P1_host.txt; df -h . >> P1_host.txt`. Em Windows, anote CPU, RAM e disco livre manualmente no mesmo arquivo.
- **Resultado esperado (autores):** versão `7.1.6r167084` \[README.md:37\].
- **Evidência:** `P1_host.txt`.
- **Sucesso:** VirtualBox 7.1.6; RAM e disco livres compatíveis com a seção de requisitos.
- **Falha:** outra versão do VirtualBox, RAM livre abaixo de 8 GB ou disco abaixo de 80 GB.
- **Interrupção:** RAM ou disco insuficientes. Uma versão diferente do VirtualBox não interrompe; registre o desvio.

### P2 — Baixar a imagem da VM

- **Selo / reivindicação:** F; todas.
- **Diretório:** `~/sbrc25-mininet-gui/`.
- **Comando:** abrir no navegador `https://drive.google.com/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing` e baixar \[README.md:53\]. Depois, \[NÃO DOCUMENTADO\] `sha256sum Mininet-GUI-Desktop-VM-SBRC-2025.ova > P2_ova.sha256` (Windows: `certutil -hashfile Mininet-GUI-Desktop-VM-SBRC-2025.ova SHA256`).
- **Justificativa do hash:** os autores não publicam hash; registrá-lo identifica qual imagem foi avaliada.
- **Resultado esperado (autores):** arquivo `Mininet-GUI-Desktop-VM-SBRC-2025.ova` \[README.md:55\].
- **Evidência:** `P2_ova.sha256`; tamanho do arquivo.
- **Sucesso:** download completo, arquivo com esse nome.
- **Falha:** link indisponível, cota do Drive excedida ou download corrompido.
- **Interrupção:** imagem inacessível. Registre como falha de disponibilidade da VM; a alternativa é a instalação manual (seção de requisitos), anotada como desvio.

### P3 — Importar a VM

- **Selo / reivindicação:** F; todas.
- **Diretório:** `~/sbrc25-mininet-gui/`.
- **Comando:** no VirtualBox, Arquivo → Importar Appliance → selecionar a `.ova` \[README.md:55: "Abra o arquivo … no VirtualBox, para importar a máquina virtual"\]. Alternativa por linha de comando \[NÃO DOCUMENTADO\]: `VBoxManage import Mininet-GUI-Desktop-VM-SBRC-2025.ova`.
- **Resultado esperado (autores):** máquina virtual importada.
- **Evidência:** `P3_import.png` (tela do VirtualBox com a VM listada) ou a saída do comando.
- **Sucesso:** VM aparece na lista.
- **Falha:** erro de importação.
- **Interrupção:** a importação falha duas vezes com arquivo íntegro.

### P4 — Conferir recursos da VM \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F (ambiente).
- **Justificativa:** os autores declaram RAM e CPU mínimas \[README.md:38, 103\], mas não mandam verificar a configuração importada.
- **Diretório:** `~/sbrc25-mininet-gui/`.
- **Comando:** `VBoxManage list vms` e depois `VBoxManage showvminfo "<nome listado>" | grep -E "Memory size|Number of CPUs" > P4_vm.txt`.
- **Resultado esperado (autores):** ao menos 8 GB e 1 núcleo.
- **Evidência:** `P4_vm.txt`.
- **Sucesso:** memória ≥ 8192 MB e CPUs ≥ 1.
- **Falha:** valores menores. Ajuste nas configurações da VM e registre o ajuste.
- **Interrupção:** o hospedeiro não comporta 8 GB para a VM.

### P5 — Iniciar a VM e entrar

- **Selo / reivindicação:** F; todas.
- **Diretório:** não se aplica.
- **Comando:** iniciar a VM no VirtualBox e entrar com usuário `mininet`, senha `mininet` \[README.md:57, 82\].
- **Resultado esperado (autores):** não declarado além de "Execute a máquina virtual" e "faça login"; espera-se sessão gráfica aberta, pois P7 usa Ctrl+Alt+T e P8 usa navegador.
- **Evidência:** `P5_login.png`.
- **Sucesso:** área de trabalho da VM visível.
- **Falha:** VM não inicia ou credenciais recusadas.
- **Interrupção:** a VM não chega à área de trabalho.

### P6 — Conferir a versão do código na VM \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R; todas.
- **Justificativa:** a avaliação está fixada no commit `465648a4…`, mas a VM é um binário externo; só a comparação mostra se o código executado é o avaliado.
- **Diretório:** `/home/mininet/mininet-gui` (caminho de \[run.sh:7\]).
- **Comando:** abrir terminal (Ctrl+Alt+T) e executar:

```bash
mkdir -p /home/mininet/evidencias
cd /home/mininet/mininet-gui
(git rev-parse HEAD 2>&1; sha256sum mininet-gui-backend/mininet_gui_backend/api.py mininet-gui-frontend/src/components/NetworkGraph.vue mininet-gui-frontend/src/components/TopologyForm.vue mininet-gui-frontend/src/components/Webshell.vue mininet-gui-frontend/src/components/NodeStats.vue run.sh) > /home/mininet/evidencias/P6_versao.txt
```

- **Resultado esperado (índice de `artefato.txt`, não dos autores):** commit `465648a4425a4457af0348ab951cf7f71d37a86f`, se houver `.git`; hashes começando por `1ea14fe4` (api.py), `c8272489` (NetworkGraph.vue), `a2ce7c41` (TopologyForm.vue), `9758dc08` (Webshell.vue), `d395d496` (NodeStats.vue) e `e1e2a1e8` (run.sh).
- **Evidência:** `P6_versao.txt`.
- **Sucesso:** todos os hashes coincidem.
- **Falha:** algum hash diverge ou o diretório não existe.
- **Interrupção:** não interrompe. Continue, mas registre que os resultados se referem à versão da VM, não ao commit avaliado.

### P7 — Iniciar o Mininet-GUI

- **Selo / reivindicação:** F; todas.
- **Diretório:** `/home/mininet` (terminal novo).
- **Comando:** `mininet_gui` ou, alternativamente, `/home/mininet/mininet-gui/run.sh` \[README.md:84\]. O script usa `sudo` \[run.sh:3, 14\]; se pedir senha, use `mininet` \[NÃO DOCUMENTADO: o README não menciona o pedido de senha\].
- **Resultado esperado (autores):** "mostrará em sua saída do terminal uma URL (Exemplo: `http://10.0.2.15:5173`)" \[README.md:86\]; o script imprime "Mininet-GUI is available at:" seguido da URL \[run.sh:27-28\].
- **Evidência:** `P7_terminal.png` com a saída completa. Após cerca de 30 s, \[NÃO DOCUMENTADO\] copiar os logs que o script indica \[run.sh:23-24\]:

```bash
cp /home/mininet/mininet-gui/mininet-gui-backend/nohup.out /home/mininet/evidencias/P7_backend.log
cp /home/mininet/mininet-gui/mininet-gui-frontend/nohup.out /home/mininet/evidencias/P7_frontend.log
```

- **Justificativa da cópia:** os logs registram erros de inicialização que não aparecem no terminal.
- **Sucesso:** URL impressa; logs sem traceback do backend nem erro do Vite.
- **Falha:** URL ausente, erro de `uvicorn`, `npm` ou `nvm` nos logs.
- **Interrupção:** se P8 também falhar. Uma mensagem isolada como `nvm: command not found` \[run.sh:20\] não interrompe se a interface abrir.

### P8 — Abrir a interface

- **Selo / reivindicação:** F; C1.
- **Diretório:** navegador dentro da VM.
- **Comando:** abrir a URL impressa em P7 \[README.md:86\].
- **Resultado esperado (autores):** interface com "Barra lateral", "Painel inferior" (WebShell) e "Área principal" com o grafo \[artigo.pdf p. 7, Fig. 2\].
- **Evidência:** `P8_interface.png`.
- **Sucesso:** barra lateral com "Generate Topology", "Run Pingall Test" e paleta com "Controller"; painel WebShell visível.
- **Falha:** página em branco, erro de conexão ou alerta "Network Error".
- **Interrupção:** a interface não carrega após repetir P7 uma vez. F não é atribuído e R não é avaliado.

## Teste mínimo — selo F (P9–P13)

F é atribuído se P9, P10, P11 e P13 tiverem sucesso; P12 é opcional para os autores. Estes passos são os passos 4, 5, 6, 7 e 9 do "Teste mínimo" \[README.md:88-98\]. O passo 8, também opcional, fica no bloco de C3 (P15) para isolar a modificação em tempo real. Exportar antes dele não depende de nada que o passo 8 cria.

### P9 — Criar o controlador c1 (passo 4)

- **Selo / reivindicação:** F; C1, C2.
- **Diretório:** interface web (P8).
- **Comando:** "arraste o ícone rotulado 'Controller', localizado na aba lateral esquerda, para o centro da tela… selecione a opção 'Default' e em seguida pressione o botão 'Submit'" \[README.md:88\].
- **Resultado esperado (autores):** "criar o controller" \[README.md:88\]. O nome `c1` é o que o passo 5 usa \[README.md:90\].
- **Evidência:** `P9_c1.png`.
- **Sucesso:** nó `c1` visível no grafo e aba `c1` no WebShell (o WebShell lista todos os nós \[Webshell.vue:9-16\]).
- **Falha:** alerta de erro ou nó ausente.
- **Interrupção:** c1 não é criado após uma segunda tentativa. F não é atribuído.

### P10 — Gerar topologia Single com 2 hosts (passo 5)

- **Selo / reivindicação:** F; C1, C4 (parcial).
- **Diretório:** interface web.
- **Comando:** "Clique no botão 'Generate Topology'… selecione o 'Topology Type' Single, o 'Controller' c1, e no campo 'Hosts' insira o número 2. Em seguida, pressione o botão 'Submit'" \[README.md:90\].
- **Resultado esperado (autores):** não declarado no README. O artigo diz que "os links verdes indicam as conexões ativas" e a associação switch–controlador aparece em "linhas pontilhadas na cor cinza" \[artigo.pdf p. 7\]. Derivado do código: 1 switch `s1`, hosts `h1` e `h2`, links s1–h1 e s1–h2 \[NetworkGraph.vue:512-523\].
- **Evidência:** `P10_single2.png`.
- **Sucesso:** s1, h1 e h2 no grafo; 2 links verdes; linha cinza pontilhada s1–c1.
- **Falha:** nós faltando, links cinza sólidos (rede não iniciada) ou alerta de erro.
- **Interrupção:** nenhum nó é criado. F não é atribuído.

### P11 — Executar pingall (passo 6)

- **Selo / reivindicação:** F; C2.
- **Diretório:** interface web.
- **Comando:** "Execute um teste de pingall clicando no botão 'Run Pingall Test' na aba lateral esquerda e aguarde os resultados aparecerem" \[README.md:92\].
- **Resultado esperado (autores):** "aguarde os resultados aparecerem" \[README.md:92\]. O README não declara perda esperada. Derivado do código: modal "Pingall Results" \[NetworkGraph.vue:496\] com linhas no formato `h1->h2: 1/1, rtt min/avg/max/mdev … ms` \[api.py:159\].
- **Evidência:** `P11_pingall.png`.
- **Sucesso:** linhas h1->h2 e h2->h1 com recebidos iguais aos enviados.
- **Falha:** modal vazio, alerta de erro ou recebidos = 0.
- **Interrupção:** erro do backend. Copie o log (comando de P7 com nome `P11_backend.log`). F não é atribuído; R não é avaliado.

### P12 — Teste com iperf (passo 7, opcional)

- **Selo / reivindicação:** F; C5 (apoio).
- **Diretório:** abas `h1` e `h2` do WebShell.
- **Comando:** "selecione no webshell o terminal do node h1 e digite o comando `iperf -s`. Depois, abra o terminal do node h2 e digite o comando `iperf -c 10.0.0.1`" \[README.md:94\]. Ao final, \[NÃO DOCUMENTADO\] Ctrl+C na aba h1 para encerrar o servidor, porque `iperf -s` não termina sozinho e ocupa o terminal usado em P21.
- **Resultado esperado (autores):** "Aguarde 1 minuto para o teste completar-se" \[README.md:94\].
- **Evidência:** `P12_iperf_h1.png`, `P12_iperf_h2.png`.
- **Sucesso:** na aba h2, relatório do iperf com intervalo e taxa de transferência.
- **Falha:** `iperf: command not found`, "connection refused" ou nenhuma saída após 1 minuto.
- **Interrupção:** não interrompe; o passo é opcional. Registre o resultado.

### P13 — Exportar JSON e script (passo 9)

- **Selo / reivindicação:** F.
- **Diretório:** interface web; depois `/home/mininet/Downloads` (pasta padrão do navegador, presumida).
- **Comando:** "clique nos botões 'Export Topology (JSON)' e 'Export Mininet Script'" \[README.md:98\]. Depois, \[NÃO DOCUMENTADO\] mover e inspecionar:

```bash
cd /home/mininet/Downloads
mv network_export.json /home/mininet/evidencias/P13_single2.json
mv network_export.py /home/mininet/evidencias/P13_single2.py
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print({k: len(v) for k, v in d.items()})" /home/mininet/evidencias/P13_single2.json
```

- **Justificativa:** a inspeção confirma que o conteúdo exportado corresponde ao grafo; os nomes `network_export.json` e `network_export.py` vêm de \[api.js:231, 272\].
- **Resultado esperado (autores):** "o arquivo JSON com a configuração da topologia atual e o script do mininet para executar a topologia fora do Mininet-GUI" \[README.md:98\]. Derivado do código \[export.py:104-108\]: `{'switches': 1, 'hosts': 2, 'controllers': 1, 'links': 2}`.
- **Evidência:** `P13_single2.json`, `P13_single2.py` e a saída do comando.
- **Sucesso:** os dois arquivos existem; contagens iguais às esperadas; o script contém `net.addHost("h1"` e `net.addHost("h2"`.
- **Falha:** download não ocorre, arquivo vazio ou contagens diferentes.
- **Interrupção:** não interrompe. Falha aqui é problema de F a registrar; os blocos de R continuam.

## Selo R — blocos por reivindicação (P14–P23)

R depende de C4 (P17–P20) e C5 (P21); os demais blocos são registro. Os autores documentam procedimentos de R apenas para C4 e C5 \[README.md:105-114\] e um procedimento opcional que cobre parte de C3 \[README.md:96\]. Execute os blocos na ordem abaixo, porque C4 reinicia a topologia.

### C1 — Interface e grafo interativo

Evidência principal já produzida em P8–P10 (passos 1–5 do teste mínimo, como indica `reivindicacoes.md`). Resultado esperado da tabela: "elementos criados pelo usuário representados no grafo e respondendo às ações".

#### P14 — Mover um nó no grafo \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R (registro); C1.
- **Justificativa:** o README mostra criação por arrastar \[README.md:88, 112\], mas não indica uma ação sobre um nó já criado. "Respondendo às ações" exige observar uma.
- **Diretório:** interface web, com a topologia de P10.
- **Comando:** arrastar `h1` para outra posição; recarregar a página (F5).
- **Resultado esperado:** não declarado pelos autores. Derivado do código: o fim do arraste envia a posição ao backend \[NetworkGraph.vue:282-284; api.py:270-295\].
- **Evidência:** `P14_antes.png`, `P14_depois.png`, `P14_recarregado.png`.
- **Sucesso:** o nó se move com seus links e, após recarregar, os nós continuam no grafo.
- **Falha:** o nó não se move ou a topologia some após recarregar.
- **Interrupção:** não interrompe.

### C2 — Emulação integrada

Sem passo novo. A reivindicação é verificada por P9–P11 (passos 4–6 do README). Resultado esperado da tabela: "nós emulados e resultado de `pingall` exibido na interface". Sucesso = P11 com sucesso.

### C3 — Modificação em tempo real

O README cobre apenas a criação, no passo 8 opcional. A remoção é \[NÃO DOCUMENTADO\].

#### P15 — Segundo controlador e link entre topologias (passo 8)

- **Selo / reivindicação:** R (registro); C3.
- **Diretório:** interface web, sem reiniciar a topologia de P10.
- **Comando:** seguir \[README.md:96\] na ordem:
  1. Arrastar novo "Controller", type "Remote", IP `127.0.0.1`, porta `6633`.
  2. "Generate Topology" do tipo Single com 2 hosts, controlador `c2`.
  3. "Create Link" e arrastar de `s1` para `s2`.
  4. No WebShell, aba `c2`: `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`.
  5. "Run Pingall Test".
- **Observações:** a criação do controlador remoto pode bloquear por até 60 s \[api.py:205, comentário TODO\]; aguarde. Se `ryu-manager` não existir, use o comando de instalação dos autores \[README.md:77\]: `pip3 install ryu eventlet==0.30.0 dnspython==1.16.0`, e registre o desvio.
- **Resultado esperado (autores):** "o sucesso dessa ação é indicado por uma linha verde conectando os dois nós"; "Para testar a conexão, execute um teste com o botão de Pingall" \[README.md:96\]. Derivado do código: novos nós `s2`, `h3`, `h4` \[NetworkGraph.vue:289-299\].
- **Evidência:** `P15_link_verde.png`, `P15_ryu.png` (saída da aba c2), `P15_pingall.png`.
- **Sucesso:** linha verde s1–s2 criada sem "Reset Topology"; pingall com recebidos > 0 entre hosts das duas topologias (por exemplo h1->h3).
- **Falha:** link não criado, alerta de erro ou pingall sem comunicação entre as topologias após o Ryu iniciar.
- **Interrupção:** não interrompe R. Registre C3 como não reproduzida e siga para C4.

#### P16 — Remover link e nó com a emulação ativa \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R (registro); C3.
- **Justificativa:** C3 inclui "criar e remover nós e links … sem reiniciá-la" (`reivindicacoes.md`; artigo p. 6), mas o README não tem procedimento de remoção. O botão "Delete Selected" existe na interface \[Side.vue:35-37\] e aparece na Fig. 2.
- **Diretório:** interface web, sem reiniciar; depois terminal da VM.
- **Comando:**
  1. Clicar no link s1–s2, clicar "Delete Selected", executar "Run Pingall Test".
  2. Clicar em `h4`, clicar "Delete Selected", executar "Run Pingall Test".
  3. No terminal da VM, conferir que a rede não foi reiniciada:

```bash
cd /home/mininet/mininet-gui/mininet-gui-backend
grep -c "/api/mininet/pingall" nohup.out > /home/mininet/evidencias/P16_log.txt
grep -c "/api/mininet/reset" nohup.out >> /home/mininet/evidencias/P16_log.txt
```

- **Resultado esperado:** não declarado pelos autores. Derivado do código \[api.py:298-325\]: após 1, os pares entre {h1, h2} e {h3, h4} falham e os pares internos continuam respondendo; após 2, `h4` some do pingall. Na contagem, a primeira linha deve ser > 0 (o log registra requisições) e a segunda, 0.
- **Evidência:** `P16_sem_link.png`, `P16_pingall1.png`, `P16_sem_h4.png`, `P16_pingall2.png`, `P16_log.txt`.
- **Sucesso:** grafo e pingall refletem as duas remoções; nenhuma chamada a `/api/mininet/reset`.
- **Falha:** remoção some só do grafo e o pingall não muda; erro do backend; ou a primeira contagem é 0, o que torna a segunda inconclusiva.
- **Interrupção:** não interrompe R.

### C4 — Geração automatizada (Single, Linear, Tree)

C4 é reproduzida se os três modelos tiverem sucesso. O procedimento dos autores: "clique no botão 'Generate Topology'. Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK" \[README.md:107-108\]. O botão do formulário se chama "Submit" \[TopologyForm.vue:43\], e o "número de dispositivos" muda por modelo: Hosts (Single), Switches e Hosts per switch (Linear), Layers e Fanout (Tree) \[TopologyForm.vue:19-42\]. Os autores não declaram as contagens esperadas; as abaixo são derivadas de \[NetworkGraph.vue:512-584\].

| Modelo | Valores a inserir | Switches | Hosts | Links |
| --- | --- | --- | --- | --- |
| Single | Hosts = 3 | 1 | 3 | 3 |
| Linear | Switches = 3; Hosts per switch = 2 | 3 | 6 | 8 |
| Tree | Layers = 2; Fanout = 2 | 3 | 4 | 6 |

#### P17 — Reiniciar topologia e recriar c1 \[NÃO DOCUMENTADO, com uso do passo 4\]

- **Selo / reivindicação:** R; C4.
- **Justificativa:** sem partir de uma topologia vazia, as contagens de cada modelo se misturam com nós anteriores. O README não descreve o reinício; o botão "Reset Topology" existe \[Side.vue:22-24\] e o artigo cita "reinicialização da emulação" (p. 7). O reinício apaga os controladores \[api.py:134\], então c1 é recriado.
- **Diretório:** interface web.
- **Comando:** "Reset Topology" → confirmar o diálogo \[NetworkGraph.vue:619\]; depois repetir o passo 4 do README (controlador Default) \[README.md:88\].
- **Resultado esperado:** grafo vazio, depois apenas `c1`.
- **Evidência:** `P17_vazio.png`, `P17_c1.png`.
- **Sucesso:** grafo vazio após o reinício e c1 criado.
- **Falha:** nós antigos permanecem ou alerta de erro.
- **Interrupção:** o reinício falha. Reinicie o Mininet-GUI (P7, P8) e registre; se persistir, C4 fica indeterminada.

#### P18 — Modelo Single

- **Selo / reivindicação:** R; C4.
- **Diretório:** interface web; depois `/home/mininet/Downloads`.
- **Comando:** "Generate Topology" → Single, controller c1, Hosts = 3 → Submit \[README.md:107-108\]. Depois, \[NÃO DOCUMENTADO\] "Run Pingall Test" e "Export Topology (JSON)" \[README.md:92, 98\], e:

```bash
cd /home/mininet/Downloads
mv network_export.json /home/mininet/evidencias/P18_single.json
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print({k: len(v) for k, v in d.items()})" /home/mininet/evidencias/P18_single.json
```

- **Justificativa do pingall e da exportação:** o pingall mostra que a topologia foi emulada, não só desenhada; a exportação conta os elementos que o backend registrou.
- **Resultado esperado (autores):** topologia do tipo escolhido com a quantidade escolhida \[README.md:107-108\]; contagens na tabela acima.
- **Evidência:** `P18_grafo.png`, `P18_pingall.png`, `P18_single.json` e saída do comando.
- **Sucesso:** contagens iguais à tabela (controllers = 1) e pingall com recebidos iguais aos enviados.
- **Falha:** contagens diferentes, erro ou pares sem resposta.
- **Interrupção:** não interrompe os outros modelos; uma falha já torna C4 não reproduzida.

#### P19 — Modelo Linear

- **Selo / reivindicação:** R; C4.
- **Diretório:** igual a P18.
- **Comando:** repetir P17; depois "Generate Topology" → Linear, controller c1, Switches = 3, Hosts per switch = 2 → Submit; pingall e exportação como em P18, salvando como `P19_linear.json`.
- **Resultado esperado:** 3 switches, 6 hosts, 8 links (6 host–switch e 2 entre switches).
- **Evidência:** `P19_vazio.png`, `P19_grafo.png`, `P19_pingall.png`, `P19_linear.json`.
- **Sucesso / falha / interrupção:** como em P18.

#### P20 — Modelo Tree

- **Selo / reivindicação:** R; C4.
- **Diretório:** igual a P18.
- **Comando:** repetir P17; depois "Generate Topology" → Tree, controller c1, Layers = 2, Fanout = 2 → Submit; pingall e exportação como em P18, salvando como `P20_tree.json`.
- **Resultado esperado:** 3 switches, 4 hosts, 6 links; árvore com raiz no topo, como na Fig. 2 do artigo (que mostra uma árvore maior).
- **Evidência:** `P20_vazio.png`, `P20_grafo.png`, `P20_pingall.png`, `P20_tree.json`.
- **Sucesso / falha / interrupção:** como em P18. Mantenha esta topologia para P21.

### C5 — Terminal dos nós via WebShell

#### P21 — Comando no namespace de um host

- **Selo / reivindicação:** R; C5.
- **Diretório:** interface web com a topologia Tree de P20; depois terminal da VM.
- **Comando:**
  1. &#91;NÃO DOCUMENTADO\] Recarregar a página (F5). Justificativa: as abas do WebShell abertas antes do reinício podem manter conexões de nós apagados com o mesmo nome; o código só fecha as conexões quando a lista de nós fica vazia \[Webshell.vue:54-62\].
  2. "na aba inferior titulada 'Webshell' selecione a aba com o nome desse nó" \[README.md:112-113\]: aba `h1`. Digitar `ip -br addr` e Enter. Repetir na aba `h2`. A escolha do comando é \[NÃO DOCUMENTADO\]: os autores dizem apenas "executar comandos" \[README.md:114\]; `ip -br addr` mostra de forma direta em qual namespace o shell está.
  3. &#91;NÃO DOCUMENTADO\] Contraste no terminal da VM, fora da interface: `ip -br addr > /home/mininet/evidencias/P21_vm_raiz.txt`.
- **Resultado esperado (autores):** "utilize o terminal bash para executar comandos diretamente no namespace daquele nó" \[README.md:114\]. Derivado do código: aba h1 com `lo` e `h1-eth0` em `10.0.0.1/8`; aba h2 com `h2-eth0` em `10.0.0.2/8` \[api.py:476; NetworkGraph.vue:299\].
- **Evidência:** `P21_h1.png`, `P21_h2.png`, `P21_vm_raiz.txt`.
- **Sucesso:** cada aba mostra a saída do comando com apenas a interface do próprio host, diferente da saída do terminal da VM.
- **Falha:** nenhuma saída, erro de WebSocket, ou a aba mostra as interfaces da VM (o shell não está no namespace do nó).
- **Interrupção:** falha nas duas abas após recarregar e repetir uma vez. C5 não reproduzida; R não é atribuído.

### C6 — Regras de fluxo OpenFlow

Os autores não documentam procedimento para C6 (coluna "não" em `reivindicacoes.md`), então os dois passos são \[NÃO DOCUMENTADO\]. C6 não entra na regra de R; o registro serve para F e para o relatório.

#### P22 — Visualizar a tabela de fluxo \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** registro; C6 (visualização).
- **Justificativa:** o artigo afirma visualização de regras (p. 6, "Flow Rule Editor"); o acesso pela interface é um duplo clique no nó \[NetworkGraph.vue:277-281\], não descrito no README.
- **Diretório:** interface web com a topologia de P20.
- **Comando:** "Run Pingall Test"; logo em seguida, duplo clique em `s1` → aba "Flow Table" \[NodeStats.vue:37\].
- **Resultado esperado:** "visualização … de regras de fluxo OpenFlow nos switches" \[artigo.pdf p. 6\]. Derivado do código: tabela com cookie, duration, priority e match fields \[NodeStats.vue:79-88\].
- **Evidência:** `P22_flow_table.png`.
- **Sucesso:** tabela com ao menos uma regra.
- **Falha:** modal não abre, aba ausente ou tabela vazia logo após o pingall.
- **Interrupção:** não interrompe.

#### P23 — Procurar criação e remoção de regras \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** registro; C6 (criação e remoção).
- **Justificativa:** o artigo afirma "criação e remoção de regras de fluxo OpenFlow nos switches" (p. 6), e a análise do código não achou implementação. Só a inspeção da interface confirma se o recurso existe na VM.
- **Diretório:** interface web.
- **Comando:** no modal de P22 e na barra lateral, procurar controle para adicionar ou remover regra. Se existir, inserir uma regra e removê-la, conferindo a aba "Flow Table" após cada ação.
- **Resultado esperado:** pelo artigo, controle presente. Pelo código do commit avaliado, ausente.
- **Evidência:** `P23_modal.png`, `P23_barra.png` e, se houver controle, `P23_inserida.png` e `P23_removida.png`.
- **Sucesso:** a regra aparece e depois desaparece da tabela.
- **Falha:** não há controle, ou a tabela não muda. C6 não reproduzida na parte de criação e remoção.
- **Interrupção:** não interrompe.

### Encerramento

#### P24 — Reunir evidências \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R; todas.
- **Justificativa:** a revisão precisa justificar os selos com as evidências observadas (instruções oficiais), e os logs finais registram erros posteriores a P7.
- **Diretório:** `/home/mininet`.
- **Comando:**

```bash
cp /home/mininet/mininet-gui/mininet-gui-backend/nohup.out /home/mininet/evidencias/P24_backend.log
cp /home/mininet/mininet-gui/mininet-gui-frontend/nohup.out /home/mininet/evidencias/P24_frontend.log
cd /home/mininet/evidencias && sha256sum * > SHA256SUMS
tar czf /home/mininet/evidencias.tgz -C /home/mininet evidencias
```

Transfira `evidencias.tgz` ao hospedeiro (pasta compartilhada do VirtualBox ou outro meio) e junte às capturas de tela.

- **Resultado esperado:** arquivo compactado com logs, JSONs, textos e `SHA256SUMS`.
- **Sucesso:** arquivo transferido e íntegro.
- **Falha:** arquivos ausentes.
- **Interrupção:** não se aplica.

## Tempo estimado

O roteiro completo leva entre 2 h 45 min e 3 h 50 min; a maior incerteza é o download da `.ova`, cujo tamanho os autores não informam. As estimativas são deste roteiro: os autores só declaram a espera de 1 minuto do iperf \[README.md:94\].

| Bloco | Passos | Mínimo (min) | Máximo (min) | Principal fonte de variação |
| --- | --- | --- | --- | --- |
| Preparação | P1–P8 | 53 | 108 | Download e importação da `.ova` |
| Teste mínimo (F) | P9–P13 | 20 | 20 | Inclui 1 min de iperf |
| C1 | P14 | 5 | 5 | — |
| C2 | (P9–P11) | 0 | 0 | Já coberta pelo teste mínimo |
| C3 | P15–P16 | 25 | 35 | Até 60 s do controlador remoto; instalação do Ryu, se faltar |
| C4 | P17–P20 | 33 | 33 | Três reinícios e três exportações |
| C5 | P21 | 8 | 8 | — |
| C6 | P22–P23 | 10 | 10 | — |
| Encerramento | P24 | 10 | 10 | Transferência ao hospedeiro |
| **Total** | P1–P24 | **164** | **229** |  |

## Tabela de todos os passos

Dos 24 passos, 16 partem de procedimentos dos autores e 8 são \[NÃO DOCUMENTADO\] no todo (P1, P4, P6, P14, P16, P22, P23, P24); vários passos dos autores têm complementos não documentados, indicados na coluna Origem.

| ID | Selo | Reivindicação | Origem | Ação | Sucesso | Se falhar | Tempo (min) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | F | todas | \[NÃO DOCUMENTADO\] | Registrar hospedeiro e versão do VirtualBox | VirtualBox 7.1.6; RAM e disco suficientes | Interromper se faltar RAM ou disco | 5 |
| P2 | F | todas | README.md:53 + hash \[NÃO DOC.\] | Baixar `.ova` e registrar SHA-256 | Arquivo completo | Interromper se inacessível | 15–60 |
| P3 | F | todas | README.md:55 | Importar a VM | VM listada | Interromper após 2 falhas | 10–20 |
| P4 | F | todas | \[NÃO DOCUMENTADO\] | Conferir RAM ≥ 8 GB e CPU ≥ 1 | Valores atendidos | Ajustar; interromper se impossível | 5 |
| P5 | F | todas | README.md:57, 82 | Iniciar VM; login mininet/mininet | Área de trabalho visível | Interromper | 5 |
| P6 | F, R | todas | \[NÃO DOCUMENTADO\] | Comparar hashes com o commit `465648a4` | Hashes coincidem | Registrar desvio; continuar | 5 |
| P7 | F | todas | README.md:84 + logs \[NÃO DOC.\] | `mininet_gui` | URL impressa; logs sem erro | Interromper se P8 falhar | 5 |
| P8 | F | C1 | README.md:86 | Abrir URL no navegador da VM | Interface com barra lateral e WebShell | Interromper: F e R negados | 3 |
| P9 | F | C1, C2 | README.md:88 | Criar controlador c1 (Default) | c1 no grafo e no WebShell | Interromper: F negado | 3 |
| P10 | F | C1, C4 | README.md:90 | Single, c1, 2 hosts | s1, h1, h2; 2 links verdes | Interromper: F negado | 3 |
| P11 | F | C2 | README.md:92 | Run Pingall Test | h1↔h2 com recebidos = enviados | Interromper: F negado, R não avaliado | 3 |
| P12 | F | C5 (apoio) | README.md:94 + Ctrl+C \[NÃO DOC.\] | iperf h1 servidor, h2 cliente | Relatório do iperf em h2 | Registrar; continuar | 5 |
| P13 | F | — | README.md:98 + inspeção \[NÃO DOC.\] | Exportar JSON e script; contar elementos | 1/2/1/2 elementos; script com h1, h2 | Registrar para F; continuar | 5 |
| P14 | R (registro) | C1 | \[NÃO DOCUMENTADO\] | Mover h1; recarregar página | Nó move e topologia persiste | Registrar; continuar | 5 |
| P15 | R (registro) | C3 | README.md:96 | c2 remoto, Single com c2, link s1–s2, Ryu, pingall | Link verde sem reset; h1→h3 responde | C3 não reproduzida; continuar | 15–25 |
| P16 | R (registro) | C3 | \[NÃO DOCUMENTADO\] | Remover link s1–s2 e h4; pingall; contar resets no log | Pingall reflete remoções; 0 resets | C3 não reproduzida; continuar | 10 |
| P17 | R | C4 | \[NÃO DOC.\] + README.md:88 | Reset Topology; recriar c1 | Grafo vazio, depois só c1 | Reiniciar P7–P8; persistindo, C4 indeterminada | 3 |
| P18 | R | C4 | README.md:107-108 + pingall/export \[NÃO DOC.\] | Single, Hosts = 3 | 1 sw, 3 hosts, 3 links; pingall completo | C4 não reproduzida | 8 |
| P19 | R | C4 | README.md:107-108 + P17 | Linear, 3 switches × 2 hosts | 3 sw, 6 hosts, 8 links; pingall completo | C4 não reproduzida | 11 |
| P20 | R | C4 | README.md:107-108 + P17 | Tree, Layers = 2, Fanout = 2 | 3 sw, 4 hosts, 6 links; pingall completo | C4 não reproduzida | 11 |
| P21 | R | C5 | README.md:112-114 + F5/comando \[NÃO DOC.\] | `ip -br addr` nas abas h1 e h2 | `h1-eth0` 10.0.0.1/8 e `h2-eth0` 10.0.0.2/8, distintos da VM | C5 não reproduzida; R negado | 8 |
| P22 | registro | C6 | \[NÃO DOCUMENTADO\] | Pingall; duplo clique em s1; aba Flow Table | Tabela com regras | Registrar | 5 |
| P23 | registro | C6 | \[NÃO DOCUMENTADO\] | Procurar controle para inserir e remover regra | Regra inserida e removida | C6 não reproduzida (criação/remoção) | 5 |
| P24 | F, R | todas | \[NÃO DOCUMENTADO\] | Copiar logs, gerar SHA256SUMS, compactar e transferir | Pacote íntegro no hospedeiro | Registrar | 10 |

**Decisão após a execução.** F: atribuir se P8–P11 e P13 tiverem sucesso. R: atribuir se P18, P19, P20 e P21 tiverem sucesso (regra de `reivindicacoes.md`). C3 e C6 não alteram R, mas entram no parecer como divergências entre artigo e artefato.
