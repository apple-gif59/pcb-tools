param([string]$Out, [string]$Class, [string]$Name, [string]$ElemClass = '', [int]$DX = -1, [switch]$Double, [switch]$DryRun)
# Mouse-click the element (inside the top-level window of class $Class) whose Name equals $Name
# (and class equals $ElemClass if given). Clicks at the element centre, or at x = left + $DX if $DX >= 0.
# Hit-tests before clicking and aborts if the element under the cursor is a different one.
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName WindowsBase
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class W32k {
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, UIntPtr e);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
}
'@
[void][W32k]::SetProcessDPIAware()
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$res = 'window not found'
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, $Class)
$w = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
if ($w -ne $null) {
  [void][W32k]::SetForegroundWindow([IntPtr]$w.Current.NativeWindowHandle)
  $nc = New-Object System.Windows.Automation.PropertyCondition($A::NameProperty, $Name)
  $els = $w.FindAll([System.Windows.Automation.TreeScope]::Descendants, $nc)
  $hit = $null
  foreach ($e in $els) { if ($ElemClass -eq '' -or $e.Current.ClassName -eq $ElemClass) { $hit = $e; break } }
  if ($hit -eq $null) { $res = 'element not found' } else {
    $r = $hit.Current.BoundingRectangle
    if ($r.IsEmpty -or [double]::IsInfinity($r.X)) { $res = 'offscreen' } else {
      $x = [int]($r.X + $r.Width / 2); if ($DX -ge 0) { $x = [int]($r.X + $DX) }
      $y = [int]($r.Y + $r.Height / 2)
      [void][W32k]::SetCursorPos($x, $y)
      Start-Sleep -Milliseconds 200
      $under = $A::FromPoint((New-Object System.Windows.Point($x, $y)))
      $ok = ($under.Current.Name -eq $Name) -or ($under.Current.NativeWindowHandle -ne 0 -and $under.Current.NativeWindowHandle -eq $hit.Current.NativeWindowHandle)
      if (-not $ok) { $res = 'ABORT hit-test: under=' + $under.Current.ClassName + '/' + $under.Current.Name } elseif ($DryRun) { $res = 'DRYRUN ok at ' + $x + ',' + $y } else {
        $n = 1; if ($Double) { $n = 2 }
        for ($i = 0; $i -lt $n; $i++) {
          [W32k]::mouse_event(0x0002, 0, 0, 0, [UIntPtr]::Zero); Start-Sleep -Milliseconds 40
          [W32k]::mouse_event(0x0004, 0, 0, 0, [UIntPtr]::Zero); Start-Sleep -Milliseconds 80
        }
        $res = 'CLICKED ' + $Name + ' at ' + $x + ',' + $y
      }
    }
  }
}
[System.IO.File]::WriteAllText($Out, $res)
