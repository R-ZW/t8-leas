# Roteiro consolidado — Foremost-NG (execução de referência, protocolo §6.2)

**Versão avaliada:** `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` (`pacote/artefato.zip`, SHA-256 `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a`; ver `../versao.md`).
**Consolidado em:** 17/10/2026. **Status:** rascunho para revisão do aluno antes do B2; não congelado.

## 1. Fontes e método

Somente os roteiros B1 da **cadeia 1** dos três provedores foram usados para montar a união:

| Provedor (rótulo) | Fonte | Extração | SHA-256 do trecho usado | Linhas |
|---|---|---|---|---|
| Anthropic (A) | `llm-anthropic/anexos-saida/cadeia-1-B1-documento.md` (arquivo inteiro; é só o documento B1) | cópia | `a1812de44282ba8a2cf8f0a01503ce67917b839ecaaae0c6ee7f056acb2306ec` | 646 |
| OpenAI (O) | `llm-openai/cadeia-1.md`, seção `## Resposta B1` | script abaixo | `c45b7787ad4615007eef465a13a4808da31c1bf2ab6e8819e7595660185033bc` | 190 |
| Google (G) | `llm-google/cadeia-1.md`, seção `## Resposta B1` | script abaixo | `a9f6ccbbbd3f69691e6f4acca9db425ba8b825fc44c20904d65a87731ad06ce1` | 499 |

Script de extração (executado com `python -I`, saída numa pasta temporária fora do repositório); as seções `## Resposta A` e a pasta `runs/*/referencia/` não foram lidas:

```python
import sys, pathlib
# Extrai somente a seção "## Resposta B1" (até o próximo "## Prompt"/"## Resposta" ou fim).
src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out, on = [], False
for line in src.read_text(encoding='utf-8').splitlines():
    if line.startswith('## Resposta B1'):
        on = True
    elif on and (line.startswith('## Prompt') or line.startswith('## Resposta')):
        break
    if on:
        out.append(line)
dst.write_text('\n'.join(out) + '\n', encoding='utf-8')
```

Os B1 das cadeias 2 e 3 (mesmo script; para A, `cadeia-{2,3}-B1-documento.md`) foram consultados **apenas pelas tabelas-resumo**, para achar passo essencial ausente (§6.5). Resultado dessa consulta:

- **Acrescentado:** teste com imagem DFTT (A, cadeia 3, P9–P11: `-v -i <imagem DFTT> -o …` e `-t evtx,elf,exe` sobre ela). Nenhum B1 da cadeia 1 propõe imagem DFTT, e o protocolo §12 exige o DFTT #11 como passo D3 comparado ao gabarito. Entra como P39–P41.
- **Acrescentado como parte de P11:** conferência da árvore obtida contra o pacote fixado (A, cadeia 2, P6: `sha256sum` dos fontes contra o índice de `artefato.txt`).
- **Não acrescentado:** contêiner `ubuntu:latest` como base (A, cadeia 2, P2), porque o ambiente da execução já foi fixado em `ambiente/` (ver §3); empacotamento final das evidências (A, cadeias 2 e 3), porque não verifica reivindicação. Nenhum B1, de nenhuma cadeia, pede para construir (`docker build`) o `Dockerfile` dos autores; por isso não há passo separado para ele.

## 2. Convenções

- **IDs:** `P01`–`P41` são deste roteiro. Entre colchetes, os IDs originais: `A:P7` = passo P7 do roteiro A da cadeia 1; `A3:P9` = cadeia 3.
- **Fonte autoral:** `README:linha` (README.md do SHA fixado), `artigo p.N` (`pacote/artigo.pdf`), `Dockerfile:linha`, `Makefile:linha` (`src/Makefile`). Sem fonte dos autores: **[NÃO DOCUMENTADO]**.
- **Desvios (protocolo §6.3):** D0 segue a documentação; D1 correção trivial; D2 passo [NÃO DOCUMENTADO] proposto pelos revisores (inclui montar entradas sintéticas e conferências com ferramentas não citadas pelos autores); D3 dado de origem externa (DFTT, amostra pública). Um comando dos autores executado sobre entrada D2 ou D3 recebe o desvio da entrada.
- **Ordem de execução:** (1) passos dos autores que não exigem entrada (D0/D1); (2) passos [NÃO DOCUMENTADO] (D2), incluindo os comandos dos autores sobre entradas sintéticas; (3) testes externos DFTT (D3).
- **Arquivos extraídos:** nenhum é executado.

### Tempo máximo e critério de desistência

- **Tempo máximo:** 2 h de execução por reivindicação (C1 a C7) e 2 h para o bloco de preparação/teste mínimo (F). Esgotado o tempo, o passo em curso é registrado como **inconclusivo** e a execução segue para a próxima reivindicação.
- **Desistência:** um passo **essencial** (P04 compilação, P05 instalação; em cada reivindicação, a execução de carving correspondente) que falhe com erro **não documentado** cujo contorno exija desvio D2 (alterar código, `Makefile`, opções não documentadas, ou procedimento inventado para contornar o erro) encerra aquela reivindicação, registrada como **falha** (com o erro) ou **inconclusivo** (se o erro não for atribuível ao artefato). Montar entradas sintéticas e conferir saídas não são contornos de erro: são os passos D2 planejados abaixo.
- **Bloqueio:** passo que depende de insumo ausente (chave VirusTotal, `evidence2.dd`, macOS) é registrado como **bloqueado**, sem substituto.

## 3. Ambiente

| Item | Proposto | Origem | Fonte autoral |
|---|---|---|---|
| Sistema | Linux; Ubuntu (A: VM Ubuntu LTS mais recente; G: Ubuntu ou Unix-like virtualizado; O: Linux) | A, G, O | README:3 ("Linux-based"); Dockerfile:1 (`ubuntu:latest`, sem versão) |
| Pacotes | `gcc make git libssl-dev libcurl4-openssl-dev` | A, G (O cita sem pedir instalação) | Dockerfile:3–6; Makefile:1, 46 (`-lssl -lcrypto -lcurl`); README:31–35 não lista pacotes |
| Hardware | A: 2 vCPU, 4 GB, 20 GB; G: 1 vCPU, 2 GB, 1–5 GB | A, G | [NÃO DOCUMENTADO] |
| Isolamento | VM/ambiente virtual | A, G | [NÃO DOCUMENTADO] pelos autores (recomendação das instruções oficiais) |
| Registro | gravar sessão de terminal | A, O | [NÃO DOCUMENTADO] (exigência do protocolo) |

**Execução:** contêiner da imagem `ambiente/Dockerfile` (Ubuntu 24.04 `noble-20250619`, apt fixado no snapshot de 08/07/2025, pacotes do Dockerfile dos autores fixados por versão, mais `sudo`, `man-db`, `ca-certificates`, `unzip`), sobre Docker Desktop/WSL2. Justificativa e diferenças (contêiner, não VM; kernel WSL2) em `ambiente/ambiente.md`.

**Instalação de dependências (P00).** Proposta por A [A:P2] e G [G:P1]; fonte autoral Dockerfile:3–6 (`apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev`). Na versão inicial deste roteiro ela foi dada como satisfeita pela construção da imagem. Na execução, P04 falhou por falta de `ctype.h`: a imagem foi construída com `--no-install-recommends`, que omitiu `libc6-dev` (recomendação do `gcc`; o log `ambiente/construcao-imagem.txt`, linha 167, lista os recomendados omitidos), enquanto o `apt-get install -y` do Dockerfile dos autores não usa essa opção. Por isso P00 foi executado no contêiner: P00a, o comando de A:P2 (com `sudo`), e P00b, `sudo apt-get install -y libc6-dev` (D1). Em seguida, P04–P06 e P08 foram repetidos (sufixo `-2`).

## 4. Passos

### 4.1 Passos dos autores sem entrada de dados (D0/D1)

| ID | Origem | Diretório | Comando | Fonte autoral | Esperado (autores) | Desvio previsto |
|---|---|---|---|---|---|---|
| P01 | A [A:P4]; G cita a fonte [G:P2] | `~/trabalho` | `git clone https://github.com/cristianzsh/foremost-ng.git` | artigo p.6, §4; Dockerfile:8 | repositório clonado | D0 |
| P02 | A [A:P6]; G registra a divergência [G:P2] | `~/trabalho/foremost-ng` | `make` (na raiz) | artigo p.6, §4 (`cd foremost-ng`, `make`) | compilação | D0 |
| P03 | O [O:P2] (A usa o zip como alternativa [A:P4]) | `~/trabalho` | README: `tar xzvf foremost-ng-<version>.tar.gz; cd foremost-ng-<version>/src`. Execução: `unzip /pacote/artefato.zip` e `cd foremost-ng-bb812a22/src` (não existe `.tar.gz` com esse nome; o zip é o pacote do SHA fixado) | README:23, 27–28 | diretório `src` com `Makefile` | D1 |
| P04 | A, G, O [A:P7; G:P2; O:P3] | `…/foremost-ng-bb812a22/src` | `make` | README:31–33; Makefile:65–101 | binário `foremost-ng` | D1 (árvore vinda do zip) |
| P05 | A, G, O [A:P8; G:P2; O:P3] | idem | `sudo make install` | README:34; artigo p.6–7; Makefile:107–118 | binário em `/usr/local/bin`, manual em `/usr/share/man/man8`, `foremost.conf` em `/usr/local/etc`; "available system-wide" (artigo p.7) | D0 |
| P06 | A, G [A:P9; G:P3] | `~` | `man foremost-ng` (salvo com `MANPAGER=cat`) | README:76–79; artigo p.7 | página de manual | D0 |
| P07 | A, G, O [A:P26; G:P15; O:P9] | — | `export VT_API_KEY=<chave>` + `foremost-ng -x -t elf -i <entrada> -o …` | README:89–101; artigo p.7, §4 e §4.1 | consulta pelo hash, contagens no `audit.txt` | **bloqueado** (sem chave) |
| P08 | A, G, O [A:P31; G:P16; O:P11] | `…/src` | `./foremost-ng -v -x evidence2.dd` | artigo p.8, Fig. 2 | tabela da Fig. 2 (12 arquivos) | **bloqueado** (sem `evidence2.dd`); o comando é executado só para registrar a saída na ausência do arquivo, como propõe G |

### 4.2 Passos [NÃO DOCUMENTADO] propostos pelos revisores (D2)

#### Preparação e verificação

| ID | Origem | Comando / ação | Por que (justificativa dos revisores) | Fonte autoral |
|---|---|---|---|---|
| P09 | A [A:P3]; G (versões como evidência) [G:P1]; O (registro de versões) [O:P3] | `cat /etc/os-release; uname -m; gcc --version; make --version; openssl version; curl --version; dpkg -l libssl-dev libcurl4-openssl-dev` | versões exigidas pelo critério F; README não as dá | [NÃO DOCUMENTADO] |
| P10 | A [A:P5; A3:P4] | `git checkout bb812a22…; git rev-parse HEAD; git status --short` (no clone de P01) | `git clone` traz o HEAD, não o SHA avaliado | [NÃO DOCUMENTADO] |
| P11 | A [A:P4, alternativa; A2:P6] | `sha256sum /pacote/artefato.zip`; comparar a árvore do clone com a do zip | garantir que o código executado é o fixado | [NÃO DOCUMENTADO] |
| P12 | A [A:P14 e P19: `file binutils gcc-multilib python3-pip curl jq`, `python-evtx`]; G [G:P1: `python3 file binutils`] | instalar ferramentas de verificação | os autores não fornecem entradas nem ferramenta de verificação; o artigo cita "standard event log tools" sem nomear (p.6) | [NÃO DOCUMENTADO] |
| P13 | A [A:P10]; G [G:P3] | `foremost-ng -h`; `foremost-ng -V` | confirma que o binário instalado inicia e lista `-t -i -o -v -x` | [NÃO DOCUMENTADO] (opções existem em `src/main.c`) |

#### Teste mínimo (F)

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P14 | A [A:P11]; G [G:P4] | A: `min.dd` de 1 MiB com script Bash no offset 524288. G: `disk.img` de 2 MiB com o ELF `foremost-ng` no offset 4096 e um script no offset 524288; `mkdir -p /temp/output` | entradas criadas | [NÃO DOCUMENTADO] (artigo p.7 usa `disk.img` sem fornecê-lo) |
| P15 | A [A:P12]; G [G:P5]; O [O:P4] | `foremost-ng -i min.dd -o ~/aval/saida_min` (A) e `./foremost-ng -i disk.img -o /temp/output/carved` (G, sintaxe literal do artigo) | todos os parsers inspecionam; subdiretórios por formato; `audit.txt` | comando: artigo p.7, §4.1; entrada D2 |
| P16 | A [A:P13]; G [G:P5] | `cat audit.txt; ls -R`; `cmp` do script recuperado com o original | `00001024.script` (A); ELF e script recuperados (G) | [NÃO DOCUMENTADO] (conferência) |

#### C1 — EVTX

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P17 | A [A:P14]; G [G:P6] | A: `.evtx` real exportado de um Windows (`wevtutil epl Application …`). G: imagem `c1_evtx.img` (256 KiB) com cabeçalho `ElfFile\0` sintético e 1 chunk de 64 KiB no offset 8192 | entrada com EVTX | [NÃO DOCUMENTADO] |
| P18 | G [G:P7]; A [A:P16, P18] | `./foremost-ng -v -t evtx -i c1_evtx.img -o /tmp/out_c1`; `file`; verificação do magic; para o EVTX real, localização no offset previsto e `cmp` com o original | `00000016.evtx` (G); `.evtx` no offset previsto (A) | comando: artigo p.7, §4.1 (`-t evtx,…`); conferência [NÃO DOCUMENTADO] |
| P19 | A [A:P19]; G (`evtx_dump`, se instalado) [G:P7] | `evtx_dump.py` no original e no recuperado; contar `<Event ` | recuperado lido sem exceção, mesma contagem | [NÃO DOCUMENTADO] ("standard event log tools", artigo p.6) |

#### C2 — Scripts

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P20 | A [A:P14]; G [G:P8] | A: `s_bash.sh`, `s_py.py`, `s_ps.ps1`, negativos `neg_comentario.sh`, `neg_curto.sh`. G: `c2_script.img` com 2 válidos (offsets 4096, 16384), 1 com < 32 bytes (32768) e 1 só com comentários (49152) | entradas criadas | [NÃO DOCUMENTADO] |
| P21 | G [G:P9]; A [A:P16, P20] | `./foremost-ng -v -t script -i c2_script.img -o /tmp/out_c2` (G); conferência `head`/`cmp` (A) | `00000008.script` e `00000032.script` (G); três scripts idênticos ao original (A) | `-t script` [NÃO DOCUMENTADO] no README/artigo (G); artigo p.6, §3 descreve o parser |
| P22 | A [A:P21]; G [G:P9] | verificar que os negativos não foram extraídos | negativos descartados | artigo p.6, §3 ("at least 32 bytes … more than comments"); conferência [NÃO DOCUMENTADO] |

#### C3 — Mach-O

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P23 | A [A:P14]; G [G:P10] | A: Mach-O fat e thin reais via `lipo` num macOS. G: `c3_macho.img` com thin sintético de 4096 B (offset 8192) e fat sintético de 8192 B (offset 32768) | entradas criadas | [NÃO DOCUMENTADO] |
| P24 | G [G:P11]; A [A:P22] | `./foremost-ng -v -t macho -i c3_macho.img -o /tmp/out_c3`; `file`; `ls -l`; `cmp` (A) | thin 4096 B e fat 8192 B reconhecidos por `file` | `-t macho` [NÃO DOCUMENTADO] (G); artigo p.6, §3 descreve o parser |
| P25 | A [A:P23] | `lipo -info`; `otool -h` num macOS | estrutura lida sem erro | [NÃO DOCUMENTADO]; pulado sem macOS (o próprio roteiro A prevê) |

#### C4 — ELF

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P26 | A [A:P14]; G [G:P12] | A: `cp /bin/ls amostras/elf64_ls`; `gcc -m32 -o amostras/elf32_ola ola.c`. G: `memory.dump` (512 KiB) com ELF32 sintético de 4096 B (offset 4096) e o binário `foremost-ng` (offset 65536) | entradas criadas | [NÃO DOCUMENTADO] (artigo p.7 usa `memory.dump` sem fornecê-lo) |
| P27 | G [G:P13]; A [A:P24] | `./foremost-ng -v -t elf -i memory.dump -o /tmp/out_c4`; `file`; `readelf -h -l`; `readelf -S`; tamanhos; `cmp -n` do prefixo (A) | ELF32 `00000008.elf` e ELF64 `00000128.elf` legíveis (G); ELF 32/64 sem erro em `readelf -h -l` (A) | comando: artigo p.7, §4.1 (`-x -t elf`, sem `-x` aqui); conferência [NÃO DOCUMENTADO] |

#### Imagem combinada (C1–C5)

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P28 | A [A:P15, P16, P17] | montar `teste.dd` com todas as amostras de A (separadas por 1 MiB, offsets em `P15_offsets.txt`); `foremost-ng -i teste.dd -o saida_todos`; `foremost-ng -t evtx,elf,exe -i teste.dd -o saida_tipos`; conferências de A:P18, P20–P22, P24 sobre essas saídas | arquivos nos nomes esperados (offset ÷ 512); em `saida_tipos`, só `evtx`, `elf`, `exe` | comandos: artigo p.7, §4.1; montagem [NÃO DOCUMENTADO] |

#### C5 — VirusTotal

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P29 | A [A:P25, 1ª parte]; G [G:P14]; O [O:P10] | `env -u VT_API_KEY ./foremost-ng -x -t elf -i memory.dump -o ./carved-files_nokey` (G); `unset VT_API_KEY; foremost-ng -x -t elf -i teste.dd -o saida_vt_semchave` (A) | aviso, carving mantido, nenhuma consulta | comando: artigo p.7, §4.1; entrada D2 |
| P30 | A [A:P25, 2ª parte] | `VT_API_KEY=chave_invalida foremost-ng -x …` | aviso com chave inválida | artigo p.7 ("missing or invalid"); **não executado**: a instrução desta execução proíbe usar chave inventada |
| P31 | = P07 | com chave válida | — | **bloqueado** |
| P32 | A [A:P27] | `curl` na API v3 pelo SHA-256 de cada ELF recuperado | rótulo coerente com a API | [NÃO DOCUMENTADO]; **bloqueado** (sem chave) |
| P33 | A [A:P28] | enviar um ELF recuperado ao VirusTotal pela interface web | hash passa a ser conhecido | [NÃO DOCUMENTADO]; **bloqueado** (sem conta/chave) |

#### C6 — Figura 2

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P34 | A [A:P29]; G (`find .. -name evidence2.dd`) [G:P16]; O (obtenção [NÃO DOCUMENTADO]) [O:P11] | pedir `evidence2.dd` aos autores; procurar o arquivo na árvore | imagem obtida | [NÃO DOCUMENTADO]; o pedido aos autores **não foi enviado** (`mensagem-autores.md`); busca pública registrada em `insumos.md` |
| P35 | A [A:P30] | `stat -c %s evidence2.dd` = 2845109643; `sha256sum` | tamanho da Fig. 2 | [NÃO DOCUMENTADO]; **bloqueado** |
| P36 | = P08 | `./foremost-ng -v -x evidence2.dd` | tabela da Fig. 2 | artigo p.8; **bloqueado** |
| P37 | A [A:P32]; O (comparação linha a linha) [O:P11]; G [G:P16] | comparar as 12 linhas (nome, offset) com a Fig. 2 | 12 linhas iguais | artigo p.8, Fig. 2; **bloqueado** |

#### C7 — Arquitetura (fora da regra de R)

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P38 | A [A:P33]; G [G:P17] | A: `grep -n 'needle->type ==' extract.c`; `grep -n 'init_builtin(.*\(ELF\|MACHO\|EVTX\|SCRIPT\)' state.c`; `grep -n 'define \(ELF\|MACHO\|EVTX\|SCRIPT\)' main.h`. G: `grep -n "typedef struct s_spec" -A 19 main.h`; `grep -n "void init_all" -A 82 state.c`; `grep -n "unsigned char \*extract_file" -A 69 extract.c` | parsers registrados numa lista; despachante (artigo p.3, §2) | [NÃO DOCUMENTADO] (inspeção) |

### 4.3 Testes externos (D3)

| ID | Origem | Comando / ação | Esperado | Fonte autoral |
|---|---|---|---|---|
| P39 | A, cadeia 3 [A3:P9, P10]; protocolo §12 | DFTT #11 (`11-carve-fat.dd`, MD5 conferido em `insumos.md`): `foremost-ng -v -i 11-carve-fat.dd -o saida`; comparar MD5 dos recuperados com o gabarito oficial (15 arquivos): esperados × recuperados × corretos | arquivos do gabarito recuperados | DFTT citado no artigo p.7 ("Carving test samples can be downloaded from https://dftt.sourceforge.net"); escolha da imagem [NÃO DOCUMENTADO] |
| P40 | A, cadeia 3 [A3:P11] | `foremost-ng -t evtx,elf,exe -i 11-carve-fat.dd -o …` | só subdiretórios `evtx`, `elf`, `exe` (ou nenhum) | artigo p.7, §4.1 |
| P41 | A, cadeia 3 [A3:P9–P11] (imagem "escolhida no site") | DFTT #12 (`12-carve-ext2.dd`): como P39 e P40, contra o gabarito de 10 arquivos | idem | idem |

### 4.4 Identificadores usados na execução

Quando A e G propõem variantes do mesmo passo, a execução usa sufixo `a` (variante de A) e `b` (variante de G), por exemplo `P15a`/`P15b`; `-conf` marca a conferência feita logo após um carving; `-2` marca a repetição de um passo. Acrescentados na execução, ambos D2: `P11-2` (comparação da árvore ignorando CR, porque os arquivos de texto do zip têm fim de linha CRLF) e `P16-G-cmp` (comparação byte a byte das saídas dos testes de G com os bytes recortados das imagens de entrada).

## 5. Passos propostos que não serão executados como escritos

| Passo | Origem | Motivo | Tratamento |
|---|---|---|---|
| Exportar `.evtx` de um Windows com `wevtutil epl Application` | A [A:P14] | o host disponível é o Windows pessoal do aluno; o log exportado traria dados da máquina para as evidências | EVTX sintético de G (D2) e amostra EVTX pública (D3): `system.evtx` dos dados de teste do python-evtx, commit `c0007441657899c39180de10a2be1a0e43dbeaf9`, 1.118.208 B, SHA-256 `ccb83cfe…f8dc6ae` |
| Obter Mach-O reais com `lipo` e `lipo -info`/`otool -h` | A [A:P14, P23] | não há macOS disponível | Mach-O sintéticos de G (D2), também inseridos na imagem combinada de A (P28); P25 bloqueado |
| Chave inválida em `-x` | A [A:P25] | instrução desta execução: não inventar chave | não executado |
| Chave válida, consulta manual e envio ao VirusTotal | A, G, O [A:P26–P28; G:P15; O:P9] | sem chave VirusTotal | bloqueado |
| Pedido de `evidence2.dd` aos autores | A [A:P29] | mensagem não enviada (decisão do aluno) | bloqueado |
| Repetir a extração ELF da T7 (protocolo §12) | protocolo §12 | as entradas da T7 (ELF de 2.648 B, script de 98 B) não foram preservadas (`insumos.md`) | ELF novos de A e G em Ubuntu (P26–P28) |
| `docker build` do `Dockerfile` dos autores | nenhum B1 pede | — | não executado |

## 6. Tabela-resumo

| ID | Bloco | Reiv. | Origem | Fonte autoral | Desvio |
|---|---|---|---|---|---|
| P00 | autores | F | A, G | Dockerfile:3–6 | D1 (acrescentado na execução; ver §3) |
| P01 | autores | F | A, G | artigo p.6 | D0 |
| P02 | autores | F | A, G | artigo p.6 | D0 |
| P03 | autores | F | O, A | README:23–28 | D1 |
| P04 | autores | F | A, G, O | README:31–33 | D1 |
| P05 | autores | F | A, G, O | README:34 | D0 |
| P06 | autores | F | A, G | README:76–79 | D0 |
| P07 | autores | C5 | A, G, O | README:89–101; artigo p.7 | bloqueado |
| P08 | autores | C6 | A, G, O | artigo p.8 | bloqueado |
| P09 | revisores | F | A, G, O | [NÃO DOCUMENTADO] | D2 |
| P10 | revisores | F, R | A | [NÃO DOCUMENTADO] | D2 |
| P11 | revisores | F, R | A | [NÃO DOCUMENTADO] | D2 |
| P12 | revisores | C1–C4 | A, G | [NÃO DOCUMENTADO] | D2 |
| P13 | revisores | F | A, G | [NÃO DOCUMENTADO] | D2 |
| P14 | revisores | F | A, G | [NÃO DOCUMENTADO] | D2 |
| P15 | revisores (comando dos autores) | F | A, G, O | artigo p.7 | D2 |
| P16 | revisores | F, C2 | A, G | [NÃO DOCUMENTADO] | D2 |
| P17 | revisores | C1 | A, G | [NÃO DOCUMENTADO] | D2 / D3 |
| P18 | revisores (comando dos autores) | C1 | G, A | artigo p.7 | D2 / D3 |
| P19 | revisores | C1 | A, G | [NÃO DOCUMENTADO] | D2 / D3 |
| P20 | revisores | C2 | A, G | [NÃO DOCUMENTADO] | D2 |
| P21 | revisores | C2 | G, A | [NÃO DOCUMENTADO] (`-t script`) | D2 |
| P22 | revisores | C2 | A, G | artigo p.6 | D2 |
| P23 | revisores | C3 | A, G | [NÃO DOCUMENTADO] | D2 |
| P24 | revisores | C3 | G, A | [NÃO DOCUMENTADO] (`-t macho`) | D2 |
| P25 | revisores | C3 | A | [NÃO DOCUMENTADO] | bloqueado |
| P26 | revisores | C4 | A, G | [NÃO DOCUMENTADO] | D2 |
| P27 | revisores (comando dos autores) | C4 | G, A | artigo p.7 | D2 |
| P28 | revisores (comandos dos autores) | C1–C4 | A | artigo p.7 | D2 / D3 |
| P29 | revisores (comando dos autores) | C5 | A, G, O | artigo p.7 | D2 |
| P30 | revisores | C5 | A | artigo p.7 | não executado |
| P31 | = P07 | C5 | A, G, O | README:89–101 | bloqueado |
| P32 | revisores | C5 | A | [NÃO DOCUMENTADO] | bloqueado |
| P33 | revisores | C5 | A | [NÃO DOCUMENTADO] | bloqueado |
| P34 | revisores | C6 | A, G, O | [NÃO DOCUMENTADO] | bloqueado |
| P35 | revisores | C6 | A | [NÃO DOCUMENTADO] | bloqueado |
| P36 | = P08 | C6 | A, G, O | artigo p.8 | bloqueado |
| P37 | revisores | C6 | A, O, G | artigo p.8 | bloqueado |
| P38 | revisores | C7 | A, G | [NÃO DOCUMENTADO] | D2 |
| P39 | revisores (cadeia 3) + protocolo §12 | F (complementar) | A (cadeia 3) | artigo p.7 (site DFTT) | D3 |
| P40 | revisores (cadeia 3) | F (complementar) | A (cadeia 3) | artigo p.7 | D3 |
| P41 | revisores (cadeia 3) | F (complementar) | A (cadeia 3) | artigo p.7 | D3 |
