# Cadeia FN-1 — anthropic

- provedor: anthropic
- modelo_exibido: Opus 5.5 Médio
- versao: claude-opus-5-5 (campo model da API do claude.ai)
- esforco: effort_level=medium; thinking_mode=auto
- interface: claude.ai (web) no Google Chrome, operado pelo agente Claude Code pela extensão Claude in Chrome com autorização do aluno; chat avulso com anexos; memória pausada; busca na web indisponível
- data_hora_A: 2026-10-15 23:13 BRT
- data_hora_B1: 2026-10-15 23:16 BRT
- data_hora_B2: pendente
- anexos_A: artigo.pdf=d9b12aa44caeab3d8374fd9ad092c3b9ecec1f18d589125f0ca2f8d00dc9e715, artefato.txt=6de9ecff1194121da658fd3684742c0b2a42b7899ed73b7d3649b9e928330446, instrucoes-oficiais.md=446e5f94605b2fe60ac9c4028f7be57b0488bc79c3c8ef2ef782428f8e290a47, reivindicacoes.md=3d27bc26b64ae7c16272dc9d7a68c25ccacf98d82dbfcdc5bfd7d3ab7932dbac
- anexo_B2: pendente
- metodo_exportacao: transcrição gerada da API do claude.ai (conversa adeeb21b-6f25-490a-9c41-f2f93f52efa8, https://claude.ai/chat/adeeb21b-6f25-490a-9c41-f2f93f52efa8); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos; o original permanece na conta
- desvios: resposta A usou 8 chamada(s) de ferramenta do claude.ai: bash_tool ("Inspect artifact file"); bash_tool ("Read README and Makefile"); bash_tool ("Locate files and key features"); bash_tool ("ELF and main.c"); bash_tool ("Check data, dir.c VT and vt_query.c"); bash_tool ("Read ELF/Mach-O/EVTX/script parsers"); bash_tool ("Builtin registry in state.c"); bash_tool ("Config defaults") | resposta A contém raciocínio (thinking) exibido pela interface, omitido nesta transcrição | resposta B1 usou 25 chamada(s) de ferramenta do claude.ai: view ("Read docs skill before creating the runbook"); Claude Docs:guide (""); Claude Docs:batch (""); Artifact (""); Claude Docs:guide (""); bash_tool ("Check Fig. 2 offsets vs names"); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); Claude Docs:update (""); tool_search (""); Claude Docs:read (""); Claude Docs:update ("") | resposta B1 contém raciocínio (thinking) exibido pela interface, omitido nesta transcrição | resposta B1 entregou o roteiro como documento do Claude Docs (https://claude.ai/code/artifact/a46da080-a8cd-45db-a001-65818b35a151), salvo sem alteração pela função "Copiar como Markdown" do claude.ai em `anexos-saida/cadeia-1-B1-documento.md`

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

Vou abrir o artefato para examinar o conteúdo.

# Parecer analítico: Foremost-NG (SBSeg 2025), selos F e R

Esta é uma avaliação analítica. Não executei o artefato e nada abaixo afirma que algo funcionou.

## A. Materiais examinados

- **`instrucoes-oficiais.md`**: lido na íntegra.
- **`reivindicacoes.md`**: lido na íntegra.
- **`artigo.pdf`**: lido na íntegra, pp. 1–8, incluindo a imagem da Fig. 2.
- **`artefato.txt`**: aberto pelo terminal. Li o índice, `README.md`, `Dockerfile`, `src/Makefile`, `src/main.c`, `src/dir.c` (função `write_to_disk`), `src/vt_query.c`, `src/extract.c` (`extract_elf`, `extract_macho`, `extract_evtx`, `extract_script` e o despachante `extract_file`), `src/state.c` (registro de parsers, linhas 327–403 e 637–707) e `src/config.c` (`load_config_file`). Nos demais arquivos fiz apenas buscas por palavra-chave.
- **Arquivos binários não inspecionáveis**: aparecem só no índice e ficam registrados como evidência ausente. São eles `screenshots/foremost-ng-01.png`, `screenshots/foremost-ng-02.png`, `src/foremost-ng.8.gz` (página de manual) e `windows_dlls/*`.

Citações de código usam a numeração original do arquivo, como `artefato.txt` recomenda.

## B. Selo Funcional (F)

**Critérios oficiais aplicáveis** [instrucoes-oficiais.md:Funcional (F)]:
- F1: "O artefato precisa ser executável e permitir a observação de funcionalidades."
- F2: "O README deve informar dependências, versões de dependências/linguagens/ambiente, ambiente de execução, instalação, execução e pelo menos um exemplo mínimo."
- F3: "O revisor deve executar o artefato e apresentar prova de execução e saídas no parecer. Ler código ou README, por si só, não constitui prova de funcionamento."

**Avaliação por critério**

| Critério | Situação | Evidência |
|---|---|---|
| F2a: dependências | **Não atendido** no README | A seção de Linux traz só `make` e `sudo make install` [README.md:31–35]. As bibliotecas exigidas aparecem apenas no Makefile, `LINK_OPT += -lssl -lcrypto -lcurl` [src/Makefile:46], e no Dockerfile, `gcc make git libssl-dev libcurl4-openssl-dev` [Dockerfile:5]. O README não lista OpenSSL nem libcurl para Linux. Só menciona curl para BSD [README.md:39] e OpenSSL para macOS [README.md:52–54]. |
| F2b: versões | **Não atendido** | Não há versão de compilador, OpenSSL, libcurl nem distribuição. O Dockerfile usa `FROM ubuntu:latest` [Dockerfile:1], sem fixar versão, e clona o HEAD do GitHub, não o commit avaliado: `RUN git clone https://github.com/cristianzsh/foremost-ng.git` [Dockerfile:8]. |
| F2c: ambiente | Parcial | "`foremost-ng` is a Linux-based file recovery tool" [README.md:3], com seções para BSD, macOS e Windows [README.md:37–68]. |
| F2d: instalação | Atendido, com ressalva | "`cd foremost-ng-<version>/src` … `make` / `sudo make install`" [README.md:28–34]. Há uma inconsistência com o artigo: ele manda `cd foremost-ng` e `make` na raiz [artigo.pdf:p. 6, §4], mas o índice só tem `src/Makefile` [artefato.txt:índice]. |
| F2e: execução | Parcial | Há apenas a sintaxe geral, "`foremost-ng [options] [image_or_device]`" [README.md:84], e a remissão a `man foremost-ng` [README.md:79]. A página de manual é binária e não pôde ser inspecionada. |
| F2f: exemplo mínimo | **Não atendido** | O README não traz comando concreto, dado de entrada nem saída esperada [README.md:74–85]. O artefato não contém imagem de teste: o índice não lista nenhum `.dd`/`.img`. |
| F1: executável e funcionalidades observáveis | Só verificável por execução | O código é coerente com uma CLI funcional, com opções em `getopt(argc, argv, "o:b:c:t:s:i:k:hqmQTadvVwx")` [src/main.c:121] e escrita de arquivos e de `audit.txt` [src/dir.c:239–295; src/main.h:162]. Isso é leitura de código, não prova de funcionamento. |
| F3: prova de execução | Só verificável por execução | Não executei. As capturas de tela do README estão em binário omitido. |

**Decisão para F: Não atribuir.** Um critério documental obrigatório falha: o README não informa dependências nem versões e não traz exemplo mínimo executável [README.md:21–85]. Pela regra fornecida, isso basta, mesmo que a compilação e a execução tendam a funcionar.

**Confiança de que o comitê atribuiu F: 50/100.** As lacunas são de documentação. Um revisor que compile via Dockerfile e rode sobre uma imagem qualquer provavelmente observaria funcionamento. Comitês costumam aceitar isso, sobretudo depois da resposta dos autores.

**O que mudaria a decisão**:
- Os autores corrigirem o README (lista de pacotes e versões, um comando de exemplo e uma imagem pequena de teste). Isso transformaria a situação em Indeterminado.
- Em seguida, a execução precisaria mostrar compilação sem erro, `foremost-ng -h`, uma execução sobre imagem de teste com subdiretórios por formato e `audit.txt` preenchido.

## C. Selo Reprodutível (R)

**Critérios oficiais aplicáveis** [instrucoes-oficiais.md:Reprodutível (R)]:
- R1: "O revisor deve conseguir reproduzir as principais reivindicações do artigo."
- R2: "A documentação do artefato deve trazer instruções de execução dessas reivindicações e descrever o processo usado pelos autores para chegar aos resultados publicados."
- R3: "O revisor deve executar os experimentos e confrontar os resultados com os do artigo, incluindo figuras/tabelas pertinentes."
- Regra de R: "R é atribuído se C1 a C6 forem reproduzidas" [reivindicacoes.md:Regra para o selo R].

**R2 está não atendido de forma transversal.** O README não descreve nenhum experimento, conjunto de dados ou processo dos autores, e não cita as reivindicações [README.md:1–119]. Os novos formatos (EVTX, script, Mach-O, ELF) nem aparecem em "Features" [README.md:11–17]. A ajuda da CLI só exemplifica "`-t  Specify file type (e.g., jpeg,pdf)`" [src/main.c:101]. O artigo aponta amostras externas, "Carving test samples can be downloaded from https://dftt.sourceforge.net" [artigo.pdf:p. 7], mas o artefato não as inclui nem diz quais usar.

**C1: EVTX.** Classificação: depende de execução.
- O parser existe e procura a assinatura: `if (memcmp(buf, "ElfFile\0\0", 8) != 0)` [src/extract.c:2474].
- Ele lê o número de chunks e o multiplica por 64 KiB: `chunk_count = htoi(&buf[0x18], …)` e `full_size = (uint64_t)chunk_count * 65536ULL` [src/extract.c:2479, 2489].
- O formato está registrado como `"evtx", "ElfFile\0\0"` [src/state.c:381].
- Não há `.evtx` de teste no artefato, e a Fig. 2 não mostra nenhum EVTX.
- Risco técnico: pelo que sei do formato EVTX, o número de chunks fica em outro deslocamento do cabeçalho, e o cabeçalho de 4 KiB não entra na conta. Isso é conhecimento externo aos anexos, então não o uso como evidência. Ainda assim, pode produzir arquivos de tamanho incorreto. A execução precisa confirmar que o `.evtx` extraído abre em ferramenta de eventos.

**C2: Scripts.** Classificação: depende de execução.
- O mínimo de 32 bytes está no código: `const uint64_t MIN_SCRIPT_SIZE = 32;` [src/extract.c:2521].
- O parser recusa scripts que só têm comentários: `// No real content after the shebang‐line: skip carve` [src/extract.c:2611].
- O shebang está registrado: `"script", "#!"` [src/state.c:384].
- Faltam dados de teste no artefato. A Fig. 2 mostra um `00005492.script` [artigo.pdf:p. 8], mas a imagem de origem não acompanha o artefato.

**C3: Mach-O fat/thin.** Classificação: depende de execução.
- Fat: `// FAT magic (always big-endian on disk) = 0xCA FE BA BE` [src/extract.c:2326], com cálculo de deslocamento e tamanho por arquitetura [src/extract.c:2342–2344].
- Thin 32 e 64 bits pelos comandos de carga: `if (cmd == 0x19 /* LC_SEGMENT_64 */)` [src/extract.c:2433].
- As três assinaturas estão registradas [src/state.c:372–379].
- Não há amostra Mach-O no artefato nem na Fig. 2.
- Risco: a assinatura `CAFEBABE` também aparece em outros formatos, o que pode gerar falsos positivos. Isso só a execução mostra.

**C4: ELF 32/64.** Classificação: depende de execução.
- O parser distingue as classes, `if (ei_class == 1)` e `else if (ei_class == 2)` [src/extract.c:2176, 2240], e delimita o arquivo pelos `PT_LOAD` [src/extract.c:2213, 2279].
- Ele aceita apenas little-endian: `// If not LE, skip.` [src/extract.c:2171].
- Risco: o arquivo termina no fim do último segmento carregável [src/extract.c:2228–2232]. A tabela de seções pode ficar fora do arquivo extraído. O artigo afirma que o ELF extraído "retains the correct executable layout and symbol information" [artigo.pdf:p. 6]. A execução precisa verificar com um analisador ELF.

**C5: VirusTotal.** Classificação: depende de execução, e exige chave de API, um recurso externo.
- A opção existe: `case 'x': set_mode(s, mode_virustotal);` [src/main.c:131].
- O hash é calculado sobre o arquivo gravado, `sha_checksum(fn, "sha256", sha256); vt = vt_check_hash(sha256);` [src/dir.c:278–279], e o rótulo vai para o audit [src/dir.c:280–295].
- A chave vem do ambiente, `getenv("VT_API_KEY")` [src/vt_query.c:38], e a URL é `"https://www.virustotal.com/api/v3/files/"` [src/vt_query.c:21].
- O README documenta a chave [README.md:89–108].

Há três divergências documentais:
- **Sem chave.** O código imprime o erro a cada arquivo e retorna zeros [src/vt_query.c:140–142]. O rótulo vira então "Clean (0)" [src/dir.c:281], o que se confunde com um resultado real. O artigo diz que a ferramenta "will emit a warning and skip all VT lookups" [artigo.pdf:p. 7]. A consulta de fato não ocorre, mas o registro engana.
- **Hash não registrado.** O artigo promete "A recovery.log summarizing each extraction with byte offsets, hash values" [artigo.pdf:p. 7, §4.2]. O código não tem `recovery.log`: a busca no artefato não encontra a string. A linha do audit também não grava o hash [src/dir.c:292–295]. Para conferir a associação hash–arquivo, o revisor precisa recalcular o hash.
- **Leitura frágil do JSON.** A extração usa `sscanf` com formato rígido: `"\"last_analysis_stats\": {\"malicious\": %d, \"suspicious\": %*d, \"undetected\": %d"` [src/vt_query.c:180]. Se a resposta tiver outra ordem ou outra formatação, a contagem não é lida.

**C6: Fig. 2 (`./foremost-ng -v -x evidence2.dd`).** Classificação: **não reproduzível**.
- A entrada `evidence2.dd`, de "2 GB (2845109643 bytes)" [artigo.pdf:p. 8, Fig. 2], não está no artefato. O índice não traz nenhuma imagem de disco [artefato.txt:índice].
- O README não indica onde obtê-la, e `reivindicacoes.md` registra "O README indica como reproduzir?: não".
- Falta, portanto, o dado necessário para comparar arquivos e offsets.
- Há uma checagem de coerência que não substitui reprodução. Os nomes da Fig. 2 seguem a regra do código, `blk = t_off / s->block_size` [src/dir.c:214]: por exemplo, 2228224 / 512 = 4352, que corresponde a `00004352.elf`. A versão "1.5.7" na figura coincide com `VERSION = 1.5.7` [src/Makefile:4].

**C7: arquitetura extensível** (fora da regra de R, inspecionada). O despachante é uma cadeia `if/else` por tipo [src/extract.c:2628–2697]. Um novo parser exige editar `main.h` [src/main.h:193–201], `state.c` em dois pontos [src/state.c:369–385, 672–697] e `extract_file`. Isso contradiz o artigo, que diz que a mudança "does not require modifying the dispatcher logic itself" [artigo.pdf:p. 3].

**Decisão para R: Não atribuir.**
- C6 falha por ausência do dado necessário.
- R2 falha porque a documentação não traz instruções das reivindicações nem descreve o processo dos autores.
- Mesmo que C1 a C5 fossem confirmadas por execução, a regra exige C1 a C6.

**Confiança de que o comitê atribuiu R: 15/100.** Sem a imagem da Fig. 2 e sem um roteiro de reprodução, é improvável que o comitê tenha concedido o selo. A única ressalva é a hipótese de os autores terem fornecido os dados na fase de resposta, o que não consta dos anexos.

**O que mudaria a decisão**:
- Os autores disponibilizarem `evidence2.dd` (ou outra imagem equivalente documentada) e um roteiro por reivindicação.
- Na execução, observar:
  - os mesmos arquivos e offsets da Fig. 2;
  - um `.evtx` extraído que abra em ferramenta de eventos;
  - um script extraído com a linha do interpretador;
  - Mach-O fat e thin reconhecidos por `file`/`otool`;
  - ELF 32 e 64 bits legíveis por `readelf`;
  - com chave de API, rótulos coerentes com uma consulta manual pelo SHA-256 de cada arquivo;
  - sem chave, o aviso e nenhuma requisição.

## D. Lacunas e riscos

**Evidências ausentes**:
- A imagem `evidence2.dd`.
- Qualquer amostra de teste (EVTX, Mach-O, ELF, script).
- A página de manual (`foremost-ng.8.gz`) e as capturas do README, que são binárias e não puderam ser inspecionadas.
- A decisão oficial e a resposta dos autores, que não estão nos anexos.

**Riscos de execução**:
- O Dockerfile não constrói o commit avaliado, porque clona o HEAD [Dockerfile:8], e usa `ubuntu:latest` [Dockerfile:1].
- O artigo manda rodar `make` na raiz [artigo.pdf:p. 6], mas não há Makefile na raiz.
- A verificação TLS está desligada, `CURLOPT_SSL_VERIFYPEER, 0L` [src/vt_query.c:167]. O artigo declara isso [artigo.pdf:p. 3], mas é um risco de segurança da integração.
- Os resultados do VirusTotal mudam com o tempo e dependem de cota da API, como `reivindicacoes.md` já reconhece.
- Os riscos técnicos de C1 e C4 (deslocamento do número de chunks do EVTX, ELF truncado antes da tabela de seções) vêm de conhecimento externo aos anexos. Por isso não pesaram na decisão, mas precisam ser verificados em execução.

**Divergências artigo × código**: `recovery.log` com hashes não existe; "SHA-256 (or SHA-1)" no código é só SHA-256 [src/dir.c:278]; a arquitetura não é extensível sem mexer no despachante (C7).

```json
{"F": {"decisao": "Não atribuir", "confianca": 50, "evidencias": ["artefato.txt:README.md:31-35", "artefato.txt:README.md:74-85", "artefato.txt:Dockerfile:1", "artefato.txt:Dockerfile:5", "artefato.txt:Dockerfile:8", "artefato.txt:src/Makefile:46", "artefato.txt:src/main.c:121", "artefato.txt:índice (sem dados de teste)", "artigo.pdf:p. 6, §4"]},
 "R": {"decisao": "Não atribuir", "confianca": 15, "evidencias": ["artefato.txt:README.md:1-119", "artefato.txt:índice (evidence2.dd ausente)", "artigo.pdf:p. 8, Fig. 2", "artigo.pdf:p. 7, §4.2", "artefato.txt:src/extract.c:2474-2489", "artefato.txt:src/extract.c:2521-2611", "artefato.txt:src/extract.c:2326-2433", "artefato.txt:src/extract.c:2171-2232", "artefato.txt:src/dir.c:214", "artefato.txt:src/dir.c:278-295", "artefato.txt:src/vt_query.c:140-142", "artefato.txt:src/vt_query.c:180", "artefato.txt:src/extract.c:2628-2697", "reivindicacoes.md:Regra para o selo R"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "depende_execucao", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

Esqueleto do roteiro criado; agora preencho as seções, começando pelo escopo.

Agora o escopo e as convenções.

Agora os requisitos do ambiente.

Agora a preparação (P1–P8).

Agora o teste mínimo de F (P9–P13).

Agora a montagem da imagem de teste para C1–C4 (P14–P17).

Agora o bloco de C1 (EVTX).

Agora o bloco de C2 (scripts).

Agora o bloco de C3 (Mach-O).

Agora o bloco de C4 (ELF).

Agora o bloco de C5 (VirusTotal).

Agora o bloco de C6 (Figura 2).

Agora C7 (inspeção, fora da regra de R).

Agora o tempo estimado.

Por fim, a tabela com todos os passos.

Ajusto a marcação dos passos de conferência e a numeração citada no início.

Montei o roteiro de 33 passos (P1–P33) como um documento: [Roteiro de execução — Foremost-NG (SBSeg 2025), selos F e R](https://claude.ai/code/artifact/a46da080-a8cd-45db-a001-65818b35a151). Nada foi executado; os resultados esperados vêm do artigo, do README, do Dockerfile ou do Makefile, e onde os autores não dizem nada está escrito "não informado".

Dos 33 passos, 13 seguem procedimento dos autores, 14 estão marcados [NÃO DOCUMENTADO] e 6 estão marcados [CONFERÊNCIA NÃO DOCUMENTADA]. Esses 6 conferem um resultado que os autores descrevem, mas com ferramentas escolhidas por mim (`cmp`, `file`, `readelf`).

Quatro pontos mudam a forma de executar:

- **Commit avaliado:** nem o README nem o artigo levam ao commit `bb812a22`, e o Dockerfile clona o HEAD atual do GitHub. Por isso há um checkout explícito em P5.
- **Dados de entrada para C1–C5:** o artefato não traz nenhum. P14 e P15 montam uma imagem de teste com amostras em offsets conhecidos. Para isso você precisa de um `.evtx` exportado de um Windows e de binários Mach-O de um macOS. Sem eles, C1 ou C3 ficam "não verificadas".
- **C6:** depende de pedir `evidence2.dd` aos autores (P29). Sem essa imagem, R não pode ser atribuído pela regra de `reivindicacoes.md`.
- **Tabela da Fig. 2 em P32:** transcrevi a partir de uma figura de baixa resolução. Confira contra o PDF antes de comparar. Os 12 offsets são coerentes com os nomes dos arquivos (offset ÷ 512).

O tempo estimado é de 4 h 30 min a 7 h de trabalho ativo, sem contar a espera pela resposta dos autores.
