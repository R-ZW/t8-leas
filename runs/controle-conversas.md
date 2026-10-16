# Folha de controle — 18 conversas avaliadoras

**Estado inicial: 15/10/2026.** Nenhuma conversa experimental foi aberta. O identificador único é **provedor + ID**: cada provedor tem FN-1…FN-3 e MG-1…MG-3. “Não iniciada” significa que nenhum Prompt A, B1 ou B2 foi enviado. Os caminhos abaixo estão **reservados**, não são exportações existentes.

**Agenda provisória:** A/B1 em 16/10/2026, 10h–18h (America/Sao_Paulo), somente se os dois pacotes C03, hashes, acesso aos anexos e configurações de [Foremost-NG](foremost-ng/llms.md) e [Mininet-GUI](mininet-gui/llms.md) estiverem conferidos. B2 depois da execução comum e do registro factual congelado; registrar nova previsão se houver adiamento. Os colegas responsáveis por Claude e Gemini devem confirmar seu horário real; não presumir que aceitaram a janela.

| Provedor | ID | Artefato | A | B1 | B2 | Exportação integral prevista | Método/horários reais |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GPT / OpenAI | FN-1 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-openai/cadeia-1.md` | — |
| GPT / OpenAI | FN-2 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-openai/cadeia-2.md` | — |
| GPT / OpenAI | FN-3 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-openai/cadeia-3.md` | — |
| GPT / OpenAI | MG-1 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-openai/cadeia-1.md` | — |
| GPT / OpenAI | MG-2 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-openai/cadeia-2.md` | — |
| GPT / OpenAI | MG-3 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-openai/cadeia-3.md` | — |
| Claude / Anthropic | FN-1 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-anthropic/cadeia-1.md` | — |
| Claude / Anthropic | FN-2 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-anthropic/cadeia-2.md` | — |
| Claude / Anthropic | FN-3 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-anthropic/cadeia-3.md` | — |
| Claude / Anthropic | MG-1 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-anthropic/cadeia-1.md` | — |
| Claude / Anthropic | MG-2 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-anthropic/cadeia-2.md` | — |
| Claude / Anthropic | MG-3 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-anthropic/cadeia-3.md` | — |
| Gemini / Google | FN-1 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-google/cadeia-1.md` | — |
| Gemini / Google | FN-2 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-google/cadeia-2.md` | — |
| Gemini / Google | FN-3 | Foremost-NG | Não iniciada | Não iniciada | Não iniciada | `runs/foremost-ng/llm-google/cadeia-3.md` | — |
| Gemini / Google | MG-1 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-google/cadeia-1.md` | — |
| Gemini / Google | MG-2 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-google/cadeia-2.md` | — |
| Gemini / Google | MG-3 | Mininet-GUI | Não iniciada | Não iniciada | Não iniciada | `runs/mininet-gui/llm-google/cadeia-3.md` | — |

## Como atualizar cada linha

1. Antes de A, preencher em `llms.md` do artefato o nome/versão **mostrados na tela**, interface/plano com anexos, nível de raciocínio visível, navegação, memória/personalização, horário previsto revisado e método de exportação disponível. Conferir que os quatro arquivos de A tenham exatamente os mesmos hashes entre provedores para o mesmo artefato; se ZIP falhar, aplicar a mesma apresentação extraída a todos, documentando-a antes de A. Para B2, conferir o mesmo hash do registro factual nas nove cadeias do artefato.
2. Marcar A, B1 e B2 separadamente como `não iniciada`, `concluída` ou `bloqueada: motivo`, com data/hora real em BRT. Não marcar B2 antes do registro factual. Manter A→B1→B2 **na mesma conversa** e não reutilizar uma conversa entre IDs.
3. Após B2, salvar a transcrição completa no caminho reservado, sem corrigir as respostas. Anotar em “Método/horários reais” se veio de exportação nativa, cópia fiel ou ambos, mais caminho/hash do original e lacunas. Conferir a sequência completa de prompts, respostas, anexos e timestamps. Uma exportação parcial permanece `pendente de conferência`, não `concluída`.
4. Nunca anexar selos oficiais ou respostas de outros provedores. O GPT usa chat com anexos e não executa o artefato dentro da conversa avaliadora. Qualquer ferramenta, busca, incapacidade de ler arquivo ou mudança de modelo durante uma cadeia deve ser registrada como desvio, preservando a evidência.

**Contagem:** 3 provedores × 2 artefatos × 3 conversas = **18** linhas. Os diretórios `llm-*/` contêm somente marcadores de reserva nesta etapa; `cadeia-1.md`, `cadeia-2.md` e `cadeia-3.md` serão criados apenas com conversas reais.
