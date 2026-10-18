# Complemento de P11 (D2): os arquivos de texto do artefato.zip têm fim de linha CRLF
# e os do clone têm LF. Para cada arquivo do zip: compara byte a byte; se diferir,
# compara de novo removendo CR do lado do zip.
cd /tmp/zipref/foremost-ng-bb812a22
brutos=0; semcr=0; difs=0
for f in $(find . -type f | sort); do
  if cmp -s "$f" ~/trabalho/foremost-ng/"$f"; then
    brutos=$((brutos+1))
  elif tr -d '\r' < "$f" | cmp -s - ~/trabalho/foremost-ng/"$f"; then
    semcr=$((semcr+1)); echo "igual sem CR: $f"
  else
    difs=$((difs+1)); echo "DIFERENTE: $f"
  fi
done
echo "arquivos no zip: $(find . -type f | wc -l); iguais byte a byte: $brutos; iguais apos remover CR: $semcr; diferentes: $difs"
echo "arquivos no clone (sem .git): $(cd ~/trabalho/foremost-ng && find . -path ./.git -prune -o -type f -print | wc -l)"
