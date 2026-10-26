param([string]$Out, [string]$Title = 'Error', [switch]$ClickOK)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class W32h { [DllImport("user32.dll")] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l); }
'@
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$sb = New-Object System.Text.StringBuilder
$all = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
foreach ($w in $all) {
  if ($w.Current.ClassName -eq 'TMessageForm' -and $w.Current.Name -eq $Title) {
    [void]$sb.AppendLine('pid=' + $w.Current.ProcessId)
    $els = $w.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
    foreach ($e in $els) {
      $v = ''
      try { $v = $e.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).Current.Value } catch {}
      [void]$sb.AppendLine('  ' + $e.Current.ControlType.ProgrammaticName + ' | ' + $e.Current.ClassName + ' | name=' + $e.Current.Name + ' | value=' + $v)
      if ($ClickOK -and $e.Current.Name -eq 'OK' -and $e.Current.ClassName -eq 'TButton') {
        [void][W32h]::SendMessage([IntPtr]$e.Current.NativeWindowHandle, 0x00F5, [IntPtr]::Zero, [IntPtr]::Zero); [void]$sb.AppendLine('  -> clicked OK')
      }
      if ($ClickOK -and $e.Current.Name -eq 'OK' -and $e.Current.ClassName -eq 'TXPBitBtn') {
        $e.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke(); [void]$sb.AppendLine('  -> invoked OK')
      }
    }
  }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true)))
