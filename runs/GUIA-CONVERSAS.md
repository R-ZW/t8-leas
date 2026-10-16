# Guia das conversas avaliadoras (condição principal)

Este guia vale para quem roda uma das três LLMs. Divisão: **Claude/Anthropic** com o Eduardo, **ChatGPT/OpenAI** e **Gemini/Google** com os colegas. Os três usam o **app desktop** do provedor, em chat comum com anexos. Cada pessoa abre **6 conversas**: FN-1, FN-2 e FN-3 (Foremost-NG) e MG-1, MG-2 e MG-3 (Mininet-GUI). A situação de cada uma vai para a [folha de controle](controle-conversas.md).

Quem decide e executa cada parte está em [decisoes-operacionais.md](decisoes-operacionais.md).

Regra de ouro: **as três LLMs recebem exatamente os mesmos bytes e o mesmo texto**. Qualquer diferença vira desvio registrado; ela nunca é corrigida em silêncio.

## 0. Antes de tudo: linha de base humana (Eduardo e, se quiserem, cada colega)

Antes de abrir qualquer resposta de LLM, preencha `<artefato>/humano/decisao-analitica.md` a partir do mesmo pacote. Declare no arquivo o que você já sabia (selos oficiais, resultados da T7). Com esse conhecimento prévio, a linha de base **não é cega**, e o relatório precisa dizer isso.

## 1. Pegar os anexos certos

Use a pasta `<artefato>/pacote/` deste repositório, depois de um `git pull`. O `.gitattributes` mantém os bytes iguais em qualquer sistema operacional. Anexe **estes quatro arquivos**:

| Arquivo | Foremost-NG (SHA-256) | Mininet-GUI (SHA-256) |
| --- | --- | --- |
| `artigo.pdf` | `d9b12aa4…c9e715` | `4e3ff858…2bf08` |
| `artefato.txt` | `6de9ecff…330446` | `5e1da9b3…c83eb` |
| `instrucoes-oficiais.md` | `446e5f94…290a47` | `fc8e01dd…989059` |
| `reivindicacoes.md` | `3d27bc26…32dbac` | `100366e5…9ed0bc` |

Os hashes completos estão em `pacote/MANIFESTO.sha256`. Confira antes da primeira cadeia:

```powershell
certutil -hashfile artefato.txt SHA256
```

**Não anexe** `artefato.zip`, `MANIFESTO.sha256`, a pasta `prompts/`, nada de `referencia/`, `preregistro.md`, `llms.md` nem respostas de outra LLM. O ZIP foi trocado por `artefato.txt` porque o Claude não aceita ZIP e o Gemini lê no máximo 10 arquivos por ZIP (veja `pacote/prompts/LEIA-ME.md`).

## 2. Configurar o app (uma vez, antes da pré-checagem)

Os nomes dos menus mudam com as versões. Registre **o que você viu na tela** em `<artefato>/llms.md` (nome e versão exibidos do modelo, nível de raciocínio, estado de memória e de busca). Se não conseguir desligar algo, registre isso: ausência de botão não significa desligado.

| | Claude (desktop) | ChatGPT (desktop) | Gemini (desktop) |
| --- | --- | --- | --- |
| Memória e histórico | Configurações → desligar a memória e a busca/referência a chats anteriores | Configurações → Personalização: desligar a memória e a referência ao histórico de chats; instruções personalizadas vazias | Configurações: desligar o contexto pessoal, as conversas anteriores e as informações salvas |
| Busca na web | desligar a busca no menu de ferramentas do chat | desligar a busca no menu de ferramentas | registrar se não houver como desligar (o prompt proíbe) |
| Conectores, extensões e apps | todos desligados | todos desligados | apps conectados desligados |
| Projeto | **não** usar projeto; chat avulso | **não** usar projeto nem GPT personalizado | **não** usar Gem |
| Chat temporário | não usar | **não** usar: some antes do B2 | não usar |
| Modelo e raciocínio | o mesmo nas 6 conversas; anotar o nome exato | idem | idem |

Os três precisam usar um nível de raciocínio nominalmente equivalente (por exemplo, o padrão de cada app). Combinem isso antes e anotem.

## 3. Pré-checagem (conversa descartável, fora das cadeias)

Em um chat novo que **não** será uma cadeia, anexe os quatro arquivos de um artefato e envie apenas:

> Sem avaliar nada, responda só: (1) os nomes dos arquivos anexados; (2) quantas linhas começam com "===== INÍCIO DO ARQUIVO" em artefato.txt; (3) a última linha de artefato.txt; (4) o título do artigo.

Respostas esperadas: Foremost-NG **21** arquivos de texto, última linha `===== FIM DO ARQUIVO: src/vt_query.h =====`; Mininet-GUI **42**, última linha `===== FIM DO ARQUIVO: setup.sh =====`. Se a resposta não bater, por exemplo com arquivo truncado, rejeitado ou só parcialmente lido, **pare e avise o grupo**: não comecem as cadeias com leituras diferentes. Anote o resultado em `llms.md` → "Pré-checagem de anexos idênticos". Depois apague essa conversa, se quiser; ela não entra na análise.

## 4. Uma cadeia (repita para FN-1…3 e MG-1…3)

1. Abra **uma conversa nova**.
2. Anexe os 4 arquivos do artefato, cole o conteúdo de `pacote/prompts/prompt-A.txt` **sem mudar nada** e envie. Anote data e hora (BRT).
3. Quando a resposta terminar, cole `pacote/prompts/prompt-B1.txt` na **mesma conversa** e envie. Anote a hora.
4. Não envie mais nada, com duas exceções, sempre com estas frases exatas (e registre como desvio):
   - se a resposta parar no meio: `Continue exatamente de onde parou.`
   - se a LLM fizer uma pergunta: `Prossiga apenas com o material anexado, registrando como evidência ausente o que faltar.`
5. **Não feche nem apague a conversa**: o B2 será enviado nela mesma, dias depois.
6. Exporte já o que houver (seção 5) e marque A e B1 na folha de controle.

Não leia as respostas de outro provedor antes de concluir as suas 6 cadeias A/B1. Não comente o estudo dentro das conversas.

## 5. Exportar a cadeia

Crie `<artefato>/llm-<openai|anthropic|google>/cadeia-<N>.md` a partir de [MODELO-cadeia.md](MODELO-cadeia.md). Cole cada prompt e cada resposta **na íntegra**, usando o botão de copiar da própria mensagem, sem corrigir nada. Os cabeçalhos `## Prompt A`, `## Resposta A`… precisam ficar exatamente como no modelo, porque o script de análise depende deles. Se o app oferecer exportação nativa (exportação de dados da conta), guarde o arquivo bruto em `llm-<provedor>/exportacao-bruta/` e anote o caminho. Uma exportação parcial fica `pendente de conferência`.

## 6. B2 (depois da execução)

O B2 só começa quando `<artefato>/execucao/registro-factual.md` estiver congelado e o hash estiver anotado na folha. Nas **nove** cadeias do artefato: anexe esse mesmo arquivo, cole `prompt-B2-modelo.txt` com `{CONDICAO}` já preenchido pelo grupo (texto idêntico para todos), envie e exporte a resposta em `## Prompt B2` e `## Resposta B2`.
