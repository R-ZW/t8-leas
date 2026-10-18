# Cadeia MG-2 — [REMOVIDO]

- provedor: [REMOVIDO]
- modelo_exibido: [REMOVIDO]
- versao: [REMOVIDO]
- esforco: [REMOVIDO]
- interface: [REMOVIDO]
- data_hora_A: 2026-10-17 13:52 BRT
- data_hora_B1: 2026-10-17 13:56 BRT
- data_hora_B2: 2026-10-17 23:26 BRT
- anexos_A: artigo.pdf=4e3ff858506f2f9e6da30af4412caa402890ac154b910df390b74e2ee2a2bf08, artefato.txt=5e1da9b36fe62beddfdb9b8dbbceefa67c1c38e14f45c8bd3247519bcf83c8eb, instrucoes-oficiais.md=fc8e01dd0ffdbff06af86a07bd44662c3394903c0d3a6be0222e678963989059, reivindicacoes.md=100366e5dfad9c560f9d5066e67d1e23df8f6ad7c3d5ce2e62aff02a529ed0bc
- anexo_B2: registro-factual.md=0efda099a39c28b4fd3a91e0c5e38290c3238aa87ccde3281ad3ec9062df9b0e
- metodo_exportacao: transcrição integral gerada a partir do log oficial da sessão isolada (`0b73303b-be46-4f0a-8aa2-c1e9840b15dd`, `transcript_full.jsonl`); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos
- desvios: resposta A usou 9 chamada(s) de ferramenta somente-leitura para abrir os 4 anexos: [REMOVIDO] ("Read instrucoes-oficiais.md"); [REMOVIDO] ("Read reivindicacoes.md"); [REMOVIDO] ("Read artigo.pdf"); [REMOVIDO] ("Read start of artefato.txt"); [REMOVIDO] ("Read artefato.txt lines 801-1600"); [REMOVIDO] ("Read artefato.txt lines 2250-3050"); [REMOVIDO] ("Read artefato.txt lines 3051-3850"); [REMOVIDO] ("Read artefato.txt lines 3851-4650"); [REMOVIDO] ("Read artefato.txt lines 4651-4930") | resposta A contém raciocínio (thinking) omitido nesta transcrição | resposta B1 contém raciocínio (thinking) omitido nesta transcrição | resposta B2 usou 1 chamada(s) de ferramenta somente-leitura para abrir o registro factual: [REMOVIDO] ("Read registro-factual.md") | resposta B2 contém raciocínio (thinking) omitido nesta transcrição

## Prompt A

Atue como revisor do Comitê de Avaliação de Artefatos do SBRC 2025. Avalie somente os selos Funcional (F) e Reprodutível (R), seguindo exatamente as instruções oficiais anexadas (instrucoes-oficiais.md).

MATERIAL
Use exclusivamente os arquivos anexados: artigo.pdf (fonte das reivindicações), artefato.txt (o artefato completo na versão 465648a4425a4457af0348ab951cf7f71d37a86f, em arquivo único: índice de todos os arquivos do repositório e o texto integral de cada arquivo de texto, com o número da linha original), instrucoes-oficiais.md e reivindicacoes.md (lista de reivindicações principais e regra para o selo R). Não navegue na web nem consulte memória, outras conversas, projetos ou conectores. Se precisar de algo que não está nos anexos, registre como evidência ausente.

TAREFA
Esta é uma avaliação analítica: você não executou o artefato e não deve afirmar que algo funcionou.

Para cada selo:
1. Liste os critérios oficiais aplicáveis, citando o trecho das instruções.
2. Para cada critério, indique: atendido na documentação, não atendido, ou só verificável por execução.
3. Cite cada evidência no formato [arquivo:seção ou linha] e transcreva o trecho curto que a sustenta.
4. Decida: Atribuir, Não atribuir ou Indeterminado, usando esta regra:
   - Não atribuir: há evidência de que um critério obrigatório não é atendido (por exemplo, falta o dado necessário para uma reivindicação principal).
   - Indeterminado: nenhum critério obrigatório falha na documentação, mas a decisão depende de execução.
   - Atribuir: somente se os critérios estiverem atendidos com evidência suficiente para isso.
5. Informe sua confiança de 0 a 100 de que o comitê oficial atribuiu o selo.
6. Liste o que precisaria ser observado na execução para mudar sua decisão.

Para R, avalie cada reivindicação de reivindicacoes.md separadamente.

FORMATO
Responda em texto com as seções: A. Materiais examinados (liste os arquivos que você efetivamente abriu); B. Selo F; C. Selo R (por reivindicação); D. Lacunas e riscos.
Ao final, inclua um bloco JSON exatamente neste formato:
{"F": {"decisao": "...", "confianca": 0, "evidencias": ["arquivo:local", "..."]},
 "R": {"decisao": "...", "confianca": 0, "evidencias": ["..."],
       "por_reivindicacao": {"C1": "reproduzivel|nao_reproduzivel|depende_execucao"}}}

## Resposta A

## A. Materiais examinados

Foram abertos e examinados exclusivamente os quatro arquivos do pacote:
- `runs/mininet-gui/pacote/instrucoes-oficiais.md`
- `runs/mininet-gui/pacote/reivindicacoes.md`
- `runs/mininet-gui/pacote/artigo.pdf`
- `runs/mininet-gui/pacote/artefato.txt` (contendo `LICENSE`, `README.md`, `example_network_export.json`, `example_network_export.py`, `setup.sh`, `run.sh`, código do backend em `mininet-gui-backend/` e código do frontend em `mininet-gui-frontend/`)

---

## B. Selo F (Funcional)

### 1. Critérios oficiais aplicáveis e avaliação por critério

Conforme `[instrucoes-oficiais.md:10-15]`:
- **Trecho oficial:** *"O ambiente escolhido precisa satisfazer os requisitos mínimos do artefato; a página recomenda virtualização. Recursos específicos necessários devem estar descritos no apêndice."* `[instrucoes-oficiais.md:10]` e *"O código ou artefato deve poder ser executado, e o revisor deve conseguir observar funcionalidades. O README deve informar dependências e versões, ambiente de execução, instalação, execução e um exemplo mínimo. A conclusão funcional requer observação do artefato, não apenas a presença das instruções."* `[instrucoes-oficiais.md:15]`.

Avaliação de cada critério:

1. **README informa dependências e versões:** **Atendido na documentação.**
   - `[README.md:37-38]`: `"A execução do Mininet-GUI requer o Oracle VirtualBox (versão 7.1.6 r167084). / Memória RAM: Mínimo de 8GB para a máquina virtual."`
   - `[README.md:77]`: `"pip3 install ryu eventlet==0.30.0 dnspython==1.16.0"`
   - `[setup.sh:13-19]`: `"curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash"` e `"nvm install 18.20.7"`
   - `[mininet-gui-frontend/package.json:10-23]`: lista dependências JS com versões (`"axios": "^1.2.1"`, `"vis-network": "^9.1.2"`, `"vue": "^3.2.45"`, `"vite": "^4.0.0"`, etc.).
   - `[mininet-gui-backend/requirements.txt:1-4]`: `"fastapi / websockets / uvicorn / python-multipart"` (sem fixação de versão neste arquivo, embora a VM pré-configurada encapsule o ambiente).

2. **README informa ambiente de execução e recursos necessários:** **Atendido na documentação.**
   - `[README.md:26-32]`: `"Para a demonstração, foi utilizado um laptop com as seguintes configurações: / Processador: Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz 2.50 GHz / RAM instalada: 8,00 GB / Sistema Operacional: Windows 11 Home Single Language ... Espaço disponível em disco: Pelo menos 80GB livres"`
   - `[README.md:63]`: `"Utilize os comandos abaixo para instalar manualmente (testado no ubuntu 20.04):"`
   - `[README.md:103]`: `"A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM."`

3. **README informa instruções de instalação:** **Atendido na documentação.**
   - `[README.md:49-57]`: `"## Máquina Virtual (recomendado) ... Passo 1: Baixe o arquivo ova neste link: <https://drive.[REMOVIDO]/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing> / Passo 2: Abra o arquivo Mininet-GUI-Desktop-VM-SBRC-2025.ova no VirtualBox, para importar a máquina virtual / Passo 3: Execute a máquina virtual (user mininet, senha mininet)"`
   - `[README.md:60-73]`: `"## Instalação manual ... git clone https://github.com/mininet/mininet / cd mininet / ./util/install.sh -nfv / cd .. / git clone https://github.com/latarc/mininet-gui / cd mininet-gui / ./setup.sh"`

4. **README informa instruções de execução:** **Atendido na documentação.**
   - `[README.md:82-86]`: `"Passo 1: Execute a VM dentro do VirtualBox e faça login (usuário: mininet, senha: mininet) / Passo 2: Abra o terminal (Ctrl+Alt+T) e rode o seguinte comando: mininet_gui (ou alternativamente /home/mininet/mininet-gui/run.sh) / Passo 3: A execução do comando do Passo 2 mostrará em sua saída do terminal uma URL (Exemplo: http://10.0.2.15:5173). Acesse essa URL em um navegador dentro da VM."`
   - `[run.sh:14-28]`: inicia o backend com `uvicorn mininet_gui_backend.api:app --host=0.0.0.0 --port=8000`, grava `.env` e inicia o frontend com `nvm use 18.20.7 ; nohup npm run dev &`.

5. **README inclui exemplo mínimo de teste:** **Atendido na documentação.**
   - `[README.md:80-99]`: seção `# Teste mínimo` com 9 passos detalhando criação de controlador (`Passo 4`), geração de topologia Single com 2 hosts (`Passo 5`), teste de conectividade com `Run Pingall Test` (`Passo 6`), teste opcional com `iperf` via WebShell (`Passo 7`), cenário opcional com múltiplos controladores e Ryu (`Passo 8`) e exportação da topologia em JSON e script Python (`Passo 9`).

6. **Execução do artefato e observação de funcionalidades:** **Só verificável por execução.**
   - `[instrucoes-oficiais.md:15]`: `"O código ou artefato deve poder ser executado, e o revisor deve conseguir observar funcionalidades. ... A conclusão funcional requer observação do artefato, não apenas a presença das instruções."`
   - Na análise estática do commit `465648a4425a4457af0348ab951cf7f71d37a86f`, identificou-se um erro de sintaxe JavaScript em `[mininet-gui-frontend/src/core/api.js:299]` (`"  }i"` no fechamento do bloco `catch` de `requestRunPingall`), além de uma variável `dst` não declarada em `deleteEdge` `[mininet-gui-frontend/src/components/NetworkGraph.vue:256-265]`. Contudo, como o método principal recomendado de execução é a máquina virtual externa (`Mininet-GUI-Desktop-VM-SBRC-2025.ova`, `[README.md:49-57]`), cujo conteúdo não faz parte do pacote estático, somente a execução permite verificar se a VM executa diretamente sem esse erro de sintaxe ou se a instalação manual falha ao carregar `api.js`.

### 2. Decisão para o Selo F
- **Decisão:** **Indeterminado**
- **Justificativa:** Nenhum critério obrigatório de documentação falha no `README.md`, mas a atribuição do selo F exige a observação prática do artefato em execução (`[instrucoes-oficiais.md:15]`), não realizada nesta avaliação analítica.
- **Confiança (0 a 100) de que o comitê oficial atribuiu o selo F:** **85** (o `README.md` segue o modelo do SBRC 2025, disponibiliza VM dedicada `Mininet-GUI-Desktop-VM-SBRC-2025.ova` e vídeo de demonstração, e implementa os componentes centrais de backend e frontend).
- **O que precisaria ser observado na execução para mudar a decisão:**
  - **Para mudar para Atribuir:** Importar e iniciar a VM (ou instalar manualmente corrigindo eventual erro em `api.js:299`), executar `mininet_gui` (`run.sh`), abrir a interface web na porta `5173`, executar os passos do "Teste mínimo" (`[README.md:82-99]`) e observar a criação de nós, geração de topologia, resultado do `pingall`, uso do WebShell e exportação de arquivos JSON/Python funcionando.
  - **Para mudar para Não atribuir:** Observar que a VM está indisponível/corrompida e que a execução falha de forma impeditiva (por exemplo, o frontend não compila/carrega devido ao erro de sintaxe `}i` em `[mininet-gui-frontend/src/core/api.js:299]` ou o backend falha ao instanciar o Mininet).

---

## C. Selo R (Reprodutível)

### 1. Critérios oficiais aplicáveis e regra do selo R

- **Critério oficial:** *"O revisor deve conseguir reproduzir as **principais reivindicações do artigo**. Para isso, o artefato precisa fornecer instruções de execução e descrição do processo empregado nos experimentos que produziram os resultados do artigo. A avaliação confronta o resultado observado com a reivindicação correspondente."* `[instrucoes-oficiais.md:19]`.
- **Regra específica para o selo R neste artefato:** *"Na seção "Experimentos", o README marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R."* `[reivindicacoes.md:16]` e *"As reivindicações descrevem comportamentos, sem valores numéricos com tolerância declarada pelos autores. Uma reivindicação é reproduzida quando o resultado esperado da tabela é observado. Em C4, nos três modelos."* `[reivindicacoes.md:20]`.

Status dos critérios gerais de R:
1. **Instruções de execução e descrição do processo para as reivindicações de R (C4 e C5):** **Atendido na documentação** (`[README.md:80-115]`, seções `# Teste mínimo` e `# Experimentos`).
2. **Reprodução e observação prática dos resultados esperados confrontados com as reivindicações:** **Só verificável por execução** (`[instrucoes-oficiais.md:19]`, `[reivindicacoes.md:16-20]`).

### 2. Avaliação separada por reivindicação (`reivindicacoes.md`)

#### Reivindicação C1 — Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo
- **Fonte no artigo:** `[artigo.pdf:p.1, resumo]`, `[artigo.pdf:p.2, §1]` (*"1. Interface web dinâmica para manipulação intuitiva da topologia de rede."*), `[artigo.pdf:pp.4-6, §3]`, `[artigo.pdf:p.7, Fig. 2]`.
- **Resultado esperado:** elementos criados pelo usuário representados no grafo e respondendo às ações (`[reivindicacoes.md:7]`).
- **Instruções na documentação:** **Atendido na documentação.** `[README.md:88-91]` descreve arrastar o ícone `"Controller"` da barra lateral para o centro da tela, configurar o modal e gerar a topologia; `[README.md:96]` descreve o botão `"Create Link"` clicando e arrastando entre nós.
- **Implementação no código:** `[mininet-gui-frontend/src/components/NetworkGraph.vue:2-3, 138, 207-285, 416-440]` instancia `vis-network`, trata `handleDrop` para criar hosts, switches e controladores, atualiza posições via `handleNodeDragEnd` e gerencia arestas; `[mininet-gui-backend/mininet_gui_backend/api.py:161-295]` provê os endpoints correspondentes.
- **Verificação do resultado esperado:** **Só verificável por execução (`depende_execucao`).**

#### Reivindicação C2 — Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade
- **Fonte no artigo:** `[artigo.pdf:p.2, §1]` (*"2. Emulação integrada, eliminando a necessidade de configurações externas."*), `[artigo.pdf:pp.4-5, §3]`, `[artigo.pdf:p.6, §4, caso 1]`.
- **Resultado esperado:** nós emulados e resultado de `pingall` exibido na interface (`[reivindicacoes.md:8]`).
- **Instruções na documentação:** **Atendido na documentação.** `[README.md:88-93]` (*"Passo 6: Execute um teste de pingall clicando no botão "Run Pingall Test" na aba lateral esquerda e aguarde os resultados aparecerem."*).
- **Implementação no código:** `[mininet-gui-backend/mininet_gui_backend/api.py:40-53, 107-122, 152-159]` inicia a rede Mininet no `lifespan` e executa `app.net.pingFull()` em `POST /api/mininet/pingall`; `[mininet-gui-frontend/src/components/NetworkGraph.vue:494-502]` e `[mininet-gui-frontend/src/components/PingallResults.vue:1-64]` exibem a tabela de resultados no modal.
- **Verificação do resultado esperado:** **Só verificável por execução (`depende_execucao`).**

#### Reivindicação C3 — Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la
- **Fonte no artigo:** `[artigo.pdf:p.1, resumo]`, `[artigo.pdf:p.2, §1]` (*"3. Suporte a modificações na topologia em tempo real."*), `[artigo.pdf:p.6, §3]`.
- **Resultado esperado:** rede alterada enquanto a emulação continua ativa (`[reivindicacoes.md:9]`).
- **Instruções na documentação:** **Parcialmente atendido na documentação.** `[README.md:96]` (`Passo 8 (opcional)`) instrui adicionar novo controlador, nova subtopologia e novo link com a emulação já ativa e testar com `Pingall`, mas não inclui passo explícito de remoção de nós ou links.
- **Implementação no código:** `[mininet-gui-backend/mininet_gui_backend/api.py:161-267, 298-325]` adiciona/remove nós e links dinamicamente na instância `app.net` em execução, chamando `start` nos switches. No frontend, `[mininet-gui-frontend/src/components/NetworkGraph.vue:238-251]` implementa `deleteNode`, mas `deleteEdge` (`[mininet-gui-frontend/src/components/NetworkGraph.vue:252-274]`) referencia `dst` nas linhas 260–261 sem declará-la (`let src = this.nodes.get(link.from);` na linha 257 sem o correspondente `let dst = this.nodes.get(link.to);`), o que causaria `ReferenceError` ao remover um link pela interface na versão do repositório.
- **Verificação do resultado esperado:** **Só verificável por execução (`depende_execucao`).**

#### Reivindicação C4 — Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido (Reivindicação obrigatória para R)
- **Fonte no artigo:** `[artigo.pdf:p.2, §1]` (*"4. Geração automatizada de topologias, incluindo diversos modelos amplamente utilizados."*), `[artigo.pdf:p.6, §3]` (*"Topology Generator: oferece um mecanismo para geração automatizada de topologias de rede. Suporta os modelos single, linear e tree, com a quantidade de switches definida pelo usuário."*), `[artigo.pdf:pp.6-7, §4 e Fig. 2]`.
- **Resultado esperado:** topologia de cada modelo gerada com a quantidade de dispositivos escolhida, nos três modelos (`[reivindicacoes.md:10, 20]`).
- **Instruções na documentação:** **Atendido na documentação.**
  - `[README.md:105-108]`: `"## Reivindicação "Geração automatizada de topologias, incluindo diversos modelos amplamente utilizados" / Após inicializar o mininet_gui e acessar a interface web do frontend, clique no botão "Generate Topology". Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK."`
  - `[README.md:90]` (`Passo 5`): detalha o uso do botão `"Generate Topology"` e do botão `"Submit"` no modal.
- **Implementação no código:**
  - `[mininet-gui-frontend/src/components/TopologyForm.vue:5-44]`: formulário com `<select id="type" v-model="topologyType">` contendo `Single`, `Linear` e `Tree` e campos numéricos para quantidade de dispositivos/camadas (`Hosts` para Single; `Switches` e `Hosts per switch` para Linear; `Layers` e `Fanout` para Tree).
  - `[mininet-gui-frontend/src/components/NetworkGraph.vue:512-585, 608-617]`: métodos `createSingleTopo(nDevices, controller)`, `createLinearTopo(nDevices, nHosts, controller)`, `createTreeTopo(depth, fanout, controller)` e `handleCreateTopology`.
- **Verificação do resultado esperado:** **Só verificável por execução (`depende_execucao`).**

#### Reivindicação C5 — Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado (Reivindicação obrigatória para R)
- **Fonte no artigo:** `[artigo.pdf:p.1, resumo]`, `[artigo.pdf:p.2, §1]` (*"5. Terminal integrado dos nós via WebShell."*), `[artigo.pdf:pp.5-6, §3]`, `[artigo.pdf:p.6, §4, caso 2]`, `[artigo.pdf:p.7, Fig. 2]`.
- **Resultado esperado:** saída do comando exibida na aba do nó selecionado (`[reivindicacoes.md:11]`).
- **Instruções na documentação:** **Atendido na documentação.**
  - `[README.md:110-114]`: `"## Reivindicação "Terminal integrado dos nós via WebShell" / Após inicializar o mininet_gui e acessar a interface web do frontend, crie ao menos um nó (seja pelo Gerador de Topologias ou clicando e arrastando) e na aba inferior titulada "Webshell" selecione a aba com o nome desse nó, clicando nela. / Em seguida, utilize o terminal bash para executar comandos diretamente no namespace daquele nó."`
  - `[README.md:94, 96]`: exemplifica comandos `iperf -s`, `iperf -c 10.0.0.1` e `ryu-manager` no WebShell.
- **Implementação no código:**
  - `[mininet-gui-backend/mininet_gui_backend/api.py:450-491]`: endpoint `@app.websocket("/api/mininet/terminal/{node_id}")` que abre pseudoterminal (`pty.openpty()`) e executa `node.popen(["/bin/bash", "-i"], stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, text=True, close_fds=True)`.
  - `[mininet-gui-frontend/src/components/Webshell.vue:8-35, 68-161]`: renderiza abas por nó, conecta via WebSocket em `/api/mininet/terminal/${nodeId}`, envia teclas pressionadas e exibe a saída sanitizada do terminal.
- **Verificação do resultado esperado:** **Só verificável por execução (`depende_execucao`).**

#### Reivindicação C6 — Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches
- **Fonte no artigo:** `[artigo.pdf:p.2, §1]` (*"6. Visualização e criação das regras de fluxo."*), `[artigo.pdf:p.5, §3]` (*"Flow Rule Integration: oferece funcionalidades para edição e visualização das tabelas de fluxo dos dispositivos de rede."*), `[artigo.pdf:p.6, §3]` (*"Flow Rule Editor: consiste em uma ferramenta para visualização, criação e remoção de regras de fluxo OpenFlow nos switches."*).
- **Resultado esperado:** tabela de fluxo exibida, com a regra inserida ou removida no switch (`[reivindicacoes.md:12]`).
- **Instruções na documentação:** **Não atendido.** O `README.md` não menciona visualização, criação ou remoção de regras de fluxo em nenhuma seção (`[reivindicacoes.md:12]`).
- **Implementação no código:** **Não atendido (implementação incompleta).**
  - A visualização somente-leitura da tabela de fluxos existe quando se dá duplo clique em um switch (`[mininet-gui-frontend/src/components/NetworkGraph.vue:277-281]`), abrindo `NodeStats.vue` com a aba `"Flow Table"` (`[mininet-gui-frontend/src/components/NodeStats.vue:36-38, 62-93]`), alimentada por `node.dpctl("dump-flows")` em `GET /api/mininet/stats/{node_id}` (`[mininet-gui-backend/mininet_gui_backend/api.py:363-383]`).
  - Contudo, **não existe no código** do backend (`[mininet-gui-backend/mininet_gui_backend/api.py:1-491]`) nem do frontend (`[mininet-gui-frontend/src/core/api.js:1-342]`, `[mininet-gui-frontend/src/components/NodeStats.vue:1-180]`) qualquer endpoint, formulário ou componente (`Flow Rule Editor`) para **criar** ou **remover** regras de fluxo pela interface.
- **Verificação do resultado esperado:** **Não reproduzível (`nao_reproduzivel`).**

### 3. Decisão para o Selo R
- **Decisão:** **Indeterminado**
- **Justificativa:** De acordo com a regra fixada em `[reivindicacoes.md:16]`, *"R é atribuído se C4 e C5 forem reproduzidas. C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R."* Tanto C4 quanto C5 possuem instruções de execução no `README.md` (`[README.md:105-114]`) e implementação completa correspondente no código (`TopologyForm.vue`, `NetworkGraph.vue`, `Webshell.vue`, `api.py`), de modo que nenhum critério obrigatório para R falha na documentação, mas a confirmação da reprodução de C4 (nos três modelos: Single, Linear e Tree) e C5 depende da execução.
- **Confiança (0 a 100) de que o comitê oficial atribuiu o selo R:** **80** (a seção `# Experimentos` do `README.md` delimita especificamente as reivindicações C4 e C5, ambas implementadas e demonstráveis na VM pré-configurada).
- **O que precisaria ser observado na execução para mudar a decisão:**
  - **Para mudar para Atribuir:** Executar o Mininet-GUI, acionar `"Generate Topology"` e observar a criação correta das topologias nos três modelos (`Single`, `Linear` e `Tree`) com o número de dispositivos escolhido (**C4**), e abrir a aba `"WebShell"` de um nó emulado, executar comandos Bash (como `ifconfig`, `ping` ou `iperf`) e observar a saída exibida na aba do nó selecionado (**C5**).
  - **Para mudar para Não atribuir:** Observar falha em qualquer um dos três modelos de geração de topologia (`Single`, `Linear` ou `Tree`) em **C4** ou falha na conexão WebSocket/execução de comandos Bash no WebShell em **C5** (ou falha geral de execução da aplicação).

---

## D. Lacunas e riscos

1. **Erro de sintaxe JavaScript no repositório (`api.js`):** Em `[mininet-gui-frontend/src/core/api.js:299]` (`[artefato.txt:4752]`), há um caractere `"i"` espúrio após a chave de fechamento do bloco `catch` da função `requestRunPingall` (`"  }i"`). Na instalação manual a partir do commit `465648a4425a4457af0348ab951cf7f71d37a86f`, o parser do Vite/ES Module acusará `SyntaxError` ao carregar `src/core/api.js`, impedindo o funcionamento do frontend até que o caractere seja removido (embora a VM `.ova` recomendada em `[README.md:49-57]` possa conter uma árvore sem esse erro de digitação).
2. **Bug na remoção de links (`deleteEdge`) no frontend:** Em `[mininet-gui-frontend/src/components/NetworkGraph.vue:256-265]` (`[artefato.txt:3048-3057]`), o método `deleteEdge` declara `let src = this.nodes.get(link.from);`, mas omite a declaração de `dst` antes de acessar `console.log("dst", dst);` e `dst.type == "controller"`, causando `ReferenceError: dst is not defined` ao tentar excluir uma aresta pela interface gráfica (afetando parte de C3).
3. **Funcionalidade ausente para edição de regras de fluxo (C6):** O artigo reivindica um módulo *"Flow Rule Editor: consiste em uma ferramenta para visualização, criação e remoção de regras de fluxo OpenFlow nos switches"* (`[artigo.pdf:p.6, §3]`) e a contribuição 6 (`[artigo.pdf:p.2, §1]`), mas o código implementa apenas a visualização da tabela (`dump-flows` em `[mininet-gui-backend/mininet_gui_backend/api.py:363-383]` e `[mininet-gui-frontend/src/components/NodeStats.vue:62-93]`), sem funcionalidades de criação ou remoção de regras e sem documentação no `README.md`.
4. **Pequenas inconsistências no `README.md`:**
   - Divergência nos requisitos de memória RAM para a VM: `[README.md:38]` indica *"Mínimo de 8GB para a máquina virtual"*, enquanto `[README.md:103]` indica *"A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM"*.
   - Em `[README.md:108]`, a instrução de C4 diz *"então clique em OK"*, enquanto o botão real no componente `[mininet-gui-frontend/src/components/TopologyForm.vue:43]` (e no Passo 5 do próprio `[README.md:91]`) é rotulado como `"Submit"`.
   - Caminhos fixos (`/home/mininet/mininet-gui`) em `[setup.sh:5]` e `[run.sh:7]`, exigindo que o usuário do sistema na instalação manual também se chame `mininet` ou edite os scripts.

```json
{"F": {"decisao": "Indeterminado", "confianca": 85, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:26-39", "README.md:47-99", "run.sh:1-28", "setup.sh:1-24", "mininet-gui-frontend/src/core/api.js:299"]},
 "R": {"decisao": "Indeterminado", "confianca": 80, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:5-20", "README.md:80-115", "mininet-gui-frontend/src/components/TopologyForm.vue:1-73", "mininet-gui-frontend/src/components/NetworkGraph.vue:512-617", "mininet-gui-frontend/src/components/Webshell.vue:1-192", "mininet-gui-backend/mininet_gui_backend/api.py:347-384", "mininet-gui-backend/mininet_gui_backend/api.py:450-491", "mininet-gui-frontend/src/components/NodeStats.vue:36-93"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "depende_execucao", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

# Roteiro de Execução e Verificação — Mininet-GUI (Selos F e R)

> **Nota:** Este roteiro foi elaborado exclusivamente por análise estática de `artigo.pdf`, `artefato.txt` (commit `465648a4425a4457af0348ab951cf7f71d37a86f`), `instrucoes-oficiais.md` e `reivindicacoes.md`. Nenhuma execução foi realizada.

---

## 1. Requisitos de Hardware e Software do Ambiente

### Hardware (segundo `README.md:26-39, 103`)
- **Máquina hospedeira de referência (`README.md:26-32`):**
  - **Processador:** Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz (baseado em x64, 64 bits) ou equivalente com suporte a virtualização.
  - **Memória RAM instalada no host:** 8,00 GB.
  - **Espaço disponível em disco:** Pelo menos 80 GB livres.
- **Alocação para a Máquina Virtual (VM):**
  - **Memória RAM da VM:** Mínimo de 8 GB informado em `README.md:38` (*"Memória RAM: Mínimo de 8GB para a máquina virtual"*), ou mínimo de 2 GB de RAM e 1 core de CPU informado em `README.md:103` (*"A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM"*). Recomenda-se alocar entre 2 GB e 8 GB conforme disponibilidade do host.

### Software (segundo `README.md:30, 37, 49-78`, `setup.sh:1-24`, `mininet-gui-backend/requirements.txt:1-4`, `mininet-gui-frontend/package.json:10-23`)
- **Opção A — Máquina Virtual pré-configurada (recomendado pelos autores em `README.md:43-57`):**
  - Sistema Operacional Host: Windows 11 64 bits (`README.md:30`) ou sistema compatível com VirtualBox.
  - Hipervisor: Oracle VirtualBox versão `7.1.6 r167084` (`README.md:37, 51`).
  - Imagem da VM: `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (link no `README.md:53`; credenciais: usuário `mininet`, senha `mininet`, `README.md:57`).
- **Opção B — Instalação manual (`README.md:60-78`, `setup.sh:1-24`):**
  - Sistema Operacional: Ubuntu 20.04 (`README.md:63`), com usuário `mininet` e diretório `/home/mininet/mininet-gui` (caminhos fixos em `setup.sh:5` e `run.sh:7`).
  - Pacotes de sistema e rede: `git`, `curl`, `npm`, `python3`, `pip3`, Mininet (`./util/install.sh -nfv`, que instala Open vSwitch, `iperf`, `dpctl`, etc.).
  - Backend Python: `fastapi`, `websockets`, `uvicorn`, `python-multipart` (`mininet-gui-backend/requirements.txt:1-4`) e opcionalmente `ryu`, `eventlet==0.30.0`, `dnspython==1.16.0` (`README.md:77`).
  - Frontend Node.js: `nvm` `v0.40.2`, Node.js `18.20.7` (`setup.sh:13-19`), pacotes npm (`vue ^3.2.45`, `vite ^4.0.0`, `vis-network ^9.1.2`, `vis-data ^7.1.4`, `axios ^1.2.1`, etc. em `mininet-gui-frontend/package.json:10-23`).
  - Navegador Web com suporte a ES6 e WebSockets.

---

## 2. Preparação e Instalação do Ambiente

### Passo P1 — Importação da Máquina Virtual (ou Instalação Manual)
- **Identificador:** P1
- **Selo e reivindicação relacionados:** Selo F e Selo R (pré-requisito geral para C1–C6)
- **Diretório:** Host local (para VirtualBox) ou `/home/mininet` dentro de Ubuntu 20.04 (para instalação manual)
- **Comando exato:**
  - **Via VM (recomendado, `README.md:53-57`):**
    1. Baixar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` de `https://drive.[REMOVIDO]/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing`
    2. Abrir e importar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no Oracle VirtualBox.
    3. Iniciar a VM e autenticar com usuário `mininet` e senha `mininet`.
  - **Alternativa via Instalação Manual (`README.md:65-78`):**
    ```bash
    git clone https://github.com/mininet/mininet
    cd mininet
    ./util/install.sh -nfv
    cd ..
    git clone https://github.com/latarc/mininet-gui
    cd mininet-gui
    ./setup.sh
    pip3 install ryu eventlet==0.30.0 dnspython==1.16.0
    source ~/.bashrc
    ```
- **Resultado esperado segundo os autores:** Máquina virtual iniciada e autenticada com o usuário `mininet` (`README.md:57, 82`), ou dependências de backend, Mininet, Node `18.20.7` e alias `mininet_gui` instalados (`README.md:65-78`, `setup.sh:9-24`).
- **Evidência a salvar:** Captura de tela da sessão logada na VM (ou log completo do terminal da execução de `./setup.sh` e `pip3 install`).
- **Critério de sucesso:** Login concluído na VM com diretório `/home/mininet/mininet-gui` presente (ou término de `setup.sh` sem erros fatais).
- **Critério de falha:** Link do arquivo `.ova` inacessível/corrompido e falha na instalação manual de dependências (`mininet`, `uvicorn`, `node 18.20.7` ou pacotes npm).
- **Critério de interrupção:** Interromper a avaliação caso nem a VM possa ser importada/iniciada nem a instalação manual conclua a instalação do Mininet, FastAPI/Uvicorn e Vite/Node.

---

### Passo P2 — [NÃO DOCUMENTADO] Inspeção e saneamento de erros de sintaxe do commit no frontend
- **Identificador:** P2 `[NÃO DOCUMENTADO]`
- **Justificativa da necessidade:** No código do commit `465648a4425a4457af0348ab951cf7f71d37a86f` (`artefato.txt:4752`), o arquivo `mininet-gui-frontend/src/core/api.js` possui um caractere `i` espúrio na linha 299 (`}i`), que gera `SyntaxError` no Vite e impede o carregamento do frontend. Além disso, `mininet-gui-frontend/src/components/NetworkGraph.vue:257-261` (`artefato.txt:3049-3053`) usa a variável `dst` sem declará-la em `deleteEdge`. É necessário inspecionar se a VM já está corrigida ou se o erro está presente antes de executar os testes.
- **Selo e reivindicação relacionados:** Selo F e Selo R (C1–C5)
- **Diretório:** `/home/mininet/mininet-gui`
- **Comando exato:**
  ```bash
  nl -ba mininet-gui-frontend/src/core/api.js | sed -n '295,301p'
  nl -ba mininet-gui-frontend/src/components/NetworkGraph.vue | sed -n '252,266p'
  ```
  *(Nota: Caso a execução com o código original no Passo P3 falhe no navegador por `SyntaxError` em `api.js:299`, registrar a falha do código original e aplicar a correção mínima `sed -i '299s/}i/}/' mininet-gui-frontend/src/core/api.js` para prosseguir com a verificação das demais funcionalidades).*
- **Resultado esperado segundo os autores:** Não documentado pelos autores (autores assumem execução direta via `run.sh`).
- **Evidência a salvar:** Saída no terminal dos comandos `nl -ba` mostrando o estado original dos arquivos na VM/repositório.
- **Critério de sucesso:** Identificação clara do estado dos arquivos `api.js` e `NetworkGraph.vue` antes da execução.
- **Critério de falha:** Diretório `/home/mininet/mininet-gui` inexistente na VM.
- **Critério de interrupção:** Não interrompe (passo diagnóstico/preparatório).

---

## 3. Teste Mínimo — Verificação do Selo F (`README.md:80-99`)

### Passo P3 — Inicialização do Mininet-GUI e acesso à interface web (Teste mínimo, Passos 2 e 3)
- **Identificador:** P3
- **Selo e reivindicação relacionados:** Selo F; embasa C1 e C2
- **Diretório:** `/home/mininet` (ou `/home/mininet/mininet-gui`)
- **Comando exato:**
  No terminal da VM (`Ctrl+Alt+T`), conforme `README.md:84-86`:
  ```bash
  mininet_gui
  ```
  *(ou alternativamente `/home/mininet/mininet-gui/run.sh`)*
  Em seguida, abrir o navegador dentro da VM e acessar a URL exibida na saída do terminal (ex.: `http://10.0.2.15:5173`).
- **Resultado esperado segundo os autores:** O script exibe `#### Mininet-GUI is available at: ####` seguido de `http://<IP>:5173` (`run.sh:27-28`, `README.md:86`), e o navegador carrega a interface web contendo a barra lateral esquerda (`Topology Controls`, `Actions`, `Export/Import`, `Nodes Palette`), a área central do grafo e o painel inferior `WebShell` (`artigo.pdf:p.7, Fig. 2`).
- **Evidência a salvar:** Saída do terminal ao rodar `mininet_gui`, arquivos de log `/home/mininet/mininet-gui/mininet-gui-backend/nohup.out` e `/home/mininet/mininet-gui/mininet-gui-frontend/nohup.out` (`run.sh:23-24`) e captura de tela do navegador com a interface carregada (e console do navegador F12).
- **Critério de sucesso:** Backend Uvicorn ativo na porta `8000`, frontend Vite ativo na porta `5173` e interface gráfica renderizada no navegador.
- **Critério de falha:** Tela em branco no navegador causada por erro de compilação no Vite (ex.: `SyntaxError` em `api.js:299`) ou falha do `uvicorn` ao iniciar o Mininet em `mininet-gui-backend/nohup.out`.
- **Critério de interrupção:** Se a interface ficar em branco devido a `}i` em `mininet-gui-frontend/src/core/api.js:299`, registrar a evidência para o Selo F, corrigir a linha 299 conforme descrito em P2, reiniciar `/home/mininet/mininet-gui/run.sh` e recarregar a página; se ainda assim o backend ou frontend não iniciarem, interromper a execução.

---

### Passo P4 — Criação de um Controlador Padrão no Grafo (Teste mínimo, Passo 4)
- **Identificador:** P4
- **Selo e reivindicação relacionados:** Selo F; C1
- **Diretório:** Interface web no navegador (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:88`:
  1. Na barra lateral esquerda (`Nodes Palette`), arrastar o ícone rotulado `"Controller"` para o centro da área do grafo.
  2. Na caixa de diálogo (`Controller Form`) que se abre, manter/selecionar a opção `"Default"` em `Controller Type`.
  3. Clicar no botão `"Submit"`.
- **Resultado esperado segundo os autores:** O modal fecha e o nó controlador `c1` passa a ser exibido no grafo interativo e uma aba `C1` aparece no painel inferior `WebShell` (`README.md:88`, `artigo.pdf:p.7, Fig. 2`).
- **Evidência a salvar:** Captura de tela do modal `Controller Form` e do grafo exibindo o nó `c1` criado.
- **Critério de sucesso:** Nó `c1` visível no grafo e requisição `POST /api/mininet/controllers` retornando status 200.
- **Critério de falha:** Modal não abre ao soltar o ícone, ou erro `"Network Error"` / HTTP 400/500 ao submeter.
- **Critério de interrupção:** Não interrompe, mas impede a associação de controlador nos passos seguintes se falhar.

---

### Passo P5 — Geração de Topologia Single com 2 Hosts (Teste mínimo, Passo 5)
- **Identificador:** P5
- **Selo e reivindicação relacionados:** Selo F; C1, C2, C4 (modelo Single)
- **Diretório:** Interface web no navegador (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:90`:
  1. Clicar no botão `"Generate Topology"` na barra lateral esquerda (`Topology Controls`).
  2. No modal `Create Topology`, selecionar:
     - `Topology Type`: `Single`
     - `Controller`: `c1`
     - `Hosts`: `2`
  3. Clicar no botão `"Submit"`.
- **Resultado esperado segundo os autores:** Um switch (`s1 <00:00:00:00:00:00:00:01>`) conectado ao controlador `c1` (linha tracejada cinza) e a 2 hosts (`h1` e `h2`, com linhas contínuas verdes indicando links ativos) é exibido no grafo (`README.md:90`, `artigo.pdf:p.7`).
- **Evidência a salvar:** Captura de tela do modal preenchido e do grafo resultante com `c1`, `s1`, `h1` e `h2`.
- **Critério de sucesso:** Nós `s1`, `h1` e `h2` e respectivos links criados no grafo e abas `S1`, `H1`, `H2` adicionadas ao `WebShell`.
- **Critério de falha:** Nós ou links não aparecem no grafo ou alerta de erro de rede/API é exibido.
- **Critério de interrupção:** Interromper se a criação básica de switches/hosts no Mininet falhar no backend.

---

### Passo P6 — Teste de Conectividade com Pingall (Teste mínimo, Passo 6)
- **Identificador:** P6
- **Selo e reivindicação relacionados:** Selo F; C2
- **Diretório:** Interface web no navegador (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:92`:
  1. Clicar no botão `"Run Pingall Test"` na barra lateral esquerda (`Actions`).
  2. Aguardar os resultados aparecerem no modal `"Pingall Results"`.
- **Resultado esperado segundo os autores:** Abre-se o modal `"Pingall Results"` exibindo a tabela de conectividade entre `h1` e `h2` (`src`, `dst`, `packets_sent`, `packets_recv`, `min`, `avg`, `max`, `mdev`) com pacotes recebidos com sucesso (`1/1`) (`README.md:92`, `PingallResults.vue:30-62`).
- **Evidência a salvar:** Captura de tela do modal `"Pingall Results"` com os dados de ping entre `h1` e `h2`.
- **Critério de sucesso:** Tabela exibida no modal com `packets_sent: 1` e `packets_recv: 1` para `h1 -> h2` e `h2 -> h1`.
- **Critério de falha:** Modal permanece em `"No ping results available."` após a resposta da API ou erro HTTP 400/500.
- **Critério de interrupção:** Não interrompe.

---

### Passo P7 — Teste de Desempenho com Iperf no WebShell (Teste mínimo, Passo 7 opcional)
- **Identificador:** P7
- **Selo e reivindicação relacionados:** Selo F; C5 (e Caso de Uso 2 do artigo, `artigo.pdf:p.6, §4`)
- **Diretório:** Painel inferior `WebShell` na interface web (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:94`:
  1. Fechar o modal de Pingall (`X` ou `Esc`).
  2. No painel inferior `WebShell`, clicar na aba `H1`, clicar na janela do terminal e digitar:
     ```bash
     iperf -s
     ```
  3. No painel inferior `WebShell`, clicar na aba `H2`, clicar na janela do terminal e digitar:
     ```bash
     iperf -c 10.0.0.1
     ```
  4. Aguardar até 1 minuto para a conclusão do teste.
- **Resultado esperado segundo os autores:** O terminal da aba `H1` exibe o servidor `iperf` escutando na porta 5001 e o terminal da aba `H2` (e `H1`) exibe o relatório de transferência e largura de banda medida entre `10.0.0.2` (`h2`) e `10.0.0.1` (`h1`) (`README.md:94`, `artigo.pdf:p.6, §4, caso 2`).
- **Evidência a salvar:** Capturas de tela das abas `H1` e `H2` do `WebShell` mostrando a saída do `iperf`.
- **Critério de sucesso:** Comandos executados via WebSocket nos namespaces de `h1` e `h2` com saída do `iperf` renderizada no componente `WebShell`.
- **Critério de falha:** Terminal WebShell não conecta ao WebSocket, não aceita digitação ou não retorna saída.
- **Critério de interrupção:** Não interrompe.

---

### Passo P8 — Múltiplos Controladores e Modificação em Tempo Real (Teste mínimo, Passo 8 opcional)
- **Identificador:** P8
- **Selo e reivindicação relacionados:** Selo F; C1, C2, C3, C5 (e Caso de Uso 3 do artigo, `artigo.pdf:p.7, §4`)
- **Diretório:** Interface web (`http://<IP>:5173`) e `WebShell`
- **Comando exato:**
  Conforme `README.md:96`:
  1. Arrastar um novo ícone `"Controller"` da barra lateral para o centro da tela.
  2. No modal `Controller Form`, alterar `Controller Type` para `"Remote"`, preencher `IP`: `127.0.0.1` e `Port`: `6633`, e clicar em `"Submit"` (criando `c2`).
  3. Clicar em `"Generate Topology"`, selecionar `Topology Type`: `Single`, `Controller`: `c2`, `Hosts`: `2`, e clicar em `"Submit"` (criando `s2`, `h3`, `h4` com a emulação já em andamento).
  4. Clicar no botão `"Create Link"` na barra lateral esquerda e conectar os switches `s1` e `s2` clicando e arrastando de um para o outro.
  5. No painel `WebShell`, selecionar a aba do controlador `C2` e executar:
     ```bash
     ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13
     ```
  6. Clicar no botão `"Run Pingall Test"` na barra lateral esquerda.
- **Resultado esperado segundo os autores:** Uma linha verde conecta `s1` e `s2`, o controlador SDN Ryu inicia na aba `C2` do WebShell escutando na porta `6633`, e o teste de `Pingall` mostra conectividade entre todos os 4 hosts (`h1`, `h2`, `h3`, `h4`) das duas sub-redes sem necessidade de reiniciar a emulação (`README.md:96`).
- **Evidência a salvar:** Captura de tela do grafo com as duas subtopologias interligadas (`s1`–`s2`), da aba `C2` no WebShell rodando `ryu-manager` e do modal `"Pingall Results"` com os 4 hosts.
- **Critério de sucesso:** Adição dinâmica de `c2`, `s2`, `h3`, `h4` e do link `s1`–`s2` com a rede em execução e `pingall` bem-sucedido entre os hosts.
- **Critério de falha:** Falha ao criar link `s1`–`s2`, erro ao iniciar `ryu-manager` (ex.: `ryu` não instalado) ou falta de conectividade entre os switches após iniciar o controlador.
- **Critério de interrupção:** Não interrompe.

---

### Passo P9 — Exportação da Topologia em JSON e Script Python (Teste mínimo, Passo 9)
- **Identificador:** P9
- **Selo e reivindicação relacionados:** Selo F
- **Diretório:** Interface web (`http://<IP>:5173`) e diretório de downloads do navegador
- **Comando exato:**
  Conforme `README.md:98`:
  1. Clicar no botão `"Export Topology (JSON)"` na barra lateral esquerda (`Export/Import`).
  2. Clicar no botão `"Export Mininet Script"` na barra lateral esquerda (`Export/Import`).
- **Resultado esperado segundo os autores:** O navegador baixa os arquivos `network_export.json` (contendo `switches`, `hosts`, `controllers` e `links` em JSON) e `network_export.py` (script Python compatível com a API do Mininet), análogos aos arquivos `example_network_export.json` e `example_network_export.py` do repositório (`README.md:12, 98`, `api.js:219-281`).
- **Evidência a salvar:** Os dois arquivos baixados (`network_export.json` e `network_export.py`).
- **Critério de sucesso:** Ambos os arquivos são baixados e contêm os nós e links correspondentes à topologia ativa no grafo.
- **Critério de falha:** Download não ocorre ou arquivos gerados estão vazios/inválidos.
- **Critério de interrupção:** Não interrompe.

---

## 4. Verificação do Selo R — Blocos por Reivindicação (`reivindicacoes.md`)

> **Regra do Selo R (`reivindicacoes.md:14-20`):** Na seção `"Experimentos"`, o `README.md` marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 (nos três modelos: Single, Linear e Tree) e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R; ainda assim, todas as seis reivindicações possuem blocos de verificação abaixo.

---

### Bloco da Reivindicação C1 — Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo
- **Reivindicação (`reivindicacoes.md:7`):** Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo (`artigo.pdf:p.1; p.2, §1; pp.4-6, §3; p.7, Fig. 2`).
- **Resultado esperado (`reivindicacoes.md:7`):** Elementos criados pelo usuário representados no grafo e respondendo às ações.
- **Cobertura pelo Teste Mínimo:** Parcialmente verificada em **P4**, **P5** e **P8**. Complementada pelo passo **P10** abaixo para verificar a criação manual individual de `Host` e `Switch` via arrastar-e-soltar e o reposicionamento no grafo.

#### Passo P10 — [NÃO DOCUMENTADO] Criação manual de Host e Switch por Drag-and-Drop e movimentação no grafo
- **Identificador:** P10 `[NÃO DOCUMENTADO]`
- **Justificativa da necessidade:** O `README.md:88, 96, 112` menciona criar nós *"clicando e arrastando"*, mas o passo a passo do Teste Mínimo só instrui arrastar o ícone `"Controller"`, criando switches e hosts apenas via `"Generate Topology"`. Para verificar integralmente C1 (manipulação direta de hosts, switches, controladores e links no grafo), é necessário arrastar manualmente um `Host` e um `Switch` da paleta `Nodes Palette`, conectá-los e movê-los no canvas.
- **Selo e reivindicação relacionados:** Selo F e Selo R (C1)
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  1. Clicar em `"Reset Topology"` na barra lateral esquerda e confirmar no diálogo do navegador (`OK`).
  2. Arrastar o ícone `"Host"` de `Nodes Palette` para o grafo; arrastar o ícone `"Switch"` de `Nodes Palette` para o grafo; arrastar o ícone `"Controller"` (`Default` -> `"Submit"`).
  3. Clicar em `"Create Link"`, arrastar do `Switch` (`s1`) para o `Controller` (`c1`) e depois do `Host` (`h1`) para o `Switch` (`s1`).
  4. Clicar e arrastar o nó `h1` para uma nova posição no grafo.
- **Resultado esperado segundo os autores:** Os ícones de `h1`, `s1` e `c1` aparecem no grafo nas posições escolhidas, a associação `s1`–`c1` é exibida como linha pontilhada cinza, o link `h1`–`s1` como linha verde contínua, e a nova posição do nó é atualizada (`artigo.pdf:p.7`, `NetworkGraph.vue:209-237, 416-440`).
- **Evidência a salvar:** Captura de tela do grafo após criar e mover manualmente `h1`, `s1` e `c1`.
- **Critério de sucesso:** Criação manual dos três tipos de nós, criação dos links e atualização de posição sem erros.
- **Critério de falha:** Falha no evento de drop ou na criação de links manuais.
- **Critério de interrupção:** Não interrompe.

---

### Bloco da Reivindicação C2 — Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade
- **Reivindicação (`reivindicacoes.md:8`):** Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade (`artigo.pdf:p.2, §1; pp.4-5, §3; p.6, §4, caso 1`).
- **Resultado esperado (`reivindicacoes.md:8`):** Nós emulados e resultado de `pingall` exibido na interface.
- **Verificação:** Totalmente coberta pelos passos **P5** e **P6** (e **P8**) do Teste Mínimo (`README.md:88-93`), onde a topologia é instanciada diretamente no Mininet pelo backend e o teste `"Run Pingall Test"` exibe os resultados na interface.

---

### Bloco da Reivindicação C3 — Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la
- **Reivindicação (`reivindicacoes.md:9`):** Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la (`artigo.pdf:p.1; p.2, §1; p.6, §3; p.7`).
- **Resultado esperado (`reivindicacoes.md:9`):** Rede alterada enquanto a emulação continua ativa.
- **Cobertura pelo Teste Mínimo:** A criação em tempo real de nós e links com a emulação ativa é verificada em **P8** (`README.md:96`). Falta apenas verificar a **remoção** de nós e links em tempo real (**P11**).

#### Passo P11 — [NÃO DOCUMENTADO] Remoção de link e de nó em tempo real com a emulação ativa
- **Identificador:** P11 `[NÃO DOCUMENTADO]`
- **Justificativa da necessidade:** A reivindicação C3 inclui *"criar e remover nós e links com a emulação em andamento, sem reiniciá-la"* (`reivindicacoes.md:9`), mas o `README.md` não documenta um passo de remoção. Além disso, a análise estática identificou um provável bug em `deleteEdge` (`NetworkGraph.vue:256-265`, variável `dst` não declarada).
- **Selo e reivindicação relacionados:** Selo F e Selo R (C3)
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  1. Com uma topologia ativa no grafo (ex.: `c1`, `s1`, `h1`, `h2` criada como em P5), clicar sobre o link entre `h2` e `s1` para selecioná-lo e clicar no botão `"Delete Selected"` na barra lateral esquerda (ou pressionar a tecla `Delete`/`d`).
  2. Selecionar o nó `h2` no grafo e clicar no botão `"Delete Selected"`.
  3. Verificar no console do navegador (`F12 -> Console`) e na aba `WebShell` (ou via `"Run Pingall Test"`) se a remoção ocorreu com a emulação ativa.
- **Resultado esperado segundo os autores:** O link e o nó selecionados são removidos do grafo e da instância do Mininet sem interromper a emulação (`artigo.pdf:p.6, §3`, `Side.vue:35-38`, `api.py:298-325`).
- **Evidência a salvar:** Captura de tela do grafo e do Console do navegador (`F12`) ao acionar `"Delete Selected"` para uma aresta e para um nó.
- **Critério de sucesso:** Tanto o nó quanto o link são removidos da interface e do Mininet (`DELETE /api/mininet/delete_node/...` e `DELETE /api/mininet/delete_link/...`) mantendo a emulação ativa.
- **Critério de falha:** Exclusão de link lança `ReferenceError: dst is not defined` no console do navegador (`NetworkGraph.vue:260`) e não envia a requisição `DELETE /api/mininet/delete_link` ao backend.
- **Critério de interrupção:** Não interrompe.

---

### Bloco da Reivindicação C4 — Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido (Obrigatória para o Selo R)
- **Reivindicação (`reivindicacoes.md:10, 16, 20`):** Geração automatizada de topologias nos modelos `Single`, `Linear` e `Tree`, com número de dispositivos escolhido (`artigo.pdf:p.2, §1; p.6, §3; pp.6-7, §4 e Fig. 2`). **Critério obrigatório para R:** deve ser observada nos **três modelos** (`reivindicacoes.md:20`).
- **Procedimento dos autores (`README.md:105-108`):** *"Após inicializar o mininet_gui e acessar a interface web do frontend, clique no botão "Generate Topology". Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK [Submit]."*

#### Passo P12 — Reprodução de C4 no modelo Single
- **Identificador:** P12
- **Selo e reivindicação relacionados:** Selo R (C4 — Modelo 1 de 3: `Single`)
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:90, 107-108`:
  1. Clicar em `"Reset Topology"` e confirmar (`OK`) para limpar o grafo `[NÃO DOCUMENTADO na seção Experimentos, necessário para isolar a visualização do modelo]`.
  2. Arrastar um `"Controller"` (`Default` -> `"Submit"`) para criar `c1`.
  3. Clicar no botão `"Generate Topology"`.
  4. Selecionar `Topology Type`: `Single`, `Controller`: `c1`, `Hosts`: `3` e clicar em `"Submit"`.
- **Resultado esperado segundo os autores:** Topologia `Single` gerada automaticamente no grafo contendo 1 switch (`s1`) associado a `c1` e conectado aos 3 hosts (`h1`, `h2`, `h3`) (`README.md:90, 107-108`, `NetworkGraph.vue:512-523`).
- **Evidência a salvar:** Captura de tela do modal `Create Topology` configurado para `Single` e do grafo gerado com 1 switch e 3 hosts.
- **Critério de sucesso:** 1 switch e 3 hosts criados e interligados no grafo e no Mininet.
- **Critério de falha:** Topologia não é gerada ou quantidade de dispositivos difere da escolhida.
- **Critério de interrupção:** Se falhar, C4 não é reproduzida nos três modelos (impacta diretamente o Selo R).

#### Passo P13 — Reprodução de C4 no modelo Linear
- **Identificador:** P13
- **Selo e reivindicação relacionados:** Selo R (C4 — Modelo 2 de 3: `Linear`)
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:107-108` e campos do formulário em `TopologyForm.vue:23-32`:
  1. Clicar em `"Reset Topology"` e confirmar (`OK`) `[NÃO DOCUMENTADO na seção Experimentos, necessário para limpar a topologia anterior]`.
  2. Arrastar um `"Controller"` (`Default` -> `"Submit"`) para criar `c1`.
  3. Clicar no botão `"Generate Topology"`.
  4. Selecionar `Topology Type`: `Linear`, `Controller`: `c1`, preencher `Switches`: `3` e `Hosts per switch`: `2` `[campo adicional obrigatório no formulário TopologyForm.vue:29-31, não detalhado nominalmente no README]`, e clicar em `"Submit"`.
- **Resultado esperado segundo os autores:** Topologia `Linear` gerada automaticamente no grafo contendo 3 switches (`s1`, `s2`, `s3`) conectados em linha (`s1`–`s2`–`s3`), cada um conectado a 2 hosts (total de 6 hosts, `h1` a `h6`) e associados a `c1` (`README.md:107-108`, `NetworkGraph.vue:524-552`).
- **Evidência a salvar:** Captura de tela do modal `Create Topology` configurado para `Linear` e do grafo gerado com 3 switches em linha e 6 hosts.
- **Critério de sucesso:** 3 switches encadeados linearmente e 2 hosts por switch criados no grafo e no Mininet.
- **Critério de falha:** Switches não são interligados em cadeia ou número de switches/hosts difere do informado.
- **Critério de interrupção:** Se falhar, C4 não é reproduzida nos três modelos (impacta diretamente o Selo R).

#### Passo P14 — Reprodução de C4 no modelo Tree
- **Identificador:** P14
- **Selo e reivindicação relacionados:** Selo R (C4 — Modelo 3 de 3: `Tree`)
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  Conforme `README.md:107-108` e campos do formulário em `TopologyForm.vue:33-42`:
  1. Clicar em `"Reset Topology"` e confirmar (`OK`) `[NÃO DOCUMENTADO na seção Experimentos, necessário para limpar a topologia anterior]`.
  2. Arrastar um `"Controller"` (`Default` -> `"Submit"`) para criar `c1`.
  3. Clicar no botão `"Generate Topology"`.
  4. Selecionar `Topology Type`: `Tree`, `Controller`: `c1`, preencher `Layers`: `2` e `Fanout`: `2` `[campos obrigatórios no formulário TopologyForm.vue:35-41, correspondentes a depth e fanout]`, e clicar em `"Submit"`.
- **Resultado esperado segundo os autores:** Topologia em árvore (`Tree`) gerada automaticamente no grafo com profundidade (`Layers`) 2 e fator de ramificação (`Fanout`) 2, contendo 1 switch raiz, 2 switches agregadores no nível seguinte e 4 hosts nas folhas (`h1` a `h4`), análoga à árvore ilustrada na Figura 2 do artigo (`artigo.pdf:p.7, Fig. 2`, `README.md:107-108`, `NetworkGraph.vue:553-585`).
- **Evidência a salvar:** Captura de tela do modal `Create Topology` configurado para `Tree` (`Layers: 2`, `Fanout: 2`) e do grafo em árvore gerado.
- **Critério de sucesso:** Estrutura hierárquica em árvore criada com `2^0 + 2^1 = 3` switches e `2^2 = 4` hosts conectados corretamente.
- **Critério de falha:** Estrutura em árvore não é gerada ou conexões entre camadas falham.
- **Critério de interrupção:** Se falhar, C4 não é reproduzida nos três modelos (impacta diretamente o Selo R).

---

### Bloco da Reivindicação C5 — Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado (Obrigatória para o Selo R)
- **Reivindicação (`reivindicacoes.md:11, 16`):** Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado (`artigo.pdf:p.1; p.2, §1; pp.5-6, §3; p.6, §4, caso 2; p.7, Fig. 2`). **Critério obrigatório para R.**
- **Procedimento dos autores (`README.md:110-114`):** *"Após inicializar o mininet_gui e acessar a interface web do frontend, crie ao menos um nó (seja pelo Gerador de Topologias ou clicando e arrastando) e na aba inferior titulada "Webshell" selecione a aba com o nome desse nó, clicando nela. Em seguida, utilize o terminal bash para executar comandos diretamente no namespace daquele nó."*

#### Passo P15 — Execução de comandos Bash no namespace de um nó via WebShell
- **Identificador:** P15
- **Selo e reivindicação relacionados:** Selo R (C5)
- **Diretório:** Painel inferior `WebShell` na interface web (`http://<IP>:5173`)
- **Comando exato:**
  Com a topologia gerada no Passo P14 ativa:
  1. Na aba inferior intitulada `"WebShell"`, clicar na aba do nó `H1`.
  2. Clicar na área preta do terminal e executar os comandos Bash (como ilustrado em `artigo.pdf:p.7, Fig. 2` e `README.md:94, 112-114`):
     ```bash
     ip addr show
     ping -c 3 10.0.0.2
     ```
- **Resultado esperado segundo os autores:** A saída dos comandos executados no namespace de rede isolado do nó `h1` (exibindo a interface `h1-eth0` com IP `10.0.0.1/8` e as respostas de ICMP echo de `10.0.0.2`) é exibida em tempo real dentro da aba `H1` do `WebShell` (`reivindicacoes.md:11`, `README.md:112-114`, `artigo.pdf:p.7, Fig. 2`).
- **Evidência a salvar:** Captura de tela do painel `WebShell` com a aba `H1` selecionada mostrando a saída de `ip addr show` e `ping -c 3 10.0.0.2`.
- **Critério de sucesso:** Prompt Bash interativo funcional dentro da aba do nó selecionado, exibindo o namespace de rede exclusivo do nó (`h1-eth0`) e a saída dos comandos.
- **Critério de falha:** Aba não abre sessão de terminal, conexão WebSocket em `/api/mininet/terminal/h1` falha, ou comandos não produzem saída na aba.
- **Critério de interrupção:** Se falhar, C5 não é reproduzida (impacta diretamente o Selo R).

---

### Bloco da Reivindicação C6 — Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches
- **Reivindicação (`reivindicacoes.md:12`):** Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches (`artigo.pdf:p.2, §1; pp.5-6, §3; p.7, §5`). *(Nota: Segundo `reivindicacoes.md:16`, C6 não entra na regra de atribuição do Selo R).*

#### Passo P16 — [NÃO DOCUMENTADO] Inspeção da tabela de fluxo OpenFlow no switch e verificação da ausência de editor de regras
- **Identificador:** P16 `[NÃO DOCUMENTADO]`
- **Justificativa da necessidade:** O `README.md` não contém instruções para C6 (`reivindicacoes.md:12`). No código (`NetworkGraph.vue:277-281`, `NodeStats.vue:36-93`), a visualização da tabela de fluxos é acionada por duplo clique sobre um switch no grafo, mas não existem controles na GUI nem endpoints no backend (`api.py`) para criar ou remover regras de fluxo. Este passo verifica empiricamente essa limitação durante a execução.
- **Selo e reivindicação relacionados:** Selo F / Contribuição C6
- **Diretório:** Interface web (`http://<IP>:5173`)
- **Comando exato:**
  1. Na área do grafo, efetuar **duplo clique** sobre o ícone de um switch (ex.: `s1`).
  2. No modal `Node Info: s1` que se abre, clicar na aba `"Flow Table"`.
  3. Verificar se a tabela de fluxos é exibida e se existe algum botão, formulário ou controle na interface para inserir ou remover regras de fluxo OpenFlow.
- **Resultado esperado segundo os autores:** No artigo (`artigo.pdf:p.6, §3`), os autores afirmam existir um *"Flow Rule Editor: consiste em uma ferramenta para visualização, criação e remoção de regras de fluxo OpenFlow nos switches"*, cujo resultado esperado seria *"tabela de fluxo exibida, com a regra inserida ou removida no switch"* (`reivindicacoes.md:12`). Pelo código examinado (`NodeStats.vue:62-93`), espera-se observar apenas a tabela somente-leitura de fluxos retornada por `dpctl dump-flows`, sem opção de criação ou remoção na interface.
- **Evidência a salvar:** Captura de tela do modal `Node Info: s1` na aba `"Flow Table"`.
- **Critério de sucesso (para reprodução completa de C6):** Tabela de fluxo exibida com suporte à inserção e remoção de regras de fluxo pela interface.
- **Critério de falha (para C6):** Ausência de funcionalidade na interface para criar ou remover regras de fluxo OpenFlow (confirmando que C6 é `nao_reproduzivel`).
- **Critério de interrupção:** Fim do roteiro de execução.

---

## 5. Tempo Estimado de Execução

| Etapa | Tempo estimado |
|---|---|
| Download e importação da VM `.ova` no VirtualBox (ou instalação manual via `setup.sh`) (P1–P2) | 15 a 30 minutos |
| Execução do Teste Mínimo completo para o Selo F (P3–P9, incluindo 1 min do `iperf`) | 10 a 15 minutos |
| Execução dos blocos específicos de reivindicações para o Selo R (P10–P16: C1, C3, C4 nos 3 modelos, C5 e C6) | 10 a 15 minutos |
| **Tempo total estimado** | **35 a 60 minutos** |

---

## 6. Tabela Resumo de Todos os Passos

| ID | Documentado? | Selo / Reivindicação | Diretório / Local | Comando / Ação Exata | Resultado Esperado | Evidência a Salvar | Critério de Sucesso | Critério de Falha | Critério de Interrupção |
|---|---|---|---|---|---|---|---|---|---|
| **P1** | Sim (`README.md:49-78`) | F, R (Setup) | Host (VirtualBox) ou `/home/mininet` | Importar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` e logar (`mininet`/`mininet`), ou clonar e rodar `./setup.sh` | VM iniciada ou ambiente instalado sem erros | Screenshot do login na VM ou log do `setup.sh` | Sessão ativa com `/home/mininet/mininet-gui` | Falha na VM e falha no `setup.sh` | Interromper se nem VM nem instalação manual funcionarem |
| **P2** | `[NÃO DOCUMENTADO]` | F, R (Diagnóstico de código) | `/home/mininet/mininet-gui` | `nl -ba mininet-gui-frontend/src/core/api.js \| sed -n '295,301p'` e `nl -ba .../NetworkGraph.vue \| sed -n '252,266p'` | Verificar presença de `}i` em `api.js:299` e falta de `dst` em `NetworkGraph.vue:257` | Saída do terminal dos comandos `nl -ba` | Estado original do código registrado | Diretório ausente | Não interrompe |
| **P3** | Sim (`README.md:84-86`) | F / C1, C2 | `/home/mininet` e Navegador | `mininet_gui` (ou `/home/mininet/mininet-gui/run.sh`) e abrir `http://<IP>:5173` | Backend (`:8000`) e frontend (`:5173`) ativos; GUI carregada no navegador | Saída do terminal, `nohup.out` e screenshot da GUI | Interface carregada e sem erro fatal | Tela branca (`SyntaxError` em `api.js:299`) ou erro no Uvicorn | Se tela branca por `api.js:299`, registrar, corrigir `api.js:299` e reiniciar; se persistir, interromper |
| **P4** | Sim (`README.md:88`) | F / C1 | GUI (`http://<IP>:5173`) | Arrastar `"Controller"` para o grafo -> `Default` -> `"Submit"` | Controlador `c1` exibido no grafo e aba `C1` no WebShell | Screenshot do modal e do nó `c1` no grafo | Nó `c1` criado (`POST /api/mininet/controllers` 200) | Erro de rede ou nó não aparece | Não interrompe |
| **P5** | Sim (`README.md:90`) | F / C1, C2, C4 | GUI (`http://<IP>:5173`) | `"Generate Topology"` -> `Single`, `Controller: c1`, `Hosts: 2` -> `"Submit"` | Switch `s1` e hosts `h1`, `h2` criados com links verdes no grafo | Screenshot do modal e do grafo com `c1, s1, h1, h2` | `s1`, `h1`, `h2` e links criados no grafo e Mininet | Alerta de erro ou topologia não gerada | Interromper se o backend não conseguir criar nós no Mininet |
| **P6** | Sim (`README.md:92`) | F / C2 | GUI (`http://<IP>:5173`) | Clicar em `"Run Pingall Test"` na barra lateral | Modal `"Pingall Results"` exibe tabela de ping entre `h1` e `h2` | Screenshot do modal `"Pingall Results"` | `packets_recv: 1` para `h1->h2` e `h2->h1` | `"No ping results available."` ou erro HTTP | Não interrompe |
| **P7** | Sim (`README.md:94`) | F / C5 | Painel `WebShell` na GUI | Aba `H1`: `iperf -s`; Aba `H2`: `iperf -c 10.0.0.1` (aguardar 1 min) | Relatório de banda do `iperf` exibido nas abas `H1` e `H2` | Screenshots das abas `H1` e `H2` no WebShell | Saída de transferência e banda exibida no terminal web | WebSocket não conecta ou comando não executa | Não interrompe |
| **P8** | Sim (`README.md:96`) | F / C1, C2, C3, C5 | GUI e `WebShell` | Criar `c2` (`Remote`, `127.0.0.1:6633`), gerar `Single` (2 hosts, `c2`), `"Create Link"` `s1`–`s2`, rodar `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13` em `C2`, rodar `"Run Pingall Test"` | Segunda sub-rede adicionada em tempo real, conectada via `s1`–`s2`, Ryu ativo e `pingall` entre `h1..h4` OK | Screenshots do grafo, da aba `C2` com Ryu e do `Pingall Results` | Rede expandida sem reiniciar emulação e pings respondidos | Falha ao criar link, iniciar Ryu ou pingall sem resposta | Não interrompe |
| **P9** | Sim (`README.md:98`) | F | GUI (`Export/Import`) | Clicar em `"Export Topology (JSON)"` e `"Export Mininet Script"` | Download de `network_export.json` e `network_export.py` | Arquivos `network_export.json` e `network_export.py` | Arquivos baixados com a topologia atual válida | Falha no download ou arquivos vazios | Não interrompe |
| **P10** | `[NÃO DOCUMENTADO]` | F, R / C1 | GUI (`Nodes Palette` e grafo) | `"Reset Topology"` -> arrastar manualmente `Host`, `Switch`, `Controller` -> `"Create Link"` entre eles -> arrastar `h1` para nova posição | Nós criados manualmente no grafo, conectados e reposicionados | Screenshot do grafo após criação manual e drag | `h1`, `s1`, `c1` criados, conectados e movidos (`node_position` 200) | Drop não cria nós ou erro ao mover/conectar | Não interrompe |
| **P11** | `[NÃO DOCUMENTADO]` | F, R / C3 | GUI (`Actions` e grafo) | Com topologia ativa, selecionar link `h2`–`s1` e clicar `"Delete Selected"`; selecionar nó `h2` e clicar `"Delete Selected"` | Remoção em tempo real do link e do nó sem reiniciar a emulação | Screenshot do grafo e do Console (`F12`) | Link e nó removidos da GUI e do Mininet | `ReferenceError: dst is not defined` ao tentar remover link (`NetworkGraph.vue:260`) | Não interrompe |
| **P12** | Sim (`README.md:105-108`) | R / C4 (`Single`) | GUI (`Create Topology`) | `"Reset Topology"` -> criar `c1` -> `"Generate Topology"`: `Single`, `Controller: c1`, `Hosts: 3` -> `"Submit"` | Topologia `Single` gerada com 1 switch e 3 hosts | Screenshot do modal e da topologia `Single` | 1 switch e 3 hosts gerados e conectados | Quantidade incorreta ou falha na geração | Falha impede reprodução completa de C4 (Selo R) |
| **P13** | Sim (`README.md:105-108`) | R / C4 (`Linear`) | GUI (`Create Topology`) | `"Reset Topology"` -> criar `c1` -> `"Generate Topology"`: `Linear`, `Controller: c1`, `Switches: 3`, `Hosts per switch: 2` -> `"Submit"` | Topologia `Linear` gerada com 3 switches em linha e 6 hosts | Screenshot do modal e da topologia `Linear` | 3 switches encadeados e 2 hosts por switch gerados | Falha nos links entre switches ou na contagem de nós | Falha impede reprodução completa de C4 (Selo R) |
| **P14** | Sim (`README.md:105-108`) | R / C4 (`Tree`) | GUI (`Create Topology`) | `"Reset Topology"` -> criar `c1` -> `"Generate Topology"`: `Tree`, `Controller: c1`, `Layers: 2`, `Fanout: 2` -> `"Submit"` | Topologia `Tree` gerada com 3 switches (1 raiz, 2 filhos) e 4 hosts | Screenshot do modal e da topologia `Tree` | Árvore de profundidade 2 e fanout 2 gerada corretamente | Topologia não reflete árvore com `Layers` e `Fanout` escolhidos | Falha impede reprodução completa de C4 (Selo R) |
| **P15** | Sim (`README.md:110-114`) | R / C5 (`WebShell`) | Painel `WebShell` na GUI | Clicar na aba `H1` do `WebShell` e rodar `ip addr show` e `ping -c 3 10.0.0.2` | Saída dos comandos Bash no namespace de `h1` exibida na aba `H1` | Screenshot da aba `H1` com saída de `ip addr show` e `ping` | Saída exibida corretamente na aba do nó selecionado | Terminal inoperante ou sem saída | Falha impede reprodução de C5 (Selo R) |
| **P16** | `[NÃO DOCUMENTADO]` | F, R / C6 (`Flow Rules`) | GUI (Grafo / Modal `Node Info`) | Duplo clique no switch `s1` -> clicar na aba `"Flow Table"` -> procurar controles de inserção/remoção de regras | Tabela de fluxos exibida; verificar se há criação/remoção de regras na GUI | Screenshot do modal `Node Info: s1` na aba `"Flow Table"` | Tabela exibida com opção de inserir/remover regra | Apenas leitura disponível; sem criação/remoção de regras (confirma C6 não reproduzível) | Fim do roteiro |

## Prompt B2

Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que atende parcialmente (VM dos autores no VirtualBox 7.1.6 com 8 GB de RAM, mas sobre o Hyper-V em modo NEM e com o navegador do host em vez de um navegador dentro da VM, como detalhado na seção 1 do registro) aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.

Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.

## Resposta B2

# Reavaliação Pós-Execução — Mininet-GUI (Selos F e R)

## 1. Confronto Passo a Passo com a Avaliação Analítica

Abaixo, cada passo relevante do registro factual (`registro-factual.md`) é confrontado com a avaliação analítica e o roteiro prévios, separando os passos documentados pelos autores (Seção 2 do registro) dos passos complementares `[NÃO DOCUMENTADO]` marcados como `D2` (Seção 3 do registro, tratados estritamente como evidência complementar).

### 1.1 Passos documentados pelos autores (`registro-factual.md:72-91`)

- **E02, E04, E06 (correspondentes a P1 — Obtenção, importação e boot da VM):** **Confirma com ressalvas de documentação.**
  - *Observado:* O link do [REMOVIDO] Drive em `[README.md:53]` estava inativo, mas a OVA oficial da release `v0.0.1` do repositório dos autores (`Mininet-GUI-VM-SBRC-2025.ova`) foi importada no VirtualBox `7.1.6 r167084` e iniciou em ~95 s com login `mininet`/`mininet` por SSH (a VM não possui interface gráfica desktop) `[registro-factual.md:27-32, 74-76]`.
  - *Relação com a análise:* Confirma que a distribuição em VM funciona no VirtualBox `7.1.6 r167084`, revelando adicionalmente que o link do Drive expirou e que a VM da release opera em modo texto (exigindo navegador no host via rede host-only).

- **E09, E10 (correspondentes a P3 — Inicialização via `mininet_gui` e abertura da URL):** **Confirma a funcionalidade (e contradiz o impacto impeditivo do erro em `api.js:299`).**
  - *Observado:* `mininet_gui` iniciou o backend Uvicorn (`:8000`) e o frontend Vite (`:5173`) em 4,7 s, imprimindo `http://192.168.56.101:5173`, e a interface carregou normalmente no navegador `[registro-factual.md:77-78]`.
  - *Relação com a análise:* Confirma que o comando de inicialização funciona como documentado em `[README.md:84-86]` e contradiz a hipótese analítica de que o caractere `i` em `mininet-gui-frontend/src/core/api.js:299` (`}i`) impediria o compilador do Vite de servir a página (veja explicação em E08 abaixo).

- **E11, E12, E13 (correspondentes a P4, P5, P6 — Criação de controlador `c1`, geração de topologia Single com 2 hosts e teste de Pingall):** **Confirma.**
  - *Observado:* O controlador `c1` foi criado via drag-and-drop (`E11`), a topologia `Single` com 2 hosts (`s1`, `h1`, `h2`) e links ativos em verde foi gerada (`E12`), e `"Run Pingall Test"` exibiu em menos de 2 s a tabela `"Pingall Results"` com `1/1` pacotes recebidos em `h1->h2` e `h2->h1` (`E13`) `[registro-factual.md:79-81]`.
  - *Relação com a análise:* Confirma integralmente a execução funcional de **C1**, **C2** e do modelo `Single` de **C4** pelo procedimento dos autores.

- **E14 (correspondente a P7 — Teste opcional com `iperf` nas abas do WebShell):** **Confirma.**
  - *Observado:* `iperf -s` na aba `h1` e `iperf -c 10.0.0.1` na aba `h2` mediram `6.62 Gbits/sec` em 10 s, exibindo os relatórios em ambas as abas `[registro-factual.md:82]`.
  - *Relação com a análise:* Confirma o funcionamento do WebShell (**C5**) e do Caso de Uso 2 do artigo (`[artigo.pdf:p.6, §4]`).

- **E16 (correspondente a P8 — Passo 8 opcional: segundo controlador remoto `c2`, segunda topologia, link `s1`–`s2`, `ryu-manager` e Pingall):** **Confirma parcialmente a análise e expõe falha documental/ambiental na VM.**
  - *Observado:* `c2 <127.0.0.1:6633>`, `s2`, `h3`, `h4` e o link verde `s1`–`s2` foram criados com a emulação ativa (após afastar manualmente os nós gerados sobrepostos), mas `ryu-manager` falhou na aba `c2` com `"Command 'ryu-manager' not found"`, resultando em 0 pacotes recebidos entre as duas topologias no Pingall `[registro-factual.md:33, 83, 137]`.
  - *Relação com a análise:* Na etapa analítica, notou-se que `[README.md:75-78]` colocava `pip3 install ryu...` como passo opcional da instalação manual; a execução revelou que os autores não instalaram o `ryu` dentro da VM pré-configurada (que roda sem Internet em rede host-only), impedindo a conclusão do Passo 8 opcional do `README.md:96`.

- **E17 (correspondente a P9 — Exportação JSON e Script Python):** **Confirma.**
  - *Observado:* `network_export.json` (2514 bytes) e `network_export.py` (1105 bytes, válido em `ast.parse`) foram baixados contendo exatamente os 2 switches, 4 hosts, 2 controladores e 5 links da topologia ativa `[registro-factual.md:84]`.
  - *Relação com a análise:* Confirma o funcionamento completo do módulo `Topology Exporter` no Teste Mínimo.

- **E19, E20, E21, E22 (correspondentes a P12, P13, P14 — Reprodução de C4 nos modelos `Single`, `Linear` e `Tree`):** **Confirma.**
  - *Observado:* `Single` com 3 hosts (`E19`: 1 switch, 3 hosts, 3 links), `Linear` 3×2 (`E20`: 3 switches em cadeia, 6 hosts, 8 links), `Linear` 2×1 (`E21`: 2 switches, 2 hosts, 3 links) e `Tree` 2×2 (`E22`: 3 switches sendo `s3` raiz e `s1`/`s2` filhos, 4 hosts, 6 links) foram gerados no grafo conforme as quantidades escolhidas `[registro-factual.md:85-88]`.
  - *Relação com a análise:* Confirma a reprodução integral da reivindicação **C4** nos três modelos exigidos por `[reivindicacoes.md:10, 20]`.

- **E24 (correspondente a P15 — Reprodução de C5 com `ip addr show` na aba `h1` do WebShell):** **Confirma.**
  - *Observado:* Na aba `h1` do WebShell, `ip addr show` exibiu `lo` (`127.0.0.1/8`) e `h1-eth0@if40` (`10.0.0.1/8`, MAC `00:00:00:00:00:01`) `[registro-factual.md:89]`.
  - *Relação com a análise:* Confirma a reprodução integral da reivindicação **C5** conforme o procedimento dos autores (`[README.md:110-114]`).

---

### 1.2 Passos `[NÃO DOCUMENTADO]` (`D2` — Evidência complementar, `registro-factual.md:93-119`)

*(Conforme a instrução 3, estes passos são analisados exclusivamente como evidência complementar diagnóstica, e não como reprodução das reivindicações dos autores).*

- **E05, E07 (correspondentes a P1/P2 — Ajuste de RAM da OVA e verificação do commit):** **Confirma.**
  - *Observado:* A OVA vinha configurada com 1536 MB de RAM (abaixo dos 2 GB / 8 GB indicados no README) e foi ajustada para 8192 MB (`E05`). O commit na VM é `be68302`, ancestral do commit avaliado `465648a4`, mas **todos os arquivos de `mininet-gui-backend/` e `mininet-gui-frontend/` são idênticos** entre ambos `[registro-factual.md:39-44, 101-102]`.
- **E08 (correspondente a P2 — Inspeção de `api.js:299` sem corrigir):** **Contradiz a gravidade do defeito apontado na análise.**
  - *Observado:* A linha 299 de `mininet-gui-frontend/src/core/api.js` de fato contém `}i` (`[registro-factual.md:103]`), mas o frontend compilou e executou sem precisar de correção. Isso ocorre porque, em JavaScript, `}i` logo após o bloco `catch (error) { ... return false; }` ainda está dentro do corpo de `requestRunPingall` (fechado por `};` na linha 300), sendo interpretado como uma instrução de expressão inalcançável (`i;`) por inserção automática de ponto-e-vírgula (ASI), e não como erro de sintaxe no carregamento do módulo.
- **E15 (apoio a C3 — Verificação de `ryu` na VM):** **Confirma a causa da falha em E16.**
  - *Observado:* `ModuleNotFoundError: No module named 'ryu'` na VM `[registro-factual.md:104]`.
- **E18, E23 (correspondentes a P12–P14 — Reset antes de cada modelo e contagem via API em C4):** **Confirma.**
  - *Observado:* Os 5 acionamentos de `"Reset Topology"` zeraram o grafo e a API (`E18`), e as contagens na API bateram exatamente com os parâmetros escolhidos em `E19`–`E22` (`E23`) `[registro-factual.md:105-106]`.
- **E25, E26, E27 (correspondentes a P15 — Isolamento de namespace no WebShell em C5):** **Confirma.**
  - *Observado:* `h1` (`net:[4026532228]`), `h2` (`net:[4026532269]`) e a VM (`net:[4026531992]`) operam em namespaces de rede distintos, e `h1` pinga `h2` com 0% de perda `[registro-factual.md:107-109]`.
- **E28a, E28b, E29 (correspondentes a P10 — Persistência de posição e adição manual da paleta com rede ativa):** **Confirma.**
  - *Observado:* A posição de `h1` arrastado persiste após reload (`E28a`), switches/hosts soltos da paleta com a rede ativa são criados e respondem 20/20 no Pingall (`E28b`, `E29`) `[registro-factual.md:110-112]`.
- **E30a, E30b, E30c, E30d (correspondentes a P11 — Remoção em tempo real de link e nó para C3):** **Contradiz o local exato do bug de remoção e revela falha no backend após remover nó.**
  - *Observado:* A remoção do link `h2`–`s1` funcionou (`E30a`, `DELETE /api/mininet/delete_link/h2/s1` 200 OK — a linha 258 `let dst = this.nodes.get(link.to);` existia em `NetworkGraph.vue` na linha 3050 de `artefato.txt`). A remoção do nó `h4` (`E30b`) removeu o nó do grafo e do Mininet sem reiniciar a emulação (`E30d`), porém manteve o link órfão `['h4','s2']` em `/api/mininet/links` e fez com que `"Run Pingall Test"` (`E30c`) falhasse com **HTTP 500 Internal Server Error** (`AttributeError: 'NoneType' object has no attribute 'IP'` em `pingFull()`, `api.py:157`) `[registro-factual.md:113-116]`.
- **E31, E32 (correspondentes a P16 — Inspeção da tabela de fluxos e ausência de editor de regras em C6):** **Confirma integralmente a avaliação analítica.**
  - *Observado:* O duplo clique em `s1` exibiu a aba `"Flow Table"` com 5 regras OpenFlow instaladas após o Pingall (`E31`), mas confirmou-se que **não existe nenhum controle no modal ou na página para criar ou remover regras de fluxo** (`E32`) `[registro-factual.md:117-118]`.

---

## 2. Nova Decisão para o Selo F (Funcional)

- **Decisão:** **Atribuir** (mudou em relação à decisão analítica `Indeterminado`: `"mudou": true`).
- **Justificativa:**
  1. Todos os critérios documentais obrigatórios (`[instrucoes-oficiais.md:15]`) estão atendidos no `README.md` (dependências e versões, ambiente de execução, instruções de instalação, execução e teste mínimo).
  2. Na execução (`[registro-factual.md:74-84, 133]`), o artefato foi iniciado com sucesso na VM dos autores (`E09`, `E10`) e todas as funcionalidades principais do **Teste mínimo** foram observadas diretamente: criação de controlador no grafo interativo (`E11`), geração automatizada de topologia e início da emulação Mininet (`E12`), execução e exibição dos resultados de `pingall` na interface (`E13`), execução de `iperf` entre hosts pelos terminais do WebShell (`E14`), criação de controlador remoto, segunda sub-rede e link em tempo real (`E16`, falhando apenas o binário externo `ryu-manager` no passo opcional 8) e exportação da topologia para JSON e script Python válido (`E17`).
- **Confiança (0 a 100):** **95** (subiu de **85** na etapa analítica para **95**).
- **Explicação da mudança:** Na avaliação analítica, a decisão era `Indeterminado` exclusivamente porque a regra oficial (`[instrucoes-oficiais.md:15]`) exige a observação prática do artefato em execução e havia dúvida sobre o impacto de `}i` em `api.js:299`. O registro factual comprovou que o frontend compila e funciona sem alterações (`E08`–`E17`) e que o Teste Mínimo é cumprido com sucesso. A confiança não é 100 apenas pelos pequenos desvios ambientais no `README.md` (link do [REMOVIDO] Drive inativo exigindo usar a OVA da release `v0.0.1`, ausência de desktop gráfico na VM exigindo navegador no host, e ausência do `ryu` pré-instalado para o passo 8 opcional).

---

## 3. Nova Decisão para o Selo R (Reprodutível)

### 3.1 Avaliação por reivindicação após a execução

- **C1 (Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo):** **`reproduzivel`** (mudou de `depende_execucao`).
  - Comprovada pelos passos documentados pelos autores `E10`, `E11`, `E12` e `E16` (elementos criados, representados no grafo e respondendo às ações de criação, arraste e ligação) `[registro-factual.md:78-80, 83, 126]`, com confirmação complementar em `E28a`–`E28b` (`D2`).
- **C2 (Emulação integrada: inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade):** **`reproduzivel`** (mudou de `depende_execucao`).
  - Comprovada pelos passos documentados `E12` e `E13` (nós emulados no Mininet e tabela `"Pingall Results"` exibida na interface com `1/1` pacotes recebidos entre `h1` e `h2`) `[registro-factual.md:80-81, 127]`, com confirmação complementar em `E29` e `E31` (`D2`).
- **C3 (Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la):** **`nao_reproduzivel`** (mudou de `depende_execucao`).
  - No único passo documentado pelos autores relacionado a C3 (`E16`, passo 8 opcional do `README.md:96`), a adição dos nós e do link `s1`–`s2` ocorreu com a emulação ativa, mas o passo falhou por ausência do `ryu-manager` na VM (sem conectividade entre as topologias), e os autores **não documentaram** procedimento para remoção de nós ou links `[registro-factual.md:83, 128]`. Ademais, a evidência complementar `D2` (`E30b`–`E30c`, que não substitui instruções dos autores) mostrou que a remoção de um nó (`h4`) deixa link órfão em `/api/mininet/links` e causa erro HTTP 500 (`AttributeError: 'NoneType' object has no attribute 'IP'`) ao executar `"Run Pingall Test"` `[registro-factual.md:114-115]`.
- **C4 (Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido — Obrigatória para R):** **`reproduzivel`** (mudou de `depende_execucao`).
  - Comprovada integralmente pelos passos documentados pelos autores (`[README.md:90, 105-108]`) nos **três modelos** exigidos por `[reivindicacoes.md:20]`: `Single` com 2 hosts (`E12`) e 3 hosts (`E19`), `Linear` com 3 switches × 2 hosts (`E20`) e 2 switches × 1 host (`E21`), e `Tree` com 2 camadas e fanout 2 (`E22`), todos gerando no grafo exatamente a estrutura e a quantidade de dispositivos escolhida `[registro-factual.md:80, 85-88, 129]`, com confirmação complementar na API em `E18` e `E23` (`D2`).
- **C5 (Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado — Obrigatória para R):** **`reproduzivel`** (mudou de `depende_execucao`).
  - Comprovada pelos passos documentados pelos autores (`[README.md:94, 110-114]`) em `E14` (`iperf -s` e `iperf -c 10.0.0.1` nas abas `h1` e `h2`) e `E24` (`ip addr show` na aba `h1` exibindo `h1-eth0@if40` com `10.0.0.1/8` e MAC `00:00:00:00:00:01`) `[registro-factual.md:82, 89, 130]`, com confirmação complementar de isolamento de namespace em `E25`–`E27` (`D2`).
- **C6 (Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches):** **`nao_reproduzivel`** (mantida como `nao_reproduzivel`).
  - Não há instruções no `README.md` (`[reivindicacoes.md:12]`) e a evidência complementar `D2` (`E31`–`E32`) confirmou que, embora o duplo clique em `s1` exiba a aba `"Flow Table"` com as regras instaladas (`E31`), não há nenhum controle na interface para criar ou remover regras de fluxo (`E32`) `[registro-factual.md:117-118, 131]`.

### 3.2 Decisão final para o Selo R
- **Decisão:** **Atribuir** (mudou em relação à decisão analítica `Indeterminado`: `"mudou": true`).
- **Justificativa:** Conforme a regra oficial para o Selo R fixada em `[reivindicacoes.md:16]`: *"Na seção "Experimentos", o README marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R."* Como tanto **C4** (nos três modelos: `Single`, `Linear` e `Tree`, passos `E12`, `E19`–`E22`) quanto **C5** (passos `E14` e `E24`) foram integralmente reproduzidas seguindo o procedimento documentado pelos autores no `README.md`, o critério de atribuição do Selo R foi plenamente atendido.
- **Confiança (0 a 100):** **90** (subiu de **80** na etapa analítica para **90**).
- **Explicação da mudança:** Na avaliação analítica, a decisão era `Indeterminado` porque a verificação do comportamento de C4 (nos três modelos) e C5 dependia de execução. Com a reprodução bem-sucedida de C4 (`E19`–`E22`) e C5 (`E14`, `E24`) na execução registrada em `registro-factual.md`, a decisão passa a ser `Atribuir`. A confiança é de 90 (e não 100) apenas porque C3 e C6 — embora fora da regra de R fixada a partir da seção "Experimentos" do README — apresentaram limitações na execução (`ryu` ausente no passo 8 opcional, erro HTTP 500 no Pingall após remoção de nó em D2, e ausência de edição de regras em C6).

```json
{"F": {"decisao": "Atribuir", "confianca": 95, "mudou": true, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:26-99", "registro-factual.md:74-84", "registro-factual.md:103", "registro-factual.md:133"]},
 "R": {"decisao": "Atribuir", "confianca": 90, "mudou": true, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:5-20", "README.md:101-115", "registro-factual.md:78-90", "registro-factual.md:113-118", "registro-factual.md:124-132"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "reproduzivel", "C3": "nao_reproduzivel", "C4": "reproduzivel", "C5": "reproduzivel", "C6": "nao_reproduzivel"}}}
```
