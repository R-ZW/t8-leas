#!/usr/bin/env python3
"""Compara a saída do foremost-ng com o gabarito oficial do DFTT (D3).

Uso: compara-gabarito.py GABARITO.tsv DIR_SAIDA [BS]

Para cada arquivo do gabarito: procura um arquivo recuperado cujo número no
nome (offset/BS, bs=512 por padrão) seja o setor inicial publicado
("recuperado no setor") e compara o MD5 ("correto"). Também procura o MD5 do
gabarito entre todos os recuperados, em qualquer posição. Lista os
recuperados que não correspondem a nenhum arquivo do gabarito.
"""
import csv, hashlib, os, re, sys

gab_path, saida = sys.argv[1], sys.argv[2]
with open(gab_path, newline='', encoding='utf-8') as f:
    gab = list(csv.DictReader(f, delimiter='\t'))

recuperados = []  # (setor, caminho relativo, tamanho, md5)
for raiz, _, nomes in os.walk(saida):
    for n in sorted(nomes):
        if n == 'audit.txt':
            continue
        p = os.path.join(raiz, n)
        m = re.match(r'(\d+)', n)
        setor = int(m.group(1)) if m else None
        md5 = hashlib.md5(open(p, 'rb').read()).hexdigest()
        recuperados.append((setor, os.path.relpath(p, saida), os.path.getsize(p), md5))
recuperados.sort(key=lambda r: (r[0] is None, r[0], r[1]))

md5s = {}
for r in recuperados:
    md5s.setdefault(r[3], []).append(r[1])

print(f'gabarito: {gab_path} ({len(gab)} arquivos)')
print(f'saida: {saida} ({len(recuperados)} arquivos recuperados, sem audit.txt)')
print()
print('n\tnome\tsetor\ttam_esperado\trecuperado_no_setor\ttam_recuperado\tmd5_igual\tmd5_em_outro_arquivo')
n_rec = n_ok = n_md5_qualquer = 0
usados = set()
for g in gab:
    setor = int(g['setor_inicial'])
    no_setor = [r for r in recuperados if r[0] == setor]
    alvo = no_setor[0] if no_setor else None
    igual = bool(alvo and alvo[3] == g['md5'])
    outros = [p for p in md5s.get(g['md5'], []) if not alvo or p != alvo[1]]
    if alvo:
        n_rec += 1
        usados.add(alvo[1])
    if igual:
        n_ok += 1
    if g['md5'] in md5s:
        n_md5_qualquer += 1
        usados.update(md5s[g['md5']])
    print('\t'.join([g['n'], g['nome'], str(setor), g['tamanho'],
                     alvo[1] if alvo else '-', str(alvo[2]) if alvo else '-',
                     'sim' if igual else 'nao', ','.join(outros) or '-']))
print()
print(f'RESUMO esperados={len(gab)} recuperados_no_setor={n_rec} corretos_md5_no_setor={n_ok} '
      f'md5_do_gabarito_em_qualquer_recuperado={n_md5_qualquer} total_recuperados={len(recuperados)} '
      f'recuperados_sem_correspondencia={len(recuperados) - len(usados)}')
print()
print('recuperados sem correspondencia no gabarito (setor, arquivo, tamanho, md5):')
for r in recuperados:
    if r[1] not in usados:
        print(f'  {r[0]}\t{r[1]}\t{r[2]}\t{r[3]}')
