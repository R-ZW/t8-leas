# Cadeia FIC-1 — openai (DADOS SINTÉTICOS FALSOS — fixture de teste)

- provedor: openai
- **modelo_exibido:** GPT-Ficticio-9
- **versao:** 0.0-teste
- **esforco:** médio
- interface: ChatGPT desktop (fictício), chat avulso com anexos
- data_hora_A: 2099-01-01 10:00 BRT
- data_hora_B1: 2099-01-01 10:20 BRT
- data_hora_B2: 2099-01-02 15:00 BRT

## Prompt A

Prompt A fictício.

## Resposta A

Como ChatGPT, examinei o pacote fictício. A instalação está em [FICTICIO.md:§1], segundo o texto.

## B. Selo F

Só verificável por execução.

```json
{"F": {"decisao": "Indeterminado", "confianca": 40, "evidencias": ["FICTICIO.md:§1"]},
 "R": {"decisao": "Indeterminado", "confianca": 30, "evidencias": ["FICTICIO.md:§3"],
       "por_reivindicacao": {"C1": "depende_execucao", "C2": "depende_execucao"}}}
```

## Prompt B1

Prompt B1 fictício.

## Resposta B1

Plano fictício (P1, P2).

## Prompt B2

Prompt B2 fictício.

## Resposta B2

O registro fictício confirma P1: [registro-factual.md:P1] mostra código 0.

```json
{"F": {"decisao": "Atribuir", "confianca": 85, "evidencias": ["registro-factual.md:P1"], "mudou": true},
 "R": {"decisao": "Não atribuir", "confianca": 70, "evidencias": ["registro-factual.md:P2"], "mudou": true,
       "por_reivindicacao": {"C1": "reproduzivel", "C2": "nao_reproduzivel"}}}
```
