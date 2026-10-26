# 原理图查看和数据提取

## 选哪种办法

- 看原理图、查文字重叠：首选 `render_sheet.py`（不经过窗口的离屏渲染）。
- 要看图纸边框、AD 标准标题栏，或屏幕上的高亮、选中状态：用 AD 截图。
- 需要完整、能批量核对的信息：用下面"数据提取"里的方法，不靠图片。
- 截图读到的数值以数据为准，用元件的 `Comment` 等参数核对。

## render_sheet.py（离屏渲染）

- 位置：MCP 仓库的 `dev\render_sheet.py`（上游自带）。
- 用法：`python -X utf8 <MCP 仓库>\dev\render_sheet.py <SchDoc 完整路径> <out.png> 8000`。
  - 不用装别的包：Python 部分只用标准库，栅格化用 Windows 自带的 System.Drawing。
  - 每页几秒（脚本里有 1.2 秒 Sleep），输出宽度按第三个参数，高度按图上对象的外接框比例。
  - 从 Bash/PowerShell 工具调用时把超时设到 450 秒（它内部最多等沙盒 180 秒、栅格化 200 秒）。默认 120 秒会把 Python 杀掉，而 AD 里的脚本照跑。
  - EMF 和注入的脚本留在系统临时目录（Python 的 `tempfile.gettempdir()`）里的 `render_sheet.emf`、`render_sheet.pas`，每次覆盖。
- 原理：沙盒里 `ShowDocument` → `Sch:Select(Action=All)` → `Sch:Copy` → `Sch:DeSelect`，AD 把整页以 EMF 图元文件放进剪贴板；再用 Windows PowerShell 5.1 的 System.Drawing 把 EMF 画成 PNG。
  不依赖窗口、前台或重绘状态。
- 效果：
  - 用的是 AD 自己的绘图：中文注释、自定义标题栏里的中文、特殊字符串（图号显示工程名、页名）都正确。
  - 小号元件值、位号、管脚名不用缩放就能读。文字位置和 AD 屏幕一致，所以可以用来查文字重叠（EMF 里压在一起的文字，AD 截图里也压在一起）。
  - 极小的旋转文字（如封装名）放大后字形会挤在一起，是栅格化效果，不是重叠。
- 和 AD 屏幕的差别：EMF 只包含图上的对象，不包含图纸本身画的东西。
  - 没有图纸边框和 1～6 / A～D 分区。
  - 没有 AD 自带的标准标题栏。所以标准标题栏（Title/Size A4/Date/File/Sheet of）和自定义公司标题栏叠在一起这种重叠，EMF 里看不到。
  - 没定义的参数（`=CheckedBy`、`=Checked Date`）在 AD 屏幕上是灰字，EMF 里是空白；SIZE 格里只有一个小撇号。
  - 画面范围是对象的外接框，不是整张图纸。裁剪时不能按图纸坐标换算比例，先出缩略图定位再细裁。
- 副作用和状态：
  - 覆盖剪贴板，运行前要告诉用户。
  - 把 AD 当前激活文档切到这一页。
  - 跑完 `modified_document_count` 仍为 0。不带参数的 `Sch:DeSelect` 能清掉全选，没有残留选中。
- 它的沙盒和 MCP 的不是同一个：`sandbox_runner.py` 跑的是 `<MCP 仓库>\dev\sandbox\Sandbox.PrjScr`，日志和结果写在交换目录的 `sandbox_log.txt` / `sandbox_result.json`（v0.5.1 的 MCP 已不用这两个文件）。AD 同一时间只跑一个脚本，不要和其他 AD 脚本同时跑。成功后它会把 `dev\sandbox\Sandbox.pas` 恢复成占位内容。它出错时不会自动恢复，按 SKILL.md "出错恢复"里的手动步骤处理。
- 也可以完全走 MCP（PNG 和 render_sheet.py 的逐字节相同，出错时 MCP 自动恢复）：
  1. 把 `render_sheet.py` 里 `PAS` 常量的内容交给 `run_altium_script`：`{DOC}` 换成路径，`{{`/`}}` 换成 `{`/`}`。
  2. `powershell.exe -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\emf2png.ps1 -Emf <x.emf> -Png <x.png> -Width 8000`（就是 render_sheet.py 里的 PS 段，改成了参数）。输出目录要先建好，否则 EMF 写不出来、后面一串报错。

## AD 截图和缩放

- 整页截图能不能读，取决于电路在图纸上占多大：
  - 铺满整张图纸的页，把原图裁剪放大 3～5 倍后，位号、元件值、网络名都读得出。
  - 电路只画在图纸一角的页，裁剪后大部分能读，但小数字有歧义（3.3K 还是 3.9K），被网络标签压住的位号读不出。这种页要缩放后再截图，或者改用 `render_sheet.py`。
- 缩放参数以 `<AD 安装目录>\System\advsch.rcs` 里 `Command='Sch:Zoom'` 的条目为准（altium-script skill 的 `lookup Sch:Zoom` 直接列出）：
  - 缩放到选中对象：`Object=Selected`（实测）。rcs 里没有 `Action=Selected` 这个参数；`Sch:ZoomSelected` 是菜单项 ID（`PLSch:ZoomSelected`），对应的命令是 `Sch:Zoom` 加 `Object=Selected`，它本身不是进程名。
  - 固定比例：`ZoomLevel=2`（rcs 列出的值是 0.5、1、2、4）。
  - 适应所有对象：`Action=All`。标题栏也算对象，对电路只占一角的图没用。
- 看某一块电路（沙盒）：
  1. `SchServer.GetCurrentSchDocument` 迭代 `eSchComponent`，把要看的元件设 `.Selection := True`；
  2. `ResetParameters; AddStringParameter('Object', 'Selected'); RunProcess('Sch:Zoom');`
  3. `ResetParameters; AddStringParameter('Action', 'All'); RunProcess('Sch:Deselect');`
  4. 再调 `get_screenshot(view_type='sch')`。
  - 取消选择后缩放保持不变，画面上也没有选中高亮。选中/取消选中不会把文档标记为已修改。
  - 缩放范围是选中对象的外接框：只选 1 个元件，它会占满窗口；要看一块区域，就选分布在这块区域四周的几个元件。
  - 顶部的浮动工具栏会挡住画面最上面一条。
- 外部命令同样可用，作用于当前激活的原理图：`-RSch:Zoom(ZoomLevel=2)`、`-RSch:Zoom(Action=All)`（都实测过）。
- 切换页面：沙盒里 `Client.OpenDocument('SCH', 路径)`，再 `Client.ShowDocument`。
  - AD 只在窗口真正显示在屏幕上时才绘制原理图视图。AD 在后台时调 `ShowDocument`，标签和标题都会切过去，但画面还是上一个文档的。
  - 返回的 `captured_document` 只说明 AD 当前是哪个文档，不能证明画面已经重绘。截图后仍要看一眼画面和标签是否一致。
- 截图裁剪放大用 skill `doc-image-viewing` 的 `crop.ps1`。

## 数据提取

- 网表：沙盒里按路径找到工程 → `DM_Compile` → 遍历 `DM_PhysicalDocuments(i).DM_Components(j).DM_Pins(k)`，取 `DM_PinNumber/DM_PinName/DM_FlattenedNetName`，要管脚电气类型再加 `DM_ElectricalString`，写到 MCP 交换目录下的文本文件。导出的是快照，原理图改了要重新导。
  - 文档名用 `DM_FileName`；三层循环的上界分别是 `DM_PhysicalDocumentCount`、`DM_ComponentCount`、`DM_PinCount`；写文件见 `pcb-scripting.md`。
  - **工程不要用 `GetWorkspace.DM_FocusedProject` 取。** 它跟着焦点文档走：焦点在一个自由文档上时返回 `Free Documents`（实测），焦点在主页或别的工程时就是别的工程；v0.5.0 时沙盒出错后还会返回沙盒工程 `Sandbox.PrjScr`。拿错了工程，编译后 `DM_PhysicalDocumentCount` 为 0，不报错。
    改成遍历 `GetWorkspace.DM_Projects(I1)`（`I1` 从 0 到 `GetWorkspace.DM_ProjectCount - 1`），取 `DM_ProjectFullPath` 等于目标 `.PrjPcb` 完整路径的那个；一个都对不上（工程没打开）就别往下跑。
  - `DM_Compile` 之后先看 `DM_PhysicalDocumentCount`，再取 `DM_PhysicalDocuments(0)`：数量为 0 时取下标会出错。
  - 管脚电气类型是 `DM_ElectricalString`，返回 `Passive` 这类字符串。没有 `DM_ElectricalTypeString`，写了会报 `Undeclared identifier`（成员不存在，见 SKILL.md "沙盒规则"）。
  - 没起名字的网络，名字是 AD 自动起的 `Net<位号>_<管脚号>`，只连一个管脚的也一样，所以导出里没有空网络名。
  - 只查几个元件时，在找到的工程上调 `DM_DocumentFlattened` 拿到整个工程的扁平文档，遍历 `DM_Components(I)`，按 `DM_PhysicalDesignator` 找，读 `DM_LibraryReference`、`DM_Footprint`。
- 图上的注释/网络标号：用 olefile 读 SchDoc 的 `FileHeader` 流（RECORD=4 文字、25 网络标号）。
  - 记录格式 `[u16 长度][2 字节][文本]` 重复（`p += 4` 后取长度字节）。
  - 键名大小写混着写（`Text=`、`Location.X=`），正则要加 `re.I`，否则什么都匹配不到。
  - 中文存两遍：`%UTF8%Text=` 是 UTF-8 字节，`Text=` 是 GBK 字节。整条按 GBK 解码后取 `|Text=`；要用 `%UTF8%` 那段就单独按 UTF-8 解。
- 器件极性：`get_symbol_primitives` 看符号三角形朝向，`get_footprint_primitives` 看丝印标记，两者对照。
