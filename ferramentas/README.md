# Ferramentas de análise da T8

Python 3, só a biblioteca padrão. Rodar da raiz do repositório; `<artefato>` é `foremost-ng` ou `mininet-gui`. Cada script explica suas regras no cabeçalho.

1. **Extrair decisões** das 9 cadeias e do humano. As transcrições seguem `runs/MODELO-cadeia.md`, com os cabeçalhos `## Prompt A`, `## Resposta A`, `## Prompt B1`, `## Resposta B1`, `## Prompt B2` e `## Resposta B2` escritos exatamente assim.
   ```bash
   python ferramentas/extrair_decisoes.py <artefato>
   ```
   O script grava `analise/decisoes.csv`, `analise/por-reivindicacao.csv` e `analise/pendencias-extracao.md`. Seção ausente, JSON inválido ou decisão fora de Atribuir / Não atribuir / Indeterminado nunca vira linha no CSV. Esses casos aparecem como pendência.
2. **Cegar** para a verificação das evidências (§7). O script sorteia M1/M2/M3, remove nomes de modelo e provedor, cria `verificacao-cega/` e `analise/evidencias.csv` com a coluna `classe` vazia. A chave vai **para fora do repositório** (padrão: `~/t8-leas-chaves/<artefato>-chave.json`).
   ```bash
   python ferramentas/cegar.py <artefato>
   ```
   O verificador preenche `classe` com correta, mal_interpretada, inexistente ou nao_verificavel, sem ver a chave.
3. **Métricas** (§8 e §9). Gera `analise/metricas.md` com moda, estabilidade, cobertura, empates explícitos, a tabela comparativa (as colunas "Causa da divergência" e "Evidência-chave" são preenchidas à mão), o critério pré-registrado, a matriz A→B, a concordância entre LLMs, a calibração, o humano e a precisão das evidências. Passe `--chave` só depois da classificação cega.
   ```bash
   python ferramentas/metricas.py <artefato> --chave ~/t8-leas-chaves/<artefato>-chave.json
   ```

Testes com dados sintéticos e falsos (`testes/fixtures/`, nunca `runs/`):

```bash
python -B -m unittest discover -s ferramentas/testes -v
```
