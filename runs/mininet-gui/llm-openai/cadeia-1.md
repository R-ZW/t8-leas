# Cadeia MG-1 — openai

- provedor: openai
- modelo_exibido: GPT 6.1 Sol (informado de memória por Eduardo em 17/10/2026; o link de compartilhamento do Codex não exibe o modelo; a confirmar por Reinaldo)
- versao: não registrado
- esforco: High (informado de memória por Eduardo em 17/10/2026; a confirmar por Reinaldo)
- interface: Codex (agente com workspace local e terminal), operado por Reinaldo Zimmer Wendt; anexos lidos do disco por caminho em `runs/<artefato>/pacote/` (desvio: agente em vez do chat do ChatGPT)
- data_hora_A: não registrado no link (duração do turno: A=158s; B1=181s)
- data_hora_B1: não registrado no link
- data_hora_B2: pendente
- anexos_A: artigo.pdf=4e3ff858506f2f9e6da30af4412caa402890ac154b910df390b74e2ee2a2bf08, artefato.txt=5e1da9b36fe62beddfdb9b8dbbceefa67c1c38e14f45c8bd3247519bcf83c8eb, instrucoes-oficiais.md=fc8e01dd0ffdbff06af86a07bd44662c3394903c0d3a6be0222e678963989059, reivindicacoes.md=100366e5dfad9c560f9d5066e67d1e23df8f6ad7c3d5ce2e62aff02a529ed0bc (lidos do disco; bytes não conferidos dentro da conversa)
- anexo_B2: pendente
- metodo_exportacao: transcrição gerada por `ferramentas/transcrever_codex.py` do JSON público do link https://chatgpt.com/s/cx_6ad24fb33d348191b7241a14752470d3 (cópia bruta em `exportacao-bruta/`); textos de userMessage e agentMessage sem alteração; reasoning, imageView, fileChange e chamadas de ferramenta (não incluídas no link) omitidos. O export anterior, escrito pelo próprio modelo via Session Exporter, está em `exportacao-bruta/` e não é usado na análise
- desvios: resposta A: contém marcações :codex-file-citation da interface, mantidas sem alteração | resposta B1: contém marcações :codex-file-citation da interface, mantidas sem alteração | turno 3 fora do roteiro, omitido da transcrição: "[@Session Exporter](plugin://session-exporter@openai-curated-remote) Export this entire co"

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

Vou examinar os quatro anexos e aplicar os critérios oficiais apenas ao que eles documentam. Como a avaliação é analítica, distinguirei evidência documental de resultados que exigiriam executar o artefato. Usarei a habilidade de PDF para ler o artigo.

O material fixa C4 e C5 como as reivindicações exigidas para R. O README traz passos para ambas; agora vou conferir se o próprio código e os arquivos incluídos sustentam esses passos e se há alguma lacuna obrigatória antes de concluir.

## A. Materiais examinados

Abri os quatro anexos: instrucoes-oficiais.md :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md" purpose="source"}, reivindicacoes.md :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/reivindicacoes.md" purpose="source"}, artefato.txt :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artefato.txt" purpose="source"} e artigo.pdf :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artigo.pdf" purpose="source"}.

O anexo de instruções se declara um **resumo, não uma transcrição literal** da página oficial [instrucoes-oficiais.md:Natureza deste arquivo] “não é transcrição literal”. Apliquei os critérios tal como constam nesse anexo. Não executei o artefato.

## B. Selo F

**Critérios aplicáveis e estado**

- **Relação com o artigo — atendido na documentação.** A revisão deve identificar as principais contribuições e avaliar o artefato em relação a elas [instrucoes-oficiais.md:Contexto de revisão] “lê o artigo e identifica suas principais contribuições”. O artigo enumera seis contribuições [artigo.pdf:p. 2, §1] “As principais contribuições do Mininet-GUI incluem”; o README apresenta a ferramenta e suas funções [README.md:4] “criação, edição e execução de topologias”.
- **Dependências e versões no README — não atendido.** O critério exige [instrucoes-oficiais.md:Funcional (F)] “O README deve informar dependências e versões”. Ele informa a versão do VirtualBox [README.md:37] “7.1.6 r167084”, mas a instalação do Mininet usa um clone sem versão fixada [README.md:65-68] “git clone https://github.com/mininet/mininet”, e as dependências do backend aparecem sem versões [mininet-gui-backend/requirements.txt:1-4] “fastapi”, “websockets”, “uvicorn”, “python-multipart”.
- **Ambiente, instalação, execução e exemplo mínimo — atendido na documentação, com ressalvas.** O critério os exige [instrucoes-oficiais.md:Funcional (F)] “ambiente de execução, instalação, execução e um exemplo mínimo”. Há instruções para VM e instalação manual [README.md:49-73] “Máquina Virtual (recomendado)” e “Instalação manual”; há comando de inicialização e teste de topologia e conectividade [README.md:80-92] “mininet_gui”, “Generate Topology” e “Run Pingall Test”. Os requisitos de RAM da VM, porém, divergem: [README.md:38] “Mínimo de 8GB” e [README.md:103] “no mínimo 2GB”.
- **Execução e observação das funcionalidades — só verificável por execução.** O critério diz [instrucoes-oficiais.md:Funcional (F)] “O código ou artefato deve poder ser executado” e exige que o revisor “consiga observar funcionalidades”. O próprio anexo esclarece [instrucoes-oficiais.md:Funcional (F)] “não apenas a presença das instruções”.

**Decisão: Não atribuir F.** A falta de versões de dependências necessárias deixa um requisito documental obrigatório sem atendimento, independentemente do resultado de uma execução futura. Minha confiança de que o comitê oficial **atribuiu** F é **35/100**; os anexos não contêm a decisão oficial [instrucoes-oficiais.md:Natureza deste arquivo] “não contém ... a decisão oficial deste artefato”.

Para mudar esta decisão, seria preciso documentar as versões necessárias e resolver a divergência de RAM. Na execução, seria preciso observar a instalação e inicialização no ambiente declarado, a criação da topologia na interface e uma funcionalidade efetiva, como o resultado de `pingall`; só o código e o README não demonstram isso.

## C. Selo R — por reivindicação

**Critérios aplicáveis e estado**

- **Escopo das reivindicações — atendido na documentação.** O critério oficial é reproduzir as [instrucoes-oficiais.md:Reprodutível (R)] “principais reivindicações do artigo”. A regra específica anexada fixa **C4 e C5** como necessárias para R [reivindicacoes.md:Regra para o selo R] “R é atribuído se C4 e C5 forem reproduzidas”.
- **Instruções e processo experimental — atendido na documentação para C4 e C5.** O anexo oficial exige [instrucoes-oficiais.md:Reprodutível (R)] “instruções de execução e descrição do processo empregado nos experimentos”. O README descreve os passos de geração e de uso do terminal [README.md:105-114] “Selecione o tipo de topologia (Single, Linear ou Tree)” e “utilize o terminal bash”.
- **Confronto entre resultado e reivindicação — só verificável por execução.** A instrução determina [instrucoes-oficiais.md:Reprodutível (R)] “confronta o resultado observado com a reivindicação correspondente”. Não há resultado observado nesta avaliação.

**Avaliação individual.** “Não reproduzível” abaixo indica ausência de um procedimento documental suficiente nesta análise, e não uma falha observada em execução.

- **C1 — depende de execução; fora da regra de R.** O artigo reivindica [artigo.pdf:p. 2, §1] “Interface web dinâmica”; o README manda arrastar um controlador e gerar uma topologia [README.md:88-90] “arraste o ícone” e “Generate Topology”. Falta observar o grafo respondendo às ações.
- **C2 — depende de execução; fora da regra de R.** O README prescreve [README.md:92] “Run Pingall Test” e aguardar os resultados. Falta observar nós emulados e o resultado na interface.
- **C3 — não reproduzível pela documentação disponível; fora da regra de R.** O artigo reivindica [artigo.pdf:p. 2, §1] “modificações na topologia em tempo real”. O passo opcional descreve criar controlador e link [README.md:96] “clique no botão ‘Create Link’”, mas não estabelece como verificar que a emulação permaneceu ativa, sem reinício, durante criação e remoção.
- **C4 — depende de execução; necessária para R.** O procedimento manda escolher Single, Linear ou Tree e parâmetros de dispositivos [README.md:105-108] “Selecione o tipo de topologia ... e o número de dispositivos”. A interface apresenta os três modelos e seus campos [mininet-gui-frontend/src/components/TopologyForm.vue:5-40] “Single”, “Linear”, “Tree”; o código contém as três rotinas de geração [mininet-gui-frontend/src/components/NetworkGraph.vue:512-615] “createSingleTopo”, “createLinearTopo”, “createTreeTopo”. Isso sustenta a existência do caminho de reprodução, sem provar seu resultado. Seria preciso observar **cada um dos três modelos**, com nós e ligações correspondentes aos parâmetros escolhidos [reivindicacoes.md:Critério de reprodução] “Em C4, nos três modelos”.
- **C5 — depende de execução; necessária para R.** O README manda criar um nó, selecionar sua aba e executar comandos [README.md:110-114] “terminal bash ... no namespace daquele nó”; o teste mínimo oferece comandos `iperf` [README.md:94] “iperf -s” e “iperf -c 10.0.0.1”. O backend abre `bash` por meio do nó e envia a saída pelo WebSocket [mininet-gui-backend/mininet_gui_backend/api.py:462-486] `node.popen(["/bin/bash", "-i"])`; o frontend recebe dados na aba [mininet-gui-frontend/src/components/Webshell.vue:68-111] “handleTerminalData”. Seria preciso observar a saída do comando na aba do nó selecionado e confirmar que veio de seu namespace.
- **C6 — não reproduzível pela documentação disponível; fora da regra de R.** O artigo descreve o editor [artigo.pdf:p. 6, §3] “visualização, criação e remoção de regras de fluxo”. A seção completa de experimentos do README só instrui C4 e C5 [README.md:101-114] “Geração automatizada” e “Terminal integrado”; não fornece procedimento para inserir, verificar e remover uma regra.

**Decisão: Indeterminado para R.** C4 e C5 têm procedimentos documentados, mas ambas dependem do resultado observado. Minha confiança de que o comitê oficial **atribuiu** R é **55/100**. A decisão mudaria para **Atribuir** se a execução reproduzisse C4 nos três modelos e C5 no namespace do nó; mudaria para **Não atribuir** se uma dessas duas reivindicações falhasse.

## D. Lacunas e riscos

O arquivo único contém o índice e o texto do código, mas **não inclui a imagem `.ova`** indicada para o caminho recomendado [artefato.txt:ÍNDICE] “Conteúdo: todos os arquivos do commit”; [README.md:53-55] “Baixe o arquivo ova neste link”. A disponibilidade e o funcionamento dessa VM são evidência ausente, pois o link não foi consultado. Também não há registro de instalação, execução ou resultados observados nos anexos. As versões não fixadas e a divergência de RAM afetam a avaliação de F; para R, as lacunas decisivas são as observações de C4 e C5.

```json
{"F": {"decisao": "Não atribuir", "confianca": 35, "evidencias": ["instrucoes-oficiais.md:Funcional (F)", "README.md:35-38", "README.md:65-73", "README.md:80-92", "mininet-gui-backend/requirements.txt:1-4"]},
 "R": {"decisao": "Indeterminado", "confianca": 55, "evidencias": ["instrucoes-oficiais.md:Reprodutível (R)", "reivindicacoes.md:Regra para o selo R", "README.md:105-114", "mininet-gui-frontend/src/components/NetworkGraph.vue:512-615", "mininet-gui-backend/mininet_gui_backend/api.py:462-486"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "nao_reproduzivel", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

Vou montar o roteiro a partir do README e dos scripts incluídos, marcando separadamente as ações de registro e verificação que os autores não especificaram. Também vou explicitar quais reivindicações entram na decisão de R: o anexo fixa C4 e C5.

# Roteiro de execução e verificação de F e R

Este roteiro usa somente os procedimentos descritos nos quatro anexos: :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md" purpose="source"}, :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/reivindicacoes.md" purpose="source"}, :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artefato.txt" purpose="source"} e :codex-file-citation{path="C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artigo.pdf" purpose="source"}. **Nada foi executado por mim.**

`[NÃO DOCUMENTADO]` marca uma ação ou escolha que os autores não prescreveram; a justificativa aparece no próprio passo. Salvar capturas e saídas também é **[NÃO DOCUMENTADO]** pelos autores: é necessário para fundamentar sua revisão. Um resultado esperado descreve o que deve ser procurado, não algo já observado.

## Ambiente e limites do roteiro

- **Máquina usada na demonstração pelos autores:** Intel i5-10300H, 8 GB de RAM, Windows 11 de 64 bits e pelo menos 80 GB livres [README.md:26-32]. Isso descreve a demonstração; o README não declara que seja a configuração mínima do host.
- **Caminho recomendado:** Oracle VirtualBox **7.1.6 r167084** e a imagem `Mininet-GUI-Desktop-VM-SBRC-2025.ova`, indicada por um link no README [README.md:37, 49-57]. A imagem **não consta no índice do artefato anexado** [artefato.txt:ÍNDICE]; sua obtenção é uma condição para este caminho.
- **Recursos da VM:** o README diz “mínimo de 8GB” [README.md:38] e, na seção Experimentos, “no mínimo 2GB de RAM e um core de CPU” [README.md:103]. Registre essa divergência; os autores não a resolvem.
- **Alternativa documentada:** instalação manual testada no Ubuntu 20.04 [README.md:60-73]. Ela clona repositórios sem fixar uma revisão. Por isso, este roteiro usa a VM recomendada e inclui uma conferência **[NÃO DOCUMENTADO]** da versão antes de associar os resultados ao commit `465648a4425a4457af0348ab951cf7f71d37a86f`.
- O script de inicialização seleciona Node **18.20.7** [run.sh:20]. As versões do Mininet e das dependências Python não estão fixadas [README.md:65-68; mininet-gui-backend/requirements.txt:1-4].

## Teste mínimo — F

Siga **P1–P9** na tabela final. Eles cobrem a preparação da VM, inicialização, acesso à interface, criação de controlador e topologia Single com dois hosts, `pingall` e exportações [README.md:80-98]. O `iperf` e o cenário de múltiplos controladores são opcionais no teste mínimo; aparecem abaixo onde ajudam a examinar C5 e C3.

Para concluir F, registre o que de fato abriu e respondeu na interface. Uma tela ou instrução presente no README, isoladamente, não comprova funcionalidade [instrucoes-oficiais.md:Funcional (F)].

## Reivindicações C1–C6

A regra anexada exige **C4 e C5 para R**. C1, C2, C3 e C6 podem informar a avaliação funcional, mas não determinam R [reivindicacoes.md:Regra para o selo R].

### C1 — Grafo interativo

Use **P5–P7**. Procure o controlador e a topologia criada representados no grafo, respondendo às ações descritas no teste mínimo [README.md:88-90; reivindicacoes.md:C1]. O README fornece essas ações; não fornece uma medida adicional de interatividade.

### C2 — Emulação integrada e conectividade

Use **P7–P8**. Procure os nós criados e o resultado de `pingall` na interface [README.md:90-92; reivindicacoes.md:C2]. Não interprete a simples presença do botão como emulação bem-sucedida.

### C3 — Alteração sem reinício

Use **P15** para a criação de outro controlador, topologia e link, conforme o passo opcional dos autores [README.md:96]. **P16 é [NÃO DOCUMENTADO]**: falta um procedimento dos autores para remover nós e links e comprovar que a emulação continuou ativa sem reinício. P15, sozinho, não verifica toda a reivindicação [reivindicacoes.md:C3].

### C4 — Single, Linear e Tree — necessária para R

O **Single** é testado em **P7**, com dois hosts fixados pelos autores [README.md:90]. Use **P10–P11** para **Linear** e **Tree**, conforme a seção Experimentos [README.md:105-108]. O formulário apresenta “Switches” e “Hosts per switch” para Linear, e “Layers” e “Fanout” para Tree [mininet-gui-frontend/src/components/TopologyForm.vue:23-40]. Os valores concretos de P10–P11 são **[NÃO DOCUMENTADO]**; são escolhas de teste necessárias para comparar a topologia exibida com as entradas. Registre o estado do grafo antes e depois de cada geração, pois os autores não prescrevem reiniciar a topologia entre modelos. C4 só passa se os **três modelos** produzirem a configuração escolhida [reivindicacoes.md:Critério de reprodução].

### C5 — WebShell no namespace do nó — necessária para R

Use **P12–P13**, que repetem os comandos `iperf` do teste opcional dos autores, nas abas `h1` e `h2` [README.md:94]. A seção Experimentos manda selecionar a aba de um nó e executar comandos Bash em seu namespace [README.md:110-114]. **P14 é [NÃO DOCUMENTADO]**: a conferência adicional do endereço da interface é necessária se você quiser evidência direta de que a aba corresponde ao nó, além de observar a saída do `iperf`. A saída deve aparecer na aba do nó selecionado [reivindicacoes.md:C5].

### C6 — Regras de fluxo

**P17 é [NÃO DOCUMENTADO].** O artigo reivindica visualização, criação e remoção de regras [artigo.pdf:p. 6, §3], mas o README não dá uma sequência de interface, comando, regra de exemplo ou resultado para esse teste [README.md:101-114; reivindicacoes.md:C6]. Não improvise uma regra e a apresente como procedimento dos autores. Registre C6 como sem verificação por este roteiro; ela não entra na regra de R.

## Tempo estimado

**[NÃO DOCUMENTADO] Estimativa para planejamento:** reserve **30–60 minutos após a VM estar importada** para P3–P15, dependendo da resposta da interface e dos testes. A estimativa não vem dos autores nem de uma execução minha. Eles especificam apenas **1 minuto** de espera para o teste `iperf` [README.md:94]. O tempo para obter/importar a VM não é estimável pelos anexos. P16–P17 ficam sem duração de execução porque faltam procedimentos dos autores.

## Tabela de todos os passos

“Falha” significa resultado contrário ao esperado. “Interromper” indica quando não há base para prosseguir ou para atribuir o resultado à versão avaliada.

| ID | Selo / reivindicação | Diretório | Comando exato ou ação | Resultado esperado segundo os autores | Evidência a salvar | Sucesso | Falha | Interromper se |
|---|---|---|---|---|---|---|---|---|
| **P1** | F/R; ambiente | Host e configuração da VM | **[NÃO DOCUMENTADO]** Conferir hardware, VirtualBox 7.1.6 r167084 e recursos da VM. Necessário para saber se o ambiente satisfaz os requisitos declarados; os autores não dão comando de checagem. | Ambiente capaz de iniciar a VM [README.md:26-38, 103]. | **[NÃO DOCUMENTADO]** Registro da configuração e da divergência de RAM. | Pré-requisitos identificados e VM iniciável. | Requisito conhecido não atendido. | A VM não puder iniciar ou não houver recursos para o teste. |
| **P2** | F/R; instalação | Host; local do download não informado | Sem comando de shell: obter a `.ova` no link de [README.md:53], abrir `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no VirtualBox, iniciar e entrar com usuário `mininet`, senha `mininet` [README.md:53-57]. | VM importada e sessão aberta. | **[NÃO DOCUMENTADO]** Captura da importação e da sessão. | Login na VM. | Importação ou login falha. | `.ova` indisponível; ela não está no anexo. |
| **P3** | F/R; versão | `/home/mininet/mininet-gui`, dentro da VM | **[NÃO DOCUMENTADO]** `git rev-parse HEAD`. Necessário para vincular a VM ao commit `465648a4425a4457af0348ab951cf7f71d37a86f`; o README não ensina essa conferência. | Os autores não declaram o commit presente na VM. | **[NÃO DOCUMENTADO]** Saída integral ou erro do comando. | Saída igual ao commit avaliado. | Saída diferente. | Não houver repositório Git ou outra evidência da versão: não atribua resultados à versão anexada. |
| **P4** | F; início | Terminal da VM; diretório de chamada não fixado | `mininet_gui` **ou** `/home/mininet/mininet-gui/run.sh` [README.md:84]. | URL impressa no terminal, como `http://10.0.2.15:5173` [README.md:86]. | **[NÃO DOCUMENTADO]** Saída do terminal. | URL apresentada. | Comando encerra com erro ou não apresenta URL. | Inicialização não ocorrer. |
| **P5** | F; C1 | Navegador dentro da VM | Sem shell: abrir **a URL impressa em P4**, não presumir que o IP de exemplo seja o seu [README.md:86]. | Interface web acessível. | **[NÃO DOCUMENTADO]** Captura da página. | Interface carrega e aceita ações. | Página indisponível ou sem controles. | Não for possível acessar a interface. |
| **P6** | F; C1 | Interface web | Arrastar **Controller** ao centro; escolher **Default**; clicar **Submit** [README.md:88]. | Controlador criado no grafo. | **[NÃO DOCUMENTADO]** Captura antes/depois. | Controlador aparece e responde à ação. | Não aparece ou a ação produz erro. | A criação do controlador falhar; P7 depende de `c1`. |
| **P7** | F; C1, C2, C4/Single | Interface web | **Generate Topology** → **Topology Type: Single** → **Controller: c1** → **Hosts: 2** → **Submit** [README.md:90]. | Topologia Single com os dispositivos escolhidos. | **[NÃO DOCUMENTADO]** Captura do formulário e grafo após envio. | Controlador, switch, dois hosts e ligações correspondentes aparecem. | Configuração gerada diverge da entrada ou nada é criado. | Não houver topologia para testar. |
| **P8** | F; C2 | Interface web | Clicar **Run Pingall Test** e aguardar [README.md:92]. | Resultados de `pingall` exibidos. | **[NÃO DOCUMENTADO]** Captura ou texto integral do resultado. | Resultado aparece e permite avaliar conectividade. | Erro ou ausência de resultado. | A emulação não responder; não conclua C2 nem avance para testes que dependem dela. |
| **P9** | F; exportação do teste mínimo | Interface web; destino dos arquivos não informado | Clicar **Export Topology (JSON)** e **Export Mininet Script** [README.md:98]. | Arquivos JSON e script Python da topologia atual. | **[NÃO DOCUMENTADO]** Guardar os dois arquivos ou registrar o erro. | Ambos são produzidos. | Um arquivo não é produzido. | A interface travar; registre a falha antes de prosseguir. |
| **P10** | R; C4/Linear | Interface web | **Generate Topology** → **Linear** → **Switches: 2**, **Hosts per switch: 1** → enviar. **[NÃO DOCUMENTADO]** Esses números são parâmetros de teste escolhidos para tornar a comparação verificável; os autores não fixam valores [README.md:107-108; TopologyForm.vue:23-31]. | Topologia Linear gerada conforme os parâmetros escolhidos. | **[NÃO DOCUMENTADO]** Capturas do formulário e do grafo antes/depois. | Elementos acrescentados correspondem à configuração escolhida. | Modelo ou quantidades divergem. | A geração produzir erro; marque C4 como falha e registre. |
| **P11** | R; C4/Tree | Interface web | **Generate Topology** → **Tree** → **Layers: 2**, **Fanout: 2** → enviar. **[NÃO DOCUMENTADO]** Valores escolhidos para permitir comparação; os autores não fixam valores [README.md:107-108; TopologyForm.vue:33-40]. | Topologia Tree gerada conforme os parâmetros escolhidos. | **[NÃO DOCUMENTADO]** Capturas do formulário e do grafo antes/depois. | Estrutura em árvore corresponde às entradas. | Estrutura diverge ou não aparece. | A geração produzir erro; C4 exige também este modelo. |
| **P12** | R; C5 | Aba WebShell de `h1` | `iperf -s` [README.md:94]. | Servidor `iperf` iniciado no terminal do nó. | **[NÃO DOCUMENTADO]** Captura da aba `h1` e saída. | Aba aceita o comando e mostra sua resposta. | Comando não executa ou saída aparece em outra aba. | `iperf` não estiver disponível; não há substituto prescrito pelos autores para este teste. |
| **P13** | R; C5 | Aba WebShell de `h2` | `iperf -c 10.0.0.1`; aguardar **1 minuto** [README.md:94]. | Saída do teste no terminal do nó. | **[NÃO DOCUMENTADO]** Captura da aba `h2` e saída completa. | Comando produz saída na aba `h2`, permitindo confrontar C5. | Sem saída, erro de terminal ou saída atribuída a outro nó. | Não houver sessão WebShell funcional. |
| **P14** | R; C5; confirmação adicional | Aba WebShell do nó selecionado | **[NÃO DOCUMENTADO]** `ip addr`. Necessário para procurar uma interface/endereço do nó e fortalecer a verificação do namespace; os autores não prescrevem este comando nem um valor esperado. | Apenas a reivindicação geral de executar Bash no namespace [README.md:112-114]. | **[NÃO DOCUMENTADO]** Aba selecionada e saída integral. | Saída permite identificar o nó selecionado. | Saída contradiz a identidade do nó. | O comando não estiver disponível: registre a lacuna; não trate sua ausência, sozinha, como falha do `iperf`. |
| **P15** | F; C3, complementar e opcional | Interface web e aba WebShell de `c2` | Seguir [README.md:96]: criar **Controller / Remote / 127.0.0.1 / 6633**; gerar **Single / 2 hosts / c2**; **Create Link** de `s1` a `s2`; em `c2`, `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; depois **Run Pingall Test**. | Linha verde entre switches e teste de conexão [README.md:96]. | **[NÃO DOCUMENTADO]** Capturas antes/depois, saída do Ryu e `pingall`. | Novos elementos e link aparecem; resultados são exibidos. | Elementos/link/comando/teste falham. | Ryu não estiver disponível ou a emulação deixar de responder; este passo não prova, sozinho, ausência de reinício. |
| **P16** | F; C3, verificação completa | Não especificado | **[NÃO DOCUMENTADO]** Os autores não fornecem sequência para remover nó e link nem método para demonstrar continuidade sem reinício. O passo seria necessário para a reivindicação completa [reivindicacoes.md:C3]. **Não há comando exato a executar neste roteiro.** | Rede alterada enquanto a emulação permanece ativa [reivindicacoes.md:C3]. | Registrar que o procedimento está ausente. | Não julgável pelo roteiro dos autores. | Não julgável sem executar um procedimento adicional definido. | Aqui: não declare C3 integralmente verificada com P15. |
| **P17** | F; C6, verificação completa | Não especificado | **[NÃO DOCUMENTADO]** Não há comando, regra OpenFlow de exemplo ou sequência de interface para consultar, criar e remover regra [README.md:101-114; reivindicacoes.md:C6]. **Não há comando exato a executar neste roteiro.** | Tabela exibida e regra inserida/removida [reivindicacoes.md:C6]. | Registrar a ausência do procedimento. | Não julgável pelo roteiro dos autores. | Não julgável sem procedimento adicional definido. | Aqui: não declare C6 verificada. |
