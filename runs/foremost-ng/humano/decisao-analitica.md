# Linha de base humana — decisão analitica (foremost-ng)

- avaliador: <nome>
- data_hora: <AAAA-MM-DD HH:MM BRT>
- quando: ANTES de abrir qualquer resposta de LLM, só com os quatro anexos do pacote (mesma regra de decisão do Prompt A).
- conhecimento_previo: <o que você já sabia antes: selos oficiais, resultados da T7, conversas de planejamento. Seja específico; isso define se a linha de base é cega.>

## Selo F

<critérios oficiais, evidências no formato arquivo:linha e justificativa>

## Selo R (por reivindicação)

<uma linha por Cn: reproduzivel | nao_reproduzivel | depende_execucao, com a evidência>

## Decisão

```json
{"F": {"decisao": "Atribuir|Não atribuir|Indeterminado", "confianca": 0, "evidencias": []},
 "R": {"decisao": "Atribuir|Não atribuir|Indeterminado", "confianca": 0, "evidencias": [], "por_reivindicacao": {}}}
```
