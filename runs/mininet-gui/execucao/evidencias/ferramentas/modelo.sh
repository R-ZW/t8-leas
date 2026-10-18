#!/bin/bash
# uso: modelo.sh <rotulo> <Tipo> <campo1=valor> [campo2=valor]
S="/c/Users/eduar/AppData/Local/Temp/claude/D--Lab-artefatos-t8-leas/e5f6f2bc-804d-4a02-93e7-6fcf8f6d5c4b/scratchpad"; cd $S
R=$1; T=$2; shift 2
GRAFO='(()=>{let el=document.querySelector(".vis-network"); let i=el.parentElement.__vueParentComponent; while(i&&!(i.proxy&&i.proxy.network)) i=i.parent; const p=i.proxy; const ns=p.nodes.get(); const es=p.edges.get(); return {nos:ns.length, ids:ns.map(n=>n.id).join(","), arestas:es.length, lista:es.map(e=>e.from+"-"+e.to+(e.dashes?"(assoc)":"")).join(" ")}})()'
echo "== $R inicio $(date -u +%FT%T.%3NZ)"
node cdp.mjs dnd '#draggable-controller' 700 200
node cdp.mjs click 'form .submit-button' 2500
node cdp.mjs click '#button-create-topology' 1500
node cdp.mjs select '#type' $T
node cdp.mjs select '#controller' c1
for kv in "$@"; do node cdp.mjs fill "#${kv%%=*}" "${kv#*=}"; done
node cdp.mjs eval '[...document.querySelectorAll("form label")].map(l=>l.innerText+" "+(document.getElementById(l.htmlFor)||{}).value).join(" | ")'
node cdp.mjs shot $R-formulario
echo "== $R submit $(date -u +%FT%T.%3NZ)"
node cdp.mjs click 'form .submit-button' 1000
for i in $(seq 1 60); do n=$(node cdp.mjs eval 'document.querySelectorAll(".modal-mask").length'); [ "$n" = "0" ] && break; sleep 2; done
sleep 4
echo "== $R grafo $(date -u +%FT%T.%3NZ)"
node cdp.mjs eval "$GRAFO"
node cdp.mjs text '.tabs' | tr '\n' ' '; echo
node cdp.mjs shot $R-grafo
