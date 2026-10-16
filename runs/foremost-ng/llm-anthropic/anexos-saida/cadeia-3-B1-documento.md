# Roteiro de execução — Foremost-NG (SBSeg 2025), selos F e R

Oct 15, 2026 · @edu

## Escopo e convenções

Este roteiro verifica o selo F (passos P1–P11) e as reivindicações C1–C6 do selo R (P12–P33) no commit `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`. Nenhum passo foi executado por quem escreveu o roteiro. Todo "resultado esperado" cita o que os autores afirmam, não um resultado observado.

**Procedimentos dos autores usados como base:**

- `README.md`: seções Installation, Usage e VirusTotal API.
- `Dockerfile`: pacotes e sequência de compilação.
- Artigo, §4, pp. 6–7: instalação, uso, `-t`, `-x` e estrutura de saída.
- Artigo, Fig. 2, p. 8: execução de referência.

Qualquer passo fora dessas fontes leva a marca **\[NÃO DOCUMENTADO\]** e a justificativa de por que é necessário.

**Convenções:**

- Diretório base: `~/fng`. Subdiretórios: `evid` (evidências), `dados` (imagens de terceiros), `amostras` (arquivos conhecidos), `imagens` (imagens montadas) e `saidas` (saídas do programa).
- Toda execução grava stdout e stderr com `2>&1 | tee` e registra o código de saída com `echo "exit=${PIPESTATUS[0]}"`.
- Cada execução usa um diretório de saída novo. O programa aborta se o diretório já existir e não estiver vazio (`src/dir.c:120-126`, "not empty"). Isso não está no README.
- Nome esperado de cada arquivo recuperado: número do bloco de 512 bytes com 8 dígitos. Exemplo da Fig. 2: `00004352.elf` no offset 2228224 = 4352 × 512 (confirmado em `src/dir.c:287`).
- A chave do VirusTotal nunca entra nas evidências nem em capturas de tela.
- Interrupção geral: se a compilação (P6) falhar, o roteiro inteiro para. Um travamento durante uma reivindicação interrompe só o bloco dela; registre o erro e passe ao bloco seguinte.

## Requisitos de hardware e software

Os autores documentam só o sistema ("Linux-based", `README.md:3`; "Unix-like system", artigo p. 6) e os pacotes do `Dockerfile`. Não há requisito de hardware nem de versões; os valores abaixo são mínimos práticos propostos para este roteiro.

| Item | Valor | Origem |
| --- | --- | --- |
| Ambiente | Máquina virtual Linux dedicada, com sudo | Instruções oficiais recomendam ambiente virtual; sudo para `make install` (artigo p. 6) |
| Sistema | Ubuntu; registre a versão exata em P1 | `Dockerfile:1` usa `ubuntu:latest`, sem versão fixa |
| Arquitetura | x86\_64 (little-endian) | \[NÃO DOCUMENTADO\] Necessária para `gcc -m32` (ELF32 em C4); C3 depende da ordem de bytes do host |
| CPU / RAM | ≥ 2 vCPU, ≥ 4 GB | \[NÃO DOCUMENTADO\] Margem para processar a imagem da Fig. 2 (2845109643 bytes) |
| Disco livre | ≥ 20 GB | \[NÃO DOCUMENTADO\] `evidence2.dd` (\~2,7 GB), saídas, amostras e VM |
| Pacotes dos autores | `gcc make git libssl-dev libcurl4-openssl-dev` | `Dockerfile:5` |
| Pacotes de verificação | `gcc-multilib binutils file curl wget unzip python3-venv` + `python-evtx` (pip) | \[NÃO DOCUMENTADO\] Ferramentas para conferir os arquivos recuperados (C1, C3, C4, C5) |
| Outras máquinas | Um Windows (exportar um `.evtx`) e um macOS (Mach-O fat e thin) | \[NÃO DOCUMENTADO\] O artefato não fornece amostras desses formatos |
| Conta externa | Chave da API do VirusTotal | `README.md:95-97` |
| Rede | github.com, dftt.sourceforge.net, www.virustotal.com, pypi.org, repositórios apt | Clone (artigo p. 6), amostras (artigo p. 6), consultas VT (artigo p. 3) |
| Dado de entrada da Fig. 2 | `evidence2.dd` | Citado na Fig. 2, mas ausente do artefato e sem origem informada |

## Preparação do ambiente e compilação (P1–P8)

Esta fase segue o `Dockerfile` e o README, com dois acréscimos não documentados: o registro do ambiente e a fixação do commit avaliado. Sem compilar em P6, nenhum selo pode ser verificado.

### P1 — Registrar o ambiente \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R / todas.
- **Diretório:** `~`
- **Comando:**

```bash
mkdir -p ~/fng/{evid,dados,amostras,imagens,saidas}
{ date -Is; uname -a; cat /etc/os-release; lscpu | grep -Ei 'architecture|byte order|^cpu\(s\)'; free -h; df -h ~; } 2>&1 | tee ~/fng/evid/P1_ambiente.txt
```

- **Esperado segundo os autores:** não há; o passo não é documentado.
- **Justificativa:** as instruções oficiais pedem que o parecer descreva o ambiente. A ordem de bytes é relevante para C3.
- **Evidência:** `evid/P1_ambiente.txt`.
- **Sucesso:** arquivo com sistema, arquitetura, "Little Endian", RAM e disco.
- **Falha:** arquitetura diferente de x86\_64 ou recursos abaixo dos requisitos.
- **Interrupção:** arquitetura big-endian ou disco < 20 GB. Ajuste o ambiente antes de seguir.

### P2 — Instalar as dependências do Dockerfile

- **Selo / reivindicação:** F / todas.
- **Diretório:** `~/fng`
- **Comando** (`Dockerfile:3-6`, executado no host em vez de dentro do contêiner):

```bash
sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y gcc make git libssl-dev libcurl4-openssl-dev 2>&1 | tee ~/fng/evid/P2_deps.txt
dpkg-query -W gcc make git libssl-dev libcurl4-openssl-dev 2>&1 | tee ~/fng/evid/P2_versoes.txt
```

- **Esperado segundo os autores:** pacotes instalados; o Dockerfile compila em seguida.
- **Observação:** a segunda linha é \[NÃO DOCUMENTADO\]. Ela registra versões, que nem o README nem o Dockerfile informam.
- **Evidência:** `evid/P2_deps.txt`, `evid/P2_versoes.txt`.
- **Sucesso:** os cinco pacotes aparecem com versão em `P2_versoes.txt`.
- **Falha:** algum pacote ausente ou sem versão.
- **Interrupção:** `apt-get` não consegue instalar um dos pacotes.

### P3 — Clonar o repositório

- **Selo / reivindicação:** F / todas.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 6; `Dockerfile:8`):

```bash
cd ~/fng && git clone https://github.com/cristianzsh/foremost-ng.git 2>&1 | tee ~/fng/evid/P3_clone.txt
```

- **Esperado segundo os autores:** diretório `foremost-ng` com o código.
- **Evidência:** `evid/P3_clone.txt`.
- **Sucesso:** `~/fng/foremost-ng/src/Makefile` existe.
- **Falha:** erro de rede ou repositório inexistente.
- **Interrupção:** clone impossível e sem `artefato.zip` disponível. Com o ZIP, descompacte em `~/fng/foremost-ng` e siga para P4.

### P4 — Fixar e conferir o commit avaliado \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R / todas.
- **Diretório:** `~/fng/foremost-ng`
- **Comando:**

```bash
cd ~/fng/foremost-ng && git checkout bb812a22cb06ef87b5a2d877dfb6f40eb12d460d 2>&1 | tee ~/fng/evid/P4_commit.txt
git rev-parse HEAD | tee -a ~/fng/evid/P4_commit.txt
sha256sum README.md src/extract.c src/vt_query.c | tee -a ~/fng/evid/P4_commit.txt
```

- **Esperado segundo os autores:** não há. O artigo e o Dockerfile usam o HEAD do repositório.
- **Justificativa:** a avaliação é da versão `bb812a22`, e o HEAD pode ter mudado.
- **Evidência:** `evid/P4_commit.txt`.
- **Sucesso:** HEAD = `bb812a22…` e hashes iguais ao índice de `artefato.txt`:
  - `README.md` = `ff3414f0…`
  - `src/extract.c` = `4f81160c…`
  - `src/vt_query.c` = `d20bf972…`
- **Falha:** hashes diferentes.
- **Interrupção:** commit inexistente e sem `artefato.zip` (SHA-256 `955c770e…`) para usar no lugar.

### P5 — Compilar na raiz, como no artigo

- **Selo / reivindicação:** F / nenhuma.
- **Diretório:** `~/fng/foremost-ng`
- **Comando** (artigo p. 6: `cd foremost-ng`, `make`):

```bash
cd ~/fng/foremost-ng && make 2>&1 | tee ~/fng/evid/P5_make_raiz.txt; echo "exit=${PIPESTATUS[0]}" | tee -a ~/fng/evid/P5_make_raiz.txt
```

- **Esperado segundo os autores:** compilação concluída.
- **Evidência:** `evid/P5_make_raiz.txt`.
- **Sucesso:** `exit=0` e binário gerado.
- **Falha:** erro do tipo "no makefile found". O índice do artefato só lista `src/Makefile`. Registre a falha como divergência de documentação.
- **Interrupção:** nenhuma; siga para P6.

### P6 — Compilar em `src/`, como no README e no Dockerfile

- **Selo / reivindicação:** F / todas.
- **Diretório:** `~/fng/foremost-ng/src`
- **Comando** (`README.md:28,33`; `Dockerfile:9-10`):

```bash
cd ~/fng/foremost-ng/src && make 2>&1 | tee ~/fng/evid/P6_make.txt; echo "exit=${PIPESTATUS[0]}" | tee -a ~/fng/evid/P6_make.txt
ls -l foremost-ng && file foremost-ng | tee -a ~/fng/evid/P6_make.txt
```

- **Esperado segundo os autores:** binário `foremost-ng` gerado.
- **Evidência:** `evid/P6_make.txt`, com os avisos do compilador.
- **Sucesso:** `exit=0` e `file` indica executável ELF 64-bit.
- **Falha:** erro de compilação ou de ligação, por exemplo com `-lssl`, `-lcurl` ou `-lcrypto`.
- **Interrupção:** sem binário, encerre o roteiro. Registre F e R como não verificáveis por falha de compilação.

### P7 — Instalar

- **Selo / reivindicação:** F / todas.
- **Diretório:** `~/fng/foremost-ng/src`
- **Comando** (`README.md:34`; artigo p. 6):

```bash
cd ~/fng/foremost-ng/src && sudo make install 2>&1 | tee ~/fng/evid/P7_install.txt
{ command -v foremost-ng; ls -l /usr/local/etc/foremost.conf /usr/share/man/man8/foremost-ng.8.gz; } 2>&1 | tee -a ~/fng/evid/P7_install.txt
```

- **Esperado segundo os autores:** "the foremost-ng binary is available system-wide" (artigo p. 7).
- **Evidência:** `evid/P7_install.txt`.
- **Sucesso:** `/usr/local/bin/foremost-ng`, `foremost.conf` e a página de manual instalados.
- **Falha:** erro de instalação.
- **Interrupção:** nenhuma. Sem instalação, use `~/fng/foremost-ng/src/foremost-ng` nos passos seguintes; o `foremost.conf` está nesse diretório.

### P8 — Ajuda, versão e manual

- **Selo / reivindicação:** F / nenhuma.
- **Diretório:** `~/fng`
- **Comando** (`README.md:79`; artigo p. 7, "using man foremost-ng"):

```bash
{ foremost-ng -h; foremost-ng -V; man foremost-ng | col -b | head -60; } 2>&1 | tee ~/fng/evid/P8_ajuda.txt
```

- **Esperado segundo os autores:** documentação e opções disponíveis.
- **Evidência:** `evid/P8_ajuda.txt`.
- **Sucesso:** o uso lista `-i`, `-o`, `-t`, `-v` e `-x`; versão impressa; manual exibido.
- **Falha:** ausência dessas opções ou do manual.
- **Interrupção:** nenhuma.

## Teste mínimo para o selo F (P9–P11)

F é verificado quando o programa compilado (P6) recupera ao menos um arquivo de uma imagem real, com `audit.txt` e subdiretório por formato. Os autores indicam a DFTT como fonte de amostras (artigo p. 6), mas não dizem qual imagem usar.

### P9 — Obter uma imagem de teste da DFTT (escolha da imagem: \[NÃO DOCUMENTADO\])

- **Selo / reivindicação:** F / nenhuma.
- **Diretório:** `~/fng/dados/dftt`
- **Comando** (substitua `<URL_DO_TESTE>` pela imagem de carving escolhida no site):

```bash
mkdir -p ~/fng/dados/dftt && cd ~/fng/dados/dftt
wget -O teste_dftt.zip '<URL_DO_TESTE>' 2>&1 | tee ~/fng/evid/P9_download.txt
unzip -o teste_dftt.zip 2>&1 | tee -a ~/fng/evid/P9_download.txt
find . -type f -exec sha256sum {} + | tee ~/fng/evid/P9_hashes.txt
```

- **Esperado segundo os autores:** "Carving test samples can be downloaded from https://dftt.sourceforge.net" (artigo p. 6).
- **Justificativa:** sem uma entrada não há como observar funcionalidade. Os autores apontam o site, mas não a imagem nem o conteúdo esperado.
- **Evidência:** `evid/P9_download.txt`, `evid/P9_hashes.txt` e a URL usada, anotada no parecer.
- **Sucesso:** imagem bruta (`.dd`, `.img` ou similar) baixada e com hash registrado.
- **Falha:** site indisponível ou imagem sem arquivos carváveis.
- **Interrupção:** nenhuma. Sem DFTT, execute P10 sobre `~/fng/imagens/c4.dd` depois de P23. Isso é \[NÃO DOCUMENTADO\]; registre a substituição.

### P10 — Execução básica com `-i` e `-o`

- **Selo / reivindicação:** F / nenhuma.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 7, §4.1, mais `-v` da Fig. 2; `<IMAGEM>` é o arquivo obtido em P9):

```bash
cd ~/fng && foremost-ng -v -i dados/dftt/<IMAGEM> -o saidas/P10 2>&1 | tee evid/P10_saida.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P10_saida.txt
find saidas/P10 -type f | sort | tee evid/P10_arquivos.txt
cp saidas/P10/audit.txt evid/P10_audit.txt; ls -l saidas/P10/recovery.log 2>&1 | tee -a evid/P10_arquivos.txt
find saidas/P10 -type f ! -name audit.txt -exec file {} + | tee evid/P10_file.txt
```

- **Esperado segundo os autores:** subdiretórios por formato, arquivos nomeados como `00000001.evtx`, `audit.txt` com metadados e um `recovery.log` com offsets, hashes e VT (artigo pp. 6–7, §4.2).
- **Evidência:** `evid/P10_saida.txt`, `P10_arquivos.txt`, `P10_audit.txt`, `P10_file.txt`.
- **Sucesso:** `exit=0`, `audit.txt` presente e ao menos um arquivo recuperado, reconhecido por `file` como do formato do seu subdiretório.
- **Falha:** nenhum arquivo recuperado de uma imagem que, segundo a DFTT, contém arquivos; arquivos ilegíveis. A ausência de `recovery.log` é divergência de documentação, não falha de F.
- **Interrupção:** falha de segmentação, "Unable to load the config file" ou travamento. Registre e encerre a verificação de F.

### P11 — Restrição de formatos com `-t`

- **Selo / reivindicação:** F / nenhuma.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 7, §4.1):

```bash
cd ~/fng && foremost-ng -t evtx,elf,exe -i dados/dftt/<IMAGEM> -o saidas/P11 2>&1 | tee evid/P11_saida.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P11_saida.txt
find saidas/P11 -mindepth 1 -type d | sort | tee evid/P11_subdirs.txt
```

- **Esperado segundo os autores:** "only the EVTX, ELF, and EXE modules will run".
- **Evidência:** `evid/P11_saida.txt`, `evid/P11_subdirs.txt`.
- **Sucesso:** `exit=0` e nenhum subdiretório além de `evtx`, `elf` e `exe`. Ausência total de subdiretórios também é sucesso se a imagem não tiver esses formatos.
- **Falha:** subdiretórios de outros formatos ou erro de tipo desconhecido.
- **Interrupção:** travamento.

**Decisão sobre F:** atribua F se P6, P10 e P11 tiverem sucesso, registrando no parecer as lacunas de documentação (versões, exemplo mínimo no README e divergência em P5).

## Preparação das amostras e imagens de teste (P12–P13)

O artefato não traz dados para C1–C4, então cada reivindicação usa uma imagem montada com arquivos conhecidos em offsets conhecidos. Os dois passos abaixo são inteiramente \[NÃO DOCUMENTADO\]: sem eles não há resultado contra o qual comparar a saída.

### P12 — Instalar ferramentas de verificação \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C1, C3, C4, C5.
- **Diretório:** `~/fng`
- **Comando:**

```bash
sudo apt-get install -y gcc-multilib binutils file curl wget unzip python3-venv 2>&1 | tee ~/fng/evid/P12_ferramentas.txt
python3 -m venv ~/fng/venv && ~/fng/venv/bin/pip install python-evtx 2>&1 | tee -a ~/fng/evid/P12_ferramentas.txt
{ readelf --version | head -1; file --version | head -1; ~/fng/venv/bin/pip show python-evtx | grep -i ^version; } | tee -a ~/fng/evid/P12_ferramentas.txt
```

- **Esperado segundo os autores:** não há. O artigo diz que o EVTX "can then be parsed with standard event log tools" sem nomear a ferramenta; para ELF e Mach-O também não há ferramenta indicada.
- **Justificativa:** `readelf` confere C4, `file` confere C3 e C4, `python-evtx` confere C1, `gcc-multilib` gera o ELF32 de C4.
- **Evidência:** `evid/P12_ferramentas.txt`.
- **Sucesso:** as três versões impressas.
- **Falha:** algum pacote não instalado.
- **Interrupção:** sem `python-evtx`, C1 só pode ser conferido com outra ferramenta, por exemplo o Visualizador de Eventos do Windows; registre a troca. Sem `gcc-multilib`, C4 fica limitado ao ELF64.

### P13 — Criar o script de montagem das imagens \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C1–C5.
- **Diretório:** `~/fng`
- **Comando:**

```bash
cat > ~/fng/montar.sh <<'EOF'
#!/usr/bin/env bash
# uso: montar.sh <imagem_saida> <mapa_saida.tsv> <amostra>...
set -euo pipefail
img=$1; mapa=$2; shift 2
: > "$img"
printf 'offset\tnome_esperado\tbytes\tsha256\tamostra\n' > "$mapa"
head -c 1048576 /dev/zero >> "$img"
for f in "$@"; do
  off=$(stat -c %s "$img")
  printf '%s\t%08d\t%s\t%s\t%s\n' "$off" "$((off/512))" "$(stat -c %s "$f")" "$(sha256sum "$f" | cut -d' ' -f1)" "$f" >> "$mapa"
  cat "$f" >> "$img"
  sz=$(stat -c %s "$img")
  head -c $(( (512 - sz % 512) % 512 + 1048576 )) /dev/zero >> "$img"
done
EOF
chmod +x ~/fng/montar.sh && cp ~/fng/montar.sh ~/fng/evid/P13_montar.sh
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** cada amostra começa num múltiplo de 512 bytes, separada por 1 MiB de zeros. Assim o nome esperado (bloco em 8 dígitos) e o offset ficam conhecidos, e os zeros encerram a varredura de scripts, que para no primeiro byte não imprimível.
- **Evidência:** `evid/P13_montar.sh`; cada uso gera um mapa `.tsv` em `evid/`.
- **Sucesso:** script executável criado.
- **Falha / interrupção:** erro de sintaxe ao executá-lo em P15; corrija antes de seguir.
- **Leitura dos mapas:** a coluna `nome_esperado` dá o prefixo do arquivo recuperado (por exemplo `00002048` → `00002048.elf`). Arquivos recuperados em outros offsets são achados extras, como trechos internos de binários; registre-os, mas não contam como falha.

## Bloco C1 — EVTX (P14–P16)

C1 é reproduzida se um `.evtx` sair no bloco esperado e for lido por uma ferramenta de eventos com o mesmo número de eventos do original. Os autores não fornecem amostra EVTX nem nomeiam a ferramenta.

### P14 — Exportar um log EVTX num Windows \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C1.
- **Diretório:** `C:\temp` no Windows; depois `~/fng/amostras/c1` na VM.
- **Comando** (PowerShell como administrador no Windows; depois copie o arquivo para a VM):

```powershell
New-Item -ItemType Directory -Force C:\temp | Out-Null
wevtutil epl Application C:\temp\c1_application.evtx
Get-FileHash C:\temp\c1_application.evtx -Algorithm SHA256
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** o artefato não traz nenhum `.evtx`, e C1 exige um arquivo conhecido para comparar.
- **Evidência:** hash do Windows anotado em `evid/P14_hash_windows.txt` e `sha256sum ~/fng/amostras/c1/*.evtx` na VM, que deve coincidir.
- **Sucesso:** os dois hashes iguais.
- **Falha:** hashes diferentes, indicando cópia corrompida.
- **Interrupção:** sem acesso a um Windows ou a um `.evtx` legítimo, marque C1 como não verificada.

### P15 — Montar a imagem e executar com `-t evtx`

- **Selo / reivindicação:** R / C1.
- **Diretório:** `~/fng`
- **Comando** (forma de uso do artigo p. 7, §4.1; montagem via P13):

```bash
cd ~/fng && ./montar.sh imagens/c1.dd evid/P15_mapa_c1.tsv amostras/c1/c1_application.evtx
foremost-ng -v -t evtx -i imagens/c1.dd -o saidas/c1 2>&1 | tee evid/P15_c1.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P15_c1.txt
cp saidas/c1/audit.txt evid/P15_audit_c1.txt; ls -l saidas/c1/evtx/ | tee -a evid/P15_c1.txt
```

- **Esperado segundo os autores:** EVTX identificado pela assinatura "ElfFile", carvado pelos chunks de 64 KiB e gravado em `evtx/` (artigo p. 6).
- **Evidência:** `evid/P15_mapa_c1.tsv`, `evid/P15_c1.txt`, `evid/P15_audit_c1.txt`.
- **Sucesso:** `exit=0` e um arquivo `<nome_esperado>.evtx` em `saidas/c1/evtx/`.
- **Falha:** nenhum `.evtx` no bloco esperado.
- **Interrupção:** travamento; registre e passe ao bloco C2.

### P16 — Validar o EVTX recuperado \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C1.
- **Diretório:** `~/fng`
- **Comando** (`<NOME>` é o arquivo listado em P15):

```bash
cd ~/fng; O=amostras/c1/c1_application.evtx; C=saidas/c1/evtx/<NOME>.evtx
{ stat -c '%n %s bytes' "$O" "$C"; sha256sum "$O" "$C"; cmp -n "$(stat -c %s "$O")" "$O" "$C" && echo 'prefixo identico'; } 2>&1 | tee evid/P16_c1_comparacao.txt
venv/bin/evtx_dump.py "$O" > evid/P16_original.xml 2> evid/P16_original.err
venv/bin/evtx_dump.py "$C" > evid/P16_recuperado.xml 2> evid/P16_recuperado.err; echo "exit=$?" | tee -a evid/P16_c1_comparacao.txt
echo "eventos original=$(grep -c '<Event ' evid/P16_original.xml) recuperado=$(grep -c '<Event ' evid/P16_recuperado.xml)" | tee -a evid/P16_c1_comparacao.txt
```

- **Esperado segundo os autores:** "The resulting EVTX file can then be parsed with standard event log tools" (artigo p. 6).
- **Justificativa:** a ferramenta de leitura não é nomeada pelos autores; o resultado esperado de C1 em `reivindicacoes.md` é um arquivo "legível por ferramenta de análise de eventos".
- **Evidência:** `evid/P16_c1_comparacao.txt`, os dois `.xml` e os dois `.err`.
- **Sucesso:** o parser lê o arquivo recuperado sem erro fatal e o número de eventos é igual ao do original. Tamanho maior que o original deve ser registrado como observação, não como falha.
- **Falha:** erro fatal do parser, zero eventos ou menos eventos que o original.
- **Interrupção:** nenhuma; ao terminar, siga para C2.

## Bloco C2 — Scripts (P17–P19)

C2 é reproduzida se os três scripts válidos saírem íntegros nos blocos esperados e os dois controles negativos não forem recuperados. Os controles testam as duas regras do artigo: mínimo de 32 bytes e "more than comments".

### P17 — Criar os scripts e montar a imagem \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C2.
- **Diretório:** `~/fng/amostras/c2`
- **Comando:**

```bash
mkdir -p ~/fng/amostras/c2 && cd ~/fng/amostras/c2
printf '#!/bin/bash\n# teste C2\nfor i in 1 2 3; do echo "linha $i"; done\n' > s1_bash.sh
printf '#!/usr/bin/env python3\nimport sys\nprint("teste C2", sys.version)\n' > s2_python.py
printf '#!/usr/bin/env pwsh\nGet-ChildItem -Path . | Select-Object Name\n' > s3_pwsh.ps1
printf '#!/bin/sh\n# so comentario 1\n# so comentario 2\n# fim\n' > n1_comentarios.sh
printf '#!/bin/sh\necho oi\n' > n2_curto.sh
wc -c * | tee ~/fng/evid/P17_tamanhos.txt
cd ~/fng && ./montar.sh imagens/c2.dd evid/P17_mapa_c2.tsv amostras/c2/s1_bash.sh amostras/c2/s2_python.py amostras/c2/s3_pwsh.ps1 amostras/c2/n1_comentarios.sh amostras/c2/n2_curto.sh
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** o artefato não traz scripts de teste. `n1` tem mais de 32 bytes, mas só comentários; `n2` tem menos de 32 bytes.
- **Evidência:** `evid/P17_tamanhos.txt`, `evid/P17_mapa_c2.tsv`.
- **Sucesso:** `n2_curto.sh` com menos de 32 bytes, os demais com 32 ou mais, mapa com cinco linhas.
- **Falha / interrupção:** erro na montagem; corrija antes de P18.

### P18 — Executar com `-t script`

- **Selo / reivindicação:** R / C2.
- **Diretório:** `~/fng`
- **Comando** (forma de uso do artigo p. 7, §4.1; o identificador `script` vem do código, `src/state.c:695`):

```bash
cd ~/fng && foremost-ng -v -t script -i imagens/c2.dd -o saidas/c2 2>&1 | tee evid/P18_c2.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P18_c2.txt
cp saidas/c2/audit.txt evid/P18_audit_c2.txt; ls -l saidas/c2/script/ | tee -a evid/P18_c2.txt
```

- **Esperado segundo os autores:** scripts localizados pelo shebang, com "all printable characters up to a non-printable sentinel", mínimo de 32 bytes e mais que comentários (artigo p. 6).
- **Observação:** o artigo usa `-t` e cita scripts como formato registrado, mas não lista o identificador `script`; o nome vem do código.
- **Evidência:** `evid/P18_c2.txt`, `evid/P18_audit_c2.txt`.
- **Sucesso:** `exit=0` e arquivos em `saidas/c2/script/`.
- **Falha:** "usage" impresso (tipo não reconhecido) ou diretório vazio.
- **Interrupção:** travamento; registre e passe ao bloco C3.

### P19 — Conferir positivos e negativos \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C2.
- **Diretório:** `~/fng`
- **Comando:**

```bash
cd ~/fng && tail -n +2 evid/P17_mapa_c2.tsv | while IFS=$'\t' read -r off nome bytes hash amostra; do
  c=$(ls saidas/c2/script/"$nome".* 2>/dev/null | head -1)
  if [ -n "$c" ]; then r=$(cmp -s "$amostra" "$c" && echo identico || echo diferente); echo "$amostra -> $c ($r) primeira_linha: $(head -1 "$c")"; else echo "$amostra -> NAO RECUPERADO"; fi
done | tee evid/P19_c2_resultado.txt
```

- **Esperado segundo os autores:** scripts extraídos "complete with interpreter directives"; nada abaixo de 32 bytes ou só com comentários.
- **Evidência:** `evid/P19_c2_resultado.txt`.
- **Sucesso:** `s1`, `s2` e `s3` recuperados e idênticos, com o shebang na primeira linha; `n1` e `n2` não recuperados.
- **Falha:** qualquer um dos três positivos ausente ou diferente. Se `n1` ou `n2` for recuperado, registre a divergência da regra correspondente; o resultado esperado de C2 em `reivindicacoes.md` inclui essas regras, então trate como reprodução parcial e justifique no parecer.
- **Interrupção:** nenhuma; siga para C3.

## Bloco C3 — Mach-O fat e thin (P20–P22)

C3 é reproduzida só se o binário fat e o thin saírem nos blocos esperados e forem reconhecidos como Mach-O. A análise estática anterior indica que o ramo thin não grava nada em host little-endian (`src/extract.c:2363` e `:2409`); este bloco confirma ou refuta isso.

### P20 — Obter binários fat e thin num macOS \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C3.
- **Diretório:** `~/c3` no macOS; depois `~/fng/amostras/c3` na VM.
- **Comando** (no macOS; se `x86_64` não aparecer em `lipo -info`, use outra arquitetura listada):

```bash
mkdir -p ~/c3 && cd ~/c3
lipo -info /bin/ls | tee lipo_info.txt
cp /bin/ls macho_fat.bin
lipo /bin/ls -thin x86_64 -output macho_thin64.bin
lipo -info macho_fat.bin macho_thin64.bin | tee -a lipo_info.txt
shasum -a 256 *.bin | tee sha256_macos.txt
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** o artefato não traz Mach-O, e C3 exige um exemplar de cada tipo.
- **Observação:** um Mach-O thin de 32 bits é difícil de obter em macOS atual. Se não houver um, registre que só o thin de 64 bits foi testado.
- **Evidência:** `lipo_info.txt` e `sha256_macos.txt`, copiados para `~/fng/evid/P20_*`, e `sha256sum ~/fng/amostras/c3/*.bin` na VM, que deve coincidir.
- **Sucesso:** `macho_fat.bin` descrito como "Architectures in the fat file" e `macho_thin64.bin` como "Non-fat file", com hashes iguais nas duas máquinas.
- **Falha:** hashes diferentes.
- **Interrupção:** sem acesso a macOS ou a binários Mach-O legítimos, marque C3 como não verificada.

### P21 — Montar a imagem e executar com `-t macho`

- **Selo / reivindicação:** R / C3.
- **Diretório:** `~/fng`
- **Comando** (forma de uso do artigo p. 7, §4.1; identificador `macho` do artigo p. 3, "MACHO", e do código, `src/state.c:672`):

```bash
cd ~/fng && ./montar.sh imagens/c3.dd evid/P21_mapa_c3.tsv amostras/c3/macho_fat.bin amostras/c3/macho_thin64.bin
foremost-ng -v -t macho -i imagens/c3.dd -o saidas/c3 2>&1 | tee evid/P21_c3.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P21_c3.txt
cp saidas/c3/audit.txt evid/P21_audit_c3.txt; ls -l saidas/c3/macho/ 2>&1 | tee -a evid/P21_c3.txt
```

- **Esperado segundo os autores:** "The complete Mach-O binary, whether fat or thin, is written out" (artigo p. 6).
- **Evidência:** `evid/P21_mapa_c3.tsv`, `evid/P21_c3.txt`, `evid/P21_audit_c3.txt`.
- **Sucesso:** `exit=0` e dois arquivos `.macho`, um em cada `nome_esperado` do mapa.
- **Falha:** algum dos dois ausente. A ausência só do thin confirma o defeito apontado na análise estática.
- **Interrupção:** travamento; registre e passe ao bloco C4.

### P22 — Conferir os Mach-O recuperados \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C3.
- **Diretório:** `~/fng`
- **Comando:**

```bash
cd ~/fng && tail -n +2 evid/P21_mapa_c3.tsv | while IFS=$'\t' read -r off nome bytes hash amostra; do
  c=$(ls saidas/c3/macho/"$nome".* 2>/dev/null | head -1)
  if [ -n "$c" ]; then echo "$amostra ($bytes bytes) -> $c ($(stat -c %s "$c") bytes): $(file -b "$c")"; cmp -s "$amostra" "$c" && echo '  identico' || echo '  diferente do original'; else echo "$amostra -> NAO RECUPERADO"; fi
done | tee evid/P22_c3_resultado.txt
```

- **Esperado segundo os autores:** binário completo, com as fatias de 32 e 64 bits preservadas.
- **Justificativa:** `file` é a ferramenta disponível no Linux para reconhecer Mach-O; o resultado esperado de C3 em `reivindicacoes.md` é "reconhecível por ferramenta apropriada". Se possível, confirme também no macOS com `lipo -info` sobre os arquivos recuperados.
- **Evidência:** `evid/P22_c3_resultado.txt`.
- **Sucesso:** os dois recuperados; `file` indica "Mach-O universal binary" para o fat e "Mach-O 64-bit" para o thin.
- **Falha:** algum ausente ou não reconhecido. Tamanho diferente do original é observação a registrar, não falha.
- **Interrupção:** nenhuma; siga para C4.

## Bloco C4 — ELF 32 e 64 bits (P23–P25)

C4 é reproduzida se os dois ELF saírem nos blocos esperados e o `readelf` ler cabeçalho e cabeçalhos de programa de cada um, com a classe correta. A imagem `c4.dd` também serve de entrada para C5.

### P23 — Criar os ELF de teste e montar a imagem \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C4 e C5.
- **Diretório:** `~/fng/amostras/c4`
- **Comando:**

```bash
mkdir -p ~/fng/amostras/c4 && cd ~/fng/amostras/c4
cp /usr/bin/ls elf64_ls.bin
printf 'int main(void){return 0;}\n' > h.c && gcc -m32 -o elf32_hello.bin h.c && rm h.c
file elf64_ls.bin elf32_hello.bin | tee ~/fng/evid/P23_file.txt
cd ~/fng && ./montar.sh imagens/c4.dd evid/P23_mapa_c4.tsv amostras/c4/elf32_hello.bin amostras/c4/elf64_ls.bin
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** o artefato não traz ELF de teste; C4 pede um exemplar de 32 e um de 64 bits. Os dois são little-endian, o único caso tratado pelo código (`src/extract.c:2172`).
- **Evidência:** `evid/P23_file.txt`, `evid/P23_mapa_c4.tsv`.
- **Sucesso:** `file` indica "ELF 32-bit LSB" e "ELF 64-bit LSB"; mapa com duas linhas.
- **Falha:** `gcc -m32` falha (sem `gcc-multilib`); prossiga só com o ELF64 e registre C4 como parcialmente verificável.
- **Interrupção:** nenhuma.

### P24 — Executar com `-t elf`

- **Selo / reivindicação:** R / C4.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 7, §4.1, exemplo com `-t elf`, sem `-x`, que fica para C5):

```bash
cd ~/fng && foremost-ng -v -t elf -i imagens/c4.dd -o saidas/c4 2>&1 | tee evid/P24_c4.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P24_c4.txt
cp saidas/c4/audit.txt evid/P24_audit_c4.txt; ls -l saidas/c4/elf/ | tee -a evid/P24_c4.txt
```

- **Esperado segundo os autores:** ELF identificado pela assinatura e pela classe, extraído pela união dos segmentos carregáveis e gravado em `elf/` (artigo p. 6).
- **Evidência:** `evid/P24_c4.txt`, `evid/P24_audit_c4.txt`.
- **Sucesso:** `exit=0` e dois `.elf` nos `nome_esperado` do mapa.
- **Falha:** algum dos dois ausente.
- **Interrupção:** travamento; registre e passe ao bloco C5.

### P25 — Validar a estrutura dos ELF \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C4.
- **Diretório:** `~/fng`
- **Comando:**

```bash
cd ~/fng && tail -n +2 evid/P23_mapa_c4.tsv | while IFS=$'\t' read -r off nome bytes hash amostra; do
  c=$(ls saidas/c4/elf/"$nome".* 2>/dev/null | head -1)
  if [ -z "$c" ]; then echo "$amostra -> NAO RECUPERADO"; continue; fi
  echo "== $amostra ($bytes bytes) -> $c ($(stat -c %s "$c") bytes)"
  cmp -n "$(stat -c %s "$c")" "$c" "$amostra" && echo '  prefixo identico ao original'
  readelf -h "$c" | grep -E 'Class|Type|Machine'; readelf -l "$c" > /dev/null && echo '  readelf -l ok'
  readelf -S "$c" 2>&1 | grep -iE 'warning|error' | head -3
done 2>&1 | tee evid/P25_c4_resultado.txt
```

- **Esperado segundo os autores:** "The carved ELF file retains the correct executable layout and symbol information" (artigo p. 6).
- **Justificativa:** `readelf` é a ferramenta padrão para conferir a estrutura; o resultado esperado de C4 em `reivindicacoes.md` é "estruturalmente legível por analisador ELF".
- **Evidência:** `evid/P25_c4_resultado.txt`.
- **Sucesso:** os dois recuperados; `readelf -h` mostra ELF32 e ELF64 nos arquivos certos; `readelf -l` sem erro.
- **Falha:** algum ausente, classe errada ou erro em `readelf -h`/`-l`.
- **Observação:** avisos de `readelf -S` sobre seções fora do arquivo indicam que a tabela de seções e os símbolos ficaram de fora. Isso contradiz a frase do artigo sobre "symbol information" e deve ir ao parecer, mas não reprova o resultado esperado de C4.
- **Interrupção:** nenhuma; siga para C5.

## Bloco C5 — VirusTotal (P26–P29)

C5 é reproduzida se, com chave, cada arquivo recuperado tiver no `audit.txt` um rótulo igual ao que a API devolve para o SHA-256 desse arquivo, e se, sem chave, houver aviso e o carving terminar. Como o `audit.txt` não registra o hash (`src/dir.c:292-295`), a conferência independente em P29 é indispensável.

### P26 — Obter a chave da API

- **Selo / reivindicação:** R / C5.
- **Diretório:** navegador.
- **Comando:** nenhum; siga `README.md:95-97`: criar conta gratuita no VirusTotal e copiar a chave pessoal.
- **Esperado segundo os autores:** chave pessoal disponível.
- **Evidência:** anote no parecer só que a chave existe e o tipo de conta (gratuita ou não); nunca a chave.
- **Sucesso:** chave obtida.
- **Falha / interrupção:** sem chave, execute só P27 e marque a parte com consulta de C5 como não verificada.

### P27 — Executar com `-x` sem chave

- **Selo / reivindicação:** R / C5.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 7, §4.1, `-x -t elf`; `env -u` garante a variável ausente):

```bash
cd ~/fng && env -u VT_API_KEY foremost-ng -v -x -t elf -i imagens/c4.dd -o saidas/c5_sem 2>&1 | tee evid/P27_c5_sem.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P27_c5_sem.txt
cp saidas/c5_sem/audit.txt evid/P27_audit_c5_sem.txt; ls -l saidas/c5_sem/elf/ | tee -a evid/P27_c5_sem.txt
```

- **Esperado segundo os autores:** "If the API key is missing or invalid, Foremost-NG will still perform carving but will emit a warning and skip all VT lookups" (artigo p. 7).
- **Evidência:** `evid/P27_c5_sem.txt`, `evid/P27_audit_c5_sem.txt`.
- **Sucesso:** `exit=0`, os mesmos dois `.elf` de P24 e uma mensagem de aviso sobre `VT_API_KEY`.
- **Falha:** carving interrompido ou nenhum aviso.
- **Observação:** se a coluna VT do `audit.txt` mostrar "Clean (0)" sem consulta, registre como rótulo enganoso; não reprova este subitem.
- **Interrupção:** travamento.

### P28 — Executar com `-x` e chave válida

- **Selo / reivindicação:** R / C5.
- **Diretório:** `~/fng`
- **Comando** (artigo p. 7, `export VT_API_KEY=<YOUR_VT_API_KEY>`; `README.md:101`):

```bash
export VT_API_KEY=<SUA_CHAVE>
cd ~/fng && foremost-ng -v -x -t elf -i imagens/c4.dd -o saidas/c5_com 2>&1 | tee evid/P28_c5_com.txt; echo "exit=${PIPESTATUS[0]}" | tee -a evid/P28_c5_com.txt
cp saidas/c5_com/audit.txt evid/P28_audit_c5_com.txt
```

- **Esperado segundo os autores:** "compute SHA-256 (or SHA-1) hashes for each extracted ELF binary, query VirusTotal's API, and annotate the audit.txt with malicious and undetected counts" (artigo p. 7).
- **Evidência:** `evid/P28_c5_com.txt`, `evid/P28_audit_c5_com.txt`. Antes de guardar, confira com `grep -c "$VT_API_KEY" evid/P28_*` que a chave não aparece (resultado 0).
- **Sucesso:** `exit=0` e coluna VT preenchida com "Clean (n)" ou "Malicious (n)" para cada arquivo.
- **Falha:** coluna vazia ou erro de rede persistente (`curl_easy_perform() failed`).
- **Interrupção:** erro de rede em todas as consultas; verifique o acesso a www.virustotal.com antes de repetir em novo diretório.

### P29 — Conferir os rótulos direto na API \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C5.
- **Diretório:** `~/fng/saidas/c5_com/elf`
- **Comando:**

```bash
cd ~/fng/saidas/c5_com/elf && for f in *.elf; do h=$(sha256sum "$f" | cut -d' ' -f1); echo "== $f $h"; curl -s -H "x-apikey: $VT_API_KEY" "https://www.virustotal.com/api/v3/files/$h" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("data",{}).get("attributes",{}).get("last_analysis_stats", d.get("error")))'; done | tee ~/fng/evid/P29_vt_direto.txt
```

- **Esperado segundo os autores:** não há procedimento de conferência.
- **Justificativa:** o `audit.txt` não registra o hash, e o parsing do JSON depende de uma ordem fixa de chaves (`src/vt_query.c:180`). Só a consulta independente mostra se o rótulo corresponde à resposta real.
- **Se todos os hashes vierem como `NotFoundError`:** os arquivos carvados são inéditos para o VT e o rótulo "Clean (0)" nada prova. Envie um único arquivo benigno gerado por você (o `elf32_hello` recuperado) com `curl -s -X POST -H "x-apikey: $VT_API_KEY" -F "file=@<ARQUIVO>.elf" https://www.virustotal.com/api/v3/files`, aguarde a análise, repita P28 em `saidas/c5_com2` e repita este passo. Nunca envie arquivos de evidência real.
- **Evidência:** `evid/P29_vt_direto.txt` e, se houver reenvio, `evid/P29_reexecucao.txt`.
- **Sucesso:** para ao menos um arquivo conhecido pelo VT, o rótulo do `audit.txt` bate com a API: "Malicious (m)" se `malicious` > 0, senão "Clean (u)" com `u` = `undetected`.
- **Falha:** rótulo divergente da API, por exemplo "Clean (0)" ou "Clean (-1)" quando a API mostra `undetected` > 0.
- **Interrupção:** limite de requisições da chave atingido (HTTP 429); aguarde e repita.

## Bloco C6 — Figura 2 (P30–P33)

C6 só pode ser verificada com o arquivo `evidence2.dd`, que não está no artefato e cuja origem os autores não informam. Sem ele, C6 é não reproduzível e P31–P32 não se aplicam.

### P30 — Obter `evidence2.dd` \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C6.
- **Diretório:** `~/fng/dados`
- **Comando** (após receber o arquivo dos autores ou do comitê):

```bash
cd ~/fng/dados && ls -l evidence2.dd && sha256sum evidence2.dd | tee ~/fng/evid/P30_evidence2.txt
stat -c '%s' evidence2.dd | tee -a ~/fng/evid/P30_evidence2.txt
```

- **Esperado segundo os autores:** a Fig. 2 indica "Length: 2 GB (2845109643 bytes)".
- **Justificativa:** é a entrada da execução de referência; sem ela não há comparação possível.
- **Evidência:** `evid/P30_evidence2.txt` e o registro de como o arquivo foi obtido (pedido aos autores, data, canal).
- **Sucesso:** arquivo com exatamente 2845109643 bytes.
- **Falha:** tamanho diferente; a comparação de offsets perde validade.
- **Interrupção:** arquivo indisponível. Marque C6 como não reproduzível por falta de dado e pule para P33.

### P31 — Reproduzir a execução da Fig. 2

- **Selo / reivindicação:** R / C6.
- **Diretório:** `~/fng/foremost-ng/src` (a Fig. 2 mostra execução em `src/`, com saída em `src/output` e configuração `src/foremost.conf`).
- **Comando** (artigo p. 8, Fig. 2: `./foremost-ng -v -x evidence2.dd`; a chave de P28 deve estar exportada):

```bash
cd ~/fng/foremost-ng/src && ls -d output 2>/dev/null && echo 'ATENCAO: mova ou apague src/output antes de seguir'
cd ~/fng/foremost-ng/src && ./foremost-ng -v -x ~/fng/dados/evidence2.dd 2>&1 | tee ~/fng/evid/P31_fig2.txt; echo "exit=${PIPESTATUS[0]}" | tee -a ~/fng/evid/P31_fig2.txt
cp output/audit.txt ~/fng/evid/P31_audit_fig2.txt
```

- **Esperado segundo os autores:** tabela como a da Fig. 2, com 12 arquivos (3 ELF, 1 script, 6 EXE, 2 ZIP), seus offsets e a coluna VT.
- **Evidência:** `evid/P31_fig2.txt`, `evid/P31_audit_fig2.txt`.
- **Sucesso:** `exit=0` e `audit.txt` com a tabela de arquivos.
- **Falha:** erro, nenhum arquivo ou travamento.
- **Interrupção:** travamento ou falta de memória; registre o erro e pule para P33.

### P32 — Comparar arquivos e offsets com a Fig. 2 \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** R / C6.
- **Diretório:** `~/fng`
- **Comando** (lista transcrita da Fig. 2; confira-a no PDF antes de usar):

```bash
cat > ~/fng/evid/P32_esperado_fig2.txt <<'EOF'
00004352.elf 2228224
00004820.elf 2467840
00005108.elf 2615296
00005492.script 2811904
00399884.exe 204740608
00405060.exe 207390720
00414932.exe 212445184
00428728.exe 219508736
00442520.exe 226570240
00447356.exe 229046272
01786101.zip 914484119
01787042.zip 914965615
EOF
grep -E '^ *[0-9]+: ' ~/fng/evid/P31_audit_fig2.txt | awk '{print $2, $5}' | sort > ~/fng/evid/P32_obtido.txt
sort ~/fng/evid/P32_esperado_fig2.txt | comm -23 - ~/fng/evid/P32_obtido.txt | tee ~/fng/evid/P32_faltantes.txt
sort ~/fng/evid/P32_esperado_fig2.txt | comm -13 - ~/fng/evid/P32_obtido.txt | tee ~/fng/evid/P32_extras.txt
```

- **Esperado segundo os autores:** os 12 nomes e offsets da Fig. 2. As contagens do VT podem mudar e não precisam coincidir (`reivindicacoes.md`, Critério de reprodução).
- **Justificativa:** os autores não descrevem como comparar; o critério vem de `reivindicacoes.md`.
- **Verificação manual:** abra uma linha de `P31_audit_fig2.txt` e confirme que a 5ª coluna é o offset (o tamanho ocupa duas colunas, como "57 KB"). Se não for, ajuste `$5` no `awk`.
- **Evidência:** `P32_esperado_fig2.txt`, `P32_obtido.txt`, `P32_faltantes.txt`, `P32_extras.txt`.
- **Sucesso:** `P32_faltantes.txt` vazio. Extras são registrados, mas não reprovam.
- **Falha:** qualquer linha em `P32_faltantes.txt`.
- **Interrupção:** nenhuma.

### P33 — Empacotar as evidências \[NÃO DOCUMENTADO\]

- **Selo / reivindicação:** F e R / todas.
- **Diretório:** `~/fng`
- **Comando:**

```bash
cd ~/fng && grep -rl "${VT_API_KEY:-CHAVE_AUSENTE}" evid/ && echo 'REMOVA A CHAVE DOS ARQUIVOS LISTADOS'
cd ~/fng && sha256sum evid/* > evid/SHA256SUMS && tar czf evidencias_foremost-ng.tgz evid montar.sh
```

- **Esperado segundo os autores:** não há.
- **Justificativa:** as instruções oficiais exigem prova de execução e saídas no parecer; o pacote com hashes torna as evidências verificáveis.
- **Evidência:** `evidencias_foremost-ng.tgz` e `evid/SHA256SUMS`.
- **Sucesso:** pacote criado e nenhum arquivo contendo a chave.
- **Falha:** a chave aparece em algum arquivo; remova-a e refaça o pacote.
- **Interrupção:** nenhuma.

## Tempo estimado

O roteiro completo leva cerca de 5 a 7 horas de trabalho ativo, sem contar a espera por `evidence2.dd`. As estimativas são do roteiro; os autores não informam tempos de execução.

| Bloco | Passos | Tempo ativo | Principal fonte de variação |
| --- | --- | --- | --- |
| Ambiente e compilação | P1–P8 | 30–45 min | Velocidade do apt e da rede |
| Teste mínimo F | P9–P11 | 20–30 min | Escolha e download da imagem DFTT |
| Ferramentas e script | P12–P13 | 15–20 min | Instalação do `python-evtx` |
| C1 — EVTX | P14–P16 | 30–45 min | Acesso a um Windows e cópia do arquivo |
| C2 — Scripts | P17–P19 | 15–20 min | — |
| C3 — Mach-O | P20–P22 | 30–45 min | Acesso a um macOS e cópia dos binários |
| C4 — ELF | P23–P25 | 15–20 min | Disponibilidade do `gcc-multilib` |
| C5 — VirusTotal | P26–P29 | 30–60 min | Criação da conta, limite de requisições e eventual reenvio de arquivo |
| C6 — Fig. 2 | P30–P32 | 45–90 min | Obtenção de `evidence2.dd` (espera não contada), leitura de \~2,7 GB e 12 consultas ao VT |
| Encerramento | P33 | 10 min | — |

## Tabela com todos os passos

Dos 33 passos, 15 seguem procedimento dos autores, 2 só em parte (P2 e P9) e 16 são \[NÃO DOCUMENTADO\]. Os comandos completos estão nas seções acima.

| ID | Selo | Reivindicação | Diretório | Documentação | Ação | Evidência principal | Interrompe se |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | F, R | todas | `~` | NÃO DOCUMENTADO | Registrar ambiente | `P1_ambiente.txt` | Big-endian ou disco < 20 GB |
| P2 | F | todas | `~/fng` | Dockerfile (versões: ND) | Instalar dependências | `P2_versoes.txt` | Pacote não instalável |
| P3 | F | todas | `~/fng` | Artigo p. 6, Dockerfile | Clonar repositório | `P3_clone.txt` | Sem clone e sem ZIP |
| P4 | F, R | todas | `~/fng/foremost-ng` | NÃO DOCUMENTADO | Fixar commit `bb812a22` | `P4_commit.txt` | Commit inexistente e sem ZIP |
| P5 | F | — | `~/fng/foremost-ng` | Artigo p. 6 | `make` na raiz | `P5_make_raiz.txt` | Não interrompe |
| P6 | F | todas | `…/src` | README, Dockerfile | `make` em `src/` | `P6_make.txt` | Sem binário: encerra tudo |
| P7 | F | todas | `…/src` | README, artigo p. 6 | `sudo make install` | `P7_install.txt` | Não interrompe |
| P8 | F | — | `~/fng` | README, artigo p. 7 | Ajuda, versão, manual | `P8_ajuda.txt` | Não interrompe |
| P9 | F | — | `~/fng/dados/dftt` | Artigo p. 6 (imagem: ND) | Baixar imagem DFTT | `P9_hashes.txt` | Não interrompe |
| P10 | F | — | `~/fng` | Artigo p. 7 | `-i` e `-o` | `P10_audit.txt` | Travamento |
| P11 | F | — | `~/fng` | Artigo p. 7 | `-t evtx,elf,exe` | `P11_subdirs.txt` | Travamento |
| P12 | R | C1, C3, C4, C5 | `~/fng` | NÃO DOCUMENTADO | Ferramentas de verificação | `P12_ferramentas.txt` | Não interrompe |
| P13 | R | C1–C5 | `~/fng` | NÃO DOCUMENTADO | Script de montagem | `P13_montar.sh` | Erro de sintaxe |
| P14 | R | C1 | Windows / `amostras/c1` | NÃO DOCUMENTADO | Exportar `.evtx` | `P14_hash_windows.txt` | Sem Windows |
| P15 | R | C1 | `~/fng` | Artigo p. 7 | Montar e `-t evtx` | `P15_audit_c1.txt` | Travamento |
| P16 | R | C1 | `~/fng` | NÃO DOCUMENTADO | Ler EVTX e contar eventos | `P16_c1_comparacao.txt` | Não interrompe |
| P17 | R | C2 | `amostras/c2` | NÃO DOCUMENTADO | Criar scripts e controles | `P17_mapa_c2.tsv` | Erro na montagem |
| P18 | R | C2 | `~/fng` | Artigo p. 7 | `-t script` | `P18_audit_c2.txt` | Travamento |
| P19 | R | C2 | `~/fng` | NÃO DOCUMENTADO | Conferir positivos e negativos | `P19_c2_resultado.txt` | Não interrompe |
| P20 | R | C3 | macOS / `amostras/c3` | NÃO DOCUMENTADO | Obter fat e thin | `P20_lipo_info.txt` | Sem macOS |
| P21 | R | C3 | `~/fng` | Artigo p. 7 | Montar e `-t macho` | `P21_audit_c3.txt` | Travamento |
| P22 | R | C3 | `~/fng` | NÃO DOCUMENTADO | `file` nos Mach-O | `P22_c3_resultado.txt` | Não interrompe |
| P23 | R | C4, C5 | `amostras/c4` | NÃO DOCUMENTADO | Criar ELF32 e ELF64 | `P23_mapa_c4.tsv` | Não interrompe |
| P24 | R | C4 | `~/fng` | Artigo p. 7 | `-t elf` | `P24_audit_c4.txt` | Travamento |
| P25 | R | C4 | `~/fng` | NÃO DOCUMENTADO | `readelf` nos ELF | `P25_c4_resultado.txt` | Não interrompe |
| P26 | R | C5 | navegador | README | Obter chave VT | anotação no parecer | Sem chave: só P27 |
| P27 | R | C5 | `~/fng` | Artigo p. 7 | `-x` sem chave | `P27_audit_c5_sem.txt` | Travamento |
| P28 | R | C5 | `~/fng` | Artigo p. 7, README | `-x` com chave | `P28_audit_c5_com.txt` | Rede indisponível |
| P29 | R | C5 | `saidas/c5_com/elf` | NÃO DOCUMENTADO | Conferir rótulos na API | `P29_vt_direto.txt` | HTTP 429 |
| P30 | R | C6 | `~/fng/dados` | NÃO DOCUMENTADO | Obter `evidence2.dd` | `P30_evidence2.txt` | Arquivo indisponível: C6 não reproduzível |
| P31 | R | C6 | `…/src` | Artigo p. 8, Fig. 2 | `./foremost-ng -v -x evidence2.dd` | `P31_audit_fig2.txt` | Travamento ou falta de memória |
| P32 | R | C6 | `~/fng` | NÃO DOCUMENTADO | Comparar com a Fig. 2 | `P32_faltantes.txt` | Não interrompe |
| P33 | F, R | todas | `~/fng` | NÃO DOCUMENTADO | Empacotar evidências | `evidencias_foremost-ng.tgz` | Não interrompe |

**Regra de decisão:** F se P6, P10 e P11 tiverem sucesso. R só se C1–C6 forem reproduzidas (`reivindicacoes.md`, Regra para o selo R); uma reivindicação não verificada impede R.
