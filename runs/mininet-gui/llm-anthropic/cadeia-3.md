# Cadeia MG-3 — anthropic

- provedor: anthropic
- modelo_exibido: Opus 5.5 Médio
- versao: claude-opus-5-5 (campo model da API do claude.ai)
- esforco: effort_level=medium; thinking_mode=auto
- interface: claude.ai (web) no Google Chrome, operado pelo agente Claude Code pela extensão Claude in Chrome com autorização do aluno; chat avulso com anexos; memória pausada; busca na web indisponível
- data_hora_A: 2026-10-16 00:23 BRT
- data_hora_B1: 2026-10-16 00:26 BRT
- data_hora_B2: 2026-10-17 22:59 BRT
- anexos_A: artigo.pdf=4e3ff858506f2f9e6da30af4412caa402890ac154b910df390b74e2ee2a2bf08, artefato.txt=5e1da9b36fe62beddfdb9b8dbbceefa67c1c38e14f45c8bd3247519bcf83c8eb, instrucoes-oficiais.md=fc8e01dd0ffdbff06af86a07bd44662c3394903c0d3a6be0222e678963989059, reivindicacoes.md=100366e5dfad9c560f9d5066e67d1e23df8f6ad7c3d5ce2e62aff02a529ed0bc
- anexo_B2: registro-factual.md=0efda099a39c28b4
- metodo_exportacao: transcrição gerada da API do claude.ai (conversa 54ea4ed0-f2a2-47b8-9732-8b34e3ddfec2, https://claude.ai/chat/54ea4ed0-f2a2-47b8-9732-8b34e3ddfec2); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos; o original permanece na conta
- desvios: resposta A usou 9 chamada(s) de ferramenta do claude.ai: view ("Ler skill de leitura de arquivos antes de abrir o artefato"); bash_tool ("Inspecionar tamanho e início do artefato"); bash_tool ("Ler resto do README e localizar arquivos"); bash_tool ("Ler backend api.py e cli.py"); bash_tool ("Ler requirements, package.json, TopologyForm, run.sh, setup.sh"); bash_tool ("Buscar geração de topologia e regras de fluxo"); bash_tool ("Ler geração de topologias em NetworkGraph.vue"); bash_tool ("Ler Webshell.vue e conexão websocket"); bash_tool ("Verificar endpoints usados pelo frontend e exemplo de exportação") | resposta A contém raciocínio (thinking) exibido pela interface, omitido nesta transcrição | resposta B1 usou 14 chamada(s) de ferramenta do claude.ai: view ("Ler a skill de docs antes de criar o roteiro"); Claude Docs:guide (""); Claude Docs:batch (""); Artifact (""); Claude Docs:guide (""); bash_tool ("Localizar gatilhos da interface (estatísticas, botões)"); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update ("") | resposta B1 contém raciocínio (thinking) exibido pela interface, omitido nesta transcrição | resposta B2 usou 2 chamada(s) de ferramenta do claude.ai: bash_tool ("Ler registro factual da execução"); bash_tool ("Verificar se as evidências citadas no registro foram anexadas") | resposta B2 contém raciocínio (thinking) exibido pela interface, omitido nesta transcrição | resposta B1 entregou o roteiro como documento do Claude Docs (https://claude.ai/code/artifact/e56c6f32-fbe3-491c-8449-424cd98bb77e), salvo sem alteração pela função "Copiar como Markdown" do claude.ai em `anexos-saida/cadeia-3-B1-documento.md`

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

**Natureza da avaliação:** é analítica. Não executei o artefato, não importei a VM e não assisti ao vídeo. Nada abaixo afirma que algum comportamento funcionou.

## A. Materiais examinados

- **instrucoes-oficiais.md:** lido na íntegra.
- **reivindicacoes.md:** lido na íntegra.
- **artigo.pdf:** lido pelo conteúdo textual e pelas figuras disponibilizadas na conversa. Não o abri pela linha de comando.
- **artefato.txt:** aberto pela linha de comando. Li o índice e os seguintes arquivos completos:
  - `README.md`
  - `mininet-gui-backend/mininet_gui_backend/api.py` e `cli.py`
  - `mininet-gui-backend/requirements.txt`
  - `mininet-gui-frontend/package.json`
  - `src/components/TopologyForm.vue`
  - `run.sh` e `setup.sh`
  - `example_network_export.py`
- **artefato.txt, leitura parcial:** trechos de `NetworkGraph.vue` (linhas 488–628) e de `Webshell.vue` (linhas 1–135). Também fiz buscas por termos ("flow", "Tree/Linear/Single", "delete_", "terminal", "pingall") em todo o arquivo, exceto `package-lock.json`.
- **Não examináveis (evidência ausente):** o `.ova` da VM (link Google Drive em README.md:53), o vídeo (README.md:22) e o repositório remoto. Estão fora dos anexos.

## B. Selo Funcional (F)

**Critério F1, executabilidade e observação de funcionalidades.**
Trecho oficial: "O código ou artefato deve poder ser executado, e o revisor deve conseguir observar funcionalidades […] A conclusão funcional requer observação do artefato, não apenas a presença das instruções." [instrucoes-oficiais.md:Funcional (F)]
Status: **só verificável por execução.** O código traz pontos de entrada coerentes com o artigo:
- inicialização da rede: [artefato.txt:api.py:51] `start_network()`
- pingall: [api.py:157] `pingall_results = app.net.pingFull()`
- terminal: [api.py:462] `@app.websocket("/api/mininet/terminal/{node_id}")`

Isso mostra intenção, não funcionamento.

**Critério F2, dependências e versões.**
Trecho oficial: "O README deve informar dependências e versões" [instrucoes-oficiais.md:Funcional (F)]
Status: **atendido parcialmente.**
- Pela VM recomendada, há versão: [README.md:37] "Oracle VirtualBox (versão 7.1.6 r167084)"; [README.md:38] "Mínimo de 8GB para a máquina virtual".
- Pela instalação manual, as dependências do backend não têm versão: [requirements.txt:1–4] `fastapi`, `websockets`, `uvicorn`, `python-multipart`.
- A versão do Mininet não é fixada: [README.md:66] `git clone https://github.com/mininet/mininet`.
- O frontend usa faixas `^` [package.json:11–22], mas há `package-lock.json` no índice.
- O Node é fixado: [setup.sh:19] `nvm install 18.20.7`.

Como a VM encapsula o ambiente, não trato isso como falha obrigatória, mas é uma fragilidade.

**Critério F3, ambiente de execução.**
Status: **atendido na documentação.**
- [README.md:26–32] descreve o laptop de demonstração.
- [README.md:63] "testado no ubuntu 20.04".
- [README.md:103] "no mínimo 2GB de RAM e um core de CPU".
- Há uma inconsistência: o README pede 8 GB nas linhas 38 e 103 diz 2 GB.

**Critério F4, instalação.**
Status: **atendido na documentação.**
- [README.md:49–57] descreve a importação do `.ova`, "user `mininet`, senha `mininet`".
- [README.md:65–73] descreve a instalação manual com `./setup.sh`.
- Porém o `.ova` não está nos anexos, então não há como inspecioná-lo.

**Critério F5, execução.**
Status: **atendido na documentação.**
- [README.md:84] "rode o seguinte comando: `mininet_gui`".
- [run.sh:14] `sudo nohup uvicorn mininet_gui_backend.api:app --host=0.0.0.0 --port=8000`.
- [run.sh:28] imprime a URL `:5173`.

**Critério F6, exemplo mínimo.**
Status: **atendido na documentação.**
- [README.md:88] criar o controlador "Default".
- [README.md:90] "selecione o 'Topology Type' Single, o 'Controller' c1, e no campo 'Hosts' insira o número 2".
- [README.md:92] "Execute um teste de pingall".

**Decisão F: Indeterminado.** Nenhum critério obrigatório falha na documentação. Há fragilidade em F2, mas a VM mitiga. A conclusão depende de observar o artefato rodando, como as próprias instruções exigem.

**Confiança de que o comitê atribuiu F: 70.** A ferramenta é visual e simples de demonstrar. A VM pronta reduz o risco de instalação, e o teste mínimo é curto.

**O que observar na execução para mudar a decisão:**
- A VM importa e inicia no VirtualBox 7.1.6.
- `mininet_gui` sobe backend e frontend e exibe a URL.
- O controlador c1 aparece no grafo.
- O "Generate Topology" Single com 2 hosts desenha s1, h1 e h2 com links.
- O "Run Pingall Test" exibe o resultado h1↔h2 no modal.
- Se esses passos funcionarem, a decisão vira Atribuir. Uma falha não contornável em qualquer um deles a torna Não atribuir.

## C. Selo Reprodutível (R), por reivindicação

**Critério oficial.** "O revisor deve conseguir reproduzir as principais reivindicações do artigo […] o artefato precisa fornecer instruções de execução e descrição do processo empregado nos experimentos" [instrucoes-oficiais.md:Reprodutível (R)].
**Regra aplicada.** "R é atribuído se C4 e C5 forem reproduzidas" [reivindicacoes.md:Regra para o selo R].

**C1, interface web com grafo interativo: depende de execução (fora da regra de R).**
- O artigo afirma: [artigo.pdf:p.4, §3] "vis-network, que permite representar os elementos da rede como um grafo interativo".
- O README cobre esse comportamento: [README.md:88] "arraste o ícone rotulado 'Controller' […] para o centro da tela".
- No código, os nós e arestas são adicionados ao grafo: [NetworkGraph.vue:517] `this.edges.add({`.

**C2, emulação integrada com pingall: depende de execução (fora da regra de R).**
- O backend inicia a rede no arranque [api.py:49–52] e executa `pingFull()` [api.py:157].
- O README dá o passo correspondente: [README.md:92] "Run Pingall Test".

**C3, modificação em tempo real: depende de execução (fora da regra de R).**
- O artigo afirma: [artigo.pdf:p.5, §3] "uso dos métodos start e stop dos switches".
- O código segue essa abordagem: [api.py:188–189] `if app.net.is_started and switch.controller: new_switch.start(...)`; [api.py:256–263] reconfigura nós ao criar link com a rede ativa.
- A remoção existe: [api.py:298] `delete_node`; [api.py:318] `delete_link`.
- O README só cobre a criação de link com a rede ativa, como passo opcional [README.md:96]. Não há passo de remoção. A documentação é parcial.

**C4, geração Single/Linear/Tree: depende de execução.**
- Instruções do README: [README.md:107–108] "Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK."
- Os três modelos existem na interface: [TopologyForm.vue:7–9] `Single`, `Linear`, `Tree`.
- A implementação cobre os três: [NetworkGraph.vue:610–615] chama `createSingleTopo`, `createLinearTopo` e `createTreeTopo`.
- A lógica da árvore cria hosts na camada mais profunda e switches nas demais [NetworkGraph.vue:556–567], o que é coerente com uma TreeTopo de profundidade × fanout.
- A descrição do processo é mínima:
  - o README fala em "o número de dispositivos", mas Linear pede dois campos, "Switches" e "Hosts per switch" [TopologyForm.vue:25–30];
  - Tree pede "Layers" e "Fanout" [TopologyForm.vue:35–40];
  - o botão se chama "Submit" [TopologyForm.vue:43], não "OK".

  São imprecisões, não ausência de dado. O critério de reprodução exige observar os três modelos [reivindicacoes.md:Critério de reprodução].

**C5, terminal via WebShell: depende de execução.**
- Instruções do README: [README.md:112–114] "selecione a aba com o nome desse nó […] utilize o terminal bash para executar comandos diretamente no namespace daquele nó".
- No backend, [api.py:476] `node.popen(["/bin/bash", "-i"], stdin=slave_fd, ...)` abre um bash no contexto do nó.
- No frontend, [Webshell.vue:76] conecta com `new WebSocket(\`${this.backendWsUrl}/api/mininet/terminal/${nodeId}\`)`.
- A URL do WebSocket vem de [run.sh:17] `VITE_BACKEND_WS_URL=ws://…:8000`.
- Ressalva: os comandos executam no namespace de rede do nó para hosts. Os switches OVS ficam no namespace raiz, comportamento padrão do Mininet.

**C6, regras de fluxo OpenFlow: não reproduzível nesta versão (fora da regra de R).**
- O artigo afirma: [artigo.pdf:p.5, §3, Flow Rule Editor] "visualização, criação e remoção de regras de fluxo OpenFlow nos switches".
- No commit avaliado, o backend só lê a tabela: [api.py:363] `flow_table_raw = node.dpctl("dump-flows").strip()`.
- Não existe endpoint para inserir ou remover regras. As buscas por "flow" no arquivo só encontram leitura em `api.py:34–383` e exibição em `NodeStats.vue` (aba "Flow Table").
- O README não traz instruções para isso [reivindicacoes.md, linha C6: "não"].
- A visualização é plausível. A criação e a remoção pelo editor descrito não têm suporte no código. Restaria só o contorno manual via WebShell (`ovs-ofctl`), que não é a funcionalidade reivindicada.

**Decisão R: Indeterminado.** C4 e C5 têm instruções e código correspondente, e nenhum dado necessário falta. A reprodução, porém, só se confirma observando a execução. A lacuna de C6 é real, mas não entra na regra de R.

**Confiança de que o comitê atribuiu R: 60.** As duas reivindicações escolhidas são comportamentos simples e diretamente observáveis. O processo descrito é enxuto, e um comitê rigoroso poderia cobrar a ausência de C6, que aparece entre as contribuições.

**O que observar na execução para mudar a decisão:**
- Para C4: gerar Single (ex.: 3 hosts → 1 switch e 3 hosts), Linear (ex.: 3 switches × 2 hosts → 3 switches encadeados e 6 hosts) e Tree (ex.: 2 camadas, fanout 2 → 3 switches e 4 hosts).
- Para C4: conferir no grafo a contagem e as ligações de cada modelo.
- Para C5: abrir a aba de h1 no WebShell e rodar `ip addr show`, `hostname` e `ping -c1 10.0.0.2`.
- Para C5: ver na aba a saída com a interface `h1-eth0` e o IP do nó, como na Fig. 2 do artigo.
- Os dois resultados juntos tornam a decisão Atribuir. A falha em qualquer modelo de C4 ou no terminal a torna Não atribuir.

## D. Lacunas e riscos

1. **VM e vídeo fora dos anexos.** O caminho recomendado depende de um `.ova` hospedado externamente, que não pude inspecionar. Também não pude confirmar se ele corresponde ao commit `465648a4`.
2. **C6 sem implementação de criação e remoção.** É uma contribuição enumerada no artigo (p. 2, item 6) sem suporte no código avaliado. Isso não afeta a regra de R, mas é uma discrepância entre artigo e artefato que um revisor deve registrar.
3. **Versões frouxas na instalação manual.** O backend não tem versões fixadas [requirements.txt:1–4] e o Mininet é clonado do branch padrão [README.md:66]. A reprodução fora da VM pode divergir.
4. **Fragilidade de scripts.**
   - [run.sh:20] chama `nvm use 18.20.7` sem carregar `nvm.sh` no script. Só funciona se o `PATH` herdado já apontar para o Node correto.
   - Os caminhos são fixos em `/home/mininet/mininet-gui` [run.sh:7; setup.sh:5].
   - O módulo `cli.py` é um esboço não implementado [cli.py:20] `raise NotImplemented`, embora seja importado por `api.py:30` sem ser usado.
5. **Imprecisões no README.**
   - A RAM aparece como 8 GB [README.md:38] e como 2 GB [README.md:103].
   - O botão é chamado de "OK" no README e de "Submit" no código.
   - Os parâmetros de Linear e Tree não estão descritos.
6. **Segurança.** O backend roda com `sudo`, CORS `*` e expõe um shell root por WebSocket na rede [run.sh:14; api.py:76–81; api.py:476]. O README alerta sobre a instalação invasiva [README.md:43], mas não sobre essa exposição. A VM isolada é recomendável.

```json
{"F": {"decisao": "Indeterminado", "confianca": 70, "evidencias": ["artefato.txt:README.md:37", "artefato.txt:README.md:49-57", "artefato.txt:README.md:84", "artefato.txt:README.md:88-92", "artefato.txt:run.sh:14", "artefato.txt:mininet-gui-backend/requirements.txt:1-4", "artefato.txt:mininet-gui-backend/mininet_gui_backend/api.py:157"]},
 "R": {"decisao": "Indeterminado", "confianca": 60, "evidencias": ["reivindicacoes.md:Regra para o selo R", "artefato.txt:README.md:105-108", "artefato.txt:README.md:110-114", "artefato.txt:mininet-gui-frontend/src/components/TopologyForm.vue:7-9", "artefato.txt:mininet-gui-frontend/src/components/NetworkGraph.vue:610-615", "artefato.txt:mininet-gui-backend/mininet_gui_backend/api.py:476", "artefato.txt:mininet-gui-frontend/src/components/Webshell.vue:76", "artefato.txt:mininet-gui-backend/mininet_gui_backend/api.py:363"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "depende_execucao", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

Estrutura criada; agora preenchendo o escopo e os requisitos.

Escopo pronto para preencher; antes verifico como a interface abre a tabela de fluxo e os rótulos dos botões.

Agora o escopo e as convenções.

Escopo preenchido; agora os requisitos do ambiente.

Requisitos prontos; agora a preparação do ambiente (P1–P7).

Preparação pronta; agora o teste mínimo (P8–P14).

Teste mínimo pronto; agora os blocos de R por reivindicação (P15–P28).

Blocos R prontos; agora o tempo estimado e a tabela-resumo, e ajusto a contagem de passos não documentados no escopo.

O roteiro está pronto no documento aberto ao lado: 28 passos, sendo 12 marcados como [NÃO DOCUMENTADO]. Edite diretamente ou comente para eu revisar.

## Prompt B2

Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que atende parcialmente (VM dos autores no VirtualBox 7.1.6 com 8 GB de RAM, mas sobre o Hyper-V em modo NEM e com o navegador do host em vez de um navegador dentro da VM, como detalhado na seção 1 do registro) aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.

Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.

## Resposta B2

Baseio esta reavaliação no `registro-factual.md`. Os arquivos que ele cita (`terminal.txt`, capturas, logs, exportados) não foram anexados, então tomo as observações do registro como fato, sem conferir capturas ou hashes. Não executei nada.

## 1. Efeito de cada passo sobre a avaliação analítica

**Passos documentados pelos autores (D0/D1)**

| Passo | Resultado | Efeito |
|---|---|---|
| E02 | O link do Google Drive (README:53) está inativo. A VM veio da release `v0.0.1` dos próprios autores, e o nome do `.ova` difere de README:55. | **Contradiz em parte.** Eu tinha marcado a VM como evidência ausente. Agora há um defeito concreto na documentação de instalação, mas a fonte alternativa é dos autores, então F não fica bloqueado. |
| E04 | Importação sem erro. | Confirma. |
| E06 | A VM não tem ambiente gráfico; o acesso foi por SSH. | **Contradiz** o que o README pressupõe: terminal por Ctrl+Alt+T (README:84) e navegador dentro da VM (README:86). É divergência de documentação, sem efeito sobre as funcionalidades. |
| E09 | `mininet_gui` imprimiu a URL; backend e frontend subiram. | **Confirma.** O risco que apontei no `nvm` de run.sh:20 não se materializou: a VM roda um run.sh sem essa linha e carrega o Node pelo `~/.bashrc`. |
| E10 | Interface com barra lateral, grafo e WebShell. | Confirma (P7; C1). |
| E11–E13 | c1 criado; Single com 2 hosts e links verdes; pingall 1/1 nos dois sentidos. | **Confirma** o teste mínimo (P8–P10) e o comportamento esperado de C1 e C2. |
| E14 | O iperf (opcional) mediu 6,62 Gbit/s entre as abas h1 e h2. | Confirma; apoio a C5. |
| E16 | Ryu ausente; sem conectividade entre as duas topologias. O link s1–s2 ficou verde com a rede ativa. Os nós novos nasceram sobrepostos aos antigos. | **Confirma** dois riscos que eu tinha apontado: Ryu não garantido na VM e coordenadas fixas em `createSingleTopo` (NetworkGraph.vue:513). O passo 8 é opcional, então não bloqueia F. A criação de link com a rede ativa é evidência documentada para C3. |
| E17 | JSON e script exportados com a topologia corrente. | Confirma (P13). |
| E19–E22 | Grafos e contagens: Single 3 hosts; Linear 3×2 (3 switches, 6 hosts, 8 links); Linear 2×1; Tree 2×2 (3 switches, 4 hosts, 6 links). | **Confirma** C4 nos três modelos. As contagens coincidem com as que derivei do código. As quantidades foram escolhidas pelos revisores, mas o README manda o usuário escolhê-las. |
| E24 | Aba h1: `h1-eth0` 10.0.0.1/8. | **Confirma** C5. O procedimento é dos autores; só o comando foi escolhido. |

**Passos não documentados (D2), usados só como evidência complementar**

| Passo | Resultado | Efeito |
|---|---|---|
| E07 | A VM está no commit `be68302`, não em `465648a4`. Backend e frontend são idênticos (registro, 1.3). | Não altera. Era a ressalva prevista em P5, e o código executado é o que analisei. |
| E25–E27 | Cada aba está no namespace de rede do seu nó, diferente do da VM; ping h1→h2 sem perda. | Reforça C5. |
| E28a–E28b | Nó arrastado mantém a posição após recarregar; nós soltos da paleta podem ser ligados. | Reforça C1. |
| E29 | Pingall 20/20 incluindo h5, criado com a rede ativa. | Reforça C2 e a parte de criação de C3. |
| E30a–E30b, E30d | Link e nó removidos sem reiniciar a emulação; h1 continua alcançando h3. | Reforça a parte de remoção de C3, que o README não documenta. |
| E30c | Após as remoções, o pingall retorna HTTP 500 (`AttributeError` em `pingFull`), e `/links` mantém a entrada `h4–s2`. | **Achado novo, mas coerente com o código:** `delete_node` (api.py:298–316) não limpa `app.links`. É um defeito a registrar. Não decide R. |
| E31 | A Flow Table de s1 mostra 5 regras. | Confirma a parte de visualização de C6. |
| E32 | Nenhum controle para criar ou remover regras de fluxo. | **Confirma** minha classificação de C6 como não reproduzível. |
| E15, E05, E08, E18, E23 | Diversos. | Não alteram. E15 confirma o Ryu ausente. E05 mostra que a OVA vinha com 1536 MB e 1 vCPU, o que reforça a inconsistência entre README:38 e README:103. |

## 2. Novas decisões

**F: Atribuir.**
- O artefato foi executado e suas funcionalidades foram observadas pelo procedimento dos autores: passos 1–6 e 9 do teste mínimo (E06, E09–E13, E17), mais o passo 7 opcional (E14).
- O README informa ambiente, versão do VirtualBox, instalação, execução e um exemplo mínimo.
- Nenhum critério obrigatório falhou:
  - o link quebrado tem substituto oficial dos autores;
  - a VM sem interface gráfica não impediu nenhuma funcionalidade;
  - o passo 8 com Ryu é declarado opcional.
- Esses três pontos entram na revisão como problemas encontrados, como pedem as instruções.

**R: Atribuir.**
- **C4 reproduzida:** E19–E22 mostram os três modelos com a quantidade escolhida, observada no grafo dentro de passos documentados. A contagem pela API (E23) só reforça.
- **C5 reproduzida:** E24 mostra a saída na aba do nó selecionado. E14 também é documentado e mostra o mesmo comportamento.
- Pela regra de reivindicacoes.md, isso basta para R.

**Classificação por reivindicação**

- **C1 e C2:** reproduzíveis por E10–E13.
- **C3: reproduzível, com ressalva.** O resultado esperado ("rede alterada enquanto a emulação continua ativa") foi observado no passo documentado E16: segundo controlador, segunda topologia e link s1–s2 com a rede ativa.
  - A remoção só aparece em D2 (E30).
  - Depois da remoção, o pingall falha com HTTP 500 (E30c).
- **C6: não reproduzível.** Os autores não documentam procedimento, e E32 mostra que não há como criar ou remover regras pela interface. Só a visualização existe (E31).

Não restou motivo para Indeterminado: o registro fornece as observações que faltavam.

## 3. Confiança e mudança

- **F, confiança 85** (antes: Indeterminado, 70). A mudança vem de observar diretamente o teste mínimo. Os 15 pontos de dúvida refletem três divergências da documentação que um revisor do comitê, em 2025, talvez não tenha encontrado ou tenha julgado de outra forma: link, VM sem área gráfica e Ryu ausente.
- **R, confiança 80** (antes: Indeterminado, 60). As duas reivindicações da regra foram observadas por passos documentados, com resultado inequívoco. Resta o risco de o comitê ter cobrado C6, contribuição do artigo sem implementação de criação e remoção.
- **Limites do ambiente:** são uma execução única, Hyper-V em modo NEM, navegador do host, operação automatizada por CDP e commit `be68302`. Nada disso afeta as reivindicações, que não têm valores de desempenho e cujo código é idêntico ao do commit avaliado. Por isso não reduzi a decisão por esses fatores.

```json
{"F": {"decisao": "Atribuir", "confianca": 85, "mudou": true, "evidencias": ["registro-factual.md:E09", "registro-factual.md:E10", "registro-factual.md:E11", "registro-factual.md:E12", "registro-factual.md:E13", "registro-factual.md:E14", "registro-factual.md:E17", "registro-factual.md:E02", "registro-factual.md:E06", "registro-factual.md:E16", "artefato.txt:README.md:84-98"]},
 "R": {"decisao": "Atribuir", "confianca": 80, "mudou": true, "evidencias": ["reivindicacoes.md:Regra para o selo R", "registro-factual.md:E19", "registro-factual.md:E20", "registro-factual.md:E21", "registro-factual.md:E22", "registro-factual.md:E24", "registro-factual.md:E14", "registro-factual.md:1.3", "registro-factual.md:E23 (D2, complementar)", "registro-factual.md:E25-E27 (D2, complementar)", "registro-factual.md:E30c (D2, defeito)", "registro-factual.md:E32 (D2, C6)"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "reproduzivel", "C3": "reproduzivel", "C4": "reproduzivel", "C5": "reproduzivel", "C6": "nao_reproduzivel"}}}
```
