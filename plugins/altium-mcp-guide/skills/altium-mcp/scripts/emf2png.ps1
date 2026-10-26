param([string]$Emf, [string]$Png, [int]$Width = 8000)
# Same rasterization as altium-mcp dev/render_sheet.py (PS block), parameterized.
Add-Type -AssemblyName System.Drawing
$sig = @'
using System;
using System.Runtime.InteropServices;
public class Clip {
  [DllImport("user32.dll")] public static extern bool OpenClipboard(IntPtr h);
  [DllImport("user32.dll")] public static extern bool CloseClipboard();
  [DllImport("user32.dll")] public static extern IntPtr GetClipboardData(uint fmt);
  [DllImport("user32.dll")] public static extern bool IsClipboardFormatAvailable(uint fmt);
  [DllImport("gdi32.dll")] public static extern IntPtr CopyEnhMetaFile(IntPtr h, string f);
  [DllImport("gdi32.dll")] public static extern bool DeleteEnhMetaFile(IntPtr h);
}
'@
Add-Type -TypeDefinition $sig
if (Test-Path $Emf) { Remove-Item $Emf }
if (-not [Clip]::IsClipboardFormatAvailable(14)) { Write-Output 'NOEMF'; exit 1 }
[Clip]::OpenClipboard([IntPtr]::Zero) | Out-Null
$h = [Clip]::GetClipboardData(14)
$copy = [Clip]::CopyEnhMetaFile($h, $Emf)
[Clip]::DeleteEnhMetaFile($copy) | Out-Null
[Clip]::CloseClipboard() | Out-Null
$img = [System.Drawing.Image]::FromFile($Emf)
$w = $Width; $h2 = [int]($w * $img.Height / $img.Width)
$bmp = New-Object System.Drawing.Bitmap $w, $h2
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::White)
$g.SmoothingMode = 'AntiAlias'
$g.DrawImage($img, 0, 0, $w, $h2)
$g.Dispose()
$bmp.Save($Png, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose(); $img.Dispose()
Write-Output ('rendered ' + $w + 'x' + $h2)
