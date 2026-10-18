# Cadeia MG-1 — [REMOVIDO]

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
- metodo_exportacao: transcrição integral gerada a partir do log oficial da sessão isolada (`73e04a19-b48e-41c6-a308-5c268212514c`, `transcript_full.jsonl`); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos
- desvios: resposta A usou 10 chamada(s) de ferramenta somente-leitura para abrir os 4 anexos: [REMOVIDO] ("Read instrucoes-oficiais.md"); [REMOVIDO] ("Read reivindicacoes.md"); [REMOVIDO] ("Read artigo.pdf"); [REMOVIDO] ("Read first 800 lines of artefato.txt"); [REMOVIDO] ("Read lines 801-1600 of artefato.txt"); [REMOVIDO] ("Read lines 2401-3200 of artefato.txt"); [REMOVIDO] ("Read lines 3201-4000 of artefato.txt"); [REMOVIDO] ("Read lines 4001-4930 of artefato.txt"); [REMOVIDO] ("Read lines 2200-2400 of artefato.txt"); [REMOVIDO] ("Read lines 4801-4930 of artefato.txt") | resposta A contém raciocínio (thinking) omitido nesta transcrição | resposta B1 contém raciocínio (thinking) omitido nesta transcrição | resposta B2 usou 1 chamada(s) de ferramenta somente-leitura para abrir o registro factual: [REMOVIDO] ("Read registro-factual.md") | resposta B2 contém raciocínio (thinking) omitido nesta transcrição

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

Foram abertos e examinados exclusivamente os 4 arquivos anexados do pacote:
- `runs/mininet-gui/pacote/instrucoes-oficiais.md` (integral, linhas 1–21)
- `runs/mininet-gui/pacote/reivindicacoes.md` (integral, linhas 1–21)
- `runs/mininet-gui/pacote/artigo.pdf` (integral, páginas 1–9)
- `runs/mininet-gui/pacote/artefato.txt` (linhas 1–1600 e 2200–4930, cobrindo o índice e todos os arquivos de código-fonte, scripts e documentação do commit `465648a4425a4457af0348ab951cf7f71d37a86f`, exceto o miolo de dependências transitivas de `package-lock.json`)

---

## B. Selo F

### 1. Critérios oficiais aplicáveis e avaliação por critério

Conforme `[instrucoes-oficiais.md:13-15]`:
> "O código ou artefato deve poder ser executado, e o revisor deve conseguir observar funcionalidades. O README deve informar dependências e versões, ambiente de execução, instalação, execução e um exemplo mínimo. A conclusão funcional requer observação do artefato, não apenas a presença das instruções."

E quanto ao contexto de ambiente `[instrucoes-oficiais.md:10]`:
> "O ambiente escolhido precisa satisfazer os requisitos mínimos do artefato; a página recomenda virtualização. Recursos específicos necessários devem estar descritos no apêndice."

Avaliação de cada critério:

1. **README informa dependências e versões**: **Atendido na documentação**.
   - Evidência `[README.md:35-38]` (`[artefato.txt:120-123]`):
     > `A execução do Mininet-GUI requer o Oracle VirtualBox (versão 7.1.6 r167084).`
     > `Memória RAM: Mínimo de 8GB para a máquina virtual.`
   - Evidência `[README.md:77]` (`[artefato.txt:162]`):
     > `pip3 install ryu eventlet==0.30.0 dnspython==1.16.0`
   - Evidência `[setup.sh:19]` (`[artefato.txt:4923]`):
     > `nvm install 18.20.7`
   - Evidência `[mininet-gui-frontend/package.json:10-23]` (`[artefato.txt:2264-2277]`):
     > `"axios": "^1.2.1", "dotenv": "^16.4.7", "vis-data": "^7.1.4", "vis-network": "^9.1.2", "vis-util": "^5.0.3", "vis.js": "^1.1.0", "vue": "^3.2.45"`
   - Evidência `[mininet-gui-backend/requirements.txt:1-4]` (`[artefato.txt:1078-1081]`):
     > `fastapi` / `websockets` / `uvicorn` / `python-multipart` (listados sem versão fixada no `requirements.txt`, porém pré-instalados na VM fornecida).

2. **README informa ambiente de execução**: **Atendido na documentação**.
   - Evidência `[README.md:26-32]` (`[artefato.txt:111-117]`):
     > `Processador: Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz 2.50 GHz`
     > `RAM instalada: 8,00 GB`
     > `Sistema Operacional: Windows 11 Home Single Language`
     > `Espaço disponível em disco: Pelo menos 80GB livres`
   - Evidência `[README.md:63]` (`[artefato.txt:148]`):
     > `Utilize os comandos abaixo para instalar manualmente (testado no ubuntu 20.04):`
   - Evidência `[README.md:103]` (`[artefato.txt:188]`):
     > `A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM.`

3. **README informa instruções de instalação**: **Atendido na documentação**.
   - Evidência `[README.md:49-58]` (`[artefato.txt:134-143]`):
     > `Passo 1: Baixe o arquivo ova neste link: <https://drive.[REMOVIDO]/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing>`
     > `Passo 2: Abra o arquivo Mininet-GUI-Desktop-VM-SBRC-2025.ova no VirtualBox, para importar a máquina virtual`
     > `Passo 3: Execute a máquina virtual (user mininet, senha mininet)`
   - Evidência `[README.md:60-73]` (`[artefato.txt:145-158]`):
     > `git clone https://github.com/mininet/mininet` ... `./util/install.sh -nfv` ... `git clone https://github.com/latarc/mininet-gui` ... `./setup.sh`

4. **README informa instruções de execução e exemplo mínimo**: **Atendido na documentação**.
   - Evidência `[README.md:80-99]` (`[artefato.txt:165-184]`):
     > `# Teste mínimo`
     > `Passo 2: Abra o terminal (Ctrl+Alt+T) e rode o seguinte comando: mininet_gui (ou alternativamente /home/mininet/mininet-gui/run.sh)`
     > `Passo 3: A execução do comando do Passo 2 mostrará em sua saída do terminal uma URL (Exemplo: http://10.0.2.15:5173). Acesse essa URL em um navegador dentro da VM.`
     > `Passo 4: Para criar um controlador, arraste o ícone rotulado "Controller"...`
     > `Passo 5: Clique no botão "Generate Topology"...`
     > `Passo 6: Execute um teste de pingall clicando no botão "Run Pingall Test"...`
     > `Passo 9: Finalmente, clique nos botões "Export Topology (JSON)" e "Export Mininet Script"...`

5. **Execução do código/artefato e observação de funcionalidades**: **Só verificável por execução**.
   - Evidência `[instrucoes-oficiais.md:15]`:
     > `A conclusão funcional requer observação do artefato, não apenas a presença das instruções.`
   - O repositório inclui o backend FastAPI (`[mininet-gui-backend/mininet_gui_backend/api.py:1-491]`, `[artefato.txt:416-906]`), o frontend Vue.js/vis-network (`[mininet-gui-frontend/src/components/NetworkGraph.vue:1-687]`, `[artefato.txt:2793-3479]`) e os scripts `[run.sh:1-28]` (`[artefato.txt:4874-4901]`) e `[setup.sh:1-24]` (`[artefato.txt:4905-4928]`).
   - Entretanto, na análise estática do código do commit `465648a4425a4457af0348ab951cf7f71d37a86f`, observa-se um erro de digitação/sintaxe em `[mininet-gui-frontend/src/core/api.js:299]` (`[artefato.txt:4752]`):
     > `} catch (error) {`
     > `  alert(error.response ? error.response.data["detail"] : "Network Error");`
     > `  return false;`
     > `}i`
     > `};`
     Esse caractere `i` após `}` causaria falha de compilação no Vite caso executado diretamente a partir deste commit sem correção, embora a instalação recomendada pelo README seja a imagem externa `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (`[README.md:49-58]`), cujo conteúdo pré-instalado só pode ser verificado em execução.

### 2. Decisão para o Selo F
- **Decisão**: **Indeterminado** (nenhum critério obrigatório falha na documentação, mas a decisão depende de execução e observação prática do artefato).
- **Confiança (0 a 100) de que o comitê oficial atribuiu o selo**: **85**. (O README segue estritamente o modelo do SBRC 2025, disponibiliza vídeo de demonstração e VM `.ova` pronta para uso no VirtualBox; mesmo que o commit tenha o caractere `i` acidental em `api.js:299`, a VM provavelmente contém a versão íntegra ou o erro trivial de 1 caractere seria corrigido na fase interativa).

### 3. O que precisaria ser observado na execução para mudar a decisão
- **Para mudar para Atribuir**: Importar e iniciar a VM `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (ou instalar manualmente corrigindo `api.js:299` se necessário), executar `mininet_gui` (`run.sh`), abrir a interface web na porta `5173` e observar o funcionamento do grafo interativo, criação de controlador, geração de topologia, teste de `pingall` e exportação de JSON/script Python conforme os Passos 1 a 9 do "Teste mínimo" (`[README.md:80-99]`).
- **Para mudar para Não atribuir**: Verificar na execução que o link da VM `.ova` está inacessível/corrompido e que a execução falha de modo impeditivo (por exemplo, o frontend não carrega devido ao erro de sintaxe em `[mininet-gui-frontend/src/core/api.js:299]` ou falha do `nvm use` em `[run.sh:20]`, impedindo observar as funcionalidades mínimas).

---

## C. Selo R (por reivindicação)

### 1. Critérios oficiais aplicáveis e regra do selo R

Conforme `[instrucoes-oficiais.md:17-19]`:
> "O revisor deve conseguir reproduzir as **principais reivindicações do artigo**. Para isso, o artefato precisa fornecer instruções de execução e descrição do processo empregado nos experimentos que produziram os resultados do artigo. A avaliação confronta o resultado observado com a reivindicação correspondente."

Conforme a regra fixada em `[reivindicacoes.md:14-20]`:
> "Na seção "Experimentos", o README marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R."
> "As reivindicações descrevem comportamentos, sem valores numéricos com tolerância declarada pelos autores. Uma reivindicação é reproduzida quando o resultado esperado da tabela é observado. Em C4, nos três modelos."

### 2. Avaliação separada por reivindicação (C1 a C6)

#### **C1 — Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo**
- **Fonte no artigo**: `[artigo.pdf:p. 1, resumo; p. 2, §1, item 1; pp. 4-6, §3; p. 7, Fig. 2]` — *"1. Interface web dinâmica para manipulação intuitiva da topologia de rede."*
- **Resultado esperado**: Elementos criados pelo usuário representados no grafo e respondendo às ações (`[reivindicacoes.md:7]`).
- **Critério documental (instruções de execução/processo)**: **Atendido na documentação** (`[README.md:82-91]`, seção "Teste mínimo", passos 1–5).
  > `Passo 4: Para criar um controlador, arraste o ícone rotulado "Controller", localizado na aba lateral esquerda, para o centro da tela...`
- **Suporte no código**: Implementado em `[mininet-gui-frontend/src/components/NetworkGraph.vue:1-4, 135-285, 416-440]` (`[artefato.txt:2793-2796, 2927-3077, 3208-3232]`, grafo `vis-network` e eventos de arrastar/soltar) e `[mininet-gui-frontend/src/components/Side.vue:71-87]` (`[artefato.txt:3821-3837]`, paleta de nós).
- **Verificação do resultado esperado**: **Só verificável por execução**.
- **Classificação C1**: `depende_execucao` (embasa F; não entra na regra de R conforme `[reivindicacoes.md:16]`).

#### **C2 — Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade**
- **Fonte no artigo**: `[artigo.pdf:p. 2, §1, item 2; pp. 4-5, §3; p. 6, §4, caso 1]` — *"2. Emulação integrada, eliminando a necessidade de configurações externas."*
- **Resultado esperado**: Nós emulados e resultado de `pingall` exibido na interface (`[reivindicacoes.md:8]`).
- **Critério documental (instruções de execução/processo)**: **Atendido na documentação** (`[README.md:88-92]`, seção "Teste mínimo", passos 4–6).
  > `Passo 6: Execute um teste de pingall clicando no botão "Run Pingall Test" na aba lateral esquerda e aguarde os resultados aparecerem.`
- **Suporte no código**: Implementado no backend em `[mininet-gui-backend/mininet_gui_backend/api.py:40-56, 107-160]` (`[artefato.txt:455-471, 522-575]`, ciclo de vida da instância `Mininet` e rota `/api/mininet/pingall` chamando `app.net.pingFull()`) e no frontend em `[mininet-gui-frontend/src/components/NetworkGraph.vue:494-502]` (`[artefato.txt:3286-3294]`) e `[mininet-gui-frontend/src/components/PingallResults.vue:1-65]` (`[artefato.txt:3666-3730]`).
- **Verificação do resultado esperado**: **Só verificável por execução**.
- **Classificação C2**: `depende_execucao` (embasa F; não entra na regra de R conforme `[reivindicacoes.md:16]`).

#### **C3 — Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la**
- **Fonte no artigo**: `[artigo.pdf:p. 1, resumo; p. 2, §1, item 3; p. 6, §3; p. 7]` — *"O principal desafio na implementação do Mininet-GUI foi permitir que os nós e links sejam criados e removidos em tempo de execução, sem que a emulação da rede precisasse ser interrompida ou reiniciada."*
- **Resultado esperado**: Rede alterada enquanto a emulação continua ativa (`[reivindicacoes.md:9]`).
- **Critério documental (instruções de execução/processo)**: **Atendido parcialmente na documentação** (`[README.md:96]`, "Teste mínimo", passo 8 opcional, que demonstra adição de novo controlador, subtopologia e link entre switches com a emulação em curso, sem detalhar remoção no roteiro).
  > `Passo 8 (opcional): Multiplos controladores - arraste um novo "Controller" da barra lateral para o centro da tela... Adicionalmente, clique no botão "Create Link" e conecte os switches das duas topologias, s1 e s2...`
- **Suporte no código**: Implementado em `[mininet-gui-backend/mininet_gui_backend/api.py:180-198, 247-267, 298-344]` (`[artefato.txt:595-613, 662-682, 713-759]`, onde `create_switch` e `create_link` invocam `start` e `configDefault` com `app.net.is_started == True`, e rotas `delete_node`/`delete_link` removem elementos ativos) e `[mininet-gui-frontend/src/components/NetworkGraph.vue:209-275, 485-488]` (`[artefato.txt:3001-3067, 3277-3280]`).
- **Verificação do resultado esperado**: **Só verificável por execução**.
- **Classificação C3**: `depende_execucao` (embasa F; não entra na regra de R conforme `[reivindicacoes.md:16]`).

#### **C4 — Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido** *(Reivindicação-chave para R)*
- **Fonte no artigo**: `[artigo.pdf:p. 2, §1, item 4; p. 6, §3, "Topology Generator"; pp. 6-7, §4, caso 1 e Fig. 2]` — *"Topology Generator: oferece um mecanismo para geração automatizada de topologias de rede. Suporta os modelos single, linear e tree, com a quantidade de switches definida pelo usuário."*
- **Resultado esperado**: Topologia de cada modelo (`Single`, `Linear` e `Tree`) gerada com a quantidade de dispositivos escolhida (`[reivindicacoes.md:10, 20]`).
- **Critério documental (instruções de execução/processo)**: **Atendido na documentação** (`[README.md:105-108]` e `[README.md:90]`).
  - Evidência `[README.md:105-108]` (`[artefato.txt:190-193]`):
    > `## Reivindicação "Geração automatizada de topologias, incluindo diversos modelos amplamente utilizados"`
    > `Após inicializar o mininet_gui e acessar a interface web do frontend, clique no botão "Generate Topology". Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK.`
- **Suporte no código**: Implementado no formulário `[mininet-gui-frontend/src/components/TopologyForm.vue:5-44]` (`[artefato.txt:4066-4105]`, seleção entre `Single`, `Linear` e `Tree` e campos de quantidade de dispositivos/camadas) e nos métodos geradores em `[mininet-gui-frontend/src/components/NetworkGraph.vue:512-585, 608-617]` (`[artefato.txt:3304-3377, 3400-3409]`):
  > `if (topologyType == "Single") { await this.createSingleTopo(nDevices, controller); } else if (topologyType == "Linear") { await this.createLinearTopo(nDevices, nLayers, controller); } else if (topologyType == "Tree") { await this.createTreeTopo(nLayers, nDevices, controller); }`
- **Verificação do resultado esperado**: **Só verificável por execução**.
- **Classificação C4**: `depende_execucao`.

#### **C5 — Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado** *(Reivindicação-chave para R)*
- **Fonte no artigo**: `[artigo.pdf:p. 1, resumo; p. 2, §1, item 5; pp. 5-6, §3; p. 6, §4, caso 2; p. 7, Fig. 2]` — *"Node Terminal Sessions: implementa conexões WebSocket para gerenciar e expor os terminais dos nós no frontend para sua utilização no Webshell."*
- **Resultado esperado**: Saída do comando exibida na aba do nó selecionado (`[reivindicacoes.md:11]`).
- **Critério documental (instruções de execução/processo)**: **Atendido na documentação** (`[README.md:110-114]` e `[README.md:94, 96]`).
  - Evidência `[README.md:110-114]` (`[artefato.txt:195-199]`):
    > `## Reivindicação "Terminal integrado dos nós via WebShell"`
    > `Após inicializar o mininet_gui e acessar a interface web do frontend, crie ao menos um nó (seja pelo Gerador de Topologias ou clicando e arrastando) e na aba inferior titulada "Webshell" selecione a aba com o nome desse nó, clicando nela.`
    > `Em seguida, utilize o terminal bash para executar comandos diretamente no namespace daquele nó.`
- **Suporte no código**: Implementado no backend em `[mininet-gui-backend/mininet_gui_backend/api.py:450-491]` (`[artefato.txt:865-906]`):
  > `@app.websocket("/api/mininet/terminal/{node_id}")` ...
  > `master_fd, slave_fd = pty.openpty()`
  > `process = node.popen(["/bin/bash", "-i"], stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, text=True, close_fds=True)`
  E no frontend em `[mininet-gui-frontend/src/components/Webshell.vue:1-192]` (`[artefato.txt:4156-4347]`):
  > `const ws = new WebSocket(\`${this.backendWsUrl}/api/mininet/terminal/${nodeId}\`);`
- **Verificação do resultado esperado**: **Só verificável por execução**.
- **Classificação C5**: `depende_execucao`.

#### **C6 — Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches**
- **Fonte no artigo**: `[artigo.pdf:p. 2, §1, item 6; pp. 5-6, §3, "Flow Rule Integration" e "Flow Rule Editor"; p. 7, §5]` — *"Flow Rule Editor: consiste em uma ferramenta para visualização, criação e remoção de regras de fluxo OpenFlow nos switches."*
- **Resultado esperado**: Tabela de fluxo exibida, com a regra inserida ou removida no switch (`[reivindicacoes.md:12]`).
- **Critério documental (instruções de execução/processo)**: **Não atendido**. O `README.md` não menciona visualização, criação ou remoção de regras de fluxo OpenFlow em nenhuma seção (`[reivindicacoes.md:12]`: *"O README indica como reproduzir? não"*).
- **Suporte no código**: **Não atendido (implementação incompleta)**. O backend possui apenas leitura da tabela de fluxo via `dpctl("dump-flows")` em `[mininet-gui-backend/mininet_gui_backend/api.py:363-383]` (`[artefato.txt:778-798]`):
  > `flow_table_raw = node.dpctl("dump-flows").strip()`
  E o frontend exibe apenas uma tabela estática (somente leitura) ao dar duplo clique no switch em `[mininet-gui-frontend/src/components/NodeStats.vue:36-38, 62-93]` (`[artefato.txt:3518-3520, 3544-3575]`). Não existe no backend (`api.py`) nem no frontend qualquer endpoint, componente (`Flow Rule Editor`) ou função para criar/inserir ou remover regras de fluxo OpenFlow pela interface gráfica.
- **Classificação C6**: `nao_reproduzivel` (porém, conforme `[reivindicacoes.md:16]`, C6 não entra na regra de atribuição do selo R).

### 3. Decisão para o Selo R
- **Decisão**: **Indeterminado**. Pela regra explícita de `[reivindicacoes.md:16]` (*"R é atribuído se C4 e C5 forem reproduzidas. C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R"*), as duas reivindicações exigidas para R (**C4** e **C5**) estão documentadas na seção `# Experimentos` do `README.md` (`[README.md:105-114]`) e implementadas no código-fonte, dependendo apenas da execução para observar o comportamento esperado.
- **Confiança (0 a 100) de que o comitê oficial atribuiu o selo**: **80**. (As duas reivindicações elencadas pelos autores na seção `# Experimentos` do README — C4 e C5 — estão implementadas no código e são facilmente verificáveis na VM fornecida; há leve desconto pela brevidade da seção `# Experimentos` e pela ausência do editor de regras de fluxo prometido em C6 no texto do artigo).

### 4. O que precisaria ser observado na execução para mudar a decisão
- **Para mudar para Atribuir**: Executar a ferramenta (via VM ou instalação manual) e observar com sucesso:
  1. Em **C4**: a geração automatizada no grafo e no Mininet de topologias nos três modelos (`Single`, `Linear` e `Tree`) com o número de dispositivos configurado pelo usuário no modal "Generate Topology";
  2. Em **C5**: a abertura da aba de um nó emulado no painel inferior "WebShell", execução de comandos Bash no namespace daquele nó e exibição correta da saída na aba selecionada.
- **Para mudar para Não atribuir**: Observar durante a execução que ao menos um dos três modelos de topologia de **C4** (`Single`, `Linear` ou `Tree`) falha ao gerar os nós/links esperados, ou que o terminal WebShell (**C5**) não conecta via WebSocket / não exibe a saída dos comandos executados no nó, ou que o artefato não consegue sequer ser executado.

---

## D. Lacunas e riscos

1. **Erro de sintaxe em `mininet-gui-frontend/src/core/api.js` no commit arquivado**: Na linha 299 de `[mininet-gui-frontend/src/core/api.js:299]` (`[artefato.txt:4752]`), há um caractere `i` solto logo após o fechamento do bloco `catch` da função `requestRunPingall` (`}i`). Em uma execução direta a partir do código-fonte deste commit (ou se a VM contiver exatamente este arquivo sem modificação), o bundler Vite/esbuild acusará erro de sintaxe ao carregar `src/core/api.js` até que o caractere `i` seja removido.
2. **Funcionalidade reivindicada no artigo não implementada no código (C6 — Flow Rule Editor)**: O artigo descreve na Seção 3 os módulos *Flow Rule Integration* (`[artigo.pdf:p. 5]`) e *Flow Rule Editor* (`[artigo.pdf:p. 6]`) para *"visualização, criação e remoção de regras de fluxo OpenFlow nos switches"*. Contudo, o código contém apenas a visualização (`dump-flows` em `[mininet-gui-backend/mininet_gui_backend/api.py:363]` e tabela somente-leitura em `[mininet-gui-frontend/src/components/NodeStats.vue:62-93]`, que inclusive omite a coluna `actions`), sem qualquer implementação de criação, edição ou remoção de regras de fluxo.
3. **Uso de `nvm` em script não-interativo (`run.sh`)**: Em `[run.sh:20]` (`[artefato.txt:4893]`), o comando `(cd $FRONTEND_DIR ; nvm use 18.20.7 ; nohup npm run dev &)` invoca `nvm` sem antes carregar `source "$HOME/.nvm/nvm.sh"` (diferentemente do que é feito em `[setup.sh:16-17]`). Em subshells não-interativas do Bash, `nvm` não está definido como binário, embora `npm run dev` ainda funcione caso o Node/npm já esteja no `PATH` padrão da VM.
4. **Inconsistência documental nos requisitos de RAM da VM e rótulo de botão**: Em `[README.md:38]` (`[artefato.txt:123]`), informa-se *"Memória RAM: Mínimo de 8GB para a máquina virtual"*, embora a máquina hospedeira da demonstração tenha 8 GB totais (`[README.md:29]`) e a seção de Experimentos informe *"A execução da VM requer no mínimo 2GB de RAM"* (`[README.md:103]`). Além disso, `[README.md:108]` instrui clicar em *"OK"* no gerador de topologias, enquanto o botão real em `[mininet-gui-frontend/src/components/TopologyForm.vue:43]` (`[artefato.txt:4104]`) chama-se *"Submit"*.
5. **Dependência de artefato externo ([REMOVIDO] Drive)**: O método recomendado de instalação depende do download da imagem `Mininet-GUI-Desktop-VM-SBRC-2025.ova` hospedada no [REMOVIDO] Drive (`[README.md:53]`), cuja disponibilidade e integridade não podem ser aferidas sem acesso externo e execução.

```json
{"F": {"decisao": "Indeterminado", "confianca": 85, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:26-38", "README.md:47-99", "run.sh:1-28", "setup.sh:1-24", "mininet-gui-frontend/src/core/api.js:299"]},
 "R": {"decisao": "Indeterminado", "confianca": 80, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:7-20", "README.md:80-114", "mininet-gui-frontend/src/components/TopologyForm.vue:5-44", "mininet-gui-frontend/src/components/NetworkGraph.vue:512-617", "mininet-gui-frontend/src/components/Webshell.vue:1-192", "mininet-gui-backend/mininet_gui_backend/api.py:363-383", "mininet-gui-backend/mininet_gui_backend/api.py:450-491", "mininet-gui-frontend/src/components/NodeStats.vue:62-93"],
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

> **Nota**: Este roteiro foi elaborado analiticamente a partir de `README.md`, `artigo.pdf`, `reivindicacoes.md` e do código-fonte em `artefato.txt` (commit `465648a4425a4457af0348ab951cf7f71d37a86f`). Nenhuma execução foi realizada. Passos não descritos pelos autores no `README.md` estão marcados como **[NÃO DOCUMENTADO]** com a respectiva justificativa.

---

## 1. Requisitos de Hardware e Software do Ambiente

### Hardware documentado pelos autores
- **Máquina hospedeira usada na demonstração** (`[README.md:26-32]`):
  - Processador: Intel Core i5-10300H @ 2.50 GHz (x64, 64 bits)
  - Memória RAM: 8,00 GB
  - Espaço livre em disco: pelo menos 80 GB livres
- **Recursos para a Máquina Virtual (VM)**:
  - Seção `# Dependências` (`[README.md:38]`): mínimo de 8 GB de RAM para a VM.
  - Seção `# Experimentos` (`[README.md:103]`): mínimo de 2 GB de RAM e 1 core de CPU reservado à VM.

### Software documentado pelos autores
- **Opção A — Máquina Virtual (recomendada pelos autores em `[README.md:49-58]`)**:
  - Sistema Hospedeiro: Windows 11 64 bits (ou compatível com VirtualBox)
  - Hipervisor: Oracle VirtualBox versão `7.1.6 r167084` (`[README.md:37]`)
  - Imagem da VM: `Mininet-GUI-Desktop-VM-SBRC-2025.ova` obtida via [REMOVIDO] Drive (`[README.md:53-55]`), usuário `mininet`, senha `mininet` (`[README.md:57]`)
- **Opção B — Instalação Manual (`[README.md:60-78]` e `[setup.sh:1-24]`)**:
  - Sistema Operacional: Ubuntu 20.04 (`[README.md:63]`) — *Atenção: os autores alertam que a instalação nativa do Mininet modifica o kernel e arquivos do sistema (`[README.md:43, 62]`)*
  - Pacotes de sistema e ferramentas: `git`, `curl`, `npm`, `python3`, `pip3`, `sudo` (`[README.md:66-77]`, `[setup.sh:3, 10]`)
  - Emulador e Controlador: Mininet instalado com `./util/install.sh -nfv` (`[README.md:68]`) e opcionalmente controlador SDN Ryu com `ryu`, `eventlet==0.30.0`, `dnspython==1.16.0` (`[README.md:77]`)
  - Backend Python (`[mininet-gui-backend/requirements.txt:1-4]`): `fastapi`, `websockets`, `uvicorn`, `python-multipart`
  - Frontend Node.js (`[setup.sh:13-22]`, `[mininet-gui-frontend/package.json:10-23]`): `nvm v0.40.2`, `Node.js 18.20.7`, `vue ^3.2.45`, `vis-network ^9.1.2`, `vis-data ^7.1.4`, `axios ^1.2.1`, `vite ^4.0.0`

---

## 2. Preparação do Ambiente e Teste Mínimo (Selo F)

### **P1 — Instalação do ambiente (VM recomendada ou Instalação Manual)**
- **Selo e reivindicação relacionados**: Selo F (Instalação e preparação do ambiente)
- **Diretório**: Máquina hospedeira (Opção A - VM) ou `~` no Ubuntu 20.04 (Opção B - Manual)
- **Comando exato**:
  - **Opção A (VM — recomendado, `[README.md:53-57]`, `[README.md:82]`)**:
    1. Baixar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` de `https://drive.[REMOVIDO]/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing`
    2. Importar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no Oracle VirtualBox.
    3. Iniciar a VM e fazer login com usuário `mininet` e senha `mininet`.
  - **Opção B (Instalação manual no Ubuntu 20.04, `[README.md:65-78]`)**:
    ```bash
    git clone https://github.com/mininet/mininet
    cd mininet
    ./util/install.sh -nfv
    cd ..
    git clone https://github.com/latarc/mininet-gui
    cd mininet-gui
    ./setup.sh
    pip3 install ryu eventlet==0.30.0 dnspython==1.16.0
    ```
- **Resultado esperado segundo os autores**: VM importada e sessão iniciada com o usuário `mininet` (`[README.md:55-57, 82]`), ou dependências do Mininet, backend, Node 18.20.7, frontend e alias `mininet_gui` configurados (`[setup.sh:9-24]`).
- **Evidência a salvar**: Captura de tela da VM logada ou log completo do terminal da execução de `install.sh` e `setup.sh` (`p1_instalacao.log`).
- **Critério de sucesso**: Login realizado na VM (Opção A) ou término de `./setup.sh` sem erros fatais e diretório `/home/mininet/mininet-gui` presente (Opção B).
- **Critério de falha**: Link do arquivo `.ova` indisponível/corrompido e falha na instalação manual de dependências (`mininet`, `uvicorn` ou `npm install`).
- **Critério de interrupção**: Interromper toda a avaliação caso nem a VM possa ser importada/iniciada nem a instalação manual conclua a instalação do Mininet e das dependências.

---

### **P2 [NÃO DOCUMENTADO] — Verificação e saneamento preventivo de erro de sintaxe em `api.js` e ambiente `nvm`**
- **Justificativa**: No código-fonte arquivado no commit `465648a4425a4457af0348ab951cf7f71d37a86f`, a linha 299 de `mininet-gui-frontend/src/core/api.js` contém um caractere `i` espúrio após o fechamento de chave (`}i`), o que provoca erro de sintaxe no compilador do Vite (`npm run dev`). Além disso, `run.sh:20` executa `nvm use 18.20.7` dentro de uma subshell de script não-interativo sem carregar `$HOME/.nvm/nvm.sh`. É necessário inspecionar (e corrigir, se presente) antes de iniciar os serviços para não confundir um erro trivial de 1 caractere com falha estrutural.
- **Selo e reivindicação relacionados**: Selo F e Selo R (pré-condição técnica para execução do frontend)
- **Diretório**: `/home/mininet/mininet-gui`
- **Comando exato**:
  ```bash
  grep -n "}i" mininet-gui-frontend/src/core/api.js
  # Caso a linha 299 contenha "}i", registrar evidência e corrigir para "}":
  sed -i 's/}i$/}/' mininet-gui-frontend/src/core/api.js
  ```
- **Resultado esperado segundo os autores**: Não documentado pelos autores; espera-se que `mininet-gui-frontend/src/core/api.js` seja um módulo ES válido sem caracteres residuais fora de blocos.
- **Evidência a salvar**: Saída do comando `grep -n "}i" mininet-gui-frontend/src/core/api.js` e `git diff` antes/depois na VM (`p2_verificacao_api_js.txt`).
- **Critério de sucesso**: Arquivo `mininet-gui-frontend/src/core/api.js` sem o erro de sintaxe `}i`.
- **Critério de falha**: Arquivo ausente ou sem permissão de leitura/escrita.
- **Critério de interrupção**: Não interrompe; prosseguir para P3 registrando se a VM já estava corrigida ou se exigiu o `sed`.

---

### **P3 — Inicialização do backend e frontend (`mininet_gui` / `run.sh`) e acesso à interface web**
- **Selo e reivindicação relacionados**: Selo F (Execução do artefato; Passos 2 e 3 do Teste Mínimo)
- **Diretório**: `/home/mininet/mininet-gui`
- **Comando exato**:
  ```bash
  mininet_gui
  # Ou alternativamente, conforme README.md:84:
  /home/mininet/mininet-gui/run.sh
  ```
  Em seguida, abrir no navegador dentro da VM a URL impressa no terminal (ex.: `http://10.0.2.15:5173`, conforme `[README.md:86]`).
- **Resultado esperado segundo os autores**: O terminal exibe `Mininet-GUI bootstrap complete` e a URL `http://<IP>:5173` (`[run.sh:22-28]`, `[README.md:86]`); o navegador carrega a interface web do Mininet-GUI com barra lateral esquerda ("Topology Controls", "Actions", "Export/Import", "Nodes Palette"), área central do grafo e painel inferior "WebShell" (`[artigo.pdf:p. 7, Fig. 2]`).
- **Evidência a salvar**: Saída do terminal de `run.sh`, arquivos `/home/mininet/mininet-gui/mininet-gui-backend/nohup.out` e `/home/mininet/mininet-gui/mininet-gui-frontend/nohup.out`, e captura de tela da interface inicial carregada no navegador (`p3_interface_inicial.png`).
- **Critério de sucesso**: Processo `uvicorn` escutando na porta `8000`, processo `vite` escutando na porta `5173` e página web renderizada sem tela em branco ou erro de conexão.
- **Critério de falha**: Processo `uvicorn` ou `vite` encerra imediatamente com erro nos arquivos `nohup.out`, ou navegador não carrega a SPA na porta `5173`.
- **Critério de interrupção**: Se `vite` falhar em `run.sh:20` por `nvm: command not found` e `npm` não estiver no `PATH` padrão, carregar `export NVM_DIR="$HOME/.nvm" && source "$NVM_DIR/nvm.sh"` **[NÃO DOCUMENTADO]** e reexecutar `run.sh`. Se ainda assim backend ou frontend não iniciarem, interromper a execução.

---

### **P4 — Teste Mínimo (Passos 4 e 5): Criação de controlador Default e geração de topologia Single**
- **Selo e reivindicação relacionados**: Selo F (Teste Mínimo, Passos 4 e 5); também exercita C1 e C4 (modelo Single)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Na barra lateral esquerda ("Nodes Palette"), arrastar o ícone **"Controller"** para o centro da tela (`[README.md:88]`).
  2. Na caixa de diálogo "Controller Form", manter **"Controller Type"** em `Default` e clicar no botão **"Submit"** (`[README.md:88]`).
  3. Clicar no botão **"Generate Topology"** na barra lateral esquerda (`[README.md:90]`).
  4. No modal "Create Topology", selecionar **"Topology Type"**: `Single`, **"Controller"**: `c1`, preencher **"Hosts"**: `2` e clicar no botão **"Submit"** (`[README.md:90]`).
- **Resultado esperado segundo os autores**: O controlador `c1` é criado no grafo; em seguida, é gerada uma topologia Single composta pelo switch `s1` associado a `c1` (linha tracejada cinza) e 2 hosts (`h1`, `h2`) conectados a `s1` por links ativos (linhas verdes), além das abas `c1`, `s1`, `h1`, `h2` no painel WebShell (`[README.md:88-90]`, `[artigo.pdf:p. 7]`).
- **Evidência a salvar**: Captura de tela do grafo exibindo `c1`, `s1`, `h1` e `h2` conectados (`p4_topologia_single.png`) e log do backend (`mininet-gui-backend/nohup.out`).
- **Critério de sucesso**: Nós `c1`, `s1`, `h1`, `h2` visíveis no grafo, aresta tracejada entre `s1` e `c1`, arestas verdes entre `s1`–`h1` e `s1`–`h2`, e retorno HTTP 200 nas rotas `/api/mininet/controllers`, `/api/mininet/switches`, `/api/mininet/hosts` e `/api/mininet/links`.
- **Critério de falha**: Alerta `"Network Error"` no navegador, falha ao renderizar os nós no grafo ou erro HTTP 400/500 no backend.
- **Critério de interrupção**: Interromper o Teste Mínimo se a criação de nós básicos falhar.

---

### **P5 — Teste Mínimo (Passo 6): Teste de conectividade com Pingall**
- **Selo e reivindicação relacionados**: Selo F (Teste Mínimo, Passo 6); também exercita C2
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Clicar no botão **"Run Pingall Test"** na barra lateral esquerda, sob o grupo "Actions" (`[README.md:92]`).
  2. Aguardar a exibição dos resultados no modal **"Pingall Results"** (`[README.md:92]`).
- **Resultado esperado segundo os autores**: Modal "Pingall Results" exibe a tabela com os pares de origem/destino (`h1` -> `h2` e `h2` -> `h1`), pacotes enviados/recebidos (`1`/`1`) e métricas de RTT (`min`, `avg`, `max`, `mdev`) (`[README.md:92]`, `[mininet-gui-frontend/src/components/PingallResults.vue:30-62]`).
- **Evidência a salvar**: Captura de tela do modal "Pingall Results" preenchido (`p5_pingall_results.png`).
- **Critério de sucesso**: Tabela renderizada no modal mostrando comunicação bem-sucedida (`packets_sent: 1`, `packets_recv: 1`) entre `h1` e `h2`.
- **Critério de falha**: Modal exibe `"No ping results available."`, alerta de erro ou perda total de pacotes (`1/0`).
- **Critério de interrupção**: Não interrompe; fechar o modal clicando em `X` ou pressionando `Esc` para seguir ao próximo passo.

---

### **P6 — Teste Mínimo (Passo 7 opcional): Teste de vazão com `iperf` via WebShell**
- **Selo e reivindicação relacionados**: Selo F (Teste Mínimo, Passo 7 opcional); também exercita C5 e Caso de Uso 2 do artigo (`[artigo.pdf:p. 6, §4]`)
- **Diretório**: Painel inferior "WebShell" na Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. No painel inferior **"WebShell"**, clicar na aba **`H1`**, clicar na área do terminal e executar (`[README.md:94]`):
     ```bash
     iperf -s
     ```
  2. No painel inferior **"WebShell"**, clicar na aba **`H2`**, clicar na área do terminal e executar (`[README.md:94]`):
     ```bash
     iperf -c 10.0.0.1
     ```
  3. Aguardar até 1 minuto para a conclusão do teste (`[README.md:94]`).
- **Resultado esperado segundo os autores**: A aba `h1` exibe o servidor iperf escutando e a conexão recebida de `10.0.0.2`; a aba `h2` exibe o relatório de transferência e largura de banda medida entre `10.0.0.2` e `10.0.0.1` (`[README.md:94]`).
- **Evidência a salvar**: Capturas de tela das abas `h1` e `h2` do WebShell com a saída do `iperf` (`p6_iperf_h1.png`, `p6_iperf_h2.png`).
- **Critério de sucesso**: Saída do `iperf` exibida nos terminais de `h1` e `h2` com taxa de transferência calculada.
- **Critério de falha**: Terminal WebShell não aceita digitação, não abre sessão WebSocket ou comando `iperf` falha por falta de conectividade.
- **Critério de interrupção**: Não interrompe; prosseguir para P7.

---

### **P7 — Teste Mínimo (Passo 8 opcional): Múltiplos controladores com Ryu e ligação em tempo real**
- **Selo e reivindicação relacionados**: Selo F (Teste Mínimo, Passo 8 opcional); também exercita C1, C2, C3, C5 e Caso de Uso 3 do artigo (`[artigo.pdf:p. 7, §4]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Arrastar um novo **"Controller"** da barra lateral para o centro da tela (`[README.md:96]`).
  2. No modal "Controller Form", mudar **"Controller Type"** para `Remote`, preencher **"IP"**: `127.0.0.1` e **"Port"**: `6633`, e clicar em **"Submit"** (`[README.md:96]`).
  3. Clicar em **"Generate Topology"**, selecionar **"Topology Type"**: `Single`, **"Controller"**: `c2`, **"Hosts"**: `2`, e clicar em **"Submit"** (`[README.md:96]`).
  4. Clicar no botão **"Create Link"** na barra lateral e conectar os switches `s1` e `s2` clicando e arrastando de `s1` para `s2` (`[README.md:96]`).
  5. No painel **"WebShell"**, clicar na aba do controlador **`C2`** e executar (`[README.md:96]`):
     ```bash
     ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13
     ```
  6. Clicar no botão **"Run Pingall Test"** na barra lateral (`[README.md:96]`).
- **Resultado esperado segundo os autores**: Um segundo controlador `c2 <127.0.0.1:6633>`, um switch `s2` e dois novos hosts (`h3`, `h4`) são adicionados à topologia em execução sem reiniciá-la; uma linha verde conecta `s1` e `s2`; o controlador Ryu inicia no WebShell de `c2`; o teste de Pingall mostra conectividade entre todos os 4 hosts (`h1` a `h4`) (`[README.md:96]`).
- **Evidência a salvar**: Captura de tela do grafo com os dois controladores (`c1`, `c2`) e link verde entre `s1` e `s2` (`p7_multi_controlador.png`), saída do `ryu-manager` no WebShell e captura do modal "Pingall Results" com os 4 hosts (`p7_pingall_4hosts.png`).
- **Critério de sucesso**: Link verde criado entre `s1` e `s2`, `ryu-manager` em execução e `Pingall` exibindo respostas entre os hosts das duas sub-redes (`h1`, `h2`, `h3`, `h4`).
- **Critério de falha**: Falha ao criar controlador remoto, link entre `s1` e `s2` não estabelecido, `ryu-manager` não encontrado ou `pingall` sem conectividade entre switches.
- **Critério de interrupção**: Não interrompe; prosseguir para P8.

---

### **P8 — Teste Mínimo (Passo 9): Exportação da topologia em JSON e Script Python do Mininet**
- **Selo e reivindicação relacionados**: Selo F (Teste Mínimo, Passo 9)
- **Diretório**: Interface Web (`http://<IP>:5173`) e diretório `~/Downloads` da VM
- **Comando exato**:
  1. Clicar no botão **"Export Topology (JSON)"** na barra lateral esquerda, sob "Export/Import" (`[README.md:98]`).
  2. Clicar no botão **"Export Mininet Script"** na barra lateral esquerda, sob "Export/Import" (`[README.md:98]`).
- **Resultado esperado segundo os autores**: Download no navegador de dois arquivos: `network_export.json` (contendo as listas `switches`, `hosts`, `controllers`, `links` no mesmo formato de `example_network_export.json`) e `network_export.py` (script Python executável com a API do Mininet, no formato de `example_network_export.py`) (`[README.md:12, 98]`, `[mininet-gui-frontend/src/core/api.js:219-281]`).
- **Evidência a salvar**: Cópias dos arquivos baixados `network_export.json` e `network_export.py`.
- **Critério de sucesso**: Ambos os arquivos são baixados, não estão vazios, `network_export.json` é um JSON válido contendo os nós da topologia atual e `network_export.py` é sintaticamente válido em Python.
- **Critério de falha**: Download não inicia, erro HTTP nas rotas `/api/mininet/export_json` ou `/api/mininet/export_script`, ou arquivos gerados vazios/corrompidos.
- **Critério de interrupção**: Fim da seção do Teste Mínimo (Selo F); prosseguir para os blocos de verificação das reivindicações (Selo R).

---

## 3. Verificação por Reivindicação de `reivindicacoes.md` (Selo R)

> **Regra para o selo R (`[reivindicacoes.md:16-20]`)**: O README destaca na seção `# Experimentos` duas reivindicações a reproduzir: **C4** e **C5**. **R é atribuído se C4 (nos três modelos: Single, Linear e Tree) e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R; ainda assim, todas as seis reivindicações possuem blocos de verificação abaixo conforme solicitado.

---

### Bloco C1 — Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo

#### **P9 — Verificação de C1 (Criação e manipulação visual de elementos no grafo interativo)**
- **Selo e reivindicação relacionados**: Selo F e Reivindicação C1 (`[reivindicacoes.md:7]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Caso haja nós de testes anteriores, clicar em **"Reset Topology"** na barra lateral e confirmar no diálogo do navegador **[NÃO DOCUMENTADO no texto do README, mas presente na interface em `Side.vue:22-25` e necessário para limpar o estado entre testes]**.
  2. Seguir os passos de criação e manipulação visual (`[README.md:88-91, 96]`):
     - Arrastar **"Controller"** da paleta lateral para o grafo e submeter como `Default` (`c1`).
     - Arrastar **"Switch"** da paleta lateral para o grafo (`s1`) e arrastar **"Host"** para o grafo (`h1`, `h2`).
     - Clicar em **"Create Link"** e conectar `c1` a `s1`, `s1` a `h1` e `s1` a `h2`.
     - Arrastar os nós no canvas para alterar suas posições e usar os atalhos/controles visuais.
- **Resultado esperado segundo os autores**: Elementos criados pelo usuário são representados no grafo interativo (`vis-network`) e respondem às ações de criação, ligação e reposicionamento (`[reivindicacoes.md:7]`, `[artigo.pdf:p. 5-7]`).
- **Evidência a salvar**: Captura de tela do grafo após criação e reposicionamento dos nós (`p9_c1_grafo_interativo.png`).
- **Critério de sucesso**: Todos os elementos arrastados (`controller`, `switch`, `host`) e links aparecem no grafo e respondem à interação do mouse sem erros.
- **Critério de falha**: Nós não aparecem ao soltar no canvas, links não são criados ou grafo trava.
- **Critério de interrupção**: Não interrompe; prosseguir para o Bloco C2.

---

### Bloco C2 — Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade

#### **P10 — Verificação de C2 (Emulação Mininet gerenciada pela interface e teste `pingall`)**
- **Selo e reivindicação relacionados**: Selo F e Reivindicação C2 (`[reivindicacoes.md:8]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Com a topologia ativa no grafo (ou executando os Passos 4 a 6 do Teste Mínimo em `[README.md:88-92]`): clicar em **"Run Pingall Test"** na barra lateral esquerda.
- **Resultado esperado segundo os autores**: Nós emulados no Mininet pelo backend e resultado de `pingall` exibido na interface dentro do modal "Pingall Results" (`[reivindicacoes.md:8]`, `[README.md:92]`).
- **Evidência a salvar**: Captura de tela da tabela de resultados do `pingall` na interface (`p10_c2_pingall.png`).
- **Critério de sucesso**: Modal exibe a tabela com pacotes enviados/recebidos e tempos de RTT obtidos da execução real do `pingFull()` no Mininet.
- **Critério de falha**: Erro ao executar `pingall` ou ausência de exibição dos resultados na interface.
- **Critério de interrupção**: Não interrompe; prosseguir para o Bloco C3.

---

### Bloco C3 — Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la

#### **P11 — Verificação de C3 (Adição e remoção de nós e links com a emulação em andamento)**
- **Selo e reivindicação relacionados**: Selo F e Reivindicação C3 (`[reivindicacoes.md:9]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. **Adição em tempo real (documentada em `[README.md:96]`, Passo 8)**: Com a emulação já em andamento e sem clicar em "Reset Topology", arrastar um novo Host (ou Controller/Switch) da paleta para o grafo e conectá-lo a um switch existente usando **"Create Link"**, executando **"Run Pingall Test"** para confirmar que o novo nó participa da emulação ativa.
  2. **Remoção em tempo real ([NÃO DOCUMENTADO no passo a passo do `README.md`, mas exigido pela reivindicação C3 em `[reivindicacoes.md:9]` e `[artigo.pdf:p. 6, §3]` e implementado no botão `"Delete Selected"` em `Side.vue:35-38`])**:
     - Clicar sobre um link ou nó recém-adicionado no grafo para selecioná-lo.
     - Clicar no botão **"Delete Selected"** na barra lateral esquerda (sob "Actions") ou pressionar a tecla `Delete`/`d`.
     - Executar novamente **"Run Pingall Test"** para confirmar que a emulação continua ativa apenas com os nós remanescentes, sem ter sido reiniciada.
- **Resultado esperado segundo os autores**: A rede emulada é alterada dinamicamente (nós e links criados e removidos em tempo de execução) enquanto a emulação continua ativa, sem necessidade de interromper ou reiniciar o Mininet (`[reivindicacoes.md:9]`, `[artigo.pdf:p. 6, §3]`).
- **Evidência a salvar**: Capturas de tela antes/depois da adição e antes/depois da remoção de nós/links, acompanhadas dos respectivos modais de "Pingall Results" (`p11_c3_tempo_real_add.png`, `p11_c3_tempo_real_del.png`).
- **Critério de sucesso**: Nós e links são adicionados e removidos no grafo e no Mininet (verificado pelo resultado atualizado do `pingall`) sem reiniciar a rede.
- **Critério de falha**: Remoção ou adição exige reiniciar a rede, causa queda da emulação ou mantém nós deletados respondendo ao `pingall`.
- **Critério de interrupção**: Não interrompe; prosseguir para o Bloco C4.

---

### Bloco C4 — Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido *(Obrigatório para o Selo R)*

> **Critério de reprodução (`[reivindicacoes.md:16, 20]`)**: C4 deve ser observada nos **três modelos** (`Single`, `Linear` e `Tree`).
> **Observação sobre a interface**: Embora `[README.md:108]` mencione *"então clique em OK"*, o botão do formulário em `[mininet-gui-frontend/src/components/TopologyForm.vue:43]` (e no Passo 5 do Teste Mínimo em `[README.md:90]`) é rotulado **"Submit"**. Além disso, para testar os três modelos isoladamente sem sobrepor nós no grafo, utiliza-se o botão **"Reset Topology"** **[NÃO DOCUMENTADO na seção Experimentos, mas necessário para isolar cada modelo gerado]**.

#### **P12 — Verificação de C4, Modelo 1 (`Single`)**
- **Selo e reivindicação relacionados**: Selo R — Reivindicação C4 (`[reivindicacoes.md:10, 16, 20]`, `[README.md:90, 105-108]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Clicar em **"Reset Topology"** e confirmar **[NÃO DOCUMENTADO na seção Experimentos, necessário para partir de topologia limpa]**.
  2. (Opcional) Arrastar um **"Controller"** (`Default` -> **"Submit"**) para dispor de `c1`.
  3. Clicar no botão **"Generate Topology"** na barra lateral esquerda (`[README.md:107]`).
  4. No modal "Create Topology", selecionar **"Topology Type"**: `Single`, **"Controller"**: `c1` (ou `none`), inserir em **"Hosts"** o número de dispositivos desejado (ex.: `3`) e clicar em **"Submit"** (`[README.md:90, 107-108]`).
- **Resultado esperado segundo os autores**: Geração automatizada no grafo e no Mininet de uma topologia `Single` contendo 1 switch (`s1`) conectado à quantidade escolhida de hosts (`h1`, `h2`, `h3`) (`[reivindicacoes.md:10, 20]`, `[mininet-gui-frontend/src/components/NetworkGraph.vue:512-523]`).
- **Evidência a salvar**: Captura de tela do modal configurado para `Single` e do grafo gerado (`p12_c4_single.png`).
- **Critério de sucesso**: Grafo e abas do WebShell exibem exatamente 1 switch e o número de hosts informado (ex.: 3 hosts), todos interligados ao switch.
- **Critério de falha**: Topologia não é gerada ou quantidade de dispositivos diverge da escolhida.
- **Critério de interrupção**: Se falhar, registrar a falha de C4 (o que impede a atribuição de R segundo `[reivindicacoes.md:16]`), mas continuar para testar `Linear` e `Tree`.

#### **P13 — Verificação de C4, Modelo 2 (`Linear`)**
- **Selo e reivindicação relacionados**: Selo R — Reivindicação C4 (`[reivindicacoes.md:10, 16, 20]`, `[README.md:105-108]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Clicar em **"Reset Topology"** e confirmar **[NÃO DOCUMENTADO na seção Experimentos, necessário para limpar a topologia anterior]**.
  2. (Opcional) Arrastar um **"Controller"** (`Default` -> **"Submit"**) para dispor de `c1`.
  3. Clicar no botão **"Generate Topology"** na barra lateral esquerda (`[README.md:107]`).
  4. No modal "Create Topology", selecionar **"Topology Type"**: `Linear`, **"Controller"**: `c1` (ou `none`), preencher **"Switches"**: `3` e **"Hosts per switch"**: `2` **[valores de teste escolhidos conforme campos de `TopologyForm.vue:24-32`]** e clicar em **"Submit"** (`[README.md:107-108]`).
- **Resultado esperado segundo os autores**: Geração automatizada de uma topologia `Linear` com 3 switches (`s1`, `s2`, `s3`) encadeados linearmente (`s1`–`s2`–`s3`) e 2 hosts conectados a cada switch (totalizando 6 hosts: `h1` a `h6`) (`[reivindicacoes.md:10, 20]`, `[mininet-gui-frontend/src/components/NetworkGraph.vue:524-552]`).
- **Evidência a salvar**: Captura de tela do modal configurado para `Linear` e do grafo gerado com 3 switches e 6 hosts (`p13_c4_linear.png`).
- **Critério de sucesso**: Grafo exibe os 3 switches conectados em linha e 2 hosts por switch (6 hosts no total).
- **Critério de falha**: Switches não são conectados em linha ou número de switches/hosts diverge do especificado.
- **Critério de interrupção**: Não interrompe; prosseguir para P14 (`Tree`).

#### **P14 — Verificação de C4, Modelo 3 (`Tree`)**
- **Selo e reivindicação relacionados**: Selo R — Reivindicação C4 (`[reivindicacoes.md:10, 16, 20]`, `[README.md:105-108]`)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Clicar em **"Reset Topology"** e confirmar **[NÃO DOCUMENTADO na seção Experimentos, necessário para limpar a topologia anterior]**.
  2. (Opcional) Arrastar um **"Controller"** (`Default` -> **"Submit"**) para dispor de `c1`.
  3. Clicar no botão **"Generate Topology"** na barra lateral esquerda (`[README.md:107]`).
  4. No modal "Create Topology", selecionar **"Topology Type"**: `Tree`, **"Controller"**: `c1` (ou `none`), preencher **"Layers"**: `2` e **"Fanout"**: `2` **[valores de teste escolhidos conforme campos de `TopologyForm.vue:34-42`]** e clicar em **"Submit"** (`[README.md:107-108]`).
- **Resultado esperado segundo os autores**: Geração automatizada de uma topologia em árvore (`Tree`) com profundidade (`Layers`) 2 e grau de ramificação (`Fanout`) 2, contendo 1 switch raiz (`s3`), 2 switches filhos (`s1`, `s2`) e 4 hosts nas folhas (`h1` a `h4`), similar à Figura 2 do artigo (`[artigo.pdf:p. 7, Fig. 2]`, `[reivindicacoes.md:10, 20]`, `[mininet-gui-frontend/src/components/NetworkGraph.vue:553-585]`).
- **Evidência a salvar**: Captura de tela do modal configurado para `Tree` e do grafo em árvore gerado (`p14_c4_tree.png`).
- **Critério de sucesso**: Grafo exibe hierarquia em árvore correspondente aos parâmetros `Layers=2` e `Fanout=2` (3 switches e 4 hosts devidamente conectados).
- **Critério de falha**: Topologia em árvore não é criada ou conexões pai-filho falham.
- **Critério de interrupção**: Não interrompe; prosseguir para o Bloco C5.

---

### Bloco C5 — Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado *(Obrigatório para o Selo R)*

#### **P15 — Verificação de C5 (Execução de comandos Bash no namespace de um nó via WebShell)**
- **Selo e reivindicação relacionados**: Selo R — Reivindicação C5 (`[reivindicacoes.md:11, 16, 20]`, `[README.md:110-114]`)
- **Diretório**: Painel inferior "WebShell" na Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. Com ao menos um nó criado no grafo (por exemplo, `h1` e `h2` da topologia gerada em P14, ou criando um nó pelo Gerador de Topologias / arrastando da paleta, conforme `[README.md:112]`), localizar a aba inferior intitulada **"WebShell"** (`[README.md:112]`).
  2. Clicar na aba com o nome do nó desejado (ex.: **`H1`**) (`[README.md:113]`).
  3. Clicar dentro da janela preta do terminal e executar comandos Bash para inspecionar o namespace de rede daquele nó (`[README.md:114]`, `[artigo.pdf:p. 7, Fig. 2]`):
     ```bash
     ip addr show
     ping -c 2 10.0.0.2
     ```
- **Resultado esperado segundo os autores**: A saída do comando Bash executado no namespace do nó emulado (ex.: interface `h1-eth0` com IP `10.0.0.1/8` mostrada por `ip addr show`, conforme ilustrado na Figura 2 de `[artigo.pdf:p. 7]`, e respostas do `ping`) é exibida diretamente na aba do nó selecionado no WebShell (`[reivindicacoes.md:11]`, `[README.md:112-114]`).
- **Evidência a salvar**: Captura de tela do painel WebShell na aba `H1` mostrando o prompt Bash e a saída dos comandos `ip addr show` e `ping` (`p15_c5_webshell.png`).
- **Critério de sucesso**: Conexão WebSocket `/api/mininet/terminal/h1` ativa, comandos digitados são enviados ao `/bin/bash -i` do nó `h1`, e a saída exibida na aba `H1` comprova execução no namespace isolado do nó (`h1-eth0` com IP `10.0.0.1/8`).
- **Critério de falha**: Aba do nó não abre sessão de terminal, caracteres digitados não produzem saída ou comandos rodam fora do namespace do nó.
- **Critério de interrupção**: Não interrompe; prosseguir para o Bloco C6.

---

### Bloco C6 — Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches

> **Nota sobre C6**: Conforme `[reivindicacoes.md:12, 16]`, o `README.md` **não** fornece instruções para reproduzir C6, e C6 não entra na regra de atribuição de R (embora seja a contribuição 6 do artigo em `[artigo.pdf:p. 2, §1; pp. 5-6, §3]`). O passo abaixo é integralmente **[NÃO DOCUMENTADO]** no README e baseia-se na inspeção do código (`NetworkGraph.vue:277-281` e `NodeStats.vue:36-38, 62-93`) para comprovar em execução o que está implementado (apenas visualização) e o que está ausente (criação e remoção).

#### **P16 [NÃO DOCUMENTADO] — Verificação de C6 (Inspeção da tabela de fluxos do switch e ausência de criação/remoção)**
- **Justificativa**: O `README.md` omite qualquer instrução sobre regras de fluxo OpenFlow (`[reivindicacoes.md:12]`). Pelo código-fonte (`[mininet-gui-frontend/src/components/NetworkGraph.vue:277-281]`), o modal de estatísticas/fluxos de um nó é aberto por duplo clique (`doubleClick`) sobre o nó no grafo. Este passo é necessário para verificar experimentalmente a reivindicação C6.
- **Selo e reivindicação relacionados**: Reivindicação C6 (`[reivindicacoes.md:12]`, embasa análise de F, não entra na regra de R)
- **Diretório**: Interface Web (`http://<IP>:5173`)
- **Comando exato**:
  1. No grafo com uma topologia ativa contendo ao menos um switch (ex.: `s1`), efetuar **duplo clique** sobre o ícone do switch `s1`.
  2. No modal aberto (**"Node Info: s1"**), clicar na aba **"Flow Table"**.
  3. Verificar se a tabela de fluxos OpenFlow é exibida e se há na interface qualquer botão, formulário ou controle (*Flow Rule Editor*) que permita inserir ou remover uma regra de fluxo no switch.
- **Resultado esperado segundo os autores**: Segundo o artigo (`[artigo.pdf:p. 6, §3]`), o *Flow Rule Editor* permitiria *"visualização, criação e remoção de regras de fluxo OpenFlow nos switches"*, esperando-se ver a *"tabela de fluxo exibida, com a regra inserida ou removida no switch"* (`[reivindicacoes.md:12]`). Segundo a análise do código (`[mininet-gui-frontend/src/components/NodeStats.vue:62-93]`), apenas a visualização estática (`dump-flows`) será exibida, sem opção de criar ou remover regras.
- **Evidência a salvar**: Captura de tela do modal `"Node Info: s1"` na aba `"Flow Table"` (`p16_c6_flow_table.png`).
- **Critério de sucesso**: Para reprodução integral de C6, a tabela de fluxo deveria ser exibida e permitir inserir ou remover uma regra de fluxo no switch pela interface. (Caso exiba apenas a tabela somente-leitura sem controles de adição/remoção, confirma-se C6 como parcialmente implementada / `nao_reproduzivel`).
- **Critério de falha**: Ausência de controles para inserir ou remover regras de fluxo OpenFlow no switch (ou falha ao abrir o modal `"Node Info"`).
- **Critério de interrupção**: Fim do roteiro de execução.

---

## 4. Tempo Estimado

- **Preparação e Instalação (P1–P2)**: ~15 a 30 minutos (dependendo da velocidade de download da imagem `.ova` ou dos pacotes na instalação manual).
- **Inicialização e Teste Mínimo — Selo F (P3–P8)**: ~10 a 15 minutos (incluindo 1 minuto do teste `iperf` em P6 e inicialização do controlador Ryu em P7).
- **Verificação das Reivindicações — Selo R (P9–P16)**: ~10 a 15 minutos (~2 minutos por passo na interface web).
- **Tempo total estimado**: **35 a 60 minutos**.

---

## 5. Tabela Resumo de Todos os Passos

| Passo | Documentado no README? | Selo / Reivindicação | Diretório / Local | Comando / Ação Resumida | Resultado Esperado | Evidência a Salvar | Tempo Est. |
|---|---|---|---|---|---|---|---|
| **P1** | Sim (`README.md:49-78, 82`) | F (Instalação) | Host / `~` (VM ou Ubuntu 20.04) | Importar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no VirtualBox (login `mininet`/`mininet`) ou rodar `install.sh -nfv` + `./setup.sh` | Ambiente VM logado ou dependências instaladas | `p1_instalacao.log` / screenshot | 15–25 min |
| **P2** | **[NÃO DOCUMENTADO]** | F, R (Pré-condição) | `/home/mininet/mininet-gui` | `grep -n "}i" mininet-gui-frontend/src/core/api.js` e `sed -i 's/}i$/}/' ...` se presente | `api.js` sem erro de sintaxe `}i` na linha 299 | `p2_verificacao_api_js.txt` | 1 min |
| **P3** | Sim (`README.md:84-86`) | F (Execução) | `/home/mininet/mininet-gui` + Navegador | Executar `mininet_gui` (ou `./run.sh`) e acessar `http://<IP>:5173` | Backend (porta 8000) e Frontend (porta 5173) ativos; GUI carregada | `nohup.out` (ambos) + `p3_interface_inicial.png` | 2 min |
| **P4** | Sim (`README.md:88-90`) | F (Teste Mínimo 4–5), C1, C4 | Interface Web (`:5173`) | Arrastar `Controller` (`Default` -> `Submit`); `Generate Topology` (`Single`, `c1`, `Hosts=2` -> `Submit`) | `c1`, `s1`, `h1`, `h2` criados e conectados no grafo | `p4_topologia_single.png` | 2 min |
| **P5** | Sim (`README.md:92`) | F (Teste Mínimo 6), C2 | Interface Web (`:5173`) | Clicar em `"Run Pingall Test"` na barra lateral | Modal `"Pingall Results"` exibe conectividade entre `h1` e `h2` | `p5_pingall_results.png` | 1 min |
| **P6** | Sim (`README.md:94`) | F (Teste Mínimo 7 opc.), C5 | Interface Web (WebShell) | Aba `H1`: `iperf -s`; Aba `H2`: `iperf -c 10.0.0.1` (aguardar 1 min) | Relatório de largura de banda do `iperf` exibido nas abas `H1` e `H2` | `p6_iperf_h1.png`, `p6_iperf_h2.png` | 2 min |
| **P7** | Sim (`README.md:96`) | F (Teste Mínimo 8 opc.), C1, C2, C3, C5 | Interface Web (`:5173` + WebShell) | Criar `Controller` `Remote` (`127.0.0.1:6633`), gerar `Single` (2 hosts, `c2`), ligar `s1`–`s2`, rodar `ryu-manager ...` na aba `C2` e `Run Pingall Test` | Rede expandida com 2 controladores; link verde `s1`–`s2`; `pingall` OK entre `h1`–`h4` | `p7_multi_controlador.png`, `p7_pingall_4hosts.png` | 4 min |
| **P8** | Sim (`README.md:98`) | F (Teste Mínimo 9) | Interface Web (`:5173`) | Clicar em `"Export Topology (JSON)"` e `"Export Mininet Script"` | Download de `network_export.json` e `network_export.py` | `network_export.json`, `network_export.py` | 1 min |
| **P9** | Sim (`README.md:88-91, 96`) + Reset **[NÃO DOCUMENTADO]** | F, R — **C1** | Interface Web (`:5173`) | `Reset Topology`; arrastar `Controller`, `Switch`, `Host`, criar links com `"Create Link"` e mover nós no grafo | Elementos representados no grafo e respondendo às ações | `p9_c1_grafo_interativo.png` | 2 min |
| **P10** | Sim (`README.md:88-92`) | F, R — **C2** | Interface Web (`:5173`) | Com topologia emulada, clicar em `"Run Pingall Test"` | Nós emulados e resultado de `pingall` exibido na interface | `p10_c2_pingall.png` | 1 min |
| **P11** | Adição: Sim (`README.md:96`); Remoção: **[NÃO DOCUMENTADO]** | F, R — **C3** | Interface Web (`:5173`) | Adicionar nó/link com emulação ativa (`Run Pingall Test`) e remover nó/link via `"Delete Selected"` (`Run Pingall Test`) | Rede alterada (adição e remoção) enquanto a emulação continua ativa | `p11_c3_tempo_real_add.png`, `p11_c3_tempo_real_del.png` | 3 min |
| **P12** | Sim (`README.md:90, 105-108`) | R — **C4 (Single)** | Interface Web (`:5173`) | `Reset Topology`; `Generate Topology` -> `Single`, `Hosts=3` -> `Submit` | Topologia `Single` gerada com 1 switch e 3 hosts | `p12_c4_single.png` | 2 min |
| **P13** | Sim (`README.md:105-108`) | R — **C4 (Linear)** | Interface Web (`:5173`) | `Reset Topology`; `Generate Topology` -> `Linear`, `Switches=3`, `Hosts per switch=2` -> `Submit` | Topologia `Linear` gerada com 3 switches em linha e 6 hosts | `p13_c4_linear.png` | 2 min |
| **P14** | Sim (`README.md:105-108`) | R — **C4 (Tree)** | Interface Web (`:5173`) | `Reset Topology`; `Generate Topology` -> `Tree`, `Layers=2`, `Fanout=2` -> `Submit` | Topologia `Tree` gerada com 3 switches em árvore e 4 hosts | `p14_c4_tree.png` | 2 min |
| **P15** | Sim (`README.md:110-114`) | R — **C5 (WebShell)** | Interface Web (WebShell) | Selecionar aba `H1` no WebShell e rodar `ip addr show` e `ping -c 2 10.0.0.2` | Saída dos comandos Bash executados no namespace de `h1` exibida na aba `H1` | `p15_c5_webshell.png` | 2 min |
| **P16** | **[NÃO DOCUMENTADO]** (`reivindicacoes.md:12`) | F, R — **C6 (Flow Rules)** | Interface Web (`:5173`) | Duplo clique no switch `s1` -> aba `"Flow Table"`; procurar controles de inserção/remoção de regras | Tabela de fluxos exibida (somente leitura); constatação da ausência de criação/remoção na GUI | `p16_c6_flow_table.png` | 2 min |

## Prompt B2

Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que atende parcialmente (VM dos autores no VirtualBox 7.1.6 com 8 GB de RAM, mas sobre o Hyper-V em modo NEM e com o navegador do host em vez de um navegador dentro da VM, como detalhado na seção 1 do registro) aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.

Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.

## Resposta B2

# Avaliação Pós-Execução — Mininet-GUI (SBRC 2025)

## A. Materiais examinados

Além dos 4 arquivos examinados na etapa analítica (`instrucoes-oficiais.md`, `reivindicacoes.md`, `artigo.pdf` e `artefato.txt`), foi examinado integralmente o arquivo anexado:
- `runs/mininet-gui/execucao/registro-factual.md` (linhas 1–157)

---

## 1. Confronto dos Passos Executados com a Avaliação Analítica

Abaixo, cada passo relevante do `registro-factual.md` (Tabelas 2 e 3, passos `E01` a `E32`) é confrontado com a avaliação analítica anterior. Os passos marcados como `D2` (`[NÃO DOCUMENTADO]`) são tratados exclusivamente como **evidência complementar**, e não como reprodução direta das reivindicações documentadas pelos autores.

### 1.1 Ambiente, Instalação e Pré-condições (`E01`–`E08`)

- **`E01`, `E04`, `E05` (Host, importação da OVA no VirtualBox 7.1.6 r167084 e ajuste para 8192 MB RAM / 2 vCPUs — `D2`/`D0`)**: **Confirma** a avaliação analítica quanto à adequação das instruções de importação da VM (`[registro-factual.md:19, 30, 75, 99, 101]`). Revela como detalhe complementar (`E05`, `D2`) que a OVA vinha pré-configurada com 1536 MB de RAM e 1 vCPU, exigindo ajuste manual para atender aos 8 GB recomendados em `README.md:38` (embora o pico real de uso tenha sido de apenas 257 MB, confirmando os 2 GB mínimos de `README.md:103`). A execução sobre Hyper-V em modo NEM (`[registro-factual.md:20]`) não impediu o funcionamento.
- **`E02`, `E03` (Obtenção da VM — `D1`/`D2`)**: **Confirma** o risco apontado na Seção D (item 5) da avaliação analítica sobre a dependência de link externo no [REMOVIDO] Drive: o link em `README.md:53` estava inativo (`"O arquivo que você solicitou não existe"`, `[registro-factual.md:27, 74, 138]`). Contudo, a imagem oficial `Mininet-GUI-VM-SBRC-2025.ova` estava disponível e íntegra na seção *Releases* (`v0.0.1`) do próprio repositório GitHub dos autores (`D1`), viabilizando a execução.
- **`E06`, `E10` (Boot da VM sem interface gráfica, login via SSH `mininet`/`mininet` e acesso pelo navegador do host — `D1`)**: **Confirma parcialmente / refina** a avaliação analítica (`[registro-factual.md:32, 55-56, 76, 78, 139]`). Enquanto `README.md:55, 86` mencionava `Mininet-GUI-Desktop-VM-SBRC-2025.ova` e abertura da URL em navegador *dentro da VM*, a VM disponibilizada na release `v0.0.1` não possui ambiente gráfico (inicia em `tty1`), devendo ser acessada pelo navegador do host via rede host-only (`http://192.168.56.101:5173`), exatamente como descrito nas notas da própria release `v0.0.1`.
- **`E07` (Inspeção do commit na VM — `D2`, evidência complementar)**: **Não altera** a avaliação analítica do código (`[registro-factual.md:35, 39-44, 102]`). Embora a VM esteja no commit `be68302` (16 commits antes de `465648a4`), **nenhum arquivo** de `mininet-gui-backend/` ou `mininet-gui-frontend/` difere entre os dois commits.
- **`E08` (Inspeção de `api.js:299` e do `nvm` sem correção — `D2`, evidência complementar)**: **Confirma** o achado estático (a linha 299 de `mininet-gui-frontend/src/core/api.js` de fato contém `}i`), mas **contradiz** a previsão analítica de que esse caractere impediria a compilação do frontend (`[registro-factual.md:44, 103]`). Mesmo sem editar `api.js`, o Vite (`v4.5.9`) compilou e serviu a aplicação normalmente (pois, após o bloco `catch { ... return false; }`, a sequência `}i\n};` é interpretada pelo parser JS/esbuild como o fim do `try/catch` seguido de uma instrução de expressão `i` inalcançável antes do `};` que encerra `requestRunPingall`). Também confirma que na VM o `~/.bashrc` já carrega o `nvm` em sessão interativa.

### 1.2 Inicialização e Teste Mínimo — Selo F (`E09`–`E17`)

- **`E09`, `E10` (Execução de `mininet_gui` e abertura da interface web — `D0`/`D1`)**: **Confirma** a avaliação analítica de que o script inicializa o backend (`uvicorn` na porta 8000) e o frontend (`vite` na porta 5173) e imprime a URL de acesso, carregando a SPA com barra lateral, área de grafo e WebShell (`[registro-factual.md:77-78]`).
- **`E11` (Passo 4 do Teste Mínimo: criar Controller Default `c1` — `D0`)**: **Confirma** a avaliação analítica (Selo F e reivindicação C1). O modal abriu, criou `c1` no grafo e a aba `C1` no WebShell (`[registro-factual.md:79]`).
- **`E12` (Passo 5 do Teste Mínimo: Generate Topology `Single`, `c1`, 2 hosts — `D0`)**: **Confirma** a avaliação analítica (Selo F e reivindicações C1, C2 e C4-Single). Criou `s1`, `h1`, `h2`, links verdes `s1–h1` e `s1–h2` e associação tracejada `s1–c1` com a rede iniciada (`[registro-factual.md:80]`).
- **`E13` (Passo 6 do Teste Mínimo: Run Pingall Test — `D0`)**: **Confirma** a avaliação analítica (Selo F e reivindicação C2). Em menos de 2 s, exibiu o modal "Pingall Results" com 100% de entrega (`1/1`) entre `h1→h2` e `h2→h1` (`[registro-factual.md:81]`).
- **`E14` (Passo 7 opcional do Teste Mínimo: teste `iperf` entre `h1` e `h2` no WebShell — `D0`)**: **Confirma** a avaliação analítica (Selo F e reivindicação C5). O servidor `iperf -s` em `h1` e o cliente `iperf -c 10.0.0.1` em `h2` comunicaram-se pelo WebShell, medindo `6.62 Gbits/sec` (`[registro-factual.md:82]`).
- **`E16` (Passo 8 opcional do Teste Mínimo: segundo controlador Remote `127.0.0.1:6633`, segunda topologia Single, link `s1–s2`, `ryu-manager` e Pingall — `D0`/`D1`) e `E15` (`D2`)**: **Contradiz parcialmente** a expectativa de funcionamento integral do Passo 8 opcional (`[registro-factual.md:33, 83, 104, 137]`). A parte interna ao Mininet-GUI funcionou (criou `c2`, gerou `s2`, `h3`, `h4` — que nasceram sobrepostos às coordenadas de `s1`, `h1`, `h2` e precisaram ser afastados manualmente, `D1` — e criou o link verde `s1–s2` em tempo real). Porém, o pacote opcional `ryu` (`ryu-manager`) **não está instalado na VM** (o `README.md:75-78` só instrui `pip3 install ryu...` na seção de instalação manual, e a VM opera sem Internet). Sem o controlador Ryu na porta 6633, `s2` não encaminhou pacotes e o Pingall teve sucesso apenas entre `h1↔h2`.
- **`E17` (Passo 9 do Teste Mínimo: Export Topology JSON e Export Mininet Script — `D0`)**: **Confirma** a avaliação analítica (Selo F). Os arquivos `network_export.json` (2514 bytes) e `network_export.py` (1105 bytes, sintaxe Python válida) foram exportados corretamente (`[registro-factual.md:84]`).

### 1.3 Experimentos e Reivindicações — Selo R (`E18`–`E32`)

- **`E19`, `E20`, `E21`, `E22` (Geração automatizada de topologias `Single`, `Linear` e `Tree` — `D0` com valores `D2`) e `E18`, `E23` (Reset e contagem via API — `D2`, evidência complementar)**: **Confirma** integralmente a avaliação analítica da reivindicação **C4** (`[registro-factual.md:85-88, 105-106, 129]`). Os três modelos (`Single` com 3 hosts; `Linear` com 3×2 e 2×1; `Tree` com 2 camadas e fanout 2) geraram no grafo e no Mininet exatamente a quantidade de switches, hosts e links escolhida.
- **`E24` (Comando `ip addr show` na aba `h1` do WebShell — `D0` com comando `D2`) e `E25`, `E26`, `E27` (Verificação em `h2`, `ping` e namespaces `/proc/$$/ns/net` — `D2`, evidência complementar)**: **Confirma** integralmente a avaliação analítica da reivindicação **C5** (`[registro-factual.md:89, 107-109, 130]`). A saída do comando Bash executado no namespace do nó (`h1-eth0@if40` com IP `10.0.0.1/8` e MAC `00:00:00:00:00:01`) foi exibida na aba `H1`, e a evidência complementar `E27` (`D2`) comprovou que cada aba opera no `netns` exclusivo do processo Mininet daquele nó.
- **`E28a`, `E28b`, `E29` (Persistência de posição após arraste, criação via paleta e Pingall 20/20 com 5 hosts — `D2`, evidência complementar)**: **Confirma** como evidência complementar o funcionamento de **C1**, **C2** e da **adição em tempo real de C3** (`[registro-factual.md:110-112]`).
- **`E30a`, `E30b`, `E30c`, `E30d` (Remoção de link e de nó com a emulação em andamento — `D2`, evidência complementar)**: **Confirma com ressalva importante (bug revelado na execução)** a análise de **C3** (`[registro-factual.md:113-116, 128]`). Por um lado, a remoção do link `h2–s1` (`E30a`) e do nó `h4` (`E30b`) alterou a rede sem reiniciar a emulação (`E30d`: `start=true`, sem novo `"Creating network"` no log e com `h1` mantendo conectividade ICMP com `h3`). Por outro lado, `delete_node` em `api.py:299-316` não remove de `app.links` os links associados ao nó excluído (`['h4','s2']` permaneceu em `/links`) e deixa referências que fazem `app.net.pingFull()` (`api.py:157`) lançar `AttributeError: 'NoneType' object has no attribute 'IP'`, resultando em erro **HTTP 500** ao clicar em "Run Pingall Test" após remover um nó (`E30c`). Além disso, como a remoção não era documentada no README (sendo `E30a–E30d` passos `D2` complementares) e o único passo documentado pelos autores relacionado a C3 (`E16`) falhou por ausência do Ryu na VM, **C3** não se sustenta pelos passos documentados pelos autores.
- **`E31`, `E32` (Visualização da tabela de fluxos de `s1` e busca por controles de inserção/remoção de regras — `D2`, evidência complementar)**: **Confirma** integralmente a avaliação analítica da reivindicação **C6** (`[registro-factual.md:117-118, 131]`). O duplo clique em `s1` (`E31`, não documentado no README) exibe a aba "Flow Table" com 5 regras OpenFlow instaladas após o Pingall, mas `E32` confirma que **não existe nenhum controle na interface para criar/inserir ou remover regras de fluxo**, ratificando que C6 é `nao_reproduzivel`.

---

## B. Selo F (Decisão Pós-Execução)

1. **Avaliação dos critérios com base no registro factual**:
   - **Documentação (dependências, ambiente, instalação, execução e teste mínimo)**: Atendido na documentação (`[README.md:26-99]`), com as ressalvas observadas em execução de que o link do [REMOVIDO] Drive estava inativo (`E02`, contornado pela OVA oficial da release `v0.0.1` do próprio repositório), a VM da release não possui interface gráfica (`E06`/`E10`, acessada via SSH e navegador do host conforme instruções da release) e o pacote opcional `ryu` não veio pré-instalado na VM (`E15`/`E16`).
   - **Execução e observação de funcionalidades (`[instrucoes-oficiais.md:15]`)**: **Atendido na execução**. O artefato foi executado com sucesso (`E09`–`E14`, `E17`, `E19`–`E24`), permitindo observar na prática a inicialização integrada do Mininet e da interface web (`E09`–`E10`), criação de controladores (`E11`), geração de topologias (`E12`, `E19`–`E22`), teste de conectividade `pingall` (`E13`), execução de comandos e teste de vazão `iperf` no WebShell (`E14`, `E24`) e exportação da topologia para JSON e script Python (`E17`).
2. **Decisão**: **Atribuir** (`"mudou": true`, alterada de `Indeterminado` para `Atribuir`).
3. **Confiança (0 a 100)**: **95** (subiu de 85 para 95).
   - **Explicação da mudança**: Na fase analítica, a decisão era `Indeterminado` exclusivamente porque o critério oficial do Selo F exige a observação prática do artefato em execução (`[instrucoes-oficiais.md:15]`) e havia dúvida sobre o efeito do erro de digitação `}i` em `api.js:299`. O registro factual comprovou que o frontend compila e funciona sem necessidade de edição (`E08`–`E10`) e que todos os passos obrigatórios do Teste Mínimo (Passos 1–6 e 9) e o Passo 7 opcional funcionaram conforme descrito pelos autores.

---

## C. Selo R — Por Reivindicação (Decisão Pós-Execução)

Conforme a regra explícita de `[reivindicacoes.md:16-20]`:
> "Na seção 'Experimentos', o README marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R."

Avaliação de cada reivindicação após a execução (tratando `D2` apenas como evidência complementar):

- **C1 (Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo)**: **`reproduzivel`** (mudou de `depende_execucao`).
  - Pelos passos documentados pelos autores (`E10`–`E12`, `E16` — `D0`/`D1`), controladores, switches, hosts e links criados na interface foram representados no grafo interativo e responderam às ações do usuário (`[registro-factual.md:78-80, 83, 126]`). Como evidência complementar (`E28a`–`E28b`, `D2`), confirmou-se também a persistência de coordenadas após arraste e a criação direta via paleta.
- **C2 (Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade)**: **`reproduzivel`** (mudou de `depende_execucao`).
  - Pelos passos documentados pelos autores (`E12`–`E13` — `D0`), a emulação Mininet foi iniciada pela ferramenta e o resultado de `pingall` foi exibido na interface com conectividade entre `h1` e `h2` (`[registro-factual.md:80-81, 127]`), corroborado pela evidência complementar `E29` (`D2`, 20/20 pares com 5 hosts).
- **C3 (Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la)**: **`nao_reproduzivel`** (mudou de `depende_execucao`).
  - O único procedimento documentado pelos autores no README relacionado a C3 (`E16`, Passo 8 opcional) cobre apenas **adição** (não documenta remoção de nós/links) e teve status de **falha** na execução porque o `ryu-manager` não está instalado na VM, impedindo a conectividade entre as duas subtopologias (`[registro-factual.md:83, 128]`). Nos passos de evidência complementar (`E28b`, `E29`, `E30a`–`E30d` — `D2`, que não contam como reprodução pelos passos dos autores), embora a adição (`E28b`/`E29`) e a remoção no Mininet sem reinício (`E30a`/`E30b`/`E30d`) tenham alterado a rede com a emulação ativa, a remoção de um nó (`E30b`) deixou link órfão em `/links` e quebrou o `Run Pingall Test` da interface com erro HTTP 500 (`E30c`). Assim, C3 é classificada como `nao_reproduzivel` (não afetando a decisão do selo R conforme `[reivindicacoes.md:16]`).
- **C4 (Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido)** *(Obrigatória para R)*: **`reproduzivel`** (mudou de `depende_execucao`).
  - Pelos passos documentados pelos autores em `README.md:90, 105-108` (`E12`, `E19`, `E20`, `E21`, `E22` — `D0`), foram geradas com sucesso topologias nos **três modelos** exigidos: `Single` (2 e 3 hosts), `Linear` (3 switches × 2 hosts e 2 switches × 1 host) e `Tree` (2 camadas × fanout 2), todas com o número de dispositivos escolhido (`[registro-factual.md:80, 85-88, 129]`), o que também foi corroborado pela evidência complementar da API (`E18`, `E23` — `D2`).
- **C5 (Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado)** *(Obrigatória para R)*: **`reproduzivel`** (mudou de `depende_execucao`).
  - Pelos passos documentados pelos autores em `README.md:94, 110-114` (`E14` e `E24` — `D0`), comandos Bash executados nas abas dos nós no painel WebShell (`iperf` em `E14` e `ip addr show` na aba `h1` em `E24`) exibiram na respectiva aba a saída produzida dentro do namespace de rede do nó emulado (`h1-eth0@if40` com IP `10.0.0.1/8`, `[registro-factual.md:82, 89, 130]`), corroborado pelas evidências complementares `E25`–`E27` (`D2`).
- **C6 (Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches)**: **`nao_reproduzivel`** (mantida da avaliação analítica).
  - Os autores não documentaram procedimento no README (`[reivindicacoes.md:12]`), e os passos complementares (`E31`–`E32` — `D2`) confirmaram que a interface exibe apenas a tabela de fluxos em modo leitura (`E31`), não existindo qualquer controle ou editor para inserir ou remover regras de fluxo OpenFlow (`E32`, `[registro-factual.md:117-118, 131]`). Conforme `[reivindicacoes.md:16]`, C6 não entra na regra de atribuição de R.

### Decisão Final para o Selo R
- **Decisão**: **Atribuir** (`"mudou": true`, alterada de `Indeterminado` para `Atribuir`).
- **Confiança (0 a 100)**: **90** (subiu de 80 para 90).
  - **Explicação da mudança**: Na etapa analítica, R estava `Indeterminado` porque dependia da execução para verificar C4 (nos três modelos) e C5. Como `registro-factual.md` comprovou a reprodução integral de **C4** (`E12`, `E19`–`E22`) e **C5** (`E14`, `E24`) seguindo as instruções da seção `# Experimentos` do README (`[reivindicacoes.md:16]`), todos os requisitos para atribuir R foram atendidos. A confiança é 90 (e não 100) apenas porque contribuições secundárias fora da seção `# Experimentos` (Passo 8 opcional em E16/C3 e edição de regras de fluxo em C6) apresentaram falhas/lacunas que poderiam ser discutidas pelo comitê.

---

```json
{"F": {"decisao": "Atribuir", "confianca": 95, "mudou": true, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:26-99", "registro-factual.md:74-84", "registro-factual.md:103", "registro-factual.md:133"]},
 "R": {"decisao": "Atribuir", "confianca": 90, "mudou": true, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:7-20", "README.md:90-114", "registro-factual.md:79-89", "registro-factual.md:105-118", "registro-factual.md:124-131"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "reproduzivel", "C3": "nao_reproduzivel", "C4": "reproduzivel", "C5": "reproduzivel", "C6": "nao_reproduzivel"}}}
```
