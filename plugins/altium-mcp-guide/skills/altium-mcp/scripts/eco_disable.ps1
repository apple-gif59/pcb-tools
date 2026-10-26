param([string]$Out, [Parameter(Mandatory)][string]$Pattern, [int]$CheckX = 180, [int]$Max = 100)
# Uncheck (Enable -> False) every ECO row whose text, after the leading "True ", matches the regex $Pattern.
# Scrolls offscreen rows into view with the mouse wheel, hit-tests before each click, reads the row back after.
# Stops at the first row it cannot verify. Row texts: run eco_rows.ps1 first.
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName WindowsBase
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class W32f {
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, UIntPtr e);
}
'@
[void][W32f]::SetProcessDPIAware()
$A = [System.Windows.Automation.AutomationElement]
$root = $A::RootElement
$sb = New-Object System.Text.StringBuilder
function Save { [System.IO.File]::WriteAllText($Out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($true))) }
$cond = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TChangeManagementForm')
$dlg = $root.FindFirst([System.Windows.Automation.TreeScope]::Children, $cond)
$gc = New-Object System.Windows.Automation.PropertyCondition($A::ClassNameProperty, 'TdxTreeList')
$grid = $dlg.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $gc)
$walker = [System.Windows.Automation.TreeWalker]::RawViewWalker
$rx = '^\s*True (' + $Pattern + ')'
function Val($el) { return $el.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).Current.Value }
$count = 0
while ($count -lt $Max) {
  # find next target row
  $target = $null
  $ch = $walker.GetFirstChild($grid)
  while ($ch -ne $null) {
    if ($ch.Current.ClassName -like 'TdxTreeList*Node') { $v = Val $ch; if ($v -match $rx) { $target = $ch; break } }
    $ch = $walker.GetNextSibling($ch)
  }
  if ($target -eq $null) { [void]$sb.AppendLine('no more targets'); break }
  $text = (Val $target).Trim()
  $gr = $grid.Current.BoundingRectangle
  $visible = $false
  for ($s = 0; $s -lt 40; $s++) {
    $r = $target.Current.BoundingRectangle
    if (-not ($r.IsEmpty -or [double]::IsInfinity($r.Y))) {
      $y = [int]($r.Y + $r.Height / 2)
      if ($y -ge $gr.Y + 40 -and $y -le $gr.Y + $gr.Height - 10) { $visible = $true; break }
    }
    # wheel down one notch over the grid
    [void][W32f]::SetCursorPos([int]($gr.X + $gr.Width / 2), [int]($gr.Y + $gr.Height / 2))
    Start-Sleep -Milliseconds 50
    [W32f]::mouse_event(0x0800, 0, 0, [uint32]4294967176, [UIntPtr]::Zero)
    Start-Sleep -Milliseconds 200
  }
  if (-not $visible) { [void]$sb.AppendLine('STOP could not scroll into view: ' + $text); break }
  [void][W32f]::SetCursorPos($CheckX, $y)
  Start-Sleep -Milliseconds 100
  $under = $A::FromPoint((New-Object System.Windows.Point($CheckX, $y)))
  $uv = ''; try { $uv = (Val $under).Trim() } catch {}
  if ($uv -ne $text) { [void]$sb.AppendLine('STOP hit-test mismatch: want=' + $text + ' got=' + $uv); break }
  [W32f]::mouse_event(0x0002, 0, 0, 0, [UIntPtr]::Zero); Start-Sleep -Milliseconds 40
  [W32f]::mouse_event(0x0004, 0, 0, 0, [UIntPtr]::Zero); Start-Sleep -Milliseconds 200
  $after = (Val $target).Trim()
  if (-not $after.StartsWith('False ')) { [void]$sb.AppendLine('STOP click did not disable: ' + $after); break }
  $count++
  [void]$sb.AppendLine('disabled: ' + $after.Substring(0, [math]::Min(70, $after.Length)))
}
[void]$sb.AppendLine('total disabled this run: ' + $count)
Save
