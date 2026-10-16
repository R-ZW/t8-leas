# Roteiro de execução — Foremost-NG (SBSeg 2025, selos F e R)

Oct 15, 2026 · @edu

## Escopo e convenções

Este roteiro leva o revisor a executar o Foremost-NG no commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` e a coletar a prova de execução exigida para F e a comparação com o artigo exigida para R. Nada aqui foi executado; os resultados esperados vêm dos autores ou, quando eles não dizem nada, do próprio código, e isso é indicado em cada caso.

**Procedimentos dos autores usados como base** (todos os outros passos são marcados \[NÃO DOCUMENTADO\]):

- **README.md**: instalação Linux `cd …/src`, `make`, `sudo make install` \[README.md:26–35\]; uso `man foremost-ng` e `foremost-ng [options] [image_or_device]` \[README.md:79–84\]; chave VT `export VT_API_KEY=yourkey` \[README.md:95–101\].
- **Dockerfile**: base `ubuntu:latest`, dependências `gcc make git libssl-dev libcurl4-openssl-dev`, `make && make install` em `src` \[Dockerfile:1–10\].
- **Artigo §4**: `git clone …; cd foremost-ng; make; sudo make install` (p. 6); exemplos `-i … -o …`, `-t evtx,elf,exe`, `-x -t elf` (p. 7, §4.1); estrutura de saída (p. 7, §4.2); Fig. 2 com `./foremost-ng -v -x evidence2.dd` (p. 8).
- **Amostras**: o artigo só diz "Carving test samples can be downloaded from https://dftt.sourceforge.net" (p. 7), sem indicar qual imagem.

**Convenções**

- Cada passo traz: selo e reivindicação, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, de falha e de interrupção.
- **Falha** registra um resultado negativo e o roteiro segue. **Interrupção** para o bloco (ou o roteiro), porque continuar não produziria evidência válida.
- Diretórios fixos: `/aval/foremost-ng` (código), `/aval/amostras` (entradas), `/aval/saidas/Pn` (saídas, uma pasta nova por execução), `/aval/evid` (evidências). O programa recusa diretório de saída não vazio \[src/dir.c:124\] "not empty", por isso cada execução usa um `-o` novo.
- O arquivo de configuração é procurado no diretório corrente e depois em `/usr/local/etc/foremost.conf` \[src/config.c:218–228\]; sem ele o programa encerra. Após `make install` (P9) isso está resolvido.
- Nunca salve a chave do VirusTotal nas evidências; substitua-a por `***` nos logs.

## Requisitos do ambiente

Os autores não declaram hardware nem versões; o ambiente abaixo segue o Dockerfile e acrescenta, marcado, o que os testes exigem. Registre tudo em P1 e P3, porque a ausência de versões é uma das lacunas de F.

**Hardware** \[NÃO DOCUMENTADO\]

| Recurso | Mínimo sugerido | Motivo |
| --- | --- | --- |
| CPU | x86\_64, 2 vCPU | `gcc -m32` (ELF32, P13) exige multilib, disponível em amd64 |
| RAM | 4 GB | margem para o buffer de leitura (padrão `CHUNK_SIZE 100` \[src/main.h:230\]) e o compilador |
| Disco | 10 GB livres com C6; 3 GB sem C6 | a imagem da Fig. 2 tem 2845109643 bytes (Fig. 2, linha "Length") mais a saída |
| Rede | acesso a github.com, repositório apt do Ubuntu, www.virustotal.com, dftt.sourceforge.net, PyPI | clone, dependências, C5, C6, leitor EVTX |
| Hosts auxiliares | um Windows (C1) e um macOS (C3), ou amostras equivalentes | o artefato não traz amostras EVTX nem Mach-O |

**Software**

| Item | Fonte | Observação |
| --- | --- | --- |
| Docker | \[NÃO DOCUMENTADO\] como modo de uso; o Dockerfile existe | o README não menciona o Dockerfile |
| `ubuntu:latest` | Dockerfile:1 | imagem flutuante: registre a versão real em P2 |
| gcc, make, git, libssl-dev, libcurl4-openssl-dev | Dockerfile:5 | ausentes do README para Linux |
| `file`, `curl`, `binutils` (`readelf`) | \[NÃO DOCUMENTADO\] | conferir tipo de arquivo (C3), oráculo VT (C5), estrutura ELF (C4) |
| `gcc-multilib` | \[NÃO DOCUMENTADO\] | gerar ELF32 para C4 |
| `python3-venv` + `python-evtx` | \[NÃO DOCUMENTADO\] | "ferramenta de análise de eventos" exigida por C1 |
| Conta e chave VirusTotal | README:95–97 | necessária para C5 e C6 |
| `lipo`, `otool` (macOS) | \[NÃO DOCUMENTADO\] | preparar e validar Mach-O fat e thin (C3) |

## Preparação (P1–P9)

Esta fase põe o código exato do commit avaliado num ambiente registrado e o compila pelos dois caminhos documentados. Os passos P7 e P8 são ambos procedimentos dos autores e divergem entre si; execute os dois.

### P1 — Registrar o host \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F (registro de ambiente).
- **Por que é necessário:** os autores não declaram ambiente; o parecer precisa dizer onde a execução ocorreu.
- **Diretório:** qualquer, no host.
- **Comando:**

```
mkdir -p $HOME/aval/evid && cd $HOME/aval
{ date -u; uname -a; nproc; free -h; df -h .; docker --version; } | tee evid/P1_host.txt
```

- **Esperado segundo os autores:** nada declarado.
- **Evidência:** `evid/P1_host.txt`.
- **Sucesso:** arquivo gerado com recursos ≥ requisitos.
- **Falha:** recursos abaixo do sugerido (registre e prossiga).
- **Interrupção:** Docker ausente e sem alternativa Linux equivalente.

### P2 — Subir o contêiner base do Dockerfile

- **Selo / reivindicação:** F.
- **Base:** Dockerfile:1 "FROM ubuntu:latest". Rodar interativo com volume montado é \[NÃO DOCUMENTADO\], necessário para fixar o commit (P5), o que o Dockerfile não faz \[Dockerfile:8 clona o HEAD\].
- **Diretório:** `$HOME/aval` no host.
- **Comando:**

```
docker pull ubuntu:latest
docker image inspect ubuntu:latest --format '{{.Id}} {{.Created}}' | tee evid/P2_imagem.txt
docker run -it --name fng-aval -v $HOME/aval:/aval ubuntu:latest bash
# dentro do contêiner:
cat /etc/os-release | tee -a /aval/evid/P2_imagem.txt
```

- **Esperado segundo os autores:** imagem Ubuntu (versão não declarada).
- **Evidência:** `evid/P2_imagem.txt` (ID da imagem, versão do Ubuntu).
- **Sucesso:** shell no contêiner com `/aval` montado.
- **Falha:** —.
- **Interrupção:** contêiner não sobe.

### P3 — Instalar dependências

- **Selo / reivindicação:** F.
- **Base:** Dockerfile:3–6. A segunda linha de pacotes e o registro de versões são \[NÃO DOCUMENTADO\]: servem aos testes de R (P13–P24) e à lacuna de versões de F.
- **Diretório:** `/aval` (contêiner).
- **Comando:**

```
apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  gcc make git libssl-dev libcurl4-openssl-dev 2>&1 | tee /aval/evid/P3_apt.log
DEBIAN_FRONTEND=noninteractive apt-get install -y file curl binutils \
  gcc-multilib python3-venv 2>&1 | tee -a /aval/evid/P3_apt.log
{ gcc --version | head -1; make --version | head -1; git --version;
  dpkg -l libssl-dev libcurl4-openssl-dev | tail -2; } | tee /aval/evid/P3_versoes.txt
```

- **Esperado segundo os autores:** pacotes instalados (sem versões declaradas).
- **Evidência:** `P3_apt.log`, `P3_versoes.txt`.
- **Sucesso:** a primeira instalação termina com código 0.
- **Falha:** algum pacote da segunda linha indisponível (registre; afeta só o teste que o usa).
- **Interrupção:** falha na primeira linha (dependências de compilação).

### P4 — Clonar o repositório

- **Selo / reivindicação:** F.
- **Base:** artigo p. 6 "git clone https://github.com/cristianzsh/foremost-ng.git"; Dockerfile:8. O README pede um tarball inexistente no artefato \[README.md:27\]; use o clone.
- **Diretório:** `/aval`.
- **Comando:**

```
cd /aval && git clone https://github.com/cristianzsh/foremost-ng.git 2>&1 | tee evid/P4_clone.log
```

- **Esperado segundo os autores:** repositório clonado.
- **Evidência:** `P4_clone.log`.
- **Sucesso:** diretório `/aval/foremost-ng` criado.
- **Falha:** —.
- **Interrupção:** repositório indisponível. Alternativa: usar o `artefato.zip` do comitê, se houver, conferindo o SHA-256 `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a` e pulando para P6.

### P5 — Fixar o commit avaliado \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R.
- **Por que é necessário:** artigo e Dockerfile usam o HEAD, que pode diferir da versão submetida.
- **Diretório:** `/aval/foremost-ng`.
- **Comando:**

```
cd /aval/foremost-ng
git checkout bb812a22cb06ef87b5a2d877dfb6f40eb12d460d
git rev-parse HEAD | tee /aval/evid/P5_commit.txt
```

- **Esperado segundo os autores:** não aplicável.
- **Evidência:** `P5_commit.txt`.
- **Sucesso:** saída igual a `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`.
- **Falha:** —.
- **Interrupção:** commit inexistente no repositório (use o ZIP do comitê ou pare).

### P6 — Conferir integridade contra o índice do artefato \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R.
- **Por que é necessário:** garante que o código executado é o mesmo de `artefato.txt`.
- **Diretório:** `/aval/foremost-ng`.
- **Comando:**

```
cd /aval/foremost-ng
sha256sum README.md Dockerfile src/Makefile src/main.c src/dir.c \
  src/extract.c src/state.c src/vt_query.c | tee /aval/evid/P6_sha256.txt
```

- **Esperado (índice de `artefato.txt`):** README.md `ff3414f0…`; Dockerfile `a8848d0c…`; src/Makefile `ce9da14a…`; src/main.c `966bffda…`; src/dir.c `ae64b63a…`; src/extract.c `4f81160c…`; src/state.c `8bbf0ec5…`; src/vt\_query.c `d20bf972…`.
- **Evidência:** `P6_sha256.txt`.
- **Sucesso:** todos os prefixos coincidem.
- **Falha:** —.
- **Interrupção:** qualquer divergência (o código não é o avaliado).

### P7 — Compilar pelo procedimento do artigo

- **Selo / reivindicação:** F (critério de instalação).
- **Base:** artigo p. 6 "cd foremost-ng / make".
- **Diretório:** `/aval/foremost-ng` (raiz).
- **Comando:**

```
cd /aval/foremost-ng && make 2>&1 | tee /aval/evid/P7_make_raiz.log; echo "rc=${PIPESTATUS[0]}" >> /aval/evid/P7_make_raiz.log
```

- **Esperado segundo os autores:** compilação.
- **Atenção:** o índice do artefato só lista `src/Makefile`, sem Makefile na raiz; registre o que acontecer.
- **Evidência:** `P7_make_raiz.log`.
- **Sucesso:** binário gerado.
- **Falha:** erro do `make` (divergência documental a citar no parecer).
- **Interrupção:** nenhuma; siga para P8.

### P8 — Compilar pelo procedimento do README

- **Selo / reivindicação:** F.
- **Base:** README.md:28 "cd foremost-ng-\<version>/src" e README.md:33 "make"; Dockerfile:9–10.
- **Diretório:** `/aval/foremost-ng/src`.
- **Comando:**

```
cd /aval/foremost-ng/src && make 2>&1 | tee /aval/evid/P8_make.log; echo "rc=${PIPESTATUS[0]}" >> /aval/evid/P8_make.log
ls -l foremost-ng | tee -a /aval/evid/P8_make.log
```

- **Esperado segundo os autores:** binário `foremost-ng` (nome em src/Makefile:7).
- **Evidência:** `P8_make.log` com avisos do compilador.
- **Sucesso:** `rc=0` e binário presente.
- **Falha:** erro de compilação ou ligação.
- **Interrupção:** sem binário, F não pode ser atribuído e R não pode ser testado; pare e registre.

### P9 — Instalar

- **Selo / reivindicação:** F.
- **Base:** README.md:34 "sudo make install"; Dockerfile:10 "make install" (no contêiner, como root, sem `sudo`).
- **Diretório:** `/aval/foremost-ng/src`.
- **Comando:**

```
make install 2>&1 | tee /aval/evid/P9_install.log
ls -l /usr/local/bin/foremost-ng /usr/share/man/man8/foremost-ng.8.gz /usr/local/etc/foremost.conf | tee -a /aval/evid/P9_install.log
```

- **Esperado segundo os autores:** "the foremost-ng binary is available system-wide" (artigo p. 7); destinos em src/Makefile:107–118.
- **Evidência:** `P9_install.log`.
- **Sucesso:** os três arquivos existem.
- **Falha:** algum ausente.
- **Interrupção:** binário ausente em `/usr/local/bin` (use `./foremost-ng` em `src`, onde está `foremost.conf`, e registre).

## Teste mínimo do selo F (P10–P12)

F fica provado se P8 compila e P12 recupera um arquivo conhecido, com saída e `audit.txt` salvos. Os autores não fornecem exemplo mínimo nem dado de entrada; o arquivo de teste de P11 é do revisor e isso deve constar no parecer.

### P10 — Ler a documentação de uso instalada

- **Selo / reivindicação:** F (critério de execução documentada).
- **Base:** README.md:79 "man foremost-ng". O `zcat` e o `-h` são \[NÃO DOCUMENTADO\]: a imagem Ubuntu mínima costuma não ter `man`, e o manual só existe como binário no artefato (não pôde ser lido na análise).
- **Diretório:** `/aval`.
- **Comando:**

```
(man foremost-ng 2>/dev/null || zcat /usr/share/man/man8/foremost-ng.8.gz) > /aval/evid/P10_man.txt
foremost-ng -h 2> /aval/evid/P10_help.txt
```

- **Esperado segundo os autores:** documentação de uso disponível.
- **Evidência:** `P10_man.txt`, `P10_help.txt`.
- **Sucesso:** texto do manual legível; ajuda lista `-i`, `-o`, `-t`, `-x`, `-v`.
- **Falha:** manual vazio ou sem exemplos (registre: afeta o critério "exemplo mínimo").
- **Interrupção:** nenhuma.

### P11 — Criar a entrada mínima \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F.
- **Por que é necessário:** o artefato não inclui imagem de teste e o artigo só aponta o site DFTT, sem imagem específica. Um script conhecido, isolado por zeros, tem resultado verificável byte a byte.
- **Diretório:** `/aval/amostras`.
- **Comando:**

```
mkdir -p /aval/amostras /aval/saidas && cd /aval/amostras
printf '#!/bin/bash\n# teste minimo F\necho "foremost-ng: teste minimo"\nexit 0\n' > min.sh
rm -f min.img && truncate -s 64K min.img && cat min.sh >> min.img && truncate -s %4096 min.img
sha256sum min.sh min.img | tee /aval/evid/P11_entrada.txt
```

- **Esperado:** `min.img` com o script no offset 65536 (bloco 128 de 512 bytes).
- **Evidência:** `P11_entrada.txt`.
- **Sucesso:** arquivos criados.
- **Falha / interrupção:** —.

### P12 — Executar com a sintaxe do artigo

- **Selo / reivindicação:** F; prévia de C2.
- **Base:** artigo p. 7, §4.1 "foremost-ng -i disk.img -o /temp/output/carved".
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -i /aval/amostras/min.img -o /aval/saidas/P12 2>&1 | tee /aval/evid/P12_exec.log
find P12 -type f | sort | tee /aval/evid/P12_arquivos.txt
cp P12/audit.txt /aval/evid/P12_audit.txt
cmp P12/script/00000128.script /aval/amostras/min.sh && echo IGUAL | tee -a /aval/evid/P12_arquivos.txt
```

- **Esperado segundo os autores:** subdiretórios por formato, "each named after the corresponding file format" (p. 7); `audit.txt` no diretório de saída (p. 6); um `recovery.log` com offsets e hashes (p. 7, §4.2). Nome do arquivo = bloco de 512 bytes, como na Fig. 2 (ex.: `00004352.elf` no offset 2228224).
- **Evidência:** `P12_exec.log`, `P12_arquivos.txt`, `P12_audit.txt`.
- **Sucesso:** `script/00000128.script` existe, `cmp` imprime `IGUAL` e `audit.txt` lista o arquivo com offset 65536.
- **Falha:** arquivo ausente ou diferente. Anote também se `recovery.log` não existir (divergência com o artigo, não falha de F).
- **Interrupção:** falha de segmentação, erro de configuração ou nenhuma saída: F não pode ser atribuído; registre e pare os blocos R.

## Amostras para R (P13–P16) \[NÃO DOCUMENTADO\]

Todos os passos desta seção são \[NÃO DOCUMENTADO\]: os autores não fornecem nem descrevem entradas para C1–C5. Sem elas não há como observar o "resultado esperado" de `reivindicacoes.md`. Cada amostra tem tamanho e hash conhecidos e fica num offset registrado, o que permite comparar a saída byte a byte.

### P13 — Scripts e ELF (no contêiner)

- **Selo / reivindicação:** R — C2, C4.
- **Diretório:** `/aval/amostras`.
- **Comando:**

```
cd /aval/amostras
printf '#!/bin/bash\n# backup\nfor f in /etc/*.conf; do echo "$f"; done\n' > rec.sh
printf '#!/usr/bin/env python3\nimport sys\nprint("recuperado", sys.argv)\n' > rec.py
printf '#!/usr/bin/env pwsh\nGet-ChildItem -Path . | Write-Output\n' > rec.ps1
printf '#!/bin/sh\n# apenas comentario\n# outro comentario\n' > com.sh
printf '#!/bin/sh\nls\n' > curto.sh
printf 'int main(void){return 0;}\n' > h.c
gcc -o elf64.bin h.c && gcc -m32 -o elf32.bin h.c
file elf64.bin elf32.bin | tee /aval/evid/P13_amostras.txt
wc -c rec.sh rec.py rec.ps1 com.sh curto.sh | tee -a /aval/evid/P13_amostras.txt
```

- **Esperado:** `elf64.bin` = ELF 64-bit LSB; `elf32.bin` = ELF 32-bit LSB; `com.sh` com 32 bytes ou mais só de comentários; `curto.sh` com menos de 32 bytes.
- **Evidência:** `P13_amostras.txt`.
- **Sucesso:** todos os arquivos criados.
- **Falha:** `gcc -m32` indisponível (registre; C4 fica restrito a 64 bits e não pode ser dado como reproduzido).
- **Interrupção:** nenhuma.

### P14 — EVTX (host Windows + leitor no contêiner)

- **Selo / reivindicação:** R — C1.
- **Por que é necessário:** C1 exige um `.evtx` real e uma "ferramenta de análise de eventos"; nenhum dos dois é indicado pelos autores.
- **Diretório:** Windows: `C:\aval`; contêiner: `/aval/amostras`.
- **Comando:**

```
:: no Windows, prompt de administrador
mkdir C:\aval
wevtutil epl Application C:\aval\app.evtx
:: copie app.evtx para $HOME/aval/amostras no host do contêiner

# no contêiner
python3 -m venv /aval/venv && /aval/venv/bin/pip install python-evtx 2>&1 | tail -1 | tee /aval/evid/P14_evtx.txt
cd /aval/amostras
head -c 8 app.evtx | od -c | head -1 | tee -a /aval/evid/P14_evtx.txt
/aval/venv/bin/evtx_dump.py app.evtx > /aval/evid/P14_app_original.xml
grep -c '<Event ' /aval/evid/P14_app_original.xml | tee -a /aval/evid/P14_evtx.txt
```

- **Esperado:** cabeçalho começando por `E l f F i l e \0`; número de eventos do original registrado.
- **Evidência:** `P14_evtx.txt`, `P14_app_original.xml`.
- **Sucesso:** o leitor processa o original sem erro.
- **Falha:** —.
- **Interrupção:** sem acesso a Windows nem a outro `.evtx` de origem conhecida: marque C1 como "não verificado" e pule P17.

### P15 — Mach-O fat e thin (host macOS)

- **Selo / reivindicação:** R — C3.
- **Por que é necessário:** C3 exige os dois casos, fat e thin; nenhum vem com o artefato.
- **Diretório:** macOS: `~/aval`.
- **Comando:**

```
mkdir -p ~/aval && cd ~/aval
cp /bin/ls macho_fat.bin
lipo -info macho_fat.bin | tee P15_macho.txt
# use uma arquitetura listada acima, p. ex. x86_64 ou arm64e
lipo -thin x86_64 macho_fat.bin -output macho_thin.bin
file macho_fat.bin macho_thin.bin | tee -a P15_macho.txt
# copie os dois .bin e P15_macho.txt para $HOME/aval/amostras e $HOME/aval/evid
```

- **Esperado:** `lipo -info` diz "Architectures in the fat file"; `file` mostra "Mach-O universal binary" e "Mach-O 64-bit executable".
- **Evidência:** `P15_macho.txt`.
- **Sucesso:** um fat e um thin gerados.
- **Falha:** `/bin/ls` não é fat; escolha outro binário que `lipo -info` declare fat e registre o caminho.
- **Interrupção:** sem macOS nem amostras Mach-O de origem conhecida: marque C3 como "não verificado" e pule P19.

### P16 — Montar a imagem de teste e o gabarito de offsets

- **Selo / reivindicação:** R — C1 a C5.
- **Diretório:** `/aval/amostras`.
- **Comando:**

```
cd /aval/amostras && rm -f teste_r.img offsets.txt
truncate -s 1M teste_r.img
for f in rec.sh rec.py rec.ps1 com.sh curto.sh elf64.bin elf32.bin app.evtx macho_fat.bin macho_thin.bin; do
  [ -f "$f" ] || { echo "AUSENTE $f" >> offsets.txt; continue; }
  off=$(stat -c %s teste_r.img)
  echo "$f off=$off bloco=$((off/512)) tam=$(stat -c %s "$f") sha256=$(sha256sum "$f" | cut -d' ' -f1)" >> offsets.txt
  cat "$f" >> teste_r.img
  truncate -s %4096 teste_r.img
  truncate -s +64K teste_r.img
done
cp offsets.txt /aval/evid/P16_offsets.txt; sha256sum teste_r.img >> /aval/evid/P16_offsets.txt
```

- **Esperado:** cada amostra num offset múltiplo de 4096, separada por 64 KiB de zeros. O nome esperado de cada arquivo recuperado é o valor `bloco` com 8 dígitos (convenção vista na Fig. 2).
- **Evidência:** `P16_offsets.txt` (gabarito de todos os blocos R).
- **Sucesso:** gabarito com uma linha por amostra.
- **Falha:** —.
- **Interrupção:** nenhuma; amostras ausentes já marcam o bloco correspondente como "não verificado".
- **Nota:** binários podem conter assinaturas internas (`MZ`, `#!`, `\x7FELF`) e gerar arquivos extras. Nas comparações, considere só os offsets do gabarito e registre os extras à parte.

## Selo R — um bloco por reivindicação (P17–P28)

Pela regra de `reivindicacoes.md`, R exige C1 a C6 reproduzidas; C7 é só inspecionada. Em todos os blocos, `B` é o número de bloco lido do gabarito de P16, e o arquivo esperado é `<tipo>/<B com 8 dígitos>.<tipo>`. Um bloco interrompido por falta de amostra fica "não verificado", o que basta para R não ser atribuído.

### C1 — EVTX

**P17 — Recuperar e validar o EVTX**

- **Selo / reivindicação:** R — C1.
- **Base:** sintaxe `-t` e `-i/-o` do artigo, p. 7, §4.1. A validação com `python-evtx` e `cmp` é \[NÃO DOCUMENTADO\]; os autores só dizem "standard event log tools".
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -t evtx -i /aval/amostras/teste_r.img -o /aval/saidas/P17 2>&1 | tee /aval/evid/P17_exec.log
cp P17/audit.txt /aval/evid/P17_audit.txt
B=$(awk '$1=="app.evtx"{sub("bloco=","",$3);print $3}' /aval/amostras/offsets.txt)
F=P17/evtx/$(printf %08d $B).evtx
ls -l "$F" /aval/amostras/app.evtx | tee /aval/evid/P17_compar.txt
cmp "$F" /aval/amostras/app.evtx && echo IGUAL >> /aval/evid/P17_compar.txt
/aval/venv/bin/evtx_dump.py "$F" > /aval/evid/P17_carved.xml 2>> /aval/evid/P17_compar.txt
echo "eventos: $(grep -c '<Event ' /aval/evid/P17_carved.xml)" >> /aval/evid/P17_compar.txt
```

- **Esperado segundo os autores:** arquivo identificado por "ElfFile", delimitado pelos chunks de 64 KiB ou pelo próximo cabeçalho; "can then be parsed with standard event log tools" (artigo p. 6).
- **Evidência:** `P17_exec.log`, `P17_audit.txt`, `P17_compar.txt`, `P17_carved.xml`.
- **Sucesso:** arquivo no bloco esperado; o leitor o processa sem erro; número de eventos igual ao de P14.
- **Falha:** arquivo ausente, erro do leitor ou menos eventos que o original. Registre sempre a diferença de tamanho: o código lê a contagem de chunks em `0x18` e trunca ao buffer \[src/extract.c:2479–2490\].
- **Interrupção:** amostra ausente (P14 interrompido).

### C2 — Scripts

**P18 — Recuperar scripts e checar os filtros**

- **Selo / reivindicação:** R — C2.
- **Base:** artigo p. 7, §4.1 (`-t`, `-i`, `-o`); tipo `script` em src/state.c:384.
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -t script -i /aval/amostras/teste_r.img -o /aval/saidas/P18 2>&1 | tee /aval/evid/P18_exec.log
cp P18/audit.txt /aval/evid/P18_audit.txt
for f in rec.sh rec.py rec.ps1 com.sh curto.sh; do
  B=$(awk -v n=$f '$1==n{sub("bloco=","",$3);print $3}' /aval/amostras/offsets.txt)
  F=P18/script/$(printf %08d $B).script
  if [ -f "$F" ]; then cmp -s "$F" /aval/amostras/$f && r=IGUAL || r=DIFERENTE; else r=AUSENTE; fi
  echo "$f $F $r"
done | tee /aval/evid/P18_compar.txt
```

- **Esperado segundo os autores:** script começando por `#!`, "at least 32 bytes long and contains more than comments", extraído "complete with interpreter directives" (artigo p. 6).
- **Evidência:** `P18_exec.log`, `P18_audit.txt`, `P18_compar.txt`.
- **Sucesso:** `rec.sh`, `rec.py`, `rec.ps1` = IGUAL; `com.sh` e `curto.sh` = AUSENTE.
- **Falha:** algum `rec.*` ausente ou diferente, ou `com.sh`/`curto.sh` recuperado. O artigo também menciona "Unicode signatures" (p. 2), não testadas aqui; registre como não coberto.
- **Interrupção:** nenhuma.

### C3 — Mach-O

**P19 — Recuperar Mach-O fat e thin**

- **Selo / reivindicação:** R — C3.
- **Base:** artigo p. 7, §4.1; tipo `macho` em src/state.c:372–379. Validação com `file`, `cmp` e, no macOS, `lipo`/`otool` é \[NÃO DOCUMENTADO\].
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -t macho -i /aval/amostras/teste_r.img -o /aval/saidas/P19 2>&1 | tee /aval/evid/P19_exec.log
cp P19/audit.txt /aval/evid/P19_audit.txt
for f in macho_fat.bin macho_thin.bin; do
  B=$(awk -v n=$f '$1==n{sub("bloco=","",$3);print $3}' /aval/amostras/offsets.txt)
  F=P19/macho/$(printf %08d $B).macho
  if [ -f "$F" ]; then cmp -s "$F" /aval/amostras/$f && r=IGUAL || r=DIFERENTE; file "$F"; else r=AUSENTE; fi
  echo "$f $F $r"
done | tee /aval/evid/P19_compar.txt
# opcional, no macOS: lipo -info <fat recuperado>; otool -h <thin recuperado>
```

- **Esperado segundo os autores:** "The complete Mach-O binary, whether fat or thin, is written out" (artigo p. 6).
- **Evidência:** `P19_exec.log`, `P19_audit.txt`, `P19_compar.txt`.
- **Sucesso:** os dois arquivos no bloco esperado e reconhecidos por `file` como Mach-O universal e Mach-O 64-bit.
- **Falha:** ausente ou não reconhecido. Diferença de tamanho sem perda de reconhecimento é observação, não falha. Fatias internas do fat recuperadas à parte são extras a registrar.
- **Interrupção:** amostras ausentes (P15 interrompido).

### C4 — ELF

**P20 — Recuperar ELF32 e ELF64**

- **Selo / reivindicação:** R — C4.
- **Base:** artigo p. 7, §4.1; tipo `elf` em src/state.c:369. Validação com `readelf` é \[NÃO DOCUMENTADO\].
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -t elf -i /aval/amostras/teste_r.img -o /aval/saidas/P20 2>&1 | tee /aval/evid/P20_exec.log
cp P20/audit.txt /aval/evid/P20_audit.txt
for f in elf64.bin elf32.bin; do
  B=$(awk -v n=$f '$1==n{sub("bloco=","",$3);print $3}' /aval/amostras/offsets.txt)
  F=P20/elf/$(printf %08d $B).elf
  echo "== $f -> $F (original $(stat -c %s /aval/amostras/$f) B, recuperado $(stat -c %s "$F" 2>/dev/null || echo AUSENTE) B)"
  readelf -h -l "$F" 2>&1 | grep -E 'Class|Type|LOAD|Error|Warning'
  readelf -S "$F" 2>&1 | grep -E 'Error|Warning|There are'
done | tee /aval/evid/P20_compar.txt
```

- **Esperado segundo os autores:** detecção de 32/64 bits, extensão pelos segmentos carregáveis; "retains the correct executable layout and symbol information" (artigo p. 6).
- **Evidência:** `P20_exec.log`, `P20_audit.txt`, `P20_compar.txt`.
- **Sucesso:** os dois arquivos no bloco esperado; `readelf -h -l` sem erro, com `Class: ELF32` e `ELF64` corretos.
- **Falha:** ausente, classe errada ou erro no cabeçalho/segmentos. Avisos de `readelf -S` (seções além do fim) não reprovam C4, mas contradizem "symbol information" e devem constar no parecer.
- **Interrupção:** nenhuma; sem `elf32.bin`, C4 fica "não verificado".

**P21 — Invocação combinada do artigo**

- **Selo / reivindicação:** R — C4 (e C1).
- **Base:** artigo p. 7 "foremost-ng -t evtx,elf,exe -i disk.img -o /temp/output/carved".
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
foremost-ng -t evtx,elf,exe -i /aval/amostras/teste_r.img -o /aval/saidas/P21 2>&1 | tee /aval/evid/P21_exec.log
ls P21 | tee /aval/evid/P21_subdirs.txt; cp P21/audit.txt /aval/evid/P21_audit.txt
diff <(ls P20/elf) <(ls P21/elf) && echo ELF_IGUAL_P20 | tee -a /aval/evid/P21_subdirs.txt
```

- **Esperado segundo os autores:** "only the EVTX, ELF, and EXE modules will run", saída em subdiretórios por formato (p. 7).
- **Evidência:** `P21_exec.log`, `P21_subdirs.txt`, `P21_audit.txt`.
- **Sucesso:** só há subdiretórios de evtx, elf e exe com conteúdo; ELF igual a P20.
- **Falha:** outros tipos recuperados ou ELF diferente de P20.
- **Interrupção:** nenhuma.

### C5 — VirusTotal

**P22 — Sem chave e com chave inválida**

- **Selo / reivindicação:** R — C5.
- **Base:** artigo p. 7 "If the API key is missing or invalid, Foremost-NG will still perform carving but will emit a warning and skip all VT lookups."
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
unset VT_API_KEY
foremost-ng -x -t script -i /aval/amostras/min.img -o /aval/saidas/P22a 2>&1 | tee /aval/evid/P22a_semchave.log
VT_API_KEY=chave_invalida foremost-ng -x -t script -i /aval/amostras/min.img -o /aval/saidas/P22b 2>&1 | tee /aval/evid/P22b_invalida.log
cp P22a/audit.txt /aval/evid/P22a_audit.txt; cp P22b/audit.txt /aval/evid/P22b_audit.txt
```

- **Esperado segundo os autores:** carving concluído, aviso emitido, nenhuma consulta.
- **Evidência:** os dois logs e os dois `audit.txt`.
- **Sucesso:** `script/00000128.script` presente nos dois casos e aviso visível.
- **Falha:** carving interrompido ou nenhum aviso. Registre o rótulo da coluna VT: o código usa o resultado zerado \[src/dir.c:280–282\], e um "Clean (0)" sem consulta é divergência a citar.
- **Interrupção:** nenhuma.

**P23 — Com chave válida**

- **Selo / reivindicação:** R — C5.
- **Base:** README.md:95–101 (conta, chave, `export VT_API_KEY`); artigo p. 7 "foremost-ng -x -t elf -i memory.dump -o ./carved-files". Restringir a `script,elf` para limitar consultas é \[NÃO DOCUMENTADO\].
- **Diretório:** `/aval/saidas`.
- **Comando:**

```
cd /aval/saidas
export VT_API_KEY=<sua_chave>
foremost-ng -x -t script,elf -i /aval/amostras/teste_r.img -o /aval/saidas/P23 2>&1 | sed "s/$VT_API_KEY/***/g" | tee /aval/evid/P23_exec.log
cp P23/audit.txt /aval/evid/P23_audit.txt
```

- **Esperado segundo os autores:** hash SHA-256 de cada arquivo, consulta à API e `audit.txt` anotado "with malicious and undetected counts" (p. 7).
- **Evidência:** `P23_exec.log`, `P23_audit.txt`.
- **Sucesso:** cada arquivo recuperado tem rótulo VT na sua linha.
- **Falha:** sem rótulo ou erro de execução.
- **Interrupção:** chave recusada ou cota excedida (verifique em P24, HTTP 401/429): espere, repita e registre.

**P24 — Conferir os rótulos com a API \[NÃO DOCUMENTADO\]**

- **Selo / reivindicação:** R — C5.
- **Por que é necessário:** C5 exige "consulta associada ao hash do arquivo extraído". O `audit.txt` não grava o hash, e hash desconhecido, falha de rede e falta de chave podem gerar o mesmo rótulo. Uma consulta independente é o único gabarito.
- **Diretório:** `/aval/saidas/P23`.
- **Comando:**

```
cd /aval/saidas/P23
for F in $(find . -type f ! -name audit.txt | sort); do
  h=$(sha256sum "$F" | cut -d' ' -f1)
  curl -s -o /aval/evid/P24_vt_$h.json -w "$F $h HTTP=%{http_code}\n" \
    -H "x-apikey: $VT_API_KEY" https://www.virustotal.com/api/v3/files/$h
  grep -o '"last_analysis_stats": *{[^}]*}' /aval/evid/P24_vt_$h.json
done | tee /aval/evid/P24_oraculo.txt
```

- **Regra do código para o rótulo:** "Malicious (malicious)" se malicious > 0; senão "Clean (undetected)" \[src/dir.c:280–282\].
- **Evidência:** `P24_oraculo.txt` e os JSON.
- **Sucesso:** para ao menos um hash com HTTP 200, o rótulo em `P23_audit.txt` bate com `last_analysis_stats`.
- **Falha:** rótulo divergente para hash conhecido (por exemplo `Clean (-1)` ou `Clean (0)` com undetected > 0).
- **Interrupção:** todos os hashes com HTTP 404. Nesse caso, submeta `rec.sh` (conteúdo inofensivo; a submissão é pública) pela interface web do VirusTotal, aguarde a análise e repita P23 e P24 em `P23b`. O caso "Malicious" só é observável em C6, sem manipular malware aqui.

### C6 — Figura 2

**P25 — Obter `evidence2.dd`**

- **Selo / reivindicação:** R — C6.
- **Base:** artigo p. 7 cita o site DFTT para amostras; identificar a imagem da Fig. 2 é \[NÃO DOCUMENTADO\]. O único identificador é o tamanho na Fig. 2: "Length: 2 GB (2845109643 bytes)".
- **Diretório:** `/aval/amostras`.
- **Comando:** procure em https://dftt.sourceforge.net uma imagem com esse nome ou tamanho; após baixar e descompactar:

```
cd /aval/amostras
stat -c '%n %s' evidence2.dd | tee /aval/evid/P25_imagem.txt
sha256sum evidence2.dd >> /aval/evid/P25_imagem.txt
```

- **Esperado segundo os autores:** não há indicação.
- **Evidência:** `P25_imagem.txt` e a URL de onde veio.
- **Sucesso:** tamanho exatamente 2845109643 bytes.
- **Falha:** —.
- **Interrupção:** imagem não encontrada ou de outro tamanho: C6 é não reproduzível; pule P26 e P27 e peça a imagem aos autores pelo comitê.

**P26 — Executar o comando da Fig. 2**

- **Selo / reivindicação:** R — C6.
- **Base:** Fig. 2 "./foremost-ng -v -x evidence2.dd", executado em `src` (Fig. 2 mostra "Output directory: /tmp/foremost-ng/src/output"). O link simbólico e a remoção de `output` são \[NÃO DOCUMENTADO\]: o comando usa nome relativo, e a saída precisa estar vazia \[src/dir.c:124\].
- **Diretório:** `/aval/foremost-ng/src`.
- **Comando:**

```
cd /aval/foremost-ng/src
ln -sf /aval/amostras/evidence2.dd evidence2.dd
rm -rf output
export VT_API_KEY=<sua_chave>
./foremost-ng -v -x evidence2.dd 2>&1 | sed "s/$VT_API_KEY/***/g" | tee /aval/evid/P26_fig2.log
cp output/audit.txt /aval/evid/P26_audit.txt
```

- **Esperado segundo os autores:** a saída da Fig. 2 (tabela em P27).
- **Evidência:** `P26_fig2.log`, `P26_audit.txt`.
- **Sucesso:** execução concluída com tabela de arquivos.
- **Falha:** execução abortada.
- **Interrupção:** cota do VT esgotada no meio: repita sem `-x` para os offsets e registre a limitação.

**P27 — Comparar com a Fig. 2**

- **Selo / reivindicação:** R — C6.
- **Diretório:** `/aval/evid`.
- **Comando:**

```
grep -E '\.(elf|script|exe|zip) ' /aval/evid/P26_audit.txt | tee /aval/evid/P27_linhas.txt
```

- **Esperado segundo os autores (transcrição da Fig. 2; confira com o PDF):**

| ID | Nome | Tamanho | Offset (bytes) | Comentário | VT |
| --- | --- | --- | --- | --- | --- |
| 0 | 00004352.elf | 57 KB | 2228224 |  | Clean (0) |
| 1 | 00004820.elf | 57 KB | 2467840 |  | Clean (0) |
| 2 | 00005108.elf | 1 KB | 2615296 |  | Clean (0) |
| 3 | 00005492.script | 3 KB | 2811904 |  | Clean (0) |
| 4 | 00399884.exe | 600 KB | 204740608 | 01/01/1970 00:00:00 | Malicious (2) |
| 5 | 00405060.exe | 52 KB | 207390720 | 01/01/1970 00:00:00 | Clean (0) |
| 6 | 00414932.exe | 2 MB | 212445184 | 01/01/2015 00:00:00 | Clean (0) |
| 7 | 00428728.exe | 2 MB | 219508736 | 01/01/2015 00:00:00 | Clean (0) |
| 8 | 00442520.exe | 536 KB | 226570240 | 01/01/1970 00:00:00 | Clean (0) |
| 9 | 00447356.exe | 600 KB | 229046272 | 01/01/1970 00:00:00 | Malicious (2) |
| 10 | 01786101.zip | 470 KB | 914484119 |  | Clean (0) |
| 11 | 01787042.zip | 350 KB | 914965615 |  | Clean (0) |

- **Evidência:** `P27_linhas.txt` e uma tabela lado a lado no parecer.
- **Sucesso:** os 12 nomes e offsets presentes, com tamanhos na mesma ordem de grandeza. Contagens do VT podem diferir \[reivindicacoes.md: Critério de reprodução\].
- **Falha:** qualquer um dos 12 ausente ou com offset diferente. Arquivos extras são registrados, mas sozinhos não reprovam.
- **Interrupção:** nenhuma.

### C7 — Arquitetura (fora da regra de R)

**P28 — Inspecionar despachante e registro**

- **Selo / reivindicação:** nenhum selo; inspeção de C7.
- **Base:** artigo pp. 2–3, Fig. 1. A inspeção por `grep` é \[NÃO DOCUMENTADO\]; não há experimento associado.
- **Diretório:** `/aval/foremost-ng/src`.
- **Comando:**

```
cd /aval/foremost-ng/src
{ grep -n 'needle->type ==' extract.c; grep -n 'init_builtin(state' state.c;
  grep -nE '#define (ELF|MACHO|EVTX|SCRIPT) ' main.h; } | tee /aval/evid/P28_arquitetura.txt
```

- **Esperado segundo os autores:** registro central de parsers, cada um com identificador, assinatura, validação e recuperação; adicionar um parser "does not require modifying the dispatcher logic itself" (p. 3).
- **Evidência:** `P28_arquitetura.txt`.
- **Sucesso:** um novo parser só exigiria uma entrada de registro.
- **Falha:** exigiria também um ramo novo no despachante (`extract_file`) e uma constante em `main.h`; registre como observação.
- **Interrupção:** nenhuma.

**P29 — Empacotar as evidências \[NÃO DOCUMENTADO\]**

- **Selo / reivindicação:** F e R.
- **Por que é necessário:** o parecer deve trazer prova de execução; um pacote com hash a torna verificável.
- **Diretório:** `/aval`.
- **Comando:**

```
cd /aval && grep -rl "$VT_API_KEY" evid && echo 'REMOVA A CHAVE' ; tar czf evid.tgz evid && sha256sum evid.tgz | tee evid.tgz.sha256
```

- **Evidência:** `evid.tgz`, `evid.tgz.sha256`.
- **Sucesso:** pacote criado e nenhum arquivo contendo a chave.
- **Falha / interrupção:** chave encontrada: apague-a dos arquivos e refaça.

## Tempo estimado

O roteiro completo leva de 4 a 6 horas de trabalho, sem contar a busca e o download de `evidence2.dd`, que os autores não indicam. Os autores não estimam tempos; os valores abaixo são do revisor.

| Fase | Passos | Tempo |
| --- | --- | --- |
| Ambiente e dependências | P1–P3 | 20–30 min |
| Obtenção e integridade | P4–P6 | 10 min |
| Compilação e instalação | P7–P9 | 5–10 min |
| Teste mínimo F | P10–P12 | 15 min |
| Amostras | P13–P16 | 30–90 min (depende do acesso a Windows e macOS) |
| C1–C4 | P17–P21 | 30–45 min |
| C5 | P22–P24 | 30–60 min (conta VT; mais 1 dia se for preciso submeter amostra) |
| C6 | P25–P27 | 15 min de busca se a imagem não existir; senão download de cerca de 2,8 GB + 15–30 min de execução |
| C7 e fechamento | P28–P29 | 15 min |

## Todos os passos

Dos 29 passos, 17 partem de procedimento dos autores (vários com adaptação marcada) e 12 são inteiramente \[NÃO DOCUMENTADO\]; toda a preparação de amostras e toda a validação de saída caem no segundo grupo.

| Passo | Selo / reiv. | Diretório | Comando (resumo) | Documentado? | Sucesso |
| --- | --- | --- | --- | --- | --- |
| P1 | F | `$HOME/aval` | registrar host | \[NÃO DOCUMENTADO\] | recursos registrados |
| P2 | F | `$HOME/aval` | `docker run … ubuntu:latest` | Dockerfile:1 (modo interativo não) | shell com `/aval` |
| P3 | F | `/aval` | `apt-get install gcc make git libssl-dev libcurl4-openssl-dev` (+ extras) | Dockerfile:3–6 (extras não) | instalação com código 0 |
| P4 | F | `/aval` | `git clone …foremost-ng.git` | artigo p. 6; Dockerfile:8 | repositório clonado |
| P5 | F, R | `/aval/foremost-ng` | `git checkout bb812a22…` | \[NÃO DOCUMENTADO\] | HEAD = commit avaliado |
| P6 | F, R | `/aval/foremost-ng` | `sha256sum` vs índice | \[NÃO DOCUMENTADO\] | hashes coincidem |
| P7 | F | `/aval/foremost-ng` | `make` na raiz | artigo p. 6 | binário gerado (registrar resultado) |
| P8 | F | `/aval/foremost-ng/src` | `make` | README.md:28–33 | `rc=0` e binário |
| P9 | F | `/aval/foremost-ng/src` | `make install` | README.md:34; Dockerfile:10 | binário, manual e conf instalados |
| P10 | F | `/aval` | `man foremost-ng` / `zcat` / `-h` | README.md:79 (`zcat`, `-h` não) | manual e ajuda legíveis |
| P11 | F | `/aval/amostras` | criar `min.img` | \[NÃO DOCUMENTADO\] | entrada criada |
| P12 | F (C2) | `/aval/saidas` | `foremost-ng -i min.img -o P12` | artigo p. 7, §4.1 | `00000128.script` IGUAL + `audit.txt` |
| P13 | R — C2, C4 | `/aval/amostras` | scripts, `gcc`, `gcc -m32` | \[NÃO DOCUMENTADO\] | amostras criadas |
| P14 | R — C1 | Windows / `/aval/amostras` | `wevtutil epl`, `python-evtx` | \[NÃO DOCUMENTADO\] | original lido sem erro |
| P15 | R — C3 | macOS `~/aval` | `lipo -info`, `lipo -thin` | \[NÃO DOCUMENTADO\] | fat e thin gerados |
| P16 | R — C1–C5 | `/aval/amostras` | montar `teste_r.img` + `offsets.txt` | \[NÃO DOCUMENTADO\] | gabarito completo |
| P17 | R — C1 | `/aval/saidas` | `foremost-ng -t evtx …` + `evtx_dump.py` | artigo p. 7 (validação não) | lido sem erro, mesmos eventos |
| P18 | R — C2 | `/aval/saidas` | `foremost-ng -t script …` + `cmp` | artigo p. 7 | `rec.*` IGUAL; `com.sh`, `curto.sh` ausentes |
| P19 | R — C3 | `/aval/saidas` | `foremost-ng -t macho …` + `file` | artigo p. 7 (validação não) | fat e thin reconhecidos |
| P20 | R — C4 | `/aval/saidas` | `foremost-ng -t elf …` + `readelf` | artigo p. 7 (validação não) | ELF32 e ELF64 legíveis |
| P21 | R — C4 (C1) | `/aval/saidas` | `foremost-ng -t evtx,elf,exe …` | artigo p. 7 | só evtx/elf/exe; ELF = P20 |
| P22 | R — C5 | `/aval/saidas` | `-x` sem chave e com chave inválida | artigo p. 7 | carving + aviso |
| P23 | R — C5 | `/aval/saidas` | `export VT_API_KEY`; `-x -t script,elf` | README.md:95–101; artigo p. 7 | rótulo VT por arquivo |
| P24 | R — C5 | `/aval/saidas/P23` | `curl` na API v3 por hash | \[NÃO DOCUMENTADO\] | rótulo = estatísticas da API |
| P25 | R — C6 | `/aval/amostras` | obter `evidence2.dd` | artigo p. 7 cita DFTT (imagem não) | 2845109643 bytes |
| P26 | R — C6 | `/aval/foremost-ng/src` | `./foremost-ng -v -x evidence2.dd` | Fig. 2 (link e `rm` não) | execução concluída |
| P27 | R — C6 | `/aval/evid` | comparar com a Fig. 2 | \[NÃO DOCUMENTADO\] | 12 nomes e offsets presentes |
| P28 | C7 (fora de R) | `/aval/foremost-ng/src` | `grep` despachante e registro | \[NÃO DOCUMENTADO\] | registro sem tocar no despachante |
| P29 | F, R | `/aval` | `tar czf evid.tgz` + `sha256sum` | \[NÃO DOCUMENTADO\] | pacote sem a chave |
