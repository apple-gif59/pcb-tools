param([Parameter(Mandatory = $true)][string]$Dwg, [Parameter(Mandatory = $true)][string]$Out, [string]$AcCore)
# DWG -> <Out>\outline.dxf (DXFOUT) and <Out>\hatchlines.txt (every HATCH exploded; the pattern lines
# AutoCAD draws, keyed by the hatch handle). Both runs work on copies of the DWG in <Out>, so the
# original is never opened. The handles in hatchlines.txt match the HATCH entities in outline.dxf.
# accoreconsole: -AcCore, else the newest 'C:\Program Files\Autodesk\AutoCAD *\accoreconsole.exe'.
$ErrorActionPreference = 'Stop'
if (-not $AcCore) {
  $AcCore = Get-ChildItem 'C:\Program Files\Autodesk\AutoCAD *\accoreconsole.exe' -ErrorAction SilentlyContinue |
    Sort-Object FullName | Select-Object -Last 1 -ExpandProperty FullName
  if (-not $AcCore) { 'accoreconsole.exe not found; pass -AcCore <path>'; exit 1 }
}
New-Item -ItemType Directory -Force $Out | Out-Null
$Out = (Resolve-Path $Out).Path
if ($Out -match '[^\x20-\x7E]') { "the output folder path must be ASCII (it is written into the .scr): $Out"; exit 1 }
$fwd = $Out.Replace('\', '/')
Copy-Item -LiteralPath $Dwg (Join-Path $Out 'input.dwg') -Force
Copy-Item -LiteralPath $Dwg (Join-Path $Out 'explode.dwg') -Force
foreach ($f in 'outline.dxf', 'hatchlines.txt') { Remove-Item (Join-Path $Out $f) -ErrorAction SilentlyContinue }

# 1) DXFOUT, 16 decimal places
@"
FILEDIA 0
DXFOUT
"$fwd/outline.dxf"
16
QUIT
Y
"@ | Set-Content -Encoding ASCII (Join-Path $Out 'todxf.scr')
# 2) explode every HATCH; the LISP is inlined in the .scr because (load ...) from an untrusted folder is blocked by SECURELOAD
(Get-Content (Join-Path $PSScriptRoot 'explode_hatches.scr') -Raw).Replace('@@OUT@@', "$fwd/hatchlines.txt") |
  Set-Content -Encoding ASCII (Join-Path $Out 'explode.scr')

& $AcCore /i (Join-Path $Out 'input.dwg') /s (Join-Path $Out 'todxf.scr') | Out-File -Encoding utf8 (Join-Path $Out 'todxf.log')
& $AcCore /i (Join-Path $Out 'explode.dwg') /s (Join-Path $Out 'explode.scr') | Out-File -Encoding utf8 (Join-Path $Out 'explode.log')
foreach ($f in 'outline.dxf', 'hatchlines.txt') {
  $p = Join-Path $Out $f
  if (-not (Test-Path $p)) { "$f was not written; see todxf.log / explode.log"; exit 1 }
  "$p  $((Get-Item $p).Length) bytes"
}
