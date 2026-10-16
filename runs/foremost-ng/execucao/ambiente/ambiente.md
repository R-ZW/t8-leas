# Ambiente da execução de referência — Foremost-NG

**Preparado em:** 16/10/2026 01:35–01:50 UTC (15/10/2026, noite, America/Sao_Paulo). **Escopo:** só o ambiente; nada do artefato foi compilado ou executado nesta preparação (o teste do gravador usou `echo`, `uname`, `sh -c "echo …"`, `false` e `cp -p`).

## Escolha da versão do sistema

- O [README no SHA fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md), conferido no `pacote/artefato.zip` (SHA-256 `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a`), diz apenas que a ferramenta é “Linux-based” e dá a seção “### Linux” (`cd foremost-ng-<version>/src`, `make`, `sudo make install`). **Não fixa distribuição nem versão.** O artigo (p. 6, §4) diz “compile with a standard GCC toolchain” em “a Unix-like system”, também sem versão.
- O `Dockerfile` do próprio artefato usa `FROM ubuntu:latest`, sem versão fixada. Ele **não** foi usado como base desta imagem (é parte do artefato e pode virar passo de plano).
- **Escolha:** Ubuntu 24.04 LTS (noble), a LTS vigente na data do commit fixado (08/07/2025 19:00:20 UTC) e na data do SBSeg 2025. Para aproximar o estado de 2025:
  - imagem base com a **última tag datada anterior ao commit**: `ubuntu:noble-20250619` (criada em 19/06/2025 23:16:36 UTC);
  - índice apt fixado no **snapshot do arquivo Ubuntu no instante do commit**: `APT::Snapshot "20250708T190020Z"` ([snapshot.ubuntu.com](https://snapshot.ubuntu.com/)), com cada pacote também fixado por versão no `Dockerfile`.

## Imagem

| Item | Valor |
|---|---|
| Base (índice multiplataforma) | `docker.io/library/ubuntu:noble-20250619@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076` |
| Base (manifesto linux/amd64) | `sha256:dbdff34bb41cecdb07c79af373b44bb4c9ccba2520f014221fb95845f14bc6c1` |
| Snapshot apt | `20250708T190020Z` |
| Imagem construída | `t8/foremost-ng-ref:noble-20250619-snap20250708` |
| ID da imagem construída | `sha256:795118adb63a3010f78956bb381d8cdb3633833266ec909b896268e86328f0f7` (128.509.168 bytes, 8 camadas, criada 2026-10-16T01:38:53Z) |
| SHA-256 do `Dockerfile` | `f8470addef7cf85ab257ca2d99bc5beab87df8a18ba08cafa28052c5280ee224` |
| Saída completa do build | [`construcao-imagem.txt`](construcao-imagem.txt) |
| Lista integral de pacotes (dpkg) | [`pacotes-dpkg.txt`](pacotes-dpkg.txt) (161 pacotes) |
| Versões coletadas no contêiner | [`versoes-contenedor.txt`](versoes-contenedor.txt) |

Reconstrução: na pasta `ambiente/`, `docker build -t t8/foremost-ng-ref:noble-20250619-snap20250708 .`. O ID pode mudar em nova construção (carimbos de tempo das camadas); as versões dos pacotes não, por causa do snapshot e da fixação por versão.

## Pacotes instalados e origem de cada um

`--no-install-recommends` em todos os passos; dependências obrigatórias vêm automaticamente (lista completa em `pacotes-dpkg.txt`).

| Pacote = versão | Por quê | Fonte |
|---|---|---|
| `gcc=4:13.2.0-7ubuntu1`, `gcc-13=13.3.0-6ubuntu2~24.04` | compilador | `src/Makefile` (`RAW_CC = gcc`); artigo p. 6 (“standard GCC toolchain”) |
| `make=4.3-4.1build2` | build | README, “### Linux”: `make` |
| `libssl-dev=3.0.13-0ubuntu3.5` | cabeçalhos/libs OpenSSL | `src/Makefile` (Linux: `LINK_OPT += -lssl -lcrypto -lcurl`); README cita OpenSSL só na seção macOS |
| `libcurl4-openssl-dev=8.5.0-2ubuntu10.6` | cabeçalhos/libs libcurl | `src/Makefile` (`-lcurl`); README cita `curl` só na seção BSD |
| `git=1:2.43.0-1ubuntu7.3` | obter o código por clone | README (“Clone or download”); artigo p. 6 (`git clone …`) |
| `sudo=1.9.15p5-3ubuntu5.24.04.1` | instalar como o README manda | README e artigo: `sudo make install` |
| `man-db=2.12.0-4build2` | ler a página de manual | README (“refer to the manual page: `man foremost-ng`”); artigo p. 7 |
| `ca-certificates=20240203` | TLS de apt (snapshot só por HTTPS), `git clone` e chamadas HTTPS | infraestrutura; não listado pelo README |
| `unzip=6.0-28ubuntu4.1` | abrir `pacote/artefato.zip` | instrumentação do registro; não é dependência do artefato |

O README e o artigo **não** nomeiam pacotes Linux; os nomes `libssl-dev` e `libcurl4-openssl-dev` são os da distribuição para as bibliotecas que o `Makefile` liga. Fato de referência: o `Dockerfile` do artefato instala `gcc make git libssl-dev libcurl4-openssl-dev` (sem versões).

### Ajustes de imagem (não são pacotes)

1. **Bootstrap TLS:** a base não traz certificados e o snapshot só responde por HTTPS; apenas o passo que instala `ca-certificates` usa `Acquire::https::Verify-Peer=false`. A autenticidade dos índices/pacotes continua verificada pelas assinaturas GPG do apt; os passos seguintes usam TLS verificado.
2. **`man` real:** a imagem minimizada desvia `/usr/bin/man` para um aviso; o `Dockerfile` remove o desvio (mesmo procedimento do `unminimize`). As páginas de manual de outros pacotes continuam excluídas pela configuração `excludes` da base; a de `foremost-ng` é copiada por `make install` com `install`, fora do dpkg.
3. **Usuário:** `revisor` (uid 1001), com `sudo` sem senha, porque README e artigo usam `sudo make install`. O contêiner inicia como `revisor` em `/home/revisor`.
4. `script` (util-linux 2.39.3) já faz parte da base (`bsdutils`); nada foi instalado para o gravador além de `unzip`.

Nenhuma chave VirusTotal foi colocada na imagem.

## Ambiente medido

### Contêiner (coletado em 2026-10-16T01:39:29Z)

| Item | Valor |
|---|---|
| SO | Ubuntu 24.04.2 LTS (noble), x86_64 |
| Kernel (do host WSL2) | `Linux 6.18.33.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 18 21:54:43 UTC 2026 x86_64` |
| CPU visível | 13th Gen Intel(R) Core(TM) i5-13450HX, 16 CPUs lógicas (8 núcleos × 2 threads no lscpu da VM), hypervisor Microsoft |
| RAM visível | 8.161.746.944 bytes (≈7,6 GiB; limite padrão do WSL2, sem `.wslconfig`) + swap 2 GiB |
| Disco | `overlay` 1007G, 952G livres (disco virtual `docker_data.vhdx` no C:) |
| gcc | `gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0` |
| make | `GNU Make 4.3` |
| OpenSSL | `OpenSSL 3.0.13 30 Jan 2024` (pacotes `libssl3t64`/`libssl-dev` 3.0.13-0ubuntu3.5) |
| libcurl | `libcurl 8.5.0`, backend `OpenSSL v3+` (pacotes `libcurl4t64`/`libcurl4-openssl-dev` 8.5.0-2ubuntu10.6) |
| glibc / binutils | `GLIBC 2.39-0ubuntu8.4` / `GNU ld 2.42` |
| git / sudo / man | 2.43.0 / 1.9.15p5 / man-db 2.12.0 |
| bash / script / unzip | 5.2.21 / util-linux 2.39.3 / UnZip 6.00 |

### Host

| Item | Valor |
|---|---|
| SO | Microsoft Windows 11 Home 10.0.26300 (build 26300) |
| CPU | 13th Gen Intel(R) Core(TM) i5-13450HX, 10 núcleos, 16 threads |
| RAM | 15,69 GiB |
| Discos | NX-1TB 2280 (954 GB; volume D:, 674 GiB livres) e ADATA SM2P41C3 NVMe 256GB (238 GB; volume C:, 69 GiB livres) |
| WSL | 2.7.13.0, kernel 6.18.33.2-2 |
| Docker | Docker Desktop 4.90.0; Engine 29.7.2 (cliente e servidor), linux/amd64, storage `overlayfs` |

## Atende aos requisitos do README?

- README: “Linux-based” e procedimento “### Linux” → o contêiner é Linux (Ubuntu 24.04, x86_64). Distribuição/versão não são exigidas pelo README.
- Ferramentas usadas nos comandos do README (`tar`, `make`, `sudo`, `man`) e bibliotecas ligadas pelo `Makefile` (`ssl`, `crypto`, `curl`) estão presentes.
- **Diferença registrada:** é contêiner Docker sobre kernel WSL2, não VM Ubuntu dedicada (VirtualBox não está instalado nesta máquina). O kernel é compartilhado com o host WSL2 e não é o kernel Ubuntu da distribuição.
- A observação em README sobre glibc < 2.2.0 não se aplica (glibc 2.39).

## Como usar na execução (ainda não executado)

```bash
docker run --rm -it --name fn-ref \
  -v "D:/Lab-artefatos/t8-leas/runs/foremost-ng/execucao:/execucao" \
  -v "D:/Lab-artefatos/t8-leas/runs/foremost-ng/pacote:/pacote:ro" \
  t8/foremost-ng-ref:noble-20250619-snap20250708
# dentro do contêiner:
bash /execucao/ambiente/gravar-sessao.sh sessao /execucao/sessao-AAAAMMDD
# na sessão gravada, cada passo:
passo P01 -- unzip -q /pacote/artefato.zip -d ~/trabalho
```

No Git Bash, prefixar `MSYS_NO_PATHCONV=1` ao `docker run` para o `-v` não ser convertido. Recomenda-se trabalhar em `/home/revisor` (sistema de arquivos do contêiner) e copiar evidências para `/execucao/…`.

## Gravador de sessão (`gravar-sessao.sh`)

- `sessao DIR [COMANDO]`: `script -q -f -a -E never -T DIR/tempo.txt DIR/terminal.txt`, com cabeçalho de hora UTC, host, SO e usuário; prompt com hora ISO e código do último comando; histórico com carimbo em `DIR/historico.txt` (só em uso interativo; com `COMANDO` não há histórico). Reprodução: `scriptreplay -T DIR/tempo.txt DIR/terminal.txt`.
- `passo ID [-w DIR]… -- COMANDO`: grava em `$REG_DIR/passos.tsv` id, início/fim UTC, duração, código de saída, diretório e comando (com aspas do shell); saída em `passos/ID.saida.txt`; `sha256sum` dos arquivos criados/alterados (ctime posterior ao início) em `passos/ID.sha256`. Retorna o código do comando.
- Nenhum nome termina em `.log` (o `.gitignore` da raiz ignora `*.log`).

### Teste do gravador (2026-10-16T01:39:59Z e 01:40:11Z)

Evidência em [`teste-gravar-sessao/`](teste-gravar-sessao/). O teste usou a versão do script com SHA-256 `3df676b76dd1fa517a0a8fbe15da497fced19def97986ebc0b9b7c65c1172f8c`; depois dele, só mudou a faixa de linhas impressa pela ajuda (`sed -n '2,27p'` → `'2,25p'`), resultando na versão atual `70c1b6cfefac2e97db8545c95a10dcdbab712414be8855fd0ed20e3abdb9c24a`.

| Passo | Comando | Código | Arquivos registrados |
|---|---|---|---|
| 01 | `echo ola` | 0 | 0 |
| 02 | `uname -a` | 0 | 0 |
| 03 | `sh -c "echo conteudo > arquivo-teste.txt"` | 0 | 1 (`30e58096…8aef8d`) |
| 04 | `false` | 1 (propagado) | 0 |
| 05 | `cp -p antigo.txt copia-mtime-antigo.txt` (mtime 2001) | 0 | 1 (cópia detectada apesar do mtime antigo) |
| 06 | `sh -c "echo y > no-montado.txt"` na pasta montada do Windows | 0 | 1 (`3bb2abb6…e90877`) |

Passos 01–04 rodaram dentro de `sessao` (gravados em `terminal.txt`/`tempo.txt`; `scriptreplay` reproduziu sem erro). Passos 05–06 rodaram fora de `sessao`, só para testar a detecção de arquivos. Os caminhos `/home/revisor/teste/…` dos passos 01–05 existiam só no contêiner descartado.
