---
name: altium-mcp
description: 通过 altium MCP 操作 Altium Designer 23 的实测经验：run_altium_script 沙盒的限制、脚本出错或卡死后的恢复、模态对话框（ECO、DRC 设置）用 UI Automation 操作、保存和重开文档、MCP 工具的坑、截图和原理图查看、网表提取；规则/Room/高度/3D 体/DRC 和模拟检查、改封装库和原理图符号、ECO、keepout/挖空/非金属化孔/机械层的 API 写法；从磁盘解析 PcbDoc。调用任何 altium MCP 工具或写 DelphiScript 之前先读；和 altium-script skill 冲突时以本 skill 为准。
---

# Altium MCP 实战

下面的内容都在 AD23 + altium-mcp（上游 coffeenmusic/altium-mcp v0.5.1）上实测复现过，或者读 MCP 源码确认过。v0.5.1 重写了 `run_altium_script` 的沙盒和出错恢复，沙盒、恢复、保存几节已按 v0.5.1 在 AD23 上复测；参考文件里写"卡死执行器"而没另外注明的，是 v0.5.0 时的现象，现在怎样见下面"出错恢复"。
往本 skill 里补充经验时同样只写这两类：换个工程、换台机器也成立、结果可复现的结论。没定位到具体语句的崩溃、只出现过一次的现象、推断，都不写；工程里的位号、数量、规则名写进那个工程自己的文档；本机的安装路径、屏幕缩放、装了哪些软件不写在任何地方，写成运行时怎么查到（如下面"定位 AD 和 MCP"）。

## 定位 AD 和 MCP

- **外部命令**：用正在运行的 AD 可执行文件带参数启动。MCP 拉起的第二实例启动得晚，取最早的那个：
  `$x2 = (Get-Process X2 | Sort-Object StartTime | Select-Object -First 1).Path; Start-Process $x2 -ArgumentList '<参数>'`。
  下文的 `<AD 安装目录>` 就是 `$x2` 所在的目录（rcs 文件、SDK dll 在它的 `System\` 下）。
- **MCP 仓库**：MCP 服务进程的命令行里有 `<MCP 仓库>\server\main.py`（`Get-CimInstance Win32_Process -Filter "Name like 'python%'"` 查 `CommandLine`）。MCP 工具的行为拿不准时，读 `server\main.py`（docstring）和 `server\AltiumScript\*.pas`。
- **MCP 的交换目录** `C:\Users\Public\altium_mcp\`（`main.py` 里写死的，AD 和 MCP 都能读写）：`runs\`（`run_altium_script` 每次运行的 `.pas`、`_log.txt`、`_result.txt`，只留最近 20 份）、`temp_*.json`、`mcp_script_stuck.txt`（MCP 自己启动的脚本卡住时才有）、`last_project.txt` 等。
- 本 skill 的 `scripts\`：出错恢复、UIA 操作对话框、截图、EMF 转 PNG、从磁盘读规则和高度、PcbDoc 比对。用法见各参考文件。PowerShell 脚本用 PowerShell 7 跑：`pwsh -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\<脚本> -Out <结果.txt> ...`。
- **altium-script skill**：AD23 的 API 字典、进程表、写法模式和官方示例。成员、常量、进程名用它的 `scripts\lookup.py` 查，用法见它的 SKILL.md。本 skill 管"跑起来实际怎样、出错怎么办"，它管"有什么、签名和值是什么"。

## 沙盒（run_altium_script）规则

- 脚本是语句体，前面可以带一个 `var` 块（`var` 后面每行一条 `名字1, 名字2 : 类型;`，到第一行不是声明的为止），工具把它挪进 `Run` 的声明里（实测）。不能声明函数和过程，所以没有 `Result`。
  预置变量（以 `server\SandboxScript\Sandbox.pas` 为准）：`S1..S9: String`、`I1..I9: Integer`、**`B1..B3: Integer`**（不是 Boolean，能接 `RunBatchDesignRuleCheck` 的返回值，也能当计数器）、`F1..F4: Double`、`Obj1..Obj9: IDispatch`、`List1..List3: TStringList`、`IntMan`、`DbDoc`，以及 **`ResultText: String`**（写进去的内容就是工具返回的 `result`）。
  预置的过程和函数：`SandboxLog(Msg)`；`MM(毫米)` 转内部单位（实测 `MM(1.0)` = 393701）；`OpenSchDoc(路径)` 返回 `ISch_Document`，没打开就先打开；`SaveDoc(路径)` 置修改标志再保存（见"保存、关闭和重开"）。常量 `REPLACEALL = 1`（给 `StringReplace` 做全部替换）。`LogLines`、`LogPath`、`OutPath`、`OutLines` 是沙盒自己用的，不要赋值。
- **给没声明的普通变量赋值（`X := ...`、`for X := ...`），工具不发给 AD，直接返回** `"error": "refused before execution: the script would not compile"`，`problems` 里写着行号（实测）。脚本里出现 `with` 时不做这项检查。
- **语句体里不要用 `Exit`。** 结果在语句体之后才写盘；`Exit` 直接离开 `Run`，MCP 等满 `timeout_seconds` 后报 `"no result after N s"`，再自动停掉、恢复（实测，`recovery.recovered: true`）。要跳过后面的语句用 `if ... then ... else`。
- **`List1..List3` 只声明、没有创建。** 当字符串列表用之前先 `List1 := TStringList.Create;`，用完 `List1.Free;`。
  直接用 `List1.Count` 或 `List1.Values[...]` 会报 "Undeclared identifier: Count/Values"，`if List1 = nil` 同样报错。Obj1..Obj9 也只是空的 IDispatch 变量，要自己赋值。
- **语句体包在沙盒的 `try/except` 里，能抓到一部分运行时错误**（实测）：
  - 抓得到：读写不存在的成员（如 `IPCB_Component.SourceDesignItemID`、规则的 `MinSolderMaskWidth`、`SystemOptions.GetState_LayerColors_V6`）、在 nil 上调方法（都报 `Undeclared identifier: <成员名>`）、类型转换（`EConvertError`，具体文字在 steps 里紧接着的下一行）。立刻返回 `"error": "script error"`，执行器没事。自己写的 `try/except/finally` 对这类错误也有效。
  - 抓不到：写只读属性（实测 `Board.LayerColor[...] :=`）这类。AD 弹 "Error" 框，MCP 6 秒后把它关掉，脚本停在调试器里，等满 `timeout_seconds` 后才停掉、恢复；外层 `except` 和自己写的 `finally` 都不执行。
  所以属性名照样先用 altium-script skill 的 `lookup` 查，也不要指望 `try/finally` 一定能执行 `PostProcess`。
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
  原理图切过去后用 `Obj1 := SchServer.GetCurrentSchDocument` 核对：焦点不在原理图上时它返回 `nil`（实测）。不是 `nil` 就比较 `Obj1.DocumentName`（是完整路径）和 S1，再看 `Obj1.ObjectId`（32 是 SchDoc，33 是 SchLib）。`ISch_Document` 没有 `FileName`，读它会报错（实测）。
- `run_altium_script` 默认只等 120 秒（参数 `timeout_seconds`）。批量 DRC、批量改 Room（每条要几秒）、大批删除这类脚本，按估计时长传 300～600。**超时后 MCP 会把脚本停掉**（v0.5.1 源码：脚本开始了却没出结果，一律发 Stop），批量修改会停在中途，所以宁可给多。
- 交给 subagent 做 AD 相关的工作时，在提示里写明：上面几条、下面的恢复方法，以及允许它用 UIA 点哪些对话框。

## 出错恢复

- **出错语句之前的语句已经生效。** `last_step_reached` 只说明出错在最后一条 SandboxLog 之后的某一句，可疑语句前各加一条 SandboxLog 才能定位。
- 每次运行用一个新文件 `<交换目录>\runs\Sbx_<时间>_<pid>_<序号>.pas`（返回的 `run_file`），用 `ScriptingSystem:RunScriptFile` 跑，日志和结果也是这次运行专用的。v0.5.0 那些问题已经没有了：出错后 AD 编辑器里留着旧 Sandbox.pas、一直重跑旧脚本，旧脚本的结果被下一次调用读走，出错后 `DM_FocusedProject` 变成沙盒工程（实测出错、恢复后都不会把 run 文件加进工作区）。
- `run_altium_script` 失败时看 `error`（v0.5.1 源码；前五类在 AD23 上实测过，最后两类只读了源码）：
  | `error` | 含义 |
  |---|---|
  | `refused before execution: ...` | 有没声明的变量，没发给 AD |
  | `script error` | 被沙盒 `except` 抓到的运行时错误：`altium_message` 是 AD 的报错，`last_step_reached` 之后那句出错。执行器没事，立刻返回 |
  | `compile error` | 语法错误，什么都没执行。`location.line` 是你提交的脚本里的行号（从 `var` 块算起，实测准确） |
  | `run-time error` | AD 弹了 "Continue execution?"（实测：规则查询表达式第一次用到非法关键字时，见 `references/rules-and-drc.md`）。这时 `location` 指的是表达式里的位置，`where` 显示 `sandbox template`，不能拿来找脚本行号 |
  | `no result after N s` | 脚本开始了但没出结果：抓不到的错误（`dismissed_dialog_titles` 里有 `"Error"`）、`Exit`、或者确实没跑完。已经停掉 |
  | `no result after N s: Altium never started the script` | AD 被占着（模态框、用户自己在跑或调试的脚本），MCP 什么都没停。按"模态对话框"处理 |
  | `not run: Altium is showing a script error dialog from a script the MCP did not start` | 错误框是用户自己的脚本弹的，MCP 不动它。请用户处理，或确认后用 UIA 关掉 |
- **`compile error`、`run-time error`、`no result after N s` 这三类，MCP 会自动恢复**：关掉 AD 的错误框（只关脚本错误框和只有 OK 的 Error/Information 框，Confirm、Warning 不动）→ 发 `-REditScript:Stop` → 跑一个探针脚本。返回里 `recovery.recovered: true`、`executor_wedged: false` 就直接接着用（实测这三类之后，下一个脚本都正常）。`script error` 不需要恢复；最后两类 MCP 什么都不动。
- 只有 `executor_wedged: true`（自动恢复失败）才要手动：
  - 先用 `scripts\uia_top.ps1` 看有没有模态框（含主窗口下类名为 `Window` 的 WPF 子窗口），有就按 `references/uia-dialogs.md` 处理。模态框开着时不要发外部命令，它会再拉起一个 X2 进程。
  - 没有模态框就跑 `pwsh -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\recover.ps1`：用正在运行的 X2（见"定位 AD 和 MCP"）发 `-REditScript:Stop`；`-DryRun` 只打印路径。
  - 然后跑一个两行的小脚本确认执行器正常。

## 模态对话框

- ECO、DRC 设置、Update Footprints、提示框这类模态框开着时，AD 不接 MCP 的请求。v0.5.1（读源码）：
  - 除 `run_altium_script` 外的工具，20 秒内 AD 没接请求就放弃，返回 `"Altium did not start the command (not executed). ..."`（AD 没在运行时要等它冷启动，最多 240 秒）。接了请求但 120 秒内没回结果的，MCP 判定脚本停在调试器里，发 Stop。
  - 每次请求 MCP 都会再拉起一个 X2 进程，弹 "Information"（"another instance … busy"）。MCP 放弃请求时会顺手关掉这种只有 OK 的 Error/Information 框；手动处理时用 `uia_msg.ps1 -Title Information -ClickOK`。
  - `run_altium_script` 等满 `timeout_seconds` 后报 `Altium never started the script`，什么都不停。它在等待期间 6 秒后会关掉 X2 的 `#32770` 框和标题为 Error/Warning/Information/Confirm 的 `TMessageForm`（用户开着的 Confirm 也会被关掉），ECO、DRC 设置这类窗体不动。
- 处理顺序：`uia_top.ps1` 看有哪些 X2 实例和窗口 → 有残留的 busy 框就关掉 → 用 UIA 处理对话框 → `get_server_status` 加一个两行脚本确认恢复。
- 会话里没有 computer use 时，用 PowerShell + UI Automation 操作对话框，效果一样。窗口类名、控件、哪些做法不灵：`references/uia-dialogs.md`。

## 保存、关闭和重开

- **沙盒里可以直接保存文档**（v0.5.1 在 AD23 上实测 PcbDoc）：`SaveDoc(路径)`（先置修改标志再 `DoFileSave('')`），或者 `Doc.DoFileSave('')`（返回 -1，之后 `Modified` 为 0）。文件当场写盘，不弹框，也不生成 recovery copy。v0.5.0 用 RunScript 跑沙盒工程时会弹 "A command is currently active ... save copy?"，v0.5.1 没再出现。万一还弹，**选 No，不要选 Yes**（Yes 会另存一个 recovery copy）。
- 外部命令也能保存（等同于 Ctrl+S，保存**焦点**文档，所以先 `Client.ShowDocument(Client.OpenDocument(...))` 切过去）。保存工程文件用它，沙盒里保存 `.PrjPcb` 没测过：
  - 文档：`-RWorkspaceManager:SaveObject(ObjectKind=Document|SaveMode=Standard)`
  - 工程（`.PrjPcb`）：`-RWorkspaceManager:SaveObject(ObjectKind=Project|SaveMode=Standard)`
  之后等 4～6 秒，查文件的 LastWriteTime，再用 `uia_top.ps1` 确认没有弹框。
- 如果用户按 Ctrl+S 也弹 "A command is currently active"，说明有脚本在 `PCBServer.PreProcess` 之后崩了，没执行 `PostProcess`（v0.5.0 时观察到的），按 Esc 没用。
  处理：用沙盒补调 `PCBServer.PostProcess`，一次一个，直到 Ctrl+S 不再弹警告，再保存。
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
  - 显示缩放比例大于 100% 时也截整个窗口（v0.5.1 修复；v0.5.0 只截到左上角一块）。判断布局仍以数据为准。
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