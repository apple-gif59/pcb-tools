---
name: altium-mcp
description: 通过 altium MCP 操作 Altium Designer 23 的实测经验：run_altium_script 沙盒的限制、脚本出错或卡死后的恢复、模态对话框（ECO、DRC 设置）用 UI Automation 操作、保存和重开文档、MCP 工具的坑、截图和原理图查看、网表提取；规则/Room/高度/3D 体/DRC 和模拟检查、改封装库和原理图符号、ECO、keepout/挖空/非金属化孔/机械层的 API 写法；从磁盘解析 PcbDoc。调用任何 altium MCP 工具或写 DelphiScript 之前先读；和 altium-script skill 冲突时以本 skill 为准。
---

# Altium MCP 实战

下面的内容都在 AD23 + altium-mcp（上游 coffeenmusic/altium-mcp v0.5.0）上实测复现过，或者读 MCP 源码确认过。
往本 skill 里补充经验时同样只写这两类：换个工程、换台机器也成立、结果可复现的结论。没定位到具体语句的崩溃、只出现过一次的现象、推断，都不写；工程里的位号、数量、规则名写进那个工程自己的文档；本机的安装路径、屏幕缩放、装了哪些软件不写在任何地方，写成运行时怎么查到（如下面"定位 AD 和 MCP"）。

## 定位 AD 和 MCP

- **外部命令**：用正在运行的 AD 可执行文件带参数启动。MCP 拉起的第二实例启动得晚，取最早的那个：
  `$x2 = (Get-Process X2 | Sort-Object StartTime | Select-Object -First 1).Path; Start-Process $x2 -ArgumentList '<参数>'`。
  下文的 `<AD 安装目录>` 就是 `$x2` 所在的目录（rcs 文件、SDK dll 在它的 `System\` 下）。
- **MCP 仓库**：MCP 服务进程的命令行里有 `<MCP 仓库>\server\main.py`（`Get-CimInstance Win32_Process -Filter "Name like 'python%'"` 查 `CommandLine`）。MCP 工具的行为拿不准时，读 `server\main.py`（docstring）和 `server\AltiumScript\*.pas`。
- **MCP 的交换目录** `C:\Users\Public\altium_mcp\`（`main.py` 里写死的，AD 和 MCP 都能读写）：`sandbox_log.txt`、`sandbox_result.json`、`temp_*.json` 等。
- 本 skill 的 `scripts\`：出错恢复、UIA 操作对话框、截图、EMF 转 PNG、从磁盘读规则和高度、PcbDoc 比对。用法见各参考文件。PowerShell 脚本都是在 Windows PowerShell 5.1 下实测的，用它跑：`powershell.exe -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\<脚本> -Out <结果.txt> ...`。
- **altium-script skill**：AD23 的 API 字典、进程表、写法模式和官方示例。成员、常量、进程名用它的 `scripts\lookup.py` 查，用法见它的 SKILL.md。本 skill 管"跑起来实际怎样、出错怎么办"，它管"有什么、签名和值是什么"。

## 沙盒（run_altium_script）规则

- 只接受语句体，不能写 `Var` 声明或完整程序。预置变量（以 `server\SandboxScript\Sandbox.pas` 为准）：
  `S1..S3: String`、`I1..I3: Integer`、**`B1: Integer`**（不是 Boolean，能接 `RunBatchDesignRuleCheck` 的返回值，也能当计数器）、`Obj1..Obj5: IDispatch`、`List1: TStringList`、`IntMan`、`DbDoc`，以及 **`ResultText: String`**（写进去的内容就是工具返回的 `result`）。预置过程是 `SandboxLog(Msg: String)`。
  没有 `Obj6`，写了会在执行到那一句时出错。对象变量不够用时，`IntMan`、`DbDoc`、`List1` 都能临时装别的对象。常量 `REPLACEALL = 1` 也能用（给 `StringReplace` 做全部替换）。`LogLines`、`LogPath`、`OutPath`、`OutLines` 是沙盒自己用的，不要赋值。
- **语句体里不要用 `Exit`。** 语句体在沙盒的 `Run` 过程里，结果在语句体之后才写盘；`Exit` 直接离开 `Run`，MCP 等满 `timeout_seconds` 也拿不到结果，报 `"script started but did not finish"`、`executor_wedged: true`，但执行器其实正常（实测下一个脚本照常跑，不用恢复）。要跳过后面的语句用 `if ... then ... else`。语句体里也不能声明函数，所以没有 `Result`。
- **`List1` 只声明、没有创建。** 当字符串列表用之前先 `List1 := TStringList.Create;`，用完 `List1.Free;`。
  直接用 `List1.Count` 或 `List1.Values[...]` 会报 "Undeclared identifier: Count/Values"，`if List1 = nil` 同样报错。Obj1..Obj5 也只是空的 IDispatch 变量，要自己赋值。
- **`try/except` 抓不到运行时错误，出错后 `Finally` 也不执行。** 读写一个不存在的属性（如 `IPCB_Component.SourceDesignItemID`、规则的 `MinSolderMaskWidth`）也会让执行器卡死，不会返回错误值：属性名先用 altium-script skill 的 `lookup` 查。
- 写脚本的流程：先用几行的小脚本逐条验证 API，每个有风险的语句前加 `SandboxLog('...')`；跑通后再写循环或批量逻辑。验证过的语句放进整板循环、包在一对 `PCBServer.PreProcess`/`PostProcess` 里是没问题的。
- **每个脚本开头先切焦点文档、再核对。** `PCBServer.GetCurrentPCBBoard` 返回焦点文档的板子；焦点在 PcbLib 时它悄悄返回库的板子，迭代规则得到 0 条，不报错。`get_footprint_primitives` 和沙盒里打开库都会把焦点切走。
  ```
  S1 := '<PcbDoc 完整路径>';
  Client.ShowDocument(Client.OpenDocument('PCB', S1));
  Obj1 := PCBServer.GetCurrentPCBBoard;
  if Obj1.FileName <> S1 then ResultText := 'WRONG ' + Obj1.FileName else ...
  ```
  文档已经打开、没有未保存的改动时，`OpenDocument` 不会再开一份，返回的就是那个文档（实测打开的文档总数和 `Modified` 都不变；有未保存改动时没测过）；没打开时它会从磁盘打开。只想切到已打开的文档、不想打开新文件时，改成下面这样（IDispatch 变量和 `nil` 比较实测能用）：
  ```
  S1 := '<PcbDoc 完整路径>';
  Obj2 := Client.GetDocumentByPath(S1);
  if Obj2 = nil then ResultText := 'NOT OPEN ' + S1
  else begin
    Client.ShowDocument(Obj2);
    Obj1 := PCBServer.GetCurrentPCBBoard;
    if Obj1.FileName <> S1 then ResultText := 'WRONG ' + Obj1.FileName else ...
  end;
  ```
  原理图切过去后用 `Obj1 := SchServer.GetCurrentSchDocument` 核对：焦点不在原理图上时它返回 `nil`（实测）。不是 `nil` 就比较 `Obj1.DocumentName`（是完整路径）和 S1，再看 `Obj1.ObjectId`（32 是 SchDoc，33 是 SchLib）。`ISch_Document` 没有 `FileName`，读它会弹 Error、卡住执行器（实测）。
- `run_altium_script` 默认只等 120 秒（参数 `timeout_seconds`）。批量 DRC、批量改 Room（每条要几秒）、大批删除这类脚本，按估计时长传 300～600。超时不等于崩溃，见下面"出错恢复"。
- 交给 subagent 做 AD 相关的工作时，在提示里写明：上面几条、下面的恢复方法，以及允许它用 UIA 点哪些对话框。

## 出错恢复

- 脚本没跑完时 MCP 返回 `"success": false, "error": "script started but did not finish", "last_step_reached": "...", "executor_wedged": true`。**出错语句之前的语句已经生效**；`last_step_reached` 只说明出错在最后一条 SandboxLog 之后的某一句，可疑语句前各加一条 SandboxLog 才能定位。
- **返回值分不出"崩了"和"没跑完"**（`server\main.py` 的 `run_altium_script`）：MCP 每次调用前删掉 `sandbox_log.txt` 和 `sandbox_result.json`，在 `timeout_seconds` 内等结果文件，6 秒后开始关掉 AD 弹的框；等不到结果就一律报 `executor_wedged: true`。所以：
  - `dismissed_dialog_titles` 里有 `"Error"`：运行时错误，按下面恢复。（`"X2"` 是规则查询表达式里用了非法关键字，脚本照常跑完，但那次的结果作废，见 `references/rules-and-drc.md`。）
  - 是空的：崩溃（如写 `Board.LayerColor`，不弹框直接卡死）、脚本还在跑、在等一个关不掉的框，三种都出现过；语句体里执行了 `Exit` 也是这样，但那种情况执行器没事。先用 `scripts\uia_top.ps1` 看有没有模态框（含主窗口下类名为 `Window` 的 WPF 子窗口），有就按 `references/uia-dialogs.md` 处理；没有模态框时，脚本里有 `Exit` 就跑一个两行的小脚本确认执行器正常，没有 `Exit` 就按崩溃恢复。
  - 因此耗时长的脚本（批量 DRC、批量改 Room、大批删除）一开始就把 `timeout_seconds` 给够，别让它走到这一步：对还在跑的脚本发 Stop，会把批量修改停在中途。
  - 旧脚本在下一次调用等待期间跑完时，它的结果会被那次调用读走。恢复后的第一个探针脚本，要核对返回的 steps 是不是它自己的。
- 模态框开着时不要跑恢复：外部命令会再拉起新的 X2 进程。
- 恢复：`powershell.exe -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\recover.ps1`。它做两件事：
  1. 外部命令 `-REditScript:Stop` 停调试器，等 3 秒；
  2. 关掉旧脚本标签页：出错后 AD 会在编辑器里打开 `<MCP 仓库>\server\SandboxScript\Sandbox.pas`，只要它还开着，AD 执行的就是内存里的旧脚本。
     它用 `scripts\closer\` 的模板在交换目录生成 `closer\Closer.PrjScr`，再用外部命令 `-RScriptingSystem:RunScript(ProjectName="<交换目录>\closer\Closer.PrjScr"|ProcName="Closer>Run")` 运行（`Client.GetDocumentByPath` → `Doc.Modified := False` → `Client.CloseDocument`）。
  AD 和 MCP 仓库的路径从运行中的进程取（见"定位 AD 和 MCP"）；`-DryRun` 只解析路径、生成 Closer，不给 AD 发命令。
  结果写在交换目录的 `closer_result.txt`，正常是 `start / found / unmodified / closed`（标签页没开着时是 `start / not open`）。判断旧脚本还在不在：看 `sandbox_log.txt` 的内容是否对应刚发送的脚本。
- 恢复后先跑一个两行的小脚本确认执行器正常。

## 模态对话框

- ECO、DRC 设置、Update Footprints、提示框这类模态框开着时，**MCP 的调用会超时**（`get_screenshot` 报 "No response received from Altium (timeout)"），而且 MCP 会再拉起一个 X2 实例，弹 "Information"（"another instance … busy"）。不关掉它，之后的 MCP 调用一直超时。
- 处理顺序：`uia_top.ps1` 看有哪些 X2 实例和窗口 → `uia_msg.ps1 -Title Information -ClickOK` 关掉 busy 框 → 用 UIA 处理对话框 → `get_server_status` 加一个两行脚本确认恢复。
- 会话里没有 computer use 时，用 PowerShell + UI Automation 操作对话框，效果一样。窗口类名、控件、哪些做法不灵：`references/uia-dialogs.md`。

## 保存、关闭和重开

- 脚本里调用 `DoFileSave` 一定失败：脚本本身就算"正在运行的命令"，AD 会弹 "A command is currently active ... save copy?"。**选 No，不要选 Yes**（Yes 会另存一个 recovery copy）。
- 正确做法是外部命令（等同于 Ctrl+S，保存**焦点**文档，所以先 `Client.ShowDocument(Client.OpenDocument(...))` 切过去）：
  - 文档：`-RWorkspaceManager:SaveObject(ObjectKind=Document|SaveMode=Standard)`
  - 工程（`.PrjPcb`）：`-RWorkspaceManager:SaveObject(ObjectKind=Project|SaveMode=Standard)`
  之后等 4～6 秒，查文件的 LastWriteTime，再用 `uia_top.ps1` 确认没有弹框。
- 如果连用户按 Ctrl+S 也弹这个警告，说明有脚本在 `PCBServer.PreProcess` 之后崩了，没执行 `PostProcess`。按 Esc、关掉 Sandbox 工程都没用。
  处理：用沙盒补调 `PCBServer.PostProcess`，一次一个，直到 Ctrl+S 不再弹警告，再从外部保存。
- 关闭再从磁盘重开（放弃未保存的改动）：
  ```
  Obj1 := Client.GetDocumentByPath(S1);
  Obj1.Modified := False;          { 只在确定要放弃改动时；否则先保存，确认 Modified = 0 }
  Client.CloseDocument(Obj1);
  ```
  下一个脚本 `Client.ShowDocument(Client.OpenDocument('PCB', S1))`，再用 `GetCurrentPCBBoard` 拿新板。重开前用 SHA-256 确认磁盘上是想要的版本。
  如果之前打开过层叠管理器（标签页 `<文件名> [Stackup]`），关闭时会弹 WPF 对话框 "Layer stack has been modified in the PCB. Update with changes?"，用 `uia_wpfdlg.ps1 -ClickName Yes` 点掉；没开过就不弹。
- 读文档的修改标志：`IntToStr(Doc.Modified)` 是 -1 或 0（库手动置位后读出 1），判断用 `<> 0`。改库的 Height 和 3D 体不会自动置位，见 `references/pcblib-and-eco.md`。

## MCP 工具注意

- 坐标单位：`get_component_data` 的 x/y 是 **mil**，`get_board_summary` 是 **mm**，都相对板原点。
- `get_component_data` 的 `height` 是元件外接框在 Y 方向的长度（mil，`Rect.Top - Rect.Bottom`），**不是** Height 属性。读 Height 用元件迭代器（`references/pcb-scripting.md`）。
- `get_component_data`、`get_component_pins` 一次查全部元件（两百个上下）会超出输出上限，结果落到文件里：用 Python 读文件统计，不要逐段阅读。MCP 自己也把完整 JSON 写在 `C:\Users\Public\altium_mcp\temp_*.json`（`temp_pins_data.json`、`temp_project_components.json`、`temp_nets_data.json`、`temp_stackup_data.json` 等），可以直接复制来用。
- `create_net_class(class_name, net_names)` 返回的 `nets_added: 0` 是错的，成员实际都加上了；回读迭代 `eClassObject`，读 `MemberName[I]` 直到空串。
- `get_component_pins`、`get_component_primitives` 只在焦点文档是 PCB 时有数据，否则返回空列表 / `missing_designators`。`get_screenshot(view_type='pcb')` 在 PcbLib 聚焦时直接报错，看库就用 `scripts\screen.ps1` 截桌面。
- `get_component_pins` 的 dx/dy 是封装 0° 坐标系里的偏移（去掉了旋转，底层元件还去掉了镜像），不是板上的偏移；板上位置用它给的 x/y。docstring 里有用 dx/dy 预测摆放后焊盘位置的公式。
- `get_component_primitives` 不带图元坐标（焊盘只有名字、尺寸、外扩）。要坐标用 `get_component_pins` 或焊盘迭代器。
- `get_footprint_primitives` 会把焦点切到 PcbLib；读的是当前封装时坐标多出 50000 mil（库板原点）。
- `place_components` 翻到底层时先翻层、再设绝对角度：`layer=bottom, rotation=0` 得到的焊盘排布是原封装关于 X 轴的镜像，`rotation=180` 是关于 Y 轴的镜像（左右翻）。摆完用 `get_component_pins` 核对焊盘坐标。
- `set_component_position` 有舍入（差几个内部单位），`rotation: -1` 表示保持原角度。要精确复位用脚本 `MoveToXY`。
- `create_footprints_batch` 的规格文件要 UTF-8 带 BOM，否则中文按 GBK 解析；格式见 `references/pcblib-and-eco.md`。
- `get_pcb_layer_stackup` 只遍历电气层和它们之间的介质，不含两层阻焊，所以总厚比 AD 显示的少两层阻焊（AD 默认各 0.01016 mm）；介质类型为 0（No Dielectric）的芯板不计入总厚。`*_um` 字段是内部单位 ÷254，应该 ÷393.7（结果大了 1.55 倍），用 mil/mm 字段。
- `get_erc_violations` 在内存中编译项目，不保存文档。
- `get_screenshot`：
  - 显示缩放比例大于 100% 时，上游 v0.5.0 的截图只有窗口左上角一块（宽高各除以缩放比）：MCP 进程没声明 DPI 感知。判断布局以数据为准。
  - `view_type='pcb', zoom_to=[位号...]`：缩放到这些元件外接框的并集，四周留 10% 边距（至少 100 mil），截图后视图不恢复。只给一个元件时，焊盘号和网络名都能直接读；给的元件分散时外接框很大，放大有限。
  - `view_type='sch'` 时 `zoom_to` 被忽略（`zoomed_component_count` 为 0）。原理图怎么看见 references/schematic-viewing.md。
- `ensure_altium_script_skill` 只检查 `~/.claude/skills/altium-script/SKILL.md` 在不在（读 `main.py` 确认），在就返回 `installed: true`，传 `install=True` 也不覆盖。只有缺这个文件时，`install=True` 才把上游 coffeenmusic/altium-scripts-skill 克隆进去；那是另一套字典，和 AD23 对不上的地方见 altium-script 的 `references/patterns.md` 末尾。altium-script 装成插件时在 `~/.claude/plugins/cache/` 下，这个工具查不到，会报 `installed: false` 并提示加 `install=true`：Skill 列表里已经有 altium-script（插件版写成 `altium-script:altium-script`）就不要传 `install=True`，否则会多出一份上游字典。

## DRC

- 批量 DRC：`B1 := PCBServer.GetCurrentPCBBoard.RunBatchDesignRuleCheck(报告路径, 1, False, False);`，传 `timeout_seconds: 400`。返回 0（False），但文本报告正常生成，不弹窗。
- **违规数到上限（`MAXVIOLATIONCOUNT`，默认 500）时，报告给的是任意子集**，每次截到哪条都不一样，不能做前后对比。上限和"批量检查哪些规则类型"只能用 UIA 在 DRC 对话框里改，脚本 API 拿不到这些选项。默认的批量检查集合不含 ComponentClearance 等规则类型，要补勾。
- 报告格式、去重、模拟检查（不跑 DRC 也能逐条判定）、规则的各种坑：`references/rules-and-drc.md`。

## 参考文件（按需读）

- `references/pcb-scripting.md`：层号和显示、沙盒里读写文件、层叠（铜厚、芯板）、网络类和焊盘类、批量修改、元件快照/移动/翻面/位号、3D 体、临时测试对象、keepout 区域、Board Cutout、非金属化孔、查接口和枚举。
- `references/rules-and-drc.md`：建规则和改规则、优先级、范围表达式和查询关键字、Room、高度规则（3D 体）、各类规则的坑、批量 DRC 的报告和设置、模拟检查。
- `references/pcblib-and-eco.md`：改 PcbLib（库板原点、加删图元、Height）、create_footprints_batch、Update PCB With Footprint、SchLib 复制符号和改链、原理图实例参数、ECO 和 Room 问题的根治。
- `references/uia-dialogs.md`：模态对话框、UIA 脚本、ECO 对话框、DRC 对话框、提示框和 WPF 对话框。
- `references/file-parsing.md`：用 olefile 只读解析 PcbDoc/PcbLib（流格式、中文编码、保存噪声）、AD History 备份。
- `references/schematic-viewing.md`：`render_sheet.py` 离屏渲染、AD 截图和缩放、切换页面；网表、图上文字、器件极性等数据提取。