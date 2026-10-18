# Registro factual da execução de referência — Foremost-NG (SBSeg 2025)

**Artefato:** `cristianzsh/foremost-ng`, commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` (08/07/2025), pacote `artefato.zip` (SHA-256 `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a`).
**Execução:** 17/10/2026, 18:34–18:50 UTC, em uma única sessão de contêiner, gravada com `script` (util-linux).
**Roteiro:** união dos planos de três revisores. Os passos documentados pelos autores foram executados primeiro; depois, os passos [NÃO DOCUMENTADO] propostos pelos revisores; por fim, os testes externos com imagens DFTT.
**Conteúdo:** só fatos observados. Os status de cada passo seguem o critério de sucesso ou de falha escrito no roteiro para aquele passo.

**Convenções**
- **Desvios:** D0 seguiu a documentação; D1 correção trivial; D2 passo [NÃO DOCUMENTADO] proposto pelos revisores; D3 dado externo (DFTT, amostra pública).
- **IDs:** os sufixos `a` e `b` marcam variantes do mesmo passo propostas por revisores diferentes. `-conf` é a conferência feita logo após um carving; `-2` é a repetição de um passo.
- **Caminhos de evidência:** relativos a `execucao/`.
  - `evidencias/passos/ID.saida.txt`: saída integral do passo.
  - `evidencias/passos/ID.sha256`: SHA-256 dos arquivos criados ou alterados.
  - `evidencias/passos.tsv`: início, fim, duração, código de saída, diretório e comando de cada passo.
  - `evidencias/saidas/`: cópia das saídas.
  - `terminal.txt` e `tempo.txt`: sessão gravada, reproduzível com `scriptreplay -T tempo.txt terminal.txt`.
- **Arquivos compactados:** os maiores que 1 MB em `evidencias/saidas/` foram compactados com gzip após a execução; o SHA-256 dos originais está em `evidencias/compactados.txt`.

## 1. Ambiente

| Item | Valor |
|---|---|
| Host | Windows 11 Home 10.0.26300; Intel Core i5-13450HX (10 núcleos, 16 threads); 15,69 GiB de RAM |
| Virtualização | Docker Desktop 4.90.0, Docker Engine 29.7.2, sobre WSL 2.7.13.0. Contêiner, não VM |
| Kernel visto no contêiner | `Linux 6.18.33.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 18 21:54:43 UTC 2026 x86_64` (kernel do WSL2, compartilhado com o host) |
| SO do contêiner | Ubuntu 24.04.2 LTS (noble), x86_64. Imagem base `ubuntu:noble-20250619@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076`; apt fixado no snapshot `20250708T190020Z` (instante do commit avaliado) |
| CPU / RAM / disco visíveis | 16 CPUs lógicas (8 núcleos × 2 threads, hypervisor Microsoft); 8.161.751.040 bytes de RAM + 2 GiB de swap; `overlay` de 1007 GB com 952 GB livres |
| Compilador e bibliotecas | gcc 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04); GNU Make 4.3; glibc 2.39 (`libc6-dev` 2.39-0ubuntu8.4); GNU ld 2.42; OpenSSL 3.0.13 (`libssl-dev` 3.0.13-0ubuntu3.5); libcurl 8.5.0 (`libcurl4-openssl-dev` 8.5.0-2ubuntu10.6); git 2.43.0 |
| Ferramentas de verificação (instaladas em P12) | file 5.45; GNU readelf 2.42; Python 3.12.3; python3-evtx 0.7.4 (`evtx_dump.py`); gcc-multilib 13.2.0; curl 8.5.0; jq 1.7.1 |
| Usuário | `revisor` (uid 1001), com `sudo` sem senha |

**Construção da imagem.** A imagem veio do `Dockerfile` preparado para esta execução, que não é o dos autores. O `docker build` de 17/10/2026 reutilizou o cache nas 7 etapas, com data de criação 2026-10-16T01:38:53Z (`evidencias/E00-construcao-imagem.txt`). A imagem instalou os pacotes do `Dockerfile` dos autores (`gcc make git libssl-dev libcurl4-openssl-dev`) fixados por versão, mais `sudo`, `man-db`, `ca-certificates` e `unzip`, todos com `--no-install-recommends`.

**Pacotes instalados durante a execução, dentro do contêiner:**
- P00b: `libc6-dev` e 35 dependências (36 pacotes novos).
- P12: ferramentas de verificação (60 pacotes novos).

**Requisitos dos autores e o ambiente usado:**
- **Sistema:** o README:3 diz que a ferramenta é "Linux-based", e a seção "### Linux" (README:31–35) manda `make` e `sudo make install`, sem fixar distribuição nem versão. O ambiente é Linux (Ubuntu 24.04).
- **Base Docker:** o `Dockerfile` dos autores usa `FROM ubuntu:latest` (Dockerfile:1). A base usada aqui é a tag datada `noble-20250619`, a última anterior ao commit, e não a `latest` da data da execução.
- **Pacotes:** o `Dockerfile` dos autores instala `gcc make git libssl-dev libcurl4-openssl-dev` com `apt-get install -y` (Dockerfile:3–6), sem `--no-install-recommends`. No ambiente inicial faltava `libc6-dev`, recomendação do `gcc` que o comando dos autores instalaria (ver P04 e P00). A partir de P00b, os pacotes do `Dockerfile` e o `libc6-dev` estão presentes.
- **Isolamento:** a execução foi em contêiner Docker sobre WSL2, não em VM Ubuntu.

## 2. Passos

### 2.1 Passos dos autores sem entrada de dados (D0/D1)

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P01 | autores (artigo p.6, §4) | `git clone https://github.com/cristianzsh/foremost-ng.git` (`~/trabalho`) | repositório clonado | clonado; 68 arquivos criados, incluindo os de `.git` (código 0; 3,7 s) | `passos/P01.*` | sucesso | D0 |
| P02 | autores (artigo p.6, §4: `cd foremost-ng`, `make`) | `make` (`~/trabalho/foremost-ng`, raiz do clone) | compilação | `make: *** No targets specified and no makefile found.  Stop.` (código 2; 0,006 s). O único `Makefile` do repositório está em `src/` | `passos/P02.saida.txt` | falha | D0 |
| P03 | autores (README:23, 27–28) | README: `tar xzvf foremost-ng-<version>.tar.gz; cd foremost-ng-<version>/src`. Executado: `unzip /pacote/artefato.zip -d ~/trabalho; cd foremost-ng-bb812a22/src` | diretório `src` com `Makefile` | não há `.tar.gz` com esse nome no repositório nem nos releases; o zip do commit avaliado foi extraído, 40 arquivos (código 0; 0,8 s); `src/` contém `Makefile` e os fontes | `passos/P03.*` | sucesso | D1 |
| P04 | autores (README:31–33) | `make` (`…/foremost-ng-bb812a22/src`) | binário `foremost-ng` | `main.h:25:10: fatal error: ctype.h: No such file or directory` (código 2; 0,05 s). `ctype.h` é cabeçalho da biblioteca C (`libc6-dev`), ausente no ambiente inicial | `passos/P04.saida.txt` | falha | D1 |
| P05 | autores (README:34; artigo p.6) | `sudo make install` (idem) | binário em `/usr/local/bin`, manual e `foremost.conf` instalados | mesmo erro de P04 (código 2). Sem `make` prévio bem-sucedido, a compilação disparada por `make install` usou `gcc -Wall -O2 -DVERSION="\"1.5.7\"" -D__UNIX -c main.c`, sem `-D__LINUX` | `passos/P05.saida.txt` | falha | D0 |
| P06 | autores (README:76–79; artigo p.7) | `env MANPAGER=cat MANWIDTH=100 man foremost-ng` (`~`) | página de manual | `No manual entry for foremost-ng` (código 16), consequência de P05 | `passos/P06.saida.txt` | falha | D0 |
| P07 | autores (README:89–101; artigo p.7, §4) | verificação da variável `VT_API_KEY` | consulta ao VirusTotal com chave válida | `VT_API_KEY nao definida (nenhuma chave disponivel)` (código 0) | `passos/P07.saida.txt` | bloqueado (sem chave) | — |
| P08 | autores (artigo p.8, Fig. 2) | `./foremost-ng -v -x evidence2.dd` (`src`) | tabela da Fig. 2 | binário inexistente nesse momento (código 127); `evidence2.dd` ausente | `passos/P08.saida.txt` | bloqueado | D0 |
| P00a | autores (Dockerfile:3–6) | `sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev` (`~/trabalho`) | dependências instaladas | `0 upgraded, 0 newly installed` (código 0; 15,0 s). Com os pacotes já instalados, o comando não instala recomendações ausentes; `libc6-dev` continuou ausente | `passos/P00a.saida.txt` | sucesso | D1 (`sudo`) |
| P00b | autores (Dockerfile:3–6: pacote que o `apt-get install -y` do Dockerfile instala como recomendação do `gcc`) | `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libc6-dev` | `libc6-dev` instalado | `36 newly installed`, entre eles `libc6-dev` 2.39-0ubuntu8.4 (código 0; 17,2 s) | `passos/P00b.saida.txt` | sucesso | D1 |
| P04-2 | autores (README:31–33) | `make` (`src`) | binário `foremost-ng` | compilou 10 arquivos com `-D__UNIX -D__LINUX -DLARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64` e ligou com `-lssl -lcrypto -lcurl`; 2 avisos `-Wunused-result` (`realpath`, state.c:95 e 121); binário de 87.200 B, SHA-256 `c479c4c48ac7d83cddc33e6b82815278f6ff07caf8152cdb2cf0b3cc9a2ea5a6` (código 0; 1,1 s) | `passos/P04-2.*` | sucesso | D1 |
| P05-2 | autores (README:34) | `sudo make install` (`src`) | binário, manual e configuração instalados | `/usr/local/bin/foremost-ng` (mesmo SHA-256 de P04-2), `/usr/share/man/man8/foremost-ng.8.gz` (`c77ca018…d365`), `/usr/local/etc/foremost.conf` (`a6e9571e…4f98`); `which foremost-ng` = `/usr/local/bin/foremost-ng` (código 0) | `passos/P05-2.*` | sucesso | D0 |
| P06-2 | autores (README:76–79) | `env MANPAGER=cat MANWIDTH=100 man foremost-ng` (`~`) | página de manual | exibida (código 0). Em "BUILT-IN FORMATS" lista `jpg gif png bmp avi exe mpg mp4 wav riff wmv mov pdf ole doc zip rar htm cpp all`; não aparecem `evtx`, `elf`, `macho` nem `script`. Documenta `-x` e `export VT_API_KEY=yourkey`. Diz que `-o` cria o diretório se não existir e que o arquivo de configuração é procurado em `./foremost.conf` e depois em `/etc/foremost.conf` | `passos/P06-2.saida.txt` | sucesso | D0 |
| P08-2 | autores (artigo p.8, Fig. 2) | `./foremost-ng -v -x evidence2.dd` (`src`) | tabela da Fig. 2 | `[!] File not found or is a directory: evidence2.dd` / `[!] No valid input files to process.` (código 1); nenhum diretório criado | `passos/P08-2.saida.txt` | bloqueado (sem `evidence2.dd`) | D0 |

### 2.2 Passos [NÃO DOCUMENTADO] propostos pelos revisores (D2)

Nas linhas "comando dos autores sobre entrada sintética", a sintaxe do comando vem do artigo (p.7, §4.1); a entrada e a conferência não são documentadas.

#### Preparação e verificação

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P09 | [NÃO DOCUMENTADO] proposto pelos revisores | `cat /etc/os-release; uname -m; gcc --version; make --version; openssl version; curl --version; dpkg -l libssl-dev libcurl4-openssl-dev` | arquivo com as versões | versões da seção 1; `curl: not found` (o executável `curl` só foi instalado em P12) (código 0) | `passos/P09*.saida.txt` | sucesso | D2 |
| P10 | [NÃO DOCUMENTADO] proposto pelos revisores | `git checkout bb812a22…; git rev-parse HEAD; git status --short` (clone) | HEAD = `bb812a22…` e `status` vazio | `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`, `2025-07-08T16:00:20-03:00 Add Foremost-NG Dockerfile`; `status` vazio (código 0) | `passos/P10.saida.txt` | sucesso | D2 |
| P11 | [NÃO DOCUMENTADO] proposto pelos revisores | `sha256sum /pacote/artefato.zip`; `diff -r` entre o clone e o zip; `sha256sum` de 8 fontes do zip | hash do zip igual ao do pacote; prefixos dos 8 fontes iguais aos do índice do pacote | zip `955c770e…388e0a` (igual). README.md `ff3414f0…`, Dockerfile `a8848d0c…`, src/Makefile `ce9da14a…`, src/main.c `966bffda…`, src/dir.c `ae64b63a…`, src/extract.c `4f81160c…`, src/state.c `8bbf0ec5…`, src/vt_query.c `d20bf972…` (iguais aos prefixos esperados). `diff -r` acusou 20 arquivos diferentes (código 0) | `passos/P11.saida.txt` | sucesso | D2 |
| P11-2 | [NÃO DOCUMENTADO] proposto pelos revisores (complemento de P11, acrescentado na execução) | para cada arquivo do zip: `cmp` com o clone; se diferir, `cmp` após remover CR | — | 40 arquivos no zip e 40 no clone (sem `.git`): 20 iguais byte a byte e 20 iguais após remover CR (os arquivos de texto do zip têm fim de linha CRLF; os do clone, LF); 0 diferentes | `passos/P11-2.saida.txt` | sucesso | D2 |
| P12 | [NÃO DOCUMENTADO] proposto pelos revisores | `sudo apt-get install -y gcc-multilib file binutils python3 python3-evtx curl jq`. O leitor de EVTX proposto (`python-evtx` via `pip` em `venv`) foi instalado pelo pacote do Ubuntu `python3-evtx`, a mesma biblioteca | ferramentas instaladas | instaladas; 60 pacotes novos (código 0; 26,5 s) | `passos/P12*.saida.txt` | sucesso | D2 |
| P13a | [NÃO DOCUMENTADO] proposto pelos revisores | `foremost-ng -h` (`~`) | lista com `-t -i -o -v -x`, código 0 | `foremost-ng version 1.5.7 by Cristian Souza.` e opções `-V -t -d -i -a -w -o -c -q -Q -x -v`; `-t  Specify file type (e.g., jpeg,pdf).`; `-x  Enable VirusTotal scan (needs API key).` (código 0) | `passos/P13a.saida.txt` | sucesso | D2 |
| P13b | [NÃO DOCUMENTADO] proposto pelos revisores | `./foremost-ng -V; ./foremost-ng -h; man foremost-ng \| head -n 30` (`src`) | versão 1.5.7 e opções | `1.5.7` e aviso de copyright; ajuda igual a P13a; início do manual (códigos 0) | `passos/P13b.saida.txt` | sucesso | D2 |

#### Teste mínimo

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P14a | [NÃO DOCUMENTADO] proposto pelos revisores | criar `min.sh` (script Bash de 72 B) e `min.dd` (1 MiB, script no offset 524288) (`~/aval`) | `min.dd` com 1.048.576 B | criado; `min.dd` `24a7f89d…fff1` (código 0) | `passos/P14a.*` | sucesso | D2 |
| P14b | [NÃO DOCUMENTADO] proposto pelos revisores | Python: `disk.img` de 2 MiB com o binário `foremost-ng` (87.200 B) no offset 4096 e um script de 65 B no offset 524288; `mkdir -p /temp/output` (`src`) | `disk.img` com 2.097.152 B e `/temp/output` existente | `disk.img` criado (`569dec63…5241`); `mkdir: cannot create directory '/temp': Permission denied` (usuário sem root) | `passos/P14b.*` | falha (critério: erro de permissão ao criar `/temp/output`) | D2 |
| P15a | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `foremost-ng -i min.dd -o ~/aval/saida_min` (`~/aval`) | código 0 e `audit.txt` criado | `[INFO] Processing finished.` (código 0); configuração usada: `/usr/local/etc/foremost.conf` | `passos/P15a.*`, `saidas/P15a/` | sucesso | D2 |
| P16a | [NÃO DOCUMENTADO] proposto pelos revisores | `cat audit.txt; ls -R; cmp amostras/min.sh saida_min/script/00001024.script` | `00001024.script` no offset 524288 e `cmp` idêntico | `audit.txt`: `0: 00001024.script  72 B  524288  VT N/A`, `1 FILES EXTRACTED`, `script=1`; `IDENTICO` | `passos/P16a.saida.txt` | sucesso | D2 |
| P15b | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `./foremost-ng -i disk.img -o /temp/output/carved` (`src`) | `/temp/output/carved` com subdiretórios e `audit.txt` | `foremost-ng: /temp: Permission denied` / `foremost-ng: Unable to open output directory` (código 1). O programa não cria diretórios-pai | `passos/P15b.saida.txt` | falha | D2 |
| P14b-2 | [NÃO DOCUMENTADO] proposto pelos revisores | `sudo mkdir -p /temp/output && sudo chown revisor:revisor /temp/output` | diretório criado | criado (código 0) | `passos/P14b-2.saida.txt` | sucesso | D2 |
| P15b-2 | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `./foremost-ng -i disk.img -o /temp/output/carved` (`src`) | código 0, `audit.txt` e ≥ 1 arquivo | código 0; stderr: `WMV err num_header_objs=1313407028 headerSize=8101131813384945782`. `audit.txt`: `00000008.elf` 72 KB @4096; `00000097.evtx` 12 KB @50128; `00000122.evtx` 534 B @62954; `00000124.evtx` 1 MB @63488; `00001024.script` 65 B @524288; `5 FILES EXTRACTED` (`elf=1 evtx=3 script=1`). Configuração usada: `src/foremost.conf` | `passos/P15b-2.*`, `passos/P16b.saida.txt`, `saidas/P15b/` | sucesso | D2 |
| P16-G-cmp (disk.img) | [NÃO DOCUMENTADO] proposto pelos revisores (comparação byte a byte, acrescentada na execução) | recortar os originais de `disk.img` e comparar com `cmp` | — | ELF: original 87.200 B, recuperado 73.752 B, prefixo idêntico. Script: 65 B, idêntico. Os três `.evtx` têm offsets dentro da região do binário ELF embutido (4096–91.295); o maior (2.033.664 B) termina no fim da imagem (63.488 + 2.033.664 = 2.097.152) | `passos/P16-G-cmp.saida.txt` | — | D2 |

#### C1 — EVTX

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P17b | [NÃO DOCUMENTADO] proposto pelos revisores | Python: `c1_evtx.img` (256 KiB) com cabeçalho EVTX sintético de 4096 B (`ElfFile\0`; campo em 0x18 = 1) e 1 chunk de 64 KiB (`ElfChnk\0`, sem registros) no offset 8192 | imagem de 262.144 B | criada (`c62b1bcb…7f6190`) | `passos/P17b.*` | sucesso | D2 |
| P18b | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `./foremost-ng -v -t evtx -i c1_evtx.img -o /tmp/out_c1` (`src`) | `00000016.evtx` extraído e registrado no `audit.txt` | código 0; `0: 00000016.evtx  64 KB  8192`; `1 FILES EXTRACTED` | `passos/P18b.*`, `saidas/P18b/` | sucesso | D2 |
| P18b-conf | [NÃO DOCUMENTADO] proposto pelos revisores | `file`; verificação do magic em Python | `.evtx` com `ElfFile\0`, reconhecido ou legível por ferramenta de eventos | `MS Windows Vista-8.1 Event Log, 1 chunks (no. 1 in use), empty`; 65.536 B; magic `b'ElfFile\x00'` | `passos/P18b-conf.saida.txt` | sucesso | D2 |
| P19b | [NÃO DOCUMENTADO] proposto pelos revisores | `evtx_dump.py /tmp/out_c1/evtx/00000016.evtx` | leitura sem erro | `<Events>` vazio (0 eventos); código 0 | `passos/P19b.saida.txt` | sucesso | D2 |
| P16-G-cmp (EVTX) | [NÃO DOCUMENTADO] proposto pelos revisores (acrescentado na execução) | comparar o recuperado com cabeçalho + chunk originais (69.632 B) | — | recuperado 65.536 B = os primeiros 65.536 B do original (prefixo idêntico) | `passos/P16-G-cmp.saida.txt` | — | D2 |

#### C2 — scripts

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P20b | [NÃO DOCUMENTADO] proposto pelos revisores | Python: `c2_script.img` (128 KiB) com s1 Bash de 76 B @4096, s2 Python de 75 B @16384, s3 de 18 B (< 32 B) @32768 e s4 de 62 B (shebang e só comentários) @49152 | imagem de 131.072 B | criada (`4ea6ee3e…e651`) | `passos/P20b.*` | sucesso | D2 |
| P21b | [NÃO DOCUMENTADO] proposto pelos revisores (o identificador `-t script` não está no README nem no artigo) | `./foremost-ng -v -t script -i c2_script.img -o /tmp/out_c2` (`src`) | exatamente s1 e s2 extraídos (`00000008.script`, `00000032.script`); s3 e s4 ignorados | código 0; `00000008.script` 76 B @4096; `00000032.script` 75 B @16384; `00000096.script` 62 B @49152; `3 FILES EXTRACTED` | `passos/P21b*.saida.txt`, `saidas/P21b/` | falha (critério: extração do fragmento só com comentários) | D2 |
| P16-G-cmp (scripts) | [NÃO DOCUMENTADO] proposto pelos revisores (acrescentado na execução) | `cmp` com os bytes originais | — | s1 idêntico; s2 idêntico; s3 não extraído; s4 extraído, idêntico (`#!/bin/bash`, `# apenas comentario 1`, `# apenas comentario 2 longo`) | `passos/P16-G-cmp.saida.txt` | — | D2 |

#### C3 — Mach-O

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P23b | [NÃO DOCUMENTADO] proposto pelos revisores | Python: `c3_macho.img` (128 KiB) com Mach-O 64-bit thin sintético de 4096 B @8192 (magic `0xFEEDFACF` em little-endian, bytes `CF FA ED FE`; 1 `LC_SEGMENT_64`) e Mach-O fat sintético de 8192 B @32768 (`0xCAFEBABE`, 1 arquitetura, com a fatia thin em +4096) | imagem de 131.072 B | criada (`3b70d310…48ce8f3`) | `passos/P23b.*` | sucesso | D2 |
| P24b | [NÃO DOCUMENTADO] proposto pelos revisores (o identificador `-t macho` não está no README nem no artigo) | `./foremost-ng -v -t macho -i c3_macho.img -o /tmp/out_c3` (`src`) | thin (4096 B) e fat (8192 B) extraídos, reconhecidos por `file` | código 0; `0: 00000064.macho  8 KB  32768`; `1 FILES EXTRACTED`; nenhum arquivo no offset 8192 | `passos/P24b*.saida.txt`, `saidas/P24b/` | falha (critério: variante thin não extraída) | D2 |
| P24b-conf | [NÃO DOCUMENTADO] proposto pelos revisores | `file`; `ls -l` | — | `00000064.macho`: `Mach-O universal binary with 1 architecture: [x86_64: Mach-O 64-bit x86_64 executable, flags:<NOUNDEFS>]`, 8192 B; idêntico ao fat original (P16-G-cmp) | `passos/P24b-conf.saida.txt` | — | D2 |
| P25 | [NÃO DOCUMENTADO] proposto pelos revisores | `lipo -info` / `otool -h` num macOS | — | não executado: sem macOS | — | bloqueado | — |

#### C4 — ELF

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P26b | [NÃO DOCUMENTADO] proposto pelos revisores | Python: `memory.dump` (512 KiB) com ELF32 sintético de 4096 B @4096 (1 `PT_LOAD`) e o binário `foremost-ng` (ELF64, 87.200 B) @65536 | imagem de 524.288 B | criada (`969b154c…7db3d266`) | `passos/P26b.*` | sucesso | D2 |
| P27b | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética, sem `-x`) | `./foremost-ng -v -t elf -i memory.dump -o /tmp/out_c4` (`src`) | ELF32 `00000008.elf` e ELF64 `00000128.elf` extraídos; `readelf -h -l` lê cabeçalhos e segmentos | código 0; `00000008.elf` 4 KB @4096; `00000128.elf` 72 KB @65536; `2 FILES EXTRACTED` | `passos/P27b*.saida.txt`, `saidas/P27b/` | sucesso | D2 |
| P27b-conf | [NÃO DOCUMENTADO] proposto pelos revisores | `file`; `readelf -h -l` | — | ELF32: `ELF 32-bit LSB executable, Intel 80386 … no section header`; `readelf` lê o cabeçalho e 1 `LOAD`; idêntico ao original. ELF64: 73.752 B (original 87.200 B, prefixo idêntico); `file`: `… missing section headers at 87136`; `readelf -h -l` imprime cabeçalho (32 seções declaradas a partir do byte 85.152) e 4 `LOAD`, com `readelf: Error: Reading 2048 bytes extends past end of file for section headers`. No binário original, o último `LOAD` termina em 0x11ad0 + 0x548 = 73.752 B | `passos/P27b-conf.saida.txt`, `passos/P16-G-cmp.saida.txt` | — | D2 |

#### Imagem combinada (C1–C4)

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P20a | [NÃO DOCUMENTADO] proposto pelos revisores | amostras em `~/aval/amostras`: `cp /bin/ls elf64_ls` (142.312 B); `gcc -m32` → `elf32_ola` (14.936 B); `s_bash.sh` (54 B), `s_py.py` (57 B), `s_ps.ps1` (71 B); negativos `neg_comentario.sh` (45 B, shebang e 2 comentários) e `neg_curto.sh` (13 B). EVTX público (D3): `system.evtx` dos dados de teste do python-evtx, `https://raw.githubusercontent.com/williballenthin/python-evtx/c0007441657899c39180de10a2be1a0e43dbeaf9/tests/data/system.evtx`, 1.118.208 B, `ccb83cfe…f8dc6ae`. Mach-O: as duas amostras sintéticas de P23b (`macho_thin` 4096 B, `macho_fat` 8192 B). O EVTX exportado de um Windows e os Mach-O reais de um macOS, propostos no roteiro, não foram usados (seção 4) | `file` reconhece cada amostra | `file`: ELF 32-bit e 64-bit; `MS Windows Vista-8.1 Event Log, 9 chunks (no. 8 in use), next record no. 13528, DIRTY`; `Mach-O universal binary…` e `Mach-O 64-bit x86_64 executable`; scripts Bash, POSIX, pwsh e Python (código 0) | `passos/P20a.*`, `saidas/entradas/A-amostras/` | sucesso | D2 (EVTX: D3) |
| P28a | [NÃO DOCUMENTADO] proposto pelos revisores | montar `teste.dd` (13.873.664 B, `51d60e3b…7cc7`): cada amostra em offset múltiplo de 512, separadas por 1 MiB de zeros; nomes esperados = offset ÷ 512 | uma linha por amostra | elf32_ola @1.048.576 (`00002048`); elf64_ls @2.112.512 (`00004126`); evtx_system @3.303.424 (`00006452`); macho_fat @5.470.208 (`00010684`); macho_thin @6.526.976 (`00012748`); neg_comentario @7.579.648 (`00014804`); neg_curto @8.628.736 (`00016853`); s_bash @9.677.824 (`00018902`); s_ps @10.726.912 (`00020951`); s_py @11.776.000 (`00023000`) | `passos/P28a.saida.txt` | sucesso | D2 |
| P28b | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `foremost-ng -i teste.dd -o ~/aval/saida_todos` (`~/aval`) | código 0 e `audit.txt` | código 0; 8 arquivos: `00002048.elf` 12 KB, `00004126.elf` 136 KB, `00010684.macho` 8 KB, `00006452.evtx` 10 MB, `00014804.script` 45 B, `00018902.script` 54 B, `00020951.script` 71 B, `00023000.script` 57 B | `passos/P28b.*`, `saidas/P28b/` | sucesso | D2 (EVTX: D3) |
| P28c | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores: artigo p.7, `-t evtx,elf,exe`) | `foremost-ng -t evtx,elf,exe -i teste.dd -o ~/aval/saida_tipos` (`~/aval`) | arquivos só em `evtx`, `elf` e, se houver, `exe` | código 0; `00006452.evtx`, `00002048.elf`, `00004126.elf` (mesmos SHA-256 de P28b); nenhum outro subdiretório com arquivos | `passos/P28c.*`, `saidas/P28c/` | sucesso | D2 (EVTX: D3) |
| P28d — EVTX | [NÃO DOCUMENTADO] proposto pelos revisores | `grep`/`ls`/`cmp` do EVTX | `00006452.evtx` em `saida_todos/evtx` e `saida_tipos/evtx` | presente nas duas saídas; recuperado 10.570.240 B, original 1.118.208 B; `cmp: EOF on amostras/evtx_system.evtx after byte 1118208` (os primeiros 1.118.208 B são idênticos); 3.303.424 + 10.570.240 = 13.873.664 B, o tamanho da imagem | `passos/P28d.saida.txt` | sucesso | D3 |
| P19a | [NÃO DOCUMENTADO] proposto pelos revisores | `evtx_dump.py` no original e no recuperado; `grep -c '<Event '` | recuperado lido sem exceção; mesma contagem reforça | códigos 0; 1601 eventos no original e 1601 no recuperado; XML idêntico (`cmp`); idem para `saida_tipos` (8,1 s) | `passos/P19a.saida.txt`, `saidas/entradas/A-evidencias/P19_*.xml.gz` | sucesso | D3 |
| P28d — scripts | [NÃO DOCUMENTADO] proposto pelos revisores | `head -1` e `cmp` de `s_*` | 3 arquivos com shebang na 1ª linha, `cmp` idêntico | `s_bash.sh`, `s_ps.ps1`, `s_py.py`: shebang na 1ª linha e `IDENTICO` | `passos/P28d.saida.txt` | sucesso | D2 |
| P28d — negativos | [NÃO DOCUMENTADO] proposto pelos revisores | existência de `<nome>.script` para `neg_*` | os dois negativos descartados | `neg_comentario.sh RECUPERADO` (`00014804.script`, 45 B, mesmo SHA-256 do original); `neg_curto.sh descartado` | `passos/P28d.saida.txt` | falha (critério: um negativo recuperado) | D2 |
| P28d — Mach-O | [NÃO DOCUMENTADO] proposto pelos revisores | `file`/`stat`/`cmp` de `macho_*` | os dois arquivos nos nomes esperados, reconhecidos por `file` | `macho_fat` → `00010684.macho`, `Mach-O universal binary…`, 8192 B, `IDENTICO`; `macho_thin` → `00012748.macho` inexistente | `passos/P28d.saida.txt` | falha (critério: um dos dois ausente) | D2 |
| P28d — ELF | [NÃO DOCUMENTADO] proposto pelos revisores | `file`; `readelf -h -l` e `readelf -S` filtrados por `error\|warning`; `stat`; `cmp -n` | os dois arquivos nas duas saídas; `file` ELF 32/64; `readelf -h -l` sem erros. Falha: erro na leitura do cabeçalho ELF ou dos cabeçalhos de programa | `00002048.elf` 12.296 B (original 14.936 B) e `00004126.elf` 139.896 B (original 142.312 B), nas duas saídas, `PREFIXO_IDENTICO`; `file`: `ELF 32-bit … missing section headers at 14896` e `ELF 64-bit … missing section headers at 142248`; `readelf: Error: Reading 1160 bytes` / `1984 bytes extends past end of file for section headers` | `passos/P28d.saida.txt` | inconclusivo (há erro, mas ele se refere à tabela de seções, não ao cabeçalho ELF nem aos cabeçalhos de programa) | D2 |
| P28d-readelf | [NÃO DOCUMENTADO] proposto pelos revisores (mesmo comando sem filtro) | `readelf -h -l saida_todos/elf/*.elf` | — | ELF32: cabeçalho, 11 cabeçalhos de programa, 4 `LOAD`, 29 seções declaradas, erro de seções acima; código 0. ELF64: cabeçalho, 13 cabeçalhos de programa, 4 `LOAD`, 31 seções declaradas, erro de seções acima; código 0 | `passos/P28d-readelf.saida.txt` | — | D2 |

#### C5 — VirusTotal

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P29b | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `env -u VT_API_KEY ./foremost-ng -x -t elf -i memory.dump -o ./carved-files_nokey` (`src`) | mensagem `Error: VT_API_KEY environment variable is not set.` e `.elf` extraídos | a mensagem aparece 2 vezes (uma por arquivo); código 0; `00000008.elf` e `00000128.elf` extraídos (mesmos bytes de P27b); coluna VT do `audit.txt`: `Clean (0)` nos dois | `passos/P29b.*`, `saidas/P29b/` | sucesso | D2 |
| P29a | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre entrada sintética) | `unset VT_API_KEY; foremost-ng -x -t elf -i teste.dd -o ~/aval/saida_vt_semchave` (`~/aval`) | mesmos ELF de P28c e aviso no terminal; registrar a coluna VT | mesma mensagem 2 vezes; código 0; `00002048.elf` e `00004126.elf`; coluna VT: `Clean (0)` nos dois | `passos/P29a.*`, `saidas/P29a/` | sucesso | D2 |
| P30 | [NÃO DOCUMENTADO] proposto pelos revisores | `VT_API_KEY=chave_invalida foremost-ng -x …` | aviso com chave inválida | não executado: a execução não usou chave inventada | — | não executado | — |
| P31 (= P07) | autores (README:89–101; artigo p.7) | `export VT_API_KEY=<chave>` e `-x` | consulta e contagens | sem chave VirusTotal | — | bloqueado | — |
| P32 | [NÃO DOCUMENTADO] proposto pelos revisores | consulta manual à API v3 pelo SHA-256 | rótulo coerente com a API | sem chave | — | bloqueado | — |
| P33 | [NÃO DOCUMENTADO] proposto pelos revisores | enviar um ELF recuperado ao VirusTotal | hash conhecido | sem conta nem chave | — | bloqueado | — |

#### C6 — Figura 2

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P34 | [NÃO DOCUMENTADO] proposto pelos revisores | pedir `evidence2.dd` aos autores; `find .. -name evidence2.dd`; `find / -xdev -name evidence2.dd` (`src`) | imagem obtida | pedido aos autores não enviado; nenhum arquivo encontrado no artefato nem no contêiner (código 0); busca pública anterior sem resultado (seção 4) | `passos/P34.saida.txt` | bloqueado | — |
| P35 | [NÃO DOCUMENTADO] proposto pelos revisores | `stat -c %s evidence2.dd` (esperado 2.845.109.643 B) | tamanho da Fig. 2 | sem arquivo | — | bloqueado | — |
| P36 (= P08-2) | autores (artigo p.8, Fig. 2) | `./foremost-ng -v -x evidence2.dd` | tabela da Fig. 2 | `File not found` (P08-2) | `passos/P08-2.saida.txt` | bloqueado | D0 |
| P37 | [NÃO DOCUMENTADO] proposto pelos revisores | comparar as 12 linhas (nome, offset) com a Fig. 2 | 12 linhas iguais | sem execução de P36 | — | bloqueado | — |

#### C7 — arquitetura (inspeção)

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P38a | [NÃO DOCUMENTADO] proposto pelos revisores | `grep -n 'needle->type ==' extract.c`; `grep -n 'init_builtin(.*\(ELF\|MACHO\|EVTX\|SCRIPT\)' state.c`; `grep -n 'define \(ELF\|MACHO\|EVTX\|SCRIPT\)' main.h` (`src`) | Sucesso: um novo formato exige só o parser e a entrada no registro. Falha: um novo formato exige também editar o despachante `extract_file` (cadeia de `if/else` por tipo) | `extract.c` 2630–2690: cadeia `if (needle->type == JPEG) … else if … == ELF … MACHO … EVTX … SCRIPT … MOV \|\| VJPEG … CONF`, um ramo por tipo. `state.c`: `init_builtin` para ELF (369, 452), MACHO com assinaturas `\xCA\xFE\xBA\xBE`, `\xCE\xFA\xED\xFE`, `\xCF\xFA\xED\xFE` (372–378, 678–686), EVTX `ElfFile\0\0` (381, 693) e SCRIPT `#!` (384). O `grep` em `main.h` não devolveu linhas (código 0) | `passos/P38a.saida.txt` | falha (critério: despachante com cadeia de `if/else` por tipo) | D2 |
| P38b | [NÃO DOCUMENTADO] proposto pelos revisores | `grep -n "typedef struct s_spec" -A 19 main.h`; `grep -n "void init_all" -A 82 state.c`; `grep -n "unsigned char \*extract_file" -A 69 extract.c` (`src`) | módulos da Fig. 1 e funções `extract_evtx`, `extract_script`, `extract_macho`, `extract_elf` despachadas por `extract_file` | `s_spec` (main.h:262–280) com `suffix`, `type`, `max_len`, `header`, `footer` (com tabelas de busca), `markerlist`, `searchtype`, `case_sen`, `found`, `comment`, `vt_label`, `written`. `init_all` (state.c:321) registra os tipos internos. `extract_file` (extract.c:2628) chama `extract_elf` (2681), `extract_macho` (2683), `extract_evtx` (2685) e `extract_script` (2687) | `passos/P38b.saida.txt` | sucesso | D2 |

### 2.3 Testes externos (D3)

Imagens DFTT baixadas de `dftt.sourceforge.net` (o artigo, p.7, aponta o site sem indicar imagem). Os MD5 conferem com os publicados: #11 `0069813c892a462f88dc6d376624f7d9` e #12 `6cbd2c5248fa7030d699eb6cde051623` (`passos/P39-prep.saida.txt`). Os gabaritos oficiais transcritos estão em `evidencias/dftt/gabarito-1{1,2}.tsv` (15 e 10 arquivos; todos os MD5 conferidos contra o HTML oficial). A comparação cruza nome, setor inicial e MD5.

| Passo | Origem | Comando (diretório) | Esperado | Observado (código; duração) | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| P39 | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre imagem DFTT #11) | `foremost-ng -v -i 11-carve-fat.dd -o ~/dftt/saida11` (`~/dftt`) | código 0, `audit.txt`, ≥ 1 arquivo reconhecido por `file` como do formato do subdiretório | código 0 (1,2 s); `14 FILES EXTRACTED` (`jpg=3 gif=1 wmv=2 mov=1 rif=1 ole=3 zip=1 pdf=2`); `file` reconhece cada arquivo como do formato do seu subdiretório; `recovery.log` inexistente (só `audit.txt`) | `passos/P39*.saida.txt`, `dftt/saida11/` | sucesso | D3 |
| P39-gabarito | [NÃO DOCUMENTADO] proposto pelos revisores | `compara-gabarito.py gabarito-11.tsv saida11` | esperados × recuperados × corretos | esperados 15; recuperados no setor publicado 14; corretos por MD5 10; recuperados sem correspondência no gabarito 0 (tabela abaixo) | `passos/P39-gabarito.saida.txt` | — | D3 |
| P39-t | [NÃO DOCUMENTADO] proposto pelos revisores | `foremost-ng -t evtx,elf,exe -i 11-carve-fat.dd -o ~/dftt/saida11-t` | nenhum subdiretório além de `evtx`, `elf`, `exe` (ou nenhum) | código 0; `0 FILES EXTRACTED`; nenhum subdiretório | `passos/P39-t*.saida.txt` | sucesso | D3 |
| P41 | [NÃO DOCUMENTADO] proposto pelos revisores (comando dos autores sobre imagem DFTT #12) | `foremost-ng -v -i 12-carve-ext2.dd -o ~/dftt/saida12` | idem P39 | código 0 (2,3 s); `6 FILES EXTRACTED` (`jpg=3 gif=1 bmp=1 ole=1`); `file` reconhece cada arquivo como do formato do seu subdiretório (o `.ole` como `Composite Document File V2 Document, Cannot read section info`); `recovery.log` inexistente | `passos/P41*.saida.txt`, `dftt/saida12/` | sucesso | D3 |
| P41-gabarito | [NÃO DOCUMENTADO] proposto pelos revisores | `compara-gabarito.py gabarito-12.tsv saida12` | esperados × recuperados × corretos | esperados 10; recuperados no setor publicado 6; corretos por MD5 1; sem correspondência 0. Executado sem `-d` (detecção de blocos indiretos), opção que nenhum passo do roteiro usa | `passos/P41-gabarito.saida.txt` | — | D3 |
| P41-t | [NÃO DOCUMENTADO] proposto pelos revisores | `foremost-ng -t evtx,elf,exe -i 12-carve-ext2.dd -o ~/dftt/saida12-t` | idem P39-t | código 0; `0 FILES EXTRACTED` | `passos/P41-t*.saida.txt` | sucesso | D3 |

**DFTT #11 (FAT32), arquivo por arquivo**

| Nº | Arquivo do gabarito | Setor | Bytes esperados | Recuperado no setor | Bytes recuperados | MD5 igual |
|---|---|---|---|---|---|---|
| 1 | 2003_document.doc | 281 | 19.968 | ole/00000281.ole | 20.992 | não |
| 2 | enterprise.wav | 16021 | 318.895 | wav/00016021.wav | 318.886 | não |
| 3 | haxor2.jpg (1 byte do cabeçalho corrompido de propósito) | 16645 | 24.367 | — | — | não |
| 4 | holly.xls | 16693 | 23.040 | ole/00016693.ole | 25.088 | não |
| 5 | lin_1.2.pdf | 16741 | 1.399.508 | pdf/00016741.pdf | 1.399.508 | sim |
| 6 | nlin_14.pdf | 19477 | 122.434 | pdf/00019477.pdf | 122.434 | sim |
| 7 | paul.jpg | 19717 | 29.885 | jpg/00019717.jpg | 29.885 | sim |
| 8 | pumpkin.jpg | 19777 | 444.314 | jpg/00019777.jpg | 444.314 | sim |
| 9 | shark.jpg | 20645 | 99.298 | jpg/00020645.jpg | 99.298 | sim |
| 10 | sm1.gif | 20841 | 5.498 | gif/00020841.gif | 5.498 | sim |
| 11 | surf.mov | 20853 | 550.653 | mov/00020853.mov | 550.653 | sim |
| 12 | surf.wmv | 21929 | 1.036.994 | wmv/00021929.wmv | 1.036.994 | sim |
| 13 | test.ppt (apagado) | 23957 | 11.264 | ole/00023957.ole | 7.212.032 | não |
| 14 | wword60t.zip | 23981 | 78.899 | zip/00023981.zip | 78.899 | sim |
| 15 | domopers.wmv (apagado) | 321 | 8.037.267 | wmv/00000321.wmv | 8.037.267 | sim |

**DFTT #12 (ext2, com blocos indiretos intercalados), arquivo por arquivo**

| Nº | Arquivo do gabarito | Setor | Bytes esperados | Recuperado no setor | Bytes recuperados | MD5 igual |
|---|---|---|---|---|---|---|
| 1 | haxor2.bmp (apagado) | 5162 | 163.878 | bmp/00005162.bmp | 163.878 | não |
| 2 | jimmy.doc (apagado) | 5486 | 12.800 | ole/00005486.ole | 14.848 | não |
| 3 | jn.jpg | 5514 | 28.949 | jpg/00005514.jpg | 29.973 | não |
| 4 | lin_test.pdf | 5574 | 26.618 | — | — | não |
| 5 | main_dive.jpg (sem bloco indireto) | 5628 | 8.463 | jpg/00005628.jpg | 8.463 | sim |
| 6 | n_lin_ss.pdf | 5646 | 734.652 | — | — | não |
| 7 | blogo.gif | 5122 | 18.663 | gif/00005122.gif | 19.687 | não |
| 8 | sherry.jpg | 7090 | 133.249 | jpg/00007090.jpg | 134.273 | não |
| 9 | stats.xls | 7354 | 15.360 | — | — | não |
| 10 | test.ppt | 7386 | 17.408 | — | — | não |

Nenhum gabarito DFTT contém EVTX, ELF, Mach-O ou script.

## 3. Resultados por reivindicação

Cada resultado esperado vem de `reivindicacoes.md`. Abaixo, o que foi observado, sem decisão.

**Tempo:** nenhuma reivindicação passou de 2 h; o tempo total de comandos foi de minutos (`passos.tsv`).

**Critério de desistência:** não foi acionado. O erro de P04 foi contornado com a instalação de um pacote que o `apt-get` do `Dockerfile` dos autores instala (D1), sem alterar código nem `Makefile`.

### F — compilação, instalação e uso básico

- **Artigo, p.6:** `git clone` e `make` na raiz do repositório. O `git clone` funcionou; o `make` na raiz terminou com "no makefile found".
- **README:** o arquivo `foremost-ng-<version>.tar.gz` não existe. Com a árvore do commit avaliado (zip), `make` em `src/` falhou no ambiente inicial por falta de `ctype.h` (`libc6-dev`). Depois de instalar `libc6-dev`, `make` e `sudo make install` terminaram com código 0, e `man foremost-ng`, `-h` e `-V` funcionaram.
- **Testes mínimos com entradas sintéticas (D2):** o script do `min.dd` foi recuperado idêntico. No `disk.img` (sintaxe literal do artigo, `-o /temp/output/carved`), a primeira execução terminou com `Unable to open output directory`, porque `/temp/output` não existia e não podia ser criado sem root. Com o diretório criado via `sudo`, foram extraídos 5 arquivos: o ELF embutido (prefixo de 73.752 B do original de 87.200 B), o script idêntico e 3 `.evtx` de offsets internos ao binário ELF embutido.
- **Saída:** subdiretórios por formato e `audit.txt`. Nenhuma execução gerou `recovery.log` (citado no artigo, p.7, §4.2). Os scripts recebem a extensão `.script` (o artigo cita `00000002.sh` como exemplo).

### C1 — EVTX

Esperado: "arquivo `.evtx` extraído, legível por ferramenta de análise de eventos".

- **EVTX sintético (D2):** extraído em 8192 (`00000016.evtx`, 65.536 B, os primeiros 65.536 B dos 69.632 B de cabeçalho + chunk). `file` o reconhece como EVTX; `evtx_dump.py` lê sem erro, com 0 eventos.
- **EVTX público (D3) na imagem combinada:** extraído no nome esperado, `00006452.evtx`, com e sem `-t evtx,elf,exe`. Recuperado de 10.570.240 B: os primeiros 1.118.208 B são idênticos ao original, e o arquivo vai até o fim da imagem. `evtx_dump.py` lê original e recuperado sem erro, com 1601 eventos em cada, e o XML gerado é idêntico.
- **`disk.img`:** 3 `.evtx` extraídos de offsets dentro do binário ELF embutido.
- **DFTT:** `-t evtx,elf,exe` extraiu 0 arquivos em #11 e #12.
- **Não executado:** o EVTX exportado de um Windows, proposto no roteiro (seção 4).

### C2 — scripts

Esperado: "script extraído com a linha do interpretador e o corpo legível". Reivindicação: mínimo de 32 bytes e mais que só comentários.

- **Scripts válidos:** os 7 (Bash, Python, PowerShell/pwsh, em 4 entradas) foram extraídos byte a byte idênticos, com o shebang na 1ª linha.
- **Scripts com menos de 32 B:** os dois (18 B e 13 B) não foram extraídos.
- **Scripts com shebang e só comentários:** os dois (62 B e 45 B, ambos ≥ 32 B) foram extraídos.

### C3 — Mach-O

Esperado: "binário Mach-O extraído e reconhecível por ferramenta apropriada".

- **Mach-O fat sintético (`0xCAFEBABE`):** extraído idêntico nas duas imagens (8192 B). `file` o reconhece como `Mach-O universal binary with 1 architecture`.
- **Mach-O thin sintético 64-bit:** não extraído em nenhuma das duas imagens. Seus bytes iniciais (`CF FA ED FE`) coincidem com uma das assinaturas registradas para `macho` em `state.c` (P38a).
- **Bloqueado:** os Mach-O reais (macOS), `lipo` e `otool`, por falta de macOS.

### C4 — ELF

Esperado: "arquivo `.elf` extraído e estruturalmente legível por analisador ELF". Reivindicação: 32 e 64 bits, delimitados pelos cabeçalhos de programa.

- **ELF32 sintético (1 `PT_LOAD`, sem seções):** extraído idêntico (4096 B). `readelf -h -l` lê sem erro.
- **ELF reais compilados:** `elf32_ola` (gcc -m32, 14.936 B), `/bin/ls` (142.312 B) e o binário `foremost-ng` (87.200 B) foram extraídos como prefixos idênticos de 12.296 B, 139.896 B e 73.752 B. `readelf -h -l` imprime o cabeçalho ELF e os cabeçalhos de programa (com código 0) e acrescenta `Error: Reading N bytes extends past end of file for section headers`; `file` informa `missing section headers`. No binário `foremost-ng`, o tamanho recuperado coincide com o fim do último `PT_LOAD`.
- **Saídas com e sem `-t`:** os resultados foram iguais.
- **DFTT:** 0 ELF extraídos.
- **Insumos da T7:** os da T7 (ELF de 2.648 B) não estavam disponíveis para repetição.

### C5 — VirusTotal

Esperado: "consulta associada ao hash do arquivo extraído, com o resultado de detecção registrado; sem chave, aviso e carving sem consulta (p. 7)".

- **Sem `VT_API_KEY`, com `-x`:** o programa imprime `Error: VT_API_KEY environment variable is not set.` uma vez por arquivo, extrai os mesmos ELF da execução sem `-x` e termina com código 0. No `audit.txt`, a coluna VT mostra `Clean (0)` para cada arquivo; nas execuções sem `-x`, ela mostra `N/A`. Esta execução não registrou se houve tráfego de rede.
- **Critérios do roteiro para esse passo:** dois revisores definiram sucesso como "aviso exibido e arquivos extraídos". Um revisor definiu como falha "um resultado de detecção apresentado como se tivesse sido consultado".
- **Bloqueado ou não executado:** a consulta com chave válida, a conferência manual pela API e o envio ao VirusTotal estão bloqueados (sem chave). O teste com chave inválida não foi executado.

### C6 — Figura 2

Esperado: "tabela como a da Fig. 2, com arquivos ELF, script, EXE e ZIP, seus offsets e a coluna VT".

- **Bloqueado:** `evidence2.dd` não foi obtido. Com o arquivo ausente, `./foremost-ng -v -x evidence2.dd` imprime `[!] File not found or is a directory: evidence2.dd` e `[!] No valid input files to process.` e termina com código 1.
- Nenhuma outra imagem foi usada como substituta. A comparação com as 12 linhas da Fig. 2 não foi feita.

### C7 — arquitetura (fora da regra de R)

Esperado: "organização do código correspondente à Fig. 1".

- **Registro e estrutura:** existe uma estrutura de especificação por formato (`s_spec`: sufixo, tipo, tamanho máximo, cabeçalho, rodapé, marcadores, rótulo VT). Os formatos são registrados por `init_builtin` em `init_all` e, com `-t`, em `set_search_def`.
- **Despacho:** `extract_file` despacha por uma cadeia `if/else if` sobre `needle->type`, com um ramo por tipo; os ramos de ELF, MACHO, EVTX e SCRIPT chamam `extract_elf`, `extract_macho`, `extract_evtx` e `extract_script`.

## 4. Insumos ausentes, respostas dos autores e limitações

**Insumos ausentes**
- `evidence2.dd` (Fig. 2): não está no repositório nem em fonte pública consultada (Zenodo, releases, issues, wiki, site e apresentação do autor; busca registrada em `insumos.md`).
- Chave da API VirusTotal: não fornecida e não obtida.
- `disk.img` e `memory.dump`, citados nos comandos do artigo (p.7): não fornecidos. Foram substituídos por entradas sintéticas.
- Amostras reais de Mach-O (macOS) e de EVTX exportado do Windows: não usadas. Para EVTX, foi usada uma amostra pública.
- Entradas sintéticas da T7 (ELF de 2.648 B, script de 98 B): não preservadas.

**Respostas dos autores:** nenhuma. O pedido de `evidence2.dd` está redigido (`mensagem-autores.md`), mas não foi enviado.

**Limitações e diferenças de ambiente**
- **Contêiner, não VM:** Docker sobre WSL2, com kernel do WSL2 compartilhado com o host. A distribuição é Ubuntu 24.04 (tag de 19/06/2025, apt fixado em 08/07/2025), não `ubuntu:latest` da data da execução.
- **Ambiente inicial sem `libc6-dev`:** a imagem foi construída com `--no-install-recommends`. P04–P06 e P08 falharam por isso e foram repetidos após P00b.
- **`/temp/output`:** foi criado com `sudo` (P14b-2), porque o usuário de execução não tem permissão de escrita em `/`.
- **Leitor de EVTX:** `python-evtx` 0.7.4 foi instalado pelo pacote do Ubuntu (`python3-evtx`), não por `pip` em `venv`.
- **Entradas D2 e D3:** os resultados de C1–C4 vêm de entradas montadas para esta execução (sintéticas, binários do próprio sistema e uma amostra EVTX pública). Os autores não forneceram entrada para essas reivindicações.
- **DFTT:** #12 foi executado sem `-d`; #13 (memória, sem gabarito de arquivos) não foi executado.
- **Coluna VT sem chave:** não se verificou se houve tráfego de rede.
- **Desvios do roteiro:** o teste com chave inválida (P30) não foi executado. As comparações byte a byte das entradas sintéticas de um dos revisores (P16-G-cmp) e a comparação da árvore sem CR (P11-2) foram acrescentadas na execução.
