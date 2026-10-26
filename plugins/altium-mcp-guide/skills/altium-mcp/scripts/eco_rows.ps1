param([string]$Out)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TChangeManagementForm')
$dlg = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
$sb = New-Object System.Text.StringBuilder
$gc = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TdxTreeList')
$grid = $dlg.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $gc)
$walker = [System.Windows.Automation.TreeWalker]::RawViewWalker
function Walk($el, $depth) {
  $ch = $walker.GetFirstChild($el)
  while ($ch -ne $null) {
    if ($ch.Current.ClassName -like 'TdxTreeList*Node') {
      $v = ''
      try { $vp = $ch.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern); $v = $vp.Current.Value } catch {}
      $sel = ''
      try { $sp = $ch.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern); $sel = $sp.Current.IsSelected } catch {}
      $ec = ''
      try { $ep = $ch.GetCurrentPattern([System.Windows.Automation.ExpandCollapsePattern]::Pattern); $ec = $ep.Current.ExpandCollapseState } catch {}
      $r = $ch.Current.BoundingRectangle
      $rs = 'off'
      if (-not $r.IsEmpty -and -not [double]::IsInfinity($r.X)) { $rs = [string][math]::Round($r.X) + ',' + [math]::Round($r.Y) + ',' + [math]::Round($r.Width) + ',' + [math]::Round($r.Height) }
      [void]$sb.AppendLine(('  ' * $depth) + '[' + $ec + '|sel=' + $sel + '|rect=' + $rs + '] ' + $v)
      Walk $ch ($depth + 1)
    }
    $ch = $walker.GetNextSibling($ch)
  }
}
Walk $grid 0
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
