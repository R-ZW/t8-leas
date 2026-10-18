# Fase 3b — saída completa de readelf -h -l nos ELF recuperados da imagem combinada
# (mesmo comando da conferência de P28d, sem o filtro grep).
export REG_DIR=/execucao/evidencias
cd ~/aval
passo P28d-readelf -- sh -c 'for f in saida_todos/elf/*.elf; do echo "=== $f"; readelf -h -l "$f"; echo "exit readelf=$?"; done'
