# Cadeia FN-1 — google

- provedor: google
- modelo_exibido: Gemini Pro (High)
- versao: gemini-pro (Antigravity desktop)
- esforco: High
- interface: Antigravity (desktop), subagente isolado (`revisor-cega-gemini`, conversa `c50a3f54-b004-4345-a74c-4d49bc79770d`) com acesso somente-leitura restrito aos anexos do pacote e ao registro factual; sem memória entre conversas; busca na web desativada
- data_hora_A: 2026-10-17 13:53 BRT
- data_hora_B1: 2026-10-17 13:58 BRT
- data_hora_B2: 2026-10-17 23:26 BRT
- anexos_A: artigo.pdf=d9b12aa44caeab3d8374fd9ad092c3b9ecec1f18d589125f0ca2f8d00dc9e715, artefato.txt=6de9ecff1194121da658fd3684742c0b2a42b7899ed73b7d3649b9e928330446, instrucoes-oficiais.md=446e5f94605b2fe60ac9c4028f7be57b0488bc79c3c8ef2ef782428f8e290a47, reivindicacoes.md=3d27bc26b64ae7c16272dc9d7a68c25ccacf98d82dbfcdc5bfd7d3ab7932dbac
- anexo_B2: registro-factual.md=2041606f1236e737f2b6191d2ff9f06944c7fea87f32996f0f12fff2d51281fb
- metodo_exportacao: transcrição integral gerada a partir do log oficial da sessão isolada (`c50a3f54-b004-4345-a74c-4d49bc79770d`, `transcript_full.jsonl`); blocos de texto de prompts e respostas sem alteração; raciocínio e saídas de ferramentas omitidos
- desvios: resposta A usou 13 chamada(s) de ferramenta somente-leitura para abrir os 4 anexos: view_file ("Read instrucoes-oficiais.md"); view_file ("Read reivindicacoes.md"); view_file ("Read artigo.pdf"); view_file ("Read start of artefato.txt"); view_file ("Read artefato.txt 251-1050"); view_file ("Read artefato.txt 1051-1850"); view_file ("Read artefato.txt 1851-2650"); view_file ("Read artefato.txt 2651-3450"); view_file ("Read artefato.txt 3451-4250"); view_file ("Read artefato.txt 4251-5050"); view_file ("Read artefato.txt 5051-5850"); view_file ("Read artefato.txt 5851-6650"); view_file ("Read artefato.txt 6651-7331") | resposta A contém raciocínio (thinking) omitido nesta transcrição | resposta B1 contém raciocínio (thinking) omitido nesta transcrição | resposta B2 usou 2 chamada(s) de ferramenta somente-leitura para abrir o registro factual: view_file ("Read registro-factual.md"); view_file ("Read end of registro-factual.md") | resposta B2 contém raciocínio (thinking) omitido nesta transcrição

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

Foram abertos e examinados exclusivamente os 4 arquivos anexados do pacote:
1. `d:\Github\t8-leas\runs\foremost-ng\pacote\instrucoes-oficiais.md`
2. `d:\Github\t8-leas\runs\foremost-ng\pacote\reivindicacoes.md`
3. `d:\Github\t8-leas\runs\foremost-ng\pacote\artigo.pdf`
4. `d:\Github\t8-leas\runs\foremost-ng\pacote\artefato.txt`

---

### B. Selo F (Funcional)

#### 1. Critérios oficiais aplicáveis
Conforme `[instrucoes-oficiais.md:13-15]`:
> "O artefato precisa ser executável e permitir a observação de funcionalidades. O README deve informar dependências, versões de dependências/linguagens/ambiente, ambiente de execução, instalação, execução e pelo menos um exemplo mínimo. O revisor deve **executar** o artefato e apresentar prova de execução e saídas no parecer. Ler código ou README, por si só, não constitui prova de funcionamento."

#### 2 e 3. Avaliação por critério e evidências

- **Critério F1 — Informar dependências:** **Atendido na documentação** (parcialmente no `README.md`, mas complementado pelo `Dockerfile` e pelo `src/Makefile`).
  - `[README.md:39-43]` (`[artefato.txt:187-191]`): `"Make sure curl is installed: / pkg_add curl # OpenBSD / pkg install curl # FreeBSD"`.
  - `[README.md:52-55]` (`[artefato.txt:200-203]`): `"Install OpenSSL: / brew install openssl@3"`.
  - `[README.md:64-68]` (`[artefato.txt:212-216]`): `"Install MinGW in your Linux distribution and cross-compile: / make cross / Required DLLs can be found in the windows_dlls directory of this repository."`.
  - `[README.md:17]` (`[artefato.txt:165]`): `"VirusTotal lookup by file hash (requires a VT API key)."`.
  - `[Dockerfile:4-5]` (`[artefato.txt:113-114]`): `"&& DEBIAN_FRONTEND=noninteractive apt-get install -y \ gcc make git libssl-dev libcurl4-openssl-dev \"` (documenta os pacotes de compilação no Linux omitidos em `[README.md:31-35]`).
  - `[src/Makefile:46]` (`[artefato.txt:316]`): `"LINK_OPT += -lssl -lcrypto -lcurl"`.

- **Critério F2 — Informar versões de dependências/linguagens/ambiente:** **Atendido na documentação** (de forma mínima).
  - `[README.md:54]` (`[artefato.txt:202]`): `"brew install openssl@3"`.
  - `[README.md:70]` (`[artefato.txt:218]`): `"> **Note:** On systems with glibc < 2.2.0, you may see harmless warnings about ftello and fseeko."`.
  - `[Dockerfile:1]` (`[artefato.txt:110]`): `"FROM ubuntu:latest"`.
  - `[src/Makefile:4]` (`[artefato.txt:274]`): `"VERSION = 1.5.7"`.
  - `[artefato.txt:36-37, 45]`: DLLs pré-compiladas para Windows com versões explícitas no nome (`windows_dlls/libcrypto-3-x64.dll`, `windows_dlls/libcurl-4.dll`, `windows_dlls/libssl-3-x64.dll`).

- **Critério F3 — Informar ambiente de execução:** **Atendido na documentação**.
  - `[README.md:3]` (`[artefato.txt:151]`): `"`foremost-ng` is a Linux-based file recovery tool that extracts files from disk images or devices by scanning for configurable file headers and footers."`.
  - `[README.md:31-68]` (`[artefato.txt:179-216]`): seções de compilação/execução para `"### Linux"`, `"### BSD"`, `"### macOS"` e `"### Cross compiling for Windows"`.
  - `[Dockerfile:1-12]` (`[artefato.txt:110-121]`): definição completa de contêiner Ubuntu.

- **Critério F4 — Instruções de instalação:** **Atendido na documentação**.
  - `[README.md:27-35]` (`[artefato.txt:175-183]`): `"tar xzvf foremost-ng-<version>.tar.gz / cd foremost-ng-<version>/src / make / sudo make install"`.
  - `[Dockerfile:8-10]` (`[artefato.txt:117-119]`): `"RUN git clone https://github.com/cristianzsh/foremost-ng.git /opt/foremost-ng / WORKDIR /opt/foremost-ng/src / RUN make && make install"`.
  - `[artigo.pdf:p. 6, §4]`: `"git clone https://github.com/cristianzsh/foremost-ng.git / cd foremost-ng / make / sudo make install"`.

- **Critério F5 — Instruções de execução e pelo menos um exemplo mínimo:** **Atendido na documentação** (sintaxe básica no `README.md` com capturas de tela e página de manual; exemplos concretos no `artigo.pdf`).
  - `[README.md:76-85]` (`[artefato.txt:224-233]`): `"Run foremost-ng with the appropriate command-line options. For full details, refer to the manual page: man foremost-ng / Basic syntax: foremost-ng [options] [image_or_device]"`.
  - `[README.md:6-7]` (`[artefato.txt:154-155]`): `"<img src="screenshots/foremost-ng-01.png"/> / <img src="screenshots/foremost-ng-02.png"/>"`.
  - `[README.md:91-108]` (`[artefato.txt:239-256]`): instruções para a flag `-x` e `"export VT_API_KEY=yourkey"`.
  - `[artigo.pdf:p. 7, §4.1]`: exemplos concretos `"foremost-ng -i disk.img -o /temp/output/carved"`, `"foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved"` e `"foremost-ng -x -t elf -i memory.dump -o ./carved-files"`.

- **Critério F6 — Executabilidade, observação de funcionalidades e prova de execução com saídas:** **Só verificável por execução**.
  - `[instrucoes-oficiais.md:15]`: `"O revisor deve **executar** o artefato e apresentar prova de execução e saídas no parecer. Ler código ou README, por si só, não constitui prova de funcionamento."`.
  - `[artefato.txt:16-33]` e `[src/main.c:197-304]` (`[artefato.txt:5714-5821]`): todo o código-fonte em C e o `Makefile` estão presentes, porém a confirmação de compilação sem erros e funcionamento real depende de execução.

#### 4. Decisão para o Selo F
**Indeterminado**. Nenhum critério obrigatório falha de forma impeditiva na documentação (considerando `README.md`, `Dockerfile`, `src/Makefile` e `artigo.pdf`), mas a decisão exige execução do artefato e verificação das saídas.

#### 5. Confiança na atribuição pelo comitê oficial
**85** (em 100) de que o comitê oficial atribuiu o Selo F, pois o código-fonte em C está completo, acompanhado de `Makefile` funcional e `Dockerfile` que instala explicitamente `gcc`, `make`, `libssl-dev` e `libcurl4-openssl-dev`.

#### 6. O que precisaria ser observado na execução para mudar a decisão
- **Para mudar para Atribuir:** compilar o binário em `src/` (`make`) sem erros, executar `foremost-ng` sobre uma imagem de teste (como uma imagem do DFTT citada em `[artigo.pdf:p. 7, §4]` ou imagem sintética contendo arquivos suportados) e observar a geração do diretório de saída, do arquivo `audit.txt` e dos arquivos extraídos.
- **Para mudar para Não atribuir:** falha de compilação/linkedição no ambiente indicado ou erro fatal em tempo de execução (ex.: falha de segmentação ou incapacidade de extrair arquivos de uma imagem de entrada válida).

---

### C. Selo R (Reprodutível — por reivindicação)

#### 1. Critérios oficiais aplicáveis e regra do selo R
Conforme `[instrucoes-oficiais.md:17-19]`:
> "O revisor deve conseguir reproduzir as **principais reivindicações do artigo**. A documentação do artefato deve trazer instruções de execução dessas reivindicações e descrever o processo usado pelos autores para chegar aos resultados publicados. O revisor deve executar os experimentos e confrontar os resultados com os do artigo, incluindo figuras/tabelas pertinentes, resumindo a comparação no parecer."

Conforme `[reivindicacoes.md:17, 21]`:
> "O README não marca reivindicações a reproduzir. Por isso, valem as reivindicações principais desta lista: **C1 a C6**. **R é atribuído se C1 a C6 forem reproduzidas.** C7 é uma contribuição arquitetural, sem experimento associado no artigo; ela pode ser inspecionada, mas não entra na regra de R."
> "Uma reivindicação é reproduzida quando o resultado esperado da tabela é observado. Em C6, comparam-se os arquivos e offsets da Fig. 2. As contagens do VirusTotal mudam com o tempo e não precisam coincidir."

#### 2 e 3. Avaliação dos critérios gerais de R e de cada reivindicação (C1 a C7)

- **Critério geral R1 — Instruções de execução das reivindicações na documentação do artefato e descrição do processo usado pelos autores para chegar aos resultados publicados:** **Não atendido**.
  - `[README.md:74-108]` (`[artefato.txt:222-256]`): o `README.md` apresenta apenas `"foremost-ng [options] [image_or_device]"` e `"export VT_API_KEY=yourkey"`, sem descrever comandos ou passos para reproduzir C1–C6, sem mencionar os novos formatos (`evtx`, `script`, `macho`, `elf`) e sem documentar como a imagem `evidence2.dd` da Figura 2 foi gerada ou onde obtê-la.
  - `[reivindicacoes.md:7-13]`: registra que o `README.md` indica como reproduzir apenas de forma `"parcial"` para C1–C5 e `"não"` para C6 e C7.
  - `[artefato.txt:9-49]`: o índice completo do pacote comprova que não há imagens de disco (`.dd`, `.img`, `.dump`), arquivos de amostra ou scripts de teste no repositório.

- **Critério geral R2 — Reprodução experimental das reivindicações principais C1 a C6 e confronto com resultados/figuras do artigo:** **Não atendido** (inviável para C6 por ausência do dado de entrada `evidence2.dd`; **só verificável por execução** para C1 a C5).

##### Avaliação individual por reivindicação:

1. **C1 — Recuperação de logs de eventos do Windows (EVTX):** **`depende_execucao`**
   - *Critério documental:* Parcialmente atendido no artigo (`[artigo.pdf:p. 6, §3; p. 7, §4.1]`: `"foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved"`), mas ausente no `README.md` e sem amostra `.evtx` no pacote (`[artefato.txt:9-49]`).
   - *Evidência no código:* `[src/state.c:381-382]` (`[artefato.txt:6694-6695]`): `"init_builtin(state, EVTX, "evtx", "ElfFile\0\0", NULL, 8, 0, 100 * MEGABYTE, TRUE);"` e `[src/extract.c:2458-2517]` (`[artefato.txt:4528-4585]`): função `extract_evtx` verifica `"if (memcmp(buf, "ElfFile\0\0", 8) != 0)"`, lê `"chunk_count = htoi(&buf[0x18], FOREMOST_LITTLE_ENDIAN);"`, calcula `"full_size = (uint64_t)chunk_count * 65536ULL;"`, busca o próximo cabeçalho `"ElfFile\0\0"` e grava o arquivo `.evtx`.
   - *Observação:* Verificar se o arquivo `.evtx` extraído é efetivamente legível por uma ferramenta de análise de eventos (especialmente porque o cálculo `chunk_count * 65536ULL` lê o offset `0x18` e não soma separadamente os 4 KiB do cabeçalho `ElfFile` quando todos os chunks são extraídos) só é verificável por execução.

2. **C2 — Recuperação de scripts (Bash, Python, PowerShell):** **`depende_execucao`**
   - *Critério documental:* Descrito em `[artigo.pdf:p. 6, §3]`, mas não documentado no `README.md` nem acompanhado de imagem de teste no pacote (`[artefato.txt:9-49]`).
   - *Evidência no código:* `[src/state.c:384-385]` (`[artefato.txt:6697-6698]`): `"init_builtin(state, SCRIPT, "script", "#!", NULL, 2, 0, 2 * MEGABYTE, TRUE);"` e `[src/extract.c:2519-2622]` (`[artefato.txt:4587-4690]`): função `extract_script` define `"const uint64_t MIN_SCRIPT_SIZE = 32;"`, varre caracteres imprimíveis (`"if (isprint(c) || c == '\n' || c == '\r' || c == '\t')"`), verifica `carve_len < MIN_SCRIPT_SIZE` e exige ao menos um caractere após a primeira quebra de linha que não seja espaço nem `'#'` (`"if (*p != '#') { found_real = 1; break; }"`).
   - *Observação:* A extração do script com linha do interpretador e corpo legível depende de execução sobre imagem de entrada.

3. **C3 — Recuperação de binários Mach-O `fat` e `thin`:** **`depende_execucao`**
   - *Critério documental:* Descrito em `[artigo.pdf:p. 6, §3]`, sem instruções específicas ou amostras no `README.md` (`[artefato.txt:148-268]`).
   - *Evidência no código:* `[src/state.c:372-380]` (`[artefato.txt:6685-6693]`): registra as assinaturas `"\xCA\xFE\xBA\xBE"`, `"\xCE\xFA\xED\xFE"` e `"\xCF\xFA\xED\xFE"`. Em `[src/extract.c:2314-2455]` (`[artefato.txt:4382-4523]`), `extract_macho` trata binários FAT (`"if (buf[0] == 0xCA && buf[1] == 0xFE && buf[2] == 0xBA && buf[3] == 0xBE)"`, lendo `nfat_arch`, `arch_fileoff` e `arch_size`), Mach-O 32 bits (`"if (magic_le == 0xCEFAEDFE)"`, `cmd == 0x1`) e Mach-O 64 bits (`"if (magic_le == 0xCFFAEDFE)"`, `"if (cmd == 0x19 /* LC_SEGMENT_64 */)"`).
   - *Observação:* Verificar se o binário `.macho` extraído é reconhecível por ferramenta apropriada depende de execução.

4. **C4 — Recuperação de executáveis ELF de 32 e 64 bits:** **`depende_execucao`**
   - *Critério documental:* Descrito em `[artigo.pdf:p. 6, §3; p. 7, §4.1]` (`"foremost-ng -x -t elf -i memory.dump -o ./carved-files"`), sem amostras de teste no pacote (`[artefato.txt:9-49]`).
   - *Evidência no código:* `[src/state.c:369-370]` (`[artefato.txt:6682-6683]`): `"init_builtin(state, ELF, "elf", "\x7F\x45\x4C\x46", NULL, 4, 0, 50 * MEGABYTE, TRUE);"`. Em `[src/extract.c:2147-2309]` (`[artefato.txt:4215-4377]`), `extract_elf` valida `"if (buf[0] != 0x7F || buf[1] != 'E' || buf[2] != 'L' || buf[3] != 'F')"`, diferencia `ei_class == 1` (32 bits) e `ei_class == 2` (64 bits), percorre a tabela de cabeçalhos de programa buscando `"if (p_type_32 == 1 /* PT_LOAD */)"` e `"if (p_type_64 == 1 /* PT_LOAD */)"`, calcula `max_seg_end = p_offset + p_filesz` e grava o arquivo `.elf`.
   - *Observação:* A verificação estrutural por analisador ELF do arquivo extraído depende de execução.

5. **C5 — Enriquecimento pelo VirusTotal (`-x` e `VT_API_KEY`):** **`depende_execucao`**
   - *Critério documental:* Atendido na documentação em `[README.md:89-108]` (`[artefato.txt:237-256]`) e `[artigo.pdf:p. 3, §2; p. 7, §4 e §4.1]`.
   - *Evidência no código:* `[src/dir.c:275-283]` (`[artefato.txt:1565-1573]`): `"if (get_mode(s, mode_virustotal)) { ... sha_checksum(fn, "sha256", sha256); vt = vt_check_hash(sha256); snprintf(nd->vt_label, sizeof(nd->vt_label), vt.is_malicious ? "Malicious (%d)" : "Clean (%d)", ...); }"`. Em `[src/vt_query.c:136-198]` (`[artefato.txt:7211-7273]`), `vt_check_hash` valida `"if (api_key == NULL || strlen(api_key) == 0) { fprintf(stderr, "Error: VT_API_KEY environment variable is not set.\n"); return result; }"`, consulta `"https://www.virustotal.com/api/v3/files/"` com cabeçalho `"x-apikey: %s"` e extrai contagens com `"sscanf(stats, "\"last_analysis_stats\": {\"malicious\": %d, \"suspicious\": %*d, \"undetected\": %d", &malicious, &undetected);"`.
   - *Observação:* A confirmação do funcionamento da requisição HTTP à API v3 do VirusTotal e do parsing via `sscanf` sobre o JSON real retornado depende de execução.

6. **C6 — Exemplo de execução da Figura 2 (`./foremost-ng -v -x evidence2.dd`):** **`nao_reproduzivel`**
   - *Critério documental e de dados:* **Não atendido**.
   - *Evidência:* `[artigo.pdf:p. 8, Fig. 2]` exibe a execução `"$ ./foremost-ng -v -x evidence2.dd"` sobre o arquivo `"File: evidence2.dd"` de tamanho `"Length: 2 GB (2045109643 bytes)"`, extraindo 12 arquivos (`00004352.elf` a `01787042.zip`) em offsets específicos (`2228224` a `914965615`). Contudo, `[artefato.txt:9-49]` mostra que `evidence2.dd` não faz parte do artefato, `[reivindicacoes.md:12]` confirma que o README não indica como reproduzir C6 (`"não"`), e nem o `README.md` nem o `artigo.pdf` fornecem link de download, script gerador ou instruções para obter `evidence2.dd`. Sem esse arquivo de entrada, é impossível reproduzir os arquivos e offsets da Figura 2 exigidos em `[reivindicacoes.md:12, 21]`.

7. **C7 — Arquitetura de parsers extensível (contribuição arquitetural; fora da regra de R conforme `[reivindicacoes.md:17]`):** **`reproduzivel`** (por inspeção de código, com ressalvas)
   - *Evidência:* O pipeline de alto nível da Figura 1 (`[artigo.pdf:p. 3, Fig. 1]`: CLI -> Input validation -> File carving engine -> File extraction engine) corresponde à organização em `[src/main.c:178-304]` (`is_valid_input`, `process_command_line`), `[src/engine.c:235-412]` (`search_chunk`, `search_stream`) e `[src/extract.c:2628-2697]` (`extract_file`). Ressalva-se que, diferentemente do texto de `[artigo.pdf:p. 3, §2]` (que menciona callbacks de validação/recuperação registrados por parser), a estrutura `s_spec` em `[src/main.h:262-280]` (`[artefato.txt:6086-6104]`) não possui ponteiros de função, e o despacho em `[src/extract.c:2628-2697]` (`[artefato.txt:4696-4765]`) e `[src/state.c:408-714]` (`[artefato.txt:6721-7027]`) é feito por cadeias `if / else if` centralizadas. Conforme `[reivindicacoes.md:17]`, C7 não entra na regra de atribuição de R.

#### 4. Decisão para o Selo R
**Não atribuir**. Há evidência direta de que critérios obrigatórios para o Selo R não são atendidos: falta o dado de entrada necessário (`evidence2.dd`) para reproduzir a reivindicação principal **C6** (`[artigo.pdf:p. 8, Fig. 2]`, `[artefato.txt:9-49]`, `[reivindicacoes.md:12, 17, 21]`), além de o `README.md` não conter instruções de reprodução dos experimentos do artigo (`[instrucoes-oficiais.md:19]`). Como a regra estabelece que **"R é atribuído se C1 a C6 forem reproduzidas"** (`[reivindicacoes.md:17]`), a impossibilidade de reproduzir C6 impede a atribuição do selo R.

#### 5. Confiança na atribuição pelo comitê oficial
**15** (em 100) de que o comitê oficial atribuiu o Selo R (isto é, 85% de confiança de que o comitê oficial **não** atribuiu o Selo R, dada a ausência de dados experimentais, scripts de teste e instruções de reprodução dos resultados do artigo no repositório).

#### 6. O que precisaria ser observado na execução para mudar a decisão
- Como a falha em C6 decorre da ausência do arquivo `evidence2.dd` no artefato e na documentação, a mera execução do pacote atual não mudaria a decisão de **Não atribuir**. Para que a decisão pudesse mudar para **Atribuir** durante o processo de avaliação do comitê, seria necessário que: (1) os autores disponibilizassem a imagem `evidence2.dd` (por exemplo, na fase de esclarecimentos prevista em `[instrucoes-oficiais.md:11]`) ou ficasse demonstrado onde obtê-la; (2) a execução de `./foremost-ng -v -x evidence2.dd` reproduzisse os 12 arquivos e respectivos offsets da Figura 2 (`[artigo.pdf:p. 8, Fig. 2]`); e (3) a execução de testes para C1 a C5 confirmasse a extração íntegra de arquivos `.evtx`, `.script`, `.macho` e `.elf` e o funcionamento da consulta ao VirusTotal.

---

### D. Lacunas e riscos

1. **Ausência completa de imagens de teste e de `evidence2.dd` (`[artefato.txt:9-49]`, `[artigo.pdf:p. 8, Fig. 2]`):** O repositório não inclui `evidence2.dd` nem pequenas imagens/amostras para testar os novos parsers (`evtx`, `script`, `macho`, `elf`). A referência genérica a `https://dftt.sourceforge.net` em `[artigo.pdf:p. 7, §4]` aponta para imagens antigas do projeto DFTT e não fornece a imagem `evidence2.dd` usada na Figura 2.
2. **Omissão de dependências de compilação Linux no `README.md` (`[README.md:31-35]` vs. `[Dockerfile:4-5]`):** Na seção Linux do `README.md`, não são informados os pacotes `libssl-dev` e `libcurl4-openssl-dev` exigidos por `-lssl -lcrypto -lcurl` em `[src/Makefile:46]`, embora estejam documentados em `[Dockerfile:4-5]`.
3. **Pequena divergência de diretório na compilação (`[artigo.pdf:p. 6, §4]` vs. `[README.md:28]`):** O artigo instrui `cd foremost-ng && make`, mas o `Makefile` reside em `src/Makefile` (`[artefato.txt:16]`), exigindo `cd src` como documentado em `[README.md:28]` e `[Dockerfile:9]`.
4. **Divergência no nome do arquivo de log no artigo (`[artigo.pdf:p. 7, §4.2]` vs. `[src/main.h:162]`):** A Seção 4.2 do artigo menciona a geração de `"A recovery.log summarizing each extraction"`, mas o código gera exclusivamente `"audit.txt"` (`[src/main.h:162]`, `[artefato.txt:5986]`), conforme mencionado na própria Seção 3/4.1 do artigo.
5. **Fragilidades técnicas potenciais nos parsers e módulo VT (riscos na execução de C1–C5):**
   - Em `read_le64` (`[src/helpers.c:360-362]`, `[artefato.txt:5504-5506]`), a função chama `htoi(buf, FOREMOST_LITTLE_ENDIAN)` (32 bits) em vez de `htoll` (64 bits), truncando valores de 64 bits maiores ou iguais a 4 GiB em ELF64/Mach-O 64.
   - Em `extract_evtx` (`[src/extract.c:2479-2490]`, `[artefato.txt:4547-4558]`), lê-se `chunk_count` no offset `0x18` (que no formato EVTX corresponde ao `HeaderBlockSize`, enquanto o número de chunks de 16 bits fica em `0x2A`) e calcula-se `chunk_count * 65536ULL`, o que pode gerar arquivos `.evtx` com tamanho incorreto caso não haja outro cabeçalho `ElfFile` subsequente.
   - Em `vt_check_hash` (`[src/vt_query.c:180-181]`, `[artefato.txt:7255-7256]`), o parsing de JSON via `sscanf` depende da ordem exata das chaves `"malicious"`, `"suspicious"` e `"undetected"` na resposta da API v3 do VirusTotal; se a ordem variar, `malicious` e `undetected` permanecem `-1` e o arquivo é rotulado como `"Clean (-1)"`.
   - Quando `VT_API_KEY` está ausente com `-x`, `vt_check_hash` imprime erro no `stderr` (`[src/vt_query.c:141]`), mas `write_to_disk` (`[src/dir.c:279-282]`) ainda preenche a coluna VT do `audit.txt` com `"Clean (0)"` em vez de `"N/A"`.

```json
{"F": {"decisao": "Indeterminado", "confianca": 85, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:3-85", "README.md:89-108", "Dockerfile:1-12", "src/Makefile:1-124", "src/main.c:92-304", "artigo.pdf:p. 6-7, §4"]},
 "R": {"decisao": "Não atribuir", "confianca": 15, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:7-21", "artefato.txt:9-49", "README.md:74-108", "artigo.pdf:p. 7-8, §4.2 e Fig. 2", "src/extract.c:2147-2697", "src/state.c:321-714", "src/dir.c:275-283", "src/vt_query.c:136-198"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao", "C3": "depende_execucao", "C4": "depende_execucao", "C5": "depende_execucao", "C6": "nao_reproduzivel", "C7": "reproduzivel"}}}
```

## Prompt B1

Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.

## Resposta B1

# Roteiro de Execução e Verificação — Foremost-NG (Selos F e R)

> **Nota metodológica:** Este roteiro foi elaborado de forma estritamente analítica a partir de `artigo.pdf`, `artefato.txt` (commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`), `instrucoes-oficiais.md` e `reivindicacoes.md`. **Nenhum passo foi executado.** Passos ou comandos não fornecidos pelos autores estão explicitamente marcados como **`[NÃO DOCUMENTADO]`**, acompanhados da justificativa de sua necessidade.

---

## 1. Requisitos de Hardware e Software do Ambiente

### 1.1. Software
- **Sistema Operacional (documentado):** Linux (ex.: Ubuntu, conforme `Dockerfile:1`: `FROM ubuntu:latest`) ou sistema Unix-like em ambiente virtualizado (recomendado em `instrucoes-oficiais.md:10`). O `README.md:31-68` também lista BSD, macOS e compilação cruzada para Windows via MinGW.
- **Dependências de compilação e execução (documentadas em `Dockerfile:4-5` e `src/Makefile:46`, embora omitidas na seção Linux de `README.md:31-35`):**
  - `gcc` (compilador C)
  - `make`
  - `git`
  - `libssl-dev` (OpenSSL — cabeçalhos `openssl/evp.h` e bibliotecas `-lssl -lcrypto`)
  - `libcurl4-openssl-dev` (libcurl — cabeçalhos `curl/curl.h` e biblioteca `-lcurl`)
- **Serviço externo / Credencial (documentado em `README.md:91-108` e `artigo.pdf:p. 7, §4`):**
  - Conta gratuita no VirusTotal e chave de API na variável de ambiente `VT_API_KEY`, além de acesso de rede HTTPS a `https://www.virustotal.com/api/v3/files/` (necessário apenas para C5 e C6).
- **Utilitários auxiliares de verificação e geração de entradas `[NÃO DOCUMENTADO]`:**
  - `python3`, `file`, `binutils` (`readelf`): necessários porque o artefato (`artefato.txt:9-49`) não contém nenhuma imagem de disco de entrada nem scripts de teste, e `reivindicacoes.md:7-10` exige verificar se os arquivos `.evtx`, `.script`, `.macho` e `.elf` extraídos são estruturalmente legíveis por ferramentas apropriadas.

### 1.2. Hardware `[NÃO DOCUMENTADO]`
- **Justificativa:** Os autores não especificam requisitos mínimos de hardware no `README.md` nem no `artigo.pdf`.
- **Dimensionamento mínimo recomendado a partir do código:**
  - **CPU:** 1+ vCPU x86_64.
  - **Memória RAM:** mínimo de 2 GB livres (o motor de carving aloca buffers de `CHUNK_SIZE = 100` MB por padrão em `src/main.h:230` e `src/engine.c:383-384`).
  - **Disco:** mínimo de 1 GB livre para compilação e imagens sintéticas de teste (ou ~5 GB caso a imagem `evidence2.dd` de 2 GB da Figura 2 estivesse disponível).

### 1.3. Tempo Estimado de Execução
- **Preparação do ambiente e compilação (`P1`–`P2`):** ~3 a 5 minutos.
- **Teste mínimo para o Selo Funcional — F (`P3`–`P5`):** ~3 a 5 minutos.
- **Verificação por reivindicação para o Selo Reprodutível — R (`P6`–`P17`):** ~10 a 15 minutos.
- **Tempo total estimado:** **16 a 25 minutos**.

---

## 2. Preparação do Ambiente e Compilação (Base para F e R)

### Passo P1 — Instalação de dependências no Linux (`[NÃO DOCUMENTADO no README.md]`, documentado em `Dockerfile:3-6`)
- **Identificador:** P1
- **Status documental:** Documentado em `Dockerfile:3-6` para as bibliotecas de compilação; `[NÃO DOCUMENTADO]` quanto à inclusão de `python3`, `file` e `binutils`, necessários para criar imagens de teste ausentes no pacote e validar os binários extraídos em C1–C4.
- **Selo e reivindicação relacionados:** Selo F e Selo R (pré-requisito geral para C1 a C6)
- **Diretório:** `<raiz_do_artefato>`
- **Comando exato:**
  ```bash
  sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
      gcc make git libssl-dev libcurl4-openssl-dev \
      python3 file binutils
  ```
- **Resultado esperado segundo os autores:** Instalação sem erros do compilador GCC, `make` e bibliotecas de desenvolvimento OpenSSL e libcurl (`Dockerfile:3-6`).
- **Evidência a salvar:** Log completo da saída do `apt-get` (`p1_deps.log`) e versões instaladas (`gcc --version`, `openssl version`, `curl --version`).
- **Critério de sucesso:** Código de saída `0` e presença dos cabeçalhos `/usr/include/openssl/evp.h` e `/usr/include/curl/curl.h`.
- **Critério de falha:** Falha ao baixar ou instalar `gcc`, `make`, `libssl-dev` ou `libcurl4-openssl-dev`.
- **Critério de interrupção:** Interromper imediatamente todo o roteiro caso `gcc`, `make`, `libssl-dev` ou `libcurl4-openssl-dev` não possam ser instalados, pois a compilação em P2 é impossível sem eles (`src/Makefile:46`, `src/vt_query.c:13-14`).

### Passo P2 — Compilação e instalação do `foremost-ng` (Documentado em `README.md:28-35`, `Dockerfile:9-10`, `artigo.pdf:p. 6, §4`)
- **Identificador:** P2
- **Status documental:** Documentado em `README.md:28-35` e `Dockerfile:9-10`. *(Nota: `artigo.pdf:p. 6, §4` omite o subdiretório `src`, mas o `Makefile` está em `src/Makefile` conforme `artefato.txt:16`).*
- **Selo e reivindicação relacionados:** Selo F e Selo R (pré-requisito geral)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  cd src
  make
  sudo make install
  ```
- **Resultado esperado segundo os autores:** Compilação dos 10 arquivos `.c` gerando o binário `foremost-ng` em `src/` e instalação em `/usr/local/bin/foremost-ng`, `/usr/share/man/man8/foremost-ng.8.gz` e `/usr/local/etc/foremost.conf` (`src/Makefile:19-22, 107-119`; `artigo.pdf:p. 6-7, §4`).
- **Evidência a salvar:** Saída de compilação e instalação (`p2_build.log`) e saída de `ls -l ./foremost-ng /usr/local/bin/foremost-ng /usr/local/etc/foremost.conf`.
- **Critério de sucesso:** Código de saída `0` no `make` e no `sudo make install`, com criação do executável `./foremost-ng` e `/usr/local/bin/foremost-ng`.
- **Critério de falha:** Erro de compilação ou de linkedição (`undefined reference` ou cabeçalho ausente).
- **Critério de interrupção:** Interromper a avaliação prática de F e C1–C6 se o binário `foremost-ng` não for gerado.

---

## 3. Teste Mínimo — Selo Funcional (F)

### Passo P3 — Verificação de execução da CLI, versão e página de manual (Documentado em `README.md:79`, `src/main.c:92-112, 161-165`)
- **Identificador:** P3
- **Status documental:** Documentado em `README.md:78-80` (`man foremost-ng`) e implementado no binário em `src/main.c:92-112, 161-165` (`-h` e `-V`).
- **Selo e reivindicação relacionados:** Selo F (Funcionalidade básica da interface de linha de comando)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -V
  ./foremost-ng -h
  man foremost-ng | head -n 30
  ```
- **Resultado esperado segundo os autores:** `-V` exibe a versão `1.5.7` e informações de copyright (`src/main.c:163-164`); `-h` exibe o cabeçalho `foremost-ng version 1.5.7 by Cristian Souza.` e a lista de opções (`-V`, `-t`, `-d`, `-i`, `-a`, `-w`, `-o`, `-c`, `-q`, `-Q`, `-x`, `-v`); `man foremost-ng` abre a documentação instalada (`artigo.pdf:p. 7, §4`).
- **Evidência a salvar:** Saída do terminal (`p3_cli.log`).
- **Critério de sucesso:** Execução sem falhas de segmentação e exibição da versão e das opções de linha de comando.
- **Critério de falha:** Binário não executa, encerra com *crash* ou não reconhece as flags `-V` / `-h`.
- **Critério de interrupção:** Se o binário falhar ao exibir `-V` ou `-h`, interromper os testes seguintes e investigar a compilação.

### Passo P4 — Preparação de imagem de disco mínima `disk.img` (`[NÃO DOCUMENTADO]`)
- **Identificador:** P4
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** O artigo (`artigo.pdf:p. 7, §4.1`) apresenta o comando mínimo `foremost-ng -i disk.img -o /temp/output/carved`, mas `disk.img` não existe no repositório (`artefato.txt:9-49`). Embora `artigo.pdf:p. 7, §4` mencione que amostras podem ser baixadas de `https://dftt.sourceforge.net`, um passo local de criação de `disk.img` contendo um executável ELF do próprio sistema (o próprio `./foremost-ng`) e um script shell embutidos em offsets alinhados é indispensável para permitir o teste funcional mínimo de forma determinística e offline.
- **Selo e reivindicação relacionados:** Selo F (pré-requisito de entrada para o exemplo mínimo)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  with open("foremost-ng", "rb") as f:
      elf_data = f.read()
  script_data = b"#!/bin/bash\n# Script de teste\necho \"Foremost-NG functional test\"\n"
  img = bytearray(2 * 1024 * 1024)
  img[4096:4096+len(elf_data)] = elf_data
  img[524288:524288+len(script_data)] = script_data
  with open("disk.img", "wb") as out:
      out.write(img)
  '
  mkdir -p /temp/output
  rm -rf /temp/output/carved
  ```
- **Resultado esperado segundo os autores:** N/A (passo preparatório para suprir o arquivo `disk.img` pressuposto em `artigo.pdf:p. 7, §4.1`). Gera `disk.img` de 2 MiB com um ELF no offset `4096` e um script no offset `524288`.
- **Evidência a salvar:** Saída de `ls -lh disk.img` e hash SHA-256 de `disk.img` (`sha256sum disk.img > p4_disk_img.sha256`).
- **Critério de sucesso:** Arquivo `disk.img` criado com 2.097.152 bytes e diretório `/temp/output` existente sem `/temp/output/carved`.
- **Critério de falha:** Erro de permissão ou falta de espaço em disco ao criar `disk.img` ou `/temp/output`.
- **Critério de interrupção:** Interromper P5 se `disk.img` não for criado.

### Passo P5 — Execução do exemplo mínimo de carving (Documentado em `artigo.pdf:p. 7, §4.1`)
- **Identificador:** P5
- **Status documental:** Documentado literalmente em `artigo.pdf:p. 7, §4.1` (`foremost-ng -i disk.img -o /temp/output/carved`).
- **Selo e reivindicação relacionados:** Selo F (Exemplo mínimo de funcionamento)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -i disk.img -o /temp/output/carved
  cat /temp/output/carved/audit.txt
  ls -la /temp/output/carved/*
  ```
- **Resultado esperado segundo os autores:** Conforme `artigo.pdf:p. 7, §4.1 e §4.2`, todos os parsers registrados inspecionam os dados brutos sequencialmente, gerando o diretório `/temp/output/carved`, subdiretórios por formato encontrado (ex.: `elf/`, `script/`), os arquivos recuperados numerados sequencialmente pelo bloco e o arquivo de auditoria `audit.txt` (`src/main.h:162`, `src/dir.c:239-295`). *(Nota: `artigo.pdf:p. 7, §4.2` chama esse log de `recovery.log`, mas na página 6/7 e no código-fonte o arquivo gerado chama-se `audit.txt`).*
- **Evidência a salvar:** Cópia de `/temp/output/carved/audit.txt` e listagem dos arquivos extraídos (`p5_funcional.log`).
- **Critério de sucesso:** Execução termina com `[INFO] Processing finished.` (`src/engine.c:408`), código de saída `0`, `audit.txt` preenchido registrando `FILES EXTRACTED` >= 1 e arquivos extraídos presentes nos subdiretórios de `/temp/output/carved/`.
- **Critério de falha:** Programa falha ao abrir `disk.img`, encerra com erro (`EXIT_FAILURE`), não gera `audit.txt` ou extrai `0` arquivos.
- **Critério de interrupção:** Se P5 falhar completamente, o Selo F não é atendido; ainda assim, podem-se executar os passos específicos por formato (`-t`) em P6–P15 para diagnosticar quais módulos falham.

---

## 4. Verificação das Reivindicações — Selo Reprodutível (R)

Conforme `reivindicacoes.md:17`: *"O README não marca reivindicações a reproduzir. Por isso, valem as reivindicações principais desta lista: **C1 a C6**. **R é atribuído se C1 a C6 forem reproduzidas.** C7 é uma contribuição arquitetural, sem experimento associado no artigo; ela pode ser inspecionada, mas não entra na regra de R."*

---

### Bloco C1 — Recuperação de logs de eventos do Windows (EVTX)
> **Reivindicação C1 (`reivindicacoes.md:7`):** *"Recuperação de logs de eventos do Windows (EVTX): o parser reconhece a assinatura `ElfFile`, delimita os chunks de 64 KiB e extrai o log"* | **Resultado esperado:** *"arquivo `.evtx` extraído, legível por ferramenta de análise de eventos"*.

#### Passo P6 — Geração de imagem de disco com estrutura EVTX (`[NÃO DOCUMENTADO]`)
- **Identificador:** P6
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** Nem o `README.md` nem o `artefato.txt:9-49` fornecem um arquivo `.evtx` ou imagem de disco com logs de eventos do Windows. Para testar `extract_evtx` (`src/extract.c:2458-2517`), é necessário construir uma imagem contendo um arquivo `.evtx` sintético (ou real, se disponível no ambiente do avaliador) com cabeçalho `ElfFile\0` e chunk de 64 KiB (`ElfChnk\0`).
- **Selo e reivindicação relacionados:** Selo R / C1
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # Cria um container EVTX mínimo (cabeçalho 4 KiB + 1 chunk de 64 KiB)
  evtx_hdr = bytearray(4096)
  evtx_hdr[0:8] = b"ElfFile\x00"
  struct.pack_into("<Q", evtx_hdr, 0x08, 0)     # FirstChunkNumber
  struct.pack_into("<Q", evtx_hdr, 0x10, 1)     # LastChunkNumber
  struct.pack_into("<I", evtx_hdr, 0x18, 1)     # Offset 0x18 lido por extract_evtx como chunk_count
  struct.pack_into("<I", evtx_hdr, 0x20, 128)   # HeaderSize
  struct.pack_into("<H", evtx_hdr, 0x24, 1)     # MinorVersion
  struct.pack_into("<H", evtx_hdr, 0x26, 3)     # MajorVersion
  struct.pack_into("<H", evtx_hdr, 0x28, 4096)  # HeaderBlockSize
  struct.pack_into("<H", evtx_hdr, 0x2A, 1)     # NumberOfChunks (especificação EVTX)
  chunk = bytearray(65536)
  chunk[0:8] = b"ElfChnk\x00"
  img = bytearray(256 * 1024)
  offset = 8192
  img[offset:offset+4096] = evtx_hdr
  img[offset+4096:offset+4096+65536] = chunk
  with open("c1_evtx.img", "wb") as f:
      f.write(img)
  '
  rm -rf /tmp/out_c1
  ```
- **Resultado esperado segundo os autores:** N/A (preparação de imagem de entrada contendo assinatura `ElfFile\0\0` no offset `8192`).
- **Evidência a salvar:** Arquivo `c1_evtx.img` ou seu hash SHA-256.
- **Critério de sucesso:** `c1_evtx.img` criado com 262.144 bytes.
- **Critério de falha:** Erro na execução do script Python.
- **Critério de interrupção:** Interromper o Bloco C1 se `c1_evtx.img` não for criado.

#### Passo P7 — Execução do carving de EVTX e verificação do arquivo extraído (Parcialmente documentado em `artigo.pdf:p. 7, §4.1`)
- **Identificador:** P7
- **Status documental:** Comando `-t evtx` documentado em `artigo.pdf:p. 7, §4.1` (`foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved`); verificação do arquivo `.evtx` extraído marcada como `[NÃO DOCUMENTADO]` (necessária para aferir o resultado esperado de `reivindicacoes.md:7`).
- **Selo e reivindicação relacionados:** Selo R / C1
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -v -t evtx -i c1_evtx.img -o /tmp/out_c1
  cat /tmp/out_c1/audit.txt
  file /tmp/out_c1/evtx/*.evtx
  python3 -c '
  import glob
  files = glob.glob("/tmp/out_c1/evtx/*.evtx")
  assert len(files) == 1, f"Esperado 1 arquivo .evtx, encontrado: {files}"
  data = open(files[0], "rb").read()
  print("Arquivo:", files[0], "Tamanho:", len(data), "Magic:", data[:8])
  assert data[:8] == b"ElfFile\x00"
  '
  ```
- **Resultado esperado segundo os autores:** `foremost-ng` identifica a assinatura `ElfFile`, extrai o arquivo `.evtx` em `/tmp/out_c1/evtx/00000016.evtx` (offset `8192`) e registra a extração em `audit.txt` (`artigo.pdf:p. 6, §3; p. 7, §4.1`).
- **Evidência a salvar:** `/tmp/out_c1/audit.txt`, o arquivo `.evtx` extraído e a saída de `file` (`p7_c1_evtx.log`).
- **Critério de sucesso:** Arquivo `.evtx` extraído em `/tmp/out_c1/evtx/` com assinatura `ElfFile\0` e reconhecido/legível por ferramenta de análise de eventos (`file` / `evtx_dump`, se instalado). *(Nota de atenção: em `src/extract.c:2479-2490`, o código lê `chunk_count` no offset `0x18` — que em um arquivo EVTX real padrão vale `4096` (`HeaderBlockSize`), enquanto `NumberOfChunks` fica em `0x2A` — e calcula `chunk_count * 65536ULL` sem somar os 4096 bytes do cabeçalho inicial; observar se com um `.evtx` real isso trunca os últimos 4 KiB ou extrai bytes excedentes).*
- **Critério de falha:** Nenhum arquivo `.evtx` extraído ou arquivo corrompido/ilegível por ferramentas de análise EVTX.
- **Critério de interrupção:** Seguir para o Bloco C2 independentemente do resultado.

---

### Bloco C2 — Recuperação de scripts (Bash, Python, PowerShell)
> **Reivindicação C2 (`reivindicacoes.md:8`):** *"Recuperação de scripts (Bash, Python, PowerShell) reconhecidos por shebang (`#!`) e conteúdo textual, com mínimo de 32 bytes e mais que só comentários"* | **Resultado esperado:** *"script extraído com a linha do interpretador e o corpo legível"*.

#### Passo P8 — Geração de imagem de disco com scripts de teste (`[NÃO DOCUMENTADO]`)
- **Identificador:** P8
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** O pacote não fornece imagem de disco contendo scripts para testar C2. É necessário criar uma imagem com scripts válidos (Bash e Python com `#!`, >= 32 bytes e comandos reais) e fragmentos inválidos (< 32 bytes ou apenas comentários) para verificar os critérios de `src/extract.c:2519-2622` e `artigo.pdf:p. 6, §3`.
- **Selo e reivindicação relacionados:** Selo R / C2
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  img = bytearray(128 * 1024)
  # Script 1 válido (Bash, >= 32 bytes, com corpo executável) no offset 4096
  s1 = b"#!/bin/bash\n# Valid bash script\necho \"Hello from carved bash script\"\nexit 0\n"
  # Script 2 válido (Python, >= 32 bytes, com corpo executável) no offset 16384
  s2 = b"#!/usr/bin/env python3\n# Valid python script\nimport sys\nprint(sys.version)\n"
  # Script 3 inválido (< 32 bytes) no offset 32768
  s3 = b"#!/bin/sh\necho ok\n"
  # Script 4 inválido (>= 32 bytes, mas apenas comentários) no offset 49152
  s4 = b"#!/bin/bash\n# apenas comentario 1\n# apenas comentario 2 longo\n"
  img[4096:4096+len(s1)] = s1
  img[16384:16384+len(s2)] = s2
  img[32768:32768+len(s3)] = s3
  img[49152:49152+len(s4)] = s4
  with open("c2_script.img", "wb") as f:
      f.write(img)
  '
  rm -rf /tmp/out_c2
  ```
- **Resultado esperado segundo os autores:** N/A (preparação de imagem com 2 scripts válidos e 2 falsos positivos que devem ser descartados pelo filtro de 32 bytes e de comentários).
- **Evidência a salvar:** Hash SHA-256 de `c2_script.img`.
- **Critério de sucesso:** `c2_script.img` criado com 131.072 bytes.
- **Critério de falha:** Erro ao criar `c2_script.img`.
- **Critério de interrupção:** Interromper o Bloco C2 se `c2_script.img` não for criado.

#### Passo P9 — Execução do carving de scripts e inspeção do conteúdo (`[NÃO DOCUMENTADO]` quanto à flag `-t script`)
- **Identificador:** P9
- **Status documental:** Sintaxe geral documentada em `README.md:84` e `artigo.pdf:p. 7, §4.1`; o identificador `-t script` é **`[NÃO DOCUMENTADO]`** no `README.md` e no `artigo.pdf`, sendo obtido diretamente de `src/state.c:695` (`else if (strcmp(ft, "script") == 0)`).
- **Selo e reivindicação relacionados:** Selo R / C2
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -v -t script -i c2_script.img -o /tmp/out_c2
  cat /tmp/out_c2/audit.txt
  head -n 20 /tmp/out_c2/script/*
  ```
- **Resultado esperado segundo os autores:** Extração apenas dos scripts válidos (>= 32 bytes e contendo mais do que comentários) em `/tmp/out_c2/script/` (`00000008.script` no offset `4096` e `00000032.script` no offset `16384`), preservando a linha do interpretador (`#!`) e o corpo legível (`artigo.pdf:p. 6, §3`; `reivindicacoes.md:8`).
- **Evidência a salvar:** `/tmp/out_c2/audit.txt` e conteúdo dos arquivos em `/tmp/out_c2/script/` (`p9_c2_script.log`).
- **Critério de sucesso:** Exatamente os 2 scripts válidos extraídos com shebang e corpo intactos, enquanto os fragmentos < 32 bytes e só com comentários são ignorados.
- **Critério de falha:** Não extração dos scripts válidos, truncamento do corpo ou extração indevida dos fragmentos inválidos.
- **Critério de interrupção:** Prosseguir para o Bloco C3.

---

### Bloco C3 — Recuperação de binários Mach-O `fat` e `thin`
> **Reivindicação C3 (`reivindicacoes.md:9`):** *"Recuperação de binários Mach-O `fat` e `thin`, usando o cabeçalho universal ou os comandos de carga para determinar o tamanho"* | **Resultado esperado:** *"binário Mach-O extraído e reconhecível por ferramenta apropriada"*.

#### Passo P10 — Geração de imagem de disco com binários Mach-O `fat` e `thin` (`[NÃO DOCUMENTADO]`)
- **Identificador:** P10
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** O pacote não inclui binários Mach-O nem imagens de disco macOS/iOS. Para verificar `extract_macho` (`src/extract.c:2314-2455`), é necessário embutir em uma imagem de teste um binário Mach-O `thin` de 64 bits (`0xCFFAEDFE` em little-endian, com `LC_SEGMENT_64` = `0x19`) e um binário Mach-O `fat` universal (`0xCAFEBABE` em big-endian).
- **Selo e reivindicação relacionados:** Selo R / C3
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # 1. Constrói um binário Mach-O 64-bit thin válido de 4096 bytes
  thin64 = bytearray(4096)
  # mach_header_64: magic=0xfeedfacf, cputype=0x01000007 (x86_64), cpusubtype=3, filetype=2 (EXECUTE), ncmds=1, sizeofcmds=72, flags=1, reserved=0
  struct.pack_into("<IIIIIIII", thin64, 0, 0xFEEDFACF, 0x01000007, 3, 2, 1, 72, 1, 0)
  # segment_command_64 (cmd=0x19 LC_SEGMENT_64, cmdsize=72, segname="__TEXT", vmaddr=0, vmsize=4096, fileoff=0, filesize=4096, maxprot=7, initprot=5, nsects=0, flags=0)
  struct.pack_into("<II16sQQQQIIii", thin64, 32, 0x19, 72, b"__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 0, 4096, 0, 4096, 7, 5, 0, 0)

  # 2. Constrói um binário Mach-O FAT (Universal) de 8192 bytes contendo a fat_header (BE) e a slice thin64 no offset 4096
  fat = bytearray(8192)
  # fat_header: magic=0xCAFEBABE, nfat_arch=1
  struct.pack_into(">II", fat, 0, 0xCAFEBABE, 1)
  # fat_arch: cputype=0x01000007, cpusubtype=3, offset=4096, size=4096, align=12
  struct.pack_into(">IIIII", fat, 8, 0x01000007, 3, 4096, 4096, 12)
  fat[4096:8192] = thin64

  img = bytearray(128 * 1024)
  img[8192:8192+len(thin64)] = thin64
  img[32768:32768+len(fat)] = fat
  with open("c3_macho.img", "wb") as f:
      f.write(img)
  '
  rm -rf /tmp/out_c3
  ```
- **Resultado esperado segundo os autores:** N/A (preparação de imagem com um Mach-O `thin` de 4096 bytes no offset `8192` e um Mach-O `fat` de 8192 bytes no offset `32768`).
- **Evidência a salvar:** Hash SHA-256 de `c3_macho.img`.
- **Critério de sucesso:** `c3_macho.img` criado com 131.072 bytes.
- **Critério de falha:** Erro na geração de `c3_macho.img`.
- **Critério de interrupção:** Interromper o Bloco C3 se `c3_macho.img` não for criado.

#### Passo P11 — Execução do carving de Mach-O e validação por ferramenta (`[NÃO DOCUMENTADO]` quanto à flag `-t macho`)
- **Identificador:** P11
- **Status documental:** O identificador `-t macho` é **`[NÃO DOCUMENTADO]`** no `README.md` e no `artigo.pdf`, sendo obtido de `src/state.c:672` (`else if (strcmp(ft, "macho") == 0)`). A verificação com o utilitário `file` atende ao critério de `reivindicacoes.md:9`.
- **Selo e reivindicação relacionados:** Selo R / C3
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -v -t macho -i c3_macho.img -o /tmp/out_c3
  cat /tmp/out_c3/audit.txt
  file /tmp/out_c3/macho/*.macho
  ls -l /tmp/out_c3/macho/*.macho
  ```
- **Resultado esperado segundo os autores:** Extração do binário Mach-O `thin` (4096 bytes, offset `8192`) e do binário Mach-O `fat` (8192 bytes, offset `32768`) em `/tmp/out_c3/macho/`, ambos reconhecidos como executáveis Mach-O pelo comando `file` (`artigo.pdf:p. 6, §3`; `reivindicacoes.md:9`).
- **Evidência a salvar:** `/tmp/out_c3/audit.txt`, saída de `file /tmp/out_c3/macho/*.macho` e `ls -l` (`p11_c3_macho.log`).
- **Critério de sucesso:** Os arquivos `.macho` `thin` e `fat` são extraídos com os tamanhos exatos (4096 e 8192 bytes) e reconhecidos por `file` como `Mach-O 64-bit x86_64 executable` e `Mach-O universal binary`.
- **Critério de falha:** Não extração de uma das variantes (`fat` ou `thin`), tamanho incorreto ou não reconhecimento pela ferramenta `file`.
- **Critério de interrupção:** Prosseguir para o Bloco C4.

---

### Bloco C4 — Recuperação de executáveis ELF de 32 e 64 bits
> **Reivindicação C4 (`reivindicacoes.md:10`):** *"Recuperação de executáveis ELF de 32 e 64 bits, delimitados pelos cabeçalhos de programa"* | **Resultado esperado:** *"arquivo `.elf` extraído e estruturalmente legível por analisador ELF"*.

#### Passo P12 — Geração de imagem `memory.dump` com binários ELF de 32 e 64 bits (`[NÃO DOCUMENTADO]`)
- **Identificador:** P12
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** `artigo.pdf:p. 7, §4.1` utiliza o arquivo `memory.dump` nos exemplos de ELF (`foremost-ng -x -t elf -i memory.dump -o ./carved-files`), mas `memory.dump` não está no repositório (`artefato.txt:9-49`). É necessário gerar `memory.dump` contendo um executável ELF de 32 bits e um de 64 bits.
- **Selo e reivindicação relacionados:** Selo R / C4 (e reutilizado em C5)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  python3 -c '
  import struct
  # 1. Usa um ELF 64-bit real compilado (./foremost-ng)
  elf64 = open("foremost-ng", "rb").read()

  # 2. Constrói um ELF 32-bit little-endian válido de 4096 bytes com 1 segmento PT_LOAD
  elf32 = bytearray(4096)
  elf32[0:16] = b"\x7fELF\x01\x01\x01\x00" + b"\x00"*8
  # e_type=2 (ET_EXEC), e_machine=3 (EM_386), e_version=1, e_entry=0x08048000, e_phoff=52, e_shoff=0, e_flags=0, e_ehsize=52, e_phentsize=32, e_phnum=1
  struct.pack_into("<HHIIIIIHHHHHH", elf32, 16, 2, 3, 1, 0x08048000, 52, 0, 0, 52, 32, 1, 40, 0, 0)
  # Elf32_Phdr: p_type=1 (PT_LOAD), p_offset=0, p_vaddr=0x08048000, p_paddr=0x08048000, p_filesz=4096, p_memsz=4096, p_flags=5, p_align=4096
  struct.pack_into("<IIIIIIII", elf32, 52, 1, 0, 0x08048000, 0x08048000, 4096, 4096, 5, 4096)

  dump = bytearray(512 * 1024)
  dump[4096:4096+len(elf32)] = elf32
  dump[65536:65536+len(elf64)] = elf64
  with open("memory.dump", "wb") as f:
      f.write(dump)
  '
  rm -rf /tmp/out_c4
  ```
- **Resultado esperado segundo os autores:** N/A (preparação do arquivo `memory.dump` contendo um ELF32 no offset `4096` e um ELF64 no offset `65536`).
- **Evidência a salvar:** Hash SHA-256 de `memory.dump`.
- **Critério de sucesso:** `memory.dump` criado com 524.288 bytes.
- **Critério de falha:** Erro ao criar `memory.dump`.
- **Critério de interrupção:** Interromper os Blocos C4 e C5 se `memory.dump` não for criado.

#### Passo P13 — Execução do carving de ELF e validação com `readelf` (Comando documentado em `artigo.pdf:p. 7, §4.1`; validação com `readelf` `[NÃO DOCUMENTADO]`)
- **Identificador:** P13
- **Status documental:** Carving com `-t elf` documentado em `artigo.pdf:p. 7, §4.1`; inspeção com `readelf -h -l` e `file` marcada como `[NÃO DOCUMENTADO]` (necessária para comprovar que o `.elf` extraído é estruturalmente legível por analisador ELF, conforme `reivindicacoes.md:10`).
- **Selo e reivindicação relacionados:** Selo R / C4
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  ./foremost-ng -v -t elf -i memory.dump -o /tmp/out_c4
  cat /tmp/out_c4/audit.txt
  file /tmp/out_c4/elf/*.elf
  for f in /tmp/out_c4/elf/*.elf; do
      echo "=== Analisando $f ==="
      readelf -h -l "$f"
  done
  ```
- **Resultado esperado segundo os autores:** Extração dos binários ELF de 32 bits (`00000008.elf`, offset `4096`) e de 64 bits (`00000128.elf`, offset `65536`) em `/tmp/out_c4/elf/`, ambos com cabeçalho ELF e tabela de segmentos de programa (`PT_LOAD`) legíveis por `readelf` (`artigo.pdf:p. 6, §3`; `reivindicacoes.md:10`). *(Nota: como `extract_elf` em `src/extract.c:2213-2299` delimita o arquivo pelo fim dos segmentos `PT_LOAD` e não pela tabela de seções `e_shoff`, `readelf -S` no ELF64 pode avisar caso a tabela de seções original ficasse após o último `PT_LOAD`, mas `readelf -h -l` deve ler os cabeçalhos de programa sem erro).*
- **Evidência a salvar:** `/tmp/out_c4/audit.txt` e saída de `file` e `readelf -h -l` (`p13_c4_elf.log`).
- **Critério de sucesso:** Ambos os arquivos (ELF32 e ELF64) são extraídos e `readelf -h -l` consegue ler seus cabeçalhos ELF e segmentos de programa.
- **Critério de falha:** Falha na extração de ELF32 ou ELF64 ou corrupção dos cabeçalhos de programa.
- **Critério de interrupção:** Prosseguir para o Bloco C5.

---

### Bloco C5 — Enriquecimento pelo VirusTotal (`-x` e `VT_API_KEY`)
> **Reivindicação C5 (`reivindicacoes.md:11`):** *"Enriquecimento pelo VirusTotal: com `-x` e `VT_API_KEY`, consulta a API pelo hash de cada arquivo recuperado e registra o resultado de detecção"* | **Resultado esperado:** *"consulta associada ao hash do arquivo extraído, com o resultado de detecção registrado; sem chave, aviso e carving sem consulta (p. 7)"*.

#### Passo P14 — Execução com `-x` sem a variável `VT_API_KEY` (Documentado em `artigo.pdf:p. 7, §4.1`)
- **Identificador:** P14
- **Status documental:** Comportamento descrito em `artigo.pdf:p. 7, §4.1` (*"If the API key is missing or invalid, Foremost-NG will still perform carving but will emit a warning and skip all VT lookups"*).
- **Selo e reivindicação relacionados:** Selo R / C5 (parte 1: ausência de chave)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./carved-files_nokey
  env -u VT_API_KEY ./foremost-ng -x -t elf -i memory.dump -o ./carved-files_nokey
  cat ./carved-files_nokey/audit.txt
  ls -la ./carved-files_nokey/elf/
  ```
- **Resultado esperado segundo os autores:** Emissão de aviso/erro informando que `VT_API_KEY` não está configurada (`Error: VT_API_KEY environment variable is not set.` em `src/vt_query.c:141`) e conclusão normal do carving sem realizar consultas HTTP (`artigo.pdf:p. 7, §4.1`; `reivindicacoes.md:11`).
- **Evidência a salvar:** Saída de `stderr` e arquivo `./carved-files_nokey/audit.txt` (`p14_c5_nokey.log`).
- **Critério de sucesso:** Mensagem `Error: VT_API_KEY environment variable is not set.` exibida e arquivos `.elf` extraídos normalmente em `./carved-files_nokey/elf/`.
- **Critério de falha:** Programa aborta sem realizar o carving ou tenta acessar a rede sem chave.
- **Critério de interrupção:** Prosseguir para P15.

#### Passo P15 — Execução com `-x` e `VT_API_KEY` válida (Documentado em `README.md:99-102` e `artigo.pdf:p. 7, §4 e §4.1`)
- **Identificador:** P15
- **Status documental:** Documentado literalmente em `README.md:101` (`export VT_API_KEY=yourkey`) e `artigo.pdf:p. 7, §4.1` (`foremost-ng -x -t elf -i memory.dump -o ./carved-files`).
- **Selo e reivindicação relacionados:** Selo R / C5 (parte 2: consulta à API do VirusTotal)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  rm -rf ./carved-files
  export VT_API_KEY="<SUA_CHAVE_VIRUSTOTAL_AQUI>"
  ./foremost-ng -x -t elf -i memory.dump -o ./carved-files
  cat ./carved-files/audit.txt
  ```
- **Resultado esperado segundo os autores:** `foremost-ng` calcula o hash SHA-256 de cada arquivo extraído, consulta `https://www.virustotal.com/api/v3/files/<hash>` usando o cabeçalho `x-apikey` e preenche a coluna `VT` do `audit.txt` com `Clean (<undetected>)` ou `Malicious (<malicious>)` (`artigo.pdf:p. 3, §2; p. 7, §4.1; p. 8, Fig. 2`).
- **Evidência a salvar:** `./carved-files/audit.txt` e saída do terminal (`p15_c5_vt.log`).
- **Critério de sucesso:** Consulta HTTP realizada sem erro do `libcurl` e coluna `VT` preenchida em `audit.txt` com os resultados retornados pela API. *(Atenção: verificar se `sscanf` em `src/vt_query.c:180-181` extrai valores não negativos; se a API v3 retornar as chaves de `last_analysis_stats` em outra ordem, `audit.txt` exibirá `Clean (-1)`).*
- **Critério de falha:** Falha na requisição `curl_easy_perform()` ou incapacidade de parsear o JSON da API v3 do VirusTotal (ex.: `Clean (-1)` mesmo para hashes existentes no VirusTotal).
- **Critério de interrupção:** Prosseguir para o Bloco C6.

---

### Bloco C6 — Exemplo de execução da Figura 2 (`./foremost-ng -v -x evidence2.dd`)
> **Reivindicação C6 (`reivindicacoes.md:12, 21`):** *"Exemplo de execução da Figura 2: `./foremost-ng -v -x evidence2.dd`"* | **Resultado esperado:** *"tabela como a da Fig. 2, com arquivos ELF, script, EXE e ZIP, seus offsets e a coluna VT"*. *"Em C6, comparam-se os arquivos e offsets da Fig. 2. As contagens do VirusTotal mudam com o tempo e não precisam coincidir."*

#### Passo P16 — Tentativa de execução do comando da Figura 2 (Documentado em `artigo.pdf:p. 8, Fig. 2`)
- **Identificador:** P16
- **Status documental:** O comando `./foremost-ng -v -x evidence2.dd` está documentado na captura de tela de `artigo.pdf:p. 8, Fig. 2`. A verificação prévia da existência de `evidence2.dd` no pacote é `[NÃO DOCUMENTADO]`, pois os autores não documentaram onde obter `evidence2.dd`.
- **Selo e reivindicação relacionados:** Selo R / C6
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  find .. -name "evidence2.dd"
  ./foremost-ng -v -x evidence2.dd
  ```
- **Resultado esperado segundo os autores:** Na Figura 2 (`artigo.pdf:p. 8`), o comando processa `evidence2.dd` (`Length: 2 GB (2045109643 bytes)`) e imprime a tabela com 12 arquivos (`0: 00004352.elf` no offset `2228224` até `11: 01787042.zip` no offset `914965615`). **Contudo**, como `evidence2.dd` está ausente do artefato (`artefato.txt:9-49`), o comportamento real determinado pelo código (`src/main.c:250, 256`) é a falha imediata com `[!] File not found or is a directory: evidence2.dd` e `[!] No valid input files to process.`.
- **Evidência a salvar:** Saída de `find .. -name "evidence2.dd"` (vazia) e saída de erro de `./foremost-ng -v -x evidence2.dd` (`p16_c6_fig2.log`).
- **Critério de sucesso:** Reprodução dos 12 arquivos (`00004352.elf`, `00004820.elf`, `00005108.elf`, `00005492.script`, `00399884.exe`, `00405008.exe`, `00414932.exe`, `00428728.exe`, `00442520.exe`, `00447356.exe`, `01786109.zip`, `01787042.zip`) nos exatos offsets da Figura 2 (o que só seria possível se os autores tivessem fornecido `evidence2.dd`).
- **Critério de falha:** Arquivo `evidence2.dd` não encontrado (`[!] File not found or is a directory: evidence2.dd`), impossibilitando a reprodução de C6.
- **Critério de interrupção:** Concluir a avaliação experimental de R registrando C6 como **não reproduzível** por ausência do dado de entrada.

---

### Bloco C7 — Arquitetura de parsers extensível (Inspeção estática)
> **Reivindicação C7 (`reivindicacoes.md:13, 17`):** *"Arquitetura de parsers extensível: despachante central e parsers com identificador, assinatura, validação e recuperação"* | **Resultado esperado:** *"organização do código correspondente à Fig. 1"*. *(Conforme `reivindicacoes.md:17`, C7 não tem experimento associado e não entra na regra de R, mas pode ser inspecionada).*

#### Passo P17 — Inspeção da estrutura arquitetural do código (`[NÃO DOCUMENTADO]`)
- **Identificador:** P17
- **Status documental:** **`[NÃO DOCUMENTADO]`**.
- **Justificativa:** Os autores não fornecem comando para verificar C7; a inspeção dos arquivos-fonte em `src/` é necessária para confrontar a organização do código com a Figura 1 e a Seção 2 do artigo (`artigo.pdf:pp. 2-3`).
- **Selo e reivindicação relacionados:** C7 (Inspeção arquitetural; informativo)
- **Diretório:** `<raiz_do_artefato>/src`
- **Comando exato:**
  ```bash
  grep -n "typedef struct s_spec" -A 19 main.h
  grep -n "void init_all" -A 82 state.c
  grep -n "unsigned char \*extract_file" -A 69 extract.c
  ```
- **Resultado esperado segundo os autores:** Presença dos módulos da Figura 1 (CLI, validação de entrada, motor de carving e motor de extração) e registro de especificações de busca (`s_spec`) para cada formato (`EVTX`, `MACHO`, `ELF`, `SCRIPT`, etc.).
- **Evidência a salvar:** Saída dos comandos `grep` (`p17_c7_arch.log`).
- **Critério de sucesso:** Confirmação da existência dos módulos do pipeline da Figura 1 e das funções `extract_evtx`, `extract_script`, `extract_macho` e `extract_elf` despachadas por `extract_file`.
- **Critério de falha:** Ausência dos módulos ou dos parsers reivindicados no código-fonte.
- **Critério de interrupção:** Fim do roteiro.

---

## 5. Tabela Resumo de Todos os Passos

| Passo | Status Documental | Selo / Reivindicação | Diretório | Comando Principal | Resultado Esperado | Evidência a Salvar | Critério de Sucesso | Critério de Falha | Critério de Interrupção |
|---|---|---|---|---|---|---|---|---|---|
| **P1** | Doc. em `Dockerfile:3-6` (`python3 file binutils` `[NÃO DOCUMENTADO]`) | F e R (Pré-requisito) | `<raiz>` | `sudo apt-get update && sudo apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev python3 file binutils` | Instalação das ferramentas e bibliotecas de compilação | `p1_deps.log` | Saída `0`; cabeçalhos OpenSSL e libcurl presentes | Erro no `apt-get` | Abortar roteiro se `gcc`, `make`, `libssl-dev` ou `libcurl4-openssl-dev` falharem |
| **P2** | Doc. em `README.md:28-35`, `Dockerfile:9-10` | F e R (Compilação) | `<raiz>/src` | `make && sudo make install` | Binário `foremost-ng` compilado e instalado em `/usr/local/bin` | `p2_build.log` | Saída `0` e binário executável criado | Erro de compilação ou linkedição | Abortar execução prática se o binário não for gerado |
| **P3** | Doc. em `README.md:79`, `src/main.c:92-165` | Selo F (CLI básica) | `<raiz>/src` | `./foremost-ng -V && ./foremost-ng -h && man foremost-ng \| head -n 30` | Exibição da versão `1.5.7`, menu de ajuda e man page | `p3_cli.log` | Comandos retornam `0` e exibem ajuda/versão | Crash ou falha ao executar binário | Interromper se o binário não iniciar |
| **P4** | `[NÃO DOCUMENTADO]` (cria `disk.img` ausente no pacote) | Selo F (Entrada mínima) | `<raiz>/src` | Script Python gerando `disk.img` (2 MiB com ELF + script) e `mkdir -p /temp/output` | Criação de `disk.img` para o exemplo mínimo da p. 7 | `p4_disk_img.sha256` | `disk.img` criado com 2 MiB | Erro ao criar `disk.img` | Interromper P5 se `disk.img` não existir |
| **P5** | Doc. em `artigo.pdf:p. 7, §4.1` | Selo F (Teste mínimo) | `<raiz>/src` | `./foremost-ng -i disk.img -o /temp/output/carved` | Diretório `/temp/output/carved` com subpastas, arquivos extraídos e `audit.txt` | `p5_funcional.log` e `audit.txt` | Saída `0`, `audit.txt` gerado e >= 1 arquivo extraído | Erro de execução ou `0` arquivos extraídos | Prosseguir para P6–P15 para diagnóstico por módulo |
| **P6** | `[NÃO DOCUMENTADO]` (cria imagem com EVTX) | Selo R / **C1** | `<raiz>/src` | Script Python gerando `c1_evtx.img` com cabeçalho `ElfFile\0` e chunk de 64 KiB | Imagem `c1_evtx.img` criada (256 KiB) | Hash de `c1_evtx.img` | `c1_evtx.img` criado sem erro | Falha no script Python | Pular P7 se `c1_evtx.img` não for criado |
| **P7** | Parcial em `artigo.pdf:p. 7, §4.1` (validação `[NÃO DOCUMENTADO]`) | Selo R / **C1** | `<raiz>/src` | `./foremost-ng -v -t evtx -i c1_evtx.img -o /tmp/out_c1` e inspeção do `.evtx` | Extração de `00000016.evtx` em `/tmp/out_c1/evtx/` | `p7_c1_evtx.log` e `.evtx` extraído | `.evtx` extraído e legível por ferramenta de eventos | Nenhum `.evtx` extraído ou arquivo corrompido | Prosseguir para Bloco C2 |
| **P8** | `[NÃO DOCUMENTADO]` (cria imagem com scripts) | Selo R / **C2** | `<raiz>/src` | Script Python gerando `c2_script.img` (2 scripts válidos e 2 inválidos) | Imagem `c2_script.img` criada (128 KiB) | Hash de `c2_script.img` | `c2_script.img` criado sem erro | Falha no script Python | Pular P9 se `c2_script.img` não for criado |
| **P9** | `-t script` `[NÃO DOCUMENTADO]` no README (obtido de `src/state.c:695`) | Selo R / **C2** | `<raiz>/src` | `./foremost-ng -v -t script -i c2_script.img -o /tmp/out_c2 && head -n 20 /tmp/out_c2/script/*` | Extração dos 2 scripts válidos (>= 32 B, com código além de comentários) | `p9_c2_script.log` e arquivos `.script` | Scripts válidos extraídos com `#!` e corpo legível; inválidos descartados | Scripts válidos não extraídos ou inválidos extraídos | Prosseguir para Bloco C3 |
| **P10** | `[NÃO DOCUMENTADO]` (cria imagem com Mach-O `thin` e `fat`) | Selo R / **C3** | `<raiz>/src` | Script Python gerando `c3_macho.img` com Mach-O 64-bit `thin` e `fat` (`0xCAFEBABE`) | Imagem `c3_macho.img` criada (128 KiB) | Hash de `c3_macho.img` | `c3_macho.img` criado sem erro | Falha no script Python | Pular P11 se `c3_macho.img` não for criado |
| **P11** | `-t macho` `[NÃO DOCUMENTADO]` no README (obtido de `src/state.c:672`) | Selo R / **C3** | `<raiz>/src` | `./foremost-ng -v -t macho -i c3_macho.img -o /tmp/out_c3 && file /tmp/out_c3/macho/*.macho` | Extração dos binários Mach-O `thin` e `fat` em `/tmp/out_c3/macho/` | `p11_c3_macho.log` e arquivos `.macho` | Ambos extraídos nos tamanhos corretos e reconhecidos por `file` | Falha ao extrair `fat` ou `thin` ou arquivo corrompido | Prosseguir para Bloco C4 |
| **P12** | `[NÃO DOCUMENTADO]` (cria `memory.dump` com ELF32 e ELF64) | Selo R / **C4** (e **C5**) | `<raiz>/src` | Script Python gerando `memory.dump` com ELF 32-bit e ELF 64-bit | Imagem `memory.dump` criada (512 KiB) | Hash de `memory.dump` | `memory.dump` criado sem erro | Falha no script Python | Pular P13–P15 se `memory.dump` não for criado |
| **P13** | Doc. em `artigo.pdf:p. 7, §4.1` (`readelf` `[NÃO DOCUMENTADO]`) | Selo R / **C4** | `<raiz>/src` | `./foremost-ng -v -t elf -i memory.dump -o /tmp/out_c4 && readelf -h -l /tmp/out_c4/elf/*.elf` | Extração dos arquivos `.elf` de 32 e 64 bits em `/tmp/out_c4/elf/` | `p13_c4_elf.log` e arquivos `.elf` | ELF32 e ELF64 extraídos e cabeçalhos lidos por `readelf -h -l` | Não extração ou erro de leitura estrutural no `readelf` | Prosseguir para Bloco C5 |
| **P14** | Doc. em `artigo.pdf:p. 7, §4.1` | Selo R / **C5** (sem chave) | `<raiz>/src` | `env -u VT_API_KEY ./foremost-ng -x -t elf -i memory.dump -o ./carved-files_nokey` | Aviso de ausência de `VT_API_KEY` e carving concluído sem consulta | `p14_c5_nokey.log` | Mensagem `Error: VT_API_KEY environment variable is not set.` e arquivos extraídos | Aborto do carving ou tentativa de requisição sem chave | Prosseguir para P15 |
| **P15** | Doc. em `README.md:101`, `artigo.pdf:p. 7, §4.1` | Selo R / **C5** (com chave) | `<raiz>/src` | `export VT_API_KEY="..." && ./foremost-ng -x -t elf -i memory.dump -o ./carved-files` | Consulta por SHA-256 no VirusTotal e registro na coluna `VT` do `audit.txt` | `p15_c5_vt.log` e `audit.txt` | Consulta HTTP bem-sucedida e detecções válidas registradas na coluna `VT` | Erro HTTP/cURL ou falha de parsing (`Clean (-1)`) | Prosseguir para Bloco C6 |
| **P16** | Doc. em `artigo.pdf:p. 8, Fig. 2` (`find` `[NÃO DOCUMENTADO]`) | Selo R / **C6** | `<raiz>/src` | `find .. -name "evidence2.dd" && ./foremost-ng -v -x evidence2.dd` | Autores: tabela da Fig. 2; Real: erro `File not found` pois `evidence2.dd` falta no pacote | `p16_c6_fig2.log` | Reprodução dos 12 arquivos e offsets da Fig. 2 | Arquivo `evidence2.dd` ausente (`EXIT_FAILURE`) | Prosseguir para P17 |
| **P17** | `[NÃO DOCUMENTADO]` (inspeção estática de código) | **C7** (Fora da regra de R) | `<raiz>/src` | `grep -n "typedef struct s_spec" -A 19 main.h && grep -n "extract_file" -A 69 extract.c` | Confirmação da organização do código frente à Fig. 1 | `p17_c7_arch.log` | Módulos de CLI, validação, motor de busca e extração presentes | Ausência dos módulos ou parsers no código | Fim do roteiro |

## Prompt B2

Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que atende (Linux, como pede o README; contêiner Docker com Ubuntu 24.04 sobre WSL2, detalhado na seção 1 do registro) aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.

Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.

## Resposta B2

# Avaliação Pós-Execução — Foremost-NG (Selos F e R)

### 1. Confronto entre o Registro Factual de Execução e a Avaliação Analítica (Passo a Passo)

#### 1.1. Compilação, instalação e CLI documentadas pelos autores (`D0` / `D1`)
- **`P01` e `P02` (`[registro-factual.md:50-51]` — `git clone` e `make` na raiz do clone):** **Confirmam** a avaliação analítica (Seção D, item 3). O comando `make` executado na raiz do repositório clonado (como instruído em `[artigo.pdf:p. 6, §4]`) falha com `make: *** No targets specified and no makefile found. Stop.` (código 2), pois o único `Makefile` está em `src/Makefile`.
- **`P03` (`[registro-factual.md:52]` — descompactação do pacote e entrada em `src/`):** **Confirma** que o arquivo `foremost-ng-<version>.tar.gz` mencionado em `[README.md:27]` não existe no repositório nem em releases, mas a árvore do commit avaliado contém `src/Makefile` e todos os fontes.
- **`P04`, `P05`, `P06`, `P00a`, `P00b`, `P04-2`, `P05-2` (`[registro-factual.md:53-55, 58-61]` — dependências, `make` e `sudo make install` em `src/`):** **Confirmam** a avaliação analítica. No ambiente inicial construído com `--no-install-recommends`, faltava `libc6-dev` (`ctype.h: No such file or directory`), que o comando `apt-get install -y gcc ...` do `[Dockerfile:4-5]` dos autores instala por padrão como recomendação do `gcc`. Após instalar `libc6-dev` (`P00b`), `make` (`P04-2`) compilou os 10 arquivos `.c` com `-D__UNIX -D__LINUX -DLARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64` e ligou com `-lssl -lcrypto -lcurl` (código 0, gerando binário de 87.200 B), e `sudo make install` (`P05-2`) instalou `/usr/local/bin/foremost-ng`, `/usr/share/man/man8/foremost-ng.8.gz` e `/usr/local/etc/foremost.conf` (código 0).
- **`P06-2`, `P13a`, `P13b` (`[registro-factual.md:62, 78-79]` — `man foremost-ng`, `-h` e `-V`):** **Confirmam** a avaliação analítica quanto ao funcionamento da CLI e da página de manual, e acrescentam o detalhe de que a seção `BUILT-IN FORMATS` do manual instalado lista apenas os formatos legados, omitindo `evtx`, `elf`, `macho` e `script`.

#### 1.2. Verificação de integridade e ambiente (`D2` — evidência complementar)
- **`P09`, `P10`, `P11`, `P11-2`, `P12` (`[registro-factual.md:73-77]`):** **Confirmam** a integridade do pacote avaliado (`bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`) e a disponibilidade das bibliotecas e ferramentas auxiliares de verificação.

#### 1.3. Teste mínimo Funcional e testes externos DFTT (`D2` / `D3` — evidência complementar para R, prova de execução para F)
- **`P14a`, `P15a`, `P16a` (`[registro-factual.md:85, 87-88]` — carving mínimo sobre `min.dd`):** **Confirmam** que o binário executa sem erros (`[INFO] Processing finished.`, código 0), cria `audit.txt` e recupera byte a byte o script embutido (`00001024.script`, 72 B).
- **`P14b`, `P15b`, `P14b-2`, `P15b-2`, `P16-G-cmp (disk.img)` (`[registro-factual.md:86, 89-92]` — comando literal do artigo `./foremost-ng -i disk.img -o /temp/output/carved`):** **Confirmam** que o comando funciona (código 0) uma vez criado o diretório-pai `/temp/output` (`P14b-2`, já que `mkdir` em `dir.c` não cria diretórios-pai nem tem permissão em `/` sem `sudo`). A execução confirmou a extração do ELF64 (`00000008.elf`, 73.752 B correspondentes aos segmentos `PT_LOAD`), do script (`00001024.script`, 65 B idêntico) e a geração de `audit.txt` (sem `recovery.log`, confirmando a Seção D, item 4 da análise). Revelou ainda 3 extrações `.evtx` espúrias disparadas por bytes internos ao binário ELF embutido.
- **`P39`, `P39-gabarito`, `P39-t`, `P41`, `P41-gabarito`, `P41-t` (`[registro-factual.md:178-183]` — imagens externas DFTT #11 e #12 citadas em `[artigo.pdf:p. 7, §4]`):** **Confirmam** tanto a funcionalidade geral de carving em imagens forenses públicas (14 arquivos extraídos em DFTT #11, 10 com MD5 idêntico ao gabarito; 6 extraídos em DFTT #12) quanto a nossa avaliação analítica de que o repositório DFTT não contém arquivos dos novos formatos (`P39-t` e `P41-t` com `-t evtx,elf,exe` extraíram `0 FILES EXTRACTED`).

#### 1.4. Passos relativos às reivindicações C1 a C7 (com distinção entre `D0` e evidência complementar `D2`/`D3`)
- **Bloco C1 — EVTX (`P17b`, `P18b`, `P18b-conf`, `P19b`, `P16-G-cmp (EVTX)`, `P20a`, `P28b`, `P28c`, `P28d — EVTX`, `P19a` — `D2`/`D3`, evidência complementar):** **Confirmam** integralmente a avaliação analítica, inclusive a falha de cálculo de tamanho que apontamos em `extract_evtx` (`[src/extract.c:2479-2490]`). No EVTX sintético (`P18b`, `P16-G-cmp`), o arquivo original de 69.632 B (4 KiB de cabeçalho + 64 KiB de chunk) teve apenas 65.536 B extraídos (truncando os 4 KiB finais porque `chunk_count * 65536` ignora o cabeçalho de 4 KiB). No EVTX público real `system.evtx` (`P28d — EVTX`, 1.118.208 B), como o offset `0x18` contém `HeaderBlockSize` (4096) em vez de `NumberOfChunks` (offset `0x2A`), o parser calculou `4096 * 65536 = 268 MB` e extraiu 10.570.240 B (do início do EVTX até o fim de `teste.dd`). Ainda assim, em ambos os casos, `file` e `evtx_dump.py` leram os arquivos `.evtx` extraídos sem erro, recuperando todos os 1601 eventos com XML idêntico ao original em `P19a`.
- **Bloco C2 — Scripts (`P20b`, `P21b`, `P16-G-cmp (scripts)`, `P28d — scripts`, `P28d — negativos` — `D2`, evidência complementar):** **Confirmam parcialmente e contradizem a eficácia do filtro de comentários previsto na leitura estática**. Os 7 scripts válidos (Bash, Python, PowerShell) foram extraídos byte a byte idênticos com shebang na 1ª linha (`P21b`, `P28d — scripts`), e os scripts menores que 32 B (`s3` de 18 B e `neg_curto.sh` de 13 B) foram descartados. Entretanto, os scripts compostos apenas por shebang e linhas de comentário (`s4` de 62 B em `P21b` e `neg_comentario.sh` de 45 B em `P28d — negativos`) **foram extraídos indevidamente**, porque o laço em `src/extract.c:2599-2609` avança caractere a caractere (`p++`) em vez de linha a linha, tratando o primeiro caractere após `#` como código válido. Logo, a condição *"mais que só comentários"* de C2 (`[reivindicacoes.md:8]`) falhou nos testes complementares.
- **Bloco C3 — Mach-O (`P23b`, `P24b`, `P24b-conf`, `P25`, `P28d — Mach-O` — `D2`, evidência complementar):** **Confirmam para `fat`, mas contradizem a expectativa de funcionamento para `thin`**. O binário Mach-O `fat` (`0xCAFEBABE`, 8192 B) foi extraído idêntico e reconhecido por `file` (`P24b-conf`, `P28d — Mach-O`). Porém, o binário Mach-O `thin` de 64 bits (`0xCFFAEDFE`, 4096 B) **não foi extraído em nenhuma execução** (`P24b` e `P28d — Mach-O` falharam). Isso ocorre porque `extract_macho` (`[src/extract.c:2360, 2363, 2409]`) lê os bytes `CF FA ED FE` com `read_le32(buf)` (que retorna `0xFEEDFACF`), mas compara o resultado com o literal invertido `0xCFFAEDFE` (e `0xCEFAEDFE` para 32 bits), fazendo com que binários Mach-O `thin` nunca sejam extraídos.
- **Bloco C4 — ELF (`P26b`, `P27b`, `P27b-conf`, `P28d — ELF`, `P28d-readelf` — `D2`, evidência complementar):** **Confirmam integralmente** a avaliação analítica. Os binários ELF de 32 e 64 bits foram extraídos exatamente até o fim do último segmento `PT_LOAD` (`4096 B` para o ELF32 sintético; `12.296 B`, `139.896 B` e `73.752 B` para os ELFs compilados), e `readelf -h -l` leu sem erro o cabeçalho ELF e todos os cabeçalhos de programa (`LOAD`), acusando erro apenas na leitura da tabela de seções (`section headers`) localizada após o último `PT_LOAD`, tal como previsto na análise estática.
- **Bloco C5 — VirusTotal (`P07`, `P29b`, `P29a`, `P30`–`P33`):**
  - `P29b` e `P29a` (`[registro-factual.md:149-150]` — `D2`, sem `VT_API_KEY`): **Confirmam** exatamente o que apontamos na Seção D, item 5 da análise: sem `VT_API_KEY`, o programa imprime `Error: VT_API_KEY environment variable is not set.` para cada arquivo e realiza o carving normalmente, mas grava `Clean (0)` na coluna `VT` do `audit.txt` como se o arquivo tivesse sido verificado e considerado limpo.
  - `P07` e `P31`–`P33` (`[registro-factual.md:56, 152-154]` — com `VT_API_KEY`): **Não alteram** a avaliação analítica, pois permaneceram bloqueados por ausência de chave de API do VirusTotal (`depende_execucao`).
- **Bloco C6 — Figura 2 (`P08`, `P08-2`, `P34`–`P37` — `D0`):** **Confirmam integralmente** a avaliação analítica. O arquivo `evidence2.dd` não está presente no repositório, no contêiner nem em fontes públicas (`P34`), e a execução de `./foremost-ng -v -x evidence2.dd` (`P08-2` / `P36`) falha imediatamente com `[!] File not found or is a directory: evidence2.dd` (código 1).
- **Bloco C7 — Arquitetura (`P38a`, `P38b` — `D2`):** **Confirmam integralmente** a avaliação analítica: a estrutura `s_spec`, o registro em `init_all` e os módulos da Figura 1 existem (`P38b`), mas o despachante `extract_file` utiliza uma cadeia `if/else if` fixa por tipo (`P38a`). Conforme `[reivindicacoes.md:17]`, C7 não entra na regra de R.

---

### 2. Nova Decisão para os Selos F e R

#### Selo F (Funcional)
- **Decisão:** **Atribuir** (mudou: `true` — na etapa analítica era `Indeterminado`).
- **Justificativa:** Na etapa analítica, a decisão foi `Indeterminado` unicamente porque a atribuição de F exige execução e observação prática de saídas (`[instrucoes-oficiais.md:15]`). O registro factual comprova que, em ambiente Linux compatível com o `Dockerfile` dos autores (`Ubuntu 24.04` com `gcc`, `make`, `libssl-dev`, `libcurl4-openssl-dev` e `libc6-dev`), o artefato compila sem erros (`P04-2`), instala o binário, o arquivo de configuração e o manual (`P05-2`), responde às opções da CLI (`P06-2`, `P13a`, `P13b`) e executa o carving gerando subdiretórios por formato, arquivos recuperados e `audit.txt` tanto em imagens sintéticas (`P15a`, `P15b-2`, `P28b`, `P28c`) quanto em imagens forenses públicas DFTT (`P39`, `P41`). Todos os critérios obrigatórios do Selo F foram atendidos.

#### Selo R (Reprodutível)
- **Decisão:** **Não atribuir** (mudou: `false` — manteve `Não atribuir`).
- **Justificativa:**
  1. Conforme `[instrucoes-oficiais.md:19]` e `[reivindicacoes.md:17]`, o Selo R exige que a documentação traga instruções de execução das principais reivindicações e que **C1 a C6 sejam reproduzidas**.
  2. Os autores não forneceram nenhuma imagem de entrada (`evidence2.dd`, `disk.img`, `memory.dump`) no artefato (`[registro-factual.md:298-301, 311]`). A reivindicação principal **C6** (`./foremost-ng -v -x evidence2.dd`, Figura 2) falhou diretamente no passo documentado `P08-2` / `P36` (`File not found: evidence2.dd`, código 1), sendo **não reproduzível**.
  3. Tratando os passos `D2` e `D3` estritamente como evidência complementar (e não como reprodução de experimentos fornecidos pelos autores), tais testes não suprem a falta dos dados originais dos autores; pelo contrário, demonstraram falhas adicionais de implementação nas próprias reivindicações **C3** (incapacidade total de extrair binários Mach-O `thin` em `P24b` e `P28d — Mach-O`) e **C2** (extração indevida de scripts compostos apenas por comentários em `P21b` e `P28d — negativos`), além do truncamento/excesso de tamanho em **C1** (`P16-G-cmp (EVTX)`, `P28d — EVTX`) e do falso rótulo `Clean (0)` sem chave em **C5** (`P29a`, `P29b`).

---

### 3. Confiança (0 a 100) e Explicação da Mudança

- **Selo F — Confiança: `95`** (aumentou de `85` para `95`).
  - *Explicação da mudança:* A decisão passou de `Indeterminado` para `Atribuir` porque o registro factual forneceu a prova de compilação, instalação e funcionamento real que faltava na avaliação puramente estática. A confiança subiu para 95/100 pois o código compilou sem necessidade de editar uma única linha de código ou `Makefile` e extraiu artefatos corretamente em múltiplos testes.
- **Selo R — Confiança: `5`** de que o comitê oficial atribuiu o selo (isto é, **95%** de confiança de que o comitê oficial **não** atribuiu o Selo R; reduziu de `15` para `5`).
  - *Explicação da mudança:* A decisão permaneceu `Não atribuir`, mas a probabilidade estimada de o comitê ter atribuído o Selo R caiu de 15 para 5 porque a execução não apenas confirmou a impossibilidade de reproduzir a Figura 2 (**C6**) por ausência de `evidence2.dd`, como também revelou bugs funcionais na extração de Mach-O `thin` (**C3**) e na filtragem de scripts só com comentários (**C2**).

```json
{"F": {"decisao": "Atribuir", "mudou": true, "confianca": 95, "evidencias": ["instrucoes-oficiais.md:13-15", "README.md:3-85", "Dockerfile:1-12", "src/Makefile:1-124", "registro-factual.md:50-62", "registro-factual.md:78-92", "registro-factual.md:178-183", "registro-factual.md:230-235"]},
 "R": {"decisao": "Não atribuir", "mudou": false, "confianca": 5, "evidencias": ["instrucoes-oficiais.md:17-19", "reivindicacoes.md:7-21", "artefato.txt:9-49", "artigo.pdf:p. 7-8, §4.2 e Fig. 2", "registro-factual.md:56-63", "registro-factual.md:98-170", "registro-factual.md:237-305"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "nao_reproduzivel", "C3": "nao_reproduzivel", "C4": "reproduzivel", "C5": "depende_execucao", "C6": "nao_reproduzivel", "C7": "reproduzivel"}}}
```
