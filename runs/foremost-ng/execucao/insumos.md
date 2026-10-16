# Insumos externos — Foremost-NG

**Consultas:** 16/10/2026, 01:38–01:48 UTC (15/10/2026, 22:38–22:48 em America/Sao_Paulo). Complementa [`../versao.md`](../versao.md) (seção “Figura 2 e `evidence2.dd`”), sem repeti-lo. Horários abaixo em UTC, tirados do relógio da máquina no momento de cada requisição.

## 1. Busca de `evidence2.dd` (protocolo §4.5)

| Hora (UTC) | Fonte | Consulta / URL | Resultado |
|---|---|---|---|
| 01:40:33 | Zenodo (API) | [`q="evidence2.dd"`](https://zenodo.org/api/records?q=%22evidence2.dd%22&size=20) | 0 registros |
| 01:41:01 | Zenodo (API) | [`q=foremost-ng`](https://zenodo.org/api/records?q=foremost-ng&size=20) | conexão reiniciada pelo servidor (sem resposta) |
| 01:43:31 | Zenodo (API) | mesma consulta, repetida | 21.814 registros por termos soltos (“foremost”, “ng”); os 20 primeiros não tratam da ferramenta |
| 01:44:21 | Zenodo (API) | [`q="Foremost-NG"`](https://zenodo.org/api/records?q=%22Foremost-NG%22&size=20) (frase exata) | 0 registros |
| 01:41:29 | Zenodo (API) | [`q="foremost" AND "virustotal"`](https://zenodo.org/api/records?q=%22foremost%22%20AND%20%22virustotal%22&size=20) | 0 registros |
| 01:42:05 | Zenodo (API) | [`q=creators.name:"Souza, Cristian"`](https://zenodo.org/api/records?q=creators.name:%22Souza%2C%20Cristian%22&size=20) | 0 registros |
| 01:42:57 | GitHub releases | [API releases](https://api.github.com/repos/cristianzsh/foremost-ng/releases?per_page=100) | 1 release, `v1.5.7` (22/05/2025), **sem arquivos anexados** |
| 01:42:58 | GitHub issues/PRs | [API issues, `state=all`](https://api.github.com/repos/cristianzsh/foremost-ng/issues?state=all&per_page=100) | 1 item: [issue #1 “Windows binary”](https://github.com/cristianzsh/foremost-ng/issues/1), aberta em 27/12/2025 por terceiro, pede binário para Windows; nenhum PR |
| 01:43:31 | GitHub issue #1 | [comentários](https://api.github.com/repos/cristianzsh/foremost-ng/issues/1/comments) | 0 comentários |
| 01:42:59 | GitHub repositório | [API repo](https://api.github.com/repos/cristianzsh/foremost-ng), [`commits/main`](https://api.github.com/repos/cristianzsh/foremost-ng/commits/main), [branches](https://api.github.com/repos/cristianzsh/foremost-ng/branches) | último push 2025-07-08T19:00:27Z; `main` = `bb812a22…` (única branch) |
| 01:43:02 | GitHub forks | [API forks](https://api.github.com/repos/cristianzsh/foremost-ng/forks?per_page=100) | 0 forks |
| 01:45:16 | GitHub wiki | [github.com/cristianzsh/foremost-ng/wiki](https://github.com/cristianzsh/foremost-ng/wiki) | devolve a página principal do repositório (wiki sem páginas) |
| 01:43:02 | GitHub, repositórios do autor | [API repos de `cristianzsh`](https://api.github.com/users/cristianzsh/repos?per_page=100&sort=updated) | nenhum repositório de dados/imagens; por nome, só `forensictools`, `mxray`, `uareport`, `malware-research` e o próprio `foremost-ng` têm relação temática |
| 01:45:32 | GitHub `forensictools` | [API contents](https://api.github.com/repos/cristianzsh/forensictools/contents) | raiz: `CHANGELOG.md`, `LICENSE`, `README.md`, `build.ps1`, `docs`, `src`; nenhuma imagem `.dd` |
| 01:45:29 | GitHub, busca global de issues | [`"evidence2.dd"`](https://api.github.com/search/issues?q=%22evidence2.dd%22) | 1 resultado **sem relação** com o Foremost-NG: [Akshay473/forensic-pro-suite#244](https://github.com/Akshay473/forensic-pro-suite/issues/244) (28/05/2026), que usa `evidence1.dd`/`evidence2.dd` como nomes genéricos em exemplo de `curl` |
| 01:45:29 | GitHub, busca de código | [`"evidence2.dd"`](https://api.github.com/search/code?q=%22evidence2.dd%22) | **não realizada**: HTTP 401, a API exige autenticação (não há `gh` autenticado nesta máquina) |
| 01:45:30 | GitHub, busca de repositórios | [`foremost-ng`](https://api.github.com/search/repositories?q=foremost-ng) | 3 resultados; só `cristianzsh/foremost-ng` é a ferramenta |
| 01:42:47 | Apresentação do autor | [sbseg2025foremostng.pdf](https://cristian.sh/files/talks/sbseg2025foremostng.pdf) | HTTP 200, 367.606 bytes, SHA-256 `ed0eb159b51af97d90d19da0fb56599ba121360f6f1ec3de2d72bef446097d3d`, 23 páginas. O texto extraível (pdftotext) não contém `evidence2`, `.dd`, DFTT, Zenodo, link de dados nem hash de imagem; links presentes: tarball do Foremost 1.5.7, issue do Foremost original, documentação VirusTotal e o `git clone` do repositório. A menção a `evidence2.dd` registrada em `versao.md` está na captura de tela do slide 21 (imagem), não no texto |
| 01:45:31 | Site do autor | [cristian.sh](https://cristian.sh/) e [files.html](https://cristian.sh/files.html) (01:45:43) | só a lista de apresentações (incl. `sbseg2025foremostng.pdf`); nenhuma ocorrência de `evidence2` nem link de dados. [`/talks/`](https://cristian.sh/talks/) responde 404 |
| 01:43:02 | Vídeo do autor | [youtube.com/watch?v=RXGGKduSzJ0](https://www.youtube.com/watch?v=RXGGKduSzJ0), via `curl` | HTTP 429 (limite de requisições) |
| 01:43:08 | Vídeo do autor | [oEmbed](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=RXGGKduSzJ0&format=json) | título “Demo: Foremost-NG”, autor “Cristian Souza”; o oEmbed não traz a descrição |
| 01:43:16 | Vídeo do autor | mesma URL no navegador embutido | redirecionado para a página de verificação anti-robô do Google (`google.com/sorry`); **não contornada**, e a descrição não foi lida nesta consulta. Para a descrição, vale o registro anterior em `versao.md` |
| 01:45:58 | Página do artigo na SBC (SOL) | [sol.sbc.org.br/…/article/view/36737](https://sol.sbc.org.br/index.php/sbseg_estendido/article/view/36737) | DOI `10.5753/sbseg_estendido.2025.12307`; único arquivo é o PDF do artigo (`36737/36523`); sem material suplementar |
| ~01:46 | Buscador web | `"evidence2.dd" foremost-ng`; `Foremost-NG SBSeg 2025 artefato evidence2.dd imagem disco` | nenhum resultado com a imagem; só a página da SBC e tutoriais genéricos do Foremost original com `evidence.dd` |

**Resultado:** `evidence2.dd` **não foi localizado** em nenhuma fonte pública consultada. Lacuna desta busca: a busca de código do GitHub não foi feita (exige autenticação), e a descrição do vídeo não foi relida hoje. O rascunho de pedido aos autores está em [`mensagem-autores.md`](mensagem-autores.md) (não enviado).

## 2. Imagens DFTT para o teste externo D3

Fonte: [dftt.sourceforge.net](https://dftt.sourceforge.net/) (índice consultado às 01:38:15; páginas dos testes às 01:38:23–24). O artigo (p. 7, §4) indica o DFTT apenas de forma genérica. **Rótulo obrigatório no registro: D3 (teste externo).** Nenhuma destas imagens é `evidence2.dd` ou substitui a Fig. 2 (C6).

| Teste | Conteúdo | Gabarito publicado | Situação |
|---|---|---|---|
| [#11 Basic Data Carving Test #1](https://dftt.sourceforge.net/test11/index.html) | FAT32, 15 arquivos (DOC, WAV, JPEG, XLS, PDF, GIF, MOV, WMV, PPT, ZIP), alocados e apagados, 1 JPEG com cabeçalho corrompido, setor de boot corrompido | sim: nome, MD5, tamanho, setores | **baixada**; é a imagem usada na T7 |
| [#12 Basic Data Carving Test #2](https://dftt.sourceforge.net/test12/index.html) | ext2, 10 arquivos (BMP, DOC, JPEG, PDF, GIF, XLS, PPT), com blocos indiretos no meio dos arquivos, superbloco corrompido | sim: nome, MD5, tamanho, setores incl. blocos (IND)/(DIND) | **baixada** |
| [#13 Windows Memory Analysis #1](https://dftt.sourceforge.net/test13/index.html) | 2 imagens de memória (Windows 2003 SP0 e Windows 2000 SP0, 1 GB cada) | **não** há lista de arquivos esperados para carving; só a nota do offset do bloco EPROCESS “correto” (win2k) | **baixada**; serve apenas para observação exploratória de executáveis PE em memória, sem comparação com gabarito |
| [#8 JPEG Search Test #1](https://dftt.sourceforge.net/test8/index.html) | NTFS, 10 JPEGs em situações variadas | sim (MD5) | não baixada: só JPEG, coberto por #11/#12 |
| #1–#7, #9, #10, #14 | testes de partição, busca por palavra, undelete, rótulo de volume, ISO9660 | — | não são testes de carving |

Fatos relevantes para C1–C4: **nenhum gabarito DFTT lista ELF, Mach-O, EVTX ou script com shebang.** As únicas imagens com executáveis Windows (PE) são as de memória do #13, sem gabarito de arquivos. Os insumos sintéticos usados na T7 para o teste de script (98 bytes) e de ELF (2.648 bytes; extraído com 1.956 bytes lá) **não** estão preservados em `D:\Lab-artefatos\tarefa7` (busca por tamanho e nome em 16/10/2026); repetir esse teste em Ubuntu, como pede o protocolo §12, exigirá recriar e registrar a entrada.

### Downloads

Registro bruto em [`insumos/downloads.txt`](insumos/downloads.txt) (hora, URL pedida, código HTTP, bytes e espelho final). Manifestos: [`insumos/SHA256SUMS.txt`](insumos/SHA256SUMS.txt) e [`insumos/MD5SUMS.txt`](insumos/MD5SUMS.txt). Os binários ficam fora do Git ([`insumos/.gitignore`](insumos/.gitignore)); as páginas HTML dos testes são versionadas como `pagina-test1N.html`.

| Arquivo | URL pedida (hora UTC) | Bytes | SHA-256 | MD5 |
|---|---|---|---|---|
| `dftt-11/11-carve-fat.zip` | `https://prdownloads.sourceforge.net/dftt/11-carve-fat.zip?download` (01:39:12) | 11.596.213 | `0c5e850a29f5811a4861a8d75404f7c45ab1b4526981414c7f86d223d5a71b67` | `138e9deb392ff4d17dfb01078e7ce28e` |
| ↳ `11-carve-fat/11-carve-fat.dd` | extraído do zip | 64.979.456 | `83585232e908529286f1ff04c43b4d858604875c733183a9e3b44a07ff818d26` | `0069813c892a462f88dc6d376624f7d9` = MD5 publicado ✔ |
| `dftt-12/12-carve-ext2.zip` | `https://prdownloads.sourceforge.net/dftt/12-carve-ext2.zip?download` (01:39:26) | 1.101.117 | `826c24466f2d7f949e2be5cfa6943c9e056faeb60a65fef2356516b06254481e` | `b0c10dc8de7c3f1c2f9cc2a71e69b985` |
| ↳ `12-carve-ext2/12-carve-ext2.dd` | extraído do zip | 129.356.800 | `ffeb78b6cf8eed64c241212fb5cd1f3d226dcd58e16b67192f465e4a3ec46342` | `6cbd2c5248fa7030d699eb6cde051623` = MD5 publicado ✔ |
| `dftt-13/boomer-win2003.zip` | `https://downloads.sourceforge.net/dftt/boomer-win2003.zip` (01:39:28) | 38.892.469 | `97986c9db2ec47e4ed87579b8c1b0fcd42ecf5173c45da7d3db4ae147738cfcd` | `e7685030a01b2bd0485d8bc5479f1e3e` |
| ↳ `boomer-win2003/boomer-win2003-2006-03-17.img` | extraído do zip | 1.065.246.720 | `dc7022c2183dade6c36ebf19c74af5234bff8800e2a6f95e825287da9a214adb` | `8caa17c3d30aadff223f044ee7cf60f0` (sem MD5 publicado) |
| `dftt-13/boomer-win2k.zip` | `https://downloads.sourceforge.net/dftt/boomer-win2k.zip` (01:42:21) | 89.230.163 | `f23c37bf45573140351bcba6d894e8418cd68f9f0f3944d6ef679e0751cc406c` | `be7d87f604e190e9a835f10c9a3040f9` |
| ↳ `boomer-win2k/boomer-win2k-2006-02-27-0824.img` | extraído do zip | 1.065.246.720 | `9489bb8af1d9e1bc861f51180368de7410e92edf0c5294b302a00a11b9e9094d` | `f7317e7388f8d4c0c12832ed62920ef5` (sem MD5 publicado) |

Os zips #11 e #12 trazem também `README.txt`, `COPYING-GNU.txt` (GPL) e o HTML do gabarito; o HTML embutido é **byte a byte igual** à página online baixada hoje (#11: SHA-256 `d75582718f3a…dd432de3`; #12: `c3b21c210240…8e8f42821a4`). Os zips #13 trazem só a imagem e um `README.txt`.

## 3. Gabaritos oficiais transcritos

### DFTT #11 — Basic Data Carving Test #1 (Nick Mikus, 14/03/2005)

Imagem `raw` de FAT32, 62 MB (11 MB compactada), MD5 da imagem `0069813c892a462f88dc6d376624f7d9`, licença GPL. Setor de boot corrompido de propósito (a imagem não monta). “Sectors” = (setores do arquivo) setores da imagem.

| Nº | Nome | MD5 | Tamanho (bytes) | Nota | Setores |
|---|---|---|---|---|---|
| 1 | 2003_document.doc | e72f388b36f9370f19696b164c308482 | 19968 | A Valid DOC file | (0-38) 281-320 |
| 2 | enterprise.wav | 7629b89adade055f6783dc1773274215 | 318895 | A valid WAV file | (0-622) 16021-16644 |
| 3 | haxor2.jpg | 84e1dceac2eb127fef5bfdcb0eae324b | 24367 | An invalid JPEG with only 1 header byte corrupted. This byte is located at offset 19 within the file. | (0-47) 16645-16692 |
| 4 | holly.xls | 7917baf0219645afef8b381570c41211 | 23040 | A valid XLS file | (0-44) 16693-16738 |
| 5 | lin_1.2.pdf | e026ec863410725ba1f5765a1874800d | 1399508 | A linearized PDF | (0-2733) 16741-19475 |
| 6 | nlin_14.pdf | 5b3e806e8c9c06a475cd45bf821af709 | 122434 | A non-linearized PDF | (0-239) 19477-19716 |
| 7 | paul.jpg | 37a49f97ed279832cd4f7bd002c826a2 | 29885 | A valid jpeg | (0-58) 19717-19776 |
| 8 | pumpkin.jpg | 6c9859e5121ff54d5d6298f65f0bf3b3 | 444314 | A valid EXIF jpeg | (0-867) 19777-20644 |
| 9 | shark.jpg | d83428b8742a075b57b0dc424cd297c4 | 99298 | A valid JPEG | (0-193) 20645-20839 |
| 10 | sm1.gif | d25fb845e6a41395adaed8bd14db7bf2 | 5498 | A valid GIF | (0-10) 20841-20852 |
| 11 | surf.mov | 5328d2b066f428ea95b2793849ab97fa | 550653 | A valid MOV | (0-1075) 20853-21928 |
| 12 | surf.wmv | ff085d0c4d0e0fdc8f3427db68e26266 | 1036994 | A valid WMV | (0-2025) 21929-23955 |
| 13 | test.ppt | 7b74c2c608d92f4bb76c1d3b6bd1decc | 11264 | A deleted PPT | (0-21) 23957-23978 |
| 14 | wword60t.zip | c0be59d49b7ee0fdc492d2df32f2c6c6 | 78899 | A valid ZIP | (0-154) 23981-24135 |
| 15 | domopers.wmv | 63c0c6986cf0a446cb54b0ac65a921a5 | 8037267 | A deleted wmv | (0-15697) 321-16018 |

Nota de transcrição: no HTML, as células MD5 dos itens 2 e 10 terminam com um caractere não ASCII (provável espaço não separável); foi omitido.

### DFTT #12 — Basic Data Carving Test #2 (Nick Mikus, 14/03/2005)

Imagem `raw` de ext2, 124 MB (1,1 MB compactada), MD5 da imagem `6cbd2c5248fa7030d699eb6cde051623`, licença GPL. Superbloco corrompido de propósito. Setores marcados (IND)/(DIND) são blocos de ponteiros indiretos/duplamente indiretos intercalados no conteúdo.

| Nº | Nome | MD5 | Tamanho (bytes) | Nota | Setores |
|---|---|---|---|---|---|
| 1 | haxor2.bmp | f9633fe6b9ef2a0a5edd6de70d22c0f5 | 163878 | A deleted BMP | (0-22):5162-5184, (IND):5186, (24-320):5188-5484 |
| 2 | jimmy.doc | 2f3f914dd74819df42d1d941c7275c16 | 12800 | A deleted DOC | (0-22):5486-5508, (IND):5510, (24):5512 |
| 3 | jn.jpg | 270a0a913fa9603db8121fdf78d63aca | 28949 | A valid JPG | (0-22):5514-5536, (IND):5538, (24-56):5540-5572 |
| 4 | lin_test.pdf | 1c64456776075d1f0a662e1f6c09e340 | 26618 | A valid PDF | (0-22):5574-5596, (IND):5598, (24-50):5600-5626 |
| 5 | main_dive.jpg | 937846adb96773ee25fcb34821230976 | 8463 | A valid jpeg | (0-16):5628-5644 |
| 6 | n_lin_ss.pdf | 97be95ed3e710b63bc75e5c0775062d9 | 734652 | A valid pdf | (0-22):5646-5668, (IND):5670, (24-534):5672-6182, (DIND):6184, (IND):6186, (536-1046):6188-6698, (IND):6700, (1048-1434)6702-7088 |
| 7 | blogo.gif | 5e10b2176016885a85bffc074a142524 | 18663 | A valid gif | (0-22):5122-5144, (IND):5146, (24-36):5148-5160 |
| 8 | sherry.jpg | 3834e72d2ee266ccfb9733d716b89f2b | 133249 | A valid JPEG | (0-22):7090-7112, (IND):7114, (24-260):7116-7352 |
| 9 | stats.xls | 6351df9c1543c41c3df8eea63e06a219 | 15360 | A valid XLS | (0-22):7354-7376, (IND):7378, (24-28):7380-7384 |
| 10 | test.ppt | 99941c129cc8cfbadc15c55086982efc | 17408 | A valid PPT | (0-22):7386-7408, (IND):7410, (24-32):7412-7420 |

### DFTT #13 — Windows Memory Analysis #1 (Jesse Kornblum, ManTech; 06/01/2007)

Sem tabela de arquivos esperados. Conteúdo publicado (página e `README.txt` de cada zip):

- `boomer-win2003`: Windows 2003 SP0, máquina isolada “Boomer”, não ativado, executando Notepad; 1 GB de RAM.
- `boomer-win2k`: Windows 2000 SP0, máquina isolada “Boomer”, executando prompt de comando, WordPad e Notepad; 1 GB de RAM; há vários blocos EPROCESS de System possíveis, e o “correto” está no offset `0x5d008e0`.
- Ambas sem atividade maliciosa ou de rede no momento da captura.
