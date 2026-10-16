# Registro de mudanças anteriores ao primeiro Prompt A

As mudanças abaixo ocorreram **antes de qualquer conversa avaliadora**. Ainda não havia cadeia aberta, como mostra a [folha de controle](controle-conversas.md). Os dois pré-registros permitem edição até o primeiro Prompt A. Depois dele, toda mudança vira desvio em `<artefato>/desvios/DV-NNN.md`.

## M-001 — 15/10/2026: `reivindicacoes.md` reescrito sem juízos (v1 → v2)

**Motivo.** A v1 é anexada às LLMs no Prompt A e trazia, junto das reivindicações, avaliações do próprio grupo. Exemplos: "procedimento específico **indisponível**", "R específico **inconclusivo** sem insumos", "teste de VT **bloqueado**", "reprodução literal **indisponível**". Foram 16 ocorrências no Foremost-NG e 7 no Mininet-GUI. Esse conteúdo antecipa a conclusão e empurra as LLMs para "Não atribuir" ou "Indeterminado" em R. É o mesmo tipo de viés de instrumento que a [avaliação crítica da T7](https://diegokreutz.github.io/leas_2026_2/tarefa_7/avaliacao_critica.html) aponta no Prompt 3 (§4.2). O §4.4 do protocolo pede só: ID, reivindicação, onde está no artigo, resultado esperado, se o README indica como reproduzir (sim, parcial, não) e a regra para R.

**O que mudou na lista entregue às LLMs (`pacote/reivindicacoes.md`, v2):**
- tabela única no formato do §4.4, com as mesmas reivindicações e os mesmos IDs (Foremost-NG C1–C7; Mininet-GUI C1–C6);
- regra de R inalterada (Foremost-NG: C1–C6; Mininet-GUI: C4 e C5), redigida conforme o modelo do protocolo e sem justificativa ligada à disponibilidade de insumos;
- critério de reprodução: comportamento esperado observado. Nenhuma reivindicação tem tolerância numérica declarada pelos autores. No Foremost-NG, as contagens do VirusTotal não precisam coincidir;
- removidos: classe e limitações, "entrada exigida", critérios de sucesso pré-fixados, links externos para o GitHub e o resumo da situação documental.

**O que foi preservado.** A v1 ficou sem alteração em `<artefato>/criterios-observacao.md`, com uma nota no topo. Ela continua valendo como critério de observação na execução de referência e na análise, e **nunca é anexada às LLMs**. Ela também está no histórico do Git (commit `b7c7410`).

| Artefato | v1 (SHA-256) | v2 (SHA-256) |
| --- | --- | --- |
| Foremost-NG | `06405b993ebc1fda61263c91ec549fd250485898dfad5e3f1200cf956ca3faf8` | `3d27bc26b64ae7c16272dc9d7a68c25ccacf98d82dbfcdc5bfd7d3ab7932dbac` |
| Mininet-GUI | `3b118245e897fb20a3bd55047bb18d13fa9285fbe7a9a41964fa28954c6b31a7` | `100366e5dfad9c560f9d5066e67d1e23df8f6ad7c3d5ce2e62aff02a529ed0bc` |

**Arquivos atualizados junto:** `pacote/MANIFESTO.sha256`; `CONGELAMENTO.sha256`, que agora congela a v2 e o pré-registro; a linha 3 de cada `preregistro.md`, que aponta a v2 e este registro (no Mininet-GUI, também a nota do item "Fontes e separação de papéis"); a tabela de hashes em [auditoria-pacotes.md](auditoria-pacotes.md) e em [GUIA-CONVERSAS.md](GUIA-CONVERSAS.md).

**Limitação que permanece.** A coluna "O README indica como reproduzir?" é uma classificação humana (sim, parcial, não), exigida pelo protocolo. Ela foi limitada a apontar a seção do README, sem comentar o resultado esperado.

## M-002 — 15/10/2026: `artefato.zip` → `artefato.txt` e fins de linha

Descrita no adendo de [auditoria-pacotes.md](auditoria-pacotes.md) e em `<artefato>/pacote/prompts/LEIA-ME.md`.
