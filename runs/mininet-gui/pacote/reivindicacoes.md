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
