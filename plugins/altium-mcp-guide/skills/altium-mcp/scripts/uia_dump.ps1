param([string]$Out, [string]$Class = '', [string]$Title = '')
# Dump all descendants of the top-level X2 windows matching Class and/or Title (empty = any non-main window)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$sb = New-Object System.Text.StringBuilder
$all = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($w in $all) {
  $p = $w.Current.ProcessId
  $proc = Get-Process -Id $p -ErrorAction SilentlyContinue
  if (-not $proc -or $proc.ProcessName -ne 'X2') { continue }
  if ($Class -ne '' -and $w.Current.ClassName -ne $Class) { continue }
  if ($Title -ne '' -and $w.Current.Name -ne $Title) { continue }
  if ($Class -eq '' -and $Title -eq '' -and $w.Current.ClassName -eq 'TDocumentForm') { continue }
  [void]$sb.AppendLine('WINDOW pid=' + $p + ' class=' + $w.Current.ClassName + ' name=' + $w.Current.Name)
  $els = $w.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  foreach ($e in $els) {
    $v = ''
    try { $v = $e.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).Current.Value } catch {}
    $t = ''
    try { $t = [string]$e.GetCurrentPattern([System.Windows.Automation.TogglePattern]::Pattern).Current.ToggleState } catch {}
    $r = $e.Current.BoundingRectangle
    $rs = 'off'
    if (-not $r.IsEmpty -and -not [double]::IsInfinity($r.X)) { $rs = [string][math]::Round($r.X) + ',' + [math]::Round($r.Y) + ',' + [math]::Round($r.Width) + ',' + [math]::Round($r.Height) }
    [void]$sb.AppendLine('  ' + $e.Current.ControlType.ProgrammaticName + ' | ' + $e.Current.ClassName + ' | name=' + $e.Current.Name + ' | value=' + $v + ' | toggle=' + $t + ' | enabled=' + $e.Current.IsEnabled + ' | rect=' + $rs + ' | hwnd=' + $e.Current.NativeWindowHandle)
  }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
