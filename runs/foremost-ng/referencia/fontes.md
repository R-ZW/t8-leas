# Fontes consultadas — Foremost-NG

**Consulta:** 15/10/2026 (America/Sao_Paulo). **Escopo:** Foremost-NG, Salão de Ferramentas do SBSeg 2025. Este inventário reúne evidências documentais; nenhuma execução do software foi feita nesta etapa.

| Fonte e localização | Finalidade | Fatos confirmados na fonte | Lacunas ou ressalvas |
|---|---|---|---|
| Protocolo local: `../../../../novo_protocolo.md` | Fixar escopo e fluxo da T8 | Dois artefatos; avaliação separada de F/R; selos em referência, fora dos pacotes das LLMs. | Documento do grupo, não é fonte dos critérios oficiais nem evidência de funcionamento. |
| Artigo recebido: `../../../fontes/foremost-ng.pdf` (8 páginas; SHA-256 `42327BC79D2576D64825C7308B37E850D0354E986F3D0C81E40A6D37445546C2`) | Identificar reivindicações e demonstração publicadas em 2025 | O resumo e as seções 2–3 reivindicam arquitetura modular, novos formatos (EVTX, scripts, Mach-O, ELF) e consulta VirusTotal. Seção 4 apresenta instalação/CLI; Fig. 2 mostra uma execução. | O arquivo usado na Fig. 2 (`evidence2.dd`) não veio com o artigo recebido; não há gabarito ou valores numéricos reproduzíveis para essa execução. A chave VirusTotal não foi fornecida. |
| README atual: https://github.com/cristianzsh/foremost-ng#readme | Inspecionar documentação e caminho de instalação do repositório indicado pelo usuário | Repositório público; README descreve Linux, assinatura por cabeçalho/rodapé, uso em imagens/dispositivos, compilação dentro de `src/` com `make` e `sudo make install`, e consulta VirusTotal com `VT_API_KEY`. | É o estado corrente da branch exibida, sem SHA de 2025 fixado. O README não oferece, na seção consultada, um dataset e gabarito para reproduzir a Fig. 2. |
| Árvore `src/`: https://github.com/cristianzsh/foremost-ng/tree/main/src | Inspecionar documentação e organização disponível | A árvore exibe `Makefile`, código C, `foremost.conf` e manual compactado `foremost-ng.8.gz`. | A existência do manual não confirma que seu conteúdo atual corresponda ao artefato avaliado em 2025; o manual compactado não foi inspecionado nesta etapa. |
| Critérios oficiais: https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html | Obter requisitos da edição correta | F requer execução observável e prova/saída no parecer; R requer executar os experimentos das reivindicações principais e resumir resultados. D e S também são definidos. | Registro dos pontos pertinentes em `instrucoes-oficiais.md`; a página original continua sendo a referência integral. |
| Resultados oficiais: https://doc-artefatos.github.io/sbseg2025/results.html | Fixar comparação posterior | A linha de Foremost-NG na trilha SF mostra imagens dos quatro selos D/F/S/R. | Registro datado em `selos-oficiais.md` e `selos-oficiais.pdf`. Os selos não provam identidade com o README atual. |

## Divergências e pontos a resolver

1. **Diretório de compilação:** a seção 4 do artigo indica `cd foremost-ng` seguido de `make`; o README atual manda entrar em `src/` antes de compilar. Será preciso conferir o Makefile e o README do commit que vier a ser fixado, sem tratar ambos os procedimentos como equivalentes.
2. **Nome do registro de saída no artigo:** a página 6 menciona `audit.txt`, enquanto a página 7 menciona `recovery.log`. É uma inconsistência do próprio artigo; não se deve prometer um nome de arquivo antes de verificar a versão usada.
3. **Escopo técnico temporal:** o artigo detalha suporte a EVTX, scripts, Mach-O e ELF; o README atual descreve o uso geral, sem um procedimento de reprodução e gabarito para cada formato. Isso é lacuna de documentação, não resultado negativo de execução.
4. **Insumos:** a disponibilidade de `evidence2.dd`, uma chave VirusTotal e a versão exata examinada pelo CTA ainda não foi demonstrada. A URL do DFTT citada no artigo é sugestão de amostras para teste, não substitui a entrada/resultado da Fig. 2.

**Próxima etapa documental:** identificar commit/tag de 2025, baixar e registrar o código fixado e conferir README, manual e Makefile daquele SHA. Até lá, todas as afirmações sobre o repositório têm qualificador **README/árvore atuais**.
