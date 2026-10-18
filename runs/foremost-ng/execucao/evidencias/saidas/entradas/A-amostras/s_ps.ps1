#!/usr/bin/env pwsh
Get-ChildItem -Path . | ForEach-Object { $_.Name }
