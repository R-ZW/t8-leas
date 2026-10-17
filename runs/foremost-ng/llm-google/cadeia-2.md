# Cadeia FN-2 — google

- provedor: google
- modelo_exibido: Gemini Pro (High)
- versao: gemini-pro (Antigravity desktop)
- esforco: High
- interface: Antigravity (desktop), subagente isolado (`revisor-cega-gemini`, conversa `6f27ccd7-9d78-4b1c-8edb-124866f7300c`) com acesso somente-leitura restrito aos 4 anexos do pacote; sem memória entre conversas; busca na web desativada
- data_hora_A: 2026-10-17 13:55 BRT
- data_hora_B1: 2026-10-17 13:59 BRT
- data_hora_B2: pendente
- anexos_A: artigo.pdf=d9b12aa44caeab3d8374fd9ad092c3b9ecec1f18d589125f0ca2f8d00dc9e715, artefato.txt=6de9ecff1194121da658fd3684742c0b2a42b7899ed73b7d3649b9e928330446, instrucoes-oficiais.md=446e5f94605b2fe60ac9c4028f7be57b0488bc79c3c8ef2ef782428f8e290a47, reivindicacoes.md=3d27bc26b64ae7c16272dc9d7a68c25ccacf98d82dbfcdc5bfd7d3ab7932dbac
- anexo_B2: pendente
- metodo_exportacao: transcrição integral gerada a partir do log oficial da sessão isolada (`6f27ccd7-9d78-4b1c-8edb-124866f7300c`, `transcript_full.jsonl`); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos
- desvios: resposta A usou 13 chamada(s) de ferramenta somente-leitura para abrir os 4 anexos: view_file ("Read instrucoes-oficiais.md"); view_file ("Read reivindicacoes.md"); view_file ("Read artigo.pdf"); view_file ("Read artefato.txt lines 1-800"); view_file ("Read artefato.txt lines 801-1600"); view_file ("Read artefato.txt lines 1601-2400"); view_file ("Read artefato.txt lines 2401-3200"); view_file ("Read artefato.txt lines 3201-4000"); view_file ("Read artefato.txt lines 4001-4800"); view_file ("Read artefato.txt lines 4801-5600"); view_file ("Read artefato.txt lines 5601-6400"); view_file ("Read artefato.txt lines 6401-7331"); view_file ("Read artefato.txt lines 7201-7331") | resposta A contém raciocínio (thinking) omitido nesta transcrição | resposta B1 contém raciocínio (thinking) omitido nesta transcrição

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

### A. Materiais examinados

Foram abertos e examinados exclusivamente os 4 arquivos fornecidos no pacote:
1. `d:\Github\t8-leas\runs\foremost-ng\pacote\instrucoes-oficiais.md` (integralmente, linhas 1–21).
2. `d:\Github\t8-leas\runs\foremost-ng\pacote\reivindicacoes.md` (integralmente, linhas 1–22).
3. `d:\Github\t8-leas\runs\foremost-ng\pacote\artigo.pdf` (integralmente, páginas 1–8).
4. `d:\Github\t8-leas\runs\foremost-ng\pacote\artefato.txt` (integralmente, linhas 1–7331, contendo o índice de arquivos e o código/documentação da versão `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`: `.gitignore`, `Dockerfile`, `LICENSE`, `README.md`, `src/Makefile`, `src/ansi_colors.h`, `src/api.c`, `src/cli.c`, `src/config.c`, `src/dir.c`, `src/engine.c`, `src/extract.c`, `src/extract.h`, `src/foremost.conf`, `src/helpers.c`, `src/main.c`, `src/main.h`, `src/ole.h`, `src/state.c`, `src/vt_query.c` e `src/vt_query.h`).

---

### B. Selo F (Funcional)

#### 1. Critérios oficiais aplicáveis e 2. Status de atendimento

De acordo com `[instrucoes-oficiais.md:13-15]`:
> *"O artefato precisa ser executável e permitir a observação de funcionalidades. O README deve informar dependências, versões de dependências/linguagens/ambiente, ambiente de execução, instalação, execução e pelo menos um exemplo mínimo. O revisor deve **executar** o artefato e apresentar prova de execução e saídas no parecer. Ler código ou README, por si só, não constitui prova de funcionamento."*

Avaliação por critério:
- **F1 — Artefato executável e que permita a observação de funcionalidades (`"O artefato precisa ser executável e permitir a observação de funcionalidades"`):** **Só verificável por execução**. O código-fonte em C está completo (`[artefato.txt:16-33]`, `[src/main.c:197-304]`, `[src/engine.c:235-472]`, `[src/extract.c:1-2697]`, `[src/vt_query.c:1-218]`), acompanhado de `src/Makefile` e `Dockerfile`, mas a confirmação de compilação sem erros e funcionamento requer execução.
- **F2 — Informação de dependências no README (`"O README deve informar dependências"`):** **Atendido na documentação (com lacunas no README para Linux, supridas pelo Dockerfile e Makefile)**. Para BSD, o README indica `curl` (`[README.md:39-43]`); para macOS, `openssl@3` (`[README.md:52-55]`); para cross-compilação Windows, `MinGW` e as DLLs em `windows_dlls` (`[README.md:64-68]`). Para Linux, o `README.md` omite os pacotes de desenvolvimento necessários (`gcc`, `make`, `libssl-dev`, `libcurl4-openssl-dev`), mas estes estão explicitados no `[Dockerfile:4-5]` e nas flags `-lssl -lcrypto -lcurl` do `[src/Makefile:46]`.
- **F3 — Versões de dependências/linguagens/ambiente e ambiente de execução (`"versões de dependências/linguagens/ambiente, ambiente de execução"`):** **Atendido na documentação (de forma parcial/mínima)**. O `README.md` define a ferramenta como voltada a Linux (`"`foremost-ng` is a Linux-based file recovery tool"`, `[README.md:3]`), lista procedimentos para `Linux`, `BSD`, `macOS` e `Cross compiling for Windows` (`[README.md:31-70]`), especifica `openssl@3` no macOS (`[README.md:54]`) e nota sobre `glibc < 2.2.0` (`[README.md:70]`), enquanto o `[Dockerfile:1]` define `FROM ubuntu:latest`. Não há, contudo, fixação de versões exatas de SO/compilador/bibliotecas para Linux no `README.md`.
- **F4 — Instruções de instalação e execução (`"instalação, execução"`):** **Atendido na documentação**. O `README.md` traz as seções `## Installation` (`[README.md:21-70]`), `## Usage` (`[README.md:74-86]`), `## VirusTotal API` (`[README.md:89-109]`) e `## Uninstallation` (`[README.md:112-119]`).
- **F5 — Pelo menos um exemplo mínimo (`"e pelo menos um exemplo mínimo"`):** **Atendido parcialmente (sintaxe geral no README; exemplos concretos no artigo e manpage)**. No `[README.md:78-108]`, apresenta-se apenas `man foremost-ng`, a sintaxe abstrata `foremost-ng [options] [image_or_device]` e a exportação de `VT_API_KEY` para uso com `-x`, além de duas capturas de tela (`[README.md:6-7]`). Exemplos concretos de invocação estão no artigo (`[artigo.pdf:p.7, §4.1]`), como `foremost-ng -i disk.img -o /temp/output/carved` e `foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved`.
- **F6 — Execução pelo revisor com prova de execução e saídas (`"O revisor deve executar o artefato e apresentar prova de execução e saídas no parecer"`):** **Só verificável por execução**.

#### 3. Evidências citadas

- `[instrucoes-oficiais.md:15]`: *"O artefato precisa ser executável e permitir a observação de funcionalidades. O README deve informar dependências, versões de dependências/linguagens/ambiente, ambiente de execução, instalação, execução e pelo menos um exemplo mínimo. O revisor deve **executar** o artefato e apresentar prova de execução e saídas no parecer."*
- `[README.md:3]`: *"`foremost-ng` is a Linux-based file recovery tool that extracts files from disk images or devices by scanning for configurable file headers and footers."*
- `[README.md:26-35]`: *"tar xzvf foremost-ng-<version>.tar.gz / cd foremost-ng-<version>/src / ### Linux / make / sudo make install"*
- `[README.md:39-68]`: *"Make sure `curl` is installed: pkg_add curl # OpenBSD ... Install OpenSSL: brew install openssl@3 ... Install MinGW in your Linux distribution and cross-compile: make cross / Required DLLs can be found in the [windows_dlls](windows_dlls) directory"*
- `[README.md:70]`: *"> **Note:** On systems with glibc < 2.2.0, you may see harmless warnings about `ftello` and `fseeko`."*
- `[README.md:78-85]`: *"man foremost-ng / Basic syntax: / foremost-ng [options] [image_or_device]"*
- `[README.md:91-101]`: *"`foremost-ng` supports automatic file reputation checks using the VirusTotal API via the `-x` command-line option. ... export VT_API_KEY=yourkey"*
- `[Dockerfile:1-10]`: *"FROM ubuntu:latest / RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev ... WORKDIR /opt/foremost-ng/src / RUN make && make install"*
- `[src/Makefile:46]`: *"LINK_OPT += -lssl -lcrypto -lcurl"*
- `[artigo.pdf:p.7, §4.1]`: *"foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved"*

#### 4. Decisão para o Selo F

**Decisão:** **Indeterminado**
- **Justificativa:** Embora o `README.md` seja enxuto (delegando dependências Linux ao `Dockerfile` e exemplos concretos ao artigo e à manpage `foremost-ng.8.gz`), o pacote contém todo o código-fonte, `Makefile` e `Dockerfile` necessários para compilação e execução da ferramenta. Como a atribuição do Selo F exige obrigatoriamente a execução do artefato e observação de suas saídas (`[instrucoes-oficiais.md:15]`), a decisão analítica é **Indeterminado**.

#### 5. Confiança

- **Confiança de que o comitê oficial atribuiu o Selo F:** **88/100**. (Trata-se de ferramenta do Salão de Ferramentas com `Dockerfile` funcional, `Makefile` multiplataforma e código C autocontido de fácil compilação em ambiente Ubuntu/Linux).

#### 6. O que precisaria ser observado na execução para mudar a decisão

- **Para mudar para Atribuir:**
  1. Compilar o código em `src/` com `make` (em ambiente Linux com `gcc`, `libssl-dev` e `libcurl4-openssl-dev`, ou construindo a imagem via `Dockerfile`) sem erros de compilação/linkedição.
  2. Executar `./foremost-ng -h` e `./foremost-ng -V` verificando a exibição correta das opções de linha de comando e versão.
  3. Executar `./foremost-ng` sobre uma imagem de disco ou arquivo de teste (por exemplo, `-i <imagem> -o output`), observando a criação do diretório de saída, do arquivo `audit.txt` e a extração funcional de arquivos recuperados.
- **Para mudar para Não atribuir:**
  1. Falha de compilação ou erro fatal em tempo de execução (ex.: falha de segmentação imediata) mesmo em ambiente Linux satisfazendo as dependências do `Dockerfile`/`Makefile`.

---

### C. Selo R (Reprodutível) — Avaliação por Reivindicação

#### 1. Critérios oficiais aplicáveis e 2. Status de atendimento

De acordo com `[instrucoes-oficiais.md:17-19]`:
> *"O revisor deve conseguir reproduzir as **principais reivindicações do artigo**. A documentação do artefato deve trazer instruções de execução dessas reivindicações e descrever o processo usado pelos autores para chegar aos resultados publicados. O revisor deve executar os experimentos e confrontar os resultados com os do artigo, incluindo figuras/tabelas pertinentes, resumindo a comparação no parecer."*

E conforme a regra estabelecida em `[reivindicacoes.md:15-21]`:
> *"O README não marca reivindicações a reproduzir. Por isso, valem as reivindicações principais desta lista: **C1 a C6**. **R é atribuído se C1 a C6 forem reproduzidas.** C7 é uma contribuição arquitetural, sem experimento associado no artigo; ela pode ser inspecionada, mas não entra na regra de R. ... Uma reivindicação é reproduzida quando o resultado esperado da tabela é observado. Em C6, comparam-se os arquivos e offsets da Fig. 2. As contagens do VirusTotal mudam com o tempo e não precisam coincidir."*

Avaliação geral dos critérios de R:
- **R1 — Instruções de execução das reivindicações principais e descrição do processo na documentação do artefato (`[instrucoes-oficiais.md:19]`):** **Não atendido**. O `README.md` (`[README.md:1-119]`) não contém instruções específicas para reproduzir C1–C6, não documenta os identificadores de formatos da flag `-t` (`evtx`, `script`, `macho`, `elf`) e não descreve o procedimento nem os dados usados no experimento da Figura 2 (`evidence2.dd`).
- **R2 — Disponibilidade dos dados/artefatos de entrada necessários para reproduzir as reivindicações principais (`[instrucoes-oficiais.md:10,19]`, `[reivindicacoes.md:12,17,21]`):** **Não atendido**. O pacote (`[artefato.txt:9-50]`) não inclui nenhuma imagem de teste (`evidence2.dd`, `disk.img`, `memory.dump`) nem scripts/instruções para obtê-las ou gerá-las. Em particular, a imagem `evidence2.dd` (2,84 GB) exigida por C6 é inexistente no pacote e não possui link de download no artigo ou no README.
- **R3 — Execução dos experimentos e confronto dos resultados com os do artigo (`[instrucoes-oficiais.md:19]`):** **Não atendido para C6 (`nao_reproduzivel`)** e **só verificável por execução para C1 a C5 (`depende_execucao`)**.

#### 3. Avaliação individual por reivindicação (`reivindicacoes.md`)

- **Reivindicação C1 — Recuperação de logs de eventos do Windows (EVTX): o parser reconhece a assinatura `ElfFile`, delimita os chunks de 64 KiB e extrai o log (`[reivindicacoes.md:7]`)**
  - **Classificação:** `depende_execucao`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.6, §3]`: *"Foremost-NG identifies EVTX files by matching the ”ElfFile” magic in the event log header. It reads the number of 64 KiB chunks in the file and either locates the next EVTX header (to carve only until that point) or extracts all chunks indicated."* e `[artigo.pdf:p.7, §4.1]`: *"foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved"*.
    - No código: O tipo `EVTX` é registrado em `[src/state.c:381-382]` e `[src/state.c:688-694]` com `init_builtin(state, EVTX, "evtx", "ElfFile\0\0", NULL, 8, 0, 100 * MEGABYTE, TRUE);`. A função `extract_evtx` em `[src/extract.c:2460-2517]` verifica `if (memcmp(buf, "ElfFile\0\0", 8) != 0)` (`[src/extract.c:2474]`), lê `chunk_count = htoi(&buf[0x18], FOREMOST_LITTLE_ENDIAN);` (`[src/extract.c:2479]`), calcula `full_size = (uint64_t)chunk_count * 65536ULL;` (`[src/extract.c:2489]`), procura o próximo cabeçalho `"ElfFile\0\0"` (`[src/extract.c:2494-2502]`) e salva o arquivo `.evtx` com `write_to_disk` (`[src/extract.c:2514]`).
    - Na documentação: O `[README.md:74-86]` traz apenas a sintaxe geral, sem imagem de teste contendo arquivos `.evtx`. Além disso, há risco técnico na implementação (ver Seção D: leitura de `chunk_count` no offset `0x18` em vez de `0x2A` e omissão dos 4 KiB do cabeçalho inicial do arquivo EVTX), de modo que verificar se o arquivo `.evtx` extraído é efetivamente legível por uma ferramenta de análise de eventos depende de execução.

- **Reivindicação C2 — Recuperação de scripts (Bash, Python, PowerShell) reconhecidos por shebang (`#!`) e conteúdo textual, com mínimo de 32 bytes e mais que só comentários (`[reivindicacoes.md:8]`)**
  - **Classificação:** `depende_execucao`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.6, §3]`: *"Script carving begins by locating a shebang (#!) at the file’s start. Foremost-NG then scans forward to include all printable characters up to a non-printable sentinel, ensuring the file is at least 32 bytes long and contains more than comments."*
    - No código: Registrado em `[src/state.c:384-385]` e `[src/state.c:695-697]` com `init_builtin(state, SCRIPT, "script", "#!", NULL, 2, 0, 2 * MEGABYTE, TRUE);`. A função `extract_script` (`[src/extract.c:2519-2622]`) define `const uint64_t MIN_SCRIPT_SIZE = 32;` (`[src/extract.c:2521]`), varre bytes enquanto `isprint(c) || c == '\n' || c == '\r' || c == '\t'` (`[src/extract.c:2549]`), busca um próximo `"#!"` (`[src/extract.c:2561-2569]`), valida `if (carve_len < MIN_SCRIPT_SIZE)` (`[src/extract.c:2578]`) e verifica se após a primeira quebra de linha existe algum caractere não branco diferente de `'#'` (`if (!isspace(*p)) { if (*p != '#') { found_real = 1; break; } }`, `[src/extract.c:2600-2605]`), gravando o resultado com `write_to_disk` (`[src/extract.c:2619]`).
    - Na documentação: O `README.md` não traz instruções específicas para `-t script` nem imagem de entrada de teste; a comprovação da extração com corpo legível depende de execução.

- **Reivindicação C3 — Recuperação de binários Mach-O `fat` e `thin`, usando o cabeçalho universal ou os comandos de carga para determinar o tamanho (`[reivindicacoes.md:9]`)**
  - **Classificação:** `depende_execucao`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.6, §3]`: *"Mach-O extraction first detects the FAT (universal) magic to handle multi-architecture binaries; it then reads each architecture’s offset and size to compute the maximal range. If the FAT header is absent, it checks for thin Mach-O magic and reads load command entries to locate segment extents."*
    - No código: Registrado em `[src/state.c:372-379]` e `[src/state.c:673-687]` para as assinaturas `\xCA\xFE\xBA\xBE` (FAT), `\xCE\xFA\xED\xFE` (32 bits LE) e `\xCF\xFA\xED\xFE` (64 bits LE). Em `[src/extract.c:2314-2455]`, `extract_macho` verifica o cabeçalho FAT `0xCA 0xFE 0xBA 0xBE` (`[src/extract.c:2327]`) lendo `nfat_arch = read_be32(&buf[4])` e iterando pelas entradas de 20 bytes (`arch_fileoff + arch_size`, `[src/extract.c:2333-2348]`), ou verifica `magic_le == 0xCEFAEDFE` (`[src/extract.c:2363]`) e `magic_le == 0xCFFAEDFE` (`[src/extract.c:2409]`), percorrendo os `ncmds` comandos de carga (`cmd == 0x1` / `cmd == 0x19 /* LC_SEGMENT_64 */`) para achar o maior `fileoff + filesize` (`[src/extract.c:2387-2396, 2433-2442]`).
    - Na documentação: O `README.md` não inclui instruções ou binários/imagens de teste para Mach-O; a verificação de que o binário Mach-O extraído é reconhecível por ferramenta apropriada depende de execução.

- **Reivindicação C4 — Recuperação de executáveis ELF de 32 e 64 bits, delimitados pelos cabeçalhos de programa (`[reivindicacoes.md:10]`)**
  - **Classificação:** `depende_execucao`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.6, §3]`: *"For ELF binaries, the tool checks the ELF magic and identifies whether the file is 32-bit or 64-bit. It reads the program header table to determine all loadable segments’ extents and then extracts the union of those segments."* e `[artigo.pdf:p.7, §4.1]`: *"foremost-ng -x -t elf -i memory.dump -o ./carved-files"*.
    - No código: Registrado em `[src/state.c:369-370]` e `[src/state.c:448-454]` com cabeçalho `\x7F\x45\x4C\x46`. A função `extract_elf` (`[src/extract.c:2147-2309]`) verifica `buf[0] != 0x7F || buf[1] != 'E' || buf[2] != 'L' || buf[3] != 'F'` (`[src/extract.c:2159]`), checa `ei_data == 1` (little-endian, `[src/extract.c:2172]`) e trata `ei_class == 1` (ELF32, `[src/extract.c:2176-2240]`) e `ei_class == 2` (ELF64, `[src/extract.c:2240-2306]`), lendo `e_phoff`, `e_phentsize` e `e_phnum` e calculando `max_seg_end` sobre os segmentos com `p_type == 1 /* PT_LOAD */`.
    - Na documentação: O `README.md` não fornece imagens de teste nem comandos específicos para ELF; a confirmação de que o `.elf` extraído é estruturalmente legível por analisador ELF depende de execução.

- **Reivindicação C5 — Enriquecimento pelo VirusTotal: com `-x` e `VT_API_KEY`, consulta a API pelo hash de cada arquivo recuperado e registra o resultado de detecção (`[reivindicacoes.md:11]`)**
  - **Classificação:** `depende_execucao`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.3, §2]`: *"With both checksum and key in hand, the tool formats an HTTP GET request to https://www.virustotal.com/api/v3/files/hash, setting the x-apikey header and requesting JSON in return."* e `[artigo.pdf:p.7, §4.1]`: *"If the API key is missing or invalid, Foremost-NG will still perform carving but will emit a warning and skip all VT lookups."*
    - No código: A flag `-x` ativa `mode_virustotal` (`case 'x': set_mode(s, mode_virustotal); break;`, `[src/main.c:131]`). Ao gravar cada arquivo em `write_to_disk` (`[src/dir.c:275-283]`), se `get_mode(s, mode_virustotal)` estiver ativo, o código chama `sha_checksum(fn, "sha256", sha256)` e `vt = vt_check_hash(sha256)`, preenchendo `nd->vt_label` com `"Malicious (%d)"` ou `"Clean (%d)"` e registrando na saída de auditoria (`[src/dir.c:292-295]`). Em `[src/vt_query.c:136-198]`, `vt_check_hash` obtém `VT_API_KEY` (`if (api_key == NULL || strlen(api_key) == 0) { fprintf(stderr, "Error: VT_API_KEY environment variable is not set.\n"); return result; }`, `[src/vt_query.c:140-143]`), consulta `https://www.virustotal.com/api/v3/files/<hash>` (`[src/vt_query.c:21,155]`) e extrai `malicious` e `undetected` de `"last_analysis_stats"` via `sscanf` (`[src/vt_query.c:177-186]`).
    - Na documentação: Documentado em `[README.md:89-109]` (seção `## VirusTotal API`). A observação da consulta HTTP real e do comportamento com e sem chave depende de execução.

- **Reivindicação C6 — Exemplo de execução da Figura 2: `./foremost-ng -v -x evidence2.dd` (`[reivindicacoes.md:12]`)**
  - **Classificação:** `nao_reproduzivel`
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.7, §4.2]`: *"Figure 2 shows an execution example and the expected output."* e `[artigo.pdf:p.8, Fig. 2]`: mostra a execução de `$ ./foremost-ng -v -x evidence2.dd` sobre o arquivo `File: evidence2.dd` com `Length: 2 GB (2845109643 bytes)`, extraindo 12 arquivos (`0: 00004352.elf` no offset `2228224`, `1: 00004820.elf` no offset `2467840`, `2: 00005108.elf` no offset `2615296`, `3: 00005492.script` no offset `2811904`, `4: 00399084.exe` no offset `204740608`, ..., `11: 01797042.zip` no offset `914965615`).
    - No critério de reprodução: `[reivindicacoes.md:21]`: *"Em C6, comparam-se os arquivos e offsets da Fig. 2. As contagens do VirusTotal mudam com o tempo e não precisam coincidir."*
    - No artefato: O índice completo do repositório (`[artefato.txt:9-50]`) mostra que a imagem `evidence2.dd` **não está incluída** no artefato. O `[README.md:1-119]` também não faz qualquer menção a `evidence2.dd` nem fornece link ou script para obtê-la ou construí-la. O artigo (`[artigo.pdf:p.7]`) menciona apenas genericamente `https://dftt.sourceforge.net` para amostras de teste legadas, onde `evidence2.dd` (contendo artefatos ELF e script nos offsets específicos da Figura 2) não está identificada nem disponibilizada. Sem o arquivo de entrada `evidence2.dd`, é impossível reproduzir os arquivos e offsets da Figura 2.

- **Reivindicação C7 — Arquitetura de parsers extensível: despachante central e parsers com identificador, assinatura, validação e recuperação (`[reivindicacoes.md:13]`)** *(Nota: conforme `[reivindicacoes.md:17]`, C7 é contribuição arquitetural sem experimento associado e não entra na regra de atribuição de R)*
  - **Classificação:** `reproduzivel` (quanto à organização em módulos da Fig. 1 inspecionável no código, com ressalvas de implementação)
  - **Análise e evidências:**
    - No artigo: `[artigo.pdf:p.3, Fig. 1 e §2]`: apresenta o pipeline `Command Line Interface (CLI) -> Input validation -> File carving engine -> File extraction engine -> Carved files` e descreve parsers com identificador, assinatura, validação e função de recuperação.
    - No código: A divisão de alto nível da Figura 1 corresponde aos arquivos `src/main.c` e `src/cli.c` (CLI e validação de entrada `is_valid_input` em `[src/main.c:117-192]`), `src/engine.c` (motor de carving `search_stream` e `search_chunk` em `[src/engine.c:235-412]`), `src/extract.c` (motor de extração `extract_file` e funções `extract_*` em `[src/extract.c:1-2697]`) e `src/state.c` (registro das especificações em `search_spec` via `init_builtin` em `[src/state.c:256-403]`). Ressalta-se, porém, que a estrutura `s_spec` (`[src/main.h:262-280]`) não utiliza ponteiros de função/callbacks: o despacho em `extract_file` (`[src/extract.c:2628-2697]`) e a seleção em `set_search_def` (`[src/state.c:408-714]`) são feitos por cadeias `if / else if` estáticas.

#### 4. Decisão para o Selo R

**Decisão:** **Não atribuir**
- **Justificativa:** Pela regra oficial (`[instrucoes-oficiais.md:19]`) e pela regra específica do pacote (`[reivindicacoes.md:17]`: *"R é atribuído se C1 a C6 forem reproduzidas"*), um critério obrigatório falha: falta o dado de entrada essencial (`evidence2.dd`, de 2,84 GB) e qualquer instrução para obtê-lo ou gerá-lo, tornando **C6 não reproduzível** (`[artefato.txt:9-50]`, `[README.md:1-119]`, `[reivindicacoes.md:12,21]`). Além disso, o `README.md` não documenta os passos para reproduzir nenhuma das reivindicações C1–C6 nem fornece imagens de teste para os novos formatos (`evtx`, `script`, `macho`, `elf`).

#### 5. Confiança

- **Confiança de que o comitê oficial atribuiu o Selo R:** **10/100** (ou seja, 90/100 de confiança de que o comitê oficial **não** atribuiu o Selo R, visto que trata-se de artigo do Salão de Ferramentas cujo repositório não inclui conjuntos de dados de teste, scripts de experimentos ou instruções de reprodução da Figura 2 no `README.md`).

#### 6. O que precisaria ser observado na execução (e nos artefatos disponibilizados) para mudar a decisão

- **Para mudar de Não atribuir para Atribuir:**
  1. Os autores precisariam disponibilizar a imagem `evidence2.dd` (ou script determinístico que a gere) e instruções de reprodução das reivindicações C1–C6.
  2. Na execução de `./foremost-ng -v -x evidence2.dd`, observar a extração dos mesmos 12 arquivos (`00004352.elf` a `01797042.zip`) nos exatos offsets da Figura 2 (`[artigo.pdf:p.8]`).
  3. Na execução sobre imagens contendo artefatos EVTX (C1), Scripts Bash/Python/PowerShell (C2), binários Mach-O `fat` e `thin` (C3) e binários ELF 32/64 bits (C4), comprovar que os arquivos extraídos são íntegros e reconhecíveis/legíveis pelas ferramentas de análise correspondentes, bem como observar o enriquecimento da coluna `VT` no `audit.txt` com `-x` e `VT_API_KEY` (C5).

---

### D. Lacunas e riscos

1. **Ausência total de imagens/dados de teste no repositório (`[artefato.txt:9-50]`):** Nem `evidence2.dd` (usada na Figura 2 / C6), nem `disk.img` ou `memory.dump` (citadas na Seção 4.1 do artigo), nem pequenas imagens sintéticas contendo arquivos `.evtx`, `.elf`, `.macho` e `.script` foram incluídas no repositório.
2. **Lacunas no `README.md` (`[README.md:21-86]`):**
   - O `README.md` não lista os pacotes de dependências para compilação nativa no Linux (`libssl-dev`, `libcurl4-openssl-dev`, `gcc`, `make`), que só aparecem no `[Dockerfile:4-5]`. No BSD (`[README.md:39-43]`), menciona apenas `curl`, omitindo OpenSSL (`-lssl -lcrypto` em `[src/Makefile:37]`).
   - Há pequena divergência entre o comando de instalação no `[artigo.pdf:p.6]` (`git clone ... / cd foremost-ng / make`, que falha na raiz pois o `Makefile` está em `src/Makefile`) e o `[README.md:28]` / `[Dockerfile:9]` (que corretamente acessam o subdiretório `src`).
   - O `README.md` não documenta os valores aceitos pela flag `-t` para os novos parsers (`evtx`, `script`, `macho`, `elf`).
3. **Bug em `read_le64` (`[src/helpers.c:360-362]`):** A função auxiliar de leitura de inteiros de 64 bits little-endian usada pelos parsers ELF64 (`[src/extract.c:2251,2280-2281]`) e Mach-O 64 bits (`[src/extract.c:2435-2436]`) está implementada como `uint64_t read_le64(unsigned char *buf) { return htoi(buf, FOREMOST_LITTLE_ENDIAN); }`, chamando `htoi` (32 bits) em vez de `htoll` (64 bits). Em arquiteturas little-endian, isso trunca os 32 bits superiores (funcionando apenas enquanto offsets e tamanhos de segmentos forem menores que 4 GiB).
4. **Risco de corrupção estrutural na extração de EVTX (`[src/extract.c:2479-2490]`):** Em `extract_evtx`, o código lê `chunk_count = htoi(&buf[0x18], FOREMOST_LITTLE_ENDIAN)` (32 bits no offset `0x18`) e calcula `full_size = (uint64_t)chunk_count * 65536ULL`. Contudo, no formato binário EVTX do Windows, o cabeçalho do arquivo tem 4096 bytes (4 KiB) antes do primeiro chunk de 64 KiB, e a contagem de chunks de 16 bits fica no offset `0x2A` (enquanto `0x18` contém `next_record_id` ou `header_block_size`). Isso pode fazer com que o arquivo `.evtx` extraído tenha tamanho incorreto ou seja truncado em 4 KiB ao final.
5. **Truncamento da tabela de seções em binários ELF (`[src/extract.c:2213-2233, 2279-2299]`):** `extract_elf` calcula o tamanho do arquivo apenas até o fim do último segmento `PT_LOAD` (`p_offset + p_filesz`). Como compiladores frequentemente posicionam a tabela de cabeçalhos de seção (`e_shoff`) e `.shstrtab` após os segmentos `PT_LOAD`, ferramentas que dependem de cabeçalhos de seção podem acusar truncamento no `.elf` extraído.
6. **Divergências menores entre texto do artigo e código:**
   - Na Seção 4.2 (`[artigo.pdf:p.7]`), o texto menciona um arquivo `recovery.log` contendo hashes e offsets, e exemplos como `00000002.sh`, mas o código gera `audit.txt` (`[src/main.h:162]`) sem imprimir o hash SHA-256 na linha do arquivo (`[src/dir.c:292-295]`) e usa a extensão `.script` (`[src/state.c:384]`), exatamente como aparece na captura de tela da Figura 2 (`[artigo.pdf:p.8]`).
   - Na Seção 1 (`[artigo.pdf:p.2]`), o texto afirma identificar scripts por shebangs e assinaturas Unicode, mas o parser `SCRIPT` busca apenas a assinatura ASCII `"#!"` (`[src/state.c:384]`, `[src/extract.c:2562]`).

```json
{"F": {"decisao": "Indeterminado", "confianca": 88, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:1-119", "Dockerfile:1-12", "src/Makefile:1-171", "src/main.c:197-304", "artigo.pdf:p.6-7"]},
 "R": {"decisao": "Não atribuir", "confianca": 10, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:1-22", "artefato.txt:9-50", "README.md:1-119", "artigo.pdf:p.6-8", "src/state.c:321-714", "src/extract.c:2147-2697", "src/dir.c:209-300", "src/vt_query.c:136-198", "src/helpers.c:360-362"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "depende_execucao", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel", "C7": "reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

# Roteiro de Execução e Verificação — Foremost-NG (SBSeg 2025)

> **Nota de escopo:** Este roteiro foi elaborado de forma puramente analítica a partir de `artigo.pdf`, `artefato.txt` (commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`), `instrucoes-oficiais.md` e `reivindicacoes.md`. Nenhuma etapa foi executada. Passos não fornecidos pelos autores estão marcados como **`[NÃO DOCUMENTADO]`** com a respectiva justificativa.

---

## 1. Requisitos de Hardware e Software do Ambiente

### 1.1. Requisitos de Software (Documentados pelos Autores)
- **Sistema Operacional:**
  - **Linux (recomendado/principal):** Ubuntu (`FROM ubuntu:latest` em `[Dockerfile:1]`; ferramenta descrita como *"Linux-based file recovery tool"* em `[README.md:3]`). Recomenda-se execução em máquina virtual ou contêiner Docker (`[instrucoes-oficiais.md:10]`).
  - **Alternativas suportadas no `README.md` / `src/Makefile`:** OpenBSD/FreeBSD (`[README.md:37-48]`), macOS (`[README.md:50-60]`) ou cross-compilação para Windows via MinGW (`[README.md:62-68]`, com DLLs em `windows_dlls/`).
- **Compilador e ferramentas de build (Linux):**
  - `gcc` e `make` (`[Dockerfile:5]`, `[src/Makefile:1]`, `[artigo.pdf:p.6]`).
  - Biblioteca C padrão (`glibc >= 2.2.0` para evitar avisos em `ftello`/`fseeko`, conforme `[README.md:70]`).
- **Bibliotecas de desenvolvimento (Linux):**
  - `libssl-dev` (OpenSSL EVP para cálculo de SHA-1/SHA-256, `[Dockerfile:5]`, `[src/Makefile:46]`, `[artigo.pdf:p.3]`).
  - `libcurl4-openssl-dev` (`libcurl` para consultas HTTP à API v3 do VirusTotal, `[Dockerfile:5]`, `[src/Makefile:46]`, `[artigo.pdf:p.3]`).
- **Serviço externo / Credencial (para a reivindicação C5 e C6):**
  - Conta gratuita no VirusTotal e chave de API na variável de ambiente `VT_API_KEY`, além de conectividade HTTPS com `https://www.virustotal.com/api/v3/files/` (`[README.md:93-101]`, `[artigo.pdf:p.3, p.7]`, `[src/vt_query.c:21,139]`).

### 1.2. Requisitos de Software e Dados Adicionais (`[NÃO DOCUMENTADO]`)
- **`[NÃO DOCUMENTADO]` Utilitários de criação de imagens e validação dos arquivos extraídos:** Necessários porque a tabela de `reivindicacoes.md` exige verificar se os arquivos recuperados em C1–C4 são estruturalmente legíveis por ferramentas apropriadas, mas os autores não especificam quais usar:
  - `dd` e `python3` (para construir imagens brutas `.img`/`.dump` de teste, já que o repositório não inclui imagens de entrada);
  - `file` e `readelf` (`binutils`, para validar binários ELF em C4 e identificar Mach-O em C3);
  - `llvm-objdump` ou `otool` (opcional, para inspecionar estruturas Mach-O em C3);
  - `evtx_dump` (`python3-evtx` / `evtxexport` do `libevtx-utils`, para validar a leitura de logs `.evtx` em C1).
- **`[NÃO DOCUMENTADO]` Requisitos de Hardware:** Os autores não especificam CPU, RAM ou disco no `README.md` nem no `artigo.pdf`. Pelo código-fonte (`CHUNK_SIZE = 100` MB em `[src/main.h:230]`) e pela Figura 2 (`evidence2.dd` com `2845109643 bytes` ≈ 2,84 GB em `[artigo.pdf:p.8]`), recomenda-se no mínimo:
  - **CPU:** 1 vCPU x86_64;
  - **RAM:** ≥ 1 GB livre (o buffer de leitura aloca `100 MB` por chunk em `search_stream`, `[src/engine.c:383-384]`);
  - **Disco:** ≥ 10 GB livres (para comportar o sistema, compilação, imagens de teste e diretórios de saída).

---

## 2. Tempo Estimado

- **Preparação do ambiente e compilação (P1–P2):** ~3 a 5 minutos.
- **Teste mínimo — Selo F (P3–P5):** ~2 a 3 minutos.
- **Experimentos das reivindicações C1 a C5 e C7 — Selo R (P6–P15, P17):** ~10 a 15 minutos (incluindo preparação das imagens sintéticas de teste e chamadas à API do VirusTotal).
- **Verificação da reivindicação C6 (P16):** ~1 minuto (interrupção imediata constatando a ausência de `evidence2.dd`, ou ~5 minutos caso a imagem de 2,84 GB fosse fornecida pelos autores).
- **Tempo total estimado:** **15 a 25 minutos**.

---

## 3. Teste Mínimo — Selo Funcional (F)

### Passo P1 — Instalação de dependências de compilação no Linux `[NÃO DOCUMENTADO no README para Linux; extraído do Dockerfile]`
- **Identificador:** P1
- **Selo e reivindicação relacionados:** Selo F (Preparação do ambiente)
- **Justificativa `[NÃO DOCUMENTADO]`:** A subseção `### Linux` do `[README.md:31-35]` indica apenas `make` e `sudo make install`, omitindo os pacotes de sistema necessários para compilar `vt_query.c` (`openssl/evp.h`, `curl/curl.h`). O comando abaixo é extraído diretamente do `[Dockerfile:3-5]` fornecido no repositório. (Caso existam testes para C1–C4, instalam-se também `file`, `binutils` e `python3`).
- **Diretório:** `<raiz_do_artefato>` (diretório onde o pacote do artefato foi descompactado)
- **Comando exato:**
  ```bash
  sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev file binutils python3
  ```
- **Resultado esperado segundo os autores:** Instalação concluída sem erros dos pacotes `gcc`, `make`, `git`, `libssl-dev` e `libcurl4-openssl-dev` (`[Dockerfile:3-6]`).
- **Evidência a salvar:** Log do terminal (`p1_apt_install.log`) e versões instaladas (`gcc --version`, `make --version`, `openssl version`, `curl --version`).
- **Critério de sucesso:** Comando retorna código de saída `0` e os cabeçalhos `<openssl/evp.h>` e `<curl/curl.h>` estão disponíveis.
- **Critério de falha:** Código de saída diferente de `0` ou ausência dos pacotes `libssl-dev` / `libcurl4-openssl-dev`.
- **Critério de interrupção:** Interromper imediatamente o roteiro se o compilador `gcc` ou as bibliotecas `libssl-dev` e `libcurl4-openssl-dev` não puderem ser instalados, pois a compilação em P2 falhará obrigatoriamente (`[src/Makefile:46]`).

---

### Passo P2 — Compilação e instalação do `foremost-ng`
- **Identificador:** P2
- **Selo e reivindicação relacionados:** Selo F (Instalação)
- **Diretório:** `<raiz_do_artefato>/src` (conforme `[README.md:28]` e `[Dockerfile:9]`; nota: `[artigo.pdf:p.6]` omite `/src`, mas o `Makefile` reside em `src/Makefile`).
- **Comando exato:**
  ```bash
  cd src && make && sudo make install
  ```
- **Resultado esperado segundo os autores:** Compilação dos 10 arquivos `.c` (`main.c`, `state.c`, `helpers.c`, `config.c`, `cli.c`, `engine.c`, `dir.c`, `extract.c`, `api.c`, `vt_query.c`), geração do binário `foremost-ng` em `src/` e instalação em `/usr/local/bin/foremost-ng`, manpage em `/usr/share/man/man8/foremost-ng.8.gz` e configuração em `/usr/local/etc/foremost.conf` (`[README.md:33-34]`, `[src/Makefile:18-22, 107-119]`, `[artigo.pdf:p.6-7]`).
- **Evidência a salvar:** Saída completa do `make` e `sudo make install` (`p2_build_install.log`) e verificação de `which foremost-ng`.
- **Critério de sucesso:** Código de saída `0`, binário `src/foremost-ng` e `/usr/local/bin/foremost-ng` gerados com permissão de execução.
- **Critério de falha:** Erro de compilação ou de linkedição (`ld` falhando em `-lssl`, `-lcrypto` ou `-lcurl`).
- **Critério de interrupção:** Interromper o roteiro caso o binário `foremost-ng` não seja produzido.

---

### Passo P3 — Verificação da interface de linha de comando e página de manual
- **Identificador:** P3
- **Selo e reivindicação relacionados:** Selo F (Observação básica de execução e documentação de uso)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -V && ./foremost-ng -h && man -P cat foremost-ng | head -n 40
  ```
- **Resultado esperado segundo os autores:** Exibição da versão (`1.5.7`) e informações de copyright com `-V`, listagem colorida (ANSI) das opções de linha de comando (`-v`, `-V`, `-h`, `-T`, `-Q`, `-q`, `-a`, `-w`, `-d`, `-x`, `-t`, `-s`, `-k`, `-b`, `-c`, `-o`, `-i`) com `-h` (`[src/main.c:92-112, 161-165]`) e abertura da página de manual (`[README.md:79]`, `[artigo.pdf:p.7]`).
- **Evidência a salvar:** Saída de terminal (`p3_cli_help.log`).
- **Critério de sucesso:** Os comandos executam sem falhas, exibem a versão `1.5.7`, o menu de ajuda com a flag `-x` (*"Enable VirusTotal scan (needs API key)"*) e o texto da manpage.
- **Critério de falha:** Erro de execução (ex.: `Segmentation fault`) ou ausência do binário.
- **Critério de interrupção:** Interromper se o binário não executar.

---

### Passo P4 — Criação de imagem de disco mínima para teste funcional (`disk.img`) `[NÃO DOCUMENTADO]`
- **Identificador:** P4
- **Selo e reivindicação relacionados:** Selo F (Preparação de entrada para o exemplo mínimo)
- **Justificativa `[NÃO DOCUMENTADO]`:** O `README.md` (`[README.md:84]`) indica apenas `foremost-ng [options] [image_or_device]` e o artigo (`[artigo.pdf:p.7, §4.1]`) exemplifica `foremost-ng -i disk.img -o /temp/output/carved`, mas o arquivo `disk.img` não está incluído no artefato (`[artefato.txt:9-50]`). É necessário gerar uma imagem `disk.img` contendo arquivos válidos (ex.: o próprio binário ELF `foremost-ng` embutido entre blocos de zeros) para executar o comando mínimo documentado na Seção 4.1 do artigo.
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import os
  with open("disk.img", "wb") as f:
      f.write(b"\x00" * 512 * 10)
      with open("foremost-ng", "rb") as elf:
          f.write(elf.read())
      f.write(b"\x00" * 512 * 10)
  '
  ```
- **Resultado esperado segundo os autores:** N/A (passo auxiliar não documentado; gera `disk.img` no diretório `src/`).
- **Evidência a salvar:** Listagem `ls -lh disk.img` e hash `sha256sum disk.img` (`p4_disk_img.log`).
- **Critério de sucesso:** Arquivo `disk.img` criado com tamanho > 10 KB.
- **Critério de falha:** Arquivo `disk.img` não criado ou vazio.
- **Critério de interrupção:** Interromper o teste P5 se `disk.img` não existir.

---

### Passo P5 — Execução do exemplo mínimo de uso básico (`Basic Usage`)
- **Identificador:** P5
- **Selo e reivindicação relacionados:** Selo F (Exemplo mínimo de execução)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  mkdir -p /temp/output && rm -rf /temp/output/carved && foremost-ng -i disk.img -o /temp/output/carved
  ```
  *(Nota: comando exato da Seção 4.1 do artigo, `[artigo.pdf:p.7]`: `foremost-ng -i disk.img -o /temp/output/carved`; o `mkdir -p /temp/output` é necessário porque `mkdir()` em `src/dir.c:70` não cria diretórios pais recursivamente).*
- **Resultado esperado segundo os autores:** Todos os parsers registrados inspecionam os dados brutos sequencialmente; os artefatos recuperados são gravados em subdiretórios por formato dentro de `/temp/output/carved` (ex.: `/temp/output/carved/elf/`) e os metadados são registrados em `/temp/output/carved/audit.txt` (`[artigo.pdf:p.6, p.7 §4.1 e §4.2]`, `[src/dir.c:150-299]`).
- **Evidência a salvar:** Saída de terminal, conteúdo de `/temp/output/carved/audit.txt` e listagem `ls -laR /temp/output/carved` (`p5_basic_usage.log`).
- **Critério de sucesso:** Código de saída `0`, exibição de `[INFO] Processing: disk.img` e `[INFO] Processing finished.`, geração de `/temp/output/carved/audit.txt` com `FILES EXTRACTED >= 1` e presença do arquivo extraído em `/temp/output/carved/`.
- **Critério de falha:** Falha de execução, ausência de `audit.txt` ou `0 FILES EXTRACTED`.
- **Critério de interrupção:** Não interrompe os demais testes, mas registra falha no teste mínimo de F.

---

## 4. Blocos por Reivindicação — Selo Reprodutível (R)

---

### Bloco C1 — Recuperação de logs de eventos do Windows (EVTX)
**Reivindicação (`[reivindicacoes.md:7]`):** *Recuperação de logs de eventos do Windows (EVTX): o parser reconhece a assinatura `ElfFile`, delimita os chunks de 64 KiB e extrai o log.*

#### Passo P6 — Preparação de imagem contendo arquivo EVTX (`evtx_test.img`) `[NÃO DOCUMENTADO]`
- **Identificador:** P6
- **Selo e reivindicação relacionados:** Selo R — C1
- **Justificativa `[NÃO DOCUMENTADO]`:** O artefato não inclui imagem de disco com logs `.evtx` (`[artefato.txt:9-50]`). Para testar C1 conforme a lógica de `extract_evtx` (`[src/extract.c:2460-2517]`) e verificar se o arquivo extraído é legível por ferramenta de análise de eventos (`[reivindicacoes.md:7]`), é necessário embutir um arquivo `.evtx` em uma imagem bruta `evtx_test.img` (seja um `.evtx` real do Windows ou um container EVTX com assinatura `ElfFile\0\0` e chunks de 64 KiB).
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # Cria um container EVTX com assinatura ElfFile\0\0 e chunk_count=1 no offset 0x18 (conforme src/extract.c:2474-2479)
  # Nota: se dispuser de um arquivo .evtx real do Windows, substitua "hdr" pelo conteúdo desse arquivo.
  hdr = bytearray(65536)
  hdr[0:8] = b"ElfFile\x00"
  struct.pack_into("<I", hdr, 0x18, 1)   # offset 0x18 lido por extract_evtx
  struct.pack_into("<H", hdr, 0x2A, 1)   # offset 0x2A padrão EVTX (number_of_chunks)
  with open("evtx_test.img", "wb") as f:
      f.write(b"\x00" * 4096)
      f.write(hdr)
      f.write(b"\x00" * 4096)
  '
  ```
- **Resultado esperado segundo os autores:** N/A (passo auxiliar não documentado; gera `evtx_test.img`).
- **Evidência a salvar:** Tamanho e hash de `evtx_test.img` (`p6_evtx_prep.log`).
- **Critério de sucesso:** `evtx_test.img` criado (73.728 bytes).
- **Critério de falha:** Erro ao criar `evtx_test.img`.
- **Critério de interrupção:** Interromper o Bloco C1 se `evtx_test.img` não for gerado.

#### Passo P7 — Execução do carving de EVTX e verificação do arquivo `.evtx` extraído
- **Identificador:** P7
- **Selo e reivindicação relacionados:** Selo R — C1
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./out_c1 && ./foremost-ng -v -t evtx -i evtx_test.img -o ./out_c1 && file ./out_c1/evtx/*.evtx
  ```
  *(Nota: sintaxe `-t evtx,... -i ... -o ...` documentada em `[artigo.pdf:p.7, §4.1]`; a verificação com `file` / ferramenta de análise de eventos é `[NÃO DOCUMENTADO]` pelos autores, mas exigida pelo resultado esperado em `[reivindicacoes.md:7]`).*
- **Resultado esperado segundo os autores:** O parser identifica o magic `"ElfFile"`, extrai os chunks de 64 KiB indicados para `./out_c1/evtx/00000008.evtx`, registra a extração em `./out_c1/audit.txt` e o arquivo `.evtx` resultante pode ser analisado por ferramentas padrão de logs de eventos (`[artigo.pdf:p.6 §3, p.7 §4.1-4.2]`, `[reivindicacoes.md:7]`).
- **Evidência a salvar:** `./out_c1/audit.txt`, arquivo `./out_c1/evtx/*.evtx` e saída de `file` (e de um analisador EVTX como `evtx_dump`, se disponível) (`p7_c1_evtx.log`).
- **Critério de sucesso:** Arquivo `.evtx` extraído em `./out_c1/evtx/` no offset `4096` e reconhecido/legível por ferramenta de análise de eventos.
- **Critério de falha:** Nenhum arquivo `.evtx` extraído, ou arquivo extraído corrompido/ilegível por ferramenta de análise de eventos (por exemplo, devido ao cálculo `chunk_count * 65536` em `src/extract.c:2479-2489` que lê o offset `0x18` em vez de `0x2A` e omite os 4 KiB do cabeçalho do arquivo EVTX).
- **Critério de interrupção:** Prosseguir para o Bloco C2 independentemente do resultado de C1.

---

### Bloco C2 — Recuperação de Scripts (Bash, Python, PowerShell)
**Reivindicação (`[reivindicacoes.md:8]`):** *Recuperação de scripts (Bash, Python, PowerShell) reconhecidos por shebang (`#!`) e conteúdo textual, com mínimo de 32 bytes e mais que só comentários.*

#### Passo P8 — Preparação de imagem contendo scripts (`script_test.img`) `[NÃO DOCUMENTADO]`
- **Identificador:** P8
- **Selo e reivindicação relacionados:** Selo R — C2
- **Justificativa `[NÃO DOCUMENTADO]`:** O artefato não fornece imagem de disco com scripts deletados (`[artefato.txt:9-50]`). Cria-se uma imagem bruta contendo: (1) um script Bash válido (`>= 32` bytes e com comandos além de comentários), (2) um script Python válido (`>= 32` bytes), e (3) um fragmento curto/só comentários (`< 32` bytes ou apenas `#`), para testar os critérios de `extract_script` (`[src/extract.c:2519-2622]`).
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  bash_script = b"#!/bin/bash\n# Comentario inicial\necho \"Teste de recuperacao Foremost-NG\"\nexit 0\n"
  py_script   = b"#!/usr/bin/env python3\nimport sys\nprint(sys.version)\n"
  only_comm   = b"#!/bin/sh\n# apenas comentario sem corpo real de codigo aqui\n"
  with open("script_test.img", "wb") as f:
      f.write(b"\x00" * 2048)
      f.write(bash_script)
      f.write(b"\x00" * 2048)
      f.write(py_script)
      f.write(b"\x00" * 2048)
      f.write(only_comm)
      f.write(b"\x00" * 2048)
  '
  ```
- **Resultado esperado segundo os autores:** N/A (passo auxiliar não documentado; gera `script_test.img`).
- **Evidência a salvar:** Hash e tamanho de `script_test.img` (`p8_script_prep.log`).
- **Critério de sucesso:** `script_test.img` criado com sucesso.
- **Critério de falha:** Erro ao criar `script_test.img`.
- **Critério de interrupção:** Interromper o Bloco C2 se `script_test.img` não for gerado.

#### Passo P9 — Execução do carving de scripts e inspeção do conteúdo extraído
- **Identificador:** P9
- **Selo e reivindicação relacionados:** Selo R — C2
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./out_c2 && ./foremost-ng -v -t script -i script_test.img -o ./out_c2 && head -n 20 ./out_c2/script/*.script
  ```
  *(Nota: o identificador `-t script` está definido em `[src/state.c:695]`, mas é `[NÃO DOCUMENTADO]` no `README.md`).*
- **Resultado esperado segundo os autores:** Extração apenas dos scripts válidos (com `#!/...`, tamanho ≥ 32 bytes e conteúdo além de comentários), preservando a diretiva do interpretador e o corpo legível no subdiretório `./out_c2/script/`, descartando o fragmento que contém apenas comentários (`[artigo.pdf:p.6, §3]`, `[reivindicacoes.md:8]`, `[src/extract.c:2578-2616]`).
- **Evidência a salvar:** `./out_c2/audit.txt` e conteúdo dos arquivos `./out_c2/script/*.script` (`p9_c2_script.log`).
- **Critério de sucesso:** Exatamente 2 arquivos `.script` extraídos (`bash_script` e `py_script`), ambos contendo a linha `#!` e o corpo legível intacto, enquanto `only_comm` é ignorado.
- **Critério de falha:** Nenhum script extraído, corpo truncado/ilegível ou extração indevida de script contendo apenas comentários.
- **Critério de interrupção:** Prosseguir para o Bloco C3.

---

### Bloco C3 — Recuperação de binários Mach-O (`fat` e `thin`)
**Reivindicação (`[reivindicacoes.md:9]`):** *Recuperação de binários Mach-O `fat` e `thin`, usando o cabeçalho universal ou os comandos de carga para determinar o tamanho.*

#### Passo P10 — Preparação de imagem contendo binários Mach-O `fat` e `thin` (`macho_test.img`) `[NÃO DOCUMENTADO]`
- **Identificador:** P10
- **Selo e reivindicação relacionados:** Selo R — C3
- **Justificativa `[NÃO DOCUMENTADO]`:** O artefato não inclui binários Mach-O nem imagens de teste (`[artefato.txt:9-50]`). Constrói-se uma imagem `macho_test.img` contendo um binário Mach-O `thin` de 64 bits (`0xCFFAEDFE` com comando de carga `LC_SEGMENT_64 = 0x19`) e um binário Mach-O `fat` universal (`0xCAFEBABE` com tabela `fat_arch` big-endian), respeitando o formato Mach-O e a lógica de `[src/extract.c:2314-2455]`.
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # 1) Thin Mach-O 64-bit LE (magic 0xFEEDFACF -> bytes CF FA ED FE) de 4096 bytes
  thin64 = bytearray(4096)
  struct.pack_into("<IIIIIIII", thin64, 0,
      0xFEEDFACF, 0x01000007, 3, 2, 1, 72, 0, 0) # mach_header_64 (32 bytes): cputype=x86_64, filetype=EXECUTE, ncmds=1, sizeofcmds=72
  struct.pack_into("<II16sQQQQII", thin64, 32,
      0x19, 72, b"__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
      0x100000000, 4096, 0, 4096, 7, 5)          # LC_SEGMENT_64: fileoff=0, filesize=4096
  # 2) Fat (Universal) Mach-O BE (magic 0xCAFEBABE) contendo a fatia thin64 no offset 4096 (total 8192 bytes)
  fat = bytearray(8192)
  struct.pack_into(">II", fat, 0, 0xCAFEBABE, 1) # magic, nfat_arch=1
  struct.pack_into(">IIIII", fat, 8, 0x01000007, 3, 4096, 4096, 12) # fat_arch: offset=4096, size=4096
  fat[4096:8192] = thin64
  with open("macho_test.img", "wb") as f:
      f.write(b"\x00" * 2048)
      f.write(thin64)
      f.write(b"\x00" * 2048)
      f.write(fat)
      f.write(b"\x00" * 2048)
  '
  ```
- **Resultado esperado segundo os autores:** N/A (passo auxiliar não documentado; gera `macho_test.img`).
- **Evidência a salvar:** Hash e tamanho de `macho_test.img` (`p10_macho_prep.log`).
- **Critério de sucesso:** `macho_test.img` criado com sucesso.
- **Critério de falha:** Erro ao criar `macho_test.img`.
- **Critério de interrupção:** Interromper o Bloco C3 se `macho_test.img` não for gerado.

#### Passo P11 — Execução do carving de Mach-O e reconhecimento por ferramenta apropriada
- **Identificador:** P11
- **Selo e reivindicação relacionados:** Selo R — C3
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./out_c3 && ./foremost-ng -v -t macho -i macho_test.img -o ./out_c3 && file ./out_c3/macho/*.macho
  ```
  *(Nota: o identificador `-t macho` está definido em `[src/state.c:673]`, mas é `[NÃO DOCUMENTADO]` no `README.md`).*
- **Resultado esperado segundo os autores:** Detecção e extração completa tanto do binário Mach-O `thin` (4096 bytes) quanto do binário Mach-O `fat` (8192 bytes) em `./out_c3/macho/`, ambos reconhecíveis como binários Mach-O pela ferramenta `file` (`[artigo.pdf:p.6, §3]`, `[reivindicacoes.md:9]`).
- **Evidência a salvar:** `./out_c3/audit.txt`, tamanhos dos arquivos extraídos (`stat -c "%n %s" ./out_c3/macho/*.macho`) e saída do utilitário `file` (`p11_c3_macho.log`).
- **Critério de sucesso:** Extração dos binários `.macho` (`thin` e `fat`) com tamanhos exatos (4096 B e 8192 B) e identificação pelo comando `file` como `Mach-O 64-bit x86_64 executable` e `Mach-O universal binary`.
- **Critério de falha:** Não extração dos binários `fat` ou `thin`, tamanhos incorretos ou arquivos não reconhecidos pelo utilitário `file`.
- **Critério de interrupção:** Prosseguir para o Bloco C4.

---

### Bloco C4 — Recuperação de executáveis ELF de 32 e 64 bits
**Reivindicação (`[reivindicacoes.md:10]`):** *Recuperação de executáveis ELF de 32 e 64 bits, delimitados pelos cabeçalhos de programa.*

#### Passo P12 — Preparação de imagem contendo executáveis ELF de 32 e 64 bits (`memory.dump`) `[NÃO DOCUMENTADO]`
- **Identificador:** P12
- **Selo e reivindicação relacionados:** Selo R — C4
- **Justificativa `[NÃO DOCUMENTADO]`:** Na Seção 4.1 (`[artigo.pdf:p.7]`), os autores exemplificam `foremost-ng -x -t elf -i memory.dump -o ./carved-files`, mas `memory.dump` não acompanha o artefato (`[artefato.txt:9-50]`). Constrói-se um arquivo `memory.dump` contendo um executável ELF de 32 bits (`EI_CLASS = 1`) e um executável ELF de 64 bits (`EI_CLASS = 2`) com cabeçalhos de programa `PT_LOAD` válidos.
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # 1) ELF32 LE com 1 segmento PT_LOAD de 2048 bytes
  elf32 = bytearray(2048)
  elf32[0:4] = b"\x7fELF"
  elf32[4] = 1; elf32[5] = 1; elf32[6] = 1 # ELFCLASS32, ELFDATA2LSB, EV_CURRENT
  struct.pack_into("<HHIIIIIHHHHHH", elf32, 16,
      2, 3, 1, 0x08048000, 52, 0, 0, 52, 32, 1, 0, 0, 0) # e_phoff=52, e_phentsize=32, e_phnum=1
  struct.pack_into("<IIIIIIII", elf32, 52,
      1, 0, 0x08048000, 0x08048000, 2048, 2048, 5, 0x1000) # PT_LOAD: p_offset=0, p_filesz=2048
  # 2) ELF64 LE com 1 segmento PT_LOAD de 4096 bytes
  elf64 = bytearray(4096)
  elf64[0:4] = b"\x7fELF"
  elf64[4] = 2; elf64[5] = 1; elf64[6] = 1 # ELFCLASS64, ELFDATA2LSB, EV_CURRENT
  struct.pack_into("<HHIQQQIHHHHHH", elf64, 16,
      2, 62, 1, 0x400000, 64, 0, 0, 64, 56, 1, 0, 0, 0) # e_phoff=64, e_phentsize=56, e_phnum=1
  struct.pack_into("<IIQQQQQQ", elf64, 64,
      1, 5, 0, 0x400000, 0x400000, 4096, 4096, 0x1000) # PT_LOAD: p_offset=0, p_filesz=4096
  with open("memory.dump", "wb") as f:
      f.write(b"\x00" * 2048)
      f.write(elf32)
      f.write(b"\x00" * 2048)
      f.write(elf64)
      f.write(b"\x00" * 2048)
  '
  ```
- **Resultado esperado segundo os autores:** N/A (passo auxiliar não documentado; gera `memory.dump`).
- **Evidência a salvar:** Hash e tamanho de `memory.dump` (`p12_elf_prep.log`).
- **Critério de sucesso:** `memory.dump` criado com sucesso.
- **Critério de falha:** Erro ao criar `memory.dump`.
- **Critério de interrupção:** Interromper o Bloco C4 se `memory.dump` não for gerado.

#### Passo P13 — Execução do carving de ELF (32 e 64 bits) e validação estrutural com analisador ELF
- **Identificador:** P13
- **Selo e reivindicação relacionados:** Selo R — C4
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./out_c4 && ./foremost-ng -v -t elf -i memory.dump -o ./out_c4 && file ./out_c4/elf/*.elf && readelf -h -l ./out_c4/elf/*.elf
  ```
  *(Nota: a invocação `-t elf` segue `[artigo.pdf:p.7, §4.1]`; a validação com `file` e `readelf -h -l` é `[NÃO DOCUMENTADO]`, necessária para verificar se o `.elf` extraído é estruturalmente legível por analisador ELF, conforme `[reivindicacoes.md:10]`).*
- **Resultado esperado segundo os autores:** O parser identifica o magic ELF, distingue binários de 32 bits e 64 bits, lê a tabela de cabeçalhos de programa (`PT_LOAD`) para delimitar a extensão de cada arquivo e extrai ambos em `./out_c4/elf/*.elf` (`[artigo.pdf:p.6, §3]`, `[reivindicacoes.md:10]`).
- **Evidência a salvar:** `./out_c4/audit.txt` e saídas de `file` e `readelf -h -l` sobre os arquivos `.elf` extraídos (`p13_c4_elf.log`).
- **Critério de sucesso:** Extração dos dois arquivos `.elf` (um 32-bit de 2048 bytes e um 64-bit de 4096 bytes) em `./out_c4/elf/`, ambos lidos sem erro nos cabeçalhos ELF e de programa por `readelf -h -l`.
- **Critério de falha:** Falha na extração de 32 ou 64 bits, ou cabeçalhos de programa corrompidos segundo `readelf -h -l`.
- **Critério de interrupção:** Prosseguir para o Bloco C5.

---

### Bloco C5 — Enriquecimento pelo VirusTotal (`-x` e `VT_API_KEY`)
**Reivindicação (`[reivindicacoes.md:11]`):** *Enriquecimento pelo VirusTotal: com `-x` e `VT_API_KEY`, consulta a API pelo hash de cada arquivo recuperado e registra o resultado de detecção; sem chave, aviso e carving sem consulta (p. 7).*

#### Passo P14 — Execução com `-x` sem `VT_API_KEY` definida
- **Identificador:** P14
- **Selo e reivindicação relacionados:** Selo R — C5 (comportamento sem chave de API)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  unset VT_API_KEY && rm -rf ./carved-files-nokey && ./foremost-ng -v -x -t elf -i memory.dump -o ./carved-files-nokey
  ```
  *(Nota: comando baseado diretamente em `[artigo.pdf:p.7, §4.1]`: `foremost-ng -x -t elf -i memory.dump -o ./carved-files`).*
- **Resultado esperado segundo os autores:** Se a chave `VT_API_KEY` estiver ausente, o `foremost-ng` emite mensagem de erro/aviso (`Error: VT_API_KEY environment variable is not set.` em `[src/vt_query.c:141]`), ignora as consultas ao VirusTotal e realiza normalmente o carving dos arquivos (`[artigo.pdf:p.3 §2, p.7 §4.1]`, `[reivindicacoes.md:11]`).
- **Evidência a salvar:** Saída de `stdout`/`stderr` e arquivo `./carved-files-nokey/audit.txt` (`p14_c5_vt_nokey.log`).
- **Critério de sucesso:** Emissão da mensagem `Error: VT_API_KEY environment variable is not set.` em `stderr` e extração normal dos arquivos `.elf` em `./carved-files-nokey/elf/`.
- **Critério de falha:** Interrupção abrupta do carving sem extrair os arquivos ou ausência de mensagem sobre `VT_API_KEY`.
- **Critério de interrupção:** Prosseguir para P15.

#### Passo P15 — Execução com `-x` e `VT_API_KEY` válida configurada
- **Identificador:** P15
- **Selo e reivindicação relacionados:** Selo R — C5 (consulta à API do VirusTotal com chave)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  export VT_API_KEY="<SUA_CHAVE_VT_API_KEY>" && rm -rf ./carved-files && ./foremost-ng -v -x -t elf -i memory.dump -o ./carved-files
  ```
  *(Nota: comandos exatos documentados em `[README.md:101]` e `[artigo.pdf:p.7, §4 e §4.1]`).*
- **Resultado esperado segundo os autores:** Para cada arquivo extraído, calcula o hash SHA-256, consulta `https://www.virustotal.com/api/v3/files/<hash>` com o cabeçalho `x-apikey` e registra na coluna `VT` do `audit.txt` (e na saída `-v`) o veredito no formato `Clean (<undetected>)` ou `Malicious (<malicious>)` (`[artigo.pdf:p.3, p.7, p.8 Fig. 2]`, `[src/dir.c:275-283]`, `[src/vt_query.c:136-198]`).
- **Evidência a salvar:** Saída do terminal e arquivo `./carved-files/audit.txt` (`p15_c5_vt_withkey.log`).
- **Critério de sucesso:** Extração concluída sem erro de variável ausente, requisição HTTPS realizada ao VirusTotal e coluna `VT` preenchida em `./carved-files/audit.txt` com `Clean (...)` ou `Malicious (...)` (nota: se o hash sintético não existir na base do VirusTotal, a API retorna HTTP 404 sem objeto `last_analysis_stats`, resultando em `Clean (0)`; para observar contagem > 0, pode-se embutir um arquivo público conhecido, como `/bin/ls` ou string EICAR, na imagem de teste).
- **Critério de falha:** Erro de conexão do `libcurl` ou coluna `VT` permanecendo `N/A` mesmo com `-x` ativo.
- **Critério de interrupção:** Interromper P15 caso o avaliador não possua `VT_API_KEY` ou acesso à internet; prosseguir para o Bloco C6.

---

### Bloco C6 — Exemplo de execução da Figura 2 (`./foremost-ng -v -x evidence2.dd`)
**Reivindicação (`[reivindicacoes.md:12]`):** *Exemplo de execução da Figura 2: `./foremost-ng -v -x evidence2.dd`, gerando tabela como a da Fig. 2, com arquivos ELF, script, EXE e ZIP, seus offsets e a coluna VT.*

#### Passo P16 — Tentativa de execução do comando da Figura 2 sobre `evidence2.dd`
- **Identificador:** P16
- **Selo e reivindicação relacionados:** Selo R — C6
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -v -x evidence2.dd
  ```
  *(Nota: comando exato exibido no topo da Figura 2 em `[artigo.pdf:p.8]`).*
- **Resultado esperado segundo os autores:** Processamento do arquivo `evidence2.dd` (`Length: 2 GB (2845109643 bytes)`) e exibição/registro no `audit.txt` da tabela da Figura 2 (`[artigo.pdf:p.8]`) contendo os 12 arquivos recuperados nos respectivos offsets:
  - `0: 00004352.elf` (Size: `57 KB`, Offset: `2228224`)
  - `1: 00004820.elf` (Size: `57 KB`, Offset: `2467840`)
  - `2: 00005108.elf` (Size: `1 KB`, Offset: `2615296`)
  - `3: 00005492.script` (Size: `3 KB`, Offset: `2811904`)
  - `4: 00399084.exe` (Size: `600 KB`, Offset: `204740608`)
  - `5: 00405008.exe` (Size: `52 KB`, Offset: `207380720`)
  - `6: 00414932.exe` (Size: `2 MB`, Offset: `212445184`)
  - `7: 00428728.exe` (Size: `2 MB`, Offset: `219508736`)
  - `8: 00442520.exe` (Size: `536 KB`, Offset: `226570240`)
  - `9: 00447356.exe` (Size: `600 KB`, Offset: `229046272`)
  - `10: 01786182.zip` (Size: `5 MB`, Offset: `909404319`)
  - `11: 01797042.zip` (Size: `350 KB`, Offset: `914965615`)
- **Evidência a salvar:** Saída de erro do comando (`p16_c6_fig2.log`) comprovando que `evidence2.dd` não está presente no artefato (`[!] File not found or is a directory: evidence2.dd` / `[!] No valid input files to process.`, conforme `[src/main.c:250,256]`).
- **Critério de sucesso:** Reprodução dos 12 arquivos e seus offsets exatos conforme a Figura 2 (`[reivindicacoes.md:21]`).
- **Critério de falha:** Erro `[!] File not found or is a directory: evidence2.dd` (pois o arquivo `evidence2.dd` não foi incluído no pacote nem disponibilizado pelos autores) ou divergência nos arquivos/offsets extraídos.
- **Critério de interrupção:** Como `evidence2.dd` não existe no pacote (`[artefato.txt:9-50]`), este passo falha imediatamente; pela regra de `[reivindicacoes.md:17]` (*"R é atribuído se C1 a C6 forem reproduzidas"*), a falha em C6 impede a atribuição do Selo R.

---

### Bloco C7 — Arquitetura de parsers extensível (Inspeção de Código)
**Reivindicação (`[reivindicacoes.md:13,17]`):** *Arquitetura de parsers extensível: despachante central e parsers com identificador, assinatura, validação e recuperação. (Contribuição arquitetural sem experimento associado; pode ser inspecionada, mas não entra na regra de R).*

#### Passo P17 — Inspeção estática da estrutura arquitetural no código-fonte `[NÃO DOCUMENTADO]`
- **Identificador:** P17
- **Selo e reivindicação relacionados:** Selo R — C7 (Inspeção arquitetural complementar)
- **Justificativa `[NÃO DOCUMENTADO]`:** O artigo não define um experimento de execução para C7 (`[reivindicacoes.md:17]`). A verificação do resultado esperado (*"organização do código correspondente à Fig. 1"*, `[reivindicacoes.md:13]`) é feita inspecionando os módulos de validação de entrada (`src/main.c`), motor de carving (`src/engine.c`), registro de parsers (`src/state.c`) e despachante de extração (`src/extract.c`).
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  grep -n "init_builtin(" state.c && grep -n "extract_file(" engine.c extract.c
  ```
- **Resultado esperado segundo os autores:** Presença dos módulos da Figura 1 (`CLI`, `Input validation`, `File carving engine`, `File extraction engine`) e registro de parsers (`EVTX`, `MACHO`, `ELF`, `SCRIPT`, etc.) acionados pelo despachante central (`[artigo.pdf:p.2-3, Fig. 1]`).
- **Evidência a salvar:** Saída do `grep` (`p17_c7_arch.log`).
- **Critério de sucesso:** Identificação das chamadas `init_builtin` em `src/state.c` e do despachante `extract_file` em `src/engine.c` e `src/extract.c`.
- **Critério de falha:** Ausência dos módulos ou dos parsers no código-fonte.
- **Critério de interrupção:** Fim do roteiro.

---

## 5. Tabela Resumo de Todos os Passos

| Passo | Documentado? | Selo / Reivindicação | Diretório | Comando Exato (Resumo) | Resultado Esperado | Evidência a Salvar | Critério de Sucesso | Critério de Falha | Critério de Interrupção | Tempo Est. |
|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | `[NÃO DOCUMENTADO]` no README (extraído do `Dockerfile`) | **F** (Ambiente) | `<raiz>` | `sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev file binutils python3` | Pacotes e bibliotecas instalados | `p1_apt_install.log` | Saída `0`; `gcc`, `make`, OpenSSL e libcurl presentes | Saída `!= 0` ou pacote ausente | Interromper se `gcc`, `libssl-dev` ou `libcurl4-openssl-dev` falharem | 2 min |
| **P2** | Sim (`README.md:33-34`, `Dockerfile:9-10`) | **F** (Compilação / Instalação) | `<raiz>/src` | `cd src && make && sudo make install` | Binário `foremost-ng` compilado e instalado em `/usr/local/bin` | `p2_build_install.log` | Saída `0` e binário executável criado | Erro de compilação ou linkedição | Interromper roteiro se o binário não for gerado | 1 min |
| **P3** | Sim (`README.md:79`, `src/main.c:92-165`) | **F** (Verificação CLI / Manpage) | `<raiz>/src` | `./foremost-ng -V && ./foremost-ng -h && man -P cat foremost-ng \| head -n 40` | Exibe versão `1.5.7`, opções `-h` (incluindo `-x`) e manpage | `p3_cli_help.log` | Execução sem erro e listagem das flags | Crash ou binário inoperante | Interromper se o binário não iniciar | 1 min |
| **P4** | `[NÃO DOCUMENTADO]` | **F** (Entrada p/ teste mínimo) | `<raiz>/src` | Script Python gerando `disk.img` com binário ELF embutido | Arquivo `disk.img` criado | `p4_disk_img.log` | `disk.img` criado (> 10 KB) | `disk.img` ausente ou vazio | Interromper P5 se `disk.img` não existir | 1 min |
| **P5** | Sim (`artigo.pdf:p.7 §4.1`) | **F** (Teste mínimo) | `<raiz>/src` | `mkdir -p /temp/output && rm -rf /temp/output/carved && foremost-ng -i disk.img -o /temp/output/carved` | Extração em `/temp/output/carved` e geração de `audit.txt` | `p5_basic_usage.log` e `audit.txt` | Saída `0`, `audit.txt` criado e `>= 1` arquivo extraído | Erro de execução ou `0 FILES EXTRACTED` | Prosseguir para testes de R registrando resultado de F | 1 min |
| **P6** | `[NÃO DOCUMENTADO]` | **R — C1** (Prep. EVTX) | `<raiz>/src` | Script Python gerando `evtx_test.img` com assinatura `ElfFile\0` e chunk de 64 KiB | Arquivo `evtx_test.img` criado | `p6_evtx_prep.log` | `evtx_test.img` criado (73.728 B) | Falha ao criar `evtx_test.img` | Interromper P7 se `evtx_test.img` não existir | 1 min |
| **P7** | Parcial (`artigo.pdf:p.7`; validação `[NÃO DOCUMENTADO]`) | **R — C1** (Carving EVTX) | `<raiz>/src` | `rm -rf ./out_c1 && ./foremost-ng -v -t evtx -i evtx_test.img -o ./out_c1 && file ./out_c1/evtx/*.evtx` | Arquivo `.evtx` extraído em `./out_c1/evtx/` e legível | `p7_c1_evtx.log` e `./out_c1/audit.txt` | `.evtx` extraído no offset esperado e legível por analisador de eventos | `.evtx` não extraído ou corrompido/ilegível | Prosseguir para Bloco C2 | 2 min |
| **P8** | `[NÃO DOCUMENTADO]` | **R — C2** (Prep. Scripts) | `<raiz>/src` | Script Python gerando `script_test.img` com scripts Bash, Python e só-comentário | Arquivo `script_test.img` criado | `p8_script_prep.log` | `script_test.img` criado | Falha ao criar `script_test.img` | Interromper P9 se `script_test.img` não existir | 1 min |
| **P9** | `[NÃO DOCUMENTADO]` (`-t script` só no código) | **R — C2** (Carving Scripts) | `<raiz>/src` | `rm -rf ./out_c2 && ./foremost-ng -v -t script -i script_test.img -o ./out_c2 && head -n 20 ./out_c2/script/*.script` | Extração dos 2 scripts válidos (`>= 32` B, mais que comentários) | `p9_c2_script.log` e `./out_c2/audit.txt` | 2 arquivos `.script` legíveis com shebang; só-comentário ignorado | 0 extraídos, truncamento ou falso positivo | Prosseguir para Bloco C3 | 2 min |
| **P10** | `[NÃO DOCUMENTADO]` | **R — C3** (Prep. Mach-O) | `<raiz>/src` | Script Python gerando `macho_test.img` com binários Mach-O `thin` (4 KB) e `fat` (8 KB) | Arquivo `macho_test.img` criado | `p10_macho_prep.log` | `macho_test.img` criado | Falha ao criar `macho_test.img` | Interromper P11 se `macho_test.img` não existir | 1 min |
| **P11** | `[NÃO DOCUMENTADO]` (`-t macho` só no código) | **R — C3** (Carving Mach-O) | `<raiz>/src` | `rm -rf ./out_c3 && ./foremost-ng -v -t macho -i macho_test.img -o ./out_c3 && file ./out_c3/macho/*.macho` | Extração dos binários Mach-O `thin` e `fat` em `./out_c3/macho/` | `p11_c3_macho.log` e `./out_c3/audit.txt` | Binários `thin` e `fat` extraídos e reconhecidos por `file` | Não extração ou arquivo não reconhecido como Mach-O | Prosseguir para Bloco C4 | 2 min |
| **P12** | `[NÃO DOCUMENTADO]` | **R — C4** (Prep. `memory.dump` ELF) | `<raiz>/src` | Script Python gerando `memory.dump` com ELF32 (2 KB) e ELF64 (4 KB) | Arquivo `memory.dump` criado | `p12_elf_prep.log` | `memory.dump` criado | Falha ao criar `memory.dump` | Interromper P13 se `memory.dump` não existir | 1 min |
| **P13** | Parcial (`artigo.pdf:p.7`; `readelf` `[NÃO DOCUMENTADO]`) | **R — C4** (Carving ELF 32/64) | `<raiz>/src` | `rm -rf ./out_c4 && ./foremost-ng -v -t elf -i memory.dump -o ./out_c4 && file ./out_c4/elf/*.elf && readelf -h -l ./out_c4/elf/*.elf` | Extração de ELF32 e ELF64 delimitados por `PT_LOAD` | `p13_c4_elf.log` e `./out_c4/audit.txt` | ELF32 e ELF64 extraídos e cabeçalhos legíveis por `readelf -h -l` | Falha na extração ou erro estrutural no `readelf` | Prosseguir para Bloco C5 | 2 min |
| **P14** | Sim (`artigo.pdf:p.7 §4.1`) | **R — C5** (VT sem `VT_API_KEY`) | `<raiz>/src` | `unset VT_API_KEY && rm -rf ./carved-files-nokey && ./foremost-ng -v -x -t elf -i memory.dump -o ./carved-files-nokey` | Aviso de chave ausente em `stderr` e carving concluído sem consulta | `p14_c5_vt_nokey.log` | Mensagem `Error: VT_API_KEY environment variable is not set.` e arquivos extraídos | Aborto do carving ou ausência de aviso | Prosseguir para P15 | 1 min |
| **P15** | Sim (`README.md:101`, `artigo.pdf:p.7 §4.1`) | **R — C5** (VT com `VT_API_KEY`) | `<raiz>/src` | `export VT_API_KEY="<CHAVE>" && rm -rf ./carved-files && ./foremost-ng -v -x -t elf -i memory.dump -o ./carved-files` | Consulta SHA-256 no VirusTotal e registro na coluna `VT` do `audit.txt` | `p15_c5_vt_withkey.log` e `audit.txt` | Coluna `VT` preenchida com `Clean (...)` ou `Malicious (...)` | Erro `curl` ou coluna `VT` permanecendo `N/A` | Pular se não houver `VT_API_KEY` ou internet; ir a P16 | 2 min |
| **P16** | Sim (`artigo.pdf:p.8, Fig. 2`) | **R — C6** (Reprodução da Fig. 2) | `<raiz>/src` | `./foremost-ng -v -x evidence2.dd` | Tabela da Fig. 2 com 12 arquivos (`elf`, `script`, `exe`, `zip`) e offsets exatos | `p16_c6_fig2.log` | Extração dos 12 arquivos nos offsets exatos da Fig. 2 | `[!] File not found or is a directory: evidence2.dd` (dado ausente no pacote) | Falha imediata por ausência de `evidence2.dd` (inviabiliza Selo R) | 1 min |
| **P17** | `[NÃO DOCUMENTADO]` | **R — C7** (Inspeção da arquitetura) | `<raiz>/src` | `grep -n "init_builtin(" state.c && grep -n "extract_file(" engine.c extract.c` | Confirmação dos módulos da Fig. 1 e registro de parsers | `p17_c7_arch.log` | Localização do registro em `state.c` e despachante em `engine.c`/`extract.c` | Módulos ausentes | Fim do roteiro | 1 min |
