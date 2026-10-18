# Roteiro G, P6 (comandos literais; diretório <raiz>/src)
set -x
python3 -c '
import struct
# Cria um container EVTX mínimo (cabeçalho 4 KiB + 1 chunk de 64 KiB)
evtx_hdr = bytearray(4096)
evtx_hdr[0:8] = b"ElfFile\x00"
struct.pack_into("<Q", evtx_hdr, 0x08, 0)     # FirstChunkNumber
struct.pack_into("<Q", evtx_hdr, 0x10, 1)     # LastChunkNumber
struct.pack_into("<I", evtx_hdr, 0x18, 1)     # Offset 0x18 lido por extract_evtx como chunk_count
struct.pack_into("<I", evtx_hdr, 0x20, 128)   # HeaderSize
struct.pack_into("<H", evtx_hdr, 0x24, 1)     # MinorVersion
struct.pack_into("<H", evtx_hdr, 0x26, 3)     # MajorVersion
struct.pack_into("<H", evtx_hdr, 0x28, 4096)  # HeaderBlockSize
struct.pack_into("<H", evtx_hdr, 0x2A, 1)     # NumberOfChunks (especificação EVTX)
chunk = bytearray(65536)
chunk[0:8] = b"ElfChnk\x00"
img = bytearray(256 * 1024)
offset = 8192
img[offset:offset+4096] = evtx_hdr
img[offset+4096:offset+4096+65536] = chunk
with open("c1_evtx.img", "wb") as f:
    f.write(img)
'
rm -rf /tmp/out_c1
ls -l c1_evtx.img; sha256sum c1_evtx.img
