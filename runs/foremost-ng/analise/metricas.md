# Métricas — foremost-ng

Gerado por `ferramentas/metricas.py` a partir de `decisoes.csv`. Todas as medidas são descritivas: com um único artefato não há base para testes estatísticos.

## 1. Decisão modal, estabilidade e cobertura

Estabilidade = cadeias com a decisão modal / cadeias esperadas (3). Cobertura = decisões ≠ Indeterminado / decisões extraídas.

| LLM | Etapa | Selo | Decisões por cadeia | Modal | Estabilidade | Cobertura | Oficial | Coincide |
|---|---|---|---|---|---|---|---|---|
| OpenAI | A | F | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| OpenAI | A | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| OpenAI | B | F | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| OpenAI | B | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Anthropic | A | F | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Anthropic | A | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Anthropic | B | F | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Anthropic | B | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Google | A | F | c1: Indet., c2: Indet., c3: Indet. | Indet. | 3/3 | 0/3 (0%) | Atribuir | Não |
| Google | A | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |
| Google | B | F | c1: Atribuir, c2: Atribuir, c3: Atribuir | Atribuir | 3/3 | 3/3 (100%) | Atribuir | Sim |
| Google | B | R | c1: Não atribuir, c2: Não atribuir, c3: Não atribuir | Não atribuir | 3/3 | 3/3 (100%) | Atribuir | Não |

Cobertura agregada (F e R):

| LLM | Etapa | Cobertura |
|---|---|---|
| OpenAI | A | 6/6 (100%) |
| OpenAI | B | 6/6 (100%) |
| Anthropic | A | 6/6 (100%) |
| Anthropic | B | 6/6 (100%) |
| Google | A | 3/6 (50%) |
| Google | B | 6/6 (100%) |

## 2. Empates de moda

Nenhum empate de moda.

## 3. Tabela comparativa (§9, item 10)

"Causa da divergência" e "Evidência-chave" são preenchidas à mão. Causas admitidas (§8): Erro de julgamento da LLM; Interpretação do critério; Insumo indisponível publicamente; Diferença de versão; Ambiente; Possível erro do comitê. "n.a." = modal A e B coincidem com o oficial.

| LLM | Selo | Oficial | Analítica (modal, estabilidade) | Após execução (modal, estabilidade) | Coincide (A / B) | Mudou? | Causa da divergência | Evidência-chave |
|---|---|---|---|---|---|---|---|---|
| OpenAI | F | Atribuir | Não atribuir (3/3) | Não atribuir (3/3) | Não / Não | Não | _(preencher)_ | _(preencher)_ |
| OpenAI | R | Atribuir | Não atribuir (3/3) | Não atribuir (3/3) | Não / Não | Não | _(preencher)_ | _(preencher)_ |
| Anthropic | F | Atribuir | Não atribuir (3/3) | Não atribuir (3/3) | Não / Não | Não | _(preencher)_ | _(preencher)_ |
| Anthropic | R | Atribuir | Não atribuir (3/3) | Não atribuir (3/3) | Não / Não | Não | _(preencher)_ | _(preencher)_ |
| Google | F | Atribuir | Indet. (3/3) | Atribuir (3/3) | Não / Sim | Sim | _(preencher)_ | _(preencher)_ |
| Google | R | Atribuir | Não atribuir (3/3) | Não atribuir (3/3) | Não / Não | Não | _(preencher)_ | _(preencher)_ |

## 4. Critério pré-registrado de consistência

Consistente com o oficial = modal após execução igual ao oficial e estabilidade ≥ 2/3. Consistentes entre si = as três LLMs com a mesma modal.

| LLM | Selo | Modal B | Estabilidade B | Oficial | Consistente com o oficial? |
|---|---|---|---|---|---|
| OpenAI | F | Não atribuir | 3/3 | Atribuir | Não |
| OpenAI | R | Não atribuir | 3/3 | Atribuir | Não |
| Anthropic | F | Não atribuir | 3/3 | Atribuir | Não |
| Anthropic | R | Não atribuir | 3/3 | Atribuir | Não |
| Google | F | Atribuir | 3/3 | Atribuir | Sim |
| Google | R | Não atribuir | 3/3 | Atribuir | Não |

### Consistência e concordância entre LLMs

Pares concordantes = pares de LLMs com a mesma modal, entre os pares comparáveis (sem empate e com decisões).

| Etapa | Selo | Modais | Consistentes entre si? | Pares concordantes | Pares |
|---|---|---|---|---|---|
| Analítica (A) | F | OpenAI: Não atribuir / Anthropic: Não atribuir / Google: Indet. | Não | 1/3 | OpenAI–Anthropic: igual; OpenAI–Google: diferente; Anthropic–Google: diferente |
| Analítica (A) | R | OpenAI: Não atribuir / Anthropic: Não atribuir / Google: Não atribuir | Sim | 3/3 | OpenAI–Anthropic: igual; OpenAI–Google: igual; Anthropic–Google: igual |
| Após execução (B) | F | OpenAI: Não atribuir / Anthropic: Não atribuir / Google: Atribuir | Não | 1/3 | OpenAI–Anthropic: igual; OpenAI–Google: diferente; Anthropic–Google: diferente |
| Após execução (B) | R | OpenAI: Não atribuir / Anthropic: Não atribuir / Google: Não atribuir | Sim | 3/3 | OpenAI–Anthropic: igual; OpenAI–Google: igual; Anthropic–Google: igual |

## 5. Execução confirma ou contradiz (§9, item 12)

Uma linha por cadeia com decisão nas duas etapas. "Confirma" ainda requer conferir se a evidência é coerente; "Passo do registro que motivou" é preenchido à mão.

| LLM | Selo | Cadeia | Decisão A | Decisão B | Relação | Passo do registro que motivou |
|---|---|---|---|---|---|---|
| OpenAI | F | 1 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| OpenAI | F | 2 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| OpenAI | F | 3 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| OpenAI | R | 1 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| OpenAI | R | 2 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| OpenAI | R | 3 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | F | 1 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | F | 2 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | F | 3 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | R | 1 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | R | 2 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Anthropic | R | 3 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Google | F | 1 | Indet. | Atribuir | Resolve incerteza | _(preencher)_ |
| Google | F | 2 | Indet. | Atribuir | Resolve incerteza | _(preencher)_ |
| Google | F | 3 | Indet. | Atribuir | Resolve incerteza | _(preencher)_ |
| Google | R | 1 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Google | R | 2 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |
| Google | R | 3 | Não atribuir | Não atribuir | Confirma | _(preencher)_ |

### Matriz de transição A → B — selo F (LLMs, todas as cadeias)

|  | B: Atribuir | B: Não atribuir | B: Indet. | Total |
|---|---|---|---|---|
| A: Atribuir | 0 | 0 | 0 | 0 |
| A: Não atribuir | 0 | 6 | 0 | 6 |
| A: Indet. | 3 | 0 | 0 | 3 |

### Matriz de transição A → B — selo R (LLMs, todas as cadeias)

|  | B: Atribuir | B: Não atribuir | B: Indet. | Total |
|---|---|---|---|---|
| A: Atribuir | 0 | 0 | 0 | 0 |
| A: Não atribuir | 0 | 9 | 0 | 9 |
| A: Indet. | 0 | 0 | 0 | 0 |

### Relações por LLM

| LLM | Selo | Confirma | Contradiz | Resolve incerteza | Introduz incerteza |
|---|---|---|---|---|---|
| OpenAI | F | 3 | 0 | 0 | 0 |
| OpenAI | R | 3 | 0 | 0 | 0 |
| Anthropic | F | 3 | 0 | 0 | 0 |
| Anthropic | R | 3 | 0 | 0 | 0 |
| Google | F | 0 | 0 | 3 | 0 |
| Google | R | 3 | 0 | 0 | 0 |

## 6. Calibração

Confiança média (0–100) quando a decisão coincide com o oficial versus quando não coincide. Brier = média de (confiança/100 − 1[oficial atribuiu])², lendo a confiança como a probabilidade de o comitê ter atribuído o selo (Prompt A, item 5); menor é melhor.

| LLM | Etapa | Coincide | Não coincide (total) | …decisão firme oposta | …Indeterminado | Brier | Sem confiança |
|---|---|---|---|---|---|---|---|
| OpenAI | A | n.d. | 7.8 (n=6) | 7.8 (n=6) | n.d. | 0.851 | 0 |
| OpenAI | B | n.d. | 10.0 (n=6) | 10.0 (n=6) | n.d. | 0.818 | 0 |
| Anthropic | A | n.d. | 35.0 (n=6) | 35.0 (n=6) | n.d. | 0.458 | 0 |
| Anthropic | B | n.d. | 37.5 (n=6) | 37.5 (n=6) | n.d. | 0.467 | 0 |
| Google | A | n.d. | 49.7 (n=6) | 13.3 (n=3) | 86.0 (n=3) | 0.386 | 0 |
| Google | B | 95.0 (n=3) | 36.0 (n=3) | 36.0 (n=3) | n.d. | 0.302 | 0 |

## 7. Linha de base humana

**Nenhuma decisão humana em decisoes.csv** (arquivos `humano/` ausentes ou com pendência de extração). A comparação abaixo fica n.d.

| Etapa | Selo | Humano | Coincide com oficial | vs. modal OpenAI | vs. modal Anthropic | vs. modal Google |
|---|---|---|---|---|---|---|
| Analítica (A) | F | **ausente** | n.d. | n.d. | n.d. | n.d. |
| Analítica (A) | R | **ausente** | n.d. | n.d. | n.d. | n.d. |
| Após execução (B) | F | **ausente** | n.d. | n.d. | n.d. | n.d. |
| Após execução (B) | R | **ausente** | n.d. | n.d. | n.d. | n.d. |

## 8. Precisão das evidências

Provedores revelados com a chave de cegamento informada em `--chave`.

| LLM | Citadas | Correta | Mal interpretada | Inexistente | Não verificável | Sem classe | Precisão (corretas/citadas) |
|---|---|---|---|---|---|---|---|
| OpenAI | 67 | 67 | 0 | 0 | 0 | 0 | 67/67 (100%) |
| Anthropic | 170 | 167 | 3 | 0 | 0 | 0 | 167/170 (98%) |
| Google | 85 | 84 | 1 | 0 | 0 | 0 | 84/85 (99%) |
