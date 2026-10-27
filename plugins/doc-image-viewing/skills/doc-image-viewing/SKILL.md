---
name: doc-image-viewing
description: 在本机看 Read 工具看不清或打不开的文档：把 PDF 任意页渲染成高清 PNG、把大图裁剪放大，以及解析旧版 Office 的 .doc/.xls（不需要装 Office）。看数据手册、规格书、截图细节时用。
---

# 本机看文档和图片

脚本在本 skill 目录（加载 skill 时给出的 Base directory）的 `scripts\` 下，只用 Windows 自带组件，不需要装东西。下面命令里的 `pdf2png.ps1`、`crop.ps1` 调用时要拼成完整路径；从 Bash 调用时路径要写成 Windows 形式（不能用 `$HOME` 或 `/c/...`）。

## PDF

- Read 直接读 PDF 只支持单页，而且会缩小显示；下面的脚本不依赖 pdftoppm。
- 用 Windows 自带的 WinRT（Windows.Data.Pdf）渲染，一次调用可以渲染多页：
  - PowerShell 工具里：`& pdf2png.ps1 -PdfPath <pdf> -Page all -Width 1000 -OutDir <目录>`
  - Bash 里：`pwsh -NoProfile -ExecutionPolicy Bypass -File pdf2png.ps1 -PdfPath <pdf> -Page 0-4 -Width 1000 -OutDir <目录>`。
  - `-Page` 从 0 开始，可写 `2`、`0-4`、`"0,3,5-7"`、`all`。先检查全部页码，有越界或写错就报错，一页都不渲染。
  - 出错时：Bash 里或 `pwsh -File` 子进程调用时退出码是 1；PowerShell 工具里用 `&` 调用时是抛异常，`$LASTEXITCODE` 不会被设置，同一条命令后面的语句也不再执行，要判断成败就用 `try/catch` 包住。
  - 文件名：不给 `-OutName` 时是 `p00.png`、`p01.png`…；单页时直接用 `-OutName`；多页时把 `_pNN` 插在扩展名前（`pic.png` → `pic_p00.png`）；也可以在 `-OutName` 里写 `{0:D2}` 自定（如 `'pg{0:D2}.png'`）。`-OutName` 要带 `.png`，不写扩展名时生成的文件就没有扩展名。
  - PowerShell 里 `-OutName` 带 `{}` 时必须加引号：不加引号的 `pg{0:D2}.png` 只会把 `pg` 传进去，不报错，生成的是没有扩展名的 `pg_p00`。
  - `-OutDir` 要先建好，不存在会报错。
  - 输出第一行是 `pages: N`，N 是 PDF 的总页数（不是这次渲染的页数）；之后每页一行 `saved <文件> (page i, 宽 x 高)`，宽高是 PDF 页面本身的尺寸（单位 DIP，1/96 英寸），和 `-Width`、输出图的像素无关。
  - 实际像素宽度 = `-Width` × 系统显示缩放：缩放 200% 时 `-Width 1000` 得到 2000 宽。
  - 实现：PowerShell 7 没有内置 WinRT 投影，脚本用 .NET 的 COM 互操作直接调 WinRT。整本 21 页约 3.6 s（含 pwsh 启动）；开机后第一次调用可能要 10 s 左右。
  - 渲染总在脚本自己起的子进程里做（多一次 PowerShell 启动，约 1 s）：渲染会建硬件 D3D 设备，有的显卡驱动（实测 AMD 的 `atidxx64.dll`）在进程退出时崩溃，图写好了退出码却是 `-1073741819`。子进程写完输出后直接结束自己，跳过驱动卸载，所以退出码可信；用 `&` 在当前会话里调用也不会拖垮会话。`-Worker` 是内部参数，不要自己传。
  - 脚本存成 UTF-8 带 BOM，保存时不要去掉；改了里面的 C# 要把类名 `PdfRenderNativeV1` 的版本号加一。

## 图片裁剪放大

- `crop.ps1 -Src x.png -Out y.png -X0 .. -Y0 .. -X1 .. -Y1 .. -Scale ..`
  - PowerShell 工具里用 `&` 直接调用；Bash 里用 `pwsh -NoProfile -ExecutionPolicy Bypass -File crop.ps1 ...`。
  - 坐标是 0～1 的比例。先看整图定位，再裁局部；`-Scale` 大于 1 时放大。
  - `-Out` 所在目录要先建好，不存在会报错。
- 大 JPG/PNG 也一样先裁剪，不然 Read 只能看到缩略图。

## .doc / .xls

- 不需要 Office：`pip install olefile xlrd`（纯 Python，能装上）后自己解析。
