// Driver mínimo do Edge headless via Chrome DevTools Protocol (sem dependências; Node >= 22).
// Cada chamada conecta à aba existente, executa uma ação e desconecta.
// Uso: node cdp.mjs <comando> [args...]
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const PORT = 9333;
const TELAS = "D:/Lab-artefatos/t8-leas/runs/mininet-gui/execucao/evidencias/telas";
const DOWN = "D:/Lab-artefatos/t8-leas/runs/mininet-gui/execucao/evidencias/exportados";

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function connect() {
  const list = await (await fetch(`http://127.0.0.1:${PORT}/json`)).json();
  const page = list.find((t) => t.type === "page" && t.url.startsWith("http://192.168.56.101")) || list.find((t) => t.type === "page");
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
  let id = 0;
  const pending = new Map();
  const events = [];
  ws.onmessage = (m) => {
    const d = JSON.parse(m.data);
    if (d.id && pending.has(d.id)) { pending.get(d.id)(d); pending.delete(d.id); }
    else if (d.method) {
      events.push(d);
      if (d.method === "Page.javascriptDialogOpening") {
        console.log(`[dialogo ${d.params.type}] ${d.params.message}`);
        send("Page.handleJavaScriptDialog", { accept: process.env.DISMISS ? false : true });
      }
      if (d.method === "Runtime.consoleAPICalled" && process.env.CONSOLE) {
        console.log(`[console.${d.params.type}] ` + d.params.args.map((a) => a.value ?? a.description ?? "").join(" "));
      }
      if (d.method === "Runtime.exceptionThrown") {
        console.log(`[excecao] ${d.params.exceptionDetails.text} ${d.params.exceptionDetails.exception?.description ?? ""}`);
      }
      if (d.method === "Page.downloadProgress" && d.params.state === "completed") console.log(`[download concluido] ${d.params.guid}`);
      if (d.method === "Page.downloadWillBegin") console.log(`[download] ${d.params.suggestedFilename} ${d.params.url}`);
    }
  };
  function send(method, params = {}) {
    return new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); })
      .then((d) => { if (d.error) throw new Error(`${method}: ${JSON.stringify(d.error)}`); return d.result; });
  }
  await send("Page.enable");
  await send("Runtime.enable");
  await send("Emulation.setDeviceMetricsOverride", { width: 1600, height: 1000, deviceScaleFactor: 1, mobile: false });
  fs.mkdirSync(DOWN, { recursive: true });
  await send("Page.setDownloadBehavior", { behavior: "allow", downloadPath: DOWN.replace(/\//g, "\\") }).catch(() => {});
  return { send, ws, events };
}

async function evaluate(c, expr) {
  const r = await c.send("Runtime.evaluate", { expression: expr, awaitPromise: true, returnByValue: true });
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
  return r.result.value;
}

async function mouse(c, type, x, y, extra = {}) {
  await c.send("Input.dispatchMouseEvent", { type, x, y, button: "left", buttons: type === "mouseReleased" ? 0 : 1, clickCount: 1, ...extra });
}
async function click(c, x, y, count = 1) {
  await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y });
  for (let i = 1; i <= count; i++) {
    await mouse(c, "mousePressed", x, y, { clickCount: i });
    await mouse(c, "mouseReleased", x, y, { clickCount: i });
    await sleep(60);
  }
}
async function center(c, sel) {
  const v = await evaluate(c, `(()=>{const e=document.querySelector(${JSON.stringify(sel)}); if(!e) return null; e.scrollIntoView({block:'center'}); const r=e.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}})()`);
  if (!v) throw new Error(`seletor não encontrado: ${sel}`);
  return v;
}
// posições dos nós do vis-network (coordenadas da página), lidas pela instância Vue (só leitura)
const NODEPOS = `(()=>{let el=document.querySelector('.vis-network'); let inst=el&&el.parentElement.__vueParentComponent; while(inst&&!(inst.proxy&&inst.proxy.network)) inst=inst.parent; if(!inst) return null; const n=inst.proxy.network; const rect=n.canvas.frame.canvas.getBoundingClientRect(); const p=n.getPositions(); const out={}; for(const k in p){const d=n.canvasToDOM(p[k]); out[k]={x:Math.round(rect.x+d.x),y:Math.round(rect.y+d.y)}} return out})()`;

const UTC = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
async function shot(c, label) {
  const ts = UTC();
  await evaluate(c, `(()=>{let d=document.getElementById('__carimbo'); if(!d){d=document.createElement('div'); d.id='__carimbo'; document.body.appendChild(d)} d.style.cssText='position:fixed;right:8px;bottom:8px;z-index:2147483647;background:#000c;color:#ff0;font:bold 14px monospace;padding:4px 8px;border-radius:4px;pointer-events:none'; d.textContent=${JSON.stringify(`captura ${ts} (UTC) | ${label}`)}})()`);
  await sleep(150);
  let r = await c.send("Page.captureScreenshot", { format: "png" });
  let buf = Buffer.from(r.data, "base64");
  let ext = "png";
  if (buf.length > 950_000) { r = await c.send("Page.captureScreenshot", { format: "jpeg", quality: 80 }); buf = Buffer.from(r.data, "base64"); ext = "jpg"; }
  await evaluate(c, `document.getElementById('__carimbo')?.remove()`);
  fs.mkdirSync(TELAS, { recursive: true });
  const name = `${ts.replace(/[-:]/g, "")}-${label}.${ext}`;
  fs.writeFileSync(path.join(TELAS, name), buf);
  const h = crypto.createHash("sha256").update(buf).digest("hex");
  fs.appendFileSync(path.join(TELAS, "telas.sha256"), `${h}  ${name}\n`);
  console.log(`[tela] ${name} ${buf.length} bytes sha256=${h}`);
}

async function keyChar(c, ch) {
  const special = { "\n": ["Enter", "Enter", 13, "\r"], "\t": ["Tab", "Tab", 9, "\t"], "\b": ["Backspace", "Backspace", 8, ""] };
  if (special[ch]) {
    const [key, code, vk, text] = special[ch];
    await c.send("Input.dispatchKeyEvent", { type: "keyDown", key, code, windowsVirtualKeyCode: vk, text });
    await c.send("Input.dispatchKeyEvent", { type: "keyUp", key, code, windowsVirtualKeyCode: vk });
    return;
  }
  await c.send("Input.dispatchKeyEvent", { type: "keyDown", key: ch, text: ch });
  await c.send("Input.dispatchKeyEvent", { type: "keyUp", key: ch });
}

const [cmd, ...a] = process.argv.slice(2);
const c = await connect();
try {
  switch (cmd) {
    case "nav": await c.send("Page.navigate", { url: a[0] }); await sleep(Number(a[1] || 3000)); break;
    case "reload": await c.send("Page.reload", {}); await sleep(Number(a[0] || 3000)); break;
    case "shot": await shot(c, a[0]); break;
    case "eval": console.log(JSON.stringify(await evaluate(c, a[0]), null, 1)); break;
    case "text": console.log(await evaluate(c, `(document.querySelector(${JSON.stringify(a[0] || "body")})||{}).innerText`)); break;
    case "click": { const p = await center(c, a[0]); await click(c, p.x, p.y); console.log(`[clique] ${a[0]} em ${Math.round(p.x)},${Math.round(p.y)}`); await sleep(Number(a[1] || 800)); break; }
    case "clickxy": await click(c, +a[0], +a[1], +(a[2] || 1)); await sleep(800); break;
    case "clicktab": { // clique real na aba do WebShell pelo nome do nó
      const p = await evaluate(c, `(()=>{const b=[...document.querySelectorAll(".tab-button")].find(b=>b.innerText.trim().toLowerCase()===${JSON.stringify(a[0].toLowerCase())}); if(!b) return null; const r=b.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}})()`);
      if (!p) throw new Error("aba ausente " + a[0]); await click(c, p.x, p.y); console.log(`[clique] aba ${a[0]} em ${Math.round(p.x)},${Math.round(p.y)}`); await sleep(Number(a[1] || 2000)); break;
    }
    case "clicktext": { // clique real no primeiro botão com o texto dado
      const p = await evaluate(c, `(()=>{const b=[...document.querySelectorAll("button")].find(b=>b.innerText.trim().includes(${JSON.stringify(a[0])})); if(!b) return null; const r=b.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}})()`);
      if (!p) throw new Error("botão ausente " + a[0]); await click(c, p.x, p.y); console.log(`[clique] botão "${a[0]}" em ${Math.round(p.x)},${Math.round(p.y)}`); await sleep(Number(a[1] || 1500)); break;
    }
    case "wheel": await c.send("Input.dispatchMouseEvent", { type: "mouseWheel", x: +a[0], y: +a[1], deltaX: 0, deltaY: +a[2] }); console.log(`[roda] ${a[2]} em ${a[0]},${a[1]}`); await sleep(1200); break;
    case "rawdrag": { const [x1, y1, x2, y2] = a.map(Number); await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: x1, y: y1 }); await mouse(c, "mousePressed", x1, y1);
      for (let i = 1; i <= 20; i++) { await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: x1 + (x2 - x1) * i / 20, y: y1 + (y2 - y1) * i / 20, button: "left", buttons: 1 }); await sleep(25); }
      await mouse(c, "mouseReleased", x2, y2); console.log(`[arraste da tela] ${x1},${y1} -> ${x2},${y2}`); await sleep(1200); break; }
    case "nodepos": console.log(JSON.stringify(await evaluate(c, NODEPOS))); break;
    case "clicknode": case "dblnode": {
      const pos = await evaluate(c, NODEPOS); const p = pos[a[0]]; if (!p) throw new Error("nó ausente " + a[0]);
      await click(c, p.x, p.y, cmd === "dblnode" ? 2 : 1); console.log(`[clique${cmd === "dblnode" ? " duplo" : ""}] nó ${a[0]} em ${p.x},${p.y}`); await sleep(1000); break;
    }
    case "clickedge": { // clica no ponto médio entre dois nós
      const pos = await evaluate(c, NODEPOS); const p = pos[a[0]], q = pos[a[1]];
      const x = Math.round((p.x + q.x) / 2), y = Math.round((p.y + q.y) / 2); await click(c, x, y); console.log(`[clique] aresta ${a[0]}-${a[1]} em ${x},${y}`); await sleep(800); break;
    }
    case "dragnode": case "mousedrag": { // dragnode <id> <dx> <dy> | mousedrag <idOrigem> <idDestino>
      const pos = await evaluate(c, NODEPOS); const p = pos[a[0]];
      const q = cmd === "dragnode" ? { x: p.x + +a[1], y: p.y + +a[2] } : pos[a[1]];
      await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: p.x, y: p.y });
      await mouse(c, "mousePressed", p.x, p.y);
      for (let i = 1; i <= 20; i++) { await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: p.x + (q.x - p.x) * i / 20, y: p.y + (q.y - p.y) * i / 20, button: "left", buttons: 1 }); await sleep(25); }
      await mouse(c, "mouseReleased", q.x, q.y);
      console.log(`[arraste] ${a[0]} ${p.x},${p.y} -> ${Math.round(q.x)},${Math.round(q.y)}`); await sleep(1500); break;
    }
    case "dnd": { // arraste HTML5 da paleta: dnd <seletor> <x> <y>
      const p = await center(c, a[0]); const x = +a[1], y = +a[2];
      await c.send("Input.setInterceptDrags", { enabled: true });
      const got = new Promise((r) => { const iv = setInterval(() => { const e = c.events.find((e) => e.method === "Input.dragIntercepted"); if (e) { clearInterval(iv); r(e.params.data); } }, 20); setTimeout(() => { clearInterval(iv); r(null); }, 5000); });
      await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: p.x, y: p.y });
      await mouse(c, "mousePressed", p.x, p.y);
      for (let i = 1; i <= 10; i++) await c.send("Input.dispatchMouseEvent", { type: "mouseMoved", x: p.x + (x - p.x) * i / 10, y: p.y + (y - p.y) * i / 10, button: "left", buttons: 1 });
      const data = await got;
      if (!data) throw new Error("arraste HTML5 não interceptado");
      await c.send("Input.dispatchDragEvent", { type: "dragEnter", x, y, data });
      await c.send("Input.dispatchDragEvent", { type: "dragOver", x, y, data });
      await c.send("Input.dispatchDragEvent", { type: "drop", x, y, data });
      await mouse(c, "mouseReleased", x, y);
      await c.send("Input.setInterceptDrags", { enabled: false });
      console.log(`[arraste html5] ${a[0]} -> ${x},${y} dados=${JSON.stringify(data.items)}`); await sleep(1500); break;
    }
    case "select": { // select <seletor> <valor>: igual ao selectOption de ferramentas de teste (valor + evento change)
      console.log(await evaluate(c, `(()=>{const e=document.querySelector(${JSON.stringify(a[0])}); e.focus(); e.value=${JSON.stringify(a[1])}; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true})); return e.value})()`)); await sleep(400); break;
    }
    case "fill": { const p = await center(c, a[0]); await click(c, p.x, p.y); await evaluate(c, `document.querySelector(${JSON.stringify(a[0])}).select?.()`); await c.send("Input.insertText", { text: a[1] }); console.log(`[digitado] ${a[0]} = ${a[1]}`); await sleep(300); break; }
    case "type": { const s = a[0].replace(/\\n/g, "\n"); for (const ch of s) { await keyChar(c, ch); await sleep(15); } console.log(`[teclas] ${JSON.stringify(s)}`); await sleep(Number(a[1] || 1000)); break; }
    case "ctrlc": await c.send("Input.dispatchKeyEvent", { type: "keyDown", key: "Control", code: "ControlLeft", windowsVirtualKeyCode: 17, modifiers: 2 });
      await c.send("Input.dispatchKeyEvent", { type: "keyDown", key: "c", code: "KeyC", windowsVirtualKeyCode: 67, modifiers: 2 });
      await c.send("Input.dispatchKeyEvent", { type: "keyUp", key: "c", code: "KeyC", windowsVirtualKeyCode: 67, modifiers: 2 });
      await c.send("Input.dispatchKeyEvent", { type: "keyUp", key: "Control", code: "ControlLeft", windowsVirtualKeyCode: 17 }); console.log("[teclas] Ctrl+C"); await sleep(1000); break;
    case "key": { const [key, code, vk] = a; await c.send("Input.dispatchKeyEvent", { type: "keyDown", key, code, windowsVirtualKeyCode: +vk }); await c.send("Input.dispatchKeyEvent", { type: "keyUp", key, code, windowsVirtualKeyCode: +vk }); await sleep(800); break; }
    case "wait": await sleep(Number(a[0])); break;
    default: throw new Error("comando desconhecido " + cmd);
  }
  await sleep(200);
} catch (e) { console.log("[erro] " + e.message); process.exitCode = 1; }
finally { c.ws.close(); }
