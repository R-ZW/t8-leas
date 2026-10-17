"""Gera cadeia-N.md (formato de runs/MODELO-cadeia.md) a partir do JSON público
de um link de compartilhamento do Codex (chatgpt.com/s/cx_...).

Fonte: GET https://chatgpt.com/backend-api/wham/shared_threads/<id>, que devolve
os turnos com os itens userMessage, agentMessage, reasoning, imageView e fileChange.
Regras, iguais às usadas para o Claude:
- Prompt de cada etapa = texto do userMessage, sem alteração.
- Resposta = todos os agentMessage do turno (comentários de progresso e resposta
  final), na ordem, unidos por linha em branco e sem alteração.
- reasoning, imageView e fileChange ficam fora da transcrição e entram em `desvios`.
- A etapa é reconhecida pelo início do prompt (A, B1, B2); turnos fora do roteiro
  (por exemplo, o pedido ao Session Exporter) são omitidos e registrados em `desvios`.

Uso: python ferramentas/transcrever_codex.py <json> <saida.md> <ID> <url> <anexos_A>
"""
import json
import sys

ETAPAS = (("Atue como revisor", "A"), ("Com base no mesmo material", "B1"),
          ("Segue em anexo o registro factual", "B2"))


def etapa(texto):
    for inicio, nome in ETAPAS:
        if texto.startswith(inicio):
            return nome
    return None


def main(caminho, saida, ident, url, anexos):
    j = json.load(open(caminho, encoding="utf-8"))
    secoes, desvios, dur = [], [], {}
    for k, turno in enumerate(j["turns"]):
        itens = turno["items"]
        prompt = "".join(c["text"] for it in itens if it["type"] == "userMessage"
                         for c in it["content"] if c["type"] == "text")
        e = etapa(prompt)
        if e is None:
            desvios.append(f"turno {k + 1} fora do roteiro, omitido da transcrição: \"{prompt[:90].strip()}\"")
            continue
        resp = "\n\n".join(it["text"] for it in itens if it["type"] == "agentMessage")
        dur[e] = round(turno.get("durationMs", 0) / 1000)
        secoes.append(f"## Prompt {e}\n\n{prompt}\n\n## Resposta {e}\n\n{resp}\n")
        n_img = sum(1 for it in itens if it["type"] == "imageView")
        arqs = [c["path"] for it in itens if it["type"] == "fileChange" for c in it["changes"]]
        if n_img:
            desvios.append(f"resposta {e}: {n_img} visualização(ões) de imagem (páginas do artigo.pdf) omitidas")
        if arqs:
            desvios.append(f"resposta {e}: alterou arquivos {arqs}")
        if ":codex-file-citation{" in resp:
            desvios.append(f"resposta {e}: contém marcações :codex-file-citation da interface, mantidas sem alteração")
    duracoes = "; ".join(f"{e}={s}s" for e, s in dur.items())
    meta = [
        f"# Cadeia {ident} — openai", "",
        "- provedor: openai",
        "- modelo_exibido: a confirmar pelo operador (o link de compartilhamento do Codex não exibe o modelo)",
        "- versao: não registrado",
        "- esforco: não registrado",
        "- interface: Codex (agente com workspace local e terminal), operado por Reinaldo Zimmer Wendt; anexos lidos do disco por caminho em `runs/<artefato>/pacote/` (desvio: agente em vez do chat do ChatGPT)",
        "- data_hora_A: não registrado no link (duração do turno: " + duracoes + ")",
        "- data_hora_B1: não registrado no link",
        "- data_hora_B2: pendente",
        f"- anexos_A: {anexos} (lidos do disco; bytes não conferidos dentro da conversa)",
        "- anexo_B2: pendente",
        f"- metodo_exportacao: transcrição gerada por `ferramentas/transcrever_codex.py` do JSON público do link {url} (cópia bruta em `exportacao-bruta/`); textos de userMessage e agentMessage sem alteração; reasoning, imageView, fileChange e chamadas de ferramenta (não incluídas no link) omitidos. O export anterior, escrito pelo próprio modelo via Session Exporter, está em `exportacao-bruta/` e não é usado na análise",
        "- desvios: " + (" | ".join(desvios) if desvios else "nenhum"), "",
    ]
    with open(saida, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(meta) + "\n" + "\n".join(secoes))


if __name__ == "__main__":
    main(*sys.argv[1:6])
