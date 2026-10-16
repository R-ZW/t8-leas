"""Gera os prompts A, B1 e B2 de cada artefato a partir de um único modelo.

O texto vem do §5 e do §6 do protocolo (novo_protocolo.md). Só os campos entre
chaves mudam entre artefatos, e isso garante prompts idênticos para as três LLMs.
Adaptações deliberadas, iguais para todos, estão registradas em
runs/<artefato>/pacote/prompts/LEIA-ME.md.

Uso: python ferramentas/gerar_prompts.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / "runs"

ARTEFATOS = {
    "foremost-ng": {"EVENTO EDIÇÃO": "SBSeg 2025", "SHA": "bb812a22cb06ef87b5a2d877dfb6f40eb12d460d"},
    "mininet-gui": {"EVENTO EDIÇÃO": "SBRC 2025", "SHA": "465648a4425a4457af0348ab951cf7f71d37a86f"},
}

PROMPT_A = """Atue como revisor do Comitê de Avaliação de Artefatos do {EVENTO EDIÇÃO}. Avalie somente os selos Funcional (F) e Reprodutível (R), seguindo exatamente as instruções oficiais anexadas (instrucoes-oficiais.md).

MATERIAL
Use exclusivamente os arquivos anexados: artigo.pdf (fonte das reivindicações), artefato.txt (o artefato completo na versão {SHA}, em arquivo único: índice de todos os arquivos do repositório e o texto integral de cada arquivo de texto, com o número da linha original), instrucoes-oficiais.md e reivindicacoes.md (lista de reivindicações principais e regra para o selo R). Não navegue na web nem consulte memória, outras conversas, projetos ou conectores. Se precisar de algo que não está nos anexos, registre como evidência ausente.

TAREFA
Esta é uma avaliação analítica: você não executou o artefato e não deve afirmar que algo funcionou.

Para cada selo:
1. Liste os critérios oficiais aplicáveis, citando o trecho das instruções.
2. Para cada critério, indique: atendido na documentação, não atendido, ou só verificável por execução.
3. Cite cada evidência no formato [arquivo:seção ou linha] e transcreva o trecho curto que a sustenta.
4. Decida: Atribuir, Não atribuir ou Indeterminado, usando esta regra:
   - Não atribuir: há evidência de que um critério obrigatório não é atendido (por exemplo, falta o dado necessário para uma reivindicação principal).
   - Indeterminado: nenhum critério obrigatório falha na documentação, mas a decisão depende de execução.
   - Atribuir: somente se os critérios estiverem atendidos com evidência suficiente para isso.
5. Informe sua confiança de 0 a 100 de que o comitê oficial atribuiu o selo.
6. Liste o que precisaria ser observado na execução para mudar sua decisão.

Para R, avalie cada reivindicação de reivindicacoes.md separadamente.

FORMATO
Responda em texto com as seções: A. Materiais examinados (liste os arquivos que você efetivamente abriu); B. Selo F; C. Selo R (por reivindicação); D. Lacunas e riscos.
Ao final, inclua um bloco JSON exatamente neste formato:
{{"F": {{"decisao": "...", "confianca": 0, "evidencias": ["arquivo:local", "..."]}},
 "R": {{"decisao": "...", "confianca": 0, "evidencias": ["..."],
       "por_reivindicacao": {{"C1": "reproduzivel|nao_reproduzivel|depende_execucao"}}}}}}
"""

PROMPT_B1 = """Com base no mesmo material, produza o roteiro para que eu execute o artefato e verifique F e R. Não afirme que executou nada.

Siga somente os procedimentos fornecidos pelos autores. Quando um passo não estiver documentado pelos autores, marque-o como [NÃO DOCUMENTADO] e justifique por que ele é necessário.

Para cada passo: identificador (P1, P2...), selo e reivindicação relacionados, diretório, comando exato, resultado esperado segundo os autores, evidência a salvar, critério de sucesso, critério de falha e critério de interrupção.

Inclua: requisitos de hardware e software do ambiente; teste mínimo (F); um bloco por reivindicação de reivindicacoes.md (R); tempo estimado.
Ao final, uma tabela com todos os passos.
"""

# {CONDICAO} é preenchido uma única vez, depois da execução, e fica igual nas nove cadeias.
PROMPT_B2 = """Segue em anexo o registro factual da execução do artefato (registro-factual.md), feita em ambiente que {CONDICAO} aos requisitos dos autores. O roteiro executado consolidou os planos de três revisores, incluindo o seu.

Com base no registro e no material anterior:
1. Para cada passo relevante, diga se o resultado confirma, contradiz ou não altera sua avaliação analítica.
2. Decida novamente F e R (Atribuir, Não atribuir ou Indeterminado) com a mesma regra de antes. Use Indeterminado somente se faltar evidência que o registro não fornece; diga exatamente qual.
3. Trate passos marcados D2 e D3 como evidência complementar, não como reprodução das reivindicações dos autores.
4. Informe confiança de 0 a 100 e explique a mudança em relação à decisão analítica, se houver.
Repita o bloco JSON da etapa A com as novas decisões e acrescente "mudou": true/false para cada selo.
"""


def main():
    for nome, campos in ARTEFATOS.items():
        pasta = RAIZ / nome / "pacote" / "prompts"
        pasta.mkdir(parents=True, exist_ok=True)
        textos = {
            "prompt-A.txt": PROMPT_A.format(**campos),
            "prompt-B1.txt": PROMPT_B1,
            "prompt-B2-modelo.txt": PROMPT_B2,
        }
        for arquivo, texto in textos.items():
            (pasta / arquivo).write_text(texto, encoding="utf-8", newline="\n")
        print(pasta)


if __name__ == "__main__":
    main()
