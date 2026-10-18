# Notas da verificação cega das evidências — Foremost-NG (§7)

Verificação de 322 evidências de `evidencias.csv`, feita sem a chave de cegamento. As fontes foram só as permitidas: as respostas cegas `verificacao-cega/M*/cadeia-*.md` e o pacote (`artefato.txt`, `artigo.pdf`, `instrucoes-oficiais.md`, `reivindicacoes.md`). As citações da etapa B foram conferidas no `execucao/registro-factual.md`. A Fig. 2 do artigo (p. 8) é imagem; ela foi extraída do PDF e conferida visualmente.

## Contagens

| M | Citadas | correta | mal_interpretada | inexistente | nao_verificavel |
|---|---|---|---|---|---|
| M1 | 170 | 167 | 3 | 0 | 0 |
| M2 | 85 | 84 | 1 | 0 | 0 |
| M3 | 67 | 67 | 0 | 0 | 0 |
| Total | 322 | 318 | 4 | 0 | 0 |

## Critérios aplicados

1. **O que a classe mede.** A classe mede a fidelidade do conteúdo que a resposta atribui ao local citado: o local existe e diz o que a resposta afirma que ele diz? O acerto do juízo sobre o critério (por exemplo, "dependências: atendido") fica de fora. Esse juízo é medido pelas decisões. Exemplo: uma resposta descreve corretamente o README (curl no BSD, openssl@3 no macOS, sintaxe genérica) e conclui "atendido na documentação". A citação é `correta`, porque o README contém o que ela descreve.
2. **Afirmação funcional desmentida pelo próprio trecho → `mal_interpretada`.** Vale quando a resposta afirma que o código faz algo e a leitura do trecho citado mostra que ele não faz.
3. **Faixa que sustenta várias afirmações.** Se uma delas for desmentida pelo próprio trecho, a linha é `mal_interpretada`, e a nota registra a parte correta.
4. **Descrição literal de código.** Uma descrição literal do código que não afirma o efeito foi tratada como `correta`, mesmo quando o ramo descrito é inalcançável. Exemplo: "o ramo thin percorre os comandos de carga", sem dizer que o thin é extraído. A nota registra o defeito.
5. **Seções citadas por nome.** "Funcional (F)", "Regra para o selo R", "Critério de reprodução", "ÍNDICE", "Conteúdo", "seção 4", "§3/C2", "§4/Insumos ausentes" etc. foram aceitas porque existem com esse título nos arquivos. "tabela C6" e "reivindicacoes.md:tabela" apontam para uma linha identificável da única tabela do arquivo.
6. **Passos do registro.** Passos citados por ID (P04-2, P27b-conf, P34-P37, "2.2 P13a") foram conferidos na linha do passo, e todos existem. Listas de passos numa única evidência foram conferidas passo a passo.
7. **Numeração de linhas.** As citações sem o prefixo `artefato.txt:` (por exemplo, `README.md:21-85`, `src/extract.c:2147-2697`) seguem a convenção que o próprio `artefato.txt` indica: caminho e linha original. `artefato.txt:9-49` e `artefato.txt:9-50` são linhas do próprio `artefato.txt`: o ÍNDICE ocupa as linhas 9-49, e a 50 está em branco.

## Casos-limite (decisões que podem ser revistas)

- **Comentários em scripts (C2): 4 linhas `mal_interpretada`.** O laço de `src/extract.c:2599-2609` só pula espaços e o caractere `#`. A primeira letra de um comentário já marca `found_real`, e por isso scripts só com comentários passam. P21b e P28d confirmam isso na execução. Quatro respostas da etapa A afirmaram que o código rejeita ou implementa essa regra:
  - M1-c1-A-R-06 (`extract.c:2521-2611`): "O parser recusa scripts que só têm comentários".
  - M1-c2-A-R-08 (`extract.c:2519-2621`): "Rejeição de corpo só com comentários em [2610–2612]".
  - M1-c3-A-R-10 (`extract.c:2521-2613`): "O código bate com o comportamento descrito … rejeição de corpo só com comentários".
  - M2-c3-A-R-06 (`extract.c:2147-2697`): "a lógica descrita está implementada no código". A mesma faixa sustenta corretamente o achado do Mach-O thin, mas pelo critério 3 a linha fica `mal_interpretada`.

  O B2 de cada uma dessas cadeias reconhece o erro. Já as respostas que descreveram o laço literalmente, como teste de "caractere não branco diferente de '#'", sem dizer que ele rejeita comentários, ficaram `correta`. Pelo critério 1, essas quatro linhas seriam `correta` se a classe medisse só a existência do trecho.
- **Mach-O thin (C3).** Num host little-endian, as comparações `magic_le == 0xCEFAEDFE` e `0xCFFAEDFE` (`extract.c:2363` e `2409`) nunca são verdadeiras para os bytes registrados em `state.c:375-379`, e P24b confirma isso na execução. Na etapa A, algumas respostas só descreveram o ramo thin (comandos de carga, `LC_SEGMENT_64`), sem afirmar que ele funciona. Essas citações ficaram `correta` pelo critério 4. Se a equipe preferir tratar como `mal_interpretada` qualquer citação desse ramo usada para manter C3 como "depende de execução", as linhas afetadas são:
  - M1-c1-A-R-07 e M1-c2-A-R-09;
  - M2-c1-A-R-06 e M2-c2-A-R-07 (faixa ampla `extract.c:2147-2697`).
- **Linha além do fim do arquivo.** `reivindicacoes.md:1-22` (M2-c2-A-R-02 e M2-c2-B-R-02) cita até a linha 22, mas o arquivo tem 21 linhas, terminadas em `\n`. A mesma resposta diz ter lido `instrucoes-oficiais.md` "linhas 1–21" (o arquivo tem 20) e o `registro-factual.md` "linhas 1–315" (tem 314). Ao que parece, o leitor dessa LLM conta uma linha vazia depois do último `\n`. Todo o conteúdo citado existe, e a linha foi classificada `correta`, com nota. Pela leitura literal da regra "linha fora do intervalo é inexistente", as duas linhas virariam `inexistente`.
- **Erros de transcrição da Fig. 2, sem efeito na afirmação.** Os dois casos ficaram `correta`, com nota:
  - M2-c1-A-R-05: "2045109643 bytes", quando a figura diz 2845109643.
  - M2-c2-A-R-05: "00399084.exe" e "01797042.zip", quando a figura diz 00399884.exe e 01787042.zip.

## Outras observações

- **Nenhuma referência vaga a ponto de ser `nao_verificavel` e nenhum local inexistente.** Todas as faixas de linhas estão dentro dos arquivos, salvo o caso da linha 22 acima, e todas as seções e passos citados existem.
- **Faixas muito amplas.** M2 usa com frequência faixas de centenas de linhas (`extract.c:2147-2697`, `state.c:321-714`, `registro-factual.md:98-170`). Elas são verificáveis, mas pouco específicas: cada uma sustenta várias afirmações ao mesmo tempo. A precisão de M2 deve ser lida com isso em mente.
- **Afirmações que só aparecem no JSON.** Algumas citações da etapa B2 estão só no JSON, sem uso no corpo da resposta (por exemplo, `Dockerfile:1` em M1-c1-B). Nesses casos, a afirmação registrada é a do critério a que a citação dá suporte na própria resposta.
- **Extração automática.** A coluna `afirmacao` vinha pré-preenchida pela extração em algumas linhas, às vezes com o trecho errado. Exemplo: M1-c1-B-F-08 (P04) recebeu a linha de P04-2. Todas as afirmações foram reescritas a partir da resposta.
