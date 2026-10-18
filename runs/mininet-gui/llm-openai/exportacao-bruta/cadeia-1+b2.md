# Session Export — Mininet-GUI SBRC 2025, selos F e R

## Session Context

- **Scope:** esta conversa, desde o pedido de restauração de contexto até o pedido de exportação; a conversa anterior está representada apenas como documento fornecido pelo usuário, não como interações deste chat.
- **Workspace:** `D:\user\unipampa\8º Semestre\LEAS\atividades\t8`.
- **Subject:** restauração da avaliação analítica do Mininet-GUI e reavaliação dos selos Funcional (F) e Reprodutível (R) com um registro factual de execução.
- **Sources:** `cadeia-1-session-export.md`, `registro-factual.md`, `instrucoes-oficiais.md`, `reivindicacoes.md` e `artefato.txt` no diretório `t8-leas/runs/mininet-gui/`; o artigo PDF foi identificado no workspace, mas não relido neste chat.
- **Export time:** 2026-10-18 18:47 America/Sao_Paulo.

## Executive Summary

O usuário pediu para retomar uma conversa anterior a partir de uma exportação Markdown. Essa exportação continha um resumo, mas sua transcrição terminava no meio da saída de extração de um PDF. O assistente retomou a conclusão analítica registrada: F = Não atribuir (confiança 35/100 de atribuição pelo comitê oficial) por ausência de versões de dependências no README; R = Indeterminado (55/100), pendente de executar C4 e C5. Nenhum artefato fora executado no chat anterior conforme o resumo.

O usuário forneceu depois `registro-factual.md`, descrevendo uma execução única feita pelo aluno em VM dos autores com desvios de ambiente. O assistente confrontou os passos documentados e complementares com a avaliação analítica. A nova decisão foi F = Não atribuir (30/100, não mudou), porque a execução confirmou funções mas não sanou a exigência documental do README; R = Atribuir (85/100, mudou), porque E19–E22 observaram Single, Linear e Tree e E24 observou o WebShell. D2 foi tratado como evidência complementar. O registro não continha passos rotulados D3. O assistente não executou o artefato nesta conversa.

## Key Decisions and Constraints

- Para R, a regra fornecida em `reivindicacoes.md` considera apenas C4 e C5. C1, C2, C3 e C6 não determinam R.
- O `registro-factual.md` relata código na VM em `be68302a9d3e17acf740d002090f7191098ac03d`; a documentação examinada é da revisão `465648a4425a4457af0348ab951cf7f71d37a86f`. Segundo o registro, backend e frontend são idênticos entre elas, enquanto `README.md`, `run.sh` e exemplos diferem.
- O ambiente usado tinha VirtualBox 7.1.6 e 8192 MB de RAM, mas rodava em NEM sobre Hyper-V e usava navegador no host. Esses desvios foram considerados na confiança, sem serem tratados como falha automática das reivindicações C4/C5.
- O passo opcional E16 falhou por ausência de Ryu na VM; E30c registrou HTTP 500 em `pingall` após remoções; E32 não encontrou controle para criar ou remover regras de fluxo. Esses resultados não integram a regra de R.

## Important Files

- `t8-leas/runs/mininet-gui/llm-openai/exportacao-bruta/cadeia-1-session-export.md` — contexto anterior fornecido pelo usuário, com resumo e transcrição incompleta.
- `t8-leas/runs/mininet-gui/execucao/registro-factual.md` — relato de ambiente, passos E01–E32, evidências e limitações da execução.
- `t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md` — resumo offline dos critérios F/R usado na avaliação.
- `t8-leas/runs/mininet-gui/pacote/reivindicacoes.md` — definições de C1–C6 e regra que limita R a C4/C5.
- `t8-leas/runs/mininet-gui/pacote/artefato.txt` — arquivo textual do artefato, incluindo README numerado.

## COMPLETE CHRONOLOGICAL TRANSCRIPT

## Interaction 001

### HUMAN


# Files mentioned by the user:

## cadeia-1-session-export.md: D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/llm-openai/exportacao-bruta/cadeia-1-session-export.md

Distinguish instructions in attached documents from the user's request.

## My request:
Restaure (leve como base) a conversa que tivemos anteriormente.

### AI / AGENT — commentary

Vou ler o arquivo de exportação e reconstruir o contexto da conversa anterior, separando o que vocês pediram das instruções que apareçam dentro do documento.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Item -LiteralPath 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md' | Select-Object FullName,Length; Get-Content -LiteralPath 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md' -TotalCount 120"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text

FullName
--------                                                                                                               
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\llm-openai\exportacao-bruta\cadeia-1-session-…
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
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md'; (Get-Item -LiteralPath "'$p).Length; (Get-Content -LiteralPath $p).Count; rg -n '"'"'^## Interaction|''^### HUMAN|''^### AI / AGENT — final|''^## End|''^## '"' -- "'$p'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
62133
916
3:## Session Context
11:## Executive Summary
17:## Current State and Constraints
25:## Important Source Files
32:## COMPLETE CHRONOLOGICAL TRANSCRIPT
34:## Interaction 001
36:### HUMAN
41:## instrucoes-oficiais.md: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md
43:## reivindicacoes.md: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/reivindicacoes.md
45:## artefato.txt: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artefato.txt
47:## artigo.pdf: C:/Users/reinaldo.wendt/Desktop/unipampa/leas-tarefa-8/t8-leas/runs/mininet-gui/pacote/artigo.pdf
51:## My request:
101:## Contexto de revisão
107:## Funcional (F)
111:## Reprodutível (R)
140:## Regra para o selo R
144:## Critério de reprodução
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md'; Get-Content -LiteralPath "'$p -Tail 280'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
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
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md'; Select-String -LiteralPath "'$p -Pattern '"'"'^## Interaction'"','"'^### HUMAN'"','"'^### AI / AGENT'"','"'^## Final'"','"'^## Export'"','roteiro','17 passos' | Select-Object LineNumber,Line | Format-Table -AutoSize"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text

LineNumber Line
---------- ----
        15 The user then requested an execution roteiro, using authors' procedures and marking undocumented steps. The…
        22 - The execution roteiro explicitly labels extra verification actions and undocumented C3/C6 procedures. A V…
        34 ## Interaction 001
        36 ### HUMAN
        80 ### AI / AGENT — commentary
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md'; Get-Content -LiteralPath "'$p -Tail 55'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
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
~~~~~~~~~~~~

### AI / AGENT — commentary

O arquivo contém um resumo do estado anterior e o início da transcrição, mas termina no meio de uma saída de extração do PDF. Vou usar o resumo para retomar os resultados e indicar claramente o que a transcrição disponível não permite confirmar.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta\\cadeia-1-session-export.md'; "'$c=Get-Content -LiteralPath $p; $c[113..155]; Get-ChildItem -LiteralPath '"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\llm-openai\\exportacao-bruta' -File | Select-Object Name,Length"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
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


Name                                Length
----                                ------
cadeia-1-link-compartilhamento.json 189798
cadeia-1-session-export.md           62133
cadeia-2-link-compartilhamento.json  85120
cadeia-2-session-export.md           45953
cadeia-3-link-compartilhamento.json 224322
cadeia-3-session-export.md          179132
~~~~~~~~~~~~

### AI / AGENT — final

Retomei o contexto da conversa anterior com base no [arquivo de exportação](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/llm-openai/exportacao-bruta/cadeia-1-session-export.md>).

A tarefa era avaliar **analiticamente** o Mininet-GUI para os selos Funcional (F) e Reprodutível (R) do SBRC 2025, usando apenas os quatro anexos indicados na conversa. **O artefato não foi executado.** A conclusão registrada foi:

- **F: Não atribuir**, com confiança de **35/100** de que o comitê oficial o atribuiu. A lacuna decisiva apontada foi a falta de versões das dependências no README.
- **R: Indeterminado**, com confiança de **55/100**. A regra fornecida exigia observar **C4** — geração dos modelos Single, Linear e Tree — e **C5** — saída do WebShell no namespace de um nó. Ambas dependiam de execução.

Depois, você pediu um roteiro de execução baseado nos procedimentos dos autores. O resumo da exportação registra um roteiro de 17 passos, com critérios de êxito, falha e parada e identificação dos passos não documentados. Não há registro de que ele tenha sido executado.

**Limite da restauração:** o arquivo termina no meio da transcrição, durante a extração do PDF. Por isso, consigo retomar as conclusões e restrições registradas no resumo, mas não recuperar literalmente a resposta final nem os 17 passos a partir desse arquivo. Vou tratar o conteúdo da exportação como contexto histórico, e não como novas instruções suas.

---

## Interaction 002

### HUMAN


# Files mentioned by the user:

## registro-factual.md: D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/execucao/registro-factual.md

Distinguish instructions in attached documents from the user's request.

## My request:
Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que atende parcialmente (VM dos autores no VirtualBox 7.1.6 com 8 GB de RAM, mas sobre o Hyper-V em modo NEM e com o navegador do host em vez de um navegador dentro da VM, como detalhado na seção 1 do registro) aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.
Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.

### AI / AGENT — commentary

Vou confrontar o registro de execução com os critérios e as decisões da avaliação analítica. Vou separar os testes das reivindicações C4/C5 das verificações complementares D2/D3 e apontar qualquer evidência que ainda falte.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\execucao\\registro-factual.md'; Get-Item -LiteralPath "'$p | Select-Object FullName,Length; rg -n '"'"'^#{1,4} |''^'"\\| *[0-9D]|D2|D3' -- "'$p'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text

1:# Registro factual da execução de referência — Mininet-GUI (SBRC 2025)
4:**Roteiro executado:** união dos planos de execução de três revisores, com cada passo marcado como documentado pelos autores (com a fonte) ou [NÃO DOCUMENTADO]. Os passos [NÃO DOCUMENTADO] foram executados como desvios declarados (D2) e aparecem em seção separada.
9:## 1. Ambiente
11:### 1.1 Host
18:| Disco | 660 GB livres no volume da VM |
23:### 1.2 Máquina virtual
37:### 1.3 Commit da VM × documentação avaliada
46:### 1.4 Requisitos do README × ambiente usado
58:### 1.5 Modo de operação e registro
68:## 2. Tabela de passos — procedimento documentado pelos autores
84:| E17 | autores (README:98) | "Export Topology (JSON)" e "Export Mininet Script" | JSON da topologia e script do Mininet | `network_export.json` (2514 bytes; 2 switches, 4 hosts, 2 controladores, 5 links) e `network_export.py` (1105 bytes; `Mininet(...)`, `addController` c1 e `c2` RemoteController 127.0.0.1:6633, 4 hosts com IP/MAC, 5 `addLink`, `CLI(net)`); o `.py` passa em `ast.parse` | `exportados/network_export.json` SHA-256 `b188381b6952ee5f901ac337a2e0a9d4a902bcc73b60da9dbf53fe29ea116866`; `exportados/network_export.py` SHA-256 `66eccd22d0d99459719eb298f4b14c54701ff0a3cb4e49e2b83bd6860a458b9d`; `telas/…185112Z-E17-apos-exportar.png` | sucesso | D0 (validação do JSON e da sintaxe: D2) |
85:| E19 | autores (README:107-108); quantidade escolhida pelos revisores | Single, c1, Hosts = 3 | topologia Single "com o número de dispositivos" escolhido | grafo: `s1`, `h1`–`h3`, 3 links host–switch + associação `s1`–`c1`; API: 1 switch, 3 hosts, 3 links (18:51:58–18:52:18Z) | `telas/…185210Z-E19-single3-formulario.png`, `…185217Z-E19-single3-grafo.png`; `terminal.txt` (E19-api) | sucesso | D0 (valor: D2) |
86:| E20 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 3, Hosts per switch 2 | topologia Linear com a quantidade escolhida | grafo: `s1`–`s2`–`s3` em cadeia, 2 hosts por switch (`h1`–`h6`), 8 links; API: 3 switches, 6 hosts, 8 links (18:52:35–18:52:55Z). Os hosts de cada switch aparecem empilhados e encobrem os rótulos `h1`, `h3`, `h5`. | `telas/…185248Z-E20-linear3x2-formulario.png`, `…185255Z-E20-linear3x2-grafo.png`; `terminal.txt` (E20-api) | sucesso | D0 (valores: D2) |
87:| E21 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 2, Hosts per switch 1 | idem | grafo e API: 2 switches, 2 hosts, 3 links (`s1`–`h1`, `s2`–`h2`, `s1`–`s2`) (18:53:13–18:53:34Z) | `telas/…185327Z-E21-…`, `…185334Z-E21-linear2x1-grafo.png`; `terminal.txt` (E21-api) | sucesso | D0 (valores: D2) |
88:| E22 | autores (README:107-108); quantidades escolhidas pelos revisores | Tree, c1, Layers 2, Fanout 2 | topologia Tree com a quantidade escolhida | grafo: raiz `s3`, filhos `s1` e `s2`, 2 hosts em cada (`h1`–`h4`), 6 links; API: 3 switches, 4 hosts, 6 links (18:53:44–18:54:05Z). Os hosts ficaram abaixo da área visível; a vista foi deslocada arrastando o fundo do grafo. | `telas/…185357Z-E22-tree2x2-formulario.png`, `…185404Z-E22-tree2x2-grafo.png`, `…185432Z-E22-tree2x2-grafo-deslocado.png`; `terminal.txt` (E22-api) | sucesso | D0 (valores: D2) |
89:| E24 | autores (README:112-114); comando escolhido pelos revisores (artigo p. 7, Fig. 2) | aba `h1` do WebShell: `ip addr show` | saída "no namespace daquele nó" | na aba `h1`: `lo` 127.0.0.1/8 e `h1-eth0@if40` 10.0.0.1/8, MAC 00:00:00:00:00:01 (18:54:41–18:54:48Z) | `telas/…185448Z-E24-h1-ip-addr.png`; `saidas-interface.txt` | sucesso | D0 (comando: D2) |
93:## 3. Passos [NÃO DOCUMENTADO] (desvios declarados, D2)
99:| E01 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Registrar host, VirtualBox e recursos | requisitos registrados | ver seção 1 | `evidencias/host/host.txt`, `vbox-comandos.txt`, `vbox-execucao-trechos.txt` | sucesso | D2 |
100:| E03 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | SHA-256 da OVA | hash registrado | `9018352deec76c1ef47b15c0d6b7155fbd7ed090d34e8f97a0a302d299fc7455`; os autores não publicam hash | preparação | sucesso | D2 |
101:| E05 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Conferir e ajustar RAM/CPU | ≥ 8 GB | OVA com 1536 MB e 1 vCPU; ajustada para 8192 MB e 2 vCPUs | `vbox-comandos.txt` | sucesso | D2 |
102:| E07 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | `git rev-parse HEAD`, `status --short`, `describe` | commit registrado | `be68302a9d3e17acf740d002090f7191098ac03d`, árvore limpa, `v0.0.1-2-gbe68302`, ≠ `465648a4` (ver 1.3). O `git log` abriu o paginador e consumiu o caractere seguinte; o marcador de fim deste passo não foi gravado. | `terminal.txt` (E07) | sucesso | D2 |
103:| E08 | [NÃO DOCUMENTADO] proposto pelos revisores | pré-condição | Inspecionar `api.js` (linha 299) e o carregamento do nvm, sem corrigir | registrar | linha 299 de `mininet-gui-frontend/src/core/api.js` contém `}i`; nada foi corrigido; o frontend compilou e funcionou (E09–E32). `~/.bashrc` (linhas 120–122) carrega o nvm. | `terminal.txt` (E08) | sucesso | D2 |
104:| E15 | [NÃO DOCUMENTADO] proposto pelos revisores | apoio a C3 | `command -v ryu-manager`; `python3 -c "import ryu"` | caminho do Ryu | código 1, sem caminho; `ModuleNotFoundError: No module named 'ryu'` | `terminal.txt` (E15) | falha | D2 |
105:| E18 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | "Reset Topology" (diálogo confirmado) antes de cada modelo; recriar `c1` Default | grafo e API vazios | 5 resets (18:51:37Z, 18:52:26Z, 18:53:0xZ, 18:53:3xZ, 19:01:40Z); depois de cada um, grafo vazio e API com 0 controllers/switches/hosts/links | `telas/…185144Z-E18-reset-1.png`; `terminal.txt` (E18-*) | sucesso | D2 |
106:| E23 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | Contar nós e links pela API após cada modelo | contagens iguais às escolhidas | iguais nos 4 casos (ver E19–E22) | `terminal.txt` (E19-api … E22-api) | sucesso | D2 |
107:| E25 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h2`: `ip addr show` | `h2-eth0` com IP diferente do de `h1` | `h2-eth0@if41` 10.0.0.2/8, MAC 00:00:00:00:00:02 | `telas/…185455Z-E25-h2-ip-addr.png` | sucesso | D2 |
108:| E26 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h1`: `ping -c 2 10.0.0.2` | respostas | 2 transmitidos, 2 recebidos, 0% de perda | `telas/…185511Z-E26-h1-ping.png` | sucesso | D2 |
109:| E27 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | Comparar com o terminal da VM; nas abas, `readlink /proc/$$/ns/net` | namespaces distintos dos da VM | shell da aba `h1` no `net:[4026532228]`, o mesmo do processo `mininet:h1` (pid 3801); aba `h2` no `net:[4026532269]`, o mesmo de `mininet:h2` (pid 3803); shell da VM no `net:[4026531992]`. `ip -br addr` da VM mostra `eth0` 192.168.56.101 e as portas dos switches, sem `h1-eth0`/`h2-eth0`. | `telas/…185535Z-E27-h2-netns.png`, `…185537Z-E27-h1-netns.png`; `terminal.txt` (E27-vm, E27-ps) | sucesso | D2 |
110:| E28a | [NÃO DOCUMENTADO] proposto pelos revisores | C1 | Arrastar `h1` e recarregar a página | posição mantida | canvas: (50, 450) → (−205, 389); API `/hosts` gravou (−204,73; 388,86); após recarregar, (−204, 388). Uma tentativa anterior (18:55:49Z) partiu de coordenada errada da automação e não moveu o nó. | `telas/…185629Z-E28-depois-mover.png`, `…185640Z-E28-apos-reload.png`; `terminal.txt` (E28-api) | sucesso | D2 |
111:| E28b | [NÃO DOCUMENTADO] proposto pelos revisores | C1 (e adição para C3) | Soltar "Switch" e "Host" da paleta no grafo; "Create Link" `h5`→`s4`, `s4`→`s1`, `s4`→`c1`, com a rede em execução | nós e links aparecem | `s4` e `h5` criados sem formulário; links `h5`–`s4` e `s4`–`s1` em verde; associação `s4`–`c1` tracejada; API: 4 switches, 5 hosts, 8 links, `start=true`. O ponto em que o nó aparece fica ~250 px à direita do ponto onde foi solto. | `telas/…185658Z-E28-paleta-nos.png`, `…185723Z-E28-links-paleta.png`; `terminal.txt` (E28-api2) | sucesso | D2 |
112:| E29 | [NÃO DOCUMENTADO] proposto pelos revisores | C2 (e C3) | `curl /api/mininet/start` e `/hosts`; "Run Pingall Test" | `true`, hosts iguais aos do grafo; tabela | `true`; hosts h1–h5 (10.0.0.1–.5/8); Pingall: **20/20 pares** com 1/1, incluindo `h5`, criado com a rede em execução | `telas/…185739Z-E29-pingall.png`; `saidas-interface.txt` | sucesso | D2 |
113:| E30a | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o link `h2`–`s1`, "Delete Selected" | link some do grafo e da API | some do grafo e de `/links` (7 links); `start=true`; log: `DELETE /api/mininet/delete_link/h2/s1` 200 OK | `telas/…185805Z-E30-link-selecionado.png`, `…185808Z-E30-link-removido.png` | sucesso | D2 |
114:| E30b | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o nó `h4`, "Delete Selected" | nó some do grafo e da API | `h4` some do grafo, da lista de abas e de `/hosts` (4 hosts); `/links` **continua listando `['h4','s2']`**; log: `DELETE /api/mininet/delete_node/h4` 200 OK | `telas/…185819Z-E30-no-selecionado.png`, `…185830Z-E30-no-removido.png`; `terminal.txt` (E30-api-no) | sucesso (com resíduo em `/links`) | D2 |
115:| E30c | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | "Run Pingall Test" após as remoções | Pingall sem o nó removido | alerta "Network Error"; modal "No ping results available."; backend `POST /api/mininet/pingall` **500 Internal Server Error**, `AttributeError: 'NoneType' object has no attribute 'IP'` em `pingFull()` (api.py:157) | `telas/…190107Z-E30-pingall-apos-remocao.png`; `vm/backend-nohup.txt` (linhas 2517–2574) | falha | D2 |
116:| E30d | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Confirmar a emulação ativa: `/start`, reinícios no log, `ping -c 2 10.0.0.3` na aba `h1` | emulação ativa, sem reinício | `start=true`; "Creating network" aparece 10 vezes no log antes e depois das remoções (2 na partida + 2 por reset × 4 resets anteriores; nenhuma nova); `h1` alcança 10.0.0.3 com 0% de perda e mantém a interface `h1-eth0@if40` vista em E24 | `telas/…190130Z-E30-h1-ping-h3-apos-remocao.png`; `terminal.txt` (E30-depois) | sucesso | D2 |
117:| E31 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Reset; `c1`; Single 2 hosts; Pingall; duplo clique em `s1`; aba "Flow Table" | tabela com ao menos uma regra | modal "Node Info: s1" com abas Details e Flow Table; Flow Table com **5 regras** (prioridade 65535, idle timeout 60, campos de match ARP e ICMP entre 10.0.0.1 e 10.0.0.2), lidas cerca de 5 s após o Pingall | `telas/…190214Z-E31-node-info-s1.png`, `…190225Z-E31-flow-table-s1.png`; `saidas-interface.txt` | sucesso | D2 |
118:| E32 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Procurar no modal e na página um controle para inserir ou remover regra | controle presente, ou ausência registrada | controles do modal: "X", "Details", "Flow Table"; da página: Generate/Reset Topology, Create Link, Delete Selected, Run Pingall Test, Export/Import, ocultar barra, abas do WebShell. **Nenhum controle para criar ou remover regra de fluxo.** | `saidas-interface.txt` (E32); `telas/…190237Z-E32-modal-details.png` | falha (controle não encontrado) | D2 |
120:## 4. Resultados por reivindicação
126:| C1 | elementos criados pelo usuário representados no grafo e respondendo às ações | E10–E12 (autores); E28a–E28b (D2) | Controlador, switch, hosts e links criados pela interface aparecem no grafo e nas abas do WebShell. Um nó arrastado mantém a posição após recarregar a página. Nós soltos da paleta aparecem e podem ser ligados. Duas gerações sucessivas sem reset (E16) produziram nós sobrepostos nas mesmas coordenadas. |
127:| C2 | nós emulados e resultado de `pingall` exibido na interface | E12–E13 (autores); E29, E31 (D2) | Pingall exibido na interface: 2/2 pares (E13), 20/20 pares com 5 hosts (E29) e 2/2 pares (E31). A API informa `start=true`, e os hosts têm interfaces e IPs próprios. |
128:| C3 | rede alterada enquanto a emulação continua ativa | E16 (autores, opcional); E28b, E29, E30a–E30d (D2) | **Adição com a rede ativa:** segunda topologia, link `s1`–`s2` (E16) e `s4`/`h5` com links (E28b), sem reinício; `h5` respondeu no Pingall (20/20). **Remoção com a rede ativa:** link e nó removidos do grafo e do Mininet sem reinício (o log não tem novo "Creating network", e `h1` segue alcançando `h3`). Depois das remoções, o Pingall da interface falhou com HTTP 500 e `/links` manteve a entrada do nó removido. O passo 8 do README não se completou: `ryu-manager` não existe na VM, e não houve conectividade entre as duas topologias. |
129:| C4 | topologia de cada modelo gerada com a quantidade de dispositivos escolhida | E19–E22 (autores; quantidades escolhidas pelos revisores); E18, E23 (D2) | Single (3 hosts), Linear (3×2 e 2×1) e Tree (2 níveis, fanout 2) gerados. Contagens de switches, hosts e links iguais às escolhidas no grafo e na API, nos quatro casos. |
130:| C5 | saída do comando exibida na aba do nó selecionado | E14, E24 (autores); E25–E27 (D2) | `ip addr show` na aba `h1` mostra `h1-eth0` 10.0.0.1/8; na aba `h2`, `h2-eth0` 10.0.0.2/8. O shell de cada aba está no namespace de rede do respectivo nó, diferente do namespace da VM. O `iperf` entre as abas `h1` e `h2` mediu 6,62 Gbit/s. |
131:| C6 | tabela de fluxo exibida, com a regra inserida ou removida no switch | E31–E32 (D2; os autores não documentam procedimento) | A tabela de fluxo de `s1` é exibida (5 regras instaladas pelo controlador após o Pingall). A interface não oferece controle para inserir ou remover regras. |
135:## 5. Insumos ausentes e respostas dos autores
143:## 6. Limitações e incidentes
FullName                                                                                              Length
--------                                                                                              ------
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\execucao\registro-factual.md  27971
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Content -LiteralPath 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\execucao\\registro-factual.md' -Encoding utf8"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
# Registro factual da execução de referência — Mininet-GUI (SBRC 2025)

**Data da execução:** 2026-10-17, das 18:34:47Z (restauração do snapshot) às 19:03:35Z (VM desligada). Todas as horas estão em UTC. **Execução:** única, feita pelo aluno, com a operação automatizada por um agente de software autorizado por ele (ver "Modo de operação").
**Roteiro executado:** união dos planos de execução de três revisores, com cada passo marcado como documentado pelos autores (com a fonte) ou [NÃO DOCUMENTADO]. Os passos [NÃO DOCUMENTADO] foram executados como desvios declarados (D2) e aparecem em seção separada.
**Documentação avaliada:** `README.md` do commit `465648a4425a4457af0348ab951cf7f71d37a86f`. As citações "README:N" usam a numeração de linhas desse arquivo.

Este registro descreve fatos observados. Ele não contém avaliação dos selos.

## 1. Ambiente

### 1.1 Host

| Item | Valor |
|---|---|
| Sistema | Windows 11 Home, build 26300, 64 bits |
| CPU | Intel Core i5-13450HX, 10 núcleos e 16 threads |
| RAM | 16.069 MB no total. Antes de ligar a VM havia cerca de 753 MB livres; o `VBox.log` registrou "Host RAM: 16068MB (15.6GB) total, 725MB available". Outros programas estavam abertos, entre eles contêineres Docker de outra tarefa. |
| Disco | 660 GB livres no volume da VM |
| Hipervisor | Oracle VirtualBox **7.1.6 r167084**, a mesma versão pedida em README:37 |
| Motor de execução | O Hyper-V do Windows está ativo e o VT-x não fica disponível para o VirtualBox. O `VBox.log` registra "HM: HMR3Init: Attempting fall back to NEM: VT-x is not available" e "NEM: NEMR3Init: Snail execution mode is active!". A VM rodou sobre a API do Hyper-V (NEM), não em VT-x nativo. |
| Navegador | Microsoft Edge 155.0.4283.45 no host, em modo headless, com janela de 1600×1000 |

### 1.2 Máquina virtual

| Item | Valor |
|---|---|
| Origem | release `v0.0.1` "VM SBRC 2025" do repositório dos autores (`Mininet-GUI-VM-SBRC-2025.zip`, 1.303.516.409 bytes, SHA-256 `3a484c2d…5364e4bc`; OVA SHA-256 `9018352d…99fc7455`, cujo manifesto SHA-1 interno confere). O link do Google Drive em README:53 abria a página "O arquivo que você solicitou não existe" quando foi consultado em 15/10/2026. |
| Nome da imagem | `Mininet-GUI-VM-SBRC-2025.ova`. README:55 cita outro nome, `Mininet-GUI-Desktop-VM-SBRC-2025.ova`. |
| Estado inicial | snapshot `02-apos-identificacao` (VM importada, ajustada e já iniciada uma vez só para identificação, sem ter executado `mininet_gui`) |
| Recursos | **8192 MB de RAM**, 2 vCPUs, disco de 8 GiB (3,2 GB livres), rede host-only (`192.168.56.101`), sem acesso à Internet. A OVA vinha com 1536 MB e 1 vCPU. |
| SO | Ubuntu 20.04.1 LTS, kernel `5.4.0-42-generic #46-Ubuntu`, x86_64 |
| Interface gráfica | não há; a VM inicia em console texto (tty1). O acesso foi por SSH com o usuário e a senha publicados pelos autores (`mininet`/[senha omitida]). |
| Versões | Mininet 2.3.0; Open vSwitch 2.13.1; Python 3.8.5; Node v18.20.7 e npm 10.8.2 (via nvm, em shell interativo); vite 4.5.9; iperf 2.0.13; `ryu-manager` **ausente** (não há módulo `ryu`) |
| Pico de memória da VM | 257 MB usados de 7962 MB (`free -m` às 19:02:53Z) |
| Código na VM | `/home/mininet/[senha omitida]-gui` em **`be68302a9d3e17acf740d002090f7191098ac03d`** (`v0.0.1-2-gbe68302`, branch `sbrc2025`), com a árvore limpa |

### 1.3 Commit da VM × documentação avaliada

O commit da VM (`be68302`) é ancestral do commit da documentação avaliada (`465648a4`), com 16 commits entre os dois.

- Os 41 arquivos do projeto na VM são idênticos aos de `be68302`.
- Entre `be68302` e `465648a4` mudam apenas `README.md`, `run.sh` e dois arquivos de exemplo (`example_network_export.json` e `.py`, que não existem na VM).
- **Nenhum arquivo de `mininet-gui-backend/` ou `mininet-gui-frontend/` difere.**
- No `run.sh`, a versão `465648a4` acrescenta `nvm use 18.20.7 ;` antes de `nohup npm run dev &`. Na VM, o Node 18 já vem do `~/.bashrc` em shell interativo.

### 1.4 Requisitos do README × ambiente usado

| Requisito | Fonte | Valor usado |
|---|---|---|
| VirtualBox 7.1.6 r167084 | README:37 | 7.1.6 r167084 |
| RAM da VM: "Mínimo de 8GB" | README:38 | 8192 MB |
| RAM da VM: "no mínimo 2GB" e "um core de CPU" | README:103 | 8192 MB, 2 vCPUs |
| Host de demonstração: i5-10300H, 8 GB, Windows 11 Home, 80 GB livres | README:26-32 | i5-13450HX, 16 GB, Windows 11 Home, 660 GB livres; Hyper-V ativo (NEM). O README não fala de Hyper-V. |
| VM `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (Google Drive) | README:53-55 | `Mininet-GUI-VM-SBRC-2025.ova` da release `v0.0.1` (link do Drive inativo) |
| Navegador "dentro da VM" | README:86 | navegador do host via rede host-only. A VM da release não tem ambiente gráfico; o texto da release manda abrir a URL "em um navegador", com o exemplo `http://192.168.56.101:5173`. |
| Terminal com Ctrl+Alt+T | README:84 | sessão SSH com bash interativo (carrega o alias `mininet_gui` e o nvm do `~/.bashrc`) |

### 1.5 Modo de operação e registro

- **Terminal da VM:** uma única sessão bash interativa gravada com `script -t`, pelo script `gravar-sessao.sh`, das 18:36:48Z às 19:02:5xZ. Arquivos: [`terminal.txt`](terminal.txt) (SHA-256 `6ffa9cc8…12865`) e [`tempo.txt`](tempo.txt) (`fa7c8e50…a2976`), que podem ser reproduzidos com `scriptreplay -t tempo.txt terminal.txt`. Os comandos foram enviados à sessão por um FIFO. Cada comando é cercado por marcadores `[passo=… inicio=…]` e `[passo=… saida=<código> fim=…]`.
- **Interface web:** operada no Edge headless do host pelo Chrome DevTools Protocol (script `evidencias/ferramentas/cdp.mjs`).
  - Cliques, arrastes (inclusive o arraste HTML5 da paleta), roda do mouse e teclas foram enviados como eventos de entrada do navegador (`Input.dispatch*`).
  - Nos campos `<select>`, o valor foi atribuído por JavaScript, com o disparo dos eventos `input` e `change`.
  - As posições dos nós e as listas de nós e arestas foram lidas do componente Vue da página, só para leitura.
  - Cada captura recebeu, só no momento da captura, um carimbo com a hora UTC e o rótulo do passo, no canto inferior direito.
- **Evidências:** [`evidencias/telas/`](evidencias/telas/) (65 PNG, SHA-256 em `telas.sha256`), [`evidencias/saidas-interface.txt`](evidencias/saidas-interface.txt) (texto lido da página em cada passo), [`evidencias/exportados/`](evidencias/exportados/), [`evidencias/vm/`](evidencias/vm/) (gravação, logs `nohup.out` do backend e do frontend, conferidos por SHA-256 após a transferência) e [`evidencias/host/`](evidencias/host/) (comandos do VirtualBox, trechos do `VBox.log`, dados do host).

## 2. Tabela de passos — procedimento documentado pelos autores

Status: **sucesso** (esperado observado), **falha** (esperado não observado), **inconclusivo**, **bloqueado**. "Esperado" é o texto dos autores; quando eles não o fixam, a tabela diz isso.

| Passo | Origem | Ação | Esperado | Observado | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|
| E02 | autores (README:53; release `v0.0.1`) | Obter a VM | arquivo `.ova` da VM | link do README inativo; ZIP/OVA da release dos autores obtido e íntegro (CRC e manifesto conferem) | `ambiente/ambiente.md` (preparação) | sucesso | D1: fonte alternativa dos próprios autores |
| E04 | autores (README:55) | Importar a OVA | VM importada | importada sem erro | idem | sucesso | D0 |
| E06 | autores (README:57, 82) | Iniciar a VM e entrar | sessão aberta | boot até o login em ~95 s (18:34:48Z → SSH às 18:36:23Z); console texto, sem área de trabalho; login por SSH | `telas/20261017T183635Z-E06-console-boot.png`; `evidencias/host/vbox-comandos.txt` | sucesso | D1: SSH em vez de terminal gráfico |
| E09 | autores (README:84) | `mininet_gui` | "mostrará … uma URL" (README:86) | código de saída 0 em 0,2 s (18:41:10.720–.942Z); imprimiu "Mininet-GUI bootstrap complete" e `http://192.168.56.101:5173`; uvicorn em :8000 e vite em :5173 ("VITE v4.5.9 ready in 4713 ms") às 18:41:32Z | `terminal.txt` (passos E09, E09-verif); `vm/frontend-nohup.txt`, `vm/backend-nohup.txt` | sucesso | D0 |
| E10 | autores (README:86; release, Teste mínimo passo 3) | Abrir a URL impressa | interface web | página "Mininet-GUI" com barra lateral (Topology Controls, Actions, Export/Import, Nodes Palette), área do grafo e painel "WebShell" | `telas/…184317Z-E10-interface-1600x1000.png` | sucesso | D1: navegador do host |
| E11 | autores (README:88) | Arrastar "Controller", "Default", "Submit" | controlador criado | formulário "Controller Type: Default/Remote"; nó `c1` no grafo e aba `C1` no WebShell (18:43:26–18:43:42Z) | `telas/…184332Z-E11-dialogo-controller.png`, `…184341Z-E11-c1-criado.png` | sucesso | D0 |
| E12 | autores (README:90) | "Generate Topology": Single, c1, Hosts 2, "Submit" | topologia gerada | `s1`, `h1`, `h2`; links `s1`–`h1` e `s1`–`h2` em verde; `s1`–`c1` cinza tracejado; abas C1 S1 H1 H2; rede iniciada (18:43:51–18:44:11Z) | `telas/…184355Z-E12-formulario-single.png`, `…184411Z-E12-topologia-single.png` | sucesso | D0 |
| E13 | autores (README:92) | "Run Pingall Test" | "aguarde os resultados aparecerem" | em menos de 2 s, tabela "Pingall Results": h1→h2 e h2→h1, 1 enviado/1 recebido cada (RTT 24,340 e 4,674 ms) | `telas/…184422Z-E13-pingall.png`; `saidas-interface.txt` | sucesso | D0 |
| E14 | autores (README:94, opcional) | aba `h1`: `iperf -s`; aba `h2`: `iperf -c 10.0.0.1`; aguardar 1 min | teste completa em 1 min | `h2`: "0.0-10.0 sec 7.71 GBytes 6.62 Gbits/sec"; `h1` registrou a conexão de 10.0.0.2 com o mesmo valor; servidor encerrado com Ctrl+C (18:46:25–18:47:49Z). Uma tentativa anterior (18:44:37–18:46:00Z) não digitou nada porque o modal do Pingall continuava aberto sobre a página; ver Limitações. | `telas/…184629Z-E14-iperf-servidor-h1.png`, `…184738Z-E14-iperf-cliente-h2.png`, `…184742Z-E14-iperf-servidor-h1-relatorio.png` | sucesso | D0 |
| E16 | autores (README:96, opcional) | Controller Remote 127.0.0.1:6633 (`c2`); Single, 2 hosts, c2; "Create Link" `s1`→`s2`; na aba `c2`, `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; Pingall | "linha verde conectando os dois nós"; Ryu iniciado; teste de conexão | `c2 <127.0.0.1:6633>` criado em 3 s; `s2`, `h3`, `h4` gerados **nas mesmas coordenadas de tela** de `s1`, `h1`, `h2`, sobrepostos; os três nós foram afastados arrastando-os no grafo; link `s1`–`s2` criado em verde (`#00aa00ff`); na aba `c2`, "Command 'ryu-manager' not found, but can be installed with: apt install python3-ryu"; Pingall (~30 s): h1↔h2 com 1/1, os outros 10 pares com 0 recebidos | `telas/…184824Z-E16-single-c2.png`, `…184844Z-E16-nos-afastados.png`, `…184928Z-E16-link-s1-s2.png`, `…184945Z-E16-ryu-c2.png`, `…185024Z-E16-pingall-resultado.png` | falha (Ryu ausente na VM; sem conectividade entre as duas topologias) | D1: nós afastados à mão para permitir o arraste |
| E17 | autores (README:98) | "Export Topology (JSON)" e "Export Mininet Script" | JSON da topologia e script do Mininet | `network_export.json` (2514 bytes; 2 switches, 4 hosts, 2 controladores, 5 links) e `network_export.py` (1105 bytes; `Mininet(...)`, `addController` c1 e `c2` RemoteController 127.0.0.1:6633, 4 hosts com IP/MAC, 5 `addLink`, `CLI(net)`); o `.py` passa em `ast.parse` | `exportados/network_export.json` SHA-256 `b188381b6952ee5f901ac337a2e0a9d4a902bcc73b60da9dbf53fe29ea116866`; `exportados/network_export.py` SHA-256 `66eccd22d0d99459719eb298f4b14c54701ff0a3cb4e49e2b83bd6860a458b9d`; `telas/…185112Z-E17-apos-exportar.png` | sucesso | D0 (validação do JSON e da sintaxe: D2) |
| E19 | autores (README:107-108); quantidade escolhida pelos revisores | Single, c1, Hosts = 3 | topologia Single "com o número de dispositivos" escolhido | grafo: `s1`, `h1`–`h3`, 3 links host–switch + associação `s1`–`c1`; API: 1 switch, 3 hosts, 3 links (18:51:58–18:52:18Z) | `telas/…185210Z-E19-single3-formulario.png`, `…185217Z-E19-single3-grafo.png`; `terminal.txt` (E19-api) | sucesso | D0 (valor: D2) |
| E20 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 3, Hosts per switch 2 | topologia Linear com a quantidade escolhida | grafo: `s1`–`s2`–`s3` em cadeia, 2 hosts por switch (`h1`–`h6`), 8 links; API: 3 switches, 6 hosts, 8 links (18:52:35–18:52:55Z). Os hosts de cada switch aparecem empilhados e encobrem os rótulos `h1`, `h3`, `h5`. | `telas/…185248Z-E20-linear3x2-formulario.png`, `…185255Z-E20-linear3x2-grafo.png`; `terminal.txt` (E20-api) | sucesso | D0 (valores: D2) |
| E21 | autores (README:107-108); quantidades escolhidas pelos revisores | Linear, c1, Switches 2, Hosts per switch 1 | idem | grafo e API: 2 switches, 2 hosts, 3 links (`s1`–`h1`, `s2`–`h2`, `s1`–`s2`) (18:53:13–18:53:34Z) | `telas/…185327Z-E21-…`, `…185334Z-E21-linear2x1-grafo.png`; `terminal.txt` (E21-api) | sucesso | D0 (valores: D2) |
| E22 | autores (README:107-108); quantidades escolhidas pelos revisores | Tree, c1, Layers 2, Fanout 2 | topologia Tree com a quantidade escolhida | grafo: raiz `s3`, filhos `s1` e `s2`, 2 hosts em cada (`h1`–`h4`), 6 links; API: 3 switches, 4 hosts, 6 links (18:53:44–18:54:05Z). Os hosts ficaram abaixo da área visível; a vista foi deslocada arrastando o fundo do grafo. | `telas/…185357Z-E22-tree2x2-formulario.png`, `…185404Z-E22-tree2x2-grafo.png`, `…185432Z-E22-tree2x2-grafo-deslocado.png`; `terminal.txt` (E22-api) | sucesso | D0 (valores: D2) |
| E24 | autores (README:112-114); comando escolhido pelos revisores (artigo p. 7, Fig. 2) | aba `h1` do WebShell: `ip addr show` | saída "no namespace daquele nó" | na aba `h1`: `lo` 127.0.0.1/8 e `h1-eth0@if40` 10.0.0.1/8, MAC 00:00:00:00:00:01 (18:54:41–18:54:48Z) | `telas/…185448Z-E24-h1-ip-addr.png`; `saidas-interface.txt` | sucesso | D0 (comando: D2) |

Tempo do teste mínimo (E09–E17): 18:41:10Z → 18:51:12Z. Tempo de C4 (E18–E23): 18:51:29Z → 18:54:32Z. Nenhum bloco chegou perto do limite de 2 h.

## 3. Passos [NÃO DOCUMENTADO] (desvios declarados, D2)

Todos foram propostos pelos revisores e não constam da documentação dos autores. São evidência complementar.

| Passo | Origem | Reivindicação | Ação | Esperado (revisores) | Observado | Evidência | Status | Desvio |
|---|---|---|---|---|---|---|---|---|
| E01 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Registrar host, VirtualBox e recursos | requisitos registrados | ver seção 1 | `evidencias/host/host.txt`, `vbox-comandos.txt`, `vbox-execucao-trechos.txt` | sucesso | D2 |
| E03 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | SHA-256 da OVA | hash registrado | `9018352deec76c1ef47b15c0d6b7155fbd7ed090d34e8f97a0a302d299fc7455`; os autores não publicam hash | preparação | sucesso | D2 |
| E05 | [NÃO DOCUMENTADO] proposto pelos revisores | ambiente | Conferir e ajustar RAM/CPU | ≥ 8 GB | OVA com 1536 MB e 1 vCPU; ajustada para 8192 MB e 2 vCPUs | `vbox-comandos.txt` | sucesso | D2 |
| E07 | [NÃO DOCUMENTADO] proposto pelos revisores | rastreabilidade | `git rev-parse HEAD`, `status --short`, `describe` | commit registrado | `be68302a9d3e17acf740d002090f7191098ac03d`, árvore limpa, `v0.0.1-2-gbe68302`, ≠ `465648a4` (ver 1.3). O `git log` abriu o paginador e consumiu o caractere seguinte; o marcador de fim deste passo não foi gravado. | `terminal.txt` (E07) | sucesso | D2 |
| E08 | [NÃO DOCUMENTADO] proposto pelos revisores | pré-condição | Inspecionar `api.js` (linha 299) e o carregamento do nvm, sem corrigir | registrar | linha 299 de `mininet-gui-frontend/src/core/api.js` contém `}i`; nada foi corrigido; o frontend compilou e funcionou (E09–E32). `~/.bashrc` (linhas 120–122) carrega o nvm. | `terminal.txt` (E08) | sucesso | D2 |
| E15 | [NÃO DOCUMENTADO] proposto pelos revisores | apoio a C3 | `command -v ryu-manager`; `python3 -c "import ryu"` | caminho do Ryu | código 1, sem caminho; `ModuleNotFoundError: No module named 'ryu'` | `terminal.txt` (E15) | falha | D2 |
| E18 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | "Reset Topology" (diálogo confirmado) antes de cada modelo; recriar `c1` Default | grafo e API vazios | 5 resets (18:51:37Z, 18:52:26Z, 18:53:0xZ, 18:53:3xZ, 19:01:40Z); depois de cada um, grafo vazio e API com 0 controllers/switches/hosts/links | `telas/…185144Z-E18-reset-1.png`; `terminal.txt` (E18-*) | sucesso | D2 |
| E23 | [NÃO DOCUMENTADO] proposto pelos revisores | C4 | Contar nós e links pela API após cada modelo | contagens iguais às escolhidas | iguais nos 4 casos (ver E19–E22) | `terminal.txt` (E19-api … E22-api) | sucesso | D2 |
| E25 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h2`: `ip addr show` | `h2-eth0` com IP diferente do de `h1` | `h2-eth0@if41` 10.0.0.2/8, MAC 00:00:00:00:00:02 | `telas/…185455Z-E25-h2-ip-addr.png` | sucesso | D2 |
| E26 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | aba `h1`: `ping -c 2 10.0.0.2` | respostas | 2 transmitidos, 2 recebidos, 0% de perda | `telas/…185511Z-E26-h1-ping.png` | sucesso | D2 |
| E27 | [NÃO DOCUMENTADO] proposto pelos revisores | C5 | Comparar com o terminal da VM; nas abas, `readlink /proc/$$/ns/net` | namespaces distintos dos da VM | shell da aba `h1` no `net:[4026532228]`, o mesmo do processo `mininet:h1` (pid 3801); aba `h2` no `net:[4026532269]`, o mesmo de `mininet:h2` (pid 3803); shell da VM no `net:[4026531992]`. `ip -br addr` da VM mostra `eth0` 192.168.56.101 e as portas dos switches, sem `h1-eth0`/`h2-eth0`. | `telas/…185535Z-E27-h2-netns.png`, `…185537Z-E27-h1-netns.png`; `terminal.txt` (E27-vm, E27-ps) | sucesso | D2 |
| E28a | [NÃO DOCUMENTADO] proposto pelos revisores | C1 | Arrastar `h1` e recarregar a página | posição mantida | canvas: (50, 450) → (−205, 389); API `/hosts` gravou (−204,73; 388,86); após recarregar, (−204, 388). Uma tentativa anterior (18:55:49Z) partiu de coordenada errada da automação e não moveu o nó. | `telas/…185629Z-E28-depois-mover.png`, `…185640Z-E28-apos-reload.png`; `terminal.txt` (E28-api) | sucesso | D2 |
| E28b | [NÃO DOCUMENTADO] proposto pelos revisores | C1 (e adição para C3) | Soltar "Switch" e "Host" da paleta no grafo; "Create Link" `h5`→`s4`, `s4`→`s1`, `s4`→`c1`, com a rede em execução | nós e links aparecem | `s4` e `h5` criados sem formulário; links `h5`–`s4` e `s4`–`s1` em verde; associação `s4`–`c1` tracejada; API: 4 switches, 5 hosts, 8 links, `start=true`. O ponto em que o nó aparece fica ~250 px à direita do ponto onde foi solto. | `telas/…185658Z-E28-paleta-nos.png`, `…185723Z-E28-links-paleta.png`; `terminal.txt` (E28-api2) | sucesso | D2 |
| E29 | [NÃO DOCUMENTADO] proposto pelos revisores | C2 (e C3) | `curl /api/mininet/start` e `/hosts`; "Run Pingall Test" | `true`, hosts iguais aos do grafo; tabela | `true`; hosts h1–h5 (10.0.0.1–.5/8); Pingall: **20/20 pares** com 1/1, incluindo `h5`, criado com a rede em execução | `telas/…185739Z-E29-pingall.png`; `saidas-interface.txt` | sucesso | D2 |
| E30a | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o link `h2`–`s1`, "Delete Selected" | link some do grafo e da API | some do grafo e de `/links` (7 links); `start=true`; log: `DELETE /api/mininet/delete_link/h2/s1` 200 OK | `telas/…185805Z-E30-link-selecionado.png`, `…185808Z-E30-link-removido.png` | sucesso | D2 |
| E30b | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Selecionar o nó `h4`, "Delete Selected" | nó some do grafo e da API | `h4` some do grafo, da lista de abas e de `/hosts` (4 hosts); `/links` **continua listando `['h4','s2']`**; log: `DELETE /api/mininet/delete_node/h4` 200 OK | `telas/…185819Z-E30-no-selecionado.png`, `…185830Z-E30-no-removido.png`; `terminal.txt` (E30-api-no) | sucesso (com resíduo em `/links`) | D2 |
| E30c | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | "Run Pingall Test" após as remoções | Pingall sem o nó removido | alerta "Network Error"; modal "No ping results available."; backend `POST /api/mininet/pingall` **500 Internal Server Error**, `AttributeError: 'NoneType' object has no attribute 'IP'` em `pingFull()` (api.py:157) | `telas/…190107Z-E30-pingall-apos-remocao.png`; `vm/backend-nohup.txt` (linhas 2517–2574) | falha | D2 |
| E30d | [NÃO DOCUMENTADO] proposto pelos revisores | C3 | Confirmar a emulação ativa: `/start`, reinícios no log, `ping -c 2 10.0.0.3` na aba `h1` | emulação ativa, sem reinício | `start=true`; "Creating network" aparece 10 vezes no log antes e depois das remoções (2 na partida + 2 por reset × 4 resets anteriores; nenhuma nova); `h1` alcança 10.0.0.3 com 0% de perda e mantém a interface `h1-eth0@if40` vista em E24 | `telas/…190130Z-E30-h1-ping-h3-apos-remocao.png`; `terminal.txt` (E30-depois) | sucesso | D2 |
| E31 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Reset; `c1`; Single 2 hosts; Pingall; duplo clique em `s1`; aba "Flow Table" | tabela com ao menos uma regra | modal "Node Info: s1" com abas Details e Flow Table; Flow Table com **5 regras** (prioridade 65535, idle timeout 60, campos de match ARP e ICMP entre 10.0.0.1 e 10.0.0.2), lidas cerca de 5 s após o Pingall | `telas/…190214Z-E31-node-info-s1.png`, `…190225Z-E31-flow-table-s1.png`; `saidas-interface.txt` | sucesso | D2 |
| E32 | [NÃO DOCUMENTADO] proposto pelos revisores | C6 | Procurar no modal e na página um controle para inserir ou remover regra | controle presente, ou ausência registrada | controles do modal: "X", "Details", "Flow Table"; da página: Generate/Reset Topology, Create Link, Delete Selected, Run Pingall Test, Export/Import, ocultar barra, abas do WebShell. **Nenhum controle para criar ou remover regra de fluxo.** | `saidas-interface.txt` (E32); `telas/…190237Z-E32-modal-details.png` | falha (controle não encontrado) | D2 |

## 4. Resultados por reivindicação

Os resultados esperados vêm da lista de reivindicações entregue aos revisores. Nenhuma reivindicação tem valor numérico publicado pelos autores. Por isso não há diferenças absolutas nem relativas a calcular.

| ID | Resultado esperado | Passos | Observado |
|---|---|---|---|
| C1 | elementos criados pelo usuário representados no grafo e respondendo às ações | E10–E12 (autores); E28a–E28b (D2) | Controlador, switch, hosts e links criados pela interface aparecem no grafo e nas abas do WebShell. Um nó arrastado mantém a posição após recarregar a página. Nós soltos da paleta aparecem e podem ser ligados. Duas gerações sucessivas sem reset (E16) produziram nós sobrepostos nas mesmas coordenadas. |
| C2 | nós emulados e resultado de `pingall` exibido na interface | E12–E13 (autores); E29, E31 (D2) | Pingall exibido na interface: 2/2 pares (E13), 20/20 pares com 5 hosts (E29) e 2/2 pares (E31). A API informa `start=true`, e os hosts têm interfaces e IPs próprios. |
| C3 | rede alterada enquanto a emulação continua ativa | E16 (autores, opcional); E28b, E29, E30a–E30d (D2) | **Adição com a rede ativa:** segunda topologia, link `s1`–`s2` (E16) e `s4`/`h5` com links (E28b), sem reinício; `h5` respondeu no Pingall (20/20). **Remoção com a rede ativa:** link e nó removidos do grafo e do Mininet sem reinício (o log não tem novo "Creating network", e `h1` segue alcançando `h3`). Depois das remoções, o Pingall da interface falhou com HTTP 500 e `/links` manteve a entrada do nó removido. O passo 8 do README não se completou: `ryu-manager` não existe na VM, e não houve conectividade entre as duas topologias. |
| C4 | topologia de cada modelo gerada com a quantidade de dispositivos escolhida | E19–E22 (autores; quantidades escolhidas pelos revisores); E18, E23 (D2) | Single (3 hosts), Linear (3×2 e 2×1) e Tree (2 níveis, fanout 2) gerados. Contagens de switches, hosts e links iguais às escolhidas no grafo e na API, nos quatro casos. |
| C5 | saída do comando exibida na aba do nó selecionado | E14, E24 (autores); E25–E27 (D2) | `ip addr show` na aba `h1` mostra `h1-eth0` 10.0.0.1/8; na aba `h2`, `h2-eth0` 10.0.0.2/8. O shell de cada aba está no namespace de rede do respectivo nó, diferente do namespace da VM. O `iperf` entre as abas `h1` e `h2` mediu 6,62 Gbit/s. |
| C6 | tabela de fluxo exibida, com a regra inserida ou removida no switch | E31–E32 (D2; os autores não documentam procedimento) | A tabela de fluxo de `s1` é exibida (5 regras instaladas pelo controlador após o Pingall). A interface não oferece controle para inserir ou remover regras. |

**Teste mínimo do README (passos 1–9):** passos 1–6 e 9 com o resultado descrito pelos autores; passo 7 (opcional, iperf) concluído; passo 8 (opcional) com a criação do controlador remoto, da segunda topologia e do link verde, mas sem o Ryu (ausente na VM) e sem conectividade entre as topologias no Pingall.

## 5. Insumos ausentes e respostas dos autores

- **Ryu:** não está instalado na VM da release `v0.0.1`. README:75-78 documenta a instalação do Ryu só para a instalação manual. A VM não tem Internet (rede host-only), e nada foi instalado.
- **Link da VM no README** (README:53): inativo na consulta de 15/10/2026. Foi usada a OVA da release `v0.0.1` dos autores.
- **VM "Desktop" com navegador interno** (README:55, 86): não disponível; a VM da release não tem ambiente gráfico.
- **Valores esperados:** os autores não publicam contagens, saídas de referência, tempos nem vazão. As quantidades de C4 e os comandos de C5 foram escolhidos pelos revisores antes da execução.
- **Contato com os autores:** nenhum foi feito; não há respostas.

## 6. Limitações e incidentes

- **Execução única**, em um único host. Os tempos e as vazões dependem do modo NEM sobre o Hyper-V e da memória livre do host (~725 MB no início).
- **Software × documentação:** a VM roda o commit `be68302`. A documentação avaliada é do commit `465648a4`. Backend e frontend são idênticos; mudam `README.md`, `run.sh` (linha `nvm use 18.20.7`) e dois arquivos de exemplo.
- **Navegador:** a interface foi usada pelo navegador do host, não por um navegador dentro da VM. A interação foi automatizada por eventos de entrada do navegador (CDP), não por uma pessoa com mouse e teclado. Os valores dos `<select>` foram atribuídos por script, com o evento `change`.
- **Incidentes da automação** (as capturas e os textos estão preservados):
  - A primeira captura de E10 saiu em 500×320; foi refeita em 1600×1000.
  - Em E13/E14 e E16/E17, o primeiro clique automático no "X" do modal "Pingall Results" não fechou o modal. Os cliques seguintes caíram na máscara do modal: as teclas do primeiro iperf não chegaram ao terminal, e a primeira tentativa de exportar não baixou nada. Em E14, a aba `h1` chegou a ser ativada uma vez por `click()` em JavaScript, sem efeito nos resultados. Tudo foi repetido depois de fechar o modal.
  - Em E16 e E28a, uma leitura de coordenadas errada fez um arraste começar fora do nó; os arrastes foram repetidos.
  - No fim de E32, três cliques automáticos no modal "Node Info" não o fecharam (`…190243Z-E32-barra-lateral.png`); a barra lateral está registrada em E10.
- **Modal do Pingall:** logo após o clique, o modal mostra "No ping results available." até chegar a resposta. Em E16, a resposta levou cerca de 30 s.
- **Limpeza do Mininet:** ao iniciar, o backend apagou `/tmp/*.out`, onde estava a cópia da saída ao vivo da sessão gravada. A gravação em `~/evidencias` (o `terminal.txt`) não foi afetada.
- **Processos:** havia processos `bash` defuntos (`<defunct>`) filhos do uvicorn depois dos resets (`terminal.txt`, E27-ps).
- **Estado da VM:** o snapshot `02-apos-identificacao` não foi alterado. Depois da execução, a VM foi desligada por ACPI às 19:03:35Z, e foi criado o snapshot `03-apos-execucao-referencia`.
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "rg --files 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui' | rg '(instrucoes-oficiais\\.md|reivindicacoes\\.md|artefato\\.txt|artigo\\.pdf|registro-factual\\.md)"'$'"'"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\referencia\instrucoes-oficiais.md
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\pacote\reivindicacoes.md
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\pacote\instrucoes-oficiais.md
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\pacote\artigo.pdf
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\pacote\artefato.txt
D:\user\unipampa\8º Semestre\LEAS\atividades\t8\t8-leas\runs\mininet-gui\execucao\registro-factual.md
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "rg -n 'README\\.md|====|"'^'"\\d+\\|.*(Requirements|Dependencies|Installation|VM|Teste mínimo|Experimentos|Node|Ryu|VirtualBox|Python|npm|version|versão)' 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt' | Select-Object -First 100"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
7:Para citar evidência use caminho:linha, por exemplo README.md:12.
11:README.md | 9086 | texto | e424434fa7cf0985a9472d2b29c62b46d121d6db8c199428841406ccef1e3753
54:===== INÍCIO DO ARQUIVO: LICENSE (28 linhas) =====
83:===== FIM DO ARQUIVO: LICENSE =====
85:===== INÍCIO DO ARQUIVO: README.md (146 linhas) =====
94:  9| O arquivo README.md divide-se nas seguintes seções: Selos Considerados, Informações Básicas, Dependências, Preocupações com segurança, Instalação, Teste mínimo, Experimentos e LICENSE.
186:101| # Experimentos
188:103| A execução da VM requer no mínimo 2GB de RAM e um core de CPU reservado à VM.
232:===== FIM DO ARQUIVO: README.md =====
234:===== INÍCIO DO ARQUIVO: example_network_export.json (115 linhas) =====
350:===== FIM DO ARQUIVO: example_network_export.json =====
352:===== INÍCIO DO ARQUIVO: example_network_export.py (49 linhas) =====
402:===== FIM DO ARQUIVO: example_network_export.py =====
404:===== INÍCIO DO ARQUIVO: mininet-gui-backend/.gitignore (5 linhas) =====
410:===== FIM DO ARQUIVO: mininet-gui-backend/.gitignore =====
412:===== INÍCIO DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/__init__.py (0 linhas) =====
413:===== FIM DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/__init__.py =====
415:===== INÍCIO DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/api.py (491 linhas) =====
529:114|         app.net.nameToNode[controller].start()
531:116|         switch = app.net.nameToNode[switch_id]
604:189|         new_switch.start([app.net.nameToNode[switch.controller]])
650:235|     if sw_id not in app.net.nameToNode or ctl_id not in app.net.nameToNode:
652:237|     sw = app.net.nameToNode[sw_id]
653:238|     ctl = app.net.nameToNode[ctl_id]
665:250|     if link[0] not in app.net.nameToNode or link[1] not in app.net.nameToNode:
673:258|             node = app.net.nameToNode[node]
694:279|     if node_id not in app.net.nameToNode:
695:280|         raise HTTPException(status_code=404, detail=f"Node {node_id} not found")
696:281|     node = app.net.nameToNode[node_id]
700:285|     debug("updated xy",(app.net.nameToNode[node_id].x, app.net.nameToNode[node_id].y))
710:295|     return {"message": f"Node {node_id} updated successfully"}
715:300|     if node_id not in app.net.nameToNode:
716:301|         raise HTTPException(status_code=404, detail=f"Node {node_id} not found")
717:302|     node = app.net.nameToNode[node_id]
718:303|     app.net.delNode(node)
730:315|                 app.net.nameToNode[switch_id].start([])
731:316|     return {"message": f"Node {node_id} deleted successfully"}
737:322|         raise HTTPException(status_code=404, detail=f"Node not found")
744:329|     if src_id not in app.net.nameToNode or dst_id not in app.net.nameToNode:
748:333|         node = app.net.nameToNode[node_id]
764:349|     if node_id not in app.net.nameToNode:
765:350|         raise HTTPException(status_code=404, detail=f"Node {node_id} not found")
767:352|     node = app.net.nameToNode[node_id]
770:355|         raise HTTPException(status_code=404, detail=f"Node {node_id} not found")
907:===== FIM DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/api.py =====
909:===== INÍCIO DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/cli.py (20 linhas) =====
930:===== FIM DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/cli.py =====
932:===== INÍCIO DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/export.py (111 linhas) =====
1044:===== FIM DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/export.py =====
1046:===== INÍCIO DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/schema.py (28 linhas) =====
1061:15| class Controller(Node):
1067:21| class Host(Node):
1072:26| class Switch(Node):
1075:===== FIM DO ARQUIVO: mininet-gui-backend/mininet_gui_backend/schema.py =====
1077:===== INÍCIO DO ARQUIVO: mininet-gui-backend/requirements.txt (4 linhas) =====
1082:===== FIM DO ARQUIVO: mininet-gui-backend/requirements.txt =====
1084:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/.gitignore (3 linhas) =====
1088:===== FIM DO ARQUIVO: mininet-gui-frontend/.gitignore =====
1090:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/.prettierrc.json (1 linhas) =====
1092:===== FIM DO ARQUIVO: mininet-gui-frontend/.prettierrc.json =====
1094:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/index.html (13 linhas) =====
1108:===== FIM DO ARQUIVO: mininet-gui-frontend/index.html =====
1110:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/package-lock.json (1141 linhas) =====
2111:1001|       "version": "9.0.1",
2112:1002|       "resolved": "https://registry.npmjs.org/uuid/-/uuid-9.0.1.tgz",
2125:1015|       "version": "7.1.9",
2126:1016|       "resolved": "https://registry.npmjs.org/vis-data/-/vis-data-7.1.9.tgz",
2132:1022|       "peerDependencies": {
2138:1028|       "version": "9.1.9",
2139:1029|       "resolved": "https://registry.npmjs.org/vis-network/-/vis-network-9.1.9.tgz",
2145:1035|       "peerDependencies": {
2155:1045|       "version": "5.0.7",
2156:1046|       "resolved": "https://registry.npmjs.org/vis-util/-/vis-util-5.0.7.tgz",
2165:1055|       "peerDependencies": {
2171:1061|       "version": "1.1.0",
2172:1062|       "resolved": "https://registry.npmjs.org/vis.js/-/vis.js-1.1.0.tgz",
2176:1066|       "version": "4.5.9",
2177:1067|       "resolved": "https://registry.npmjs.org/vite/-/vite-4.5.9.tgz",
2194:1084|       "optionalDependencies": {
2197:1087|       "peerDependencies": {
2206:1096|       "peerDependenciesMeta": {
2231:1121|       "version": "3.5.13",
2232:1122|       "resolved": "https://registry.npmjs.org/vue/-/vue-3.5.13.tgz",
2241:1131|       "peerDependencies": {
2244:1134|       "peerDependenciesMeta": {
2252:===== FIM DO ARQUIVO: mininet-gui-frontend/package-lock.json =====
2254:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/package.json (24 linhas) =====
2273:19|   "devDependencies": {
2279:===== FIM DO ARQUIVO: mininet-gui-frontend/package.json =====
2281:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/src/App.vue (42 linhas) =====
2324:===== FIM DO ARQUIVO: mininet-gui-frontend/src/App.vue =====
2326:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/src/assets/controller.svg (6 linhas) =====
2327:1| <?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->
2328:2| <svg fill="#000000" width="800px" height="800px" viewBox="0 0 36 36" version="1.1"  preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
2333:===== FIM DO ARQUIVO: mininet-gui-frontend/src/assets/controller.svg =====
2335:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/src/assets/ethernet-cable-off.svg (1 linhas) =====
2337:===== FIM DO ARQUIVO: mininet-gui-frontend/src/assets/ethernet-cable-off.svg =====
2339:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/src/assets/ethernet-cable.svg (1 linhas) =====
2341:===== FIM DO ARQUIVO: mininet-gui-frontend/src/assets/ethernet-cable.svg =====
2343:===== INÍCIO DO ARQUIVO: mininet-gui-frontend/src/assets/host.svg (6 linhas) =====
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "Get-Content -LiteralPath 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\pacote\\instrucoes-oficiais.md' -Encoding utf8; Get-Content -LiteralPath 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\pacote\\reivindicacoes.md' -Encoding utf8"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
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
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\pacote\\artefato.txt'; "'$c=Get-Content -LiteralPath $p -Encoding utf8; $c[84..205]'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
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
 57| Passo 3: Execute a máquina virtual (user `mininet`, senha [valor omitido])
 58| 
 59| 
 60| ## Instalação manual
 61| 
 62| Atenção: os comandos abaixo irão modificar o kernel e outras configurações do seu sistema operacional, portanto use com cautela.
 63| Utilize os comandos abaixo para instalar manualmente (testado no ubuntu 20.04):
 64| 
 65| ```bash
 66| git clone https://github.com/mininet/[senha omitida]
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
 82| Passo 1: Execute a VM dentro do VirtualBox e faça login (usuário: `mininet`, senha [valor omitido])
 83| 
 84| Passo 2: Abra o terminal (Ctrl+Alt+T) e rode o seguinte comando: `mininet_gui` (ou alternativamente `/home/mininet/[senha omitida]-gui/run.sh`)
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
~~~~~~~~~~~~

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (failed, exit 1):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command "rg -n 'D3|D2' 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\execucao\\registro-factual.md' | Measure-Object -Line; rg -n 'D3' 'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\execucao\\registro-factual.md'"
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text

Lines Words Characters Property
----- ----- ---------- --------
   34
~~~~~~~~~~~~

### AI / AGENT — commentary

Os testes documentados de C4 e C5 tiveram os resultados esperados, o que resolve a incerteza anterior sobre R. Para F, a execução confirmou as funções centrais, mas preciso manter separado o requisito documental do README e as falhas observadas no passo opcional e nos testes complementares.

### TOOL / TERMINAL / SYSTEM OUTPUT

Command (completed, exit 0):

~~~~~~~~~~~~text
"C:\\Users\\wendt\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell\\pwsh.exe" -Command '$p='"'D:\\user\\unipampa\\8º Semestre\\LEAS\\atividades\\t8\\t8-leas\\runs\\mininet-gui\\execucao\\registro-factual.md'; rg -n '"'^'"\\| E(02|04|06|09|10|11|12|13|14|16|17|19|20|21|22|24|07|08|15|18|23|25|26|27|28a|28b|29|30a|30b|30c|30d|31|32) \\|' -- "'$p | ForEach-Object { ($_ -split '"':',2)[0] + ' ' + ([regex]::Match("'$_,'"'\\| E["'^|]+ '"\\|')).Value }; rg -n '"'^## [1-6]'"\\.|"'^### 1'"\\.|"'^'"\\*\\*Teste mínimo' -- "'$p'
~~~~~~~~~~~~

Output:

~~~~~~~~~~~~text
74 | E02 |
75 | E04 |
76 | E06 |
77 | E09 |
78 | E10 |
79 | E11 |
80 | E12 |
81 | E13 |
82 | E14 |
83 | E16 |
84 | E17 |
85 | E19 |
86 | E20 |
87 | E21 |
88 | E22 |
89 | E24 |
102 | E07 |
103 | E08 |
104 | E15 |
105 | E18 |
106 | E23 |
107 | E25 |
108 | E26 |
109 | E27 |
110 | E28a |
111 | E28b |
112 | E29 |
113 | E30a |
114 | E30b |
115 | E30c |
116 | E30d |
117 | E31 |
118 | E32 |
9:## 1. Ambiente
11:### 1.1 Host
23:### 1.2 Máquina virtual
37:### 1.3 Commit da VM × documentação avaliada
46:### 1.4 Requisitos do README × ambiente usado
58:### 1.5 Modo de operação e registro
68:## 2. Tabela de passos — procedimento documentado pelos autores
93:## 3. Passos [NÃO DOCUMENTADO] (desvios declarados, D2)
120:## 4. Resultados por reivindicação
133:**Teste mínimo do README (passos 1–9):** passos 1–6 e 9 com o resultado descrito pelos autores; passo 7 (opcional, iperf) concluído; passo 8 (opcional) com a criação do controlador remoto, da segunda topologia e do link verde, mas sem o Ryu (ausente na VM) e sem conectividade entre as topologias no Pingall.
135:## 5. Insumos ausentes e respostas dos autores
143:## 6. Limitações e incidentes
~~~~~~~~~~~~

### AI / AGENT — final

Reavaliei os selos com o [registro factual](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/execucao/registro-factual.md>), os [critérios fornecidos](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md>) e a [regra das reivindicações](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/pacote/reivindicacoes.md>). Trato as observações como uma execução registrada pelo aluno, não como uma execução feita por mim. “Confirma” e “contradiz” abaixo referem-se à expectativa funcional examinada na avaliação analítica; uma confirmação não elimina, por si só, uma lacuna documental.

| Passos do registro | Efeito sobre a avaliação analítica |
|---|---|
| E01–E08 | **Não alteram diretamente os selos.** Confirmam que a VM foi obtida, importada e iniciada, mas documentam os desvios de ambiente e o commit diferente. O backend e o frontend são idênticos entre os commits; o `run.sh` mudou. O registro não demonstra a execução da revisão `465648a4` inteira. |
| E09–E13 | **Confirmam** a execução da aplicação, a interface, a criação da topologia Single e o `pingall` com 2/2 pares. Resolvem a dúvida anterior sobre observar funções básicas, embora não corrijam o README. |
| E14 | **Confirma** o WebShell e o teste opcional de `iperf`; também apoia C5. |
| E15–E16 | **Contradizem** a conclusão bem-sucedida do passo opcional de múltiplos controladores: o Ryu está ausente da VM e não houve conectividade entre as duas topologias. Isso limita F, mas não integra a regra de R. |
| E17 | **Confirma** a exportação de JSON e Python. A checagem de sintaxe complementar não equivale a executar o script exportado. |
| E19–E22 | **Confirmam C4:** Single, Linear e Tree foram geradas com as quantidades escolhidas. São os passos dos autores que resolvem a primeira pendência de R. |
| E24 | **Confirma C5:** `ip addr show` apareceu na aba `h1` do WebShell. Resolve a segunda pendência de R. |
| E18, E23, E25–E27 | **Reforçam, sem substituir, E19–E22 e E24.** Resets, contagens pela API e comparação dos namespaces são verificações D2 dos revisores. |
| E28a–E29 | **Confirmam complementarmente** a manipulação visual, a adição de nós com a rede ativa e o `pingall` com 20/20 pares. São D2, não reprodução formal de uma reivindicação dos autores. |
| E30a–E30b, E30d | **Confirmam complementarmente** remoções sem reiniciar a emulação: o grafo mudou e `h1` continuou alcançando `h3`. |
| E30c | **Contradiz** o funcionamento íntegro após as remoções: o `pingall` da interface retornou HTTP 500, e a API ainda listava um link do nó removido. |
| E31–E32 | **Confirmam** a visualização da tabela de fluxo, mas **contradizem** a parte de C6 sobre criar ou remover regras pela interface testada: nenhum controle foi encontrado. São D2 e não entram na regra de R. |

Esses resultados estão nas [tabelas de passos documentados](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/execucao/registro-factual.md:68>) e [complementares](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/execucao/registro-factual.md:93>). O registro não identifica nenhum passo **D3**; portanto, não atribuo a D3 qualquer reprodução.

### Novas decisões

**F — Não atribuir; não mudou.** A execução confirmou várias funcionalidades e fortaleceu a parte prática de F. Permanece, porém, a falha documental obrigatória que fundamentou a decisão anterior: os [critérios de F](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/pacote/instrucoes-oficiais.md>) exigem que o README informe dependências **e versões**; sua [seção “Dependências”](<D:/user/unipampa/8º Semestre/LEAS/atividades/t8/t8-leas/runs/mininet-gui/pacote/artefato.txt:119>) informa a versão do VirtualBox, mas não as versões dos demais componentes necessários. As versões medidas na VM não passam a constar do README. A ausência do Ryu no passo opcional reforça a ressalva, mas não é o fundamento isolado da decisão. **Confiança de que o comitê oficial atribuiu F: 30/100**, ante 35/100 na análise anterior. Isso é uma estimativa sobre uma decisão oficial desconhecida, não uma consulta ao resultado do comitê.

**R — Atribuir; mudou de Indeterminado.** Pela regra previamente fornecida, R depende de **C4 e C5**. Os passos documentados E19–E22 observaram os três modelos de C4, e E24 observou a saída do comando no WebShell para C5. Não falta evidência de execução para essa regra. **Confiança de que o comitê oficial atribuiu R: 85/100**, ante 55/100. Mantenho alguma reserva porque a VM continha um commit anterior, o navegador foi usado no host e a execução ocorreu sobre NEM; o registro delimita esses desvios e informa que o código do backend e do frontend não mudou entre os commits.

Para o bloco abaixo, “reproduzivel” em C1/C2 registra os resultados observados nos passos dos autores; **somente C4 e C5 determinam R**. C3 e C6 permanecem sem reprodução formal por procedimento dos autores, apesar da evidência complementar.

```json
{
  "F": {
    "decisao": "Não atribuir",
    "confianca": 30,
    "mudou": false,
    "evidencias": [
      "instrucoes-oficiais.md:Funcional (F)",
      "artefato.txt:README.md:35-38",
      "registro-factual.md:seção 2/E09-E17",
      "registro-factual.md:seção 2/E16"
    ]
  },
  "R": {
    "decisao": "Atribuir",
    "confianca": 85,
    "mudou": true,
    "evidencias": [
      "reivindicacoes.md:Regra para o selo R",
      "registro-factual.md:seção 2/E19-E22",
      "registro-factual.md:seção 2/E24",
      "registro-factual.md:seção 1.3"
    ],
    "por_reivindicacao": {
      "C1": "reproduzivel",
      "C2": "reproduzivel",
      "C3": "depende_execucao",
      "C4": "reproduzivel",
      "C5": "reproduzivel",
      "C6": "depende_execucao"
    }
  }
}
```

---

## Interaction 003

### HUMAN

[@Session Exporter](plugin://session-exporter@openai-curated-remote) Export this entire conversation to a context-named Markdown file.

### AI / AGENT — commentary

Vou usar o Session Exporter para salvar a conversa acessível desta sessão em um arquivo Markdown com nome baseado no tema, incluindo o estado atual da reavaliação F/R.

### AI / AGENT — commentary

A transcrição acessível está reunida em três interações. Estou verificando a formatação do arquivo e os trechos sensíveis antes de entregar o link; a primeira checagem encontrou blocos de saída com delimitadores Markdown que preciso ajustar.

---

## Export Integrity Report

- HUMAN messages exported: 3.
- AI / AGENT messages exported: 8.
- TOOL / TERMINAL / SYSTEM blocks exported: 14.
- Earliest interaction represented: Interaction 001 (request to restore prior context).
- Latest interaction represented: Interaction 003 (request to export this conversation, in progress when the artifact was written).
- Known inaccessible content: the older conversation cited in `cadeia-1-session-export.md` is incomplete within that source. Its missing portion was not presented as part of this chat or invented. No current-chat HUMAN or AI / AGENT message was inaccessible in first-party history.
- Intentional redactions or omissions: credential values in visible source excerpts were redacted; hidden reasoning, internal skill instructions, and export setup outputs were excluded. The source files themselves remain at the paths above.
- Completeness: the transcript is believed complete for visible HUMAN and AI / AGENT messages in this current chat through the export request. The final response linking this file necessarily follows the artifact and is not included.
- Completeness audit: passed for the accessible current-chat scope, subject to the disclosed redactions and omissions.

