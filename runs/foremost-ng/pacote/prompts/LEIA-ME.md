# Prompts da coleta

Gerados por `ferramentas/gerar_prompts.py` a partir do texto dos §5 e §6.4 do protocolo. Copie e cole **sem alterar nada**.

| Arquivo | Quando | Anexos |
| --- | --- | --- |
| `prompt-A.txt` | primeira mensagem de uma conversa nova | `artigo.pdf`, `artefato.txt`, `instrucoes-oficiais.md`, `reivindicacoes.md` |
| `prompt-B1.txt` | logo após a resposta de A, na mesma conversa | nenhum |
| `prompt-B2-modelo.txt` | depois do registro factual congelado, na mesma conversa | `execucao/registro-factual.md` |

Adaptações deliberadas em relação ao texto do protocolo, iguais para as três LLMs e decididas antes de qualquer Prompt A:

1. `artefato.zip` foi trocado por `artefato.txt`, uma apresentação em arquivo único gerada por `ferramentas/achatar_artefato.py`. O app do Claude não aceita ZIP e o Gemini lê no máximo dez arquivos por ZIP, e o §4.6 manda entregar a mesma extração às três. O arquivo contém todos os arquivos de texto do commit com número de linha. Binários (imagens, DLLs, `.gz`, `.ico`) aparecem só no índice, com hash.
2. "Não navegue na web" foi ampliado para "nem consulte memória, outras conversas, projetos ou conectores", conforme o `llms.md` de cada artefato.
3. `{CONDICAO}` do B2 é preenchido uma única vez ("atende" ou "não atende, porque ..."), depois da execução, e fica idêntico nas nove cadeias do artefato.
