# 调用进程

进程就是 AD 的菜单命令，名字写成 `服务器:命令`（`PCB:Zoom`、`WorkspaceManager:Compile`），参数是 `名=值|名=值` 的字符串。脚本里能做而 API 不方便做的事（缩放、选择、出报告、发布 PDF、编译工程）都可以调进程。

## 名字和参数先查

**进程名写错不报错。** 实测 `RunProcess('PCB:PCBLayerSet')`（上游说明里的名字，AD23 没有这个命令）不报错、不弹框，什么也不发生。所以每个进程名都先查：

```
python -X utf8 <本 skill 目录>/scripts/lookup.py PCB:Zoom
python -X utf8 <本 skill 目录>/scripts/lookup.py -s "zoom|redraw"
```

- 数据在 `data/processes.json`，从 AD 安装目录的 `System\*.ins`（各服务器声明的命令）和 `System\*.rcs`（菜单、工具栏、快捷键实际发出的命令和参数）提取。
- 输出里"AD 菜单传的参数"是 AD 自己在用的参数组合，可以原样照抄。
- 菜单以外的参数只能从示例脚本或实测得到，见下表。参数是否生效要在 AD 里看效果（截图，或读回对象状态）。
- 两处都查不到的名字当作不存在。`.ins` 也不全：`PCB:SelectNext` 只出现在 `.rcs` 菜单里。

## 两种调用写法

```
{ 1. 参数栈：逐个加参数，结果也从参数栈读 }
ResetParameters;
AddStringParameter('ObjectKind', 'Netlist');
AddIntegerParameter('Index', 4);
AddStringParameter('ReturnGeneratedDocuments', 'True');
RunProcess('WorkspaceManager:GenerateReport');
GetIntegerParameter('Result', I1);        { var 参数，要传变量 }
GetStringParameter('File1', S1);

{ 2. 参数写成一整串 }
Client.SendMessage('PCB:Zoom', 'Action=Redraw', 255, Client.CurrentView);
```

- `AddColorParameter(Name, Red, Green, Blue)` 加颜色参数。
- `Client.SendMessage` 的第三个参数是参数缓冲区的最大长度，示例里写 255 或 1024。它注册在 `IProcessLauncher` 上，不在 `IClient` 上；altium-mcp 实测能用，`lookup Client.SendMessage` 会说明这两点。
- 字典里还有 `Client.PostMessage(...)`（异步，同样只注册在 `IProcessLauncher` 上）和 `Client.CommandLauncher.LaunchCommand(...)`，参数同 `SendMessage`，都没实测。
- 外部命令行也能调进程：`X2.EXE -RPCB:UpdateFootprints`，用法见 altium-mcp。

## 示例脚本里的参数

菜单不传、只在官方示例里出现的参数。示例是老版本写的，在 AD23 上先实测。

| 进程 | 参数 | 示例 |
|---|---|---|
| `WorkspaceManager:GenerateReport` | 网表：`ObjectKind=Netlist`、`Index`（示例注释：1 EDIF、2 Multiwire、3 Pcad、4 Protel、5 Verilog、6 VHDL、7 XSPICE）、`ReturnGeneratedDocuments=True`；结果 `Result`（0 是失败）、`File1` | `Processes/ShowNetList.pas` |
| `WorkspaceManager:GenerateReport` | 装配、BOM：`ObjectKind=Assembly\|Index=2`、`ObjectKind=Report\|Kind=SimpleBOM\|Target=Document` | `PCB/PCB Outputs/PCBOutputGenerator.pas` |
| `WorkspaceManager:Print` | 发布 PDF：`Action=PublishToPDF`、`ObjectKind=OutputSingle`、`SelectedName1`…、`DisableDialog`、`OutputFilePath`、`OpenOutput`、`ZoomLevel`、`FitSCHPrintSizeToDoc`、`MarkPins` 等 | `Processes/PublishToPDFScript.pas` |
| `PCB:PlacePolygonPlane` | `Layer`、`Name`、`HatchStyle`、`TrackWidth`、`GridSize`、`PourOver`、`RemoveDead`、`PolygonType`；顶点 `Kind0`/`Vx0`/`Vy0`… | `Processes/PlacePCBPolygon.pas` |
| `Pcb:SetupPreferences` | 层颜色 `TopSignalColor`、`Mid1Color`…（十进制颜色值） | `Processes/pcbcolor.pas` |
| `Pcb:DocumentPreferences` | 层显示 `TopSignal`、`Mid1`…（`True`/`False`） | `Processes/pcblayer.pas` |
| `Client:RunCommonDialog` | `Dialog=Color`、`Color`；结果 `Result`、`Color` | `Processes/RunCommonDialog.pas` |
| `Sch:PlacePort` | `Location.X/Y`、`Style`、`IOType`、`Alignment`、`Width`、`Name`、`AreaColor`、`TextColor` | `Processes/PlaceSchPort.pas` |
| `Sch:PlaceWire`、`Sch:PlacePowerPort`、`Sch:AskForXYLocation`、`IntegratedLibrary:PlaceLibraryComponent` | 坐标、方向、库和元件名；`AskForXYLocation` 的结果 `LocationX`/`LocationY`/`Result` | `Processes/CirWiz.pas` |
| `Sch:Select`、`Sch:Deselect`、`Sch:Clear` | `Sch:Select`、`Sch:Deselect` 用 `Action=InsideArea`、`Action=All` 等（菜单里也有）；`Sch:Clear` 不带参数，删除选中的对象 | `Processes/Clrins1.pas` |
| `Sch:Copy`、`Sch:Paste`、`Sch:ToggleSelection` | | `Processes/Quikcopy.pas` |
| `SimView:ImportWaveforms` | `DocumentFilename`、`FileName`、`ChartType`、`PlotWaves0`… | `Processes/ImportWaveforms.pas` |
| `WorkspaceManager:OpenObject` | 新建工程：`ObjectKind=NewAnything\|Kind=PcbProject`（菜单里也有） | `WSM/AddDocToProject.pas` |
| `WorkspaceManager:SaveObject` | `ObjectKind=Document`、`SaveMode=Standard`、`FileFormat` | `SCH/Circad Translator/ImportUtils.pas` |

层显示和层颜色改用 API 时的实测做法见 altium-mcp 的 pcb-scripting.md "层"。

## 上游说明里对不上的进程

| 上游写法 | AD23 |
|---|---|
| `PCB:PCBLayerSet`、`PCB:PCBChangeSystemColors` | 没有这两个命令（`PCBLayerSet` 实测调用无反应）。层显示、层颜色见上表的 `pcblayer.pas`、`pcbcolor.pas` |
| `Sch:ZoomSelected`、`Sch:Zoom` 加 `Action=Selected` | 菜单用的是 `Sch:Zoom` 加 `Object=Selected`（altium-mcp 实测）。PCB 是 `PCB:Zoom` 加 `Action=Selected` |
| `PCB:RunQuery` 加 `Index`、`Expression` | 按表达式查，菜单用的参数名是 `Expr=<查询表达式>`，配合 `Apply=True`、`Select=True`、`Zoom=True`、`Mask=True` 等。`Index` 只和 `Source=Favorite`、`Source=History` 一起用，是收藏、历史列表里的序号。原文用 `lookup PCB:RunQuery` 看 |
| `PCB:Select` 加 `ObjectKind=Component` | 菜单里没有 `ObjectKind`。`PCB:Select` 的主参数是 `Scope=...`；另有 `ContextObject=Component`/`Room`（只和 `Scope=ComponentConnections`、`ComponentNets`、`RoomConnections` 一起用）、`UpdateCaption=False`、`ContextSensitive=True` |
| `Sch:PlaceIntegratedComponentFromDB` | 没有这个命令 |
| `Pcb:SetupPreferences` 加 `TrackQuality=Draft` 等显示质量参数 | 菜单和示例里都没有，没核实 |
