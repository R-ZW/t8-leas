"""Acrescenta o B2 do GPT a cadeia-N.md a partir de um export do Session Exporter.

Uso excepcional: o B2 do GPT foi feito em conversas NOVAS do Codex (contexto
restaurado a partir dos exports anteriores) e só existe como export escrito pelo
próprio modelo, sem link de compartilhamento. Por isso o texto não é literal e a
etapa B2 do GPT é marcada como NÃO COMPARÁVEL (ver runs/decisoes-operacionais.md).

Regras:
- Prompt B2 = texto após "## My request:" do pedido que começa com
  "Segue em anexo o registro factual", até o próximo cabeçalho do export.
- Resposta B2 = a última mensagem "AI / AGENT" antes do HUMAN seguinte
  (o pedido de export), até o próximo cabeçalho de interação.

Uso: python ferramentas/extrair_b2_session_export.py <export> <cadeia-N.md> --gravar
"""
import re
import sys

CAB = re.compile(r"^#{2,3} (?:Interaction \d+\s*[—-]\s*)?(HUMAN|AI / AGENT[^\n]*|TOOL / TERMINAL[^\n]*)$|^## Interaction \d+\s*$|^## Export Integrity Report", re.M)


def extrair(t):
    i = t.find("Segue em anexo o registro factual")
    if i < 0:
        raise SystemExit("prompt B2 não encontrado")
    fim_prompt = CAB.search(t, i)
    prompt = t[i:fim_prompt.start()].strip()
    cabs = [m for m in CAB.finditer(t, i)]
    humano = next((m for m in cabs if (m.group(1) or "").startswith("HUMAN")), None)
    limite = humano.start() if humano else len(t)
    ais = [m for m in cabs if m.start() < limite and (m.group(1) or "").startswith("AI / AGENT")]
    if not ais:
        raise SystemExit("resposta B2 não encontrada")
    ultimo = ais[-1]
    prox = next((m for m in cabs if m.start() > ultimo.start() and (m.group(0).startswith("## Interaction") or (m.group(1) or "").startswith(("HUMAN", "TOOL"))) ), None)
    resp = t[ultimo.end():prox.start() if prox else limite].strip()
    resp = re.sub(r"\n---\s*$", "", resp).strip()
    return prompt, resp, ultimo.group(0)


def main(exp, cadeia, gravar):
    t = open(exp, encoding="utf-8").read()
    prompt, resp, cab = extrair(t)
    print(f"{exp}: cabeçalho da resposta = {cab!r}; prompt {len(prompt)} chars; resposta {len(resp)} chars; JSON={'\"decisao\"' in resp}")
    print("   início:", resp[:100].replace("\n", " "))
    print("   fim:   ", resp[-140:].replace("\n", " "))
    if not gravar:
        return
    c = open(cadeia, encoding="utf-8").read()
    if "## Prompt B2" in c:
        raise SystemExit("cadeia já tem B2")
    nota = ("B2 NÃO COMPARÁVEL: enviado em conversa NOVA do Codex (contexto restaurado a partir do export do Session Exporter de A/B1), "
            "em outro workspace com o repositório inteiro acessível; texto extraído do export escrito pelo modelo "
            f"(`exportacao-bruta/{exp.replace(chr(92), '/').split('/')[-1]}`), sem link de compartilhamento, logo não literal")
    c = re.sub(r"^- data_hora_B2: .*$", "- data_hora_B2: não registrado (17–18/10/2026, conversa nova)", c, count=1, flags=re.M)
    c = re.sub(r"^- anexo_B2: .*$", "- anexo_B2: registro-factual.md (lido do disco no novo workspace; bytes não conferidos)", c, count=1, flags=re.M)
    c = re.sub(r"^(- desvios: .*)$", lambda m: m.group(1) + " | " + nota, c, count=1, flags=re.M)
    c = c.rstrip("\n") + f"\n\n## Prompt B2\n\n{prompt}\n\n## Resposta B2\n\n{resp}\n"
    with open(cadeia, "w", encoding="utf-8", newline="\n") as f:
        f.write(c)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--gravar" in sys.argv)
