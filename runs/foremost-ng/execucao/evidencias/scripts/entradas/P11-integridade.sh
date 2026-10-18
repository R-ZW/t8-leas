# Roteiro A:P4 (alternativa: conferir sha256 do artefato.zip) e A2:P6 (comparar fontes).
sha256sum /pacote/artefato.zip
rm -rf /tmp/zipref && mkdir /tmp/zipref && unzip -q /pacote/artefato.zip -d /tmp/zipref
if diff -r -x .git ~/trabalho/foremost-ng /tmp/zipref/foremost-ng-bb812a22; then
  echo "ARVORES IGUAIS (clone em bb812a22, sem .git) x (artefato.zip)"
else
  echo "ARVORES DIFERENTES"
fi
cd /tmp/zipref/foremost-ng-bb812a22 && sha256sum README.md Dockerfile src/Makefile src/main.c src/dir.c src/extract.c src/state.c src/vt_query.c
