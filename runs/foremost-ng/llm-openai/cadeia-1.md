# Cadeia FN-1 — openai

- provedor: openai
- modelo_exibido: GPT 6.1 Sol (informado de memória por Eduardo em 17/10/2026; o link de compartilhamento do Codex não exibe o modelo; a confirmar por Reinaldo)
- versao: não registrado
- esforco: High (informado de memória por Eduardo em 17/10/2026; a confirmar por Reinaldo)
- interface: Codex (agente com workspace local e terminal), operado por Reinaldo Zimmer Wendt; anexos lidos do disco por caminho em `runs/<artefato>/pacote/` (desvio: agente em vez do chat do ChatGPT)
- data_hora_A: não registrado no link (duração do turno: A=229s; B1=174s)
- data_hora_B1: não registrado no link
- data_hora_B2: pendente
- anexos_A: artigo.pdf=d9b12aa44caeab3d8374fd9ad092c3b9ecec1f18d589125f0ca2f8d00dc9e715, artefato.txt=6de9ecff1194121da658fd3684742c0b2a42b7899ed73b7d3649b9e928330446, instrucoes-oficiais.md=446e5f94605b2fe60ac9c4028f7be57b0488bc79c3c8ef2ef782428f8e290a47, reivindicacoes.md=3d27bc26b64ae7c16272dc9d7a68c25ccacf98d82dbfcdc5bfd7d3ab7932dbac (lidos do disco; bytes não conferidos dentro da conversa)
- anexo_B2: pendente
- metodo_exportacao: transcrição gerada por `ferramentas/transcrever_codex.py` do JSON público do link https://chatgpt.com/s/cx_6ad2372a368c8191829a6aad6848bf07 (cópia bruta em `exportacao-bruta/`); textos de userMessage e agentMessage sem alteração; reasoning, imageView, fileChange e chamadas de ferramenta (não incluídas no link) omitidos. O export anterior, escrito pelo próprio modelo via Session Exporter, está em `exportacao-bruta/` e não é usado na análise
- desvios: resposta A: 1 visualização(ões) de imagem (páginas do artigo.pdf) omitidas | resposta B1: 1 visualização(ões) de imagem (páginas do artigo.pdf) omitidas | turno 3 fora do roteiro, omitido da transcrição: "[@Session Exporter](plugin://session-exporter@openai-curated-remote) Export this entire co"

## Prompt A

Atue como revisor do Comitê de Avaliação de Artefatos do SBSeg 2025. Avalie somente os selos Funcional (F) e Reprodutível (R), seguindo exatamente as instruções oficiais anexadas (instrucoes-oficiais.md).

MATERIAL
Use exclusivamente os arquivos anexados: artigo.pdf (fonte das reivindicações), artefato.txt (o artefato completo na versão bb812a22cb06ef87b5a2d877dfb6f40eb12d460d, em arquivo único: índice de todos os arquivos do repositório e o texto integral de cada arquivo de texto, com o número da linha original), instrucoes-oficiais.md e reivindicacoes.md (lista de reivindicações principais e regra para o selo R). Não navegue na web nem consulte memória, outras conversas, projetos ou conectores. Se precisar de algo que não está nos anexos, registre como evidência ausente.

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

Vou ler os quatro anexos e confrontar os critérios oficiais com as evidências do artigo e do artefato. Tratarei qualquer requisito que dependa de execução como não verificado.

O resumo oficial exige execução para F e confronto dos resultados para R. Já encontrei instruções gerais de instalação e uso no artefato; agora vou verificar se ele também inclui os insumos e passos específicos das reivindicações C1 a C6.

A Figura 2 usa `evidence2.dd`, mas o índice completo do artefato não inclui essa imagem. Isso impede conferir os arquivos e offsets exigidos para C6. Também identifiquei uma possível inconsistência no registro do VirusTotal sem chave; vou tratá-la como risco estático, sem presumir o resultado de uma execução.

## A. Materiais examinados

Abri `artigo.pdf`, `artefato.txt`, `instrucoes-oficiais.md` e `reivindicacoes.md`. Examinei o texto do artigo e a Figura 2, além do índice, README e trechos do código incluídos em `artefato.txt`. Não executei o artefato. O arquivo de instruções se apresenta como **resumo offline**, e não como transcrição literal da página oficial [instrucoes-oficiais.md:Natureza deste arquivo: “não é transcrição literal”].

## B. Selo Funcional (F)

| Critério das instruções anexadas | Estado | Evidência |
|---|---|---|
| O artefato deve ser executável e permitir observar funcionalidades [instrucoes-oficiais.md:Funcional (F): “executável e permitir a observação de funcionalidades”]. | **Só verificável por execução.** | Há instruções de compilação [README.md:31–35: “make”; “sudo make install”], mas elas não demonstram funcionamento. |
| O README deve informar dependências e suas versões, linguagens e ambiente [instrucoes-oficiais.md:Funcional (F): “dependências, versões de dependências/linguagens/ambiente”]. | **Não atendido integralmente.** | O README menciona `curl`, OpenSSL e MinGW conforme a plataforma [README.md:37–68: “Make sure `curl` is installed”; “Install OpenSSL”; “Install MinGW”], mas não especifica versões para o conjunto de dependências e ambiente. O Dockerfile usa base variável [Dockerfile:1: “FROM ubuntu:latest”]. |
| O README deve explicar instalação e execução [instrucoes-oficiais.md:Funcional (F): “instalação, execução”]. | **Atendido na documentação, em nível geral.** | Há passos de instalação por plataforma [README.md:21–68: “Installation”] e sintaxe de chamada [README.md:74–85: “foremost-ng [options] [image_or_device]”]. |
| O README deve conter pelo menos um exemplo mínimo [instrucoes-oficiais.md:Funcional (F): “pelo menos um exemplo mínimo”]. | **Não atendido.** | A seção de uso fornece apenas uma sintaxe com marcadores, sem uma entrada concreta e um comando completo [README.md:82–85: “Basic syntax: foremost-ng [options] [image_or_device]”]. |
| O revisor deve executar e apresentar prova de execução e saídas [instrucoes-oficiais.md:Funcional (F): “executar”; “prova de execução e saídas”]. | **Só verificável por execução.** | O próprio critério ressalva que ler código ou README “não constitui prova de funcionamento” [instrucoes-oficiais.md:Funcional (F)]. |

**Decisão: Não atribuir F.** Faltam requisitos obrigatórios do README, sobretudo versões suficientes e um exemplo mínimo concreto. A execução, mesmo bem-sucedida, não corrigiria por si só essas lacunas documentais. **Confiança de que o comitê oficial atribuiu F: 10/100**; os anexos não contêm sua decisão nem eventuais esclarecimentos posteriores dos autores.

Para mudar a decisão, seria necessário um README corrigido e, na execução, observar instalação bem-sucedida em ambiente identificado, um comando mínimo com entrada real, arquivos recuperados e saídas registradas no parecer.

## C. Selo Reprodutível (R)

As instruções exigem reproduzir as “principais reivindicações do artigo”, documentar sua execução e o processo usado pelos autores, e executar os experimentos comparando os resultados com o artigo [instrucoes-oficiais.md:Reprodutível (R)]. A regra anexa define **C1 a C6** como obrigatórias e pede, em C6, comparação de arquivos e offsets; C7 não integra R [reivindicacoes.md:Regra para o selo R; Critério de reprodução].

| Critério de R | Estado | Evidência |
|---|---|---|
| Instruções no artefato para cada reivindicação e descrição do processo que gerou os resultados publicados [instrucoes-oficiais.md:Reprodutível (R): “instruções de execução dessas reivindicações” e “processo usado pelos autores”]. | **Não atendido.** | O README apresenta sintaxe geral [README.md:74–85] e configuração da chave [README.md:89–107: “VT_API_KEY”], sem roteiro, dados de entrada e resultados esperados para C1 a C6. |
| Reprodução das principais reivindicações [instrucoes-oficiais.md:Reprodutível (R): “reproduzir as principais reivindicações do artigo”]. | **Não atendido no material disponível.** | C2 e C3 apresentam contradições identificáveis no código; falta a imagem específica necessária a C6, conforme detalhado abaixo. |
| Execução e confronto com figuras e tabelas [instrucoes-oficiais.md:Reprodutível (R): “executar os experimentos e confrontar os resultados com os do artigo”]. | **Só verificável por execução.** | A Figura 2 fornece a referência para o confronto [artigo.pdf:p.8, Fig. 2: “`./foremost-ng -v -x evidence2.dd`”], mas não há execução observada nesta avaliação. |

**C1 — EVTX: depende de execução.** O artigo reivindica a assinatura `ElfFile` e chunks de 64 KiB [artigo.pdf:p.6, §3: “ElfFile”; “64 KiB chunks”]. O código registra a assinatura [src/state.c:381–382: `“ElfFile\0\0”`] e calcula `chunk_count * 65536` [src/extract.c:2473–2515]. Isso documenta uma implementação proposta, mas não prova que um `.evtx` recuperado seja legível. Falta no pacote uma entrada de teste identificada e seu resultado esperado [artefato.txt:ÍNDICE].

**C2 — Scripts: não reproduzível como reivindicado, pela análise estática.** A reivindicação exige mais que comentários [artigo.pdf:p.6, §3: “contains more than comments”]. Embora o código imponha 32 bytes [src/extract.c:2521: `MIN_SCRIPT_SIZE = 32`], ele percorre cada caractere após o shebang e aceita o primeiro que não seja `#` nem espaço [src/extract.c:2599–2604: `if (*p != '#') ... found_real = 1`]. Assim, letras dentro de uma linha que começa por `#` podem fazer um script composto apenas de comentários passar pelo filtro. Essa é uma inferência do código, não um resultado de execução.

**C3 — Mach-O `fat` e `thin`: não reproduzível como reivindicado, pela análise estática.** O artigo inclui ambos [artigo.pdf:p.6, §3: “whether fat or thin”]. Para `thin`, o registro procura os bytes `CE FA ED FE` e `CF FA ED FE` [src/state.c:375–379], mas o extrator lê esses bytes como inteiro *little-endian* e compara o valor com as sequências não convertidas [src/extract.c:2359–2364: `read_le32(buf)`; `== 0xCEFAEDFE`; src/extract.c:2408–2409: `== 0xCFFAEDFE`]. A função `read_le32` usa conversão *little-endian* [src/helpers.c:350–355]. Essas comparações não correspondem às assinaturas registradas para `thin`.

**C4 — ELF de 32 e 64 bits: depende de execução.** O artigo prevê delimitação pelos cabeçalhos de programa [artigo.pdf:p.6, §3: “program header table”]. O código contém ramos para as duas classes e calcula limites a partir de segmentos `PT_LOAD` [src/extract.c:2176–2177; src/extract.c:2212–2236; src/extract.c:2240–2253; src/extract.c:2278–2302]. É preciso observar os arquivos extraídos e validá-los com um analisador ELF.

**C5 — VirusTotal: depende de execução e de chave válida.** O README instrui `-x` e `VT_API_KEY` [README.md:89–107]. O código calcula hash, chama a consulta e escreve uma etiqueta no registro [src/dir.c:274–295: `sha_checksum`; `vt_check_hash`; `vt_label`]. Sem chave, a função informa erro [src/vt_query.c:139–143: “VT_API_KEY environment variable is not set”], mas o chamador ainda formata o resultado zerado como `Clean (0)` [src/dir.c:280–282]; isso é um risco de interpretação do registro, não uma observação de execução. Faltam chave e resposta de API nos anexos.

**C6 — Exemplo da Figura 2: não reproduzível com o material fornecido.** A figura usa `evidence2.dd` e apresenta arquivos e offsets para comparação [artigo.pdf:p.8, Fig. 2: “`./foremost-ng -v -x evidence2.dd`”]. O índice declarado como completo contém README, código, capturas de tela e DLLs, mas não `evidence2.dd` [artefato.txt:ÍNDICE: “Conteúdo: todos os arquivos do commit”]. O README tampouco dá um procedimento para obtê-la ou reconstruí-la [README.md:74–107]. Sem essa entrada, não é possível conferir os arquivos e offsets exigidos [reivindicacoes.md:Critério de reprodução: “Em C6, comparam-se os arquivos e offsets da Fig. 2”].

**Decisão: Não atribuir R.** C2 e C3 contradizem partes obrigatórias das reivindicações no código disponível, e falta a entrada indispensável à comparação de C6. Além disso, a documentação não descreve o processo de obtenção dos resultados publicados. **Confiança de que o comitê oficial atribuiu R: 2/100**; não há decisão oficial nos anexos.

Para mudar a decisão, seria necessário corrigir e documentar C2 e C3, fornecer `evidence2.dd` ou um procedimento verificável que produza a mesma entrada, e então observar: EVTX legível (C1); scripts válidos extraídos e arquivos só de comentários rejeitados (C2); Mach-O `fat` e `thin` reconhecíveis (C3); ELF 32/64 estruturalmente legíveis (C4); consulta e registro de detecção associados ao hash, inclusive comportamento sem chave (C5); e arquivos e offsets da Figura 2 (C6). As contagens do VirusTotal podem variar [reivindicacoes.md:Critério de reprodução].

## D. Lacunas e riscos

A ausência de `evidence2.dd`, de entradas de teste para C1 a C5, de chave e resposta do VirusTotal e de um roteiro experimental impede confirmar resultados por documentação [artefato.txt:ÍNDICE; README.md:74–107]. A análise do código aponta falhas específicas em C2 e C3, mas nenhuma conclusão acima afirma que uma execução ocorreu. O artigo também menciona `recovery.log` [artigo.pdf:p.7, §4.2], enquanto o código nomeia `audit.txt` [src/main.h:162: `AUDIT_FILE_NAME "audit.txt"`]; esse nome de saída precisaria ser esclarecido na comparação.

```json
{
  "F": {
    "decisao": "Não atribuir",
    "confianca": 10,
    "evidencias": [
      "instrucoes-oficiais.md:Funcional (F)",
      "README.md:21-85",
      "Dockerfile:1"
    ]
  },
  "R": {
    "decisao": "Não atribuir",
    "confianca": 2,
    "evidencias": [
      "instrucoes-oficiais.md:Reprodutível (R)",
      "reivindicacoes.md:Regra para o selo R",
      "reivindicacoes.md:Critério de reprodução",
      "artigo.pdf:p.8, Fig. 2",
      "artefato.txt:ÍNDICE",
      "src/extract.c:2599-2604",
      "src/state.c:375-379",
      "src/extract.c:2359-2364",
      "src/extract.c:2408-2409"
    ],
    "por_reivindicacao": {
      "C1": "depende_execucao",
      "C2": "nao_reproduzivel",
      "C3": "nao_reproduzivel",
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

Vou montar o roteiro apenas com comandos e expectativas presentes nos quatro anexos. Onde faltar arquivo de entrada, comando ou validação descrita pelos autores, vou marcar [NÃO DOCUMENTADO] e indicar o ponto em que a execução deve parar.

# Roteiro de execução para F e R

**Este é um roteiro, não um relato de execução.** Usei somente `artigo.pdf`, `artefato.txt`, `instrucoes-oficiais.md` e `reivindicacoes.md`. Os comandos abaixo são reproduzidos do README ou do artigo. `[NÃO DOCUMENTADO]` identifica um comando, insumo ou procedimento que os autores não forneceram; não há comando substituto presumido.

**Interrupção inicial:** o anexo `artefato.txt` contém o texto dos arquivos e um índice de binários, mas não é a árvore executável nem o `artefato.zip` do qual foi gerado [artefato.txt:cabeçalho e ÍNDICE]. O README manda abrir um `.tar.gz`, cujo nome concreto não é dado [README.md:23–28]. Assim, **P1–P2 não podem ser concluídos com os anexos atuais**. O restante do roteiro é condicional ao recebimento do artefato executável da revisão indicada.

## Ambiente e tempo

| Requisito | Informação fornecida pelos autores |
|---|---|
| Hardware: CPU, RAM e espaço livre | **[NÃO DOCUMENTADO]**. São necessários para dimensionar a compilação, as imagens e os arquivos extraídos; a Figura 2 apenas mostra uma entrada de 2.845.109.643 bytes [artigo.pdf:p.8, Fig. 2]. |
| Sistema e compilação | Ferramenta descrita como baseada em Linux [README.md:3]. Para Linux: `make` e `sudo make install` [README.md:31–35]. O artigo menciona GCC [artigo.pdf:p.6, §4]. |
| Bibliotecas e versões | O Dockerfile relaciona `gcc`, `make`, `git`, `libssl-dev` e `libcurl4-openssl-dev`, sem fixar versões [Dockerfile:1–6]. As versões completas do ambiente são **[NÃO DOCUMENTADO]**, necessárias para repetir a compilação. |
| VirusTotal | `-x`, chave válida em `VT_API_KEY` e acesso à API [README.md:89–107; artigo.pdf:p.7, §4.1]. A chave não acompanha os anexos. |
| Entradas | `disk.img`, `memory.dump` e `evidence2.dd` aparecem nos comandos do artigo, mas não constam do índice do artefato [artigo.pdf:p.7–8; artefato.txt:ÍNDICE]. Sua obtenção e conteúdo são **[NÃO DOCUMENTADO]**. |

**Tempo estimado:** **[NÃO DOCUMENTADO] pelos autores e não quantificável com os anexos.** Faltam especificações do computador, as imagens de entrada e tempos de referência. Registre início e fim de cada execução; o tempo de consulta ao VirusTotal também dependerá da API. Uma duração numérica agora seria especulativa.

Os critérios de registro seguem as instruções anexadas: F requer execução e prova das saídas; R requer confronto das reivindicações principais com o artigo [instrucoes-oficiais.md:Funcional (F); Reprodutível (R)]. **Salvar a sessão do terminal e os resultados é uma exigência da avaliação; o método ou comando de captura é [NÃO DOCUMENTADO] pelos autores.**

## Preparação e teste mínimo de F

### P1 — Conferir o material de entrada

- **Selo/reivindicação:** F e R; pré-requisito de C1–C6.
- **Diretório:** local em que o pacote executável da revisão `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` for entregue — **[NÃO DOCUMENTADO]**.
- **Comando exato:** **[NÃO DOCUMENTADO]** para conferir revisão e integridade. A conferência é necessária para não testar outra versão. `artefato.txt` informa um SHA-256 para `artefato.zip`, mas o ZIP não foi anexado [artefato.txt:cabeçalho].
- **Resultado esperado:** fonte e binários necessários disponíveis na revisão indicada.
- **Evidência a salvar:** identificação do pacote recebido, sua revisão e a lista de entradas disponíveis.
- **Sucesso:** pacote da revisão indicada e entradas identificadas.
- **Falha:** pacote comprovadamente de outra revisão.
- **Interrupção:** pacote ausente ou revisão impossível de confirmar. **Esta é a situação dos anexos atuais.**

### P2 — Descompactar e entrar no código

- **Selo/reivindicação:** F e R; pré-requisito.
- **Diretório:** onde estiver o arquivo de distribuição.
- **Comandos exatos do README:**
  ```bash
  tar xzvf foremost-ng-<version>.tar.gz
  cd foremost-ng-<version>/src
  ```
  [README.md:23–28]. `<version>` é um marcador dos autores, não um nome de arquivo pronto para executar.
- **Resultado esperado:** diretório `src` com o `Makefile` e o código [artefato.txt:ÍNDICE].
- **Evidência a salvar:** saída da descompactação e identificação da árvore obtida.
- **Sucesso:** os comandos levam ao `src` da revisão de P1.
- **Falha:** erro de descompactação ou ausência de `src/Makefile` num pacote comprovadamente correto.
- **Interrupção:** não há `.tar.gz` correspondente. Converter o `artefato.txt` em árvore de arquivos ou abrir o ZIP mencionado nele é **[NÃO DOCUMENTADO]** pelos autores; esse procedimento seria necessário antes de P3.

### P3 — Compilar e instalar

- **Selo/reivindicação:** F e R; pré-requisito.
- **Diretório:** `foremost-ng-<version>/src`.
- **Comandos exatos para Linux:**
  ```bash
  make
  sudo make install
  ```
  [README.md:31–35].
- **Resultado esperado:** binário `foremost-ng` disponível no sistema [artigo.pdf:p.7, §4].
- **Evidência a salvar:** saída completa dos dois comandos, mensagens de erro e versão do ambiente. O comando para registrar versões é **[NÃO DOCUMENTADO]**; isso é necessário para avaliar a repetibilidade.
- **Sucesso:** compilação e instalação terminam sem erro e disponibilizam o binário.
- **Falha:** erro de compilação ou instalação no ambiente com dependências satisfeitas.
- **Interrupção:** dependência ausente, permissão de instalação indisponível ou versão do ambiente impossível de estabelecer; os autores não dão um procedimento completo de preparação com versões fixas.

### P4 — Teste mínimo de F e execução comum a C1–C4

- **Selo/reivindicação:** F; a mesma execução pode fornecer dados para R/C1–C4.
- **Diretório:** diretório que contenha `disk.img` — **[NÃO DOCUMENTADO]** pelos autores.
- **Comando exato do artigo:**
  ```bash
  foremost-ng -i disk.img -o /temp/output/carved
  ```
  [artigo.pdf:p.7, §4.1].
- **Resultado esperado:** varredura de todos os parsers registrados, subdiretórios por formato e arquivos recuperados [artigo.pdf:p.7, §4.1–4.2].
- **Evidência a salvar:** sessão do terminal, diretório de saída, arquivos recuperados e registro de extrações. O artigo alterna entre `audit.txt` [artigo.pdf:p.6–7] e `recovery.log` [artigo.pdf:p.7, §4.2]; salve o registro efetivamente produzido.
- **Sucesso:** comando termina e permite observar ao menos uma recuperação verificável em uma imagem sabidamente contendo arquivo recuperável.
- **Falha:** erro do programa ou ausência de recuperação **quando a entrada tiver conteúdo recuperável previamente conhecido**.
- **Interrupção:** `disk.img` ausente ou conteúdo desconhecido. Sua obtenção e preparação são **[NÃO DOCUMENTADO]**; sem elas, saída vazia não demonstra falha de F. O comportamento ao reutilizar `/temp/output/carved` também é **[NÃO DOCUMENTADO]**: não repita P4 nesse mesmo destino sem esclarecer isso.

## Verificações de R por reivindicação

P5–P8 **avaliam a saída da única execução P4**; o comando é exibido para identificar sua origem, não para mandar executá-lo novamente. C1–C6 são as reivindicações obrigatórias para R [reivindicacoes.md:Regra para o selo R]. C7 fica fora dessa regra.

### P5 — C1: EVTX

- **Selo/reivindicação:** R/C1.
- **Diretório:** `/temp/output/carved`, saída de P4.
- **Comando exato que gerou a saída:** `foremost-ng -i disk.img -o /temp/output/carved` [artigo.pdf:p.7, §4.1]. **[NÃO DOCUMENTADO]**: comando e ferramenta para validar o EVTX; o artigo diz apenas “standard event log tools” [artigo.pdf:p.6, §3].
- **Resultado esperado:** `.evtx` extraído, reconhecido pela assinatura `ElfFile`, delimitado em chunks de 64 KiB e legível [artigo.pdf:p.6, §3; reivindicacoes.md:C1].
- **Evidência a salvar:** arquivo extraído, offset e registro da extração; resultado da leitura por ferramenta apropriada, se essa validação for definida.
- **Sucesso:** EVTX íntegro e legível, correspondente a uma entrada EVTX conhecida.
- **Falha:** entrada EVTX conhecida não recuperada ou saída ilegível.
- **Interrupção:** entrada EVTX não identificada em `disk.img`, ou ausência de procedimento/ferramenta de validação.

### P6 — C2: scripts

- **Selo/reivindicação:** R/C2.
- **Diretório:** `/temp/output/carved`, saída de P4.
- **Comando exato que gerou a saída:** `foremost-ng -i disk.img -o /temp/output/carved`. **[NÃO DOCUMENTADO]**: geração ou seleção de exemplos Bash, Python e PowerShell e de um controle só com comentários.
- **Resultado esperado:** scripts com shebang, ao menos 32 bytes, corpo legível além de comentários [artigo.pdf:p.6, §3; reivindicacoes.md:C2].
- **Evidência a salvar:** scripts extraídos, seus offsets e comparação com as entradas conhecidas.
- **Sucesso:** os casos válidos são extraídos com conteúdo legível e o caso composto só de comentários não é aceito.
- **Falha:** caso válido ausente, truncado ou caso só com comentários aceito.
- **Interrupção:** `disk.img` não contém casos conhecidos; não há conjunto de testes dos autores nos anexos. A verificação negativa é especialmente necessária porque a leitura do código apontou risco nesse filtro [src/extract.c:2599–2604].

### P7 — C3: Mach-O

- **Selo/reivindicação:** R/C3.
- **Diretório:** `/temp/output/carved`, saída de P4.
- **Comando exato que gerou a saída:** `foremost-ng -i disk.img -o /temp/output/carved`. **[NÃO DOCUMENTADO]**: ferramenta/comando para reconhecer a estrutura Mach-O e obtenção de entradas `fat` e `thin`.
- **Resultado esperado:** binários dos dois tipos extraídos e reconhecíveis [artigo.pdf:p.6, §3; reivindicacoes.md:C3].
- **Evidência a salvar:** arquivos `fat` e `thin`, offsets, tamanhos e resultado de validação estrutural.
- **Sucesso:** ambos os tipos são recuperados e reconhecidos.
- **Falha:** um tipo conhecido não é recuperado ou a saída é estruturalmente inválida.
- **Interrupção:** ausência de amostras conhecidas ou de procedimento de validação. O caso `thin` precisa constar da entrada, dada a divergência identificada entre assinatura e comparação no código [src/state.c:375–379; src/extract.c:2359–2364, 2408–2409].

### P8 — C4: ELF

- **Selo/reivindicação:** R/C4.
- **Diretório:** `/temp/output/carved`, saída de P4.
- **Comando exato que gerou a saída:** `foremost-ng -i disk.img -o /temp/output/carved`. **[NÃO DOCUMENTADO]**: ferramenta/comando de análise estrutural ELF e obtenção de amostras de 32 e 64 bits.
- **Resultado esperado:** `.elf` extraídos, delimitados pelos cabeçalhos de programa e legíveis por analisador ELF [artigo.pdf:p.6, §3; reivindicacoes.md:C4].
- **Evidência a salvar:** arquivos de ambas as classes, offsets, tamanhos e validação estrutural.
- **Sucesso:** ELF32 e ELF64 conhecidos são recuperados e estruturalmente legíveis.
- **Falha:** classe conhecida ausente, truncada ou inválida.
- **Interrupção:** a entrada não contém as duas classes conhecidas ou falta procedimento de validação.

### P9 — C5: configurar e verificar VirusTotal com chave

- **Selo/reivindicação:** R/C5.
- **Diretório:** para o primeiro comando, sessão de shell Unix; para o segundo, diretório que contenha `memory.dump` — **[NÃO DOCUMENTADO]**.
- **Comandos exatos dos autores:**
  ```bash
  export VT_API_KEY=yourkey
  foremost-ng -x -t elf -i memory.dump -o ./carved-files
  ```
  [README.md:99–102; artigo.pdf:p.7, §4.1]. `yourkey` exige substituição por chave válida obtida pelo usuário.
- **Resultado esperado:** hash de cada ELF recuperado consultado no VirusTotal e contagens de detecções registradas [artigo.pdf:p.7, §4.1; reivindicacoes.md:C5].
- **Evidência a salvar:** saída do terminal, `.elf`, hash associado, registro e coluna/etiqueta VT; proteja a chave ao salvar o terminal.
- **Sucesso:** consulta associada ao hash de cada arquivo recuperado e resultado de detecção registrado.
- **Falha:** com chave válida e serviço disponível, falta consulta ou a detecção não corresponde ao arquivo.
- **Interrupção:** `memory.dump`, chave ou serviço indisponível. **[NÃO DOCUMENTADO]**: imagem concreta, chave de teste, comando de conferência independente do hash e procedimento para distinguir erro de API de resultado limpo.

### P10 — C5: comportamento sem chave

- **Selo/reivindicação:** R/C5.
- **Diretório:** onde estiver `memory.dump`; use saída ainda não ocupada, mas a preparação desse destino é **[NÃO DOCUMENTADO]**.
- **Comando exato:** o artigo fornece `foremost-ng -x -t elf -i memory.dump -o ./carved-files`. **[NÃO DOCUMENTADO]**: comando para remover `VT_API_KEY` da sessão e procedimento para repetir a execução sem colidir com a saída de P9.
- **Resultado esperado:** aviso, carving preservado e nenhuma consulta VT [artigo.pdf:p.7, §4.1].
- **Evidência a salvar:** aviso, arquivos recuperados, registro e ausência de resultado de consulta.
- **Sucesso:** o comportamento sem chave corresponde aos três pontos esperados.
- **Falha:** carving cessa, falta aviso ou um resultado de detecção é apresentado como se tivesse sido consultado.
- **Interrupção:** não é possível estabelecer comprovadamente uma sessão sem chave ou uma saída independente usando procedimentos dos autores.

### P11 — C6: repetir a Figura 2

- **Selo/reivindicação:** R/C6.
- **Diretório:** `src/` com binário local `./foremost-ng` e `evidence2.dd` no mesmo diretório, como aparece na figura [artigo.pdf:p.8, Fig. 2].
- **Comando exato da figura:**
  ```bash
  ./foremost-ng -v -x evidence2.dd
  ```
- **Resultado esperado:** tabela com **3 ELF, 1 script, 6 EXE e 2 ZIP** e os respectivos offsets. A Figura 2 mostra, por exemplo, ELF nos offsets `2228224`, `2467840` e `2615296`; script em `2811904`; EXE em `204740608`, `207390720`, `212445184`, `219508736`, `226570240` e `229046272`; ZIP em `914484119` e `914965615` [artigo.pdf:p.8, Fig. 2]. A coluna VT aparece na figura, mas suas contagens atuais não precisam coincidir [reivindicacoes.md:Critério de reprodução].
- **Evidência a salvar:** saída completa, registro, tabela de nomes, tipos e offsets, arquivos recuperados e comparação linha a linha com a figura.
- **Sucesso:** arquivos e offsets da figura são reproduzidos; divergências nas contagens VT são anotadas separadamente.
- **Falha:** com a **mesma** `evidence2.dd` comprovada, arquivos ou offsets divergem.
- **Interrupção:** `evidence2.dd` ausente, identidade da imagem impossível de confirmar ou chave/API indisponível para avaliar a coluna VT. Sua obtenção é **[NÃO DOCUMENTADO]**; a imagem não está no índice do artefato [artefato.txt:ÍNDICE]. Portanto, P11 não pode ser realizado com os anexos atuais.

## Resumo dos passos

| Passo | Selo/reivindicação | Comando dos autores ou lacuna principal | Condição para avançar |
|---|---|---|---|
| P1 | F/R, preparação | **[NÃO DOCUMENTADO]** conferência da revisão | Pacote executável correto recebido |
| P2 | F/R, preparação | `tar xzvf foremost-ng-<version>.tar.gz`; `cd foremost-ng-<version>/src` | Arquivo real correspondente disponível |
| P3 | F/R, instalação | `make`; `sudo make install` | Binário disponível sem erro |
| P4 | F; execução comum | `foremost-ng -i disk.img -o /temp/output/carved` | `disk.img` conhecida e saída observável |
| P5 | R/C1 | Saída de P4; validação EVTX **[NÃO DOCUMENTADO]** | EVTX conhecido e ferramenta de leitura definidos |
| P6 | R/C2 | Saída de P4; casos de script **[NÃO DOCUMENTADO]** | Casos válidos e só com comentários disponíveis |
| P7 | R/C3 | Saída de P4; casos Mach-O **[NÃO DOCUMENTADO]** | Amostras `fat` e `thin` conhecidas |
| P8 | R/C4 | Saída de P4; análise ELF **[NÃO DOCUMENTADO]** | ELF32 e ELF64 conhecidos |
| P9 | R/C5 | `export VT_API_KEY=yourkey`; comando `-x -t elf` do artigo | `memory.dump`, chave e API disponíveis |
| P10 | R/C5 | Remoção da chave e repetição segura **[NÃO DOCUMENTADO]** | Sessão sem chave comprovada |
| P11 | R/C6 | `./foremost-ng -v -x evidence2.dd` | A mesma `evidence2.dd` da figura disponível |

**Estado do roteiro com o material atual:** interromper em **P1**. Isso registra ausência de insumos; não constitui teste executado nem resultado negativo de funcionamento.
