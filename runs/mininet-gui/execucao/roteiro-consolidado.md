# Roteiro consolidado — Mininet-GUI (SBRC 2025)

**Montado em:** 2026-10-17, antes de ligar a VM para a execução de referência. **Protocolo:** §6.2 (união dos planos B1 da cadeia 1) e §6.5 (consulta às cadeias 2 e 3 só para achar passo essencial ausente).

**Entradas lidas (extraídas por script, só a parte B1):**

| Sigla | Provedor | Arquivo | Passos no B1 |
|---|---|---|---|
| A | Anthropic | `llm-anthropic/anexos-saida/cadeia-1-B1-documento.md` | P1–P27 |
| O | OpenAI | `llm-openai/cadeia-1.md`, seção `## Resposta B1` | P1–P17 |
| G | Google | `llm-google/cadeia-1.md`, seção `## Resposta B1` | P1–P16 |

As seções `## Resposta A` e a pasta `referencia/` não foram lidas. Neste roteiro, "A P11" significa "passo P11 do plano de A".

**Fontes autorais citadas:** `README.md` do commit avaliado `465648a4…` (numeração de linhas desse arquivo); `artigo.pdf` (páginas 1–9 do PDF); texto da release `v0.0.1` "VM SBRC 2025" (fonte da VM efetivamente usada, ver `ambiente/ambiente.md`); código do commit da VM `be68302…` quando um rótulo da interface precisa ser localizado. Passo sem apoio dos autores leva **[NÃO DOCUMENTADO]**.

## 1. Regras de execução

- **Ambiente:** VM oficial da release `v0.0.1` (OVA de 17/03/2025, código `be68302`), VirtualBox 7.1.6 r167084 (versão pedida em README:37), sobre Hyper-V/NEM. Interface web aberta no navegador do **host** pela rede host-only (`http://192.168.56.101:5173`), porque a VM da release não tem ambiente gráfico. README:86 manda usar "um navegador dentro da VM"; o texto da release manda abrir a URL "em um navegador" e dá o exemplo `http://192.168.56.101:5173`.
- **RAM da VM: 8 GB (8192 MB), 2 vCPUs.** O README traz dois valores: "Mínimo de 8GB para a máquina virtual" (README:38) e "no mínimo 2GB de RAM e um core de CPU" (README:103). A OVA vem com 1536 MB e 1 vCPU, abaixo dos dois. Decisão: usar o valor mais exigente (8 GB), como propõem A P5 e o §12 do protocolo; O P1 e G (seção 1) só registram a divergência. A divergência fica registrada; não foi resolvida pelos autores.
- **Ordem:** (1) teste mínimo do README, passos 1–9; (2) C4; (3) C5; (4) passos [NÃO DOCUMENTADO] de C1, C2, C3 e C6. Os passos [NÃO DOCUMENTADO] que fazem parte de C4 e C5 (limpeza, contagem, `ip addr`) rodam dentro dos blocos de C4 e C5, mas são registrados como desvios declarados.
- **Desvios:** D0 = segue a documentação; D1 = correção trivial; D2 = passo ou contorno [NÃO DOCUMENTADO]; D3 = insumo externo. Todo passo [NÃO DOCUMENTADO] é registrado como D2, em seção separada do registro factual.
- **Tempo máximo:** **2 h por reivindicação** (C1–C6), contadas do primeiro passo do bloco. O teste mínimo tem também 2 h. Ao estourar, o bloco é encerrado com status "inconclusivo (tempo esgotado)".
- **Critério de desistência** de um passo ou bloco:
  1. surge um erro não documentado que só se contorna com desvio D2 em **passo essencial** (passos 1–6 e 9 do teste mínimo, geração em C4, comando no WebShell em C5). O contorno não é aplicado como se fosse dos autores: registra-se o erro, a evidência e o status "falha" ou "bloqueado"; um contorno só é tentado depois, registrado como D2 e separado;
  2. o tempo máximo do bloco se esgota;
  3. a VM fica inutilizável sobre o Hyper-V (não inicia, trava ou não responde por 10 min): registra-se o fato e para-se a execução, sem trocar de ambiente.
  Passos opcionais (README:94 e 96) e [NÃO DOCUMENTADO] não interrompem a execução: falham e a execução segue.
- **Registro por passo:** ação ou comando, código de saída (comandos), início/fim em UTC e duração, trecho da saída, captura de tela com hora UTC no nome e na imagem, SHA-256 de cada arquivo exportado.

## 2. Passos consolidados

Colunas: **ID** do roteiro consolidado; **Origem** = passos dos provedores que o propuseram; **Fonte autoral** ou [NÃO DOCUMENTADO]; **Ação**; **Esperado**; **Desvio previsto**.

### 2.1 Preparação (já feita pela sessão de ambiente; aqui só se confere e registra)

| ID | Origem | Fonte autoral | Ação | Esperado | Desvio |
|---|---|---|---|---|---|
| E01 | A P1, O P1 | [NÃO DOCUMENTADO] (requisitos em README:26-38, 103) | Registrar host, versão do VirtualBox, RAM livre e disco | VirtualBox 7.1.6r167084; recursos registrados | D2 (registro) |
| E02 | A P2, O P2, G P1 | README:53 (link do Drive); release `v0.0.1` (ZIP no GitHub) | Obter a OVA | arquivo da VM dos autores | link do README inativo (ver `versao.md`); OVA obtida pela release dos mesmos autores |
| E03 | A P3 | [NÃO DOCUMENTADO] | SHA-256 da OVA | hash registrado (sem referência dos autores) | D2 (registro) |
| E04 | A P4, O P2, G P1 | README:55; release, passos 2–3 | Importar a OVA no VirtualBox | VM listada | D0 |
| E05 | A P5, O P1 | [NÃO DOCUMENTADO] (README:38 × 103) | Conferir/ajustar RAM e CPU da VM | 8192 MB, ≥ 1 vCPU | D2 (ajuste de 1536 → 8192 MB, 1 → 2 vCPUs) |
| E06 | A P6, O P2, G P1 | README:57, 82 | Iniciar a VM e entrar (`mininet`/`mininet`) | sessão aberta ("área de trabalho" no README; console na VM da release) | D0 |
| E07 | A P7, O P3 | [NÃO DOCUMENTADO] | `git -C /home/mininet/mininet-gui rev-parse HEAD`, `status --short` | commit registrado; comparar com `465648a4…` | D2 (registro) |
| E08 | G P2 | [NÃO DOCUMENTADO] | Inspecionar `mininet-gui-frontend/src/core/api.js` (linha com `}i`) e o carregamento do nvm pelo `run.sh` **sem corrigir**; a correção proposta por G só seria aplicada, como D2, se o frontend falhar no E09 | registro do conteúdo | D2 (inspeção) |

### 2.2 Teste mínimo do README (selo F)

| ID | Origem | Fonte autoral | Ação | Esperado (autores) | Desvio |
|---|---|---|---|---|---|
| E09 | A P8, O P4, G P3 | README:84 | Em shell interativo da VM: `mininet_gui` (alternativa `/home/mininet/mininet-gui/run.sh`); guardar `nohup.out` do backend e do frontend (A P8, G P3) | URL impressa no terminal (README:86); `uvicorn` em :8000 e `vite` em :5173 (G P3) | D0 (registro dos logs: D2) |
| E10 | A P9, O P5, G P3 | README:86; release, Teste mínimo passo 3 | Abrir a URL impressa no navegador do host | interface com barra lateral, grafo e WebShell (artigo p. 7, Fig. 2) | D1 (navegador do host, não da VM) |
| E11 | A P10, O P6, G P4 | README:88 | Arrastar "Controller" para o centro; "Default"; "Submit" | controlador `c1` criado | D0 |
| E12 | A P11, O P7, G P4 | README:90 | "Generate Topology" → Single, Controller c1, Hosts 2 → "Submit" | `s1`, `h1`, `h2`, links ativos em verde, associação `s1`–`c1` pontilhada (artigo p. 7) | D0 |
| E13 | A P12, O P8, G P5 | README:92 | "Run Pingall Test" e aguardar | resultados exibidos (tabela h1→h2 e h2→h1) | D0 |
| E14 | A P13, O P12–P13, G P6 | README:94 (opcional) | Aba `h1`: `iperf -s`; aba `h2`: `iperf -c 10.0.0.1`; aguardar 1 min; encerrar o servidor com Ctrl+C (A P13) | relatório do iperf com vazão em `h2` | D0 |
| E15 | A P14 | [NÃO DOCUMENTADO] | `which ryu-manager` / `command -v ryu-manager` na VM | caminho do Ryu | D2 |
| E16 | A P15, O P15, G P7 | README:96 (opcional) | Novo Controller Remote 127.0.0.1:6633 (`c2`); Single, 2 hosts, c2; "Create Link" `s1`→`s2`; aba `c2`: `ryu-manager --ofp-tcp-listen-port 6633 ryu.app.simple_switch_13`; "Run Pingall Test" | linha verde `s1`–`s2`; Ryu em execução; pingall com os 4 hosts | D0 |
| E17 | A P16, O P9, G P8 | README:98 | "Export Topology (JSON)" e "Export Mininet Script"; SHA-256 dos arquivos; validade de JSON e de sintaxe Python (G P8) | arquivo JSON da topologia atual e script do Mininet | D0 (validação: D2) |

### 2.3 C4 — Geração automatizada (Single, Linear, Tree)

Fonte: README:105-108 ("Generate Topology", tipo e "número de dispositivos", "clique em OK"); artigo p. 6 ("Topology Generator") e pp. 6–7 (caso 1, Fig. 2). O botão do formulário é "Submit" (TopologyForm.vue). Linear pede "Switches" e "Hosts per switch"; Tree pede "Layers" e "Fanout"; o README não cita esses campos. Quantidades fixadas **antes** da execução:

| ID | Origem | Fonte autoral | Ação | Esperado (contagem derivada pelos revisores; os autores não a declaram) | Desvio |
|---|---|---|---|---|---|
| E18 | A P20, G P12–P14 (passo 1), cadeia 2 de A (P17) | [NÃO DOCUMENTADO] (botão "Reset Topology" existe; artigo p. 7) | "Reset Topology" → confirmar; recriar `c1` Default (G P12–P14, passo 2) antes de cada modelo | grafo vazio; API sem nós; depois só `c1` | D2 |
| E19 | A P21, G P12 | README:107-108 (valor: [NÃO DOCUMENTADO]) | Single, Controller c1, Hosts = 3 | 1 switch, 3 hosts, 3 links host–switch | D0 (valores: D2) |
| E20 | A P22, G P13 | README:107-108 (valores: [NÃO DOCUMENTADO]) | Linear, c1, Switches = 3, Hosts per switch = 2 | 3 switches em cadeia, 6 hosts, 8 links (6 host–switch, 2 switch–switch) | D0 (valores: D2) |
| E21 | O P10 | README:107-108 (valores: [NÃO DOCUMENTADO]) | Linear, c1, Switches = 2, Hosts per switch = 1 | 2 switches, 2 hosts, 3 links | D0 (valores: D2) |
| E22 | A P23, O P11, G P14 | README:107-108 (valores: [NÃO DOCUMENTADO]) | Tree, c1, Layers = 2, Fanout = 2 | 3 switches (1 raiz, 2 filhos), 4 hosts, 6 links | D0 (valores: D2) |
| E23 | A P21–P23 (contagem por `curl`) | [NÃO DOCUMENTADO] (endpoints `/api/mininet/{switches,hosts,links}` no código) | Após cada modelo, contar nós e links pela API do backend na VM, e registrar o grafo antes/depois (O P10–P11) | contagens iguais às da coluna "esperado" | D2 |

O plano O não limpa a topologia entre modelos; o roteiro limpa (E18), conforme A e G, e registra o estado antes e depois de cada geração, conforme O. O plano A sugere Controller "none" para isolar a geração; G sugere `c1` ou `none`; o roteiro usa `c1` em todos os modelos (README:90 usa `c1` no exemplo) e registra a escolha.

### 2.4 C5 — WebShell no namespace do nó

Fonte: README:110-114 (criar nó, aba do nó no "Webshell", comandos bash "no namespace daquele nó"); artigo p. 5 ("Node Terminal Sessions"), p. 6 ("Webshell", caso 2), p. 7 (Fig. 2, aba `h1` com `ip addr`). Executado sobre a topologia Tree do E22.

| ID | Origem | Fonte autoral | Ação | Esperado | Desvio |
|---|---|---|---|---|---|
| E24 | A P24, O P14, G P15 | README:112-114 (o comando é [NÃO DOCUMENTADO]; artigo p. 7, Fig. 2 mostra `ip addr`) | Aba `h1` → `ip addr show` | saída na aba `h1` com `lo` e `h1-eth0` (10.0.0.x) | D0 (comando: D2) |
| E25 | A P25 | [NÃO DOCUMENTADO] | Aba `h2` → `ip addr show` | `h2-eth0` com IP diferente do de `h1` | D2 |
| E26 | G P15 | [NÃO DOCUMENTADO] | Aba `h1` → `ping -c 2 10.0.0.2` | respostas de 10.0.0.2 | D2 |
| E27 | cadeia 2 de A (P21: "distintos da VM") | [NÃO DOCUMENTADO] | No terminal da VM (fora da interface), `ip -br addr` para comparar com as saídas das abas | VM mostra `eth0` 192.168.56.101, sem `h1-eth0` | D2 |

E14 (iperf nas abas `h1`/`h2`) também serve como observação de C5, como propõem O (P12–P13) e G (P6).

### 2.5 Passos [NÃO DOCUMENTADO] de C1, C2, C3 e C6 (desvios declarados)

| ID | Origem | Reivindicação | Ação | Esperado | Desvio |
|---|---|---|---|---|---|
| E28 | A P17, G P9 | C1 | Arrastar `h1` para outra posição e recarregar a página (A); criar Host e Switch arrastando da paleta e ligá-los com "Create Link" (G) | nó acompanha o arraste e mantém a posição após recarregar; nós arrastados aparecem e se ligam | D2 |
| E29 | A P18, G P10 | C2 | `curl -s http://localhost:8000/api/mininet/start` e `/hosts` na VM; "Run Pingall Test" com a topologia ativa (G) | `true` e hosts iguais aos do grafo; tabela de pingall | D2 |
| E30 | A P19, G P11, O P16 (sem comando; registra a lacuna); cadeia 2 de A (P16: contar reinícios no log) | C3 | Com a emulação ativa: selecionar link `s1`–`h2` → "Delete Selected"; selecionar um nó → "Delete Selected"; "Run Pingall Test"; `curl` em `/start` e `/links`; procurar reinício da rede no `nohup.out` do backend | link/nó somem do grafo e da API; pingall sem o nó removido; `start` continua `true`; nenhum reinício no log | D2 |
| E31 | A P26, G P16 | C6 | "Run Pingall Test" com controlador; duplo clique em `s1` → aba "Flow Table" | tabela com ao menos uma regra | D2 |
| E32 | A P27, G P16, O P17 (sem comando; registra a lacuna) | C6 | Procurar no modal "Node Info" e na barra lateral um controle para inserir ou remover regra | controle presente e regra inserida/removida (artigo pp. 5–6), ou ausência registrada | D2 |

## 3. Passos das cadeias 2 e 3 consultados (§6.5)

Todos os passos dos B1 das cadeias 2 e 3 dos três provedores têm correspondente acima, com estas exceções, que **não** foram consideradas essenciais e ficam fora da execução:

- cadeia 3 de A, P28: inserir e remover regra com `ovs-ofctl` fora da interface, como contraprova da "Flow Table". A cadeia 1 de A (P27) diz para não usar `ovs-ofctl` como substituto; o passo não exercita a função reivindicada.
- cadeia 3 de A, P22, e cadeia 2 de A, P13 e P18: contar nós e links pelos JSON exportados. O E23 já conta pela API; o JSON exportado do teste mínimo é guardado no E17.
- cadeia 3 de A, P25: `ping` a partir de `h1`. Já coberto pelo E26.
- cadeia 3 de A, P17 ("pingall e sessão h1 após remoção"): **incluído durante a execução, dentro do E30.** O Pingall após as remoções falhou (HTTP 500); o comando na sessão `h1` foi o meio que restou para observar se a emulação continuava ativa. Fica registrado como D2.
- cadeias 2 e 3 de A, P24/P14: reunir logs e SHA-256. Já faz parte das regras de registro (seção 1).

## 4. Tempo previsto

| Bloco | IDs | Previsão | Limite |
|---|---|---|---|
| Preparação (conferência) | E01–E08 | 15 min | — |
| Teste mínimo | E09–E17 | 30–60 min (NEM pode alongar) | 2 h |
| C4 | E18–E23 | 30–45 min | 2 h |
| C5 | E24–E27 | 15 min | 2 h |
| C1, C2, C3, C6 | E28–E32 | 30–45 min | 2 h cada |
