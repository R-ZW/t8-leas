# Decisões operacionais — 15/10/2026

O aluno Eduardo Prates Tiadoro delegou estas decisões e a condução operacional ao agente Claude Code (Opus 5.5) que orquestra a T8. Tudo foi registrado antes de qualquer Prompt A. O relatório final precisa declarar quem fez cada parte.

| Tema | Decisão | Motivo |
| --- | --- | --- |
| Conversas avaliadoras | Cada integrante roda o seu provedor no **app desktop** (Eduardo no Claude, colegas no ChatGPT e no Gemini), seguindo [GUIA-CONVERSAS.md](GUIA-CONVERSAS.md). O agente orquestrador **não** conduz conversas avaliadoras. | O §4.6 pede a mesma interface de chat com anexos. O agente tem contexto de planejamento, que o protocolo veda às LLMs avaliadoras, e não tem acesso aos apps. |
| Execução de referência (§6.3) | Feita por **agentes Claude Code** com autorização e supervisão do aluno, em sessões separadas das conversas avaliadoras. O registro factual é único e idêntico para as nove cadeias de cada artefato. | O aluno autorizou que a execução do agente conte como a dele. Isso é um **desvio declarado** do texto "execução pelo aluno". O executor não emite juízo sobre os selos, e as três LLMs recebem o mesmo registro, de modo que o executor não é confundido com o provedor (problema 4.1 da avaliação crítica). Ameaça residual: o executor é da mesma família de modelos de um dos avaliadores (Anthropic). |
| Ambiente Foremost-NG | Contêiner Ubuntu limpo (Docker Desktop/WSL2), com dependências do README e imagem base com digest registrado. | §12: rodar em Linux, não em Windows/MSYS2 como na T7. |
| Ambiente Mininet-GUI | **VM dos autores** (release `v0.0.1`, "VM SBRC 2025") no VirtualBox 7.1.6, com 8 GB de RAM. Docker foi descartado como substituto. | §12 e avaliação crítica §4.5: um ambiente fora dos requisitos não gera evidência sobre o artefato. |
| Linha de base humana (§3) | **Não é delegável.** O agente não preenche `humano/` em nome do aluno, porque isso produziria um quarto julgamento de LLM rotulado como humano. Se o aluno não preencher `humano/decisao-analitica.md` antes de abrir respostas de LLM, a linha de base é declarada **ausente** no relatório. | Integridade dos dados. A linha de base é recomendada pelo protocolo, mas não é item obrigatório da tarefa. |
| Mensagem aos autores (§4.5) | O rascunho fica em `foremost-ng/execucao/mensagem-autores.md`. O envio fica com o aluno, pela conta dele. | Comunicação externa em nome do aluno. |

## Adendo — 17/10/2026

| Tema | Decisão | Motivo |
| --- | --- | --- |
| Interfaces efetivamente usadas | Claude no claude.ai (web, chat); GPT no **Codex** (agente com terminal); Gemini no **Antigravity** (subagente isolado só de leitura). As três ficam como estão, com o desvio declarado. Esforço: Claude Médio; GPT e Gemini High. | Decisão do grupo em 17/10/2026. Conferiu-se nas transcrições que nenhum dos três leu arquivos fora de `pacote/` nem executou o artefato. Resta a ameaça da avaliação crítica §4.4 (produto + modelo), que deve constar no relatório. |
| Transparência do executor | O agente que opera a execução de referência também operou as conversas do Claude e, ao testar o extrator, viu decisões da etapa A e a coluna `oficial` (selos oficiais). As sessões de execução recebem a instrução de ler só os roteiros B1, nunca as respostas A nem `referencia/`. | O registro factual é só de fatos e é idêntico para as três LLMs, mas a exposição prévia deve ser declarada. |
| Ordem da consolidação | O roteiro consolidado usa os B1 da cadeia 1 de cada provedor (§6.2). Os B1 das cadeias 2 e 3 são consultados só para achar passo essencial ausente (§6.5). | Protocolo. |

## Adendo — 18/10/2026

| Tema | Decisão | Motivo |
| --- | --- | --- |
| B2 do GPT | **Aceito como está e classificado como NÃO COMPARÁVEL.** As 6 respostas B2 do GPT foram geradas em conversas **novas** do Codex, em outro workspace (`D:\user\unipampa\8º Semestre\LEAS\atividades\t8`), com o contexto "restaurado" a partir dos exports escritos pelo próprio modelo, e não na mesma conversa de A/B1 (§3 e §6.4 do protocolo). Nesse workspace o repositório inteiro estava acessível: FN-1 e MG-1 leram `referencia/instrucoes-oficiais.md`, e FN-3 e MG-3 leram evidências brutas da execução e o roteiro consolidado, material que Claude e Gemini não receberam; FN-3 e MG-3 também listaram os arquivos do repositório. Não se encontrou leitura de `selos-oficiais` nem das respostas de outros provedores. O texto vem do Session Exporter (não literal; as novas conversas não têm link de compartilhamento) e foi extraído por `ferramentas/extrair_b2_session_export.py`. | Reinaldo informou que não consegue refazer o B2 nas conversas originais; decisão do aluno em 18/10/2026. Na análise, as decisões B do GPT entram só de forma descritiva e ficam **fora** do critério de consistência A→B, da matriz de transição e da concordância entre LLMs na etapa B. As métricas são calculadas com e sem elas. |
| Verificação cega (§7) | O cegamento é feito por `ferramentas/cegar.py`, com a chave fora do repositório (`~/t8-leas-chaves/`). A classificação das evidências é feita por sessões de agente que não leem a chave nem as pastas `llm-*`: só `verificacao-cega/`, o pacote e o registro factual. | Não há colega disponível para o cegamento manual; desvio declarado. Pistas de estilo (marcações do Codex, documentos do Claude Docs) podem permitir identificar o provedor apesar da troca de nomes. |

| Linha de base humana (18/10) | **Não preenchida**, declarada ausente. | As avaliações dos modelos já haviam sido abertas e o aluno não emitiu parecer prévio às cegas (§3); preenchida agora, ela não seria cega. Decisão do aluno em 18/10/2026. |
