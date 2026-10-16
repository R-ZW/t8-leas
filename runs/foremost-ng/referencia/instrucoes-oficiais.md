# Instruções oficiais de revisão — SBSeg 2025

**Fonte oficial:** https://doc-artefatos.github.io/sbseg2025/revinstrucoes.html  
**Consulta:** 15/10/2026 (America/Sao_Paulo).  
**Natureza deste arquivo:** registro analítico dos critérios consultados, com link para o texto integral oficial. Não é uma cópia literal da página.

## Processo e critérios

- O revisor deve comparar a qualidade do artefato ao artigo e aos requisitos de cada selo. A avaliação do artefato é distinta da revisão científica do artigo.
- A edição descreve duas rodadas: parecer inicial e decisão após resposta dos autores. O parecer deve explicitar etapas realizadas, execução observada, resultados e problemas.
- **Disponível (D):** código/dados em repositório estável; README com objetivo, organização, selos pretendidos, ambiente, dependências, segurança, instalação, teste mínimo, experimentos/reivindicações e licença.
- **Funcional (F):** código/artefato executável e funcionalidades observáveis. A documentação deve informar dependências e versões, ambiente, instalação/execução e exemplo mínimo. A página exige que o revisor **execute** o artefato e inclua prova da execução e saídas no parecer.
- **Sustentável (S):** código modular, organizado, inteligível e documentado minimamente; reivindicações do artigo localizáveis no artefato.
- **Reprodutível (R):** instruções e processo para reproduzir as principais reivindicações do artigo. A página exige que o revisor **execute os experimentos**, confira resultados como tabelas/figuras e resuma os resultados no parecer.
- Uma revisão breve deve justificar cada selo atribuído ou negado após a avaliação.

## Implicação para a T8

Leitura de README e compilação isolada não bastam para confirmar F. Para R, é preciso identificar as reivindicações principais e suas entradas, executar o procedimento dos autores e confrontar o observado com o artigo. Falta de insumo deve ser registrada como limite da reprodução, sem criar resultado fictício.

**Arquivo de resultados da mesma edição:** https://doc-artefatos.github.io/sbseg2025/results.html. Ver `selos-oficiais.md` nesta pasta.
