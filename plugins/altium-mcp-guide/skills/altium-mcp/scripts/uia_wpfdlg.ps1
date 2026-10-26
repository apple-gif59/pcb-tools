param([string]$Out, [string]$ClickName = '')
# Dump (and optionally Invoke a button in) the WPF dialog child window of the AD main window.
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$sb = New-Object System.Text.StringBuilder
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TDocumentForm')
$w = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
$kids = $w.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($k in $kids) {
  if ($k.Current.ClassName -ne 'Window') { continue }
  [void]$sb.AppendLine('DIALOG name=' + $k.Current.Name + ' rect=' + $k.Current.BoundingRectangle)
  $els = $k.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  foreach ($e in $els) {
    [void]$sb.AppendLine('  ' + $e.Current.ControlType.ProgrammaticName + ' | ' + $e.Current.ClassName + ' | name=' + $e.Current.Name + ' | aid=' + $e.Current.AutomationId)
    if ($ClickName -ne '' -and $e.Current.Name -eq $ClickName -and $e.Current.ControlType.ProgrammaticName -eq 'ControlType.Button') {
      $p = $e.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
      $p.Invoke()
      [void]$sb.AppendLine('  >>> INVOKED ' + $ClickName)
    }
  }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
