param([string]$Out)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$root = [System.Windows.Automation.AutomationElement]::RootElement
$sb = New-Object System.Text.StringBuilder
$all = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($w in $all) {
  $p = $w.Current.ProcessId
  $proc = Get-Process -Id $p -ErrorAction SilentlyContinue
  if ($proc -and $proc.ProcessName -eq 'X2') {
    [void]$sb.AppendLine('TOP pid=' + $p + ' class=' + $w.Current.ClassName + ' name=' + $w.Current.Name + ' offscreen=' + $w.Current.IsOffscreen)
    $kids = $w.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
    foreach ($k in $kids) {
      if ($k.Current.ControlType.ProgrammaticName -eq 'ControlType.Window') {
        [void]$sb.AppendLine('   child window class=' + $k.Current.ClassName + ' name=' + $k.Current.Name)
      }
    }
  }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
