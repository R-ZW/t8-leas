# Roteiro de execução — Foremost-NG (SBSeg 2025), selos F e R

Oct 15, 2026 · @edu

## Escopo e convenções

Este roteiro leva a uma decisão sobre F e R para o commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`, em 33 passos (P1–P33). Ele foi escrito a partir dos anexos; nada aqui foi executado, e todo resultado esperado é o declarado pelos autores ou, quando eles não declaram, está escrito "não informado pelos autores".

**Fontes de procedimento dos autores** (as únicas usadas como "documentado"): `README.md` (instalação, uso, VirusTotal), `Dockerfile` (pacotes do ambiente), `src/Makefile` (alvos de compilação) e o artigo, pp. 6–8 (§4, §4.1, §4.2 e Fig. 2). O vídeo citado no artigo (p. 7) e a página de manual `foremost-ng.8.gz` não estavam legíveis nos anexos; não foram usados.

**\[NÃO DOCUMENTADO\]** marca todo passo que os autores não descrevem. Cada um traz a justificativa: por que, sem ele, um critério de F ou de R não pode ser verificado. O ponto central é que os autores não fornecem nenhum dado de entrada; por isso C1–C5 dependem de uma imagem de teste montada pelo revisor (P14–P15), e C6 depende de obter dos autores a imagem `evidence2.dd` (P29). Os passos marcados \[CONFERÊNCIA NÃO DOCUMENTADA\] (P13, P18, P20–P22, P24) comparam a saída com o resultado que os autores descrevem, mas usam ferramentas escolhidas pelo revisor (cmp, file, readelf); sem elas, o resultado esperado de cada reivindicação não pode ser constatado.

**Formato de cada passo**: selo e reivindicação; diretório; comando exato; resultado esperado segundo os autores; evidência a salvar; critério de sucesso; critério de falha; critério de interrupção.

**Convenções do ambiente** \[NÃO DOCUMENTADO — necessárias para que o parecer traga prova de execução, exigida pelas instruções oficiais\]:

- Área de trabalho: `~/aval`. Repositório: `~/aval/foremost-ng`. Amostras: `~/aval/amostras`. Evidências: `~/aval/evidencias`.
- Grave toda a sessão de terminal: `script -f ~/aval/evidencias/sessao.log` logo após P1, e saia com `exit` só ao final. Os comandos dos autores aparecem abaixo sem alteração; a gravação fica por fora deles.
- Cada execução de carving usa um diretório de saída novo e inexistente, para que um resultado não se misture com outro.
- Não execute nenhum arquivo extraído: a Fig. 2 mostra arquivos marcados como maliciosos (linhas 4 e 9).

## Requisitos do ambiente

Os autores documentam apenas o sistema (Linux, Ubuntu sem versão fixada) e cinco pacotes; hardware, versões e ferramentas de verificação não são informados. A tabela separa o que é dos autores do que é escolha do revisor.

| Item | Requisito | Fonte | Situação |
| --- | --- | --- | --- |
| Sistema | Linux; Ubuntu (imagem `ubuntu:latest`, versão não fixada) | \[README.md:3\]; \[Dockerfile:1\] | Documentado, sem versão |
| Pacotes de compilação | `gcc make git libssl-dev libcurl4-openssl-dev` | \[Dockerfile:5\] | Documentado só no Dockerfile, não no README |
| Rede | GitHub (clone), espelhos do apt, `www.virustotal.com` (C5, C6) | \[artigo.pdf:p. 6\]; \[src/vt\_query.c:21\] | Implícito |
| Conta externa | Chave de API do VirusTotal na variável `VT_API_KEY` | \[README.md:95–101\] | Documentado |
| Hardware | Recomendação do revisor: VM x86\_64, 2 vCPU, 4 GB de RAM, 20 GB livres (a imagem da Fig. 2 tem 2.845.109.643 bytes) | \[artigo.pdf:p. 8, Fig. 2\] para o tamanho | \[NÃO DOCUMENTADO\] |
| Isolamento | VM com snapshot; as instruções oficiais recomendam ambiente virtual | \[instrucoes-oficiais.md:Contexto de revisão\] | \[NÃO DOCUMENTADO\] pelos autores |
| Ferramentas de verificação | `file`, `readelf` (binutils), `gcc-multilib` (ELF 32 bits), `python3-pip` e `python-evtx` (leitor de EVTX), `curl`, `jq` | — | \[NÃO DOCUMENTADO\]: o artigo diz que os arquivos são legíveis por "standard event log tools" (p. 6), sem nomear nenhuma |
| Amostras | 1 arquivo `.evtx` (exportado de um Windows), 1 Mach-O fat e 1 thin (de um macOS), ELF 32 e 64 bits, scripts Bash/Python/PowerShell | — | \[NÃO DOCUMENTADO\]: o artefato não traz dados de teste; o artigo só aponta `https://dftt.sourceforge.net` (p. 7), sem dizer qual imagem usar |
| Dados da Fig. 2 | `evidence2.dd` | \[artigo.pdf:p. 8, Fig. 2\] | Ausente do artefato |

O Dockerfile dos autores não serve para avaliar este commit: ele clona o HEAD atual do GitHub, não `bb812a22` \[Dockerfile:8\]. Por isso o roteiro usa uma VM Ubuntu com os pacotes do Dockerfile e o checkout explícito do commit (P5). Use a versão LTS mais recente do Ubuntu e registre-a em P3.

## Preparação: obter, compilar e instalar (P1–P8)

Se P7 ou P8 falharem, o roteiro para: F não é atribuído e R não pode ser avaliado. Não corrija código nem Makefile; qualquer correção seria um procedimento não documentado e deve apenas ser registrada.

### P1 — Criar o ambiente \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: F, R / todas.
- **Justificativa**: os autores não descrevem ambiente além de "Linux"; as instruções oficiais pedem ambiente que satisfaça os requisitos e recomendam ambiente virtual.
- **Diretório**: `~`
- **Comando**: crie a VM Ubuntu e tire um snapshot; depois `mkdir -p ~/aval/evidencias ~/aval/amostras && cd ~/aval && script -f ~/aval/evidencias/sessao.log`
- **Esperado segundo os autores**: não informado.
- **Evidência**: nome e versão do hipervisor, configuração da VM (CPU, RAM, disco), início de `sessao.log`.
- **Sucesso**: VM ativa e gravação de sessão iniciada.
- **Falha**: sem acesso à rede ou disco livre inferior a 20 GB.
- **Interrupção**: sem rede, pare (P2, P4 e C5 precisam dela).

### P2 — Instalar dependências

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval`
- **Comando**: `sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev`
- **Esperado segundo os autores**: pacotes instalados \[Dockerfile:3–5\]. O Dockerfile roda como root; em VM, o `sudo` é a única adaptação.
- **Evidência**: saída do comando em `sessao.log`.
- **Sucesso**: apt termina sem erro.
- **Falha**: algum pacote inexistente na versão do Ubuntu usada.
- **Interrupção**: pacote indisponível, pare e registre como falha de documentação de dependências (F).

### P3 — Registrar versões \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: F / —.
- **Justificativa**: o critério F exige versões de dependências e ambiente; o README não as informa, então o parecer precisa registrá-las.
- **Diretório**: `~/aval`
- **Comando**: `{ cat /etc/os-release; uname -m; gcc --version | head -1; make --version | head -1; openssl version; curl --version | head -1; dpkg -l libssl-dev libcurl4-openssl-dev | tail -2; } > evidencias/P3_versoes.txt 2>&1`
- **Esperado segundo os autores**: não informado.
- **Evidência**: `evidencias/P3_versoes.txt`.
- **Sucesso**: arquivo com todas as versões.
- **Falha**: não se aplica.
- **Interrupção**: nenhuma.

### P4 — Clonar o repositório

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval`
- **Comando**: `git clone https://github.com/cristianzsh/foremost-ng.git`
- **Esperado segundo os autores**: repositório clonado \[artigo.pdf:p. 6, §4; Dockerfile:8\].
- **Evidência**: saída do clone.
- **Sucesso**: diretório `~/aval/foremost-ng` criado.
- **Falha**: repositório inexistente ou privado.
- **Interrupção**: em caso de falha, use o `artefato.zip` original e confira `sha256sum artefato.zip` = `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a` \[artefato.txt:cabeçalho\]; sem nenhum dos dois, pare.

### P5 — Fixar o commit avaliado \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: F, R / todas.
- **Justificativa**: o README parte de um `tar.gz` com versão genérica e o artigo, de um `git clone` do HEAD; nenhum dos dois garante a versão avaliada.
- **Diretório**: `~/aval/foremost-ng`
- **Comando**: `git checkout bb812a22cb06ef87b5a2d877dfb6f40eb12d460d && git rev-parse HEAD && git status --short`
- **Esperado segundo os autores**: não informado.
- **Evidência**: saída dos três comandos.
- **Sucesso**: `git rev-parse HEAD` imprime exatamente `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` e `git status --short` sai vazio.
- **Falha**: commit não encontrado.
- **Interrupção**: commit ausente e sem `artefato.zip` verificado, pare.

### P6 — Compilar como manda o artigo

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval/foremost-ng`
- **Comando**: `make; echo "exit=$?"`
- **Esperado segundo os autores**: compilação \[artigo.pdf:p. 6, §4: `cd foremost-ng` e `make`\].
- **Evidência**: saída e código de saída.
- **Sucesso**: compilação concluída.
- **Falha**: `make` reclama da falta de Makefile; o artefato só tem `src/Makefile` \[artefato.txt:índice\]. Registre como inconsistência entre artigo e artefato.
- **Interrupção**: nenhuma; siga para P7, que segue o README.

### P7 — Compilar como manda o README

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval/foremost-ng/src`
- **Comando**: `make; echo "exit=$?"; ls -l foremost-ng`
- **Esperado segundo os autores**: binário `foremost-ng` \[README.md:28–33; src/Makefile:7, 100–101\].
- **Evidência**: log completo de compilação, incluindo avisos; `ls -l`.
- **Sucesso**: `exit=0` e `foremost-ng` presente.
- **Falha**: erro de compilação ou de ligação (`-lssl -lcrypto -lcurl`, \[src/Makefile:46\]).
- **Interrupção**: falha, pare o roteiro.

### P8 — Instalar

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval/foremost-ng/src`
- **Comando**: `sudo make install; echo "exit=$?"; which foremost-ng; ls -l /usr/local/etc/foremost.conf`
- **Esperado segundo os autores**: "the foremost-ng binary is available system-wide" \[artigo.pdf:p. 7\]; binário em `/usr/local/bin`, manual em `/usr/share/man/man8`, configuração em `/usr/local/etc` \[src/Makefile:107–118\].
- **Evidência**: saída da instalação, `which`, `ls`.
- **Sucesso**: `which` imprime `/usr/local/bin/foremost-ng` e `foremost.conf` existe.
- **Falha**: erro de instalação.
- **Interrupção**: falha, pare o roteiro.

## Teste mínimo do selo F (P9–P13)

F fica demonstrado se P12 e P13 mostrarem um arquivo recuperado, no subdiretório do formato e registrado em `audit.txt`. Como os autores não fornecem exemplo mínimo nem dado de entrada \[README.md:74–85\], a imagem de P11 é montada pelo revisor.

### P9 — Ler o manual

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval`
- **Comando**: `man foremost-ng` (para salvar: `MANPAGER=cat man foremost-ng > evidencias/P9_man.txt`)
- **Esperado segundo os autores**: documentação completa da ferramenta \[README.md:76–79; artigo.pdf:p. 7\].
- **Evidência**: `evidencias/P9_man.txt`.
- **Sucesso**: página exibida; registre se ela lista `-x` e os tipos `evtx`, `elf`, `macho`, `script`.
- **Falha**: "No manual entry". Em VMs mínimas pode faltar o pacote `man-db`; registre qual foi o caso.
- **Interrupção**: nenhuma.

### P10 — Ajuda da linha de comando \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: F / —.
- **Justificativa**: confirma que o binário instalado inicia e lista as opções usadas no artigo; nem README nem artigo citam `-h`, mas ele está no próprio programa.
- **Diretório**: `~/aval`
- **Comando**: `foremost-ng -h; echo "exit=$?"`
- **Esperado segundo os autores**: não informado. O código imprime as opções, incluindo "-x  Enable VirusTotal scan (needs API key)." \[src/main.c:110\].
- **Evidência**: saída completa.
- **Sucesso**: lista com `-t`, `-i`, `-o`, `-v`, `-x` e `exit=0`.
- **Falha**: erro de execução ou falha de segmentação.
- **Interrupção**: falha de segmentação, pare (F não atribuído).

### P11 — Montar a imagem mínima \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: F / —.
- **Justificativa**: as instruções oficiais exigem ao menos um exemplo mínimo executado; o artefato não traz nenhum dado de entrada.
- **Diretório**: `~/aval`
- **Comando**:

```
printf '#!/bin/bash\n# teste minimo\necho "foremost-ng teste minimo F"\nls -l /tmp\n' > amostras/min.sh
truncate -s 1M min.dd
dd if=amostras/min.sh of=min.dd bs=512 seek=1024 conv=notrunc
sha256sum amostras/min.sh min.dd > evidencias/P11_hashes.txt
```

- **Esperado segundo os autores**: não informado.
- **Evidência**: `evidencias/P11_hashes.txt`.
- **Sucesso**: `min.dd` com 1.048.576 bytes e o script no offset 524.288 (bloco 1024).
- **Falha**: não se aplica.
- **Interrupção**: nenhuma.

### P12 — Executar o carving padrão

- **Selo / reivindicação**: F / —.
- **Diretório**: `~/aval`
- **Comando**: `foremost-ng -i min.dd -o ~/aval/saida_min; echo "exit=$?"`
- **Esperado segundo os autores**: "every registered parser … will inspect the raw data"; arquivos em "subdirectories under specified output directory, each named after the corresponding file format" \[artigo.pdf:p. 7, §4.1\]; metadados em `audit.txt` \[artigo.pdf:p. 6\].
- **Evidência**: saída do terminal; `find ~/aval/saida_min -type f | sort > evidencias/P12_arquivos.txt`; cópia de `saida_min/audit.txt`.
- **Sucesso**: `exit=0` e `audit.txt` criado.
- **Falha**: erro, nenhum diretório de saída ou `audit.txt` ausente.
- **Interrupção**: falha, pare: F não atribuído.

### P13 — Conferir a saída mínima \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: F / (C2 por antecipação).
- **Diretório**: `~/aval`
- **Comando**: `cat saida_min/audit.txt; ls -R saida_min; cmp amostras/min.sh saida_min/script/00001024.script && echo IDENTICO`
- **Esperado segundo os autores**: arquivo nomeado por número sequencial de 8 dígitos e registro em `audit.txt` \[artigo.pdf:p. 7, §4.2\]. O artigo cita a extensão `.sh`; a Fig. 2 mostra `.script`.
- **Evidência**: saída dos três comandos.
- **Sucesso**: `audit.txt` lista `00001024.script` no offset 524288 e `cmp` imprime `IDENTICO`.
- **Falha**: nenhum arquivo do tipo script recuperado, ou conteúdo diferente do original.
- **Interrupção**: nenhum arquivo recuperado, pare: a funcionalidade não foi observada e F não é atribuído. Extensão `.script` em vez de `.sh` é divergência a registrar, não falha.

## Imagem de teste para C1–C4 (P14–P17)

Uma única imagem com amostras em offsets conhecidos permite conferir, para cada reivindicação, nome, offset e conteúdo do arquivo recuperado. Toda esta seção é \[NÃO DOCUMENTADO\]: o artefato não traz amostras e o artigo só aponta o site DFTT (p. 7), sem dizer qual imagem contém EVTX, Mach-O, ELF ou scripts. Sem uma entrada com esses formatos, nenhuma de C1–C4 pode ser observada.

### P14 — Reunir as amostras \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C1–C4.
- **Justificativa**: acima. As amostras negativas testam as duas regras de C2 (mínimo de 32 bytes e corpo além de comentários).
- **Diretório**: `~/aval`
- **Comando** (na VM):

```
sudo apt-get install -y gcc-multilib file binutils python3-pip curl jq
cp /bin/ls amostras/elf64_ls
printf '#include <stdio.h>\nint main(void){puts("ola");return 0;}\n' > /tmp/ola.c
gcc -m32 -o amostras/elf32_ola /tmp/ola.c
printf '#!/bin/bash\nfor i in 1 2 3; do\n  echo "linha $i"\ndone\n' > amostras/s_bash.sh
printf '#!/usr/bin/env python3\nimport sys\nprint("ola", sys.argv)\n' > amostras/s_py.py
printf '#!/usr/bin/env pwsh\nGet-ChildItem -Path . | ForEach-Object { $_.Name }\n' > amostras/s_ps.ps1
printf '#!/bin/sh\n# so comentario\n# outro comentario\n' > amostras/neg_comentario.sh
printf '#!/bin/sh\nls\n' > amostras/neg_curto.sh
```

- **Comando** (fora da VM): no macOS, `lipo -archs /bin/ls`; depois `cp /bin/ls macho_fat` e `lipo -thin <uma arquitetura listada> /bin/ls -output macho_thin`. No Windows, prompt de administrador: `wevtutil epl Application C:\temp\evtx_app.evtx`. Copie os três arquivos para `~/aval/amostras/`.
- **Fechamento**: `file amostras/* > evidencias/P14_file.txt; sha256sum amostras/* > evidencias/P14_amostras.txt`
- **Esperado segundo os autores**: não informado.
- **Evidência**: `P14_file.txt`, `P14_amostras.txt`, origem de cada amostra (máquina, sistema, data).
- **Sucesso**: `file` reconhece ELF 32 e 64 bits, Mach-O universal e Mach-O thin, e o `.evtx` existe.
- **Falha**: alguma amostra não obtida.
- **Interrupção**: sem `.evtx`, C1 fica "não verificado"; sem Mach-O, C3 fica "não verificado". As demais seguem. Um Mach-O thin de 32 bits dificilmente estará disponível; registre que só 64 bits foi testado.

### P15 — Montar `teste.dd` \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C1–C5.
- **Justificativa**: cada amostra fica em offset múltiplo de 512, separada por 1 MiB de zeros, o que permite prever o nome do arquivo recuperado (offset ÷ 512, com 8 dígitos) e isolar cada recuperação.
- **Diretório**: `~/aval`
- **Comando**:

```
IMG=teste.dd; GAP=1048576; off=$GAP
rm -f $IMG; truncate -s $off $IMG
: > evidencias/P15_offsets.txt
for f in amostras/*; do
  [ "$f" = amostras/min.sh ] && continue
  dd if="$f" of=$IMG bs=512 seek=$((off/512)) conv=notrunc status=none
  printf '%s %s %08d %s\n' "$f" "$off" "$((off/512))" "$(sha256sum < "$f" | cut -d' ' -f1)" >> evidencias/P15_offsets.txt
  sz=$(stat -c %s "$f")
  off=$(( (off + sz + GAP + 511) / 512 * 512 ))
done
truncate -s $((off + GAP)) $IMG
sha256sum $IMG >> evidencias/P15_offsets.txt
```

- **Esperado segundo os autores**: não informado.
- **Evidência**: `evidencias/P15_offsets.txt` (amostra, offset, nome esperado, SHA-256).
- **Sucesso**: uma linha por amostra e o hash da imagem.
- **Falha / interrupção**: erro de `dd`; corrija o comando de montagem antes de seguir.

### P16 — Carving padrão sobre `teste.dd`

- **Selo / reivindicação**: R / C1–C4.
- **Diretório**: `~/aval`
- **Comando**: `foremost-ng -i teste.dd -o ~/aval/saida_todos; echo "exit=$?"`
- **Esperado segundo os autores**: todos os parsers registrados inspecionam a imagem e gravam por subdiretório de formato \[artigo.pdf:p. 7, §4.1\].
- **Evidência**: saída do terminal; `saida_todos/audit.txt`; `find saida_todos -type f | sort > evidencias/P16_arquivos.txt`.
- **Sucesso**: `exit=0` e `audit.txt` presente.
- **Falha**: erro ou nenhuma saída.
- **Interrupção**: falha, pare os blocos C1–C4. Arquivos extras (por exemplo, `exe` ou `script` recortados de dentro de binários) são esperados; registre-os sem tratá-los como falha.

### P17 — Carving restrito por tipo

- **Selo / reivindicação**: R / C1, C4.
- **Diretório**: `~/aval`
- **Comando**: `foremost-ng -t evtx,elf,exe -i teste.dd -o ~/aval/saida_tipos; echo "exit=$?"`
- **Esperado segundo os autores**: "only the EVTX, ELF, and EXE modules will run", cada arquivo em subdiretório de formato \[artigo.pdf:p. 7, §4.1\].
- **Evidência**: `saida_tipos/audit.txt`; `ls saida_tipos`.
- **Sucesso**: apenas os subdiretórios `evtx`, `elf` e, se houver, `exe` contêm arquivos.
- **Falha**: arquivos de outros tipos (por exemplo, `script` ou `macho`) aparecem.
- **Interrupção**: nenhuma; registre e siga.

## C1 — Recuperação de EVTX (P18–P19)

C1 é reproduzida se P18 e P19 tiverem sucesso: um `.evtx` recuperado no offset esperado e lido sem erro por uma ferramenta de eventos \[reivindicacoes.md:C1\]. Se P14 não obteve um `.evtx`, C1 fica "não verificada".

### P18 — Localizar e comparar o EVTX recuperado \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: R / C1.
- **Diretório**: `~/aval`
- **Comando**: `grep evtx evidencias/P15_offsets.txt; grep -i evtx saida_todos/audit.txt saida_tipos/audit.txt; ls -l saida_todos/evtx saida_tipos/evtx; stat -c %s amostras/evtx_app.evtx; cmp amostras/evtx_app.evtx saida_todos/evtx/<nome esperado>.evtx && echo IDENTICO`
- **Esperado segundo os autores**: o parser reconhece a assinatura "ElfFile", lê o número de chunks de 64 KiB e recorta até o próximo cabeçalho EVTX ou até o total de chunks \[artigo.pdf:p. 6, §3\].
- **Evidência**: saída dos comandos; tamanho do original e do recuperado.
- **Sucesso**: `<nome esperado>.evtx` (da coluna 3 de `P15_offsets.txt`) presente em `saida_todos/evtx` e em `saida_tipos/evtx`.
- **Falha**: nenhum `.evtx` recuperado, ou recuperado em offset diferente.
- **Interrupção**: falha, C1 não reproduzida; pule P19. Tamanho diferente do original não é falha aqui: registre a diferença e siga para P19.

### P19 — Ler o EVTX com ferramenta de eventos \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C1.
- **Justificativa**: o artigo afirma que o arquivo "can then be parsed with standard event log tools" (p. 6), mas não indica nenhuma; sem uma ferramenta, o resultado esperado de C1 não pode ser observado.
- **Diretório**: `~/aval`
- **Comando**:

```
sudo apt-get install -y python3-venv
python3 -m venv ~/aval/venv && ~/aval/venv/bin/pip install python-evtx
~/aval/venv/bin/evtx_dump.py amostras/evtx_app.evtx > evidencias/P19_original.xml
~/aval/venv/bin/evtx_dump.py saida_todos/evtx/<nome esperado>.evtx > evidencias/P19_recuperado.xml; echo "exit=$?"
grep -c '<Event ' evidencias/P19_original.xml evidencias/P19_recuperado.xml
```

- Se o executável tiver outro nome, confira com `ls ~/aval/venv/bin`.
- **Esperado segundo os autores**: arquivo legível por ferramenta padrão \[artigo.pdf:p. 6\].
- **Evidência**: os dois XML, o código de saída e as contagens de eventos.
- **Sucesso**: o recuperado é lido sem exceção e lista eventos. Contagem igual à do original reforça o resultado.
- **Falha**: exceção ou erro de leitura no arquivo recuperado, com o original sendo lido normalmente.
- **Interrupção**: se nem o original for lido, a ferramenta é o problema; troque de leitor e registre a troca.

## C2 — Recuperação de scripts (P20–P21)

C2 é reproduzida se P20 e P21 tiverem sucesso: os três scripts recuperados com a linha do interpretador e o corpo, e as duas amostras negativas descartadas, como descreve o artigo (p. 6).

### P20 — Conferir os scripts Bash, Python e PowerShell \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: R / C2.
- **Diretório**: `~/aval`
- **Comando**:

```
ls -l saida_todos/script
while read f off nome h; do
  case "$f" in amostras/s_*)
    alvo=saida_todos/script/$nome.script
    echo "== $f -> $alvo"; head -1 "$alvo"; cmp "$f" "$alvo" && echo IDENTICO;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P20_scripts.txt
```

- **Esperado segundo os autores**: script reconhecido pelo shebang (`#!`) e extraído inteiro, "complete with interpreter directives" \[artigo.pdf:p. 6, §3\].
- **Evidência**: `evidencias/P20_scripts.txt`; `grep script saida_todos/audit.txt`.
- **Sucesso**: os três arquivos existem, a primeira linha é o shebang de cada um e `cmp` imprime `IDENTICO` para os três.
- **Falha**: algum script ausente, truncado ou sem a linha do interpretador.
- **Interrupção**: nenhuma; siga para P21.

### P21 — Conferir o descarte das amostras negativas \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: R / C2.
- **Diretório**: `~/aval`
- **Comando**:

```
while read f off nome h; do
  case "$f" in amostras/neg_*)
    if [ -e saida_todos/script/$nome.script ]; then echo "$f RECUPERADO"; else echo "$f descartado"; fi;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P21_negativos.txt
```

- **Esperado segundo os autores**: o parser garante "the file is at least 32 bytes long and contains more than comments" \[artigo.pdf:p. 6, §3\].
- **Evidência**: `evidencias/P21_negativos.txt`.
- **Sucesso**: `neg_curto.sh` (13 bytes) e `neg_comentario.sh` (só comentários) aparecem como "descartado".
- **Falha**: qualquer um aparece como "RECUPERADO".
- **Interrupção**: nenhuma.

## C3 — Recuperação de Mach-O fat e thin (P22–P23)

C3 é reproduzida se P22 tiver sucesso para as duas amostras; P23 reforça o reconhecimento com ferramentas do próprio macOS. Se P14 não obteve amostras Mach-O, C3 fica "não verificada".

### P22 — Localizar e reconhecer os Mach-O recuperados \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: R / C3.
- **Diretório**: `~/aval`
- **Comando**:

```
ls -l saida_todos/macho; grep macho saida_todos/audit.txt
while read f off nome h; do
  case "$f" in amostras/macho_*)
    alvo=saida_todos/macho/$nome.macho
    echo "== $f -> $alvo"; file "$alvo"; stat -c %s "$f" "$alvo"; cmp "$f" "$alvo" && echo IDENTICO;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P22_macho.txt
```

- **Esperado segundo os autores**: para fat, o parser lê deslocamento e tamanho de cada arquitetura e calcula a faixa máxima; para thin, lê os comandos de carga; "The complete Mach-O binary, whether fat or thin, is written out" \[artigo.pdf:p. 6, §3\].
- **Evidência**: `evidencias/P22_macho.txt`.
- **Sucesso**: os dois arquivos existem nos nomes esperados; `file` reconhece um como Mach-O universal e o outro como Mach-O da arquitetura extraída.
- **Falha**: algum dos dois ausente, ou `file` não o reconhece como Mach-O.
- **Interrupção**: nenhuma. Tamanho diferente do original é registrado como observação, não como falha.

### P23 — Reconhecer no macOS \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C3.
- **Justificativa**: o resultado esperado de C3 é um binário "reconhecível por ferramenta apropriada" \[reivindicacoes.md:C3\]; os autores não indicam qual. `lipo` e `otool` leem a estrutura interna, o que `file` não faz.
- **Diretório**: pasta do macOS para onde os dois arquivos recuperados forem copiados.
- **Comando**: `lipo -info <arquivo fat recuperado>; otool -h <arquivo thin recuperado>`
- **Esperado segundo os autores**: não informado.
- **Evidência**: saída dos dois comandos.
- **Sucesso**: `lipo` lista as mesmas arquiteturas do original; `otool -h` imprime o cabeçalho sem erro.
- **Falha**: erro de formato em qualquer um.
- **Interrupção**: sem acesso a macOS, pule; C3 se decide só por P22.

## C4 — Recuperação de ELF 32 e 64 bits (P24)

C4 é reproduzida se P24 tiver sucesso para as duas amostras, nas duas execuções (P16 e P17).

### P24 — Localizar e analisar os ELF recuperados \[CONFERÊNCIA NÃO DOCUMENTADA\]

- **Selo / reivindicação**: R / C4.
- **Diretório**: `~/aval`
- **Comando**:

```
ls -l saida_todos/elf saida_tipos/elf
while read f off nome h; do
  case "$f" in amostras/elf*)
    for d in saida_todos saida_tipos; do
      alvo=$d/elf/$nome.elf
      echo "== $f -> $alvo"; file "$alvo"
      readelf -h -l "$alvo" 2>&1 | grep -iE 'error|warning' || echo "readelf -h -l sem erros"
      readelf -S "$alvo" 2>&1 | grep -iE 'error|warning' | head -3
      stat -c %s "$f" "$alvo"
      cmp -n $(stat -c %s "$alvo") "$f" "$alvo" && echo PREFIXO_IDENTICO
    done;;
  esac
done < evidencias/P15_offsets.txt | tee evidencias/P24_elf.txt
```

- **Esperado segundo os autores**: o parser verifica a assinatura ELF, identifica 32 ou 64 bits, lê a tabela de cabeçalhos de programa e extrai a união dos segmentos carregáveis; o arquivo "retains the correct executable layout and symbol information" \[artigo.pdf:p. 6, §3\].
- **Evidência**: `evidencias/P24_elf.txt`.
- **Sucesso**: os dois arquivos existem nos nomes esperados, nas duas saídas; `file` os identifica como ELF 32-bit e ELF 64-bit; `readelf -h -l` não aponta erros.
- **Falha**: algum arquivo ausente, ou erro na leitura do cabeçalho ELF ou dos cabeçalhos de programa.
- **Interrupção**: nenhuma. Avisos de `readelf -S` (tabela de seções fora do arquivo) não reprovam C4, cujo critério é ser "estruturalmente legível" \[reivindicacoes.md:C4\]; registre-os como divergência da frase do artigo sobre "symbol information".

## C5 — Enriquecimento pelo VirusTotal (P25–P28)

C5 é reproduzida se P25 mostrar carving com aviso sem chave e se P26 com P27 (ou P28) mostrarem, para ao menos um arquivo conhecido pelo VirusTotal, um rótulo coerente com a consulta manual pelo SHA-256 desse arquivo. As contagens não precisam coincidir com as do artigo \[reivindicacoes.md:Critério de reprodução\]. Use `-t elf` para limitar as consultas a dois arquivos: a cota da API pública é pequena, e o código não espaça as requisições.

### P25 — Executar sem chave e com chave inválida

- **Selo / reivindicação**: R / C5.
- **Diretório**: `~/aval`
- **Comando**:

```
unset VT_API_KEY
foremost-ng -x -t elf -i teste.dd -o ~/aval/saida_vt_semchave 2>&1 | tee evidencias/P25_semchave.txt
VT_API_KEY=chave_invalida foremost-ng -x -t elf -i teste.dd -o ~/aval/saida_vt_invalida 2>&1 | tee evidencias/P25_invalida.txt
cat saida_vt_semchave/audit.txt saida_vt_invalida/audit.txt
```

- **Esperado segundo os autores**: "If the API key is missing or invalid, Foremost-NG will still perform carving but will emit a warning and skip all VT lookups" \[artigo.pdf:p. 7, §4.1\].
- **Evidência**: os dois logs e os dois `audit.txt`.
- **Sucesso**: nos dois casos, os mesmos ELF de P17 são recuperados e um aviso aparece no terminal.
- **Falha**: carving interrompido, ou nenhum aviso em algum dos casos.
- **Interrupção**: nenhuma. Registre o que a coluna VT mostra; um veredito como "Clean (0)" para consulta que não ocorreu é divergência a relatar.

### P26 — Executar com chave válida

- **Selo / reivindicação**: R / C5.
- **Diretório**: `~/aval`
- **Comando**:

```
export VT_API_KEY=<SUA_CHAVE>
foremost-ng -x -t elf -i teste.dd -o ~/aval/saida_vt 2>&1 | tee evidencias/P26_vt.txt
cat saida_vt/audit.txt; ls saida_vt
```

- **Esperado segundo os autores**: o programa calcula o hash de cada ELF recuperado, consulta a API e anota em `audit.txt` as contagens de detecções maliciosas e não detectadas \[artigo.pdf:p. 7, §4.1\]; o veredito traz "malicious count, undetected count, and a clean/malicious flag" \[artigo.pdf:p. 3\]; a saída inclui um `recovery.log` com offsets, hashes e dados do VirusTotal \[artigo.pdf:p. 7, §4.2\]. A chave segue \[README.md:97–101\].
- **Evidência**: log, `audit.txt`, listagem de `saida_vt`. Não salve a chave em nenhuma evidência.
- **Sucesso**: cada ELF tem na coluna VT um rótulo `Clean (n)` ou `Malicious (n)`, sem mensagens de erro de rede.
- **Falha**: coluna VT vazia ou `N/A`, ou erro de `curl`.
- **Interrupção**: erro de cota, espere alguns minutos e repita com novo diretório de saída. Ausência de `recovery.log` ou de uma das duas contagens é divergência a registrar, não falha.

### P27 — Conferir a consulta pelo hash \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C5.
- **Justificativa**: `audit.txt` não registra o hash do arquivo, e o `recovery.log` prometido pode não existir; sem recalcular o hash, não há como confirmar que a consulta corresponde ao arquivo recuperado.
- **Diretório**: `~/aval`
- **Comando**:

```
for a in saida_vt/elf/*.elf; do
  h=$(sha256sum "$a" | cut -d' ' -f1); echo "== $a $h"
  curl -s -H "x-apikey: $VT_API_KEY" https://www.virustotal.com/api/v3/files/$h | jq -c '.data.attributes.last_analysis_stats // .error'
  sleep 20
done | tee evidencias/P27_vt_manual.txt
```

- **Esperado segundo os autores**: não informado.
- **Evidência**: `evidencias/P27_vt_manual.txt`.
- **Sucesso**: para cada arquivo conhecido pelo VirusTotal, o rótulo de P26 é coerente com as contagens manuais (`Malicious` se `malicious` > 0, e o número exibido igual ao campo correspondente).
- **Falha**: rótulo incoerente com a consulta manual.
- **Interrupção**: se a API responder `NotFoundError` para todos os hashes, não há resultado de detecção a comparar; vá para P28.

### P28 — Tornar um hash conhecido \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C5.
- **Justificativa**: arquivos recuperados por carving podem não coincidir byte a byte com os originais e, por isso, não ter análise no VirusTotal; sem uma análise existente, C5 não tem resultado de detecção para registrar.
- **Diretório**: navegador; depois `~/aval`.
- **Comando**: envie o ELF de 64 bits recuperado em P26 pela interface web do VirusTotal e aguarde a análise; então repita P26 com `-o ~/aval/saida_vt2` e P27 sobre `saida_vt2/elf`.
- **Esperado segundo os autores**: não informado.
- **Evidência**: link da análise no VirusTotal; logs da repetição.
- **Sucesso**: o rótulo da repetição é coerente com a consulta manual.
- **Falha**: rótulo incoerente.
- **Interrupção**: envie apenas arquivo seu e sem conteúdo sigiloso, pois o envio o torna disponível a terceiros. Se não puder enviar, classifique C5 como "parcialmente verificada" e justifique no parecer.

## C6 — Execução da Figura 2 (P29–P32)

C6 é reproduzida se P31 recuperar os 12 arquivos da Fig. 2 com os mesmos nomes e offsets; contagens do VirusTotal podem diferir \[reivindicacoes.md:Critério de reprodução\]. Sem `evidence2.dd`, C6 é "não reproduzível" e o bloco termina em P29.

### P29 — Obter `evidence2.dd` \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C6.
- **Justificativa**: a imagem não está no artefato \[artefato.txt:índice\] e nem o README nem o artigo dizem como obtê-la; sem ela, a Fig. 2 não pode ser confrontada.
- **Diretório**: —
- **Comando**: pedir aos autores, pelo canal do comitê, a imagem `evidence2.dd` usada na Fig. 2 e sua origem.
- **Esperado segundo os autores**: não informado.
- **Evidência**: data do pedido e resposta dos autores.
- **Sucesso**: imagem recebida.
- **Falha**: imagem indisponível.
- **Interrupção**: falha, classifique C6 como não reproduzível e pule P30–P32. Pela regra de reivindicacoes.md, R não é atribuído.

### P30 — Conferir a imagem recebida \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: R / C6.
- **Justificativa**: garante que a imagem é a da Fig. 2, cujo único identificador publicado é o tamanho.
- **Diretório**: `~/aval/foremost-ng/src`
- **Comando**: `stat -c %s evidence2.dd; sha256sum evidence2.dd > ~/aval/evidencias/P30_evidence2.txt`
- **Esperado segundo os autores**: "Length: 2 GB (2845109643 bytes)" \[artigo.pdf:p. 8, Fig. 2\].
- **Evidência**: tamanho e SHA-256.
- **Sucesso**: 2845109643 bytes.
- **Falha**: outro tamanho.
- **Interrupção**: tamanho diferente, peça esclarecimento aos autores antes de seguir.

### P31 — Repetir a execução da Fig. 2

- **Selo / reivindicação**: R / C6 (e C5).
- **Diretório**: `~/aval/foremost-ng/src` (a Fig. 2 mostra o binário local, a configuração `src/foremost.conf` e a saída em `src/output`).
- **Comando**: confirme que `output` não existe (`ls output`) e rode `export VT_API_KEY=<SUA_CHAVE>; ./foremost-ng -v -x evidence2.dd 2>&1 | tee ~/aval/evidencias/P31_fig2.txt`
- **Esperado segundo os autores**: a saída da Fig. 2 \[artigo.pdf:p. 8\], com cabeçalho "foremost-ng version 1.5.7" e a tabela abaixo.
- **Evidência**: `P31_fig2.txt`; cópia de `output/audit.txt`; `find output -type f | sort`.
- **Sucesso**: execução conclui e imprime a tabela de arquivos.
- **Falha**: erro ou nenhuma tabela.
- **Interrupção**: não execute os arquivos recuperados (linhas 4 e 9 são marcadas como maliciosas). Erro de cota do VirusTotal: repita depois com `output` removido.

### P32 — Comparar com a Fig. 2

- **Selo / reivindicação**: R / C6.
- **Diretório**: `~/aval/foremost-ng/src`
- **Comando**: compare cada linha de `output/audit.txt` com a tabela abaixo; salve a comparação em `~/aval/evidencias/P32_comparacao.txt`.
- **Esperado segundo os autores**: a tabela transcrita da Fig. 2. Confira a transcrição contra o PDF antes de comparar: a figura tem baixa resolução.

| ID | Arquivo | Tamanho | Offset | Comentário | VT |
| --- | --- | --- | --- | --- | --- |
| 0 | 00004352.elf | 57 KB | 2228224 | — | Clean (0) |
| 1 | 00004820.elf | 57 KB | 2467840 | — | Clean (0) |
| 2 | 00005108.elf | 1 KB | 2615296 | — | Clean (0) |
| 3 | 00005492.script | 3 KB | 2811904 | — | Clean (0) |
| 4 | 00399884.exe | 600 KB | 204740608 | 01/01/1970 00:00:00 | Malicious (2) |
| 5 | 00405060.exe | 52 KB | 207390720 | 01/01/1970 00:00:00 | Clean (0) |
| 6 | 00414932.exe | 2 MB | 212445184 | 01/01/2015 00:00:00 | Clean (0) |
| 7 | 00428728.exe | 2 MB | 219508736 | 01/01/2015 00:00:00 | Clean (0) |
| 8 | 00442520.exe | 536 KB | 226570240 | 01/01/1970 00:00:00 | Clean (0) |
| 9 | 00447356.exe | 600 KB | 229046272 | 01/01/1970 00:00:00 | Malicious (2) |
| 10 | 01786101.zip | 470 KB | 914484119 | — | Clean (0) |
| 11 | 01787042.zip | 350 KB | 914965615 | — | Clean (0) |

- **Evidência**: `P32_comparacao.txt`, linha a linha: igual, diferente ou ausente.
- **Sucesso**: as 12 linhas presentes, com mesmo nome e mesmo offset; tamanhos compatíveis.
- **Falha**: alguma linha ausente ou com offset diferente.
- **Interrupção**: nenhuma. Linhas a mais e contagens diferentes do VirusTotal são registradas, não reprovam C6. Nos nomes, o número de 8 dígitos é o offset dividido por 512 (bs=512 na figura), o que serve de checagem interna.

## C7 — Arquitetura extensível (P33, fora da regra de R)

C7 não entra na decisão de R \[reivindicacoes.md:Regra para o selo R\]; o passo abaixo apenas registra se o código corresponde à descrição do artigo.

### P33 — Inspecionar despachante e registro de parsers \[NÃO DOCUMENTADO\]

- **Selo / reivindicação**: — / C7.
- **Justificativa**: o artigo não associa experimento a C7; a única verificação possível é a leitura do código.
- **Diretório**: `~/aval/foremost-ng/src`
- **Comando**: `grep -n 'needle->type ==' extract.c > ~/aval/evidencias/P33_despachante.txt; grep -n 'init_builtin(.*\(ELF\|MACHO\|EVTX\|SCRIPT\)' state.c >> ~/aval/evidencias/P33_despachante.txt; grep -n 'define \(ELF\|MACHO\|EVTX\|SCRIPT\)' main.h >> ~/aval/evidencias/P33_despachante.txt`
- **Esperado segundo os autores**: parsers com identificador, assinatura, validação e recuperação, registrados numa lista; adicionar ou remover um parser "does not require modifying the dispatcher logic itself" \[artigo.pdf:p. 3, §2\].
- **Evidência**: `P33_despachante.txt`.
- **Sucesso**: um novo formato exige só o parser e a entrada no registro.
- **Falha**: um novo formato exige também editar o despachante `extract_file` (cadeia de `if/else` por tipo).
- **Interrupção**: nenhuma.

## Tempo estimado

O roteiro completo leva de 4 h 30 min a 7 h de trabalho ativo, sem contar a espera pela resposta dos autores em P29. Os autores não informam tempos; os valores abaixo são estimativas do revisor \[NÃO DOCUMENTADO\] e variam com a velocidade de disco, a rede e a cota do VirusTotal.

| Fase | Passos | Tempo estimado |
| --- | --- | --- |
| Ambiente, compilação e instalação | P1–P8 | 30–45 min |
| Teste mínimo (F) | P9–P13 | 15–20 min |
| Amostras e imagem de teste | P14–P17 | 45–90 min (depende de acesso a Windows e macOS) |
| C1–C4 | P18–P24 | 45–60 min |
| C5 | P25–P28 | 30–60 min, mais a espera da análise em P28 |
| C6 | P29–P32 | espera pelos autores; depois 30–60 min (imagem de 2,8 GB e 12 consultas ao VirusTotal) |
| C7 | P33 | 10 min |
| Redação do parecer | — | 60 min |

## Tabela de todos os passos

Dos 33 passos, 13 seguem procedimento dos autores, 6 conferem resultados descritos pelos autores com ferramentas do revisor ("Parcial") e 14 são \[NÃO DOCUMENTADO\]; a decisão de R depende de C1–C6, e a de F, de P7, P8, P12 e P13.

| Passo | Selo | Reiv. | Documentado? | O que faz | Interrompe se |
| --- | --- | --- | --- | --- | --- |
| P1 | F, R | todas | Não | Cria VM e grava a sessão | sem rede |
| P2 | F | — | Sim (Dockerfile:3–5) | Instala `gcc make git libssl-dev libcurl4-openssl-dev` | pacote indisponível |
| P3 | F | — | Não | Registra versões | — |
| P4 | F | — | Sim (artigo p. 6) | `git clone` | sem repositório nem zip |
| P5 | F, R | todas | Não | Fixa o commit `bb812a22` | commit ausente |
| P6 | F | — | Sim (artigo p. 6) | `make` na raiz | — (registra divergência) |
| P7 | F | — | Sim (README:28–33) | `make` em `src` | falha de compilação |
| P8 | F | — | Sim (README:34) | `sudo make install` | falha de instalação |
| P9 | F | — | Sim (README:79) | `man foremost-ng` | — |
| P10 | F | — | Não | `foremost-ng -h` | falha de segmentação |
| P11 | F | — | Não | Monta `min.dd` com um script | — |
| P12 | F | — | Sim (artigo p. 7) | `foremost-ng -i min.dd -o …` | sem saída |
| P13 | F | C2 | Parcial (artigo p. 7) | Confere `audit.txt` e o script | nada recuperado |
| P14 | R | C1–C4 | Não | Reúne amostras | amostra ausente invalida só a reivindicação dela |
| P15 | R | C1–C5 | Não | Monta `teste.dd` com offsets conhecidos | erro de montagem |
| P16 | R | C1–C4 | Sim (artigo p. 7) | Carving padrão | sem saída |
| P17 | R | C1, C4 | Sim (artigo p. 7) | `-t evtx,elf,exe` | — |
| P18 | R | C1 | Parcial (artigo p. 6) | Localiza e compara o `.evtx` | nada recuperado |
| P19 | R | C1 | Não | Lê o `.evtx` com `python-evtx` | leitor falha no original |
| P20 | R | C2 | Parcial (artigo p. 6) | Confere três scripts | — |
| P21 | R | C2 | Parcial (artigo p. 6) | Confere descarte dos negativos | — |
| P22 | R | C3 | Parcial (artigo p. 6) | Localiza e reconhece Mach-O | — |
| P23 | R | C3 | Não | `lipo`/`otool` no macOS | sem macOS: pular |
| P24 | R | C4 | Parcial (artigo p. 6) | `readelf` nos ELF 32 e 64 | — |
| P25 | R | C5 | Sim (artigo p. 7) | `-x` sem chave e com chave inválida | — |
| P26 | R | C5 | Sim (README:97–101; artigo p. 7) | `-x` com chave válida | erro de cota: repetir |
| P27 | R | C5 | Não | Consulta manual pelo SHA-256 | todos `NotFoundError`: P28 |
| P28 | R | C5 | Não | Envia um ELF recuperado ao VirusTotal | sem envio: C5 parcial |
| P29 | R | C6 | Não | Pede `evidence2.dd` aos autores | sem imagem: C6 não reproduzível |
| P30 | R | C6 | Não | Confere 2845109643 bytes | tamanho diferente |
| P31 | R | C6 | Sim (artigo p. 8, Fig. 2) | `./foremost-ng -v -x evidence2.dd` | erro de execução |
| P32 | R | C6 | Sim (artigo p. 8, Fig. 2) | Compara as 12 linhas | — |
| P33 | — | C7 | Não | Inspeciona o despachante | — |
