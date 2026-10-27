# 用 UI Automation 操作 AD 的对话框（AD23 实测）

ECO、DRC 设置、Update PCB 这类模态对话框，MCP 和沙盒都点不了。会话里没有 computer use 时，用 PowerShell + UI Automation 操作，效果一样。

## 先知道的几件事

- **对话框开着时，AD 不接 MCP 的请求**（`get_screenshot` 也一样）：v0.5.1 的工具约 20 秒后返回 "Altium did not start the command (not executed)"，`run_altium_script` 等满超时后报 "Altium never started the script"（读源码，见 SKILL.md "模态对话框"）。MCP 每次调用还会再拉起一个 X2 实例，它弹一个 "Information" 框（"There is another instance of running, but it is busy… try again later"，类名 `TMessageForm`）。MCP 放弃请求时会自己关掉这个框；还开着的话，用 `uia_msg.ps1 -Title Information -ClickOK` 关掉（多余的 X2 实例随之退出）。
  处理顺序：关掉残留的 busy 框 → 用 UIA 处理对话框 → `get_server_status` 加一个两行的小脚本，确认 MCP 恢复。
- 脚本都在本 skill 的 `scripts\`，用 PowerShell 7 跑：
  `pwsh -NoProfile -ExecutionPolicy Bypass -File <本 skill 目录>\scripts\<脚本> -Out <结果.txt> ...`
  结果写进 `-Out` 文件（UTF-8 带 BOM），再用 Read 看。
- 鼠标点击要先 `SetProcessDPIAware`（脚本里已做），坐标用物理像素。点之前用 `AutomationElement.FromPoint` 确认光标下就是目标，点完回读状态。
- 文本框、数值框改值用 `WM_SETTEXT`（`uia_setvalue.ps1`），它会回读确认。
- AD 进程没了要重启时：先从注册表取安装目录，`X2.EXE` 就在它下面：
  `$b = Get-ItemProperty 'HKLM:\SOFTWARE\Altium\Builds\*' | Sort-Object { [version]$_.Version } -Descending | Select-Object -First 1; $x2 = Join-Path $b.ProgramsInstallPath 'X2.EXE'`
  （`Builds` 下子键的 `ProgramsInstallPath` 是安装目录；子键不止一个时，这条命令取 `Version` 最高的）。再 `Start-Process $x2 -ArgumentList '"<PrjPcb 完整路径>"'`，等它起来（约一分钟）。工程里的文档都是关着的，用沙盒 `Client.ShowDocument(Client.OpenDocument('PCB', 路径))` 打开。
- 对话框里改的设置，以"点 OK 提交 → 重新打开对话框 → 再读"为准（DRC 对话框点完勾选框，当场 UIA 读到的还是旧值）。
- 提示框 `TMessageForm` 的 OK 按钮有两种：`TButton` 不支持 Invoke，用 `SendMessage BM_CLICK`；`TXPBitBtn` 用 InvokePattern。`uia_msg.ps1 -ClickOK` 两种都处理。
- 提示框的文字 UIA 读不到时（如标题 "Error" 的框），用 `screen.ps1` 截全屏（DPI-aware，跨多屏），再用 skill `doc-image-viewing` 的 `crop.ps1` 裁出来看。

## 脚本

| 脚本 | 作用 |
|---|---|
| `uia_top.ps1 -Out` | 列出所有 X2 进程的顶层窗口（pid、类名、标题）和它们的子窗口。先跑它，看有几个 X2、开着哪些框 |
| `uia_msg.ps1 -Out -Title <标题> [-ClickOK]` | 列出标题为 `<标题>` 的 `TMessageForm` 里的控件；加 `-ClickOK` 点 OK |
| `uia_dump.ps1 -Out [-Class <窗口类>] [-Title <标题>]` | 导出匹配窗口的全部后代：类型、类名、名字、值、勾选状态、是否可用、矩形（离屏记 off）、hwnd。两个参数都不给时导出除主窗口以外的所有 X2 顶层窗口 |
| `uia_click.ps1 -Out -Class <窗口类> [-Title] -Button <控件名> [-Toggle]` | 按名字找控件，Invoke（或 Toggle），不支持就发 BM_CLICK。不给 `-Out` 时最后写文件会报 "Empty path name"，但点击已经生效 |
| `uia_find.ps1 -Out -Pattern <正则> [-Class TDocumentForm]` | 在某类顶层窗口里按名字或值（正则）找控件，输出类名、名字、值、矩形 |
| `uia_clickat.ps1 -Out -Class <窗口类> -Name <控件名> [-ElemClass] [-DX] [-Double] [-DryRun]` | 鼠标点控件中心（或左边缘 +DX），点前做命中测试，对不上就放弃 |
| `uia_setvalue.ps1 -Out -Class <窗口类> -ElemClass <控件类> -OldValue <现值> -NewValue <新值>` | 找到值等于 `<现值>` 的控件，用 WM_SETTEXT 改值并回读 |
| `uia_wpfdlg.ps1 -Out [-ClickName <按钮名>]` | 列出 AD 主窗口（`TDocumentForm`）里的 WPF 子对话框，按名字 Invoke 按钮 |
| `screen.ps1 -Out <out.png>` | DPI-aware 全屏截图（所有显示器拼在一起），输出宽×高 |
| `eco_rows.ps1 -Out` | 读 ECO 对话框的全部行 |
| `eco_disable.ps1 -Out -Pattern <正则>` | 逐行取消勾选匹配的 ECO 行 |
| `eco_button.ps1 -Out -Button <按钮名>` | 点 ECO 对话框的按钮（Validate Changes / Execute Changes / Close） |

## ECO 对话框（Engineering Change Order）

- 打开：PCB 为当前文档时，外部命令 `-RWorkspaceManager:Compare(ObjectKind=Project|Action=UpdateMe)`。当前文档是 PcbLib 时会报 "Cannot compare a source document against its owner project PCBLIB"。
- 结构：窗口类 `TChangeManagementForm`；列表是 DevExpress `TdxTreeList`，每行是 `TdxTreeList*Node`。
  - 行的 ValuePattern 文本以 `True `/`False ` 开头，就是 Enable 勾选状态，回读可靠。
  - 行不在可视区时，`BoundingRectangle` 是无穷大，直接取整会报错；`Select()` 不会把行滚进来，要在列表中部滚鼠标滚轮。
  - 右键菜单（`TdxBarSubMenuControl`）里的 Enable All / Disable All，UIA Invoke 和鼠标点都**不生效**。
  - 取消勾选的可行做法：逐行用鼠标点 Enable 列的勾选框，点前命中测试、点后回读变成 `False `。`-CheckX`（默认 180）是勾选框的**屏幕绝对 x**（物理像素），对话框挪了位置要先截图量一下。
  - 按钮是 `TXPBitBtn`，支持 InvokePattern。执行后 "Execute Changes" 变灰，各行的 Check/Done 列可读出结果。
- 流程：`eco_rows.ps1` 读全部行 → 确认只有想要的改动；有多余的，用 `eco_disable.ps1` 取消 → 再读一遍 → `eco_button.ps1 -Button "Execute Changes"` → 读 Check/Done → `-Button Close`。
- 比较器没有差异时不弹 ECO，弹 "Comparator Results (No Differences)" 提示框，用 `uia_msg.ps1 -Title "Comparator Results (No Differences)" -ClickOK` 关掉。这也是确认原理图和 PCB 同步的办法。
- ECO 里冒出一批 Remove/Change/Add Rooms 的原因和根治，见 `pcblib-and-eco.md`。

## DRC 对话框（Tools » Design Rule Check）

用来改违规数上限和批量检查哪些规则类型，脚本 API 改不了这两样。只改设置、不在对话框里跑 DRC。

1. 打开：外部命令 `-RPCB:DesignRuleCheck`，等 5 秒。窗口类 `TDesignRuleCheckForm`，标题 `Design Rule Checker [mm]`，默认停在 Report Options 页。
2. 改上限：控件是 `TXPSpinEdit`（name 和 value 都是现值，如 500）。
   `uia_setvalue.ps1 -Out x.txt -Class TDesignRuleCheckForm -ElemClass TXPSpinEdit -OldValue 500 -NewValue 20000`。
   同一页还有默认勾选的 "Create Violations"（DRC 结果留在文档里，见 `rules-and-drc.md`）。
3. 改批量检查项：
   - 左侧树 `DRCTree` 里点 "Rules To Check" 节点：`uia_clickat.ps1 -Out x.txt -Class TDesignRuleCheckForm -Name 'Rules To Check' -ElemClass TdxTreeListTextNode`。
   - 右侧列表 `RulesOnOffList` 每行是 `TdxTreeListTextNode`，value 是"名称 分类 Online Batch"，如 `Component Clearance Placement True False`。用 `uia_dump.ps1 -Class TDesignRuleCheckForm` 列全部行；离屏行 rect 是 off，点不了。
   - 点 Batch 列的勾选框：`uia_clickat.ps1 ... -Name '<规则类型名>' -ElemClass TdxTreeListTextNode -DX <偏移>`。DX 是 Batch 勾选框离行左缘的物理像素：先用 `screen.ps1` 截图、量表头，对话框尺寸或缩放比例变了要重量。
   - 点完 UIA 读到的 value 不刷新，仍是旧值，按第 5 步核对。
4. `uia_click.ps1 -Out x.txt -Class TDesignRuleCheckForm -Button OK` 提交（按钮是 `TXPBitBtn`）。PCB 变成已修改，外部 SaveObject 保存。
5. 核对：重新打开对话框、切到同一页再 dump，看到新状态；核对完 `-Button Cancel` 关掉。保存后读磁盘的 `Design Rule Checker Options6`（`MAXVIOLATIONCOUNT`、`RULESETTOCHECK`）。

## 其他对话框和窗口

- **Component(s) Update Options**（PcbLib 里 `-RPCB:UpdateFootprints` 弹出）：类名 `TComponentUpdateOptions`，7 个 `TXPCheckBox` 默认全选，OK/Cancel 是 `TXPBitBtn`：`uia_click.ps1 -Class TComponentUpdateOptions -Button OK`。
- **TMessageForm 提示框**：MCP 拉起的第二实例弹的 "Information"（busy）框，OK 是 `TButton`；"Comparator Results (No Differences)" 的 OK 是 `TXPBitBtn`。`uia_msg.ps1 -ClickOK` 两种都能点。
  有的提示框（如标题 "Error"，内容 "Cannot compare a source document against its owner project PCBLIB"）文字 UIA 读不到，截屏看。
- **WPF 对话框**不是顶层窗口，是 AD 主窗口（`TDocumentForm`）下类名为 `Window` 的子窗口（Name 是 `Altium.Controls.Wpf.Dialogs.DialogViewModel`）。`uia_top.ps1` 只把它列成 "child window class=Window"。里面的 Button 支持 Invoke：`uia_wpfdlg.ps1 -Out x.txt -ClickName Yes`。
  例：关闭 PcbDoc 时的 "Layer stack has been modified in the PCB. Update with changes?"（Yes/No 加 "Don't ask again"），只在打开过层叠管理器时出现。
- **层叠管理器**（`-RLayerStackManager:OpenPcbLayerStack(Tab=LayerStack|ShowInBoardPlanner=1)`）打开的是主窗口里的文档页 `<文件名> [Stackup]`，不是对话框。里面的数值能用 `uia_find.ps1 -Pattern 'Total Thickness'` 读出来。打开后焦点变成它，保存 PCB 前要切回。
- 分辨窗口属于哪个 X2 实例：`uia_top.ps1` 输出每个顶层窗口的 pid；MCP 拉起的第二实例是启动时间最晚的那个（`Get-Process X2 | Select Id, StartTime`）。
