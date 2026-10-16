# Cadeia FIC-1 — anthropic (DADOS SINTÉTICOS FALSOS — fixture de teste)

- provedor: anthropic
- modelo_exibido: Claude Ficticio 0.1
- versao: teste-0
- esforco: não exposto
- data_hora_A: 2099-01-01 10:30 BRT
- data_hora_B2: 2099-01-02 15:30 BRT

## Prompt A

Prompt A fictício.

## Resposta A

Sou o Claude, da Anthropic. Ver [FICTICIO.md:§2].

```json
{"F": {"decisao": "Indeterminado", "confianca": 45, "evidencias": ["FICTICIO.md:§2"]},
 "R": {"decisao": "Atribuir", "confianca": 55, "evidencias": ["FICTICIO.md:§2"],
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "reproduzivel"}}}
```

## Prompt B1

Prompt B1 fictício.

## Resposta B1

Plano fictício.

## Prompt B2

Prompt B2 fictício.

## Resposta B2

```json
{"F": {"decisao": "Atribuir", "confianca": 80, "evidencias": ["registro-factual.md:P1"], "mudou": true},
 "R": {"decisao": "Não atribuir", "confianca": 65, "evidencias": ["registro-factual.md:P2"], "mudou": true,
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "nao_reproduzivel"}}}
```
