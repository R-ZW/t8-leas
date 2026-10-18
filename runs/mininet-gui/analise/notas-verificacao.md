# Notas da verificação cega das evidências — mininet-gui

Verificação de `evidencias.csv` (258 linhas) conforme o §7 do protocolo, sem conhecer o provedor de M1, M2 e M3.

## Material consultado

- Respostas cegas: `verificacao-cega/M*/cadeia-*.md` (seções `## Resposta A` e `## Resposta B2`).
- `pacote/artefato.txt`: arquivos separados pelos marcadores `INÍCIO/FIM DO ARQUIVO`, com a numeração original de cada um.
- `pacote/artigo.pdf`: texto extraído com `pdftotext -layout`, página a página.
- `pacote/instrucoes-oficiais.md`, `pacote/reivindicacoes.md`.
- `execucao/registro-factual.md`: o SHA-256 confere com `execucao/CONGELAMENTO.sha256`. As linhas citadas pelas LLMs (por exemplo, 77-84 para E09–E17) batem com a numeração desse arquivo.

## Critérios adotados

- Citação de `README.md:…`, `run.sh:…`, `api.py:…` etc. sem o prefixo `artefato.txt:` foi lida como arquivo dentro de `artefato.txt`.
- Uma seção citada por nome abreviado e inequívoco foi aceita como existente. Exemplos: `instrucoes-oficiais.md:Funcional` para “Funcional (F)” e `artigo.pdf:p. 2, §1` para a seção 1 na p. 2, convenção que o próprio `reivindicacoes.md` usa.
- Um intervalo de linhas que inclui linhas em branco no fim, ou passos de outra seção do registro (como `seção 2/E09-E17`, que abrange E15 da seção 3), foi aceito quando o conteúdo pertinente está dentro dele.
- `afirmacao` traz um trecho da resposta ligado à evidência do JSON. Quando a evidência só aparece no JSON, sem citação no corpo do texto, usei a frase da resposta que trata do mesmo ponto.
- Juízos de valor sobre o selo, como “dependências e versões: atendido”, não foram reclassificados. A classe avalia se o local existe e contém o que a resposta diz que contém.

## Casos limítrofes

- **`mininet-gui-frontend/src/core/api.js:299` (3 linhas, todas de M2, etapa A): `mal_interpretada`.** A linha existe e contém `}i`, mas a afirmação é que isso seria erro de sintaxe e impediria a compilação no Vite. Em JavaScript, `}i` seguido de `};` é válido: `i` vira uma instrução de expressão inalcançável depois do `try/catch`, com inserção automática de ponto e vírgula. O registro factual (E08, l. 103) confirma que o frontend compilou sem correção. As respostas B2 de M2 também reconhecem que a previsão estava errada.
- **README como fonte de “dependências e versões” (M2, várias linhas): `correta`.** M2 cita README 26-38/26-99 como prova de que esse critério está “atendido”. O trecho existe e diz o que M2 transcreve: VirtualBox 7.1.6 r167084, RAM, ambiente da demonstração e versões do Ryu na l. 77. Só que a seção “Dependências” não traz versões das dependências Python nem do Mininet. M1 chega à conclusão oposta a partir das mesmas linhas, e M3 fala em “parcial”. Tratei a divergência como juízo sobre o critério, não como leitura errada do local. A nota de cada linha registra que só o VirtualBox tem versão nessa seção.

## Problemas no corpo das respostas, fora do JSON e sem linha no CSV

- M2, cadeia 2, etapa A: afirma que `deleteEdge` usa `dst` sem declarar (`NetworkGraph.vue:256-265`). A variável é declarada na l. 258 (`let dst = this.nodes.get(link.to);`). A própria resposta B2 de M2 reconhece isso.
- M3, cadeia 3, etapa A: cita `[artigo.pdf:p.5, §3, Flow Rule Editor]`, mas o item “Flow Rule Editor” está na p. 6. Na p. 5 está “Flow Rule Integration”.
- M1, cadeia 1, B2: o link para a seção “Dependências” aponta `artefato.txt:119`, uma linha em branco; o cabeçalho está na l. 120. O JSON cita corretamente `README.md:35-38`.

## Contagens

| | correta | mal_interpretada | inexistente | nao_verificavel | total |
|---|---|---|---|---|---|
| M1 | 61 | 0 | 0 | 0 | 61 |
| M2 | 77 | 3 | 0 | 0 | 80 |
| M3 | 117 | 0 | 0 | 0 | 117 |
| **Total** | **255** | **3** | **0** | **0** | **258** |
