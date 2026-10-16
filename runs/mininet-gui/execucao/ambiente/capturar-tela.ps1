# Captura a tela da VM com hora UTC no nome e registra o SHA-256 num manifesto.
# Uso no host: powershell -File capturar-tela.ps1 -Rotulo R1-topologia [-Vm "Mininet-GUI-VM-SBRC-2025"] [-Destino <pasta>]
param(
    [Parameter(Mandatory = $true)][string]$Rotulo,
    [string]$Vm = "Mininet-GUI-VM-SBRC-2025",
    [string]$Destino = (Join-Path $PSScriptRoot "..\evidencias\telas")
)
$ErrorActionPreference = "Stop"
$vbox = Join-Path $env:ProgramFiles "Oracle\VirtualBox\VBoxManage.exe"
New-Item -ItemType Directory -Force $Destino | Out-Null
$utc = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
$png = Join-Path (Resolve-Path $Destino) "$utc-$Rotulo.png"
& $vbox controlvm $Vm screenshotpng $png
if ($LASTEXITCODE -ne 0) { throw "screenshotpng falhou ($LASTEXITCODE)" }
$hash = (Get-FileHash -Algorithm SHA256 $png).Hash.ToLower()
# Formato do sha256sum; a hora UTC da captura está no próprio nome do arquivo.
$linha = "$hash  $(Split-Path -Leaf $png)"
Add-Content -Encoding utf8 -Path (Join-Path $Destino "telas.sha256") -Value $linha
$linha
