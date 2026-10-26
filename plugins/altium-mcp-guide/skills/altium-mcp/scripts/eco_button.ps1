param([string]$Out, [string]$Button)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TChangeManagementForm')
$dlg = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
if ($dlg -eq $null) { [System.IO.File]::WriteAllText($Out, 'ECO dialog not found'); exit }
$bc = New-Object System.Windows.Automation.PropertyCondition($A::NameProperty, $Button)
$b = $dlg.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $bc)
if ($b -eq $null) { [System.IO.File]::WriteAllText($Out, 'button not found'); exit }
$b.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
[System.IO.File]::WriteAllText($Out, 'invoked ' + $Button)
