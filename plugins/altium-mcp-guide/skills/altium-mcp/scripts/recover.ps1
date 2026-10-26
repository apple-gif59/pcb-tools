param([string]$SandboxPas, [switch]$DryRun)
# Recovers the run_altium_script executor after a script error:
#   1. -REditScript:Stop stops the paused DelphiScript debugger;
#   2. runs closer\Closer.pas, which closes the Sandbox.pas editor tab AD opened at the error
#      (while that tab is open, AD keeps running the old script from memory).
# X2.EXE comes from the running AD process (the earliest-started one; an extra instance spawned
# by MCP starts later). Sandbox.pas comes from the running MCP server's command line
# (<repo>\server\main.py -> <repo>\server\SandboxScript\Sandbox.pas) unless -SandboxPas is given.
# Closer is generated into MCP's exchange dir, which AD can always read; result in closer_result.txt.
# -DryRun: resolve paths and generate Closer, but send nothing to AD.
$x2p = Get-Process X2 -ErrorAction SilentlyContinue | Sort-Object StartTime | Select-Object -First 1
if (-not $x2p) { 'X2 is not running'; exit 1 }
$x2 = $x2p.Path
if (-not $SandboxPas) {
  # the path that ends in \server\main.py; may contain spaces, must not run into the interpreter's path
  $rx = '([A-Za-z]:\\(?:(?![A-Za-z]:\\)[^"])*?)\\server\\main\.py'
  $mcp = Get-CimInstance Win32_Process -Filter "Name like 'python%'" | Where-Object { $_.CommandLine -match $rx } | Select-Object -First 1
  if (-not $mcp) { 'MCP server process not found; pass -SandboxPas <repo>\server\SandboxScript\Sandbox.pas'; exit 1 }
  [void]($mcp.CommandLine -match $rx)
  $SandboxPas = Join-Path $Matches[1] 'server\SandboxScript\Sandbox.pas'
}
$exchange = 'C:\Users\Public\altium_mcp'
$dir = Join-Path $exchange 'closer'
$res = Join-Path $exchange 'closer_result.txt'
New-Item -ItemType Directory -Force $dir | Out-Null
Copy-Item (Join-Path $PSScriptRoot 'closer\Closer.PrjScr') $dir -Force
$pas = (Get-Content (Join-Path $PSScriptRoot 'closer\Closer.pas') -Raw).Replace('@@SANDBOX@@', $SandboxPas).Replace('@@RESULT@@', $res)
Set-Content -Path (Join-Path $dir 'Closer.pas') -Value $pas -Encoding Default
if ($DryRun) { "x2=$x2"; "sandbox=$SandboxPas"; "closer=$dir\Closer.pas"; exit 0 }
Start-Process $x2 -ArgumentList '-REditScript:Stop'
Start-Sleep -Seconds 3
Remove-Item $res -ErrorAction SilentlyContinue
Start-Process $x2 -ArgumentList ('-RScriptingSystem:RunScript(ProjectName="' + $dir + '\Closer.PrjScr"|ProcName="Closer>Run")')
Start-Sleep -Seconds 4
Get-Content $res -ErrorAction SilentlyContinue
