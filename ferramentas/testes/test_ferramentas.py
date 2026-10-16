"""Testes das ferramentas da T8 com dados SINTÉTICOS (fixtures/runs/artefato-ficticio).

Rodar da raiz do repositório:
    python -B -m unittest discover -s ferramentas/testes -v

Cada teste copia as fixtures para uma pasta temporária; nada é gravado em runs/
nem dentro de ferramentas/testes/.
"""

import contextlib
import csv
import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
FERRAMENTAS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FERRAMENTAS))

import cegar  # noqa: E402
import extrair_decisoes as ex  # noqa: E402
import metricas  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "runs"
ART = "artefato-ficticio"


def ler_csv(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def silencioso(func, *args):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return func(*args)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.runs = self.tmp / "runs"
        shutil.copytree(FIXTURES, self.runs)
        self.art = self.runs / ART
        self.analise = self.art / "analise"

    def tearDown(self):
        self._tmp.cleanup()

    def extrair(self):
        self.assertEqual(silencioso(ex.main, [ART, "--runs", str(self.runs)]), 0)
        return ler_csv(self.analise / "decisoes.csv")

    def metricas(self, *extra):
        self.assertEqual(silencioso(metricas.main, [ART, "--runs", str(self.runs), *extra]), 0)
        return (self.analise / "metricas.md").read_text(encoding="utf-8")

    @staticmethod
    def achar(linhas, llm, cadeia, etapa, selo):
        achadas = [l for l in linhas if (l["llm"], l["cadeia"], l["etapa"], l["selo"])
                   == (llm, str(cadeia), etapa, selo)]
        return achadas[0] if achadas else None

    @staticmethod
    def linha_tabela(md, secao, *celulas):
        """Primeira linha de tabela da seção '## <secao>' que começa com as células dadas."""
        prefixo = "| " + " | ".join(celulas) + " |"
        dentro = False
        for linha in md.splitlines():
            if linha.startswith("## "):
                dentro = linha.startswith(f"## {secao}")
            elif dentro and linha.startswith(prefixo):
                return [c.strip() for c in linha.strip("|").split("|")]
        raise AssertionError(f"linha não encontrada na seção {secao}: {prefixo}")


class TestNormalizacao(unittest.TestCase):
    def test_decisoes_canonicas(self):
        for bruto, esperado in [("ATRIBUIR", "Atribuir"), ("não atribuir", "Não atribuir"),
                                ("Nao_Atribuir", "Não atribuir"), (" indeterminado ", "Indeterminado"),
                                ("NÃO-ATRIBUIR", "Não atribuir")]:
            self.assertEqual(ex.normalizar_decisao(bruto), esperado, bruto)

    def test_decisao_invalida_nao_e_adivinhada(self):
        for bruto in ["Talvez", "Atribuir|Não atribuir|Indeterminado", "...", "", None, 1,
                      "Indeterminado (depende)"]:
            self.assertIsNone(ex.normalizar_decisao(bruto), bruto)

    def test_confianca(self):
        self.assertEqual(ex.normalizar_confianca("35%"), "35")
        self.assertEqual(ex.normalizar_confianca(72.5), "72.5")
        self.assertIsNone(ex.normalizar_confianca(120))
        self.assertIsNone(ex.normalizar_confianca("alta"))
        self.assertIsNone(ex.normalizar_confianca(True))

    def test_json_com_cerca_e_aspas_tipograficas(self):
        texto = "x\n```json\n{“F”: {“decisao”: “Atribuir”}, “R”: {“decisao”: “Indeterminado”}}\n```\n"
        obj, erro, _ = ex.extrair_json(texto)
        self.assertIsNone(erro)
        self.assertEqual(obj["F"]["decisao"], "Atribuir")

    def test_json_quebrado_vira_erro(self):
        obj, erro, _ = ex.extrair_json('```json\n{"F": {"decisao": "Atribuir" "confianca": 1}}\n```')
        self.assertIsNone(obj)
        self.assertIn("JSON inválido", erro)

    def test_json_ausente(self):
        obj, erro, _ = ex.extrair_json("Sem bloco nenhum aqui. {x}")
        self.assertIsNone(obj)
        self.assertIn("ausente", erro)

    def test_secoes_ignoram_titulos_da_llm(self):
        _, secoes = ex.separar_secoes("## Resposta A\nx\n## B. Selo F\ny\n### Resposta B2\nz\n## Prompt B1\n")
        self.assertIn("## B. Selo F", secoes["resposta a"][0])
        self.assertIn("### Resposta B2", secoes["resposta a"][0])
        self.assertNotIn("resposta b2", secoes)

    def test_oficial_lido_da_referencia(self):
        caminho = FIXTURES / ART / "referencia" / "selos-oficiais.md"
        self.assertEqual(ex.ler_selos_oficiais(caminho), {"F": "Atribuir", "R": "Não atribuir"})


class TestExtracao(Base):
    def test_linhas_e_normalizacao(self):
        linhas = self.extrair()
        self.assertEqual(list(linhas[0].keys()), ex.COLUNAS_DECISOES)
        self.assertEqual(len(linhas), 33)
        l = self.achar(linhas, "openai", 2, "A", "R")  # “NÃO ATRIBUIR” com aspas tipográficas
        self.assertEqual(l["decisao"], "Não atribuir")
        self.assertEqual(self.achar(linhas, "openai", 2, "A", "F")["confianca"], "35")
        self.assertEqual(self.achar(linhas, "openai", 2, "B", "R")["decisao"], "Não atribuir")
        l = self.achar(linhas, "openai", 1, "B", "F")
        self.assertEqual((l["modelo"], l["versao"], l["esforco"], l["data_hora"]),
                         ("GPT-Ficticio-9", "0.0-teste", "médio", "2099-01-02 15:00 BRT"))
        self.assertEqual(l["arquivo_conversa"], f"runs/{ART}/llm-openai/cadeia-1.md")
        self.assertEqual((l["oficial"], l["coincide"], l["mudou"]), ("Atribuir", "sim", "sim"))
        self.assertEqual(self.achar(linhas, "openai", 1, "A", "F")["mudou"], "")
        # Último bloco vence o modelo repetido na resposta.
        self.assertEqual(self.achar(linhas, "openai", 3, "A", "F")["decisao"], "Indeterminado")

    def test_json_quebrado_nao_gera_decisao(self):
        linhas = self.extrair()
        self.assertIsNone(self.achar(linhas, "anthropic", 2, "A", "F"))
        self.assertIsNone(self.achar(linhas, "anthropic", 2, "A", "R"))
        b = self.achar(linhas, "anthropic", 2, "B", "F")
        self.assertEqual((b["decisao"], b["mudou"]), ("Não atribuir", ""))
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertRegex(pend, r"anthropic/cadeia-2\.md, etapa A .*JSON inválido")

    def test_cadeia_sem_b2(self):
        linhas = self.extrair()
        self.assertIsNotNone(self.achar(linhas, "anthropic", 3, "A", "F"))
        self.assertIsNone(self.achar(linhas, "anthropic", 3, "B", "F"))
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertRegex(pend, r"anthropic/cadeia-3\.md, etapa B \(## Resposta B2\): seção ausente")

    def test_decisao_fora_das_categorias(self):
        linhas = self.extrair()
        self.assertIsNone(self.achar(linhas, "google", 3, "A", "R"))
        self.assertIsNotNone(self.achar(linhas, "google", 3, "A", "F"))
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn('valor lido: "Talvez"', pend)

    def test_mudou_declarado_incoerente_vira_aviso(self):
        linhas = self.extrair()
        self.assertEqual(self.achar(linhas, "google", 1, "B", "F")["mudou"], "nao")
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertRegex(pend, r"google/cadeia-1\.md, selo F: \"mudou\" declarado = true")

    def test_humano_parcial_e_ausente(self):
        linhas = self.extrair()
        self.assertEqual(self.achar(linhas, "humano", 1, "A", "R")["decisao"], "Não atribuir")
        self.assertIsNone(self.achar(linhas, "humano", 1, "B", "F"))
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn("humano/decisao-final.md: decisão humana da etapa B ausente", pend)

        shutil.rmtree(self.art / "humano")
        linhas = self.extrair()
        self.assertFalse([l for l in linhas if l["llm"] == "humano"])
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn("decisao-analitica.md: decisão humana da etapa A ausente", pend)

    def test_modelo_humano_nao_preenchido_e_pendencia(self):
        (self.art / "humano" / "decisao-final.md").write_text(
            '- data_hora: <AAAA-MM-DD HH:MM BRT>\n```json\n'
            '{"F": {"decisao": "Atribuir|Não atribuir|Indeterminado", "confianca": 0, "evidencias": []},\n'
            ' "R": {"decisao": "Atribuir|Não atribuir|Indeterminado", "confianca": 0, "evidencias": [],'
            ' "por_reivindicacao": {}}}\n```\n', encoding="utf-8")
        linhas = self.extrair()
        self.assertIsNone(self.achar(linhas, "humano", 1, "B", "F"))
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn("decisao-final.md (humano, etapa B), selo F: decisão ausente ou fora", pend)

    def test_provedor_do_cabecalho_divergente_vira_aviso(self):
        caminho = self.art / "llm-google" / "cadeia-2.md"
        caminho.write_text(caminho.read_text(encoding="utf-8").replace(
            "- provedor: google", "- provedor: openai"), encoding="utf-8")
        linhas = self.extrair()
        self.assertEqual(self.achar(linhas, "google", 2, "B", "F")["llm"], "google")
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn('llm-google/cadeia-2.md: cabeçalho diz provedor "openai"', pend)
        self.assertNotIn("cadeia-1.md: cabeçalho diz provedor", pend)

    def test_cadeia_faltando_e_listada(self):
        (self.art / "llm-google" / "cadeia-2.md").unlink()
        self.extrair()
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn("llm-google/cadeia-2.md: cadeia ausente", pend)

    def test_por_reivindicacao(self):
        self.extrair()
        linhas = ler_csv(self.analise / "por-reivindicacao.csv")
        l = [x for x in linhas if (x["llm"], x["cadeia"], x["etapa"], x["reivindicacao"])
             == ("openai", "2", "A", "C1")][0]
        self.assertEqual((l["classificacao"], l["valor_original"]), ("nao_reproduzivel", "Não reproduzível"))
        l = [x for x in linhas if (x["llm"], x["cadeia"], x["etapa"], x["reivindicacao"])
             == ("google", "1", "A", "C2")][0]
        self.assertEqual(l["classificacao"], "")
        pend = (self.analise / "pendencias-extracao.md").read_text(encoding="utf-8")
        self.assertIn('C2: classificação fora das categorias (valor lido: "talvez")', pend)


class TestMetricas(Base):
    def setUp(self):
        super().setUp()
        self.extrair()

    def test_empate_de_moda_explicito(self):
        md = self.metricas()
        linha = self.linha_tabela(md, "1.", "Anthropic", "B", "F")
        self.assertEqual(linha[4:6], ["Empate: Atribuir = Não atribuir (1 cada)", "1/3 (empate)"])
        self.assertEqual(self.linha_tabela(md, "2.", "Anthropic", "B", "F")[3],
                         "Atribuir: 1, Não atribuir: 1")
        self.assertEqual(self.linha_tabela(md, "4.", "Anthropic", "F")[-1], "Não (empate)")
        self.assertEqual(self.linha_tabela(md, "3.", "Anthropic", "F")[5:7],
                         ["Não / n.d. (empate)", "n.d. (empate)"])

    def test_moda_e_estabilidade(self):
        md = self.metricas()
        linha = self.linha_tabela(md, "1.", "OpenAI", "B", "R")
        self.assertEqual(linha[4:9], ["Não atribuir", "2/3", "2/3 (67%)", "Não atribuir", "Sim"])
        # anthropic R após execução: 2 decisões (c3 sem B2) contam sobre 3 esperadas.
        self.assertEqual(self.linha_tabela(md, "1.", "Anthropic", "B", "R")[4:7],
                         ["Não atribuir", "2/3", "2/2 (100%)"])

    def test_criterio_de_consistencia(self):
        md = self.metricas()
        self.assertEqual(self.linha_tabela(md, "4.", "OpenAI", "F")[2:], ["Atribuir", "3/3", "Atribuir", "Sim"])
        self.assertEqual(self.linha_tabela(md, "4.", "OpenAI", "R")[-1], "Sim")  # 2/3 basta
        self.assertEqual(self.linha_tabela(md, "4.", "Google", "F")[-1], "Sim")
        self.assertEqual(self.linha_tabela(md, "4.", "Google", "R")[-1], "Não")
        f = self.linha_tabela(md, "4.", "Após execução (B)", "F")
        self.assertEqual(f[3], "Não (há empate)")
        self.assertTrue(f[4].startswith("1/1 (2 par(es) excluído(s)"))
        self.assertEqual(self.linha_tabela(md, "4.", "Após execução (B)", "R")[3:5], ["Não", "1/3"])

    def test_estabilidade_abaixo_de_dois_tercos_nao_e_consistente(self):
        caminho = self.analise / "decisoes.csv"
        linhas = [l for l in ler_csv(caminho)
                  if not (l["llm"] == "google" and l["etapa"] == "B" and l["selo"] == "F"
                          and l["cadeia"] != "1")]
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=ex.COLUNAS_DECISOES)
            w.writeheader()
            w.writerows(linhas)
        md = self.metricas()
        self.assertEqual(self.linha_tabela(md, "4.", "Google", "F")[2:], ["Atribuir", "1/3", "Atribuir", "Não"])

    def test_transicoes(self):
        md = self.metricas()
        self.assertEqual(self.linha_tabela(md, "5.", "Anthropic", "R", "1")[5], "Contradiz")
        self.assertEqual(self.linha_tabela(md, "5.", "Google", "F", "3")[5], "Introduz incerteza")
        self.assertEqual(self.linha_tabela(md, "5.", "OpenAI", "F", "1")[5], "Resolve incerteza")
        self.assertEqual(self.linha_tabela(md, "5.", "Google", "F", "1")[5], "Confirma")
        self.assertIn("Anthropic, F, cadeia 3: falta a etapa B", md)
        self.assertIn("Anthropic, F, cadeia 2: falta a etapa A", md)
        self.assertEqual(self.linha_tabela(md, "5.", "A: Indet.")[1:], ["5", "0", "0", "5"])
        # Relações por LLM: Google F = 1 confirma, 0 contradiz, 1 resolve, 1 introduz.
        self.assertEqual(self.linha_tabela(md, "5.", "Google", "F", "1", "0")[4:], ["1", "1"])

    def test_tabela_comparativa_e_causa(self):
        md = self.metricas()
        linha = self.linha_tabela(md, "3.", "OpenAI", "F")
        self.assertEqual(linha[2:], ["Atribuir", "Indet. (3/3)", "Atribuir (3/3)", "Não / Sim", "Sim",
                                     "_(preencher)_", "_(preencher)_"])
        self.assertEqual(self.linha_tabela(md, "3.", "Google", "F")[5:8], ["Sim / Sim", "Não", "n.a."])
        self.assertIn("| Causa da divergência |", md)

    def test_humano_ausente_na_etapa_b(self):
        md = self.metricas()
        self.assertEqual(self.linha_tabela(md, "7.", "Após execução (B)", "F")[2:4], ["**ausente**", "n.d."])
        self.assertEqual(self.linha_tabela(md, "7.", "Analítica (A)", "R")[2:4], ["Não atribuir", "Sim"])
        self.assertEqual(self.linha_tabela(md, "3.", "Humano", "F")[3:5], ["Indet. (1/1)", "sem decisões (0/1)"])

    def test_humano_totalmente_ausente(self):
        shutil.rmtree(self.art / "humano")
        self.extrair()
        md = self.metricas()
        self.assertIn("Nenhuma decisão humana em decisoes.csv", md)
        self.assertNotIn("| Humano | F", md)
        self.assertEqual(self.linha_tabela(md, "7.", "Analítica (A)", "F")[2], "**ausente**")

    def test_calibracao(self):
        md = self.metricas()
        # OpenAI B: coincide F 85,80,90 + R 70,75 -> 80.0; R Indet 50.
        linha = self.linha_tabela(md, "6.", "OpenAI", "B")
        self.assertEqual(linha[2:6], ["80.0 (n=5)", "50.0 (n=1)", "n.d.", "50.0 (n=1)"])

    def test_precisao_evidencias_com_chave(self):
        chave = self.tmp / "chave.json"
        silencioso(cegar.main, [ART, "--runs", str(self.runs), "--chave", str(chave), "--semente", "7"])
        caminho = self.analise / "evidencias.csv"
        linhas = ler_csv(caminho)
        mapa = json.loads(chave.read_text(encoding="utf-8"))["mapeamento"]
        openai = next(m for m, p in mapa.items() if p == "openai")
        for l in linhas:
            if l["llm"] == openai:
                l["classe"] = "Correta" if l["etapa"] == "A" else "inexistente"
            elif l["llm"] != "M9":
                l["classe"] = "mal interpretada" if l["selo"] == "F" else ""
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cegar.COLUNAS_EVIDENCIAS)
            w.writeheader()
            w.writerows(linhas)
        md = self.metricas("--chave", str(chave))
        self.assertEqual(self.linha_tabela(md, "8.", "OpenAI")[1:], ["12", "6", "0", "6", "0", "0", "6/12 (50%)"])
        self.assertTrue(self.linha_tabela(md, "8.", "Google")[-1].startswith("parcial: 0/"))
        md = self.metricas()
        self.assertIn(f"| {openai} | 12 |", md)


class TestCegar(Base):
    def cegar(self, *extra):
        self.chave = self.tmp / "fora-do-git" / "chave.json"
        self.saida = self.tmp / "cega"
        return silencioso(cegar.main, [ART, "--runs", str(self.runs), "--saida", str(self.saida),
                                       "--chave", str(self.chave), *extra])

    def test_mapeamento_e_remocao_de_nomes(self):
        self.assertEqual(self.cegar(), 0)
        mapa = json.loads(self.chave.read_text(encoding="utf-8"))["mapeamento"]
        self.assertEqual(sorted(mapa), ["M1", "M2", "M3"])
        self.assertEqual(sorted(mapa.values()), sorted(ex.PROVEDORES))
        arquivos = sorted(p.relative_to(self.saida).as_posix() for p in self.saida.rglob("*.md"))
        self.assertEqual(arquivos, [f"M{i}/cadeia-{n}.md" for i in (1, 2, 3) for n in (1, 2, 3)])
        proibidos = re.compile(r"gpt|openai|claude|anthropic|\bgemini\b|google|ficticio-9|"
                               r"ficticio 0\.1|ficticio x", re.IGNORECASE)
        for p in self.saida.rglob("*.md"):
            achado = proibidos.search(p.read_text(encoding="utf-8"))
            self.assertIsNone(achado, f"{achado and achado.group()} em {p}")
        google = next(m for m, p in mapa.items() if p == "google")
        texto = (self.saida / google / "cadeia-1.md").read_text(encoding="utf-8")
        self.assertIn("geminiano", texto)  # palavra comum preservada
        self.assertIn("## Resposta A", texto)

    def test_evidencias_pre_preenchidas(self):
        self.cegar()
        linhas = ler_csv(self.analise / "evidencias.csv")
        self.assertEqual(list(linhas[0].keys()), cegar.COLUNAS_EVIDENCIAS)
        self.assertTrue(all(l["classe"] == "" for l in linhas))
        self.assertTrue(all(l["llm"] in ("M1", "M2", "M3") for l in linhas))
        self.assertEqual(len({l["id_cego"] for l in linhas}), len(linhas))
        # 33 decisões de LLM menos 2 do humano, uma evidência cada.
        self.assertEqual(len(linhas), 31)
        com_afirmacao = [l for l in linhas if l["evidencia_citada"] == "FICTICIO.md:§1" and l["afirmacao"]]
        self.assertTrue(com_afirmacao)
        for l in linhas:
            self.assertNotIn("chatgpt", l["afirmacao"].lower())

    def test_nao_sobrescreve_chave(self):
        self.assertEqual(self.cegar(), 0)
        self.assertEqual(self.cegar(), 2)
        self.assertEqual(self.cegar("--forcar"), 0)

    def test_recusa_chave_versionavel_no_repositorio(self):
        chave = FERRAMENTAS / "testes" / "chave-nao-deve-existir.json"
        r = silencioso(cegar.main, [ART, "--runs", str(self.runs), "--saida", str(self.tmp / "c"),
                                    "--chave", str(chave)])
        self.assertEqual(r, 2)
        self.assertFalse(chave.exists())


if __name__ == "__main__":
    unittest.main()
