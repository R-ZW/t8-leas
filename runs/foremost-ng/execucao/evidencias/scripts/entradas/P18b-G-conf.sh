# Roteiro G, P7 (conferência literal após o carving; diretório <raiz>/src)
cat /tmp/out_c1/audit.txt
file /tmp/out_c1/evtx/*.evtx
ls -l /tmp/out_c1/evtx/
python3 -c '
import glob
files = glob.glob("/tmp/out_c1/evtx/*.evtx")
assert len(files) == 1, f"Esperado 1 arquivo .evtx, encontrado: {files}"
data = open(files[0], "rb").read()
print("Arquivo:", files[0], "Tamanho:", len(data), "Magic:", data[:8])
assert data[:8] == b"ElfFile\x00"
'
