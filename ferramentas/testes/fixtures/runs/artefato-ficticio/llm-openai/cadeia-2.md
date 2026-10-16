# Cadeia FIC-2 — openai (DADOS SINTÉTICOS FALSOS — fixture de teste)

- provedor: openai
- modelo_exibido: GPT-Ficticio-9
- versao: 0.0-teste
- esforco: médio
- data_hora: 2099-01-01 11:00 BRT

## Prompt A

Prompt A fictício.

## Resposta A

JSON com aspas tipográficas, caixa alta, chaves acentuadas e confiança em porcentagem:

~~~
{“F”: {“decisao”: “INDETERMINADO”, “confiança”: “35%”, “evidências”: [“FICTICIO.md:§1”]},
 “R”: {“decisão”: “NÃO ATRIBUIR”, “confianca”: 20, “evidencias”: [“FICTICIO.md:§2”],
       “por_reivindicação”: {“C1”: “Não reproduzível”, “C2”: “depende de execução”}}}
~~~

## Prompt B1

Prompt B1 fictício.

## Resposta B1

Plano fictício.

## Prompt B2

Prompt B2 fictício.

## Resposta B2

```JSON
{"F": {"decisao": "atribuir", "confianca": 80, "evidencias": ["registro-factual.md:P1"], "mudou": true},
 "R": {"decisao": "Nao_atribuir", "confianca": 75, "evidencias": ["registro-factual.md:P2"], "mudou": false,
       "por_reivindicacao": {"C1": "Reproduzível", "C2": "nao_reproduzivel"}}}
```
