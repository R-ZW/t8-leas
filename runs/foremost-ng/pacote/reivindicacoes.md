# Reivindicações pré-definidas — Foremost-NG (SBSeg 2025)

**Versão do código:** proxy [`bb812a22cb06ef87b5a2d877dfb6f40eb12d460d`](https://github.com/cristianzsh/foremost-ng/commit/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d), 08/07/2025. **Escopo:** descrição documental para avaliação futura; nenhum resultado abaixo foi produzido nesta T8. Fonte do artigo: `artigo.pdf`, cópia prevista de `fontes/foremost-ng.pdf` (numeração impressa e física de 1 a 8 coincidem). Fonte do código: [README desse SHA](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md). Critério externo: [instruções de revisão do SBSeg 2025](https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html), seções F e R. Os critérios abaixo operacionalizam observações; não são resultados nem promessas dos autores além do que as fontes dizem.

**Regra congelada de seleção para R:** C1–C5 são as cinco inovações funcionais centrais enunciadas no resumo e nas seções 1–3; C6 é a única execução ilustrada como resultado (Fig. 2). São as **principais**, independentemente de dados ou chaves estarem disponíveis. C7 é arquitetura/extensibilidade descrita, verificável por inspeção estrutural, sem experimento de extensão definido; não entra no núcleo operacional de R. A ausência de procedimento/entrada não remove uma reivindicação principal nem autoriza substituí-la. Um teste externo de carving é complementar para F, nunca reprodução de C6.

## C1 — Recuperação de EVTX

- **Classe / R:** contribuição descrita; principal para R; **sem experimento completo no README**.
- **Afirmação:** o parser reconhece `ElfFile`, delimita chunks EVTX de 64 KiB e extrai um log que pode ser analisado por ferramentas de eventos.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2 (introdução), p. 6, §3, item “Windows Event Logs (EVTX)”; p. 7, §4.1 (exemplo `-t evtx,elf,exe`).
- **Procedimento dos autores no SHA:** [README, “Installation” e “Usage”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L21-L85): compilar em `src/` no Linux com `make` e `sudo make install`; sintaxe genérica `foremost-ng [options] [image_or_device]`. O README não dá comando, imagem nem parâmetros específicos para EVTX; o comando de filtragem está **somente no artigo**. Procedimento específico **indisponível**.
- **Entrada exigida:** imagem identificada contendo EVTX íntegro e gabarito do arquivo/offset; **indisponíveis nas fontes**.
- **Resultado observável:** arquivo `.evtx` recuperado, localização/offset no registro e abertura por parser de eventos.
- **Critério de sucesso pré-fixado:** com entrada e gabarito conhecidos, recuperar o EVTX no offset previsto, com estrutura parseável e conteúdo comparável ao original; mera extensão ou contagem não basta.
- **Limitação:** sem imagem e gabarito dos autores, um arquivo externo demonstra capacidade em teste complementar, mas não reproduz o resultado do artigo; resultado hoje **inconclusivo**.
- **Fontes:** artigo pp. 1–2, 6–7; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md); [regra oficial R](https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html).

## C2 — Recuperação de scripts

- **Classe / R:** contribuição descrita; principal para R; **sem experimento completo no README**.
- **Afirmação:** scripts Bash, Python ou PowerShell são reconhecidos por shebang (`#!`) e conteúdo textual; a rotina exige pelo menos 32 bytes e mais que comentários antes de extrair o script.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2 (introdução), p. 6, §3, item “Script Files”; p. 7, §4.1 (carving genérico).
- **Procedimento dos autores no SHA:** [README, “Installation” e “Usage”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L21-L85) dá a compilação e apenas sintaxe genérica. Não fornece arquivo, comando filtrado ou sequência de experimento para scripts; procedimento específico **indisponível**.
- **Entrada exigida:** imagem identificada contendo script(s) com conteúdo original e offsets conhecidos; **indisponível**.
- **Resultado observável:** arquivo `.script`/script extraído com diretiva de intérprete e conteúdo legível; registro da extração.
- **Critério de sucesso pré-fixado:** recuperar os bytes do script esperado no offset correto, preservando diretiva e corpo, e rejeitar fragmentos que não atendem às condições descritas. Teste negativo é complementar, pois os autores não forneceram gabarito.
- **Limitação:** o artigo cita PowerShell e Unicode na introdução, mas §3 descreve o reconhecimento por shebang; não presumir cobertura integral de scripts sem shebang. Sem entrada/gabarito, R fica **inconclusivo**.
- **Fontes:** artigo pp. 1–2, 6–7; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md).

## C3 — Recuperação de Mach-O

- **Classe / R:** contribuição descrita; principal para R; **sem experimento completo no README**.
- **Afirmação:** binários Mach-O `fat` ou `thin` são reconhecidos e extraídos usando cabeçalho universal ou comandos de carga para determinar a extensão do arquivo.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2 (introdução), p. 6, §3, item “Mach-O (macOS/iOS Binaries)”; p. 7, §4.1 (carving genérico).
- **Procedimento dos autores no SHA:** [README, “Installation” e “Usage”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L21-L85) documenta compilação e sintaxe genérica, sem receita Mach-O. Procedimento específico **indisponível**.
- **Entrada exigida:** imagem identificada com binário(s) Mach-O `fat`/`thin`, tamanho e conteúdo de referência; **indisponível**.
- **Resultado observável:** binário Mach-O recuperado e reconhecível por ferramenta apropriada, com offset/arquivo registrado.
- **Critério de sucesso pré-fixado:** para a entrada conhecida, recuperar o Mach-O esperado com arquitetura(s) e segmentos estruturais preservados e comparar bytes/tamanho ao gabarito; não inferir suporte a todas as variantes a partir de um caso.
- **Limitação:** o artigo não fornece imagem, caso `fat`/`thin` reproduzível nem resultado numérico; R específico **inconclusivo** sem insumos.
- **Fontes:** artigo pp. 1–2, 6–7; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md).

## C4 — Recuperação de ELF

- **Classe / R:** contribuição descrita; principal para R; **sem experimento completo no README**.
- **Afirmação:** o parser identifica ELF 32/64 bits, usa cabeçalhos de programa para delimitar segmentos carregáveis e extrai o executável para análise posterior.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), p. 2 (introdução), p. 6, §3, item “ELF”; p. 7, §4.1 (exemplos com `-t evtx,elf,exe` e `-x -t elf`).
- **Procedimento dos autores no SHA:** [README, “Installation” e “Usage”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L21-L85) cobre build Linux e sintaxe genérica; comandos exemplares com `elf` aparecem no artigo, **não** como experimento completo no README.
- **Entrada exigida:** imagem ou dump contendo ELF conhecido (incluindo tipo 32/64 e offset) e gabarito; **indisponível**.
- **Resultado observável:** arquivo `.elf` e offset no registro; estrutura ELF legível por analisador apropriado.
- **Critério de sucesso pré-fixado:** com entrada identificada, obter ELF parseável com segmentos e tamanho coerentes com o original; verificar conteúdo/bytes contra gabarito quando houver. Somente encontrar assinatura ELF não basta.
- **Limitação:** `memory.dump` e `disk.img` do artigo são exemplos, não datasets fornecidos; a Figura 2 mostra três linhas ELF, mas falta `evidence2.dd` para cotejo. Reprodução específica **indisponível**.
- **Fontes:** artigo pp. 1–2, 6–8; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md).

## C5 — Enriquecimento pelo VirusTotal

- **Classe / R:** contribuição descrita; principal para R; procedimento parcial e insumo privado **indisponível**.
- **Afirmação:** com `-x` e `VT_API_KEY`, o programa consulta a API VirusTotal pelo hash do arquivo recuperado e registra contagens/veredito de detecção.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), pp. 2–3, §2 (fluxo da API), p. 7, §4 e §4.1 (variável e exemplo `foremost-ng -x -t elf -i memory.dump -o ./carved-files`), p. 8, Fig. 2 (coluna VT).
- **Procedimento dos autores no SHA:** [README, “VirusTotal API”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L89-L109) instrui obter chave, definir `VT_API_KEY` e usar `-x`; [“Usage”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L74-L85) é genérico. O exemplo `memory.dump` está no artigo, não é arquivo fornecido.
- **Entrada exigida:** arquivo recuperável conhecido, ambiente com acesso à API e chave válida **não fornecida**; não registrar chave no pacote/log.
- **Resultado observável:** consulta efetiva e veredito/contagens associados ao arquivo extraído; na falta da chave, aviso e carving sem consulta, como descreve o artigo p. 7.
- **Critério de sucesso pré-fixado:** registrar evidência de consulta válida e associação do resultado ao hash do arquivo, com segredo ocultado; ausência de erro de rede/chave. Valores de detecção podem mudar e não são gabarito estático.
- **Limitação:** falta chave e entrada identificada; não há resposta da API congelada. Sem isso, teste de VT **bloqueado**, mesmo que carving funcione.
- **Fontes:** artigo pp. 1–3, 7–8; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md).

## C6 — Execução da Figura 2 com `evidence2.dd`

- **Classe / R:** demonstração ilustrada no artigo, **não** experimento detalhado no README; principal para R como única saída concreta publicada.
- **Afirmação:** uma execução `./foremost-ng -v -x evidence2.dd` produz a tabela ilustrada, com arquivos ELF, script, EXE e ZIP e coluna VT.
- **Artigo:** `artigo.pdf`, p. 7, §4.2 (“Figure 2 shows an execution example and the expected output”); p. 8, Fig. 2 (captura com comando, arquivo, tamanho e linhas/offsets). A [apresentação do autor, slide 21](https://cristian.sh/files/talks/sbseg2025foremostng.pdf) repete a captura.
- **Procedimento dos autores no SHA:** [README, “Usage” e “VirusTotal API”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L74-L109) só fornece sintaxe geral e configuração da chave. O comando acima é legível na **captura do artigo**, não é roteiro completo do README. Receita de obtenção/preparo de `evidence2.dd` **indisponível**.
- **Entrada exigida:** `evidence2.dd` identificado por origem e hash, chave VT válida para reproduzir essa coluna, dependências e ambiente; imagem e chave **não fornecidas**. A captura informa 2.845.109.643 bytes, mas tamanho sozinho não autentica o conteúdo.
- **Resultado observável:** log/tabela de carving com nomes, formatos e offsets comparáveis à figura; status VT variável no tempo.
- **Critério de sucesso pré-fixado:** somente com a **mesma imagem autenticada**, confrontar linhas e offsets estáveis da captura; registrar divergências. Não exigir contagens VirusTotal idênticas, pois são externas e temporais.
- **Limitação:** a [árvore completa do SHA](https://api.github.com/repos/cristianzsh/foremost-ng/git/trees/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d?recursive=1) não contém a imagem; artigo/README não dão URL ou SHA-256. A reprodução literal está **indisponível**. O [DFTT](https://dftt.sourceforge.net/) é referido genericamente no artigo p. 7, mas uma de suas imagens não pode ser tratada como `evidence2.dd`.
- **Fontes:** artigo pp. 7–8; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md); [árvore do SHA](https://api.github.com/repos/cristianzsh/foremost-ng/git/trees/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d?recursive=1); [apresentação](https://cristian.sh/files/talks/sbseg2025foremostng.pdf).

## C7 — Arquitetura de parsers extensível

- **Classe / R:** contribuição arquitetural descrita; **não principal para R operacional**, porque não há experimento de adição de parser.
- **Afirmação:** um despachante central e parsers com identificador, assinatura, validação e recuperação permitem ampliar formatos sem alterar o núcleo.
- **Artigo:** `artigo.pdf`, p. 1 (resumo), pp. 2–3, §2 e Fig. 1; p. 8, §5.
- **Procedimento dos autores no SHA:** [README, “Features”](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md#L11-L19) lista assinaturas configuráveis, mas não fornece tutorial, parser de exemplo ou teste de extensibilidade. Procedimento experimental **indisponível**.
- **Entrada exigida:** fonte do SHA e especificação de um novo formato/fixture, ausente como experimento dos autores.
- **Resultado observável:** organização e registro de módulos por inspeção; eventual novo parser funcional seria um teste complementar criado pelo executor.
- **Critério de sucesso pré-fixado:** verificar correspondência estrutural entre componentes do código e Fig. 1; não inferir facilidade de extensão nem ausência de regressões apenas da organização.
- **Limitação:** análise estática não prova o desempenho ou a facilidade de adicionar um formato; sem procedimento autoral, nenhuma reprodução experimental desta contribuição.
- **Fontes:** artigo pp. 1–3, 8; [README fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md).

## Teste complementar separado

**T-FN-01 (não integra C6 nem substitui R):** se a execução de referência precisar de um teste mínimo funcional, pode-se usar uma imagem externa identificada, por exemplo uma amostra do DFTT citada no artigo p. 7, preservando URL, versão, hash e gabarito próprio. O resultado só demonstra o comportamento naquela entrada. Será rotulado como desvio **D3 (teste externo)** no registro de execução; não se renomeará a imagem como `evidence2.dd` nem se comparará sua saída à Fig. 2.
