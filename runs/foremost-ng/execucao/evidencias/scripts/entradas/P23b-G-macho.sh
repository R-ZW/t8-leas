# Roteiro G, P10 (comandos literais; diretório <raiz>/src)
set -x
python3 -c '
import struct
# 1. Constrói um binário Mach-O 64-bit thin válido de 4096 bytes
thin64 = bytearray(4096)
# mach_header_64: magic=0xfeedfacf, cputype=0x01000007 (x86_64), cpusubtype=3, filetype=2 (EXECUTE), ncmds=1, sizeofcmds=72, flags=1, reserved=0
struct.pack_into("<IIIIIIII", thin64, 0, 0xFEEDFACF, 0x01000007, 3, 2, 1, 72, 1, 0)
# segment_command_64 (cmd=0x19 LC_SEGMENT_64, cmdsize=72, segname="__TEXT", vmaddr=0, vmsize=4096, fileoff=0, filesize=4096, maxprot=7, initprot=5, nsects=0, flags=0)
struct.pack_into("<II16sQQQQIIii", thin64, 32, 0x19, 72, b"__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 0, 4096, 0, 4096, 7, 5, 0, 0)

# 2. Constrói um binário Mach-O FAT (Universal) de 8192 bytes contendo a fat_header (BE) e a slice thin64 no offset 4096
fat = bytearray(8192)
# fat_header: magic=0xCAFEBABE, nfat_arch=1
struct.pack_into(">II", fat, 0, 0xCAFEBABE, 1)
# fat_arch: cputype=0x01000007, cpusubtype=3, offset=4096, size=4096, align=12
struct.pack_into(">IIIII", fat, 8, 0x01000007, 3, 4096, 4096, 12)
fat[4096:8192] = thin64

img = bytearray(128 * 1024)
img[8192:8192+len(thin64)] = thin64
img[32768:32768+len(fat)] = fat
with open("c3_macho.img", "wb") as f:
    f.write(img)
'
rm -rf /tmp/out_c3
ls -l c3_macho.img; sha256sum c3_macho.img
