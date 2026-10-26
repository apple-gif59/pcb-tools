param([string]$Out, [string]$Class, [string]$ElemClass, [string]$OldValue, [string]$NewValue)
# Find, inside the top-level X2 window of class $Class, the element of class $ElemClass whose value is $OldValue,
# and set its text with WM_SETTEXT.
# Reports the value read back.
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class W32v {
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, string l);
}
'@
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$res = 'window not found'
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, $Class)
$w = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
if ($w -ne $null) {
  $res = 'element not found'
  $c2 = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, $ElemClass)
  $els = $w.FindAll([System.Windows.Automation.TreeScope]::Descendants, $c2)
  foreach ($e in $els) {
    $vp = $null
    try { $vp = $e.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern) } catch {}
    if ($vp -eq $null) { continue }
    if ($vp.Current.Value -ne $OldValue) { continue }
    $h = [IntPtr]$e.Current.NativeWindowHandle
    [void][W32v]::SendMessage($h, 0x000C, [IntPtr]::Zero, $NewValue)
    Start-Sleep -Milliseconds 300
    $res = 'WM_SETTEXT hwnd=' + $h + '; read back: ' + $vp.Current.Value
    break
  }
}
[System.IO.File]::WriteAllText($Out, $res)
