# Roteiro de execução — Mininet-GUI (SBRC 2025), selos F e R

Oct 15, 2026 · @edu

## Escopo e convenções

Roteiro de 27 passos para executar o Mininet-GUI (commit `465648a4425a4457af0348ab951cf7f71d37a86f`) e decidir os selos F e R. Nada aqui foi executado; os resultados esperados vêm do README, do artigo ou, quando indicado, do código.

**Fontes.** `artefato.txt` (citado como `arquivo:linha` na numeração original), `artigo.pdf`, `instrucoes-oficiais.md` e `reivindicacoes.md`. A VM `.ova` e o vídeo estão fora dos anexos.

**Marcação \[NÃO DOCUMENTADO\].** Indica passo, parâmetro ou verificação que os autores não descrevem, sempre com a justificativa. Os demais passos reproduzem literalmente o README.

**Campos de cada passo.** Selo e reivindicação · Diretório · Comando exato · Resultado esperado (autores) · Evidência a salvar · Sucesso · Falha · Interrupção.

**Pasta de evidências \[NÃO DOCUMENTADO\].** Crie no hospedeiro uma pasta `evidencias/` e nomeie cada arquivo com o identificador do passo (ex.: `P12_pingall.png`). Os autores não pedem registro, mas as instruções oficiais exigem justificar o selo com evidência observada.

**Regra de R.** R é atribuído se C4 (nos três modelos) e C5 forem observadas (reivindicacoes.md, "Regra para o selo R"). C1, C2, C3 e C6 apoiam F e são registradas separadamente.

## Requisitos de hardware e software

A via documentada como recomendada é a VM pronta no VirtualBox; a instalação manual (README.md:60-78) altera o kernel e fica fora deste roteiro.

| Item | Valor exigido | Fonte |
| --- | --- | --- |
| CPU | x86-64; autores usaram Intel i5-10300H 2,50 GHz; mínimo de 1 núcleo reservado à VM | README.md:28, 31, 103 |
| RAM do hospedeiro | autores usaram 8 GB | README.md:29 |
| RAM da VM | "Mínimo de 8GB" (linha 38) e "no mínimo 2GB" (linha 103), valores conflitantes | README.md:38, 103 |
| Disco livre | pelo menos 80 GB | README.md:32 |
| Hipervisor | Oracle VirtualBox 7.1.6 r167084 | README.md:37, 51 |
| SO do hospedeiro | autores usaram Windows 11 Home 64 bits; outros SO não são mencionados | README.md:30-31 |
| Imagem | `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (Google Drive) | README.md:53-55 |
| Credenciais da VM | usuário `mininet`, senha `mininet` | README.md:57 |
| Navegador | dentro da VM (já incluído, segundo o passo 3 do teste mínimo) | README.md:86 |
| Rede | acesso à internet para baixar a OVA; tamanho do arquivo não informado | README.md:53 |
| Software na VM (via scripts) | Node 18.20.7, FastAPI/uvicorn sem versão fixada, Mininet sem versão declarada | setup.sh:19; requirements.txt:1-4 |
| Opcional | Ryu (`ryu-manager`), usado no passo 8; instalação documentada só para a via manual | README.md:75-78, 96 |

**Lacunas a registrar.** Não há hash da OVA, tamanho do download, versão do Mininet nem do Python. Use pelo menos 8 GB de RAM na VM, o valor mais exigente do README.

## Preparação do ambiente (P1–P7)

Os passos P2, P4 e P6 seguem o README; P1, P3, P5 e P7 são verificações não documentadas, necessárias para provar que o ambiente atende aos requisitos e que a versão avaliada é a 465648a.

### P1 \[NÃO DOCUMENTADO\] Registrar o hospedeiro

- **Selo / reivindicação:** F e R / todas.
- **Diretório:** qualquer, no hospedeiro.
- **Comando:** `VBoxManage --version` e o painel de sistema do SO (CPU, RAM, disco livre).
- **Justificativa:** as instruções oficiais exigem que o ambiente satisfaça os requisitos mínimos; o README não pede esse registro.
- **Resultado esperado:** VirtualBox 7.1.6r167084; ≥ 8 GB de RAM; ≥ 80 GB livres.
- **Evidência:** `P1_ambiente.txt` com a saída e os valores.
- **Sucesso:** os três valores atendem à tabela de requisitos.
- **Falha:** versão diferente do VirtualBox ou RAM/disco abaixo do mínimo.
- **Interrupção:** RAM < 8 GB ou disco < 80 GB: não prossiga; troque de hospedeiro. Versão diferente do VirtualBox: prossiga e registre o desvio.

### P2 Baixar a OVA

- **Selo / reivindicação:** F / pré-requisito.
- **Diretório:** pasta de downloads do hospedeiro.
- **Comando:** abrir no navegador `https://drive.google.com/file/d/1HBqlTwEWnmkPjRFJVQhEn34itKNyzhg3/view?usp=sharing` e baixar (README.md:53).
- **Resultado esperado (autores):** arquivo `Mininet-GUI-Desktop-VM-SBRC-2025.ova` (README.md:55).
- **Evidência:** `P2_download.png` (nome e tamanho do arquivo).
- **Sucesso:** download completo com o nome esperado.
- **Falha:** link indisponível, acesso negado ou arquivo com outro nome.
- **Interrupção:** link indisponível: pare; registre como evidência ausente. Sem a VM, o roteiro só pode seguir pela instalação manual, que está fora do escopo.

### P3 \[NÃO DOCUMENTADO\] Registrar o hash da OVA

- **Selo / reivindicação:** F e R / rastreabilidade.
- **Diretório:** pasta de downloads.
- **Comando:** `sha256sum Mininet-GUI-Desktop-VM-SBRC-2025.ova` (Windows: `certutil -hashfile Mininet-GUI-Desktop-VM-SBRC-2025.ova SHA256`).
- **Justificativa:** os autores não publicam hash; sem ele, o relatório não identifica a imagem avaliada.
- **Resultado esperado:** não há valor de referência.
- **Evidência:** `P3_sha256.txt`.
- **Sucesso:** hash registrado.
- **Falha:** comando sem saída (arquivo corrompido ou incompleto).
- **Interrupção:** não interrompe.

### P4 Importar a VM

- **Selo / reivindicação:** F / pré-requisito.
- **Diretório:** VirtualBox (interface gráfica).
- **Comando:** VirtualBox → Arquivo → Importar Appliance → selecionar a OVA (README.md:55: "Abra o arquivo … no VirtualBox, para importar a máquina virtual").
- **Resultado esperado (autores):** VM importada.
- **Evidência:** `P4_import.png` com a VM listada.
- **Sucesso:** VM aparece na lista sem erro.
- **Falha:** erro de importação ou de formato.
- **Interrupção:** importação falha duas vezes: pare; F = Não atribuir por falha de instalação.

### P5 \[NÃO DOCUMENTADO\] Conferir RAM e CPU da VM

- **Selo / reivindicação:** F / pré-requisito.
- **Diretório:** VirtualBox → Configurações da VM → Sistema.
- **Comando:** ler os valores; se a RAM estiver abaixo de 8 GB, ajustar para 8 GB.
- **Justificativa:** o README traz dois mínimos conflitantes (8 GB e 2 GB, README.md:38, 103) e não diz se a OVA já vem configurada.
- **Resultado esperado:** ≥ 8 GB de RAM e ≥ 1 núcleo.
- **Evidência:** `P5_config_vm.png` antes e depois de qualquer ajuste.
- **Sucesso:** valores registrados e dentro do mínimo.
- **Falha:** hospedeiro não comporta 8 GB para a VM.
- **Interrupção:** não interrompe; com menos de 8 GB, prossiga com o máximo possível (≥ 2 GB) e registre o desvio.

### P6 Iniciar a VM e fazer login

- **Selo / reivindicação:** F / pré-requisito.
- **Diretório:** VirtualBox.
- **Comando:** iniciar a VM; login `mininet` / `mininet` (README.md:57, 82).
- **Resultado esperado (autores):** área de trabalho da VM.
- **Evidência:** `P6_login.png`.
- **Sucesso:** sessão gráfica aberta.
- **Falha:** VM não inicia ou credenciais rejeitadas.
- **Interrupção:** VM não inicia após um reinício: pare; F = Não atribuir.

### P7 \[NÃO DOCUMENTADO\] Confirmar a versão do código na VM

- **Selo / reivindicação:** F e R / rastreabilidade.
- **Diretório:** `/home/mininet/mininet-gui` (caminho fixo em run.sh:7).
- **Comando:** `cd /home/mininet/mininet-gui && git rev-parse HEAD; sha256sum README.md mininet-gui-backend/mininet_gui_backend/api.py`
- **Justificativa:** o README não diz qual commit está na VM; a avaliação é da versão 465648a.
- **Resultado esperado (índice de artefato.txt):** HEAD = `465648a4425a4457af0348ab951cf7f71d37a86f`; README.md = `e424434fa7cf…3753`; api.py = `1ea14fe454ef…0d6e`.
- **Evidência:** `P7_versao.txt`.
- **Sucesso:** commit ou os dois hashes coincidem.
- **Falha:** commit e hashes divergem.
- **Interrupção:** não interrompe; com divergência, registre que a VM contém outra versão e trate os resultados como relativos a ela.

## Teste mínimo — selo F (P8–P16)

F é atribuível se P8 a P12 e P16 tiverem sucesso; P13 e P15 são opcionais para os autores e servem de apoio a C5 e C3. Siga a ordem: cada passo depende do estado deixado pelo anterior.

### P8 Iniciar o Mininet-GUI

- **Selo / reivindicação:** F / C2.
- **Diretório:** `/home/mininet` (terminal aberto com Ctrl+Alt+T).
- **Comando:** `mininet_gui` (alternativa: `/home/mininet/mininet-gui/run.sh`) (README.md:84).
- **Resultado esperado (autores):** "mostrará em sua saída do terminal uma URL (Exemplo: `http://10.0.2.15:5173`)" (README.md:86); o script imprime "Mininet-GUI bootstrap complete" e "Mininet-GUI is available at:" (run.sh:22, 27-28).
- **Evidência:** `P8_terminal.png`; cópia de `/home/mininet/mininet-gui/mininet-gui-backend/nohup.out` e `/home/mininet/mininet-gui/mininet-gui-frontend/nohup.out` (run.sh:23-24) como `P8_backend.log` e `P8_frontend.log`.
- **Sucesso:** URL impressa e nenhum erro fatal nos dois logs.
- **Falha:** sem URL; erro de importação em `nohup.out` do backend; frontend não sobe (ex.: `nvm: command not found` seguido de falha do `npm`, risco apontado em run.sh:20).
- **Interrupção:** se nem o comando nem a alternativa produzirem URL e frontend ativo, pare: F = Não atribuir e R não pode ser avaliado.

### P9 Abrir a interface

- **Selo / reivindicação:** F / C1.
- **Diretório:** navegador dentro da VM.
- **Comando:** acessar a URL impressa em P8 (README.md:86).
- **Resultado esperado (autores):** barra lateral, painel inferior com o WebShell e área principal (artigo, p. 7, Fig. 2). Rótulos no código: "Generate Topology", "Reset Topology", "Create Link", "Delete Selected", "Run Pingall Test", "Export Topology (JSON)", "Export Mininet Script" (Side.vue:20-58).
- **Evidência:** `P9_interface.png`.
- **Sucesso:** página carregada com as três áreas.
- **Falha:** página em branco, erro de conexão ou sem barra lateral.
- **Interrupção:** página não carrega após recarregar e reexecutar P8 uma vez: pare; F = Não atribuir.

### P10 Criar o controlador c1

- **Selo / reivindicação:** F / C1, C2.
- **Diretório:** interface web.
- **Comando:** arrastar "Controller" da barra lateral para o centro; no diálogo, escolher "Default" e clicar "Submit" (README.md:88).
- **Resultado esperado (autores):** controlador criado.
- **Evidência:** `P10_c1.png`.
- **Sucesso:** nó `c1` aparece no grafo e na lista de abas do WebShell.
- **Falha:** diálogo não abre, erro ao enviar ou nó ausente.
- **Interrupção:** falha após uma repetição: pare; F = Não atribuir (passo do exemplo mínimo).

### P11 Gerar topologia Single com 2 hosts

- **Selo / reivindicação:** F / C1, C2, C4 (preliminar).
- **Diretório:** interface web.
- **Comando:** "Generate Topology" → "Topology Type" Single, "Controller" c1, "Hosts" = 2 → "Submit" (README.md:90).
- **Resultado esperado (autores):** topologia criada; links ativos em verde e associação switch–controlador em linha cinza pontilhada (artigo, p. 7).
- **Evidência:** `P11_single2.png`.
- **Sucesso:** `s1`, `h1` e `h2` no grafo, com links verdes s1–h1 e s1–h2 e linha pontilhada s1–c1.
- **Falha:** nós ausentes, links cinza (rede não iniciada) ou erro.
- **Interrupção:** nenhum nó criado: pare; F = Não atribuir.

### P12 Executar o pingall

- **Selo / reivindicação:** F / C2.
- **Diretório:** interface web.
- **Comando:** "Run Pingall Test" e aguardar (README.md:92).
- **Resultado esperado (autores):** "aguarde os resultados aparecerem" (README.md:92). O código exibe a tabela src, dst, packets\_sent, packets\_recv, min, avg, max, mdev (PingallResults.vue:31).
- **Evidência:** `P12_pingall.png`.
- **Sucesso:** tabela com as linhas h1→h2 e h2→h1. Registre também se packets\_recv = packets\_sent; os autores não definem perda aceitável.
- **Falha:** "No ping results available." ou erro HTTP.
- **Interrupção:** sem resultados após 2 minutos e uma repetição: pare; F = Não atribuir.

### P13 (opcional) Teste com iperf

- **Selo / reivindicação:** F / C5 (apoio; caso de uso 2 do artigo, p. 6).
- **Diretório:** WebShell, abas `h1` e `h2`.
- **Comando:** aba `h1`: `iperf -s`; aba `h2`: `iperf -c 10.0.0.1` (README.md:94).
- **Resultado esperado (autores):** "Aguarde 1 minuto para o teste completar-se" (README.md:94); nenhum valor de vazão é declarado.
- **Evidência:** `P13_iperf_h1.png`, `P13_iperf_h2.png`.
- **Sucesso:** relatório do iperf com vazão na aba `h2`.
- **Falha:** "connection refused", comando inexistente ou aba sem saída.
- **Interrupção:** não interrompe (passo opcional). Encerre o servidor com Ctrl+C na aba `h1` antes de seguir.

### P14 \[NÃO DOCUMENTADO\] Verificar se o Ryu está instalado

- **Selo / reivindicação:** F / C3 (pré-requisito de P15).
- **Diretório:** terminal da VM, `/home/mininet`.
- **Comando:** `which ryu-manager`
- **Justificativa:** P15 usa `ryu-manager`, mas a instalação do Ryu só aparece na via manual (README.md:75-78); não se sabe se a VM o inclui.
- **Resultado esperado:** um caminho para `ryu-manager`.
- **Evidência:** `P14_ryu.txt`.
- **Sucesso:** caminho impresso.
- **Falha:** nenhuma saída.
- **Interrupção:** sem Ryu, pule P15 e registre; C3 passa a depender só de P19.

### P15 (opcional) Múltiplos controladores e link em tempo real

- **Selo / reivindicação:** F / C3 (criação de link com a emulação ativa; caso de uso 3, p. 7).
- **Diretório:** interface web e WebShell.
- **Comando (README.md:96):** arrastar novo "Controller", type "Remote", IP 127.0.0.1, porta 6633; "Generate Topology" Single, 2 hosts, controller c2; "Create Link" e arrastar de `s1` para `s2`; na aba `c2` do WebShell, `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; depois "Run Pingall Test".
- **Resultado esperado (autores):** "o sucesso dessa ação é indicado por uma linha verde conectando os dois nós" (README.md:96); pingall com resultados.
- **Evidência:** `P15_link_s1s2.png`, `P15_ryu.png`, `P15_pingall.png`.
- **Sucesso:** linha verde s1–s2, Ryu em execução na aba c2 e pingall com resultados entre os 4 hosts.
- **Falha:** link cinza ou ausente; Ryu não inicia; pingall vazio.
- **Interrupção:** a criação do controlador remoto pode bloquear até 60 s (comentário em api.py:205); aguarde 2 minutos antes de considerar falha. Não interrompe o roteiro.

### P16 Exportar a topologia

- **Selo / reivindicação:** F / exportação (resumo do artigo, p. 1).
- **Diretório:** interface web; arquivos na pasta de downloads da VM.
- **Comando:** "Export Topology (JSON)" e "Export Mininet Script" (README.md:98).
- **Resultado esperado (autores):** "o arquivo JSON com a configuração da topologia atual e o script do mininet" (README.md:98).
- **Evidência:** os dois arquivos baixados, copiados como `P16_topologia.json` e `P16_script.py`.
- **Sucesso:** dois arquivos não vazios, com os nós criados em P10–P15.
- **Falha:** nenhum download ou arquivos vazios.
- **Interrupção:** não interrompe; registre a falha como problema de F.

## Blocos por reivindicação (P17–P27)

R depende de C4 (P20–P23, três modelos) e C5 (P24–P25); C1, C2, C3 e C6 apoiam F. O README só documenta C4 e C5 como experimentos (README.md:105-114), por isso os blocos de C1, C2, C3 e C6 têm passos não documentados.

**Comandos de API \[NÃO DOCUMENTADO\].** Vários passos consultam o backend com `curl` no terminal da VM. Os endpoints existem (api.py:87-105) e o backend escuta na porta 8000 (run.sh:14), mas o README não os cita. Eles dão contagens objetivas, independentes da leitura visual do grafo.

### C1 — Interface web com grafo interativo (apoio a F)

Criação e representação de elementos já são observadas em P10 e P11. Falta a resposta às ações do usuário.

#### P17 \[NÃO DOCUMENTADO\] Mover um nó no grafo

- **Selo / reivindicação:** F / C1.
- **Diretório:** interface web, estado deixado por P15 (ou P12).
- **Comando:** arrastar `h1` para outra posição; recarregar a página (F5).
- **Justificativa:** C1 espera elementos "respondendo às ações" (reivindicacoes.md); o README não tem passo para isso. O código salva a posição no backend ao soltar o nó (NetworkGraph.vue:282; api.py:270-295).
- **Resultado esperado:** nó acompanha o arraste e mantém a posição após recarregar.
- **Evidência:** `P17_antes.png`, `P17_depois_reload.png`.
- **Sucesso:** posição mantida após recarregar.
- **Falha:** nó não se move, ou volta à posição anterior.
- **Interrupção:** não interrompe.

### C2 — Emulação integrada (apoio a F)

O resultado esperado (nós emulados e pingall exibido) é observado em P12. Falta confirmar que a emulação está ativa no backend.

#### P18 \[NÃO DOCUMENTADO\] Confirmar a emulação ativa

- **Selo / reivindicação:** F / C2.
- **Diretório:** terminal da VM, `/home/mininet`.
- **Comando:** `curl -s http://localhost:8000/api/mininet/start; echo; curl -s http://localhost:8000/api/mininet/hosts`
- **Justificativa:** separa "rede emulada" de "desenho no navegador"; o README não oferece verificação equivalente.
- **Resultado esperado:** `true`, seguido dos hosts criados.
- **Evidência:** `P18_api.txt`.
- **Sucesso:** `true` e hosts coerentes com o grafo.
- **Falha:** `false`, erro de conexão ou lista vazia.
- **Interrupção:** não interrompe.

### C3 — Modificação em tempo real (apoio a F)

A criação de link com a emulação ativa é observada em P15. A remoção não tem procedimento dos autores.

#### P19 \[NÃO DOCUMENTADO\] Remover um link com a emulação ativa

- **Selo / reivindicação:** F / C3.
- **Diretório:** interface web e terminal da VM.
- **Comando:** clicar no link `s1`–`h2` → "Delete Selected"; "Run Pingall Test"; no terminal, `curl -s http://localhost:8000/api/mininet/start; echo; curl -s http://localhost:8000/api/mininet/links`
- **Justificativa:** C3 inclui remoção "sem reiniciá-la" (artigo, p. 6; reivindicacoes.md); o README só exercita criação de link (README.md:96).
- **Resultado esperado:** link some do grafo; pingall mostra `h2` sem resposta e os demais pares respondendo; `start` continua `true`; `s1`–`h2` ausente da lista.
- **Evidência:** `P19_grafo.png`, `P19_pingall.png`, `P19_api.txt`.
- **Sucesso:** os quatro resultados acima.
- **Falha:** link permanece; emulação reiniciada (todos os nós somem) ou erro.
- **Interrupção:** não interrompe.

### C4 — Geração de topologias Single, Linear e Tree (regra de R)

Procedimento dos autores: "clique no botão 'Generate Topology'. Selecione o tipo de topologia (Single, Linear ou Tree), e o número de dispositivos, então clique em OK" (README.md:107-108). O botão real é "Submit" (TopologyForm.vue:43). Linear e Tree pedem dois parâmetros que o README não cita (TopologyForm.vue:25-40). As contagens esperadas abaixo derivam desses rótulos e do código (NetworkGraph.vue:512-585), pois os autores não as declaram.

#### P20 \[NÃO DOCUMENTADO\] Limpar a topologia

- **Selo / reivindicação:** R / C4.
- **Diretório:** interface web.
- **Comando:** "Reset Topology" → confirmar o diálogo. Repetir antes de P21, P22 e P23.
- **Justificativa:** sem topologia vazia, a contagem de cada modelo se mistura com os nós anteriores. O botão existe (Side.vue:24) e o artigo cita a reinicialização (p. 7), mas o README não a usa.
- **Resultado esperado:** grafo vazio; `curl -s http://localhost:8000/api/mininet/switches` retorna `{}`.
- **Evidência:** `P20_vazio_<modelo>.png`.
- **Sucesso:** grafo e API vazios.
- **Falha:** nós remanescentes.
- **Interrupção:** se o reset falhar, reinicie o backend com `mininet_gui` (P8); se persistir, pare C4: R = Indeterminado por impedimento de ambiente.

#### P21 Gerar Single

- **Selo / reivindicação:** R / C4.
- **Diretório:** interface web e terminal da VM.
- **Comando:** "Generate Topology" → Single, "Controller" none \[NÃO DOCUMENTADO: o README de C4 não define o controlador; "none" isola a geração\], "Hosts" = 3 → "Submit". Contagem: `curl -s http://localhost:8000/api/mininet/switches; echo; curl -s http://localhost:8000/api/mininet/hosts; echo; curl -s http://localhost:8000/api/mininet/links`
- **Resultado esperado (autores):** topologia Single "com o número de dispositivos" escolhido (README.md:107-108). Contagem derivada: 1 switch, 3 hosts, 3 links.
- **Evidência:** `P21_single.png`, `P21_api.txt`.
- **Sucesso:** contagem exata no grafo e na API.
- **Falha:** contagem diferente ou erro.
- **Interrupção:** não interrompe; registre e siga para P22. Falha em qualquer modelo leva C4 a não reproduzida.

#### P22 Gerar Linear

- **Selo / reivindicação:** R / C4.
- **Diretório:** interface web e terminal da VM (após P20).
- **Comando:** "Generate Topology" → Linear, "Controller" none, "Switches" = 3, "Hosts per switch" = 2 \[NÃO DOCUMENTADO: o README cita só "número de dispositivos"\] → "Submit". Mesmos `curl` de P21.
- **Resultado esperado (autores):** topologia Linear com o número escolhido. Contagem derivada: 3 switches em cadeia, 6 hosts, 8 links (6 host–switch e 2 switch–switch).
- **Evidência:** `P22_linear.png`, `P22_api.txt`.
- **Sucesso:** contagem exata e switches em cadeia.
- **Falha:** contagem ou forma diferente.
- **Interrupção:** como em P21.

#### P23 Gerar Tree

- **Selo / reivindicação:** R / C4.
- **Diretório:** interface web e terminal da VM (após P20).
- **Comando:** "Generate Topology" → Tree, "Controller" none, "Layers" = 2, "Fanout" = 2 \[NÃO DOCUMENTADO: o README não cita esses campos\] → "Submit". Mesmos `curl` de P21.
- **Resultado esperado (autores):** topologia Tree com o número escolhido. Contagem derivada: 3 switches (1 raiz e 2 filhos), 4 hosts, 6 links.
- **Evidência:** `P23_tree.png`, `P23_api.txt`.
- **Sucesso:** contagem exata e hierarquia em árvore.
- **Falha:** contagem ou forma diferente.
- **Interrupção:** não interrompe. C4 só é reproduzida se P21, P22 e P23 tiverem sucesso.

### C5 — Terminal dos nós via WebShell (regra de R)

Procedimento dos autores: "selecione a aba com o nome desse nó, clicando nela. Em seguida, utilize o terminal bash para executar comandos diretamente no namespace daquele nó" (README.md:112-114). O README não indica o comando; o roteiro usa `ip addr show`, o mesmo exibido na aba `h1` da Fig. 2 do artigo (p. 7).

#### P24 Executar comando no namespace de um host

- **Selo / reivindicação:** R / C5.
- **Diretório:** WebShell, aba `h1` (estado de P23).
- **Comando:** clicar na aba `h1`; digitar `ip addr show` e Enter.
- **Resultado esperado (autores):** comandos executados "no namespace daquele nó" (README.md:114); a Fig. 2 mostra a interface `h1-eth0` com endereço 10.0.0.x.
- **Evidência:** `P24_h1.png`.
- **Sucesso:** saída na aba `h1` listando `lo` e `h1-eth0` com IP 10.0.0.x.
- **Falha:** aba sem saída, erro de WebSocket ou interfaces do hospedeiro (ex.: `enp0s3`) em vez de `h1-eth0`.
- **Interrupção:** sem saída após recarregar a página uma vez: C5 não reproduzida; R = Não atribuir.

#### P25 \[NÃO DOCUMENTADO\] Confirmar namespace distinto em outro host

- **Selo / reivindicação:** R / C5.
- **Diretório:** WebShell, aba `h2`.
- **Comando:** clicar na aba `h2`; `ip addr show`.
- **Justificativa:** um único host não distingue "namespace do nó" de "um terminal qualquer"; o README não propõe comparação.
- **Resultado esperado:** `h2-eth0` com IP diferente do de P24.
- **Evidência:** `P25_h2.png`.
- **Sucesso:** interface e IP próprios de `h2`, cada saída na aba do seu nó.
- **Falha:** mesma saída de P24 ou saída na aba errada.
- **Interrupção:** não interrompe.

### C6 — Regras de fluxo OpenFlow (apoio a F)

Os autores não documentam C6 no README. O código só lê a tabela (`dump-flows`, api.py:363) e não contém `add-flow` nem `del-flows`. Os dois passos verificam o que existe e registram a ausência.

#### P26 \[NÃO DOCUMENTADO\] Visualizar a tabela de fluxo

- **Selo / reivindicação:** F / C6.
- **Diretório:** interface web.
- **Comando:** P20; criar `c1` como em P10; Single com c1 e 2 hosts como em P11; "Run Pingall Test"; duplo clique em `s1`; aba "Flow Table".
- **Justificativa:** o duplo clique abre "Node Info" (NetworkGraph.vue:277-279) e a aba "Flow Table" (NodeStats.vue:37), mas nenhum dos dois aparece no README. O pingall com controlador gera regras para preencher a tabela.
- **Resultado esperado:** "tabela de fluxo exibida" (reivindicacoes.md, C6).
- **Evidência:** `P26_flowtable.png`.
- **Sucesso:** tabela com ao menos uma regra (priority, actions, match).
- **Falha:** modal não abre ou aba vazia/inexistente.
- **Interrupção:** não interrompe.

#### P27 \[NÃO DOCUMENTADO\] Procurar a criação e a remoção de regras

- **Selo / reivindicação:** F / C6.
- **Diretório:** interface web, modal de P26.
- **Comando:** inspecionar o modal "Node Info" e a barra lateral à procura de controle para inserir ou remover regra.
- **Justificativa:** C6 inclui criação e remoção (artigo, pp. 5–6, "Flow Rule Editor"); nem o README nem o código da versão 465648a trazem esse controle.
- **Resultado esperado:** "regra inserida ou removida no switch" (reivindicacoes.md, C6). Pelo código, espera-se não encontrar o controle.
- **Evidência:** `P27_modal.png`, `P27_sidebar.png`.
- **Sucesso:** controle encontrado e regra inserida e removida, visível em nova abertura da "Flow Table".
- **Falha:** controle ausente; registre C6 como não reproduzível nesta versão.
- **Interrupção:** não use `ovs-ofctl` pelo WebShell como substituto: isso não exercita a funcionalidade reivindicada.

## Tempo estimado

O roteiro completo leva cerca de 2 h 25 min a 4 h 40 min, sem contar a redação do parecer. Os autores não informam tempos, exceto 1 minuto para o iperf (README.md:94). O download é a maior incerteza, porque o tamanho da OVA não é informado.

| Etapa | Passos | Estimativa |
| --- | --- | --- |
| Registro do hospedeiro e download da OVA | P1–P3 | 20–90 min |
| Importação, configuração e login | P4–P7 | 15–30 min |
| Teste mínimo, obrigatório | P8–P12, P16 | 20–30 min |
| Teste mínimo, opcional (iperf, Ryu, multicontrolador) | P13–P15 | 15–25 min |
| C1, C2 e C3 | P17–P19 | 15–20 min |
| C4, três modelos com contagem | P20–P23 | 20–30 min |
| C5 | P24–P25 | 10 min |
| C6 | P26–P27 | 10–15 min |
| Organização das evidências | — | 20–30 min |

## Tabela-resumo dos passos

Dos 27 passos, 15 seguem o README e 12 são \[NÃO DOCUMENTADO\]. Os que podem interromper o roteiro estão em P1, P2, P4, P6 e P8–P12; em C4 e C5, uma falha decide R sem parar a coleta.

| Passo | Selo | Reivindicação | Origem | Ação | Sucesso | Interrompe |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | F, R | todas | NÃO DOCUMENTADO | Registrar hospedeiro | VirtualBox 7.1.6, ≥ 8 GB RAM, ≥ 80 GB disco | Sim, se RAM/disco insuficientes |
| P2 | F | pré-requisito | README.md:53 | Baixar OVA | Arquivo com o nome esperado | Sim, se link indisponível |
| P3 | F, R | rastreabilidade | NÃO DOCUMENTADO | sha256 da OVA | Hash registrado | Não |
| P4 | F | pré-requisito | README.md:55 | Importar VM | VM listada | Sim, após 2 falhas |
| P5 | F | pré-requisito | NÃO DOCUMENTADO | Conferir RAM/CPU da VM | ≥ 8 GB, ≥ 1 núcleo | Não |
| P6 | F | pré-requisito | README.md:57, 82 | Iniciar e logar | Sessão aberta | Sim |
| P7 | F, R | rastreabilidade | NÃO DOCUMENTADO | Conferir commit/hashes | 465648a ou hashes iguais | Não |
| P8 | F | C2 | README.md:84-86 | `mininet_gui` | URL impressa, logs sem erro fatal | Sim |
| P9 | F | C1 | README.md:86 | Abrir URL | Três áreas da interface | Sim |
| P10 | F | C1, C2 | README.md:88 | Criar c1 | c1 no grafo e no WebShell | Sim |
| P11 | F | C1, C2, C4 | README.md:90 | Single, c1, 2 hosts | s1, h1, h2 com links verdes | Sim |
| P12 | F | C2 | README.md:92 | Pingall | Tabela h1↔h2 | Sim |
| P13 | F | C5 (apoio) | README.md:94 | iperf h1/h2 | Relatório com vazão | Não |
| P14 | F | C3 | NÃO DOCUMENTADO | `which ryu-manager` | Caminho impresso | Não (pula P15) |
| P15 | F | C3 | README.md:96 | Multicontrolador e link s1–s2 | Linha verde e pingall | Não |
| P16 | F | exportação | README.md:98 | Exportar JSON e script | Dois arquivos não vazios | Não |
| P17 | F | C1 | NÃO DOCUMENTADO | Mover nó e recarregar | Posição mantida | Não |
| P18 | F | C2 | NÃO DOCUMENTADO | `curl` start/hosts | `true` e hosts coerentes | Não |
| P19 | F | C3 | NÃO DOCUMENTADO | Remover link s1–h2 ativo | Link removido, emulação ativa | Não |
| P20 | R | C4 | NÃO DOCUMENTADO | Reset Topology | Grafo e API vazios | Sim, para C4 |
| P21 | R | C4 | README.md:107-108 | Single, 3 hosts | 1 switch, 3 hosts, 3 links | Não (decide C4) |
| P22 | R | C4 | README.md:107-108 | Linear, 3 × 2 | 3 switches, 6 hosts, 8 links | Não (decide C4) |
| P23 | R | C4 | README.md:107-108 | Tree, 2 camadas, fanout 2 | 3 switches, 4 hosts, 6 links | Não (decide C4) |
| P24 | R | C5 | README.md:112-114 | `ip addr show` na aba h1 | `h1-eth0` com 10.0.0.x | Sim, para C5 |
| P25 | R | C5 | NÃO DOCUMENTADO | `ip addr show` na aba h2 | `h2-eth0` com outro IP | Não |
| P26 | F | C6 | NÃO DOCUMENTADO | Duplo clique em s1, Flow Table | Ao menos uma regra exibida | Não |
| P27 | F | C6 | NÃO DOCUMENTADO | Procurar inserção/remoção | Controle encontrado e regra alterada | Não |

**Leitura dos resultados.** F: Atribuir se P8–P12 e P16 tiverem sucesso; Não atribuir se algum deles falhar. R: Atribuir se P21, P22, P23 e P24 tiverem sucesso; Não atribuir se qualquer um falhar. Falha em P27 não decide R pela regra fixada, mas deve constar no parecer.
