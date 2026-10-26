param([switch]$DryRun)
# Manual fallback for when run_altium_script reports executor_wedged: true (its own automatic
# recovery failed): sends -REditScript:Stop to the running AD to stop the paused DelphiScript debugger.
# altium-mcp v0.5.1 runs every script from a fresh file, so there is no stale editor tab to close.
# X2.EXE comes from the running AD process (the earliest-started one; an extra instance spawned
# by MCP starts later). Do not run it while a modal dialog is open: the command starts another X2.
# -DryRun: print the X2 path, send nothing to AD.
$x2p = Get-Process X2 -ErrorAction SilentlyContinue | Sort-Object StartTime | Select-Object -First 1
if (-not $x2p) { 'X2 is not running'; exit 1 }
$x2 = $x2p.Path
if ($DryRun) { "x2=$x2"; exit 0 }
Start-Process $x2 -ArgumentList '-REditScript:Stop'
Start-Sleep -Seconds 3
'stop sent; confirm with a two-line run_altium_script'
