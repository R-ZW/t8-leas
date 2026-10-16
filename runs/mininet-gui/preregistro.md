# Pré-registro metodológico — Mininet-GUI

**Congelamento inicial:** 15/10/2026 (America/Sao_Paulo), **antes de qualquer Prompt A/conversa avaliadora**. Versão 1 da lista: [`pacote/reivindicacoes.md`](pacote/reivindicacoes.md), IDs C1–C6. O arquivo [`CONGELAMENTO.sha256`](CONGELAMENTO.sha256) será gerado depois de finalizar este pré-registro e a lista; fica fora do pacote das LLMs.

## Fontes e separação de papéis

- Artigo recebido `fontes/mininet-gui.pdf` (pp. 1–9), [README no SHA fixado](https://github.com/latarc/mininet-gui/blob/465648a4425a4457af0348ab951cf7f71d37a86f/README.md), [instruções oficiais de revisão SBRC 2025](https://doc-artefatos.github.io/sbrc2025/revinstrucoes.html) e [`versao.md`](versao.md). O SHA é **proxy de 2025**; identidade com o código da OVA e com o checkout do CTA não foi demonstrada.
- **Os selos oficiais arquivados em `referencia/` não foram usados para escolher C1–C6, prioridade ou critérios de sucesso.** Os grafismos de selos impressos na p. 1 do artigo também não determinaram a lista. As regras oficiais F/R dão o padrão de prova, sem fornecer o resultado desta T8.
- `reivindicacoes.md` é mapa prévio, não parecer. As três demonstrações do artigo e os passos opcionais do README foram mapeados como suporte/complemento, sem transformar automaticamente cada caso em experimento principal.

## Regra de seleção para R, fixada antes do teste

1. Tomar exatamente as **seis contribuições enumeradas no artigo p. 2, §1** como universo C1–C6.
2. Marcar como **principal para R** apenas a contribuição com subseção nomeada em `# Experimentos` do README do SHA. A aplicação mecânica da regra seleciona **C4 (geração Single/Linear/Tree)** e **C5 (WebShell)**, as duas únicas subseções. C1, C2, C3 e C6 continuam documentadas no mapa, mas o teste mínimo e as funções de interface as colocam como observação funcional/complementar. Não trocar a seleção depois de ver o resultado, a disponibilidade da OVA ou os selos publicados.
3. Para C4, exigir observação dos **três modelos** com seleção/resultado registrados; o README não fixa quantidades de Linear/Tree nem gabarito de links. Para C5, exigir comando real em nó emulado e saída atribuível ao seu namespace; a subseção não fixa um comando ou resultado. Uma API ou frontend iniciados sem Mininet não bastam. `pingall`, iperf, segundo controlador e exportação são evidências complementares identificadas, não novas reivindicações principais.
4. Os [critérios SBRC 2025](https://doc-artefatos.github.io/sbrc2025/revinstrucoes.html) pedem execução observável para F e processo/resultado das principais reivindicações para R. Portanto, presença de botão ou instrução escrita não será descrita como reprodução já realizada. A falta de especificações autorais de entrada/resultado será registrada, não preenchida como se fosse documentação dos autores.

## Ambiente e hipóteses prévias

- **Configuração pretendida:** VM do autor ou Linux equivalente com Mininet/Open vSwitch, VirtualBox 7.1.6 r167084 quando se usar OVA, **8 GB RAM e ao menos 1 vCPU**. O mesmo README afirma 2 GB/1 núcleo em “Experimentos”; adotam-se 8 GB como exigência mais conservadora, sem chamar 2 GB de valor testado. Registrar configuração real e impedimento caso o host não suporte essa memória.
- **OVA:** o link do README do proxy abriu página de arquivo inexistente na consulta documentada em `versao.md`; a página da OVA atual existe, mas seu commit interno é desconhecido. Confirmar hash da OVA e `git rev-parse HEAD` dentro dela antes de atribuir qualquer execução ao SHA fixado. Se diferir, registrar desvio de versão, não igualar snapshots por nome.
- **H-MG1:** os procedimentos C4/C5 serão suficientes para planejar observações qualitativas, mas a falta de configurações e saídas de referência reduzirá a comparabilidade quantitativa.
- **H-MG2:** o teste mínimo poderá observar C1/C2; C3/C6 exigirão passos complementares porque o README não apresenta receita específica para suas afirmações completas.
- **H-MG3:** a incerteza sobre a OVA poderá bloquear a atribuição de resultados ao proxy mesmo que a aplicação abra. Uma confirmação de SHA ou comparação integral do código pode contrariar esta hipótese.

Estas hipóteses tratam de observabilidade e identidade de versão, **não** predizem o selo oficial ou simulam êxito.

## Procedimento de análise pré-fixado

- **Etapa A:** aplicar o mesmo pacote a todas as nove conversas do artefato. Separar evidência documental, passo autoral e ponto dependente de execução; para R, usar C4/C5 como núcleo, sem omitir C1/C2/C3/C6 da descrição.
- **Etapa B1/execução:** seguir o README do SHA; guardar versão da OVA/código, ambiente, ações na GUI, comandos, saídas, capturas, horário e hash dos arquivos relevantes. D0 = documentado, D1 = ajuste trivial, D2 = contorno não documentado, D3 = teste externo. Testes de C3/C6 desenhados pelo executor serão rotulados complementares, sem virar experimento autoral.
- **Etapa B2:** entregar um único registro factual congelado às nove conversas. Comparar observações de C4/C5 ao critério pré-fixado; distinguir falha do software, falha de ambiente, diferença de versão e teste bloqueado. Não converter ausência de execução em sucesso, nem declarar uma decisão F/R dentro do registro factual.

## Imutabilidade e desvios

Após o primeiro Prompt A, **não editar nem renumerar** `pacote/reivindicacoes.md` ou este pré-registro. Correção, dado novo ou ajuste de regra deverá constar de `desvios/DV-001.md`, `DV-002.md` etc., com data, motivo, Cn afetada, novo arquivo/hash e cadeias atingidas, mantendo a versão 1 intacta. Se o desvio for usado, a mesma informação deve chegar às nove conversas ou as cadeias afetadas devem recomeçar; respostas anteriores permanecem arquivadas. Atualizações factuais posteriores a B2 também serão versionadas.
