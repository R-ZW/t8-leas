# Ambiente da execução de referência — Mininet-GUI

**Preparado em:** 15/10/2026 (horário de Brasília), 2026-10-16T01:50Z–02:06Z. **Executor:** agente Claude Code (modelo Opus 5.5), com autorização do aluno para as decisões e os downloads. **Escopo:** obter e preparar a VM dos autores. O teste mínimo e as reivindicações **não** foram executados; `mininet_gui`, `run.sh`, `mn` (exceto `mn --version`) e `pingall` não foram rodados.

## Resumo

| Item | Valor |
|---|---|
| ZIP da VM | `Mininet-GUI-VM-SBRC-2025.zip`, 1.303.516.409 bytes, SHA-256 `3a484c2da5034484ab1cbc5aa86245d952257a9eb6b5b672b956e40d5364e4bc` |
| OVA extraída | `Mininet-GUI-VM-SBRC-2025.ova`, 1.330.363.392 bytes, SHA-256 `9018352deec76c1ef47b15c0d6b7155fbd7ed090d34e8f97a0a302d299fc7455` |
| VirtualBox | 7.1.6 r167084 (versão pedida pelo README; sem desvio D1) |
| Motor de execução | Hyper-V/NEM ("Snail execution mode"), pois o VT-x não está disponível com o Hyper-V ativo |
| VM ajustada | 8192 MB, 2 vCPUs, rede host-only `192.168.56.101` |
| SO da VM | Ubuntu 20.04.1 LTS, kernel 5.4.0-42-generic |
| **Commit do código na VM** | **`be68302a9d3e17acf740d002090f7191098ac03d`** (branch `sbrc2025`, `v0.0.1-2-gbe68302`, árvore limpa) |
| Relação com as referências | ≠ proxy `465648a4…` (16 commits antes dele) e ≠ tag `v0.0.1` `4a5d5764…` (2 commits depois dela) |

## 1. Obtenção da VM

| Item | Valor |
|---|---|
| Consulta à API | `https://api.github.com/repos/latarc/mininet-gui/releases/tags/v0.0.1`, 2026-10-16T01:50:30Z (JSON salvo como `release-v0.0.1-api.json`, SHA-256 `dee79ef34a7a632fbc363d8956afe1d6ac7b181e97902d6df0171140e34b7fe0`) |
| Release | "VM SBRC 2025", `prerelease: true`, criada em 2025-03-17T14:04:28Z, publicada em 2025-03-17T14:11:18Z, `target_commitish: sbrc2025` |
| Asset | id 238275228, `Mininet-GUI-VM-SBRC-2025.zip`, `size: 1303516409`, criado em 2025-03-17T17:29:53Z, `digest: null` (o GitHub não publica hash) |
| URL baixada | `https://github.com/latarc/mininet-gui/releases/download/v0.0.1/Mininet-GUI-VM-SBRC-2025.zip` (`browser_download_url` da API) |
| Download | 2026-10-16T01:50:40Z–01:57:20Z. Foi iniciado com `curl` sequencial em segundo plano, que caiu para 60–230 KiB/s por conexão. Ele foi interrompido em 212.201.472 bytes e o restante foi baixado em 12 intervalos de bytes paralelos ([`baixar-vm-segmentado.sh`](baixar-vm-segmentado.sh)), anexados ao parcial. |
| Tamanho obtido | 1.303.516.409 bytes, igual ao `size` da API |
| SHA-256 do ZIP | `3a484c2da5034484ab1cbc5aa86245d952257a9eb6b5b672b956e40d5364e4bc` |
| Integridade do ZIP | `unzip -t`: "No errors detected" (CRC-32 `cbd587c8` confere, o que valida a concatenação dos segmentos) |
| Conteúdo do ZIP | um arquivo: `Mininet-GUI-VM-SBRC-2025.ova`, data interna 2025-03-17 14:15 |
| SHA-256 da OVA | `9018352deec76c1ef47b15c0d6b7155fbd7ed090d34e8f97a0a302d299fc7455` (1.330.363.392 bytes) |
| Manifesto interno da OVA | [`ova-manifesto.mf.txt`](ova-manifesto.mf.txt): SHA-1 do VMDK `f50e8c54…c43139` e do OVF `8cfc3990…c27ea`. Os dois **conferem** com o recalculado. |
| Quem gerou a OVA | membros do tar com dono `vboxovf10/vbox_v7.1.6r167084`, datados de 2025-03-17 14:12–14:15. O próprio VirtualBox 7.1.6 r167084 exportou a OVA. |
| Descritor | [`ova-descritor.ovf.txt`](ova-descritor.ovf.txt) (OVF original) |

Local externo: `D:\Lab-artefatos\t8-mininet-vm\` (`download\`, `ova\`, `vms\`, `clone-mininet-gui\`, `comparacao\`). Os links do Google Drive (release e README) não foram usados; o estado deles está em [`../../versao.md`](../../versao.md).

## 2. VirtualBox no host

| Item | Valor |
|---|---|
| Host | Windows 11 Home build 26300, i5-13450HX (10 núcleos, 16 lógicos), 16.068 MB de RAM |
| Instalador | `https://download.virtualbox.org/virtualbox/7.1.6/VirtualBox-7.1.6-167084-Win.exe`, 123.016.232 bytes, SHA-256 `35c42c98b784974a965c358a9bda63b6cb4edde80db83f87daa2fee83e6cfad6`. Confere com o `SHA256SUMS` oficial da Oracle para 7.1.6 e tem assinatura Authenticode válida de "Oracle America, Inc.". O winget também lista 7.1.6, mas foi usado o site oficial para conferir o hash. |
| Instalação | `--silent --ignore-reboot --msi-log-file …` com elevação (UAC aprovado pelo usuário), código de saída 0, às 22:52 (-03). `VBoxManage --version` = `7.1.6r167084`. |
| Incidente | Na primeira partida (2026-10-16T01:59:31Z), a VM terminou com código 1. O `VBoxHardening.log` registrou `NtCreateFile(\Device\VBoxDrvStub) failed: 0xc0000034 STATUS_OBJECT_NAME_NOT_FOUND`, porque o driver `vboxsup` estava instalado mas parado (`sc query`: STOPPED, 1077). Não havia bloqueio de integridade de código registrado. O driver tem assinatura WHQL válida. Ele foi iniciado com `sc.exe start vboxsup`, em uma segunda elevação (UAC). Nenhuma configuração de segurança foi alterada. |
| Segurança do Windows | VBS e HVCI (Integridade da Memória) **continuam ativos**; o Hyper-V continua ligado (`HypervisorPresent=True`; Docker Desktop/WSL2 em uso por outras sessões) |
| Motor | `HM: HMR3Init: Attempting fall back to NEM: VT-x is not available` → `NEM: NEMR3Init: Snail execution mode is active!`. A VM roda **sobre a API do Hyper-V (NEM)**, com X2APIC rebaixado para APIC. Trechos em [`vbox-boot-identificacao-trechos.txt`](vbox-boot-identificacao-trechos.txt); log integral fora do repositório (`VBox-boot-identificacao.txt`, SHA-256 `04c32bb74b841b6f213429256df6a8fec5177f22bd7a4b04bbc9328b35750338`). |
| Lentidão observada | No boot de identificação, a BIOS chegou ao disco em 7 s e as Guest Additions se apresentaram em 34 s. O DHCP concedeu o IP cerca de 32 s após a partida, e o login em tty1 já estava disponível na captura de 74 s. Os comandos de identificação via SSH responderam sem atraso perceptível. Ainda não foi medido o desempenho com Mininet, OVS e frontend rodando, que é a carga em que o modo NEM tende a pesar. |

**Desvio D1:** não se aplica, pois a versão é exatamente a pedida. **Diferença de ambiente (registrar na execução):** a VM roda em NEM sobre o Hyper-V, não em VT-x nativo. O host de referência dos autores (README) era um i5-10300H com 8 GB e Windows 11; o README não diz se o Hyper-V estava ativo.

## 3. Configuração da VM

| Item | Como importada (OVA) | Ajustada | Motivo |
|---|---|---|---|
| Nome | `Mininet-GUI-VM-SBRC-2025` | igual | — |
| Tipo de SO | Ubuntu (64-bit) | igual | — |
| RAM | **1536 MB** | **8192 MB** | README, "Dependências": "Mínimo de 8GB para a máquina virtual". O valor da OVA é menor que os 8 GB e também que os 2 GB da seção "Experimentos". |
| vCPUs | 1 | 2 | pedido da preparação (≥ 2); o README pede "um core de CPU reservado à VM" |
| Rede (nic1) | Bridged → `Intel(R) Wi-Fi 6 AX201 160MHz`, Intel 82545EM, MAC `08:00:27:0A:5F:67` | **Host-only** → `VirtualBox Host-Only Ethernet Adapter` (192.168.56.1/24, DHCP 192.168.56.101–254), mesmo MAC e mesma placa | O adaptador homônimo existe neste host, mas está **desligado** (169.254.x). Com host-only, o host alcança a VM sem expô-la à LAN, e o endereço segue o exemplo `http://192.168.56.101:5173` do texto da release. Não há acesso à Internet nesta rede. |
| Disco | VMDK streamOptimized de 8 GiB (8.589.934.592 bytes), controladora SCSI LsiLogic | igual (com diferencial de snapshot) | — |
| Vídeo | VBoxVGA, 16 MB, sem 3D | igual | — |
| Firmware | BIOS | igual | — |
| USB / áudio | USB ligado / áudio desligado | igual | — |
| Pasta da VM | — | `D:\Lab-artefatos\t8-mininet-vm\vms\Mininet-GUI-VM-SBRC-2025\` | fora do repositório |

Saídas completas: [`vminfo-importada.txt`](vminfo-importada.txt) e [`vminfo-ajustada.txt`](vminfo-ajustada.txt) (`showvminfo --machinereadable`).

**Snapshots:**

| Nome | Estado |
|---|---|
| `00-importada-original` | configuração da OVA sem alteração (1536 MB, 1 vCPU, bridged) |
| `01-configurada-antes-do-boot` | 8192 MB, 2 vCPUs, host-only; **disco nunca iniciado** |
| `02-apos-identificacao` (atual) | depois do boot de identificação, desligada por `poweroff` |

**Recursos do host no boot:** o `VBox.log` registrou `Host RAM: 16068MB (15.6GB) total, 38MB available`. O host tinha um jogo, Discord, Steam, GitHub Desktop e várias instâncias do Claude abertos, e o commit livre do Windows era de cerca de 7,3 GB antes da partida. A VM iniciou mesmo assim (o convidado usava 76 MB de 7962 MB). Com 8 GB realmente ocupados durante os experimentos, o host vai paginar. Liberar memória antes da execução cabe ao usuário; nenhum programa foi fechado.

## 4. Identificação dentro da VM

**Acesso:** por SSH (`openssh-server` ativo no convidado) a `mininet@192.168.56.101`, com a senha padrão publicada pelos autores no README e na release (`mininet`/`mininet`). O `VBoxManage guestcontrol` não funciona: as Guest Additions são o pacote `6.1.6_Ubuntu r137129`, em runlevel 1 e sem o VBoxService. Impressões digitais da chave do host (gravadas em `known_hosts-vm`, fora do repositório):

- ED25519 `SHA256:yECEW93f6TS4v1axnqUGFZseXGEUuR90hOVFaqU1onQ`
- ECDSA `SHA256:WHNG8y7ZEefMoCqpD4m/A9xl0pPg0T/WUf+ygK44nZg`
- RSA `SHA256:Y8HnUUlRUJxRZmkRaPoUeE09A4/U3/I4MZ0AS+n53mI`

Script: [`identificar-vm.sh`](identificar-vm.sh), que só faz leitura. Saídas: [`identificacao-vm.txt`](identificacao-vm.txt) (2026-10-16T02:02:53Z) e os complementos [`-1`](identificacao-vm-complemento-1.txt), [`-2`](identificacao-vm-complemento-2.txt) e [`-3`](identificacao-vm-complemento-3.txt). No complemento 1, os itens que dependiam de `$P` falharam por não exportar a variável; o complemento 2 repete esses itens.

| Comando ("Como confirmar", `versao.md`) | Resultado |
|---|---|
| `git -C /home/mininet/mininet-gui rev-parse HEAD` | `be68302a9d3e17acf740d002090f7191098ac03d` ("update setup and run scripts", 2025-03-17 09:53:46 -0700, schneider8357) |
| `git … status --short` | vazio (árvore limpa); `stash list` vazio |
| `git … remote -v` | `origin https://github.com/latarc/mininet-gui` (fetch/push) |
| `git … describe --tags --always` | `v0.0.1-2-gbe68302` |
| Branch atual / refs remotas na VM | `sbrc2025`; `origin/sbrc2025` = `be68302…`, `origin/main` = `4dbb7bd…`, `origin/dev` = `cc896929…`, `v0.0.1` = `4a5d5764…` (sem `FETCH_HEAD`: clone de 17/03/2025 nunca atualizado) |
| `command -v mininet_gui` | vazio em shell não interativo (saída 127) |
| Alvo do lançador | alias em `~/.bashrc`, linha 123: `alias mininet_gui=/home/mininet/mininet-gui/run.sh`. Em shell interativo, `type mininet_gui` mostra esse alias. `run.sh`: 924 bytes, SHA-256 `25b467af6f7152061657a10157245d77010a06a63602fb64ba653a5b11645ad0`, conteúdo integral no complemento 2. |

| Componente | Versão |
|---|---|
| SO | Ubuntu 20.04.1 LTS (focal), hostname `mininet-vm` |
| Kernel | `Linux 5.4.0-42-generic #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020 x86_64` |
| Mininet | `mn --version` → 2.3.0 (pip: `mininet 2.3.0`) |
| Open vSwitch | `ovs-vsctl (Open vSwitch) 2.13.1`, DB Schema 8.2.0 |
| Python | 3.8.5 (`/usr/bin/python3`), pip 20.0.2 |
| Backend (pip) | fastapi 0.115.11, uvicorn 0.33.0, starlette 0.44.0, pydantic 2.10.6, websockets 13.1. O `requirements.txt` não fixa versões. |
| Node | **dois:** sistema `v10.19.0` (npm 6.14.4) em shell não interativo; **`v18.20.7`** (npm 10.8.2) via nvm, padrão em shell interativo (`~/.bashrc` carrega o nvm) |
| Frontend | `node_modules` presente; vite 4.5.9, vue 3.5.13 |
| Outros | git 2.25.1; `script`/`scriptreplay` do util-linux 2.34; sem `ryu-manager`; `sudo` sem senha para `mininet` |
| Relógio | fuso `America/Los_Angeles` (PDT, -0700), UTC correto, mas `System clock synchronized: no`. Usar sempre UTC nos registros. |
| Recursos vistos | 7962 MB de RAM, 352 MB de swap, 2 CPUs, `/` com 7,4 GB (3,2 GB livres), `eth0` = 192.168.56.101/24 |

**Efeitos da identificação no disco da VM:**

- O `git status` regravou `.git/index`, e o mtime de `.git/` passou a 2026-10-15 19:02:53 -0700.
- Houve logins SSH.
- O diretório `~/evidencias` do teste de gravação foi criado e removido, assim como os scripts em `/tmp`.
- `run.sh` não foi executado. Por isso não existem `mininet-gui-frontend/.env` nem `nohup.out`.

O snapshot `01-configurada-antes-do-boot` guarda o disco sem nenhuma dessas alterações.

## 5. Comparação do código

O manifesto SHA-256 dos 41 arquivos do projeto na VM foi gerado sem `.git`, `node_modules`, `venv`, `dist` e `__pycache__`. Ele foi comparado com árvores do clone `D:\Lab-artefatos\t8-mininet-vm\clone-mininet-gui` (extraídas com `git -c core.autocrlf=false archive`) e com o `pacote/artefato.zip`. Script: [`comparar-codigo.py`](comparar-codigo.py). Saída: [`comparacao-codigo.txt`](comparacao-codigo.txt).

| VM comparada com | Iguais | Diferentes | Só na referência |
|---|---|---|---|
| `be68302a…` (HEAD da VM) | **41/41** | 0 | 0 |
| tag `v0.0.1` `4a5d5764…` | 38 | `README.md`, `run.sh`, `setup.sh` | 0 |
| proxy `465648a4…` | 39 | `README.md`, `run.sh` | `example_network_export.json`, `example_network_export.py` |
| `pacote/artefato.zip` (bytes brutos) | 5 | 36 | os 2 exemplos |
| `pacote/artefato.zip` com CRLF→LF nos arquivos de texto | 39 | `README.md`, `run.sh` | os 2 exemplos |

Fatos que explicam a tabela:

- `be68302` existe no repositório público (branches `main` e `sbrc2025`). Ele é ancestral de `465648a4`: há 16 commits entre os dois, e `be68302` vem 2 commits depois da tag.
- `git diff --stat be68302 465648a4`: `README.md` (+75/−17), `example_network_export.json` (novo), `example_network_export.py` (novo) e `run.sh` (2 linhas). **Nenhum arquivo de `mininet-gui-backend/` ou `mininet-gui-frontend/` muda** entre o commit da VM e o proxy.
- `run.sh` da VM × proxy: o proxy acrescenta `nvm use 18.20.7 ;` antes de `nohup npm run dev &` e um fim de linha final. Na VM, o Node 18 vem do nvm carregado pelo `~/.bashrc` em shell interativo.
- tag × VM: `run.sh` e `setup.sh` passam a usar o caminho fixo `/home/mininet/mininet-gui`, e o `setup.sh` passa a gravar o alias `mininet_gui` no `~/.bashrc`.
- `pacote/artefato.zip` (comentário do ZIP: `465648a4425a4457af0348ab951cf7f71d37a86f`) é a árvore de `465648a4` com fins de linha CRLF. Com EOL normalizado, `diff -rq --strip-trailing-cr` contra o `git archive` de `465648a4` não acusa nenhuma diferença.

O código instalado na VM é exatamente o do commit `be68302`, com o `.git` presente e a árvore limpa. Isso identifica o software **desta OVA (release v0.0.1, ZIP de 17/03/2025)**. Não mostra qual checkout o CTA examinou.

## 6. Plano de captura de evidências da execução futura

1. **Estado inicial.** Restaurar um snapshot conhecido antes de começar (`VBoxManage snapshot Mininet-GUI-VM-SBRC-2025 restore 01-configurada-antes-do-boot`, ou `02-…`) e registrar qual foi usado. O `run.sh` executa `sudo pkill`, grava `.env` e `nohup.out`, então cada tentativa altera o disco. Antes de partir, anotar a RAM livre do host.
2. **Partida.** Usar `VBoxManage startvm Mininet-GUI-VM-SBRC-2025 --type headless` (ou `--type gui`, se for preciso interagir no console) e guardar o `Logs\VBox.log` da sessão. O log vai com extensão `.txt` ao ir para o repositório, porque `*.log` é ignorado.
3. **Terminal.** Enviar [`gravar-sessao.sh`](gravar-sessao.sh) para a VM e rodar `sh gravar-sessao.sh <rotulo>` (ex.: `teste-minimo`, `R1`) para cada bloco.
   - O script usa `script -q -t<arquivo>.tempo` do util-linux 2.34 e gera, em `~/evidencias/`, `<UTC>-<rotulo>.terminal`, `.tempo` e `.sha256`. Nenhum nome termina em `.log`.
   - Carrega o `~/.bashrc` normal, com o alias `mininet_gui` e o nvm/Node 18, e troca só o prompt por um com data e hora: `[AAAA-MM-DDTHH:MM:SS-0700] mininet@mininet-vm:~$`.
   - Reprodução: `scriptreplay -t X.tempo X.terminal`. O script foi testado pela SSH com `ssh -tt`. A gravação de teste e o arquivo de tempo foram transferidos e conferidos, e depois apagados da VM.
4. **Telas da VM.** No host, `powershell -File capturar-tela.ps1 -Rotulo <rotulo>` grava `<UTC>-<rotulo>.png` (via `VBoxManage controlvm … screenshotpng`, que funciona em headless) e acrescenta a linha `sha256sum` a `telas.sha256`. Testado: [`telas/20261016T020211Z-boot2.png`](telas/20261016T020211Z-boot2.png).
5. **Telas da interface web.** A VM só tem console (tty1, sem ambiente gráfico). O texto da release manda abrir a URL impressa pelo `run.sh` num navegador; com host-only, isso é feito no navegador do host em `http://192.168.56.101:5173`, e o backend fica em `:8000`. Capturar essas telas no host, com a hora no nome ou na barra de tarefas visível, e registrar o SHA-256 da mesma forma. O README do proxy (VM "Desktop", Drive morto) usa o navegador **dentro** da VM. Essa diferença deve ser registrada.
6. **Transferência.** No host, rodar `bash transferir-evidencias.sh <pasta-destino>` ([`transferir-evidencias.sh`](transferir-evidencias.sh)). O script gera `manifesto-convidado.sha256` na VM, copia `~/evidencias` com `scp -p` e confere com `sha256sum -c` no host. Testado com sucesso (3/3 OK). Não usa `guestcontrol`, que não está disponível.
7. **Fins de linha.** Os scripts aqui estão em LF, e o `.gitattributes` da raiz não cobre `runs/*/execucao/ambiente/`. Se houver checkout com `core.autocrlf=true`, converter os `.sh` para LF antes de enviá-los à VM.

## 7. Pendências e riscos para a execução

- **RAM do host:** no boot havia 38 MB disponíveis. Fechar programas (jogo, Steam, Discord etc.) ou registrar a pressão de memória durante a execução.
- **NEM ("Snail mode"):** registrar os tempos observados nos experimentos. A comparação com VT-x nativo não é possível neste host sem desligar o Hyper-V, o que não foi feito.
- **Sem Internet na VM** (host-only). O `run.sh` não baixa nada; se algum passo precisar de rede, acrescentar uma nic2 NAT e registrar a mudança.
- **Dois Node.js:** o `mininet_gui` funciona como esperado só em shell interativo (alias + nvm). O `gravar-sessao.sh` cobre esse caso.
- **Credenciais padrão** (`mininet`/`mininet`, `sudo` sem senha) e SSH aberto apenas na rede host-only do host.

## 8. Arquivos

Nesta pasta (SHA-256):

```
8fd106d95ed5c4ff5516de15042faddba3d290bf0db21eb78716919b2f5af5ad  baixar-vm-segmentado.sh
8e14d7c8358e0cdd7414cebb4958859d996368dac0d8d4257ffdcb12b06fb60a  capturar-tela.ps1
6d199e4f3928c853a10c79a6081551905ec1646b7d54e12fe05015807e0df62f  comparacao-codigo.txt
1d0c4d79406474539eff9a7b498a639ac26fbb52a4f2a1d0958ad47232c49604  comparar-codigo.py
0152abc817c898e0435fdc944b45c06a47887f00d317adf29ec1d1c35455104b  gravar-sessao.sh
7d73f3879bb62b927552131fbdd74b7c7994feaff673dc41791582fda6acd0eb  identificacao-vm-complemento-1.txt
4f3d201f7f240818d8c4b7aed8522975a4d4bb62ca383a00b9495ed5d98311b1  identificacao-vm-complemento-2.txt
24fe4b82f205850d21a18799310ace544d23154ed29a0bd34aa227a62c8f79f8  identificacao-vm-complemento-3.txt
b9ecf44eea360c36132e88a30aebac65d2ca03f3a8496462b5290a318cb8a17b  identificacao-vm.txt
f63ebc1262e7e6d4dc1f18b70dcdf4a4f27c87777396b2ec85401fcb245901bb  identificar-vm.sh
c6997a3ab3ee2bca1667ffcb1815dc3879bdbedeb7cc5b623a96992734758c18  ova-descritor.ovf.txt
7e8cb50d0bf460c2e80d3907cb4a8c8c44a6b2cf16306746ea59f22f51d1084b  ova-manifesto.mf.txt
3026fb9efa85837a3e181698b6a41a20542ee66f8ee875a1ed893d163c89fe32  telas/20261016T020211Z-boot2.png
e5ea49ab5a501adf443b445f2996a5ba49633e1b1038c40fe1f4ae061501e557  transferir-evidencias.sh
fbe3afe5f19e6cd858b569fb6207deef984c694ecf8277890d2dd50730fd9172  vbox-boot-identificacao-trechos.txt
e4deca064527488bf467154a37546ebc2b9fe5524b04ec27b5137e89790e7209  vminfo-ajustada.txt
1e78cc9697a4e8383504b08e85d4d78085ee3440650a19ebab686632bb0b361a  vminfo-importada.txt
```

Fora do repositório, em `D:\Lab-artefatos\t8-mininet-vm\`, ficam o ZIP, a OVA, o instalador do VirtualBox com o `SHA256SUMS` da Oracle, a VM com seus snapshots, o clone, as árvores de comparação, o log integral do boot e o `known_hosts-vm`. Os hashes desses arquivos estão em `hashes-preparacao.sha256` e em `zip.sha256`/`ova.sha256`.
