# Auditoria dos pacotes de entrada — 15/10/2026

Os dois diretórios `pacote/` agora contêm os quatro anexos de A e `MANIFESTO.sha256` para conferência local. O manifesto **não é anexo de A** na apresentação padrão. Nenhuma conversa avaliadora foi aberta, portanto aceitação e leitura dos ZIPs nas três interfaces ainda não foram confirmadas.

| Artefato | SHA de referência (proxy de 2025) | Páginas do artigo | Entradas no ZIP | Verificação |
| --- | --- | ---: | ---: | --- |
| Foremost-NG | `bb812a22cb06ef87b5a2d877dfb6f40eb12d460d` | 8 | 44 | ZIP abre sem erro CRC; comentário do arquivo ZIP contém o SHA completo |
| Mininet-GUI | `465648a4425a4457af0348ab951cf7f71d37a86f` | 9 | 52 | ZIP abre sem erro CRC; comentário do arquivo ZIP contém o SHA completo |

## Proveniência e remoção dos selos das capas

- Os artigos originais permanecem em `fontes/`. Na primeira página de cada original havia quatro **imagens** de selos oficiais. Para não revelar a resposta às LLMs, em `pacote/artigo.pdf` cada imagem foi substituída por uma imagem branca no mesmo lugar. Nenhuma outra página foi alterada intencionalmente.
- A conferência automática encontrou **mesmo número de páginas e mesmo texto extraível em todas as páginas** entre cada original e sua cópia para avaliação. A primeira página de cada cópia foi renderizada e inspecionada visualmente: os quatro selos sumiram e título, autores, resumo e começo do texto continuam legíveis. As cópias são derivadas; seus hashes diferem necessariamente dos originais.
- SHA-256 dos originais: Foremost-NG `42327bc79d2576d64825c7308b37e850d0354e986f3d0c81e40a6d37445546c2`; Mininet-GUI `63949faaec7bc9e3f88fe2338c8f0b93d42dea7a09852076372202d313d5e463`.
- Os ZIPs foram gerados por `git archive` dos commits integrais registrados em `versao.md`, com prefixo de diretório que identifica o artefato e o início do SHA. Nenhum checkout atual foi confundido com o proxy. A OVA do Mininet-GUI e `evidence2.dd` do Foremost-NG **não** fazem parte desses arquivos e continuam sujeitos às limitações em `versao.md`.
- `instrucoes-oficiais.md` de cada pacote resume apenas os critérios F/R da **edição correta**, com URL de proveniência; não traz a página de resultados. Os arquivos em `referencia/` continuam fora dos pacotes.

## Hashes dos quatro anexos de A

Os valores abaixo também constam em cada `pacote/MANIFESTO.sha256`. Um provedor só entra na comparação principal se receber os mesmos bytes do pacote do seu artefato.

| Artefato | Arquivo | SHA-256 |
| --- | --- | --- |
| Foremost-NG | `artigo.pdf` | `d9b12aa44caeab3d8374fd9ad092c3b9ecec1f18d589125f0ca2f8d00dc9e715` |
| Foremost-NG | `artefato.zip` | `955c770e29893527f789e11afc28dcc6b83d7af4a64f14b416e39f554b388e0a` |
| Foremost-NG | `instrucoes-oficiais.md` | `446e5f94605b2fe60ac9c4028f7be57b0488bc79c3c8ef2ef782428f8e290a47` |
| Foremost-NG | `reivindicacoes.md` | `06405b993ebc1fda61263c91ec549fd250485898dfad5e3f1200cf956ca3faf8` |
| Mininet-GUI | `artigo.pdf` | `4e3ff858506f2f9e6da30af4412caa402890ac154b910df390b74e2ee2a2bf08` |
| Mininet-GUI | `artefato.zip` | `e766231891c8441d21dd44208d1ee34f677a51f2dbcfb57651f88586df34d91c` |
| Mininet-GUI | `instrucoes-oficiais.md` | `fc8e01dd0ffdbff06af86a07bd44662c3394903c0d3a6be0222e678963989059` |
| Mininet-GUI | `reivindicacoes.md` | `3b118245e897fb20a3bd55047bb18d13fa9285fbe7a9a41964fa28954c6b31a7` |

**Pendência de interface:** a [documentação do Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude) não inclui ZIP entre os formatos de anexo documentados, e a [do Gemini](https://support.google.com/gemini/answer/14903178?hl=en-gw) informa limite de **dez arquivos internos por ZIP**, inferior às 44/52 entradas destes arquivos. Assim, os pacotes estão completos no disco, mas **A ainda não está liberado**. Antes do primeiro A, os três integrantes precisam confirmar em chats de preparação sem avaliação o que cada interface consegue ler. Se alguma não conseguir ler integralmente, congelar uma apresentação alternativa **idêntica** para os três provedores daquele artefato, registrar novos hashes/desvio e adaptar o nome do anexo no Prompt A de forma igual para todos. Não enviar pacotes desiguais.
