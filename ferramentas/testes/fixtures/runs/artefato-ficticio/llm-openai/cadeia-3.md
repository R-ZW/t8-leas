# Cadeia FIC-3 — openai (DADOS SINTÉTICOS FALSOS — fixture de teste)

- provedor: openai
- modelo_exibido: GPT-Ficticio-9
- versao: 0.0-teste
- esforco: médio
- data_hora_A: 2099-01-01 12:00 BRT
- data_hora_B2: 2099-01-02 16:00 BRT

## Prompt A

Ao final, inclua um bloco JSON:
{"F": {"decisao": "...", "confianca": 0, "evidencias": ["arquivo:local"]}, "R": {"decisao": "...", "confianca": 0, "evidencias": []}}

## Resposta A

Repetindo o modelo pedido: {"F": {"decisao": "...", "confianca": 0}, "R": {"decisao": "...", "confianca": 0}}

Minha decisão final:

{"F": {"decisao": "Indeterminado", "confianca": 50, "evidencias": ["FICTICIO.md:§4"]},
 "R": {"decisao": "Indeterminado", "confianca": 40, "evidencias": ["FICTICIO.md:§5"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao"}}}

## Prompt B1

Prompt B1 fictício.

## Resposta B1

Plano fictício.

## Prompt B2

Prompt B2 fictício.

## Resposta B2

```json
{"F": {"decisao": "Atribuir", "confianca": 90, "evidencias": ["registro-factual.md:P1"]},
 "R": {"decisao": "Indeterminado", "confianca": 50, "evidencias": ["registro-factual.md:P3"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "depende_execucao"}},
 "mudou": {"F": true, "R": false}}
```
