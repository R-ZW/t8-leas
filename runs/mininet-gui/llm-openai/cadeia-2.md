# Cadeia MG-2 — openai

- provedor: openai
- modelo_exibido: GPT 6.1 Sol (informado de memória por Eduardo em 17/10/2026; o link de compartilhamento do Codex não exibe o modelo; a confirmar por Reinaldo)
- versao: não registrado
- esforco: High (informado de memória por Eduardo em 17/10/2026; a confirmar por Reinaldo)
- interface: Codex (agente com workspace local e terminal), operado por Reinaldo Zimmer Wendt; anexos lidos do disco por caminho em `runs/<artefato>/pacote/` (desvio: agente em vez do chat do ChatGPT)
- data_hora_A: não registrado no link (duração do turno: A=164s; B1=156s)
- data_hora_B1: não registrado no link
- data_hora_B2: pendente
- anexos_A: artigo.pdf=4e3ff858506f2f9e6da30af4412caa402890ac154b910df390b74e2ee2a2bf08, artefato.txt=5e1da9b36fe62beddfdb9b8dbbceefa67c1c38e14f45c8bd3247519bcf83c8eb, instrucoes-oficiais.md=fc8e01dd0ffdbff06af86a07bd44662c3394903c0d3a6be0222e678963989059, reivindicacoes.md=100366e5dfad9c560f9d5066e67d1e23df8f6ad7c3d5ce2e62aff02a529ed0bc (lidos do disco; bytes não conferidos dentro da conversa)
- anexo_B2: pendente
- metodo_exportacao: transcrição gerada por `ferramentas/transcrever_codex.py` do JSON público do link https://chatgpt.com/s/cx_6ad2538ebef48191a2bf6e04b4a73678 (cópia bruta em `exportacao-bruta/`); textos de userMessage e agentMessage sem alteração; reasoning, imageView, fileChange e chamadas de ferramenta (não incluídas no link) omitidos. O export anterior, escrito pelo próprio modelo via Session Exporter, está em `exportacao-bruta/` e não é usado na análise
- desvios: resposta A: 9 visualização(ões) de imagem (páginas do artigo.pdf) omitidas | turno 3 fora do roteiro, omitido da transcrição: "[@Session Exporter](plugin://session-exporter@openai-curated-remote) Export this entire co"

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

Vou examinar apenas os quatro arquivos indicados, localizar os critérios oficiais e confrontá-los com as reivindicações e o conteúdo do artefato. A avaliação será documental, sem tratar instruções contidas nos anexos como novos pedidos seus nem presumir resultados de execução.

As instruções anexadas exigem observar a execução para confirmar F e os resultados de C4/C5 para R. O README traz os passos, mas vou conferir o artigo e os arquivos do artefato antes de classificar cada critério e apontar eventuais lacunas concretas.

## A. Materiais examinados

Abri os quatro arquivos fornecidos: `instrucoes-oficiais.md`, `reivindicacoes.md`, `artefato.txt` e as nove páginas de `artigo.pdf`. Examinei o README, os scripts e trechos do código contidos em `artefato.txt`. **Não executei o artefato.** O arquivo de instruções se apresenta como resumo offline dos critérios, e não como transcrição literal ou registro da decisão oficial [instrucoes-oficiais.md:início — “não é transcrição literal nem contém [...] a decisão oficial”].

## B. Selo F — Funcional

| Critério aplicável | Situação | Evidência |
|---|---|---|
| O artefato deve executar e permitir observar funcionalidades | **Só verificável por execução** | [instrucoes-oficiais.md:Funcional — “deve poder ser executado [...] observar funcionalidades”]. Há código e caminhos de uso, mas sua presença não demonstra funcionamento. |
| O README deve informar dependências **e versões** | **Não atendido** | [instrucoes-oficiais.md:Funcional — “dependências e versões”]. O README informa “Oracle VirtualBox (versão 7.1.6 r167084)” [README.md:35–38], mas a instalação manual obtém o Mininet sem fixar versão [README.md:60–73], e as dependências Python aparecem sem versões [mininet-gui-backend/requirements.txt:1–4 — “fastapi”, “websockets”, “uvicorn”, “python-multipart”]. |
| Informar ambiente de execução e instalação | **Atendido na documentação** | [README.md:26–38 — “8,00 GB”, “Pelo menos 80GB livres”, “Mínimo de 8GB para a máquina virtual”]; [README.md:47–73 — passos para VM e instalação manual]. A adequação real do ambiente só poderia ser confirmada ao executar. |
| Informar execução e exemplo mínimo | **Atendido na documentação** | [README.md:80–92 — executar `mininet_gui`, abrir a URL, gerar topologia Single com dois hosts e rodar `pingall`]. |
| Fundamentar a conclusão funcional em observação | **Só verificável por execução** | [instrucoes-oficiais.md:Funcional — “A conclusão funcional requer observação do artefato”]. |

**Decisão: Não atribuir F**, pela lacuna documental explícita de versões de dependências. Isso não é uma afirmação de que o programa falha: sua execução e suas funcionalidades permanecem sem verificação. Minha **confiança de que o comitê oficial tenha atribuído F é 45/100**; os anexos não contêm sua decisão.

Para mudar esta avaliação, seria necessário completar a identificação das versões e, na execução, observar a inicialização da interface, a criação da topologia do teste mínimo e o resultado do `pingall`. A execução, sozinha, não corrige a lacuna documental.

## C. Selo R — Reprodutível

O critério oficial é conseguir reproduzir as principais reivindicações, com “instruções de execução e descrição do processo” e confronto entre resultado observado e reivindicação [instrucoes-oficiais.md:Reprodutível]. A regra fornecida delimita R a **C4 e C5**: “R é atribuído se C4 e C5 forem reproduzidas” [reivindicacoes.md:Regra para o selo R]. Assim, as demais contribuições são examinadas abaixo, mas não determinam R.

| Reivindicação | Avaliação documental e evidência | Estado |
|---|---|---|
| **C1 — grafo interativo** | O artigo reivindica “Interface web dinâmica para manipulação intuitiva da topologia” [artigo.pdf:p. 2, §1]. O README orienta arrastar um controlador e gerar uma topologia [README.md:88–90]. A resposta visual às ações requer observação. | **Depende de execução**; fora da regra de R. |
| **C2 — emulação integrada** | O artigo reivindica “Emulação integrada” [artigo.pdf:p. 2, §1]. O teste mínimo manda “Execute um teste de pingall” [README.md:92]; o código prevê `app.net.pingFull()` [mininet-gui-backend/mininet_gui_backend/api.py:152–159]. Falta observar os nós e o resultado na interface. | **Depende de execução**; fora da regra de R. |
| **C3 — mudança em tempo real** | O artigo reivindica “modificações na topologia em tempo real” [artigo.pdf:p. 2, §1]. O passo opcional cria outra topologia e um link [README.md:96], mas não estabelece uma verificação explícita de continuidade da emulação. | **Depende de execução**; fora da regra de R. |
| **C4 — modelos Single, Linear e Tree** | O artigo afirma suporte aos três modelos [artigo.pdf:p. 6, §3 — “single, linear e tree”]. O README orienta selecionar “Single, Linear ou Tree” e o número de dispositivos [README.md:105–108]; o código contém as três rotinas de geração [mininet-gui-frontend/src/components/NetworkGraph.vue:512–585]. As instruções de processo estão documentadas, mas nenhum dos três resultados foi observado. | **Depende de execução**; **conta para R**. |
| **C5 — WebShell no nó** | O artigo reivindica “Terminal integrado dos nós via WebShell” [artigo.pdf:p. 2, §1]. O README orienta selecionar a aba do nó e executar comandos em seu namespace [README.md:110–114]; o backend abre `bash` com `node.popen(...)` [mininet-gui-backend/mininet_gui_backend/api.py:462–486]. É preciso observar a saída na aba correta. | **Depende de execução**; **conta para R**. |
| **C6 — regras de fluxo** | O artigo reivindica visualização e criação [artigo.pdf:p. 2, §1] e descreve criação e remoção [artigo.pdf:p. 6, §3]. O README não traz experimento para isso [README.md:101–114]. O código examinado expõe uma aba “Flow Table” [mininet-gui-frontend/src/components/NodeStats.vue:35–38] e consulta `dump-flows` [mininet-gui-backend/mininet_gui_backend/api.py:358–383], sem documentar como criar ou remover regras. | **Não reproduzível pela documentação fornecida**; fora da regra de R. |

Para os critérios que **determinam R**, as instruções de execução e os processos de C4 e C5 estão **atendidos na documentação**; a reprodução dos resultados é **só verificável por execução**. **Decisão: Indeterminado para R.** Não há, nesses dois casos, falha documental obrigatória demonstrada, mas também não há observação que autorize atribuir o selo. Minha **confiança de que o comitê oficial tenha atribuído R é 50/100**; trata-se de estimativa sob ausência da decisão oficial, não de um resultado consultado.

Para mudar R para **Atribuir**, seria preciso observar os três modelos de C4 com as quantidades escolhidas e, em C5, a saída de um comando Bash na aba do nó selecionado, demonstrando que veio do namespace desse nó. Uma falha confirmada em qualquer uma dessas duas reivindicações sustentaria **Não atribuir**.

## D. Lacunas e riscos

- A VM recomendada é indicada por um link externo [README.md:49–57 — “Baixe o arquivo ova neste link”], mas o OVA não está no índice do artefato fornecido [artefato.txt:índice]. Pela restrição desta avaliação, sua disponibilidade e seu conteúdo são **evidência ausente**.
- As versões não fixadas do Mininet e das dependências Python dificultam repetir o ambiente manual [README.md:60–73; mininet-gui-backend/requirements.txt:1–4].
- Nenhum resultado produzido pela versão examinada foi observado. A figura do artigo [artigo.pdf:p. 7, Fig. 2] e os caminhos presentes no código não substituem a execução exigida pelos critérios.

```json
{
  "F": {
    "decisao": "Não atribuir",
    "confianca": 45,
    "evidencias": [
      "instrucoes-oficiais.md:Funcional",
      "README.md:35-38",
      "README.md:60-73",
      "README.md:80-92",
      "mininet-gui-backend/requirements.txt:1-4"
    ]
  },
  "R": {
    "decisao": "Indeterminado",
    "confianca": 50,
    "evidencias": [
      "instrucoes-oficiais.md:Reprodutível",
      "reivindicacoes.md:Regra para o selo R",
      "README.md:101-114",
      "artigo.pdf:p. 2, §1",
      "artigo.pdf:p. 6, §3",
      "mininet-gui-frontend/src/components/NetworkGraph.vue:512-585",
      "mininet-gui-backend/mininet_gui_backend/api.py:462-486"
    ],
    "por_reivindicacao": {
      "C1": "depende_execucao",
      "C2": "depende_execucao",
      "C3": "depende_execucao",
      "C4": "depende_execucao",
      "C5": "depende_execucao",
      "C6": "nao_reproduzivel"
    }
  }
}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

Vou montar o roteiro a partir dos passos do README e da regra de R em `reivindicacoes.md`. Vou marcar as ações de registro de evidências e os procedimentos necessários que os autores não especificam, sem acrescentar comandos de instalação ou teste como se fossem deles.

# Roteiro de execução para F e R

Este roteiro usa apenas os procedimentos descritos no material fornecido. **Não executei o artefato.** As capturas, a conferência do commit e o isolamento dos testes estão marcados **[NÃO DOCUMENTADO]**: são ações de verificação necessárias, mas os autores não as prescrevem.

A rota principal é a **VM recomendada no README**. O arquivo OVA não consta do índice de `artefato.txt`; o README fornece um link para obtê-lo [README.md:49–57; artefato.txt:índice]. Se ele não estiver acessível, a rota abaixo fica interrompida. A instalação manual está descrita em [README.md:60–77], mas seus comandos `git clone` não fixam a versão `465648a4425a4457af0348ab951cf7f71d37a86f`; por isso, não a trato como uma execução comprovada dessa versão.

## Requisitos antes de começar

- **Host da demonstração dos autores:** processador Intel i5-10300H, 8 GB de RAM, Windows 11 de 64 bits e pelo menos 80 GB livres. São as características da demonstração, não mínimos gerais declarados [README.md:26–32].
- **Software da rota principal:** Oracle VirtualBox **7.1.6 r167084** e `Mininet-GUI-Desktop-VM-SBRC-2025.ova` [README.md:35–37, 49–57].
- **Recursos da VM:** o README diz “mínimo de 8GB” na seção Dependências, mas “no mínimo 2GB de RAM e um core de CPU” na seção Experimentos [README.md:37–38, 101–103]. **[NÃO DOCUMENTADO]** Não há reconciliação desses mínimos. Planeje 8 GB para seguir o requisito mais alto e registre a configuração efetiva.
- **Rota manual, caso seja necessária:** os autores indicam Ubuntu 20.04, Mininet, `setup.sh`, Node 18.20.7 no script e dependências Python listadas sem versões [README.md:60–77; setup.sh:1–22; mininet-gui-backend/requirements.txt:1–4]. Não há instrução dos autores para assegurar o commit fixado nessa rota.

**Regra de registro — [NÃO DOCUMENTADO]:** salve capturas da tela, saída visível do terminal e anotações dos parâmetros usados. Isso é necessário para distinguir observação de intenção documentada; o README não especifica um protocolo de coleta. Não altere comandos ou parâmetros que os autores fixaram.

## Preparação e teste mínimo — F

**P1 — Conferir recursos.** **Selo/reivindicação:** F; preparação de R. **Diretório:** host e configurações da VM; não há diretório de trabalho. **Comando exato:** nenhum; **[NÃO DOCUMENTADO]** conferir capacidade e recursos configurados. **Esperado segundo os autores:** ambiente com VirtualBox e recursos acima. **Salvar:** configuração do host e da VM. **Sucesso:** requisitos registrados e VM configurada com recursos suficientes. **Falha:** recurso abaixo do declarado. **Interrupção:** não iniciar o teste se a VM não puder receber os recursos necessários.

**P2 — Obter o OVA.** **Selo/reivindicação:** F e R; preparação. **Diretório:** local de download no host **[NÃO DOCUMENTADO]**. **Comando exato:** ação do README: baixar `Mininet-GUI-Desktop-VM-SBRC-2025.ova` pelo [link indicado pelos autores](https://drive.google.com/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing) [README.md:53]. **Esperado:** arquivo OVA disponível para importar. **Salvar:** nome e identificação do arquivo obtido **[NÃO DOCUMENTADO]**. **Sucesso:** OVA obtido. **Falha:** arquivo ausente ou inacessível. **Interrupção:** sem OVA, parar a rota principal; não presumir que `artefato.txt` seja uma VM executável.

**P3 — Importar, iniciar e entrar na VM.** **Selo/reivindicação:** F e R; preparação. **Diretório:** VirtualBox/VM. **Comando exato:** abrir o OVA no VirtualBox, executar a VM e entrar com usuário `mininet`, senha `mininet` [README.md:55–57, 82]. **Esperado:** sessão da VM acessível. **Salvar:** tela da VM iniciada **[NÃO DOCUMENTADO]**. **Sucesso:** login concluído. **Falha:** falha na importação, inicialização ou login. **Interrupção:** parar antes dos testes da aplicação se não houver sessão utilizável.

**P4 — Conferir a versão testada.** **Selo/reivindicação:** F e R; controle da versão. **Diretório:** `/home/mininet/mininet-gui`. **Comando exato:** **[NÃO DOCUMENTADO]** `git rev-parse HEAD`. **Esperado segundo os autores:** nenhum resultado é especificado; o material fornecido identifica o commit `465648a4425a4457af0348ab951cf7f71d37a86f` [artefato.txt:cabeçalho]. **Salvar:** saída do comando ou a indicação de que a VM não contém metadados Git. **Sucesso:** saída igual ao commit fixado. **Falha:** saída diferente. **Interrupção:** se a versão divergir ou não puder ser estabelecida, não atribuir os resultados à versão especificada. A conferência é necessária porque o README não identifica o commit contido no OVA.

**P5 — Iniciar a aplicação.** **Selo/reivindicação:** F; base de C1–C5. **Diretório:** terminal da VM; o README não exige diretório corrente. **Comando exato:** `mininet_gui` — alternativa dos autores: `/home/mininet/mininet-gui/run.sh` [README.md:84]. **Esperado:** uma URL no terminal, por exemplo `http://10.0.2.15:5173` [README.md:86]. **Salvar:** saída do terminal, inclusive a URL **[NÃO DOCUMENTADO]**. **Sucesso:** URL exibida. **Falha:** comando não inicia ou não exibe URL. **Interrupção:** não prosseguir aos testes de interface sem a URL.

**P6 — Abrir a interface.** **Selo/reivindicação:** F; C1–C5. **Diretório:** navegador dentro da VM. **Comando exato:** acessar **a URL exibida em P5**, conforme [README.md:86]. **Esperado:** interface web do Mininet-GUI. **Salvar:** captura da interface **[NÃO DOCUMENTADO]**. **Sucesso:** controles e área gráfica visíveis. **Falha:** página indisponível ou interface inutilizável. **Interrupção:** parar as ações de interface se ela não carregar.

**P7 — Criar o controlador.** **Selo/reivindicação:** F; C1. **Diretório:** interface web. **Comando exato:** arrastar **“Controller”** da lateral ao centro, escolher **“Default”** e pressionar **“Submit”** [README.md:88]. **Esperado:** controlador criado no grafo. **Salvar:** captura antes/depois **[NÃO DOCUMENTADO]**. **Sucesso:** controlador aparece e responde à ação. **Falha:** não aparece ou a ação dá erro. **Interrupção:** não executar P8 com `c1` se ele não tiver sido criado.

**P8 — Gerar a topologia Single.** **Selo/reivindicação:** F; C1 e C4. **Diretório:** interface web. **Comando exato:** **“Generate Topology” → “Topology Type: Single” → “Controller: c1” → “Hosts: 2” → “Submit”** [README.md:90]. **Esperado:** topologia Single com os dois hosts pedidos, representada no grafo. **Salvar:** parâmetros e grafo resultante **[NÃO DOCUMENTADO]**. **Sucesso:** topologia exibida com a quantidade escolhida. **Falha:** geração ausente, erro ou quantidade divergente. **Interrupção:** não testar conectividade ou WebShell se os nós necessários não existirem.

**P9 — Testar conectividade.** **Selo/reivindicação:** F; C2. **Diretório:** interface web. **Comando exato:** clicar **“Run Pingall Test”** e aguardar os resultados [README.md:92]. **Esperado:** resultados de `pingall` exibidos; o artigo descreve teste de conectividade [artigo.pdf:p. 6, §4]. **Salvar:** resultado integral exibido **[NÃO DOCUMENTADO]**. **Sucesso:** resultado aparece e indica conectividade entre os nós testados. **Falha:** erro, ausência de resultado ou conectividade não demonstrada. **Interrupção:** não interpretar uma tela vazia como aprovação; registrar a falha antes de seguir.

**P10 — Exportar a topologia.** **Selo/reivindicação:** F, passo final do teste mínimo dos autores. **Diretório:** interface web; destino dos arquivos não especificado. **Comando exato:** clicar **“Export Topology (JSON)”** e **“Export Mininet Script”** [README.md:98]. **Esperado:** arquivo JSON e script Python da topologia atual. **Salvar:** os dois arquivos gerados **[NÃO DOCUMENTADO]**. **Sucesso:** ambos obtidos. **Falha:** um deles não é gerado. **Interrupção:** registrar a falha; a exportação não deve ser tomada como prova de C4 ou C5.

## R — um bloco por reivindicação

A regra anexa faz **somente C4 e C5 determinarem R** [reivindicacoes.md:Regra para o selo R]. Os demais blocos registram como verificar as contribuições sem ampliar essa regra.

### C1 — Interface e grafo interativo

**Passos:** P6–P8. Observe se o controlador e os elementos da topologia aparecem após as ações do usuário e podem ser manipulados visualmente, como reivindicado [artigo.pdf:p. 2, §1; reivindicacoes.md:C1]. **[NÃO DOCUMENTADO]** O README não define uma sequência adicional nem uma medida de resposta às ações. Salve as telas antes/depois. C1 pode informar F, mas **não conta para R**.

### C2 — Emulação integrada e conectividade

**Passos:** P8–P9. Registre os nós exibidos e o resultado do `pingall` na interface [reivindicacoes.md:C2]. **[NÃO DOCUMENTADO]** Os autores não dão um limite numérico de perda ou latência para aprovação; não crie um. C2 **não conta para R**.

### C3 — Alteração com a emulação em andamento

**P11 — Executar o passo opcional de múltiplos controladores.** **Selo/reivindicação:** apoio a F; C3, fora da regra de R. **Diretório:** interface web e WebShell da VM. **Comando exato:** arrastar outro **“Controller”**, escolher **“Remote”**, IP `127.0.0.1`, porta `6633`; gerar outra topologia **Single** com **2 hosts** e controlador `c2`; usar **“Create Link”** para conectar `s1` a `s2`; no terminal WebShell de `c2`, executar `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; clicar **“Run Pingall Test”** [README.md:96]. **Esperado:** linha verde entre os switches e resultado do novo teste de conexão [README.md:96]. **Salvar:** telas antes/depois, linha verde, saída do terminal e `pingall` **[NÃO DOCUMENTADO]**. **Sucesso:** esses resultados aparecem. **Falha:** criação, ligação, Ryu ou teste falham. **Interrupção:** parar se `c2`, `s1`, `s2` ou o comando Ryu não estiverem disponíveis; não instalar componentes por um procedimento não previsto neste passo.

**P12 — Verificar continuidade da emulação.** **Selo/reivindicação:** C3, fora da regra de R. **Diretório:** interface web. **Comando exato:** **[NÃO DOCUMENTADO]** não há comando ou procedimento dos autores para comprovar que a emulação permaneceu ativa sem reinício. **Esperado segundo os autores:** modificação “sem que a emulação [...] precisasse ser interrompida ou reiniciada” [artigo.pdf:p. 6, §3]. **Salvar:** registro temporal do estado antes, durante e depois da alteração, se a interface permitir **[NÃO DOCUMENTADO]**. **Sucesso:** continuidade demonstrada. **Falha:** reinício/interrupção observado. **Interrupção:** se não houver meio de observar continuidade, classificar **C3 como não verificada**, mesmo que P11 mostre a nova ligação. Este passo é necessário porque uma linha verde final não prova ausência de reinício.

### C4 — Geração de Single, Linear e Tree **(determina R)**

P8 cobre **Single** com os parâmetros expressos pelos autores. A seção “Experimentos” manda selecionar **Single, Linear ou Tree** e o número de dispositivos [README.md:105–108]. Ela não fornece valores de teste para Linear e Tree nem manda limpar a topologia entre ensaios.

**P13 — Isolar o ensaio Linear.** **Selo/reivindicação:** R/C4. **Diretório:** interface web. **Comando exato:** **[NÃO DOCUMENTADO]** usar **“Reset Topology”**, controle presente na interface descrita no código [mininet-gui-frontend/src/components/Side.vue:22–24]. **Esperado segundo os autores:** não especificado para este preparo. **Salvar:** captura do grafo antes/depois **[NÃO DOCUMENTADO]**. **Sucesso:** área pronta para distinguir os nós do novo modelo. **Falha:** nós anteriores permanecem de modo indistinguível. **Interrupção:** não atribuir contagens ao modelo Linear se não for possível separá-lo da topologia anterior. O isolamento é necessário para conferir a quantidade gerada.

**P14 — Gerar Linear.** **Selo/reivindicação:** R/C4. **Diretório:** interface web. **Comando exato:** **“Generate Topology” → “Linear” → informar “Switches” e “Hosts per switch” → “Submit”** [README.md:105–108; mininet-gui-frontend/src/components/TopologyForm.vue:23–31]. **[NÃO DOCUMENTADO]** Os autores não fixam números; escolha-os antes do teste e registre os valores. **Esperado:** modelo Linear com as quantidades escolhidas [artigo.pdf:p. 6, §3]. **Salvar:** campos preenchidos e grafo final **[NÃO DOCUMENTADO]**. **Sucesso:** estrutura Linear e quantidades correspondentes aos campos. **Falha:** modelo ou quantidade divergente. **Interrupção:** parar a avaliação de C4 se o modelo não puder ser selecionado ou se o resultado não puder ser contado.

**P15 — Isolar o ensaio Tree.** **Selo/reivindicação:** R/C4. **Diretório:** interface web. **Comando exato:** **[NÃO DOCUMENTADO]** usar **“Reset Topology”**, pelo mesmo motivo de P13. **Esperado segundo os autores:** não especificado. **Salvar:** captura antes/depois **[NÃO DOCUMENTADO]**. **Sucesso:** nós de ensaios anteriores não se confundem com a árvore. **Falha:** não é possível distingui-los. **Interrupção:** não atribuir contagens ao modelo Tree sem isolamento ou distinção verificável.

**P16 — Gerar Tree.** **Selo/reivindicação:** R/C4. **Diretório:** interface web. **Comando exato:** **“Generate Topology” → “Tree” → informar “Layers” e “Fanout” → “Submit”** [README.md:105–108; mininet-gui-frontend/src/components/TopologyForm.vue:33–41]. **[NÃO DOCUMENTADO]** Os autores não fixam os valores; registre os escolhidos antes da geração. **Esperado:** modelo Tree correspondente aos parâmetros [artigo.pdf:p. 6, §3]. **Salvar:** campos e grafo final **[NÃO DOCUMENTADO]**. **Sucesso:** árvore exibida e quantidade de dispositivos compatível com os parâmetros registrados. **Falha:** modelo ou quantidade divergente. **Interrupção:** se não for possível verificar a árvore, C4 não está reproduzida. **C4 só passa quando Single, Linear e Tree passarem.**

### C5 — Terminal dos nós via WebShell **(determina R)**

Execute este bloco **logo após P9, antes de P13**, enquanto `h1` e `h2` da topologia Single estão disponíveis. O exemplo de comandos é o passo opcional dos autores [README.md:94]; a seção “Experimentos” orienta selecionar a aba do nó e usar Bash em seu namespace [README.md:110–114].

**P17 — Iniciar o servidor no nó h1.** **Selo/reivindicação:** R/C5. **Diretório:** aba WebShell de `h1`. **Comando exato:** `iperf -s` [README.md:94]. **Esperado:** comando executado no terminal do nó; o artigo reivindica acesso ao terminal pela interface [artigo.pdf:p. 5–6, §3]. **Salvar:** aba selecionada e saída exibida **[NÃO DOCUMENTADO]**. **Sucesso:** saída do comando na aba `h1`. **Falha:** aba ou execução indisponível. **Interrupção:** não iniciar o cliente se o servidor não estiver ativo.

**P18 — Executar o cliente no nó h2.** **Selo/reivindicação:** R/C5. **Diretório:** aba WebShell de `h2`. **Comando exato:** `iperf -c 10.0.0.1`; aguardar **1 minuto**, como orientado [README.md:94]. **Esperado:** saída do comando na aba do nó selecionado. **Salvar:** aba `h2`, comando e saída; também a saída em `h1`, se exibida **[NÃO DOCUMENTADO]**. **Sucesso:** resultado visível no terminal de `h2`, associado à execução no nó emulado. **Falha:** comando não executa, não há saída ou a saída não corresponde à aba/nó. **Interrupção:** se `h1`, `h2` ou WebShell não estiverem disponíveis, C5 permanece sem reprodução.

### C6 — Regras OpenFlow

**[NÃO DOCUMENTADO] Não há passo executável dos autores para criar e remover regras de fluxo.** O README só descreve experimentos para C4 e C5 [README.md:101–114]. A contribuição C6 aparece no artigo [artigo.pdf:p. 2, §1; p. 6, §3], e o código examinado oferece consulta à tabela (`dump-flows`) [mininet-gui-backend/mininet_gui_backend/api.py:358–383]. Não acrescente comandos `ovs-ofctl` ou um procedimento próprio e os apresente como teste dos autores. Registre a lacuna. **C6 não determina R** pela regra anexa.

## Tempo estimado

**[NÃO DOCUMENTADO] Estimativa de planejamento, não medição nem prazo dos autores:** 20–45 min para importar e iniciar a VM, 10–20 min para P5–P10, 10–25 min para os três modelos de C4, 5–10 min para C5 e 10–20 min para o passo opcional de C3. Reserve **45–100 min sem C3**, **55–120 min com C3**, **mais o tempo de download do OVA**. A única duração explicitamente indicada pelos autores é **1 minuto** para o teste `iperf` [README.md:94].

## Tabela de todos os passos

A ordem prática é P1–P9, **P17–P18**, P11–P12 se desejar examinar C3, P10, e então P13–P16.

| Passo | Ação | Selo/reivindicação | Origem |
|---|---|---|---|
| P1 | Conferir recursos | F/R | **[NÃO DOCUMENTADO]** conferência; requisitos no README |
| P2 | Obter OVA | F/R | README |
| P3 | Importar, iniciar e entrar na VM | F/R | README |
| P4 | Conferir commit | F/R | **[NÃO DOCUMENTADO]** |
| P5 | Executar `mininet_gui` | F; base de R | README |
| P6 | Abrir URL na VM | F; C1–C5 | README |
| P7 | Criar controlador Default | F; C1 | README |
| P8 | Gerar Single com dois hosts | F; C1/C4 | README |
| P9 | Rodar Pingall Test | F; C2 | README |
| P10 | Exportar JSON e script | F | README |
| P11 | Executar passo opcional de múltiplos controladores | C3 | README |
| P12 | Verificar ausência de reinício | C3 | **[NÃO DOCUMENTADO]** |
| P13 | Isolar Linear | R/C4 | **[NÃO DOCUMENTADO]** |
| P14 | Gerar Linear | R/C4 | README; valores **[NÃO DOCUMENTADO]** |
| P15 | Isolar Tree | R/C4 | **[NÃO DOCUMENTADO]** |
| P16 | Gerar Tree | R/C4 | README; valores **[NÃO DOCUMENTADO]** |
| P17 | `iperf -s` em h1 | R/C5 | README |
| P18 | `iperf -c 10.0.0.1` em h2 | R/C5 | README |
