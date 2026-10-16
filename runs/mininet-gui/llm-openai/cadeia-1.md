# Session Export — SBRC 2025 Artifact Seals F and R

## Session Context

- **Subject:** Analytical review of the Mininet-GUI SBRC 2025 artifact for Functional (F) and Reproducible (R) seals, followed by a user execution checklist.
- **Source scope:** Four user-provided attachments only: `artigo.pdf`, `artefato.txt`, `instrucoes-oficiais.md`, and `reivindicacoes.md`, under `C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/`.
- **Artifact revision named by the user:** `465648a4425a4457af0348ab951cf7f71d37a86f`.
- **Workspace:** `C:/Users/reinaldo.wendt/Documents/Codex/2026-10-16/atue-como-revisor-do-comit-de-4`; projectless, with no Git repository at that path. Before this export, its `outputs/` and `work/` directories were empty.
- **Export timestamp:** 2026-10-16 13:20 America/Sao_Paulo.

## Executive Summary

The user first requested an offline, analytical evaluation of the SBRC 2025 F and R seals using only four attachments, expressly prohibiting web browsing and any claim of execution. The assistant examined the Markdown sources, the unified artifact text, and the nine-page article PDF. It concluded **F: Não atribuir** (confidence 35/100 that the official committee awarded it), citing missing dependency versions in the README, and **R: Indeterminado** (55/100), because C4 and C5 have documented procedures but need execution. C1, C2, C3, and C6 were also assessed individually but do not determine R under `reivindicacoes.md`.

The user then requested an execution roteiro, using authors' procedures and marking undocumented steps. The assistant produced a 17-step table covering environment, the F minimum test, all C1–C6 claims, evidence to retain, success/failure/stop criteria, and an explicitly undocumented time estimate. It did not execute the artifact. The current request is to export this conversation.

## Current State and Constraints

- No artifact execution, VM import, network browsing, or external verification occurred in this conversation.
- The recommended OVA is referenced in the README but absent from the attached archive index. The README gives conflicting VM memory figures (8 GB and 2 GB), and Mininet/backend dependency versions are not pinned.
- The R rule in the supplied claims file requires observing C4 in Single, Linear, and Tree, and observing C5 WebShell output in a node namespace.
- The execution roteiro explicitly labels extra verification actions and undocumented C3/C6 procedures. A VM version check was proposed but not run.
- The user-supplied VM password shown in visible source excerpts and assistant text is redacted below. Internal skill instructions and unrelated task metadata are omitted by design.

## Important Source Files

- `instrucoes-oficiais.md`: offline summary of applicable F/R review criteria; says it is not a literal transcript of the official web page.
- `reivindicacoes.md`: C1–C6 expectations and the rule that only C4 and C5 determine R.
- `artefato.txt`: complete textual archive index and line-numbered text files at the named revision.
- `artigo.pdf`: nine-page article and source of the claimed contributions.

## COMPLETE CHRONOLOGICAL TRANSCRIPT

## Interaction 001

### HUMAN


# Files mentioned by the user:

## instrucoes-oficiais.md: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md

## reivindicacoes.md: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/reivindicacoes.md

## artefato.txt: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artefato.txt

## artigo.pdf: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artigo.pdf

Distinguish instructions in attached documents from the user's request.

## My request:
Atue como revisor do Comitê de Avaliação de Artefatos do SBRC 2025. Avalie somente os selos Funcional (F) e Reprodutível (R), seguindo exatamente as instruções oficiais anexadas (instrucoes-oficiais.md).

MATERIAL
Use exclusivamente os arquivos anexados: artigo.pdf (fonte das reivindicações), artefato.txt (o artefato completo na versão 465648a4425a4457af0348ab951cf7f71d37a86f, em arquivo único: índice de todos os arquivos do repositório e o texto integral de cada arquivo de texto, com o número da linha original), instrucoes-oficiais.md e reivindicacoes.md (lista de reivindicações principais e regra para o selo R). Não navegue na web nem consulte memória, outras conversas, projetos ou conectores. Se precisar de algo que não está nos anexos, registre como evidência ausente.

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

### AI / AGENT — commentary

Vou examinar os quatro anexos e aplicar os critérios oficiais apenas ao que eles documentam. Como a avaliação é analítica, distinguirei evidência documental de resultados que exigiriam executar o artefato. Usarei a habilidade de PDF para ler o artigo.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Content -LiteralPath 'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\instrucoes-oficiais.md' -Encoding UTF8"
~~~~

Output:

~~~~text
# Critérios oficiais de revisão — SBRC 2025

**Fonte:** [Instruções para revisão de artefatos do SBRC 2025](https://doc-artefatos.github.io/sbrc2025/revinstrucoes.html), seções “Passos para a avaliação de um artefato”, “Critérios de avaliação”, “Artefatos Funcionais (SeloF)” e “Experimentos Reprodutíveis (SeloR)”. Registro arquivado em `../referencia/instrucoes-oficiais.md`, consultado em 15/10/2026.

**Natureza deste arquivo:** resumo dos critérios relevantes à avaliação F/R, preparado para leitura offline; não é transcrição literal nem contém a página de resultados ou a decisão oficial deste artefato. A URL identifica a proveniência, sem exigir navegação.

## Contexto de revisão

- Antes da avaliação, o revisor lê o artigo e identifica suas principais contribuições. O foco é a qualidade do artefato em relação ao artigo.
- O ambiente escolhido precisa satisfazer os requisitos mínimos do artefato; a página recomenda virtualização. Recursos específicos necessários devem estar descritos no apêndice.
- A revisão justifica os selos após examinar documentação e evidências observadas, apontando problemas encontrados.

## Funcional (F)

O código ou artefato deve poder ser executado, e o revisor deve conseguir observar funcionalidades. O README deve informar dependências e versões, ambiente de execução, instalação, execução e um exemplo mínimo. A conclusão funcional requer observação do artefato, não apenas a presença das instruções.

## Reprodutível (R)

O revisor deve conseguir reproduzir as **principais reivindicações do artigo**. Para isso, o artefato precisa fornecer instruções de execução e descrição do processo empregado nos experimentos que produziram os resultados do artigo. A avaliação confronta o resultado observado com a reivindicação correspondente.
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Content -LiteralPath 'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\reivindicacoes.md' -Encoding UTF8"
~~~~

Output:

~~~~text
# Reivindicações principais — Mininet-GUI (SBRC 2025)

Lista fixada antes da avaliação a partir do artigo (`artigo.pdf`) e do artefato na versão `465648a4425a4457af0348ab951cf7f71d37a86f` (`artefato.txt`). Páginas: numeração do PDF, de 1 a 9. C1–C6 são as seis contribuições enumeradas no artigo (p. 2, §1). Seções do README: títulos do `README.md` em `artefato.txt`.

| ID | Reivindicação | Onde está no artigo | Resultado esperado | O README indica como reproduzir? |
|---|---|---|---|---|
| C1 | Interface web dinâmica para criar e manipular visualmente topologias em um grafo interativo | p. 1 (resumo); p. 2, §1, contribuição 1; pp. 4–6, §3; p. 7, Fig. 2 | elementos criados pelo usuário representados no grafo e respondendo às ações | sim: "Teste mínimo", passos 1–5 |
| C2 | Emulação integrada: a ferramenta inicia e gerencia a emulação Mininet pela interface, permitindo testar a conectividade | p. 2, §1, contribuição 2; pp. 4–5, §3; p. 6, §4, caso 1 | nós emulados e resultado de `pingall` exibido na interface | sim: "Teste mínimo", passos 4–6 |
| C3 | Modificação da topologia em tempo real: criar e remover nós e links com a emulação em andamento, sem reiniciá-la | p. 1 (resumo); p. 2, §1, contribuição 3; p. 6, §3; p. 7 | rede alterada enquanto a emulação continua ativa | parcial: "Teste mínimo", passo 8 (opcional) |
| C4 | Geração automatizada de topologias nos modelos Single, Linear e Tree, com número de dispositivos escolhido | p. 2, §1, contribuição 4; p. 6, §3, "Topology Generator"; pp. 6–7, §4, caso 1 e Fig. 2 | topologia de cada modelo gerada com a quantidade de dispositivos escolhida | sim: "Experimentos", reivindicação "Geração automatizada de topologias…"; "Teste mínimo", passo 5 |
| C5 | Terminal dos nós via WebShell: executar comandos Bash no namespace de um nó emulado | p. 1 (resumo); p. 2, §1, contribuição 5; pp. 5–6, §3; p. 6, §4, caso 2; p. 7, Fig. 2 | saída do comando exibida na aba do nó selecionado | sim: "Experimentos", reivindicação "Terminal integrado dos nós via WebShell"; "Teste mínimo", passo 7 (opcional) |
| C6 | Visualização, criação e remoção de regras de fluxo OpenFlow nas tabelas dos switches | p. 2, §1, contribuição 6; pp. 5–6, §3, "Flow Rule Integration" e "Flow Rule Editor"; p. 7, §5 | tabela de fluxo exibida, com a regra inserida ou removida no switch | não |

## Regra para o selo R

Na seção "Experimentos", o README marca duas reivindicações a reproduzir, correspondentes a **C4** e **C5**. **R é atribuído se C4 e C5 forem reproduzidas.** C1, C2, C3 e C6 são contribuições do artigo que podem embasar F, mas não entram na regra de R.

## Critério de reprodução

As reivindicações descrevem comportamentos, sem valores numéricos com tolerância declarada pelos autores. Uma reivindicação é reproduzida quando o resultado esperado da tabela é observado. Em C4, nos três modelos.
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Item -LiteralPath 'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\instrucoes-oficiais.md','C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\reivindicacoes.md','C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt','C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf' | Select-Object Name,Length,FullName | Format-Table -AutoSize"
~~~~

Output:

~~~~text

Name                   Length FullName
----                   ------ --------
instrucoes-oficiais.md   1882 C:\Users\reinaldo.wendt\Desktop\unipampa\leas-tarefa-8\t8-leas\runs\mininet-gui\pacote\i…
reivindicacoes.md        2981 C:\Users\reinaldo.wendt\Desktop\unipampa\leas-tarefa-8\t8-leas\runs\mininet-gui\pacote\r…
artefato.txt           180492 C:\Users\reinaldo.wendt\Desktop\unipampa\leas-tarefa-8\t8-leas\runs\mininet-gui\pacote\a…
artigo.pdf             529019 C:\Users\reinaldo.wendt\Desktop\unipampa\leas-tarefa-8\t8-leas\runs\mininet-gui\pacote\a…
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Content -LiteralPath 'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt' -Encoding UTF8 -TotalCount 180"
~~~~

Output:

~~~~text
ARTEFATO EM ARQUIVO ÚNICO
Origem: artefato.zip (SHA-256 e766231891c8441d21dd44208d1ee34f677a51f2dbcfb57651f88586df34d91c), gerado por git archive.
Commit (comentário do ZIP): 465648a4425a4457af0348ab951cf7f71d37a86f
Diretório raiz no ZIP: mininet-gui-465648a4/
Conteúdo: todos os arquivos do commit. Arquivos de texto aparecem na íntegra, com o número
da linha original à esquerda (LINHA| texto). Arquivos binários aparecem só no índice.
Para citar evidência use caminho:linha, por exemplo README.md:12.

ÍNDICE (caminho | bytes | tipo | sha256)
LICENSE | 1534 | texto | 478f22ae58e8b61113e2c490f6a946489b20a7dad04830922280ce8efc50e964
README.md | 9086 | texto | e424434fa7cf0985a9472d2b29c62b46d121d6db8c199428841406ccef1e3753
example_network_export.json | 2547 | texto | 204b6a82462950c05cc83dbc7052638a2d85e965a7e788fd608e67db4713f36c
example_network_export.py | 1118 | texto | 287df046e7e2e1a483738708b1b3fa29ed14b87978d6a7eba4a2d7ded634dde2
mininet-gui-backend/.gitignore | 46 | texto | 27cfcd5fb6902871188d2cda6a5c41e4265ababa26b2f353a56a2d0fb2d33786
mininet-gui-backend/mininet_gui_backend/__init__.py | 0 | texto | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
mininet-gui-backend/mininet_gui_backend/api.py | 16830 | texto | 1ea14fe454ef54b39569ceada233f0e454411f03f21efc9b8f61f30fe2830d6e
mininet-gui-backend/mininet_gui_backend/cli.py | 622 | texto | 52ebdb08b623c9875fd66ed4ecf6b16001ce102632c487ea0638aedbd8eae5ed
mininet-gui-backend/mininet_gui_backend/export.py | 2836 | texto | 97e1b01429dcb6d5a1c7659d540fa72cb98149e697d3891f4e267a92fb69f27b
mininet-gui-backend/mininet_gui_backend/schema.py | 399 | texto | 4dddb3910fb766dd6618c2fe2c9f24e89134ddd3a06c8a4ce23189a37358e396
mininet-gui-backend/requirements.txt | 46 | texto | 411ea75065cfc55deeeccd80aa1a92f21655a67b7e1fd76856d454e0d2b9f298
mininet-gui-frontend/.gitignore | 32 | texto | 8b41e08e3a96631e94934c92900840b65eca98e1c853ec265a8306cd48744813
mininet-gui-frontend/.prettierrc.json | 4 | texto | e3566b3a06430868d71e9287dfd6c6c520a3da027aabea01951d407ee131dc2f
mininet-gui-frontend/index.html | 353 | texto | 927673d3c9d3c17a9b4ca95d59c56fc08ff3c033996c150fceb92b36a333ccd7
mininet-gui-frontend/package-lock.json | 39833 | texto | 8ed86756c8b9ead7561e7fa814ac80775026091a06d76c1fe2d11864d11c5aee
mininet-gui-frontend/package.json | 498 | texto | 78e86936f05eea12e8aa99f066a05751a6f368b5bf24f58c76d41c9f45cf194b
mininet-gui-frontend/public/favicon.ico | 7732 | binário (omitido) | c9c463bb796f2bb2678ceb1bcfe917029502e9df09a8623c321ccea5fcb61474
mininet-gui-frontend/src/App.vue | 698 | texto | 52577dc727570305691ae2536ef75d44b2e25df3b4b669a7c7581730f0d8949d
mininet-gui-frontend/src/assets/controller.svg | 780 | texto | 3449b3e31037316b470c29d05d1b78433dabd527956d748f82bdb67feb10212b
mininet-gui-frontend/src/assets/ethernet-cable-off.svg | 209 | texto | 7b0c89fbe0ff790cc735535f3d367920ef9b9ccccad64baa8f3a9ee32d0e03f2
mininet-gui-frontend/src/assets/ethernet-cable.svg | 152 | texto | 8e2be6a14c2698119f1cb4f89f66f6ac6c7d5350842a4d07624322ce9dd3b83f
mininet-gui-frontend/src/assets/host.svg | 747 | texto | 446333cb5003ddf14ee31b83b4074726f129b5ee6cf841869c3f2ae962b2fa2a
mininet-gui-frontend/src/assets/light-controller.svg | 2057 | texto | 585ab9c4ab48ac78d11ce71de237fb013dd8cadb2f51937893a288b923a9bf96
mininet-gui-frontend/src/assets/light-host.svg | 2008 | texto | cc2aecb3452f52c2a22dcca56dc2d4da94ccf4b139e0a3250fb027bf169a3e0c
mininet-gui-frontend/src/assets/light-switch.svg | 1972 | texto | 118be96f53f8299771791c494d4a7e775f014f3c4ad6ecda9a0f7a36debc63e8
mininet-gui-frontend/src/assets/logo.svg | 308 | texto | da9b90952638876ba42099a1f8d6559f513c59379266e77abaa2940e7439d7e9
mininet-gui-frontend/src/assets/router.svg | 1059 | texto | 47f5e4e770b9653f4a16c104fef03e84079dd9ef242ae7e0f6078705125fb5ca
mininet-gui-frontend/src/assets/switch.svg | 758 | texto | adefe93770cf98557e2008234b80e6f5e5e3d66d5fcfff845283dae66c2bb90a
mininet-gui-frontend/src/components/ControllerForm.vue | 1391 | texto | 5fa372c802a554fdecdda15835b9c665286f013201e87e83772113715b79633d
mininet-gui-frontend/src/components/Header.vue | 1210 | texto | 341d00dd928f1b0717ddd1db2c00b1b252239d456262b96c27bc772ad4bcffda
mininet-gui-frontend/src/components/Modal.vue | 1760 | texto | b49ca2229d852af17f707f3a35575b54f45a7e649ccc7c241af0b5a0a700190c
mininet-gui-frontend/src/components/NetworkGraph.vue | 22077 | texto | c8272489b1bda41267f6b146ab51688f3f45c2941ebba5ab500f915c7b93e345
mininet-gui-frontend/src/components/NodeStats.vue | 4072 | texto | d395d49608e59dc8fc2c947a0c1a5660473607a3a6b7013ff31d887d78b03e47
mininet-gui-frontend/src/components/PingallResults.vue | 1874 | texto | 88da425654d0c454e8ef76b3d2f79c7a32330fc188f2acad8377307cc4f0ee8c
mininet-gui-frontend/src/components/Side.vue | 8383 | texto | 72e0f131a6b430176e55b4cb8243c76f29529347ad547a2d806bf6b18794c6e8
mininet-gui-frontend/src/components/TopologyForm.vue | 2498 | texto | a2ce7c41127d1b989ed1f9fa644ed5319d7f08d3deedf35293359930081b2536
mininet-gui-frontend/src/components/Webshell.vue | 7067 | texto | 9758dc0826f2ac6975bb7af86f8d55bcdc3c60cccd45b6e718caa2983c4c5b84
mininet-gui-frontend/src/core/api.js | 9306 | texto | a6d3b71267b68fcc093298300294f6da971f7957aeb7706261214be18f306298
mininet-gui-frontend/src/core/options.js | 776 | texto | 3b54a8c534dda9e5ea8aced885433fc232f15e96906956d9e8d8198eea9525f9
mininet-gui-frontend/src/main.js | 130 | texto | 58f70b4e2755bbf02d06c65cfbc8138fcd2aaa7404eb7128d5e502b7684915b1
mininet-gui-frontend/vite.config.js | 357 | texto | 2f4c8578e0a4545e9ba1a0009c973db8a2372e89d6678ddf6bc91c1bee68e9a4
run.sh | 971 | texto | e1e2a1e8d45685fe8110f76934748ff98a541a76e51657f987f50bbd174d77f5
setup.sh | 680 | texto | 9f7c7bf54590fcc8dbed8e4d798e798dda98f4c53d8295f90b8f75b687df7246

===== INÍCIO DO ARQUIVO: LICENSE (28 linhas) =====
 1| BSD 3-Clause License
 2| 
 3| Copyright (c) 2025, LaTARC Research Lab
 4| 
 5| Redistribution and use in source and binary forms, with or without
 6| modification, are permitted provided that the following conditions are met:
 7| 
 8| 1. Redistributions of source code must retain the above copyright notice, this
 9|    list of conditions and the following disclaimer.
10| 
11| 2. Redistributions in binary form must reproduce the above copyright notice,
12|    this list of conditions and the following disclaimer in the documentation
13|    and/or other materials provided with the distribution.
14| 
15| 3. Neither the name of the copyright holder nor the names of its
16|    contributors may be used to endorse or promote products derived from
17|    this software without specific prior written permission.
18| 
19| THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
20| AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
21| IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
22| DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
23| FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
24| DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
25| SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
26| CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
27| OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
28| OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
===== FIM DO ARQUIVO: LICENSE =====

===== INÍCIO DO ARQUIVO: README.md (146 linhas) =====
  1| # Mininet-GUI: Uma Abordagem Visual e Interativa para Experimentação em Redes SDN
  2| 
  3| O Mininet é um emulador amplamente utilizado para a prototipação e experimentação de Redes Definidas por Software (SDN). No entanto, sua interface gráfica principal, o MiniEdit, oferece suporte limitado e baixa interatividade, dificultando sua adoção e restringindo experimentações avançadas. Embora diversas ferramentas tenham sido propostas, nenhuma se consolidou como alternativa definitiva devido à falta de integração de funcionalidades essenciais. 
  4| Neste trabalho, apresentamos o Mininet-GUI, uma ferramenta integrada que opera através de uma interface web para viabilizar a criação, edição e execução de topologias no Mininet em tempo real. O Mininet-GUI possibilita a manipulação dinâmica de hosts, switches, controladores e links, além da execução de comandos diretamente na interface. Diferentemente das abordagens existentes, o Mininet-GUI oferece edição interativa da topologia, acesso simplificado aos terminais via WebShell e suporte à exportação/importação de topologias nos formatos JSON e Python.  
  5| O Mininet-GUI visa tornar a experimentação com SDN mais acessível e eficiente, atendendo tanto a iniciantes quanto a pesquisadores avançados. Este trabalho descreve sua arquitetura, funcionalidades e aplicabilidade por meio de casos de uso recorrentes.
  6| 
  7| # Estrutura do readme.md
  8| 
  9| O arquivo README.md divide-se nas seguintes seções: Selos Considerados, Informações Básicas, Dependências, Preocupações com segurança, Instalação, Teste mínimo, Experimentos e LICENSE.
 10| O repositório contém dois subdiretórios principais: mininet-gui-frontend, com o código da aplicação frontend, e mininet-gui-backend, com o código do backend.
 11| Além disso, há dois scripts setup.sh e run.sh, para facilitar a instalação e execução.
 12| Foram incluídos também dois arquivos: `example_network_export.json` e `example_network_export.py`, que são arquivos exemplos exportados de uma topologia criada no Mininet-GUI.
 13| 
 14| 
 15| # Selos Considerados
 16| 
 17| Os selos considerados são: Disponíveis, Funcionais, Sustentáveis e Reprodutíveis.
 18| 
 19| 
 20| # Informações básicas
 21| 
 22| Vídeo da demonstração: <https://youtu.be/YSsqHKsJlxY>
 23| 
 24| Repositório oficial: <https://github.com/latarc/mininet-gui>
 25| 
 26| Para a demonstração, foi utilizado um laptop com as seguintes configurações:
 27| 
 28| Processador:	Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz   2.50 GHz
 29| RAM instalada:	8,00 GB
 30| Sistema Operacional:	Windows 11 Home Single Language
 31| Tipo de sistema:	Sistema operacional de 64 bits, processador baseado em x64
 32| Espaço disponível em disco: Pelo menos 80GB livres
 33| 
 34| 
 35| # Dependências
 36| 
 37| A execução do Mininet-GUI requer o Oracle VirtualBox (versão 7.1.6 r167084).
 38| Memória RAM: Mínimo de 8GB para a máquina virtual.
 39| 
 40| 
 41| # Preocupações com segurança
 42| 
 43| A instalação nativa do Mininet é invasiva, e pode alterar ou remover arquivos importantes do sistema de arquivos. 
 44| Por isso, recomenda-se a utilização da VM do Mininet-GUI que disponibilizamos no repositório.
 45| 
 46| 
 47| # Instalação
 48| 
 49| ## Máquina Virtual (recomendado)
 50| 
 51| Pré-requisitos: Oracle VirtualBox (<https://www.virtualbox.org/wiki/Downloads>)
 52| 
 53| Passo 1: Baixe o arquivo ova neste link: <https://drive.google.com/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing>
 54| 
 55| Passo 2: Abra o arquivo `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no VirtualBox, para importar a máquina virtual
 56| 
 57| Passo 3: Execute a máquina virtual (user `mininet`, senha [REDACTED: default VM password])
 58| 
 59| 
 60| ## Instalação manual
 61| 
 62| Atenção: os comandos abaixo irão modificar o kernel e outras configurações do seu sistema operacional, portanto use com cautela.
 63| Utilize os comandos abaixo para instalar manualmente (testado no ubuntu 20.04):
 64| 
 65| ```bash
 66| git clone https://github.com/mininet/mininet
 67| cd mininet
 68| ./util/install.sh -nfv
 69| cd ..
 70| git clone https://github.com/latarc/mininet-gui
 71| cd mininet-gui
 72| ./setup.sh
 73| ```
 74| 
 75| Opcionalmente, para instalar o Ryu:
 76| ```bash
 77| pip3 install ryu eventlet==0.30.0 dnspython==1.16.0
 78| ```
 79| 
 80| # Teste mínimo
 81| 
 82| Passo 1: Execute a VM dentro do VirtualBox e faça login (usuário: `mininet`, senha: [REDACTED: default VM password])
 83| 
 84| Passo 2: Abra o terminal (Ctrl+Alt+T) e rode o seguinte comando: `mininet_gui` (ou alternativamente `/home/mininet/mininet-gui/run.sh`)
 85| 
 86| Passo 3: A execução do comando do Passo 2 mostrará em sua saída do terminal uma URL (Exemplo: `http://10.0.2.15:5173`). Acesse essa URL em um navegador dentro da VM.
 87| 
 88| Passo 4: Para criar um controlador, arraste o ícone rotulado "Controller", localizado na aba lateral esquerda, para o centro da tela. Em seguida, se abrirá uma caixa de diálogo, perguntando o tipo do controller. Nessa etapa, selecione a opção "Default" e em seguida pressione o botão "Submit" para criar o controller.
 89| 
 90| Passo 5: Clique no botão "Generate Topology" localizado na aba lateral esquerda. No modal, selecione o "Topology Type" Single, o "Controller" c1, e no campo "Hosts" insira o número 2. Em seguida, pressione o botão "Submit".
 91| 
 92| Passo 6: Execute um teste de pingall clicando no botão "Run Pingall Test" na aba lateral esquerda e aguarde os resultados aparecerem.
 93| 
 94| Passo 7 (opcional): Teste com iperf - selecione no webshell o terminal do node h1 e digite o comando `iperf -s`. Depois, abra o terminal do node h2 e digite o comando `iperf -c 10.0.0.1`. Aguarde 1 minuto para o teste completar-se.
 95|
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "rg -n 'README.md|Teste mínimo|Experimentos|Topology Generator|Flow Rule|WebShell|requirements|python|pip|Mininet|OpenFlow|"'^'"\\S.*:"'$'"' 'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt' | Select-Object -First 220"
~~~~

Output:

~~~~text
7:Para citar evidência use caminho:linha, por exemplo README.md:12.
11:README.md | 9086 | texto | e424434fa7cf0985a9472d2b29c62b46d121d6db8c199428841406ccef1e3753
20:mininet-gui-backend/requirements.txt | 46 | texto | 411ea75065cfc55deeeccd80aa1a92f21655a67b7e1fd76856d454e0d2b9f298
85:===== INÍCIO DO ARQUIVO: README.md (146 linhas) =====
86:  1| # Mininet-GUI: Uma Abordagem Visual e Interativa para Experimentação em Redes SDN
88:  3| O Mininet é um emulador amplamente utilizado para a prototipação e experimentação de Redes Definidas por Software (SDN). No entanto, sua interface gráfica principal, o MiniEdit, oferece suporte limitado e baixa interatividade, dificultando sua adoção e restringindo experimentações avançadas. Embora diversas ferramentas tenham sido propostas, nenhuma se consolidou como alternativa definitiva devido à falta de integração de funcionalidades essenciais. 
89:  4| Neste trabalho, apresentamos o Mininet-GUI, uma ferramenta integrada que opera através de uma interface web para viabilizar a criação, edição e execução de topologias no Mininet em tempo real. O Mininet-GUI possibilita a manipulação dinâmica de hosts, switches, controladores e links, além da execução de comandos diretamente na interface. Diferentemente das abordagens existentes, o Mininet-GUI oferece edição interativa da topologia, acesso simplificado aos terminais via WebShell e suporte à exportação/importação de topologias nos formatos JSON e Python.  
90:  5| O Mininet-GUI visa tornar a experimentação com SDN mais acessível e eficiente, atendendo tanto a iniciantes quanto a pesquisadores avançados. Este trabalho descreve sua arquitetura, funcionalidades e aplicabilidade por meio de casos de uso recorrentes.
94:  9| O arquivo README.md divide-se nas seguintes seções: Selos Considerados, Informações Básicas, Dependências, Preocupações com segurança, Instalação, Teste mínimo, Experimentos e LICENSE.
97: 12| Foram incluídos também dois arquivos: `example_network_export.json` e `example_network_export.py`, que são arquivos exemplos exportados de uma topologia criada no Mininet-GUI.
122: 37| A execução do Mininet-GUI requer o Oracle VirtualBox (versão 7.1.6 r167084).
128: 43| A instalação nativa do Mininet é invasiva, e pode alterar ou remover arquivos importantes do sistema de arquivos. 
129: 44| Por isso, recomenda-se a utilização da VM do Mininet-GUI que disponibilizamos no repositório.
140: 55| Passo 2: Abra o arquivo `Mininet-GUI-Desktop-VM-SBRC-2025.ova` no VirtualBox, para importar a máquina virtual
162: 77| pip3 install ryu eventlet==0.30.0 dnspython==1.16.0
165: 80| # Teste mínimo
183: 98| Passo 9: Finalmente, clique nos botões "Export Topology (JSON)" e "Export Mininet Script" para obter respectivamente o arquivo JSON com a configuração da topologia atual e o script do mininet para executar a topologia fora do Mininet-GUI, diretamente no Python.
186:101| # Experimentos
195:110| ## Reivindicação "Terminal integrado dos nós via WebShell"
208:123| modification, are permitted provided that the following conditions are met:
232:===== FIM DO ARQUIVO: README.md =====
355: 3| Script generated by Mininet-GUI (https://github.com/latarc/mininet-gui)
357: 5| from mininet.net import Mininet
365:13| net = Mininet(controller=Controller, switch=OVSKernelSwitch, host=Host, link=TCLink)
399:47| CLI(net)  # Start Mininet CLI
417:  2| Mininet-GUI API to deploy and manage a mininet network instance.
435: 20| from mininet.net import Mininet
464: 49|     app.net = Mininet(autoSetMacs=True, topo=Topo())
475: 60|     title="Mininet-GUI-API",
515:100| def list_edges():
519:104| def get_network_started():
523:108| def start_network():
525:110|     if app.net.is_started:
528:113|     for controller in app.controllers:
530:115|     for switch_id in app.switches:
532:117|         if switch.controller:
534:119|         else:
540:125| def stop_network():
554:139|     # Create the Mininet network
556:141|     app.net = Mininet(autoSetMacs=True, topo=Topo())
562:147| def reset_network():
568:153| def run_pingall():
570:155|     if not app.net.is_started:
577:162| def create_host(host: Host):
578:163|     if host.id in app.hosts:
581:166|     # Create host in the Mininet network using the request data
595:180| def create_switch(switch: Switch):
596:181|     # Create switch in the Mininet network using the request data
598:183|     if switch.controller and switch.controller not in app.controllers:
603:188|     if app.net.is_started and switch.controller:
605:190|     else:
616:201| def create_controller(controller: Controller):
617:202|     # Create controller in the Mininet network using the request data
619:204|     if controller.remote:
627:212|     else:
642:227| def associate_switch(data: dict):
644:229|     if "switch" not in data or "controller" not in data:
650:235|     if sw_id not in app.net.nameToNode or ctl_id not in app.net.nameToNode:
654:239|     if app.switches[sw_id].controller:
658:243|     if app.net.is_started:
663:248| def create_link(link: Tuple[str, str]):
664:249|     # Create the link in the Mininet network using the link data
665:250|     if link[0] not in app.net.nameToNode or link[1] not in app.net.nameToNode:
668:253|     if key in app.links:
671:256|     if app.net.is_started:
672:257|         for node in link:
674:259|             if node.type == "host":
676:261|             elif node.type == "sw" and node.controller:
686:271| def node_position(data: dict):
687:272|     if "node_id" not in data or "position" not in data:
694:279|     if node_id not in app.net.nameToNode:
701:286|     if node.type == "sw":
704:289|     elif node.type == "host":
707:292|     elif node.type == "controller":
714:299| def delete_node(node_id: str):
715:300|     if node_id not in app.net.nameToNode:
719:304|     if node.type == "sw":
721:306|     elif node.type == "host":
723:308|     elif node.type == "controller":
725:310|         for switch_id in app.switches:
727:312|             if switch.controller == node_id:
734:319| def delete_link(src_id: str, dst_id: str):
736:321|     if key not in app.links:
743:328| def remove_association(src_id: str, dst_id: str):
744:329|     if src_id not in app.net.nameToNode or dst_id not in app.net.nameToNode:
747:332|     for node_id in (src_id, dst_id):
749:334|         if node.type == "sw":
751:336|         elif node.type == "controller":
753:338|     if not sw or not ctl:
757:342|     if app.net.is_started:
763:348| def get_node_stats(node_id: str):
764:349|     if node_id not in app.net.nameToNode:
769:354|     if not base_data:
773:358|     if node.type == "sw":
781:366|         for line in flow_table_raw.split("\n"):
786:371|             for field in fields:
789:374|                 if len(key_val) == 2:
791:376|                     if key in FLOW_FIELDS:
793:378|                     else:
799:384|     elif node.type == "host":
803:388|         for line in arp_table.splitlines():
805:390|             if len(parts) < 6:
819:404| def export_network():
824:409| def export_network():
829:414| async def import_json(file: UploadFile = File(...)):
832:417|     try:
836:421|         for controller_data in data.get("controllers", []):
840:425|         for switch_data in data.get("switches", []):
845:430|             if controller:
851:436|         for host_data in data.get("hosts", []):
855:440|         for link in data.get("links", []):
862:447|     except json.JSONDecodeError:
865:450| async def read_pty(master_fd, websocket: WebSocket):
867:452|     try:
868:453|         while True:
871:456|             if master_fd in r:
874:459|     except Exception as e:
878:463| async def websocket_terminal(websocket: WebSocket, node_id: str):
879:464|     """WebSocket endpoint for accessing a Mininet node terminal"""
884:469|     if not node:
897:482|     try:
898:483|         while True:
902:487|     except WebSocketDisconnect:
913: 4| # and https://github.com/python/cpython/blob/3.11/Lib/cmd.py
915: 6| # and https://docs.python.org/3/library/cmd.html
921:12| class CLISession:
922:13|     def __init__(self):
926:17|     def detach_and_listen(self):
941:  9| Script generated by Mininet-GUI (https://github.com/latarc/mininet-gui)
943: 11| from mininet.net import Mininet
951: 19| net = Mininet(controller=Controller, switch=OVSKernelSwitch, host=Host, link=TCLink)
973: 41| CLI(net)  # Start Mininet CLI
1035:103| ) -> str:
1061:15| class Controller(Node):
1067:21| class Host(Node):
1072:26| class Switch(Node):
1077:===== INÍCIO DO ARQUIVO: mininet-gui-backend/requirements.txt (4 linhas) =====
1081:4| python-multipart
1082:===== FIM DO ARQUIVO: mininet-gui-backend/requirements.txt =====
1101: 7|     <title>Mininet-GUI</title>
2637: 9|     <p class="header-logo">Mininet-GUI</p>
2815: 23|   requestExportMininetScript,
2850: 58|           @exportMininetScript="exportMininetScript"
2857: 65|     <!-- Main Content (Graph + WebShell) -->
2872: 80|       <!-- WebShell at the bottom -->
3428:636|     async exportMininetScript() {
3429:637|       await requestExportMininetScript();
3806: 56|       <button class="button-control-network" id="button-export-script" @click="$emit('exportMininetScript')">
3808: 58|         Export Mininet Script
3876:126|     "exportMininetScript",
4160:  5|       <span class="title">WebShell</span>
4714:261| export const requestExportMininetScript = async () => {
4721:268|       const blob = new Blob([response.data], { type: "text/x-python" });
4895:22| echo "Mininet-GUI bootstrap complete"
4900:27| echo -e "\n\n#### Mininet-GUI is available at: ####\n"
4914:10| (cd $BACKEND_DIR ; sudo python3 -m pip install -r requirements.txt)
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (failed, exit 1):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command 'Get-Command pdftotext,pdfinfo -ErrorAction SilentlyContinue | Select-Object Name,Source'
~~~~

Output:

~~~~text

Name        Source
----        ------
pdfinfo.exe C:\Users\reinaldo.wendt\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bi…
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$pi=(Get-Command pdfinfo).Source; & $pi '"'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf'"
~~~~

Output:

~~~~text
Creator:         TeX
Producer:        pdfTeX-1.40.26
CreationDate:    Thu May 22 20:32:21 2025 Hora oficial do Brasil
ModDate:         Thu May 22 20:32:21 2025 Hora oficial do Brasil
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           9
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       529019 bytes
Optimized:       no
PDF version:     1.3
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt'; "'$s=Get-Content -LiteralPath $p -Encoding UTF8; $s[165..231]'
~~~~

Output:

~~~~text
 81| 
 82| Passo 1: Execute a VM dentro do VirtualBox e faça login (usuário: `mininet`, senha: [REDACTED: default VM password])
 83| 
 84| Passo 2: Abra o terminal (Ctrl+Alt+T) e rode o seguinte comando: `mininet_gui` (ou alternativamente `/home/mininet/mininet-gui/run.sh`)
 85| 
 86| Passo 3: A execução do comando do Passo 2 mostrará em sua saída do terminal uma URL (Exemplo: `http://10.0.2.15:5173`). Acesse essa URL em um navegador dentro da VM.
 87| 
 88| Passo 4: Para criar um controlador, arraste o ícone rotulado "Controller", localizado na aba lateral esquerda, para o centro da tela. Em seguida, se abrirá uma caixa de diálogo, perguntando o tipo do controller. Nessa etapa, selecione a opção "Default" e em seguida pressione o botão "Submit" para criar o controller.
 89| 
 90| Passo 5: Clique no botão "Generate Topology" localizado na aba lateral esquerda. No modal, selecione o "Topology Type" Single, o "Controller" c1, e no campo "Hosts" insira o número 2. Em seguida, pressione o botão "Submit".
 91| 
 92| Passo 6: Execute um teste de pingall clicando no botão "Run Pingall Test" na aba lateral esquerda e aguarde os resultados aparecerem.
 93| 
 94| Passo 7 (opcional): Teste com iperf - selecione no webshell o terminal do node h1 e digite o comando `iperf -s`. Depois, abra o terminal do node h2 e digite o comando `iperf -c 10.0.0.1`. Aguarde 1 minuto para o teste completar-se.
 95| 
 96| Passo 8 (opcional): Multiplos controladores - arraste um novo "Controller" da barra lateral para o centro da tela, mas dessa vez mude o type para "Remote" e preencha o IP 127.0.0.1 e a porta 6633. Em seguida, gere uma topologia (com o "Generate Topology") do tipo Single e com 2 hosts, e também selecione o novo controlador criado (c2). Adicionalmente, clique no botão "Create Link" e conecte os switches das duas topologias, s1 e s2, clicando e arrastando de um para o outro (o sucesso dessa ação é indicado por uma linha verde conectando os dois nós). A seguir, selecione no webshell o terminal do novo controlador c2 e execute o comando: `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13` para iniciar o controlador SDN Ryu. Optamos por utilizar o Ryu nesse exemplo, pois ele é leve e não ocupa tanto espaço na VM quanto outros (ONOS, OpenDaylight, Floodlight). Para testar a conexão, execute um teste com o botão de Pingall.
 97| 
 98| Passo 9: Finalmente, clique nos botões "Export Topology (JSON)" e "Export Mininet Script" para obter respectivamente o arquivo JSON com a configuração da topologia atual e o script do mininet para executar a topologia fora do Mininet-GUI, diretamente no Python.
 99| 
100| 
101| # Experimentos
102| 
103| A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM.
104| 
105| ## Reivindicação "Geração automatizada de topologias, incluindo diversos modelos amplamente utilizados"
106| 
107| Após inicializar o mininet_gui e acessar a interface web do frontend, clique no botão "Generate Topology". Selecione o tipo de topologia (Single, Linear ou Tree), 
108| e o número de dispositivos, então clique em OK.
109| 
110| ## Reivindicação "Terminal integrado dos nós via WebShell"
111| 
112| Após inicializar o mininet_gui e acessar a interface web do frontend, crie ao menos um nó (seja pelo Gerador de Topologias ou clicando e arrastando) e na aba inferior titulada "Webshell"
113| selecione a aba com o nome desse nó, clicando nela.
114| Em seguida, utilize o terminal bash para executar comandos diretamente no namespace daquele nó.
115| 
116| # LICENSE
117| 
118| BSD 3-Clause License
119| 
120| Copyright (c) 2025, LaTARC Research Lab
121| 
122| Redistribution and use in source and binary forms, with or without
123| modification, are permitted provided that the following conditions are met:
124| 
125| 1. Redistributions of source code must retain the above copyright notice, this
126|    list of conditions and the following disclaimer.
127| 
128| 2. Redistributions in binary form must reproduce the above copyright notice,
129|    this list of conditions and the following disclaimer in the documentation
130|    and/or other materials provided with the distribution.
131| 
132| 3. Neither the name of the copyright holder nor the names of its
133|    contributors may be used to endorse or promote products derived from
134|    this software without specific prior written permission.
135| 
136| THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
137| AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
138| IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
139| DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
140| FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
141| DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
142| SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
143| CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
144| OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
145| OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
146| 
===== FIM DO ARQUIVO: README.md =====
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (failed, exit 1):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$pi=(Get-Command pdfinfo).Source; $pt=Join-Path (Split-Path $pi) '"'pdftotext.exe'; & "'$pt -layout '"'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf' - | Select-Object -First 260"
~~~~

Output:

~~~~text
&: 
Line |
   2 |  … Source; $pt=Join-Path (Split-Path $pi) 'pdftotext.exe'; & $pt -layout …
     |                                                              ~~~
     | The term 'C:\Users\reinaldo.wendt\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftotext.exe' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (failed, exit 1):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "python -c \"import pdfplumber; p=r'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf'; d=pdfplumber.open(p); print('PAGES',len(d.pages)); [(print('\\\\n### PDF PAGE',i+1,'\\\\n'),print((pg.extract_text() or '')[:20000])) for i,pg in enumerate(d.pages)]\""
~~~~

Output:

~~~~text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber; p=r'C:\Users\reinaldo.wendt\Desktop\unipampa\leas-tarefa-8\t8-leas\runs\mininet-gui\pacote\artigo.pdf'; d=pdfplumber.open(p); print('PAGES',len(d.pages)); [(print('\\n### PDF PAGE',i+1,'\\n'),print((pg.extract_text() or '')[:20000])) for i,pg in enumerate(d.pages)]
    ^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pdfplumber'
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

MCP call: `codex_app.load_workspace_dependencies` (status: completed). The workspace dependency paths were returned and used to select the bundled Python runtime for PDF text extraction.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (failed, exit 1):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "& 'C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' -c \"import pdfplumber; p=r'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf'; d=pdfplumber.open(p); print('PAGES',len(d.pages)); [(print('\\\\n### PDF PAGE',i+1,'\\\\n'),print((pg.extract_text() or '')[:20000])) for i,pg in enumerate(d.pages)]\""
~~~~

Output:

~~~~text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\Users\reinaldo.wendt\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u0131' in position 105: character maps to <undefined>
PAGES 9
\n### PDF PAGE 1 \n
~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~text
"C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; & 'C:\\Users\\reinaldo.wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' -c \"import pdfplumber; p=r'C:\\Users\\reinaldo.wendt\\Desktop\\unipampa\\leas-tarefa-8\\t8-leas\\runs\\mininet-gui\\pacote\\artigo.pdf'; d=pdfplumber.open(p); print('PAGES',len(d.pages)); [(print('\\\\n### PDF PAGE',i+1,'\\\\n'),print((pg.extract_text() or '')[:20000])) for i,pg in enumerate(d.pages)]\""
~~~~

Output:

~~~~text
PAGES 9
\n### PDF PAGE 1 \n
Mininet-GUI: Uma Abordagem Visual e Interativa para
Experimentac¸a˜o em Redes SDN
LucasM.Schneider1,Em´ıdioP.Neto1,FelipeS.DantasSilva1
1LaTARCResearchLab
InstitutoFederaldeEducac¸a˜o,CieˆnciaeTecnologiadoRioGrandedoNorte(IFRN)
Natal,RN–Brasil.
lucasschneider.dev@gmail.com,zshemidio@gmail.com, felipe.dantas@ifrn.edu.br
Abstract. Mininet is a widely adopted emulator for prototyping and experi-
menting with Software-Defined Networking (SDN). Its main graphical inter-
face,MiniEdit,however,offerslimitedfunctionalityandlowinteractivity,which
hampers adoption and constrains advanced experimentation. Although several
alternative tools have been proposed, none has become a definitive replace-
ment, largely due to the absence of essential integrated features. We present
Mininet-GUI, a web-based tool that enables real-time creation, editing, and
execution of Mininet topologies. Mininet-GUI allows dynamic manipulation
of hosts, switches, controllers, and links, as well as direct command execu-
tion through the interface. Unlike existing approaches, it provides interactive
topology editing, simplified terminal access via WebShell, and support for ex-
porting and importing topologies in JSON and Python formats. Mininet-GUI is
designed to make SDN experimentation more accessible and efficient for both
beginners and advanced researchers. This paper describes its architecture, ca-
pabilities,andapplicabilitythroughcommonusecases.
1. Introduc¸a˜o
No aˆmbito da prototipac¸a˜o e experimentac¸a˜o de soluc¸o˜es para ecossistemas de redes de
pro´ximagerac¸a˜o,aexemplodo5G/6G,oMininet[Lantzetal. 2010]consolidou-secomo
ferramenta de refereˆncia para emulac¸a˜o de redes programa´veis. O Mininet e´ ampla-
mente reconhecido pela comunidade acadeˆmica e pela indu´stria por ser um habilitador
para a criac¸a˜o a´gil de ambientes de alta fidelidade, viabilizando a ra´pida experimentac¸a˜o
de novos conceitos, protocolos e arquiteturas de Redes Definidas por Software (SDN)
[Haleplidisetal. 2015].
A adoc¸a˜o pra´tica de SDN pode ser maximizada por meio de interfaces intuiti-
vas que reduzam as barreiras de entrada para o seu aprendizado. Entretanto, esse pro-
cesso geralmente requer o uso combinado de ferramentas distintas e configurac¸o˜es man-
uais [Cosgrove2016, Bourasetal. 2017, SalibandLester2018]. O pro´prio Mininet e´
distribu´ıdo com o MiniEdit, uma interface gra´fica integrada que possibilita a criac¸a˜o e
configurac¸a˜o de cena´rios de redes SDN. No entanto, o MiniEdit limita-se somente a fun-
cionalidades ba´sicas, como a criac¸a˜o de topologias e a configurac¸a˜o dos dispositivos,
sem suporte a linha de comando ou scripts do Mininet, essenciais para experimentac¸o˜es
avanc¸adas. Essas limitac¸o˜es impulsionaram o desenvolvimento de soluc¸o˜es alternativas,
como o Mininet Editor [Vycˇ´ıtal2019] e o Integrated [Barloweetal. 2023], que intro-
duzemnovasperspectivasdeinterac¸a˜odousua´rioatrave´sdeumainterfaceweb.
\n### PDF PAGE 2 \n
Um levantamento recente do estado da arte identificou diversas outras soluc¸o˜es
voltadas a` interac¸a˜o com o ambiente de experimentac¸a˜o do Mininet, propostas para miti-
gar as restric¸o˜es das abordagens anteriores. Tais abordagens, no entanto, ainda possuem
deficieˆncias cr´ıticas, como a falta de integrac¸a˜o da execuc¸a˜o da emulac¸a˜o diretamente na
interface, comprometendo a experieˆncia de um ambiente verdadeiramente integrado para
experimentac¸a˜o. Outras limitac¸o˜esincluem aauseˆnciade umainterface webintuitiva, de
umacessoaoconsoleparaexecuc¸a˜odecomandoseagerac¸a˜oautomatizadadetopologias.
Essaslacunassa˜oevidenciadaspelofatode abordagensrecentescontinuaremrecorrendo
aoMiniEdit[BhaskaranandM.2024,Romanovetal. 2022].
Diante desse cena´rio, caracterizado pelo crescimento da demanda por soluc¸o˜es
SDNe pelaslimitac¸o˜esdas ferramentasexistentes, propomoso Mininet-GUI,uma ferra-
mentaintegradaparaaexperimentac¸a˜ooperacionalizadaatrave´sdeumainterfacegra´fica
que permite a criac¸a˜o, edic¸a˜o e execuc¸a˜o de topologias em tempo real no Mininet.
O Mininet-GUI na˜o somente simplifica o processo de experimentac¸a˜o em SDN, mas
tambe´mforneceperspectivasparafomentaraadoc¸a˜oderedesprograma´veisporumanova
gerac¸a˜o de pesquisadores e profissionais ao maximizar as possibilidades de ensino desse
paradigma por meio de uma abordagem interativa e simplificada. Ao integrar todas as
funcionalidadesessenciaisemumau´nicaplataforma,oMininet-GUIreduzanecessidade
de manipulac¸a˜o via CLI diretamente no host hospedeiro e a dependeˆncia de mu´ltiplas
ferramentasparaarealizac¸a˜odeexperimentoscompletos.
Asprincipaiscontribuic¸o˜esdoMininet-GUIincluem:
1. Interfacewebdinaˆmicaparamanipulac¸a˜ointuitivadatopologiaderede.
2. Emulac¸a˜ointegrada,eliminandoanecessidadedeconfigurac¸o˜esexternas.
3. Suporteamodificac¸o˜esnatopologiaemtemporeal.
4. Gerac¸a˜oautomatizadadetopologias,incluindodiversosmodelosamplamenteuti-
lizados.
5. Terminalintegradodosno´sviaWebShell.
6. Visualizac¸a˜oecriac¸a˜odasregrasdefluxo.
O restante deste trabalho esta´ organizado da seguinte forma: a Sec¸a˜o 2 discute
os principais trabalhos relacionados, justificando o Mininet-GUI. A Sec¸a˜o 3 detalha a ar-
quiteturaeimplementac¸a˜odoMininet-GUI,detalhandosuasprincipaisfuncionalidadese
fluxos operacionais. A Sec¸a˜o 4 descreve os cena´rios experimentais que ilustram a apli-
cabilidade da soluc¸a˜o. Por fim, a Sec¸a˜o 5 apresenta as considerac¸o˜es finais e direc¸o˜es
futurasparaoaprimoramentodaferramenta.
2. Trabalhos Relacionados
Olevantamentodoestadodaartesobreassoluc¸o˜esdeinterac¸a˜oentreousua´rioeoambi-
entedeexperimentac¸a˜ocomMininetrevelouqueassoluc¸o˜esexistentesgeralmenteforam
implementadas para atender a demandas espec´ıficas, sem que nenhuma delas oferec¸a um
conjunto abrangente de funcionalidades. Isso significa na˜o haver uma soluc¸a˜o unificada
que integre todas as capacidades essenciais para um ambiente completo e interativo para
a experimentac¸a˜o em SDN. A seguir, sa˜o descritas as funcionalidades identificadas nas
soluc¸o˜esanalisadas,organizadasnositensF1aoF10:
F1. Emulac¸a˜o integrada: executa e controla redes virtualizadas diretamente na fer-
ramenta.
\n### PDF PAGE 3 \n
F2. Suporteamodificac¸o˜esemtemporeal: permiteacriac¸a˜oeremoc¸a˜odedisposi-
tivoselinksnatopologiaseminterromperaexecuc¸a˜o.
F3. Interface web: possibilita a interac¸a˜o via navegador, proporcionando uma ex-
perieˆnciaintuitivaedinaˆmica.
F4. Webshell: fornece acesso a` CLI dos dispositivos emulados para a execuc¸a˜o de
comandosatrave´sdainterfaceweb.
F5. Exportac¸a˜o de script Python para o Mininet: gera arquivos compat´ıveis com a
APIdoMininetemPython.
F6. Suporte a mu´ltiplos controladores customiza´veis: possibilita o uso de diversos
controladoresdistintoscomconfigurac¸o˜espersonalizadas.
F7. Manipulac¸a˜o gra´fica: permite a criac¸a˜o e posicionamento dos dispositivos
atrave´sdeoperac¸o˜escomomouse.
F8. Persisteˆncia em banco de dados: armazena configurac¸o˜es e topologias em uma
basededados.
F9. SuporteaswitchesP4: compatibilidadecomswitchesprograma´veisemP4.
F10. Gerac¸a˜o automatizada de topologias: possibilita a criac¸a˜o de topologias com-
plexas,deformaautomatizada,reduzindoaintervenc¸a˜omanual.
Embora o Mininet possua um mecanismo interno para a gerac¸a˜o automa´tica de
topologias, dispon´ıvel somente pela CLI do sistema operacional hospedeiro, essa capaci-
dade na˜o esta´ presente nas ferramentas existentes. A Sec¸a˜o 3 detalha como o Mininet-
GUI aprimora cada uma das funcionalidades apresentadas, garantindo uma abordagem
modulareintegradanainterfaceweb.
ATabela1comparaoMininet-GUIeasdemaisferramentasexistentesemrelac¸a˜o
a`sfuncionalidadeslistadas.
Tabela 1. Comparac¸a˜o de funcionalidades (codificadas) e anos de publicac¸a˜o
dasprincipaisferramentasanalisadas.
Ferramenta Ano F1 F2 F3 F4 F5 F6 F7 F8 F9 F10
MiniEdit 2010 ✓ ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗
VND 2013 ✗ ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗
OSHI 2014 ✓ ✗ ✓ ✓ ✗ ✓ ✓ ✗ ✗ ✗
NetIDE 2016 ✓ ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✗ ✗
Vycital 2019 ✗ ✗ ✓ ✗ ✓ ✓ ✓ ✗ ✗ ✗
MiTE 2021 ✗ ✗ ✗ ✗ ✓ ✓ ✓ ✗ ✓ ✗
Integrated 2023 ✓ ✓ ✓ ✗ ✓ ✗ ✗ ✓ ✗ ✗
Mininet-GUI 2025 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✗ ✗ ✓
As subsec¸o˜es seguintes discutem os trabalhos relacionados em duas categorias:
(1)Ferramentassemintegrac¸a˜oa` emulac¸a˜oe(2)Ferramentascomintegrac¸a˜oa` emulac¸a˜o.
2.1. Ferramentassemintegrac¸a˜oa` emulac¸a˜o
As ferramentas identificadas nessa categoria na˜o fornecem mecanismos integrados para
iniciar e gerenciar a emulac¸a˜o diretamente na interface. A auseˆncia desse recurso exige
queousua´rioconfigureeexecuteaemulac¸a˜omanualmente.Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats

\n### PDF PAGE 4 \n
VND [Fontesetal. 2014] viabiliza a criac¸a˜o de cena´rios OpenFlow por meio de
bibliotecascustomiza´veisemumainterfaceweb. Noentanto,suaimplementac¸a˜obaseada
emAdobeFlashtornou-seobsoleta,apo´sadescontinuac¸a˜odatecnologiaem2020.
Mininet Editor [Vycˇ´ıtal2019] oferece uma interface web e permite a definic¸a˜o
expl´ıcita das configurac¸o˜es de conexo˜es entre as portas dos dispositivos, pore´m sem
integrac¸a˜ocomaexecuc¸a˜odaemulac¸a˜o.
MiTE[Sidiqetal. 2021]fornececompatibilidadecomswitchesprograma´veisem
P4. Contudo, assim como as outras ferramentas listadas, na˜o integra a execuc¸a˜o da
emulac¸a˜o diretamente na ferramenta, obrigando o usua´rio a inicia´-la manualmente via
terminal.
2.2. Ferramentascomintegrac¸a˜oa` emulac¸a˜o
As demais ferramentas, embora oferec¸am suporte a` execuc¸a˜o e controle da emulac¸a˜o na
interface,esta˜orestritasafuncionalidadesespec´ıficas.
MiniEdit [Lantzetal. 2010], distribu´ıdo com o Mininet, possui uma interface
gra´ficasimples. Osrecursosoferecidosna˜ofornecemacessoafuncionalidadesavanc¸adas
ea` criac¸a˜odetopologiascomplexas.
NetIDE [ArandaGutie´rrezetal. 2016] permite a integrac¸a˜o de mu´ltiplos contro-
ladores, possibilitando que a mesma aplicac¸a˜o opere independentemente da tecnologia
subjacente,minimizandoovendorlock-in.
OSHI [Salsanoetal. 2014] possibilita a criac¸a˜o de redes h´ıbridas, combinando
roteamentoIPtradicionalecomutac¸a˜oSDN,facilitandoareproduc¸a˜odecena´riosrealistas
emlargaescala.
[Barloweetal. 2023]adotaumaabordagemunificadaparaconstruc¸a˜o,explorac¸a˜o
e armazenamento de mu´ltiplos modelos SDN, utilizando uma base de dados orientada a
grafosquepermiteacomparac¸a˜odediversosparaˆmetros.
A ana´lise das ferramentas existentes concluiu que nenhuma delas fornece su-
porte a modificac¸o˜es dinaˆmicas ou reconfigurac¸o˜es em tempo de execuc¸a˜o, exigindo
que o usua´rio realize diversas operac¸o˜es manuais, muitas vezes em distintas inter-
faces e aplicativos, para a conduc¸a˜o da experimentac¸a˜o. A pro´xima sec¸a˜o apresenta o
Mininet-GUI,umaferramentaquepreencheessalacunaaoproporcionarumambientede
experimentac¸a˜o integrado e interativo, maximizando as perspectivas de experimentac¸a˜o
emSDN.
3. Mininet-GUI
AarquiteturadoMininet-GUI,apresentadanaFigura1,segueomodelocliente-servidor,
compostoporumbackend,responsa´velporinstanciaregerenciaraexecuc¸a˜odoMininet,
e um frontend, uma aplicac¸a˜o Single Page Application (SPA) que oferece uma inter-
face interativa para a manipulac¸a˜o visual da topologia de rede em um grafo dinaˆmico.
A comunicac¸a˜o entre esses componentes e´ intermediada pela API Broker, que integra
uma API HTTP baseada no padra˜o OpenAPI e um gerenciador de conexo˜es WebSocket,
garantindomaiorflexibilidadeemodularidadea` plataforma.
O backend do Mininet-GUI foi desenvolvido na linguagem Python, devido a` API
nativa do Mininet tambe´m ter sido implementada nessa linguagem. Para a construc¸a˜o da
\n### PDF PAGE 5 \n
Mininet-GUI Frontend Mininet-GUI Backend
Network Controls Mininet Integration
Mininet-GUI Network Manipulation Topology Data Structures
API
Topology Generator Topology Exporter
Broker
F