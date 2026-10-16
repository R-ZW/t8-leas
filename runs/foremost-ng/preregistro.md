# Pré-registro metodológico — Foremost-NG

**Congelamento inicial:** 15/10/2026 (America/Sao_Paulo), **antes de qualquer Prompt A/conversa avaliadora**. Versão 1 da lista: [`pacote/reivindicacoes.md`](pacote/reivindicacoes.md), IDs C1–C7. O arquivo de verificação [`CONGELAMENTO.sha256`](CONGELAMENTO.sha256) será gerado após a redação final deste pré-registro e da lista; não integra o pacote fornecido às LLMs.

## Fontes e separação de papéis

- Artigo recebido `fontes/foremost-ng.pdf` (pp. 1–8), [README no SHA fixado](https://github.com/cristianzsh/foremost-ng/blob/bb812a22cb06ef87b5a2d877dfb6f40eb12d460d/README.md), [instruções oficiais de revisão SBSeg 2025](https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html) e [`versao.md`](versao.md). O SHA é **proxy de 2025**, não versão comprovada do CTA.
- Os critérios oficiais F/R são usados para distinguir funcionamento observado de reprodução das reivindicações principais. **Os selos oficiais arquivados em `referencia/` não foram usados para escolher C1–C7, sua prioridade ou os critérios de sucesso.** Os grafismos de selos já impressos na p. 1 do artigo recebido também não entraram nessa decisão.
- O texto de `reivindicacoes.md` descreve o que deve ser examinado; não contém uma decisão antecipada de atribuir/negar F ou R. Testes/saídas futuros só poderão constar do registro factual de execução.

## Regra de reivindicações principais e unidades de análise

1. **R principal:** C1 EVTX, C2 scripts, C3 Mach-O, C4 ELF, C5 VirusTotal, porque são as adições funcionais enfatizadas no resumo e no corpo; C6 Fig. 2, porque é a única execução com saída mostrada. A regra não depende da disponibilidade posterior de imagem, chave, ambiente ou de resultado obtido.
2. **F/inspeção complementar:** C7 arquitetura de parsers é uma contribuição descrita sem procedimento autoral de extensão; sua inspeção não substitui a execução de F ou de C1–C6. Uma imagem DFTT ou outra amostra externa pode servir a um teste mínimo de carving, marcada **D3** e separada de C6.
3. A unidade de comparação de C1–C4 é **entrada identificada → arquivo recuperado e verificável**, e não apenas contagem de extensões. Para C5, é consulta efetiva vinculada ao hash, sem registrar segredo; respostas do VirusTotal são mutáveis. Para C6, a comparação exige **a mesma `evidence2.dd` autenticada**; tamanho mostrado na figura não a autentica.
4. A situação documental inicial é: o README tem instalação/uso gerais e `-x`, sem seção de experimentos por formato; artigo fornece exemplos de CLI e a Fig. 2, mas não fornece imagem/gabarito por formato nem chave VT. **Disponibilidade não equivale a êxito ou falha de execução.** Registrar “indisponível/bloqueado” para a observação impossível, mantendo a reivindicação no denominador.

## Hipóteses registradas antes da coleta

- **H-FN1:** um teste mínimo de carving com entrada externa identificada poderá gerar evidência de funcionamento observável, mas não evidência de reprodução literal da Fig. 2.
- **H-FN2:** sem `evidence2.dd` autenticada e sua receita, C6 permanecerá sem reprodução verificável, mesmo se outra imagem produzir arquivos dos mesmos tipos.
- **H-FN3:** sem chave VT válida e entrada identificada, não haverá observação direta da consulta C5; um aviso de ausência de chave não é evidência da consulta.
- **H-FN4:** a falta de fixtures/gabaritos autorais limitará a conclusão sobre C1–C4; um caso externo positivo não prova cobertura geral dos quatro formatos.

Estas hipóteses são previsões sobre **observabilidade**, não decisões de selo nem resultados inventados. A avaliação posterior poderá contrariá-las mediante evidência real e citável.

## Procedimento de análise pré-fixado

- **Etapa A:** avaliação documental das sete reivindicações com o mesmo pacote para todas as conversas do artefato, sem execução alegada. Verificar documentação e separar lacuna de procedimento, lacuna de insumo e resultado dependente de execução.
- **Etapa B1/execução:** preservar comandos, diretórios, versão, ambiente Linux, entradas/hashes, saída, código de retorno e tempo. Seguir primeiro o procedimento autoral; rotular desvios D0 (documentado), D1 (ajuste trivial), D2 (contorno não documentado) e D3 (teste externo). Não introduzir resposta simulada de VirusTotal nem chamar DFTT de Fig. 2.
- **Etapa B2:** enviar **o mesmo registro factual** às nove conversas desse artefato e reaplicar C1–C7 e a regra principal acima. F requer observação de funcionamento; R requer execução das reivindicações principais com processo e resultado confrontáveis, conforme [regras do SBSeg 2025](https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html). Falta de ambiente, dado ou chave deve ser registrada como bloqueio, sem convertê-la em falha do software.

## Imutabilidade e desvios

Após o primeiro Prompt A, **não editar nem renumerar** `pacote/reivindicacoes.md` ou este pré-registro. Qualquer erro, fonte nova ou mudança necessária será descrito em `desvios/DV-001.md`, `DV-002.md` etc., com data, motivo, efeito sobre Cn, novo arquivo/hash e indicação das cadeias afetadas. Preservar o original e comunicar o mesmo desvio às nove conversas se a mudança entrar na análise; se isso impedir comparabilidade, reiniciar as cadeias afetadas ou reportar a limitação. Uma atualização do registro factual após B2 segue a mesma lógica de versão, sem apagar as respostas anteriores.
