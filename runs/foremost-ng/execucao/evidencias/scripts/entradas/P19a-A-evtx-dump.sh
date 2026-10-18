# Roteiro A, P19 (python-evtx instalado por apt em P12, no lugar de venv+pip; nome do EVTX ajustado)
cd ~/aval
nome=$(awk '$1 ~ /evtx/ {print $3}' evidencias/P15_offsets.txt)
evtx_dump.py amostras/evtx_system.evtx > evidencias/P19_original.xml; echo "exit original=$?"
evtx_dump.py saida_todos/evtx/$nome.evtx > evidencias/P19_recuperado.xml; echo "exit recuperado=$?"
grep -c '<Event ' evidencias/P19_original.xml evidencias/P19_recuperado.xml
cmp evidencias/P19_original.xml evidencias/P19_recuperado.xml && echo XML_IDENTICO
# mesma leitura sobre a saída restrita (-t evtx,elf,exe)
evtx_dump.py saida_tipos/evtx/$nome.evtx > evidencias/P19_recuperado_tipos.xml; echo "exit recuperado (saida_tipos)=$?"
grep -c '<Event ' evidencias/P19_recuperado_tipos.xml
