param([string]$Out, [string]$Class = '', [string]$Title = '', [string]$Button, [switch]$Toggle)
# Invoke (or toggle) the named control inside a top-level X2 window matched by Class and/or Title.
# Falls back to BM_CLICK for plain TButton/TCheckBox controls that do not support Invoke/Toggle.
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class W32c { [DllImport("user32.dll")] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l); }
'@
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$res = 'window not found'
$all = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($w in $all) {
  $proc = Get-Process -Id $w.Current.ProcessId -ErrorAction SilentlyContinue
  if (-not $proc -or $proc.ProcessName -ne 'X2') { continue }
  if ($Class -ne '' -and $w.Current.ClassName -ne $Class) { continue }
  if ($Title -ne '' -and $w.Current.Name -ne $Title) { continue }
  $bc = New-Object System.Windows.Automation.PropertyCondition($A::NameProperty, $Button)
  $b = $w.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $bc)
  if ($b -eq $null) { $res = 'control not found'; continue }
  $done = $false
  if ($Toggle) {
    try { $b.GetCurrentPattern([System.Windows.Automation.TogglePattern]::Pattern).Toggle(); $done = $true; $res = 'toggled ' + $Button } catch {}
  } else {
    try { $b.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke(); $done = $true; $res = 'invoked ' + $Button } catch {}
  }
  if (-not $done) {
    [void][W32c]::SendMessage([IntPtr]$b.Current.NativeWindowHandle, 0x00F5, [IntPtr]::Zero, [IntPtr]::Zero)
    $res = 'BM_CLICK ' + $Button
  }
  break
}
[System.IO.File]::WriteAllText($Out, $res)
