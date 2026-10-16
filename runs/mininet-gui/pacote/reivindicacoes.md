# Reivindicações pré-definidas — Mininet-GUI (SBRC 2025)

**Versão do código:** proxy [`465648a4425a4457af0348ab951cf7f71d37a86f`](https://github.com/latarc/mininet-gui/commit/465648a4425a4457af0348ab951cf7f71d37a86f), 22/04/2025. **Escopo:** mapa documental anterior às conversas avaliadoras; nenhuma VM ou rede foi executada nesta T8. Artigo: `artigo.pdf`, cópia prevista de `fontes/mininet-gui.pdf` (páginas físicas 1–9). Documentação: [README nesse SHA](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md). Critério externo: [instruções de revisão do SBRC 2025](https://doc-artefatos.github.io/sbrc2025/revinstrucoes.html), seções F e R. Os critérios de sucesso abaixo são regras de observação fixadas para o estudo; não afirmam execução nem completam lacunas dos autores.

## Confronto e regra fixa para R

O artigo enumera **seis contribuições** na p. 2, §1. No [README fixado, seção “Experimentos”](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L101-L114), os autores nomeiam **somente duas** reivindicações com procedimento: geração automatizada e WebShell. Portanto, **C4 e C5 são as principais para R neste estudo**. A regra é textual e anterior ao teste: entra no núcleo de R uma contribuição da lista de seis que tenha subseção própria em “Experimentos” do README do SHA. As demais permanecem no mapa e podem embasar F ou teste complementar. A seção “Teste mínimo” documenta outras ações, mas não as eleva a experimento principal. Esta operacionalização não elimina a lacuna de documentação das outras quatro contribuições nem substitui o juízo exigido pelas regras oficiais sobre as principais reivindicações do artigo.

| Contribuição enumerada no artigo p. 2 | ID | Subseção própria em “Experimentos” no README? | Papel fixado |
|---|---|---|---|
| Interface web dinâmica | C1 | Não | Contribuição descrita; observação funcional no teste mínimo |
| Emulação integrada | C2 | Não | Contribuição descrita; `pingall` no teste mínimo |
| Modificações em tempo real | C3 | Não | Contribuição descrita; procedimento específico indisponível |
| Geração automática de topologias | C4 | **Sim** | **Principal para R** |
| Terminal dos nós via WebShell | C5 | **Sim** | **Principal para R** |
| Visualização e criação de regras de fluxo | C6 | Não | Contribuição descrita; procedimento específico indisponível |

## C1 — Interface web dinâmica

- **Classe / R:** contribuição descrita; não principal para R; observação funcional coberta em parte pelo teste mínimo.
- **Afirmação:** a interface web permite criar e manipular visualmente elementos/topologias em um grafo interativo.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2, §1, contribuição 1; pp. 4–6, §3 (frontend, Network Controls/Manipulation); p. 7, Fig. 2 e descrição das áreas da interface.
- **Procedimento dos autores no SHA:** [README, “Instalação” e “Teste mínimo”, passos 1–5](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L47-L90): iniciar a VM, executar `mininet_gui`, abrir URL impressa, arrastar “Controller” e gerar uma topologia Single com 2 hosts. Sem subseção própria em “Experimentos”.
- **Entrada exigida:** VM/código do SHA em ambiente Mininet compatível, navegador na VM, controlador Default, topologia Single/2 hosts. O vínculo do código da OVA ao SHA ainda não foi verificado.
- **Resultado observável:** página acessível, controlador e nós/links representados no grafo e resposta às ações do usuário.
- **Critério de sucesso pré-fixado:** registrar a URL aberta e capturas antes/depois mostrando que as ações documentadas criaram a topologia visível; página estática sozinha não basta.
- **Limitação:** o README não fornece medida de usabilidade, tempo de resposta ou gabarito gráfico; esse teste mostra a função, não a superioridade comparativa alegada na motivação.
- **Fontes:** artigo pp. 1–2, 4–7; [README fixado, linhas 47–90](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L47-L90).

## C2 — Emulação integrada

- **Classe / R:** contribuição descrita; não principal para R; teste mínimo funcional.
- **Afirmação:** a ferramenta inicia/gerencia emulação Mininet na interface, permitindo teste de conectividade da rede criada.
- **Artigo:** `artigo.pdf`, p. 2, §1, contribuição 2; pp. 4–5, §3 (backend/Mininet Integration); p. 6, §4, caso 1, “Modelagem rápida”.
- **Procedimento dos autores no SHA:** [README, “Teste mínimo”, passos 4–6](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L88-L92): criar controlador Default, Single/2 hosts e clicar “Run Pingall Test”. Não há subseção própria em “Experimentos”.
- **Entrada exigida:** Mininet/Open vSwitch operantes na VM, controlador Default e dois hosts gerados; OVA/ambiente ainda não executados.
- **Resultado observável:** nós emulados e resultado de `pingall` exibido na interface.
- **Critério de sucesso pré-fixado:** obter resultado de `pingall` correspondente à rede criada, com conectividade registrada entre os dois hosts; salvar captura/saída e anotar eventuais perdas. Apenas iniciar frontend/API não satisfaz.
- **Limitação:** o README não fixa porcentagem/latência esperada, comando de inspeção do Mininet ou resultado de referência; não inferir comparação quantitativa com outras ferramentas.
- **Fontes:** artigo pp. 2, 4–6; [README fixado, linhas 88–92](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L88-L92).

## C3 — Modificação da topologia em tempo real

- **Classe / R:** contribuição descrita; não principal para R; **procedimento específico indisponível**.
- **Afirmação:** nós e links podem ser criados/removidos com a emulação em andamento, sem interrompê-la ou reiniciá-la.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2, §1, contribuição 3; p. 6, §3, parágrafo sobre métodos `start`/`stop` e associação de switches a controladores; p. 7, descrição da barra lateral.
- **Procedimento dos autores no SHA:** [README, “Teste mínimo”, passo 8 opcional](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L96-L96) ensina acrescentar controlador, gerar outra topologia e conectar switches; **não** especifica manter a primeira emulação ativa e medir ausência de reinício. Não há subseção “Experimentos” para C3.
- **Entrada exigida:** rede em execução com estado observável, novo nó/link e controlador configurado. O README não fornece gabarito para continuidade do estado.
- **Resultado observável:** grafo/rede alterados enquanto a emulação permanece ativa, sem reinicialização visível.
- **Critério de sucesso pré-fixado:** se um roteiro complementar for criado, registrar estado/conectividade antes e depois e evidência de que não houve parada/reinício. Não atribuir esse teste aos autores.
- **Limitação:** o passo opcional de múltiplos controladores não reproduz por si só a reivindicação temporal; procedimento e resultado específicos **indisponíveis**.
- **Fontes:** artigo pp. 1–2, 6–7; [README fixado, passo 8](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L96-L96).

## C4 — Geração automatizada de topologias

- **Classe / R:** contribuição descrita **e experimento explicitamente documentado**; **principal para R**.
- **Afirmação:** o gerador cria topologias dos modelos Single, Linear e Tree com número de dispositivos escolhido pelo usuário.
- **Artigo:** `artigo.pdf`, p. 2, §1, contribuição 4; p. 6, §3, item “Topology Generator”; pp. 6–7, §4, caso 1 e Fig. 2.
- **Procedimento dos autores no SHA:** [README, “Experimentos”, primeira reivindicação](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L101-L108): após iniciar `mininet_gui` e abrir a interface, clicar “Generate Topology”, escolher Single/Linear/Tree e quantidade de dispositivos, confirmar. [“Teste mínimo”, passo 5](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L90-L90) fixa exemplo Single, controlador c1 e 2 hosts.
- **Entrada exigida:** VM ou ambiente equivalente do SHA, controlador quando exigido pela interface, escolha dos três modelos e quantidades registradas antes do teste. O README não fixa uma quantidade para Linear/Tree.
- **Resultado observável:** cada ação cria grafo de topologia do modelo selecionado com dispositivos correspondentes à escolha; deve ser possível inspecionar a rede gerada.
- **Critério de sucesso pré-fixado:** para cada modelo, guardar seleção e captura do grafo/estado resultante, confirmando tipo e quantidade solicitados; uma execução apenas Single não cobre os três modelos reivindicados.
- **Limitação:** autores não fornecem configuração completa, número esperado de links por cenário, saídas de referência, tempos ou script de coleta; a observação pode demonstrar os modelos, mas a reprodução quantitativa fica limitada.
- **Fontes:** artigo pp. 2, 6–7; [README fixado, linhas 101–108](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L101-L108).

## C5 — WebShell integrado aos nós

- **Classe / R:** contribuição descrita **e experimento explicitamente documentado**; **principal para R**.
- **Afirmação:** a aba WebShell permite executar comandos Bash diretamente no namespace de um nó emulado.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2, §1, contribuição 5; p. 5, §3, “Node Terminal Sessions”; p. 6, §3, “Webshell” e §4, caso 2; p. 7, Fig. 2/painel inferior.
- **Procedimento dos autores no SHA:** [README, “Experimentos”, segunda reivindicação](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L110-L114): iniciar interface, criar nó, selecionar sua aba “Webshell” e executar comandos Bash. [“Teste mínimo”, passo 7 opcional](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L94-L94) especifica `iperf -s` em h1 e `iperf -c 10.0.0.1` em h2 por cerca de um minuto; isto é complemento, não a subseção principal.
- **Entrada exigida:** nó emulado com WebShell disponível e um comando Bash escolhido/registrado; para o cenário iperf, dois hosts e `iperf` instalado. Nenhum comando nem saída fixa constam da subseção “Experimentos”.
- **Resultado observável:** saída do comando aparece na aba do nó selecionado e corresponde ao namespace desse nó.
- **Critério de sucesso pré-fixado:** registrar comando, nó, saída e evidência do namespace de origem; para o teste opcional iperf, registrar servidor/cliente e vazão mostrada, sem exigir valor não publicado.
- **Limitação:** a subseção autoral é curta e não fornece comando, saída esperada ou método para comprovar isolamento de namespace; esse controle adicional é operacionalização do estudo. Vazão iperf não é gabarito de 2025.
- **Fontes:** artigo pp. 1–2, 5–7; [README fixado, linhas 94 e 110–114](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L94-L114).

## C6 — Visualização e criação de regras de fluxo

- **Classe / R:** contribuição descrita; não principal para R; **procedimento específico indisponível**.
- **Afirmação:** a interface permite visualizar, criar e remover regras OpenFlow nas tabelas dos switches.
- **Artigo:** `artigo.pdf`, p. 2, §1, contribuição 6; p. 5, §3, “Flow Rule Integration”; p. 6, §3, “Flow Rule Editor”; p. 7, §5.
- **Procedimento dos autores no SHA:** [README, “Teste mínimo” e “Experimentos”](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L80-L114) **não** dá sequência de cliques, regra de exemplo, switch, ação ou resultado para o editor de fluxos. Procedimento **indisponível**.
- **Entrada exigida:** rede com switch OpenFlow e regra de fluxo identificada; autores não fixam regra/configuração de teste.
- **Resultado observável:** tabela de fluxo exibida, regra inserida/removida e efeito correspondente no switch/tráfego.
- **Critério de sucesso pré-fixado:** num teste complementar, registrar regra antes/depois no editor e no switch, com efeito observado; não tratar simples presença do botão como prova.
- **Limitação:** sem receita/autoral e gabarito, não há experimento reproduzível para C6 no README fixado.
- **Fontes:** artigo pp. 2, 5–7; [README fixado, linhas 80–114](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md).

## Casos de uso do artigo e testes complementares

| Caso do artigo | Localização | Procedimento no README fixado | Classificação |
|---|---|---|---|
| Modelagem rápida e conectividade | `artigo.pdf`, p. 6, §4, item 1 | “Teste mínimo”, passos 4–6: controlador Default, Single/2 hosts e `pingall` | Demonstração complementar de C1, C2 e C4; `pingall` não é terceira subseção de “Experimentos” |
| Avaliação de desempenho com iperf via WebShell | `artigo.pdf`, p. 6, §4, item 2 | “Teste mínimo”, passo 7 **opcional**, `iperf -s`/`iperf -c` | Demonstração complementar de C5; sem meta de vazão publicada |
| Topologia multicontrolador | `artigo.pdf`, p. 7, §4, item 3 | “Teste mínimo”, passo 8 **opcional**, segundo controlador Remote/Ryu, ligação e `pingall` | Demonstração complementar; não prova por si só C3 (continuidade sem reinício) |
| Exportação JSON/Python | `artigo.pdf`, p. 1 (resumo), p. 5, §3, “Topology Exporter”, p. 7 (barra lateral) | “Teste mínimo”, passo 9 | Funcionalidade complementar; fora das seis contribuições enumeradas e do núcleo R |

**Condição de ambiente registrada, sem execução:** o [README do SHA](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L35-L38) pede VirtualBox 7.1.6 e 8 GB para a VM, mas a [seção “Experimentos”](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md#L101-L103) fala em 2 GB e um núcleo. A tentativa foi planejada com 8 GB e ao menos um núcleo, sujeita à disponibilidade real. O link de OVA do README histórico não abriu na consulta; nenhuma hipótese sobre seu commit interno é tratada como fato.
