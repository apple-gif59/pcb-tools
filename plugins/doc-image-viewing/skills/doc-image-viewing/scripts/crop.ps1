param([string]$Src, [string]$Out, [double]$X0, [double]$Y0, [double]$X1, [double]$Y1, [double]$Scale = 1.0)
# X0..Y1 are fractions (0..1) of the source image size
Add-Type -AssemblyName System.Drawing
$bmp = [System.Drawing.Bitmap]::FromFile($Src)
$x = [int]($X0 * $bmp.Width); $y = [int]($Y0 * $bmp.Height)
$w = [int](($X1 - $X0) * $bmp.Width); $h = [int](($Y1 - $Y0) * $bmp.Height)
$crop = $bmp.Clone((New-Object System.Drawing.Rectangle $x, $y, $w, $h), [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
if ($Scale -ne 1.0) {
    $nw = [int]($w * $Scale); $nh = [int]($h * $Scale)
    $big = New-Object System.Drawing.Bitmap $nw, $nh
    $g = [System.Drawing.Graphics]::FromImage($big)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.DrawImage($crop, 0, 0, $nw, $nh)
    $g.Dispose(); $crop.Dispose(); $crop = $big
}
$crop.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
"src $($bmp.Width)x$($bmp.Height) -> crop $($crop.Width)x$($crop.Height)"
$crop.Dispose(); $bmp.Dispose()
