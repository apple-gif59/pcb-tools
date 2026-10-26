param([string]$Out, [string]$Pattern, [string]$Class = 'TDocumentForm')
# Search all descendants of the top-level X2 window(s) of class $Class for elements whose Name or Value matches $Pattern (regex).
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$sb = New-Object System.Text.StringBuilder
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, $Class)
$ws = $root.FindAll([System.Windows.Automation.TreeScope]::Children, $cond)
foreach ($w in $ws) {
  $els = $w.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  foreach ($e in $els) {
    $n = $e.Current.Name
    $v = ''
    try { $v = $e.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).Current.Value } catch {}
    if (($n -match $Pattern) -or ($v -match $Pattern)) {
      $r = $e.Current.BoundingRectangle
      [void]$sb.AppendLine($e.Current.ControlType.ProgrammaticName + ' | ' + $e.Current.ClassName + ' | name=' + $n + ' | value=' + $v + ' | rect=' + $r)
    }
  }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
