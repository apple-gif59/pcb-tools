# 写法模式

调用顺序和 DelphiScript 的语言要点，从 coffeenmusic/altium-scripts-skill 的手写说明里挑出来、改正后迁过来。代码里的名字都用 `lookup` 核对过 AD23 字典；标"实测"的在 AD23 上跑过，其中多数结论在 altium-mcp skill 里，细节以那边为准，这里只给指针。和 AD23 对不上的上游说法列在文末。

每节末尾列出做同一件事的官方示例（`references/scripts/` 下），要完整程序时直接读示例。

## 语言要点

- **声明类型不影响运行**：`Var X;` 不写类型也能跑，成员按运行时的对象解析。写上类型（`Board : IPCB_Board;`）方便对照字典查成员：`lookup IPCB_Board.<成员>`。
- **集合**用 `MkSet(eTrackObject, eArcObject)`，不写 `[...]`；`InSet(x, s)`、`SetUnion(a, b)`、`MkSetRange(lo, hi)`。`Format('%s=%d', [S, I])` 的参数是开放数组，照常写方括号。`StringReplace` 的 `Flags` 也是集合：写 `MkSet(rfReplaceAll)`，直接传 `rfReplaceAll`（= 0）只替换第一处，不报错（实测）；沙盒里也可以用预置常量 `REPLACEALL`。
- **带下标的属性**：字典里写成 `property LayerColors_V6[L: TV6_Layer]` 的，读取时 `Opt.LayerColors_V6[eTopLayer]` 和 `Opt.LayerColors_V6(eTopLayer)` 都能用（实测）；赋值用 `[]`（altium-mcp 实测）。官方示例 `PCB/PCB Rules/ModifyWidthRules.pas` 赋值也写 `()`，AD23 上没测过。
- **getter/setter 照字典写**：`LayerColors_V6` 的 getter 是 `GetState_LayerColors`，按属性名猜的 `GetState_LayerColors_V6` 不存在，调用会报错并卡住执行器（实测）。
- **常量**只能是简单值。上游说明说不支持 `set of` 类型的常量，要用字符串加 `Pos` 代替（没实测）。
- **完整脚本**（脚本工程里的 .pas）的入口是无参数的过程。File » Run Script 对话框只列出无参数的过程，辅助过程加一个哑参数（`Dummy : Integer`）就不会出现在列表里（上游说明）。
- **命令行运行**：`X2.EXE -RScriptingSystem:RunScript(ProjectName="<.PrjScr 路径>"|ProcName="<单元名>><过程名>")`，altium-mcp 的 `recover.ps1` 就这样运行 `Closer>Run`（实测）。
- **`run_altium_script`** 只接受语句体，用沙盒的预置变量；`try/except` 抓不到运行时错误，出错后 `finally` 也不执行（altium-mcp 实测）。所以先用几行的小脚本把每条语句跑通，再组装成循环。下文模板和示例里的 `Exit` 在语句体里不能用（结果不会写盘，见 altium-mcp），要改成 `if ... then ... else`。

## PCB

### 改动和撤销

```
PCBServer.PreProcess;

{ 新建：先设好全部属性（含 Net），再加到板上并登记 }
Track := PCBServer.PCBObjectFactory(eTrackObject, eNoDimension, eCreate_Default);
Track.X1 := MilsToCoord(1000);  Track.Y1 := MilsToCoord(1000);
Track.X2 := MilsToCoord(2000);  Track.Y2 := MilsToCoord(1000);
Track.Layer := eTopLayer;  Track.Width := MilsToCoord(10);
Board.AddPCBObject(Track);
PCBServer.SendMessageToRobots(Board.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Track.I_ObjectAddress);

{ 修改：属性改动夹在 BeginModify/EndModify 之间 }
PCBServer.SendMessageToRobots(Track.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
Track.Width := MilsToCoord(20);
PCBServer.SendMessageToRobots(Track.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);

PCBServer.PostProcess;
```

- 一对 `PreProcess`/`PostProcess` 是一步撤销，分几对就是几步（示例 `PCB/Undo.pas`）。整批删除几千个图元放在同一对里也没问题（altium-mcp 实测）。
- 网络要在 `AddPCBObject` 之前设，否则 `InNet(...)` 匹配不到（altium-mcp 实测，见其 pcb-scripting.md "临时测试对象"）。
- 字典里还有 `Obj.BeginModify`/`Obj.EndModify` 方法和 `Board.NewUndo`，没实测它们和上面的消息写法是否等价。
- **删除**：遍历时只把对象收进 `TInterfaceList`，销毁迭代器后再逐个 `Board.RemovePCBObject(Obj)`，不要边遍历边删（altium-mcp 实测）。altium-mcp 的清理流程在每次 `RemovePCBObject` 后还向板发一次 `PCBM_BoardRegisteration`，示例 `PCB/DeletePCBObjects.pas` 没发。
- **元件和它的图元**：`Comp.AddPCBObject(Pad)` 后用 `SendMessageToRobots(Comp.I_ObjectAddress, ...)` 向元件登记，元件本身再加到板上（示例 `PCB/CreateComponentOnPCB.pas`）。

示例：`PCB/Undo.pas`、`PCB/CreatePCBObjects.PAS`、`PCB/CreateAVia.pas`、`PCB/DeletePCBObjects.pas`、`PCB/CreateComponentOnPCB.pas`。

### 遍历

```
Iter := Board.BoardIterator_Create;
Iter.AddFilter_ObjectSet(MkSet(eTrackObject, eArcObject));
Iter.AddFilter_AllLayers;
Iter.AddFilter_Method(eProcessAll);
Prim := Iter.FirstPCBObject;
While Prim <> Nil Do
Begin
    If (Prim.Layer = eTopLayer) And Not Prim.InComponent Then List.Add(Prim);
    Prim := Iter.NextPCBObject;
End;
Board.BoardIterator_Destroy(Iter);
```

- 按层筛选在循环里判断 `Prim.Layer`。`AddFilter_LayerSet` 对机械层不起作用，`AddFilter_LayerSet(AllLayers)` 还会漏掉 16 以上的机械层（altium-mcp 实测）。
- 按区域：`Board.SpatialIterator_Create` → 同样的过滤 → `AddFilter_Area(X1, Y1, X2, Y2)` → `Board.SpatialIterator_Destroy(Iter)`。
- 元件或网络的成员：`Comp.GroupIterator_Create` / `Comp.GroupIterator_Destroy(Iter)`，`IPCB_Net` 也继承自 `IPCB_Group`，用法相同。`Prim.IsFreePrimitive` 区分不属于元件的图元。
- 封装库：`Lib := PCBServer.GetCurrentPCBLibrary` → `Lib.LibraryIterator_Create` → `SetState_FilterAll` → `FirstPCBObject`/`NextPCBObject`（得到 `IPCB_LibComponent`）→ `Lib.LibraryIterator_Destroy(Iter)`。
- 按位号直接取元件：`Board.GetPcbComponentByRefDes('U1')`。

示例：`PCB/PCB Iterators/`（`Count_Pads.pas`、`IterateNets.PAS`、`SpatialIterator.Pas`、`LibraryIterator.pas` 等）。

### 其他

- **拿板子**：`Board := PCBServer.GetCurrentPCBBoard`。它返回焦点文档的板子，焦点在 PcbLib 时悄悄返回库的板子，所以先切焦点再核对 `Board.FileName`（altium-mcp）。
- **刷新**：`Board.ViewManager_FullUpdate`、`Board.GraphicalView_ZoomRedraw`，或 `PCB:Zoom` 加 `Action=Redraw`（见 `processes.md`）。
- **交互取点、选对象**（`Board.GetObjectAtCursor`、`ChooseLocation`、`ChooseRectangleByCorners`）会等用户在 AD 里点，只能用在完整脚本里。
- **规则和类**：`PCBServer.PCBRuleFactory(eRule_MaxMinWidth)`、`PCBServer.PCBClassFactoryByClassMember(eClassMemberKind_Net)`，设好属性后 `Board.AddPCBObject`。优先级、范围表达式、各类规则的坑见 altium-mcp 的 rules-and-drc.md；示例 `PCB/CreateRules.pas`、`PCB/PCB Rules/`。
- **封装库里建封装**：`PCBServer.CreatePCBLibComp` → `Lib.RegisterComponent(Fp)` → `Fp.AddPCBObject(...)` → `Lib.CurrentComponent := Fp`。库板原点和导航列表的坑见 altium-mcp 的 pcblib-and-eco.md；示例 `PCB/CreateFootprintInLibrary.pas`。
- **层**：层号、改层颜色、层的显示、层叠都见 altium-mcp 的 pcb-scripting.md。

## 原理图

### 改动和撤销

```
Doc := SchServer.GetCurrentSchDocument;
If Doc.ObjectID = eSchLib Then Exit;          { eSheet = 32 是原理图，eSchLib = 33 是符号库；沙盒里改成 if/else }

SchServer.ProcessControl.PreProcess(Doc, '');
Port := SchServer.SchObjectFactory(ePort, eCreate_GlobalCopy);
Port.Location := Point(MilsToCoord(500), MilsToCoord(500));
Port.Name := 'P1';
Doc.RegisterSchObjectInContainer(Port);
SchServer.RobotManager.SendMessage(Doc.I_ObjectAddress, c_BroadCast, SCHM_PrimitiveRegistration, Port.I_ObjectAddress);

SchServer.RobotManager.SendMessage(Port.I_ObjectAddress, c_BroadCast, SCHM_BeginModify, c_NoEventData);
Port.Name := 'P2';
SchServer.RobotManager.SendMessage(Port.I_ObjectAddress, c_BroadCast, SCHM_EndModify, c_NoEventData);
SchServer.ProcessControl.PostProcess(Doc, '');
Doc.GraphicallyInvalidate;
```

- `SchServer.ProcessControl` 不在 `ISch_ServerInterface` 上，它注册在 `IServerModule`、`IClient` 上，能用（altium-mcp 实测；`lookup` 会说明这两点）。
- 创建模式（`SchObjectFactory` 的第二个参数，`PCBObjectFactory` 的第三个）：官方 PCB API 文档只说它决定新对象的默认属性取自 Preferences 对话框，还是取编辑器内部的默认值。从名字看，`eCreate_GlobalCopy` 取的是 Preferences 那份。示例里 Port、Wire、Line 多用 `eCreate_GlobalCopy`，参数、引脚、PCB 对象多用 `eCreate_Default`。AD23 上实测两种模式建出的 Port、Parameter，颜色、宽度、字体都一样。要确定的属性在创建后显式赋值，选哪种都行。
- 子对象（元件的参数、引脚）：`Comp.AddSchObject(Param)`，再向 `Comp.I_ObjectAddress` 发 `SCHM_PrimitiveRegistration`。
- **删除**：先收集，再 `Doc.RemoveSchObject(Obj)`（子对象用 `Comp.RemoveSchObject(Param)`），示例在删除后同样向容器发 `SCHM_PrimitiveRegistration`。

示例：`SCH/CreateSchObjects.pas`、`SCH/PlaceSchObjects.PAS`、`SCH/DeleteSchObjects.pas`、`SCH/ReplaceSchObjects.pas`、`SCH/UserDefinedParameters/ComponentParameters.pas`。

### 遍历

```
Iter := Doc.SchIterator_Create;
Iter.AddFilter_ObjectSet(MkSet(eSchComponent));
Comp := Iter.FirstSchObject;
While Comp <> Nil Do
Begin
    PIter := Comp.SchIterator_Create;             { 元件的子对象：参数、引脚、模型 }
    PIter.AddFilter_ObjectSet(MkSet(eParameter));
    Param := PIter.FirstSchObject;
    While Param <> Nil Do
        Param := PIter.NextSchObject;
    Comp.SchIterator_Destroy(PIter);
    Comp := Iter.NextSchObject;
End;
Doc.SchIterator_Destroy(Iter);
```

- 迭代器返回 `ISch_BasicContainer`，循环里读的成员按实际类型查：元件 `lookup ISch_Component.<成员>`，参数 `lookup ISch_Parameter.<成员>`。
- 元件的 Comment 也作为名为 `Comment` 的参数出现在 `eParameter` 子对象里；位号不是参数，是单独的 `eDesignator` 子对象（altium-mcp 实测）。
- 文档的完整路径用 `Doc.DocumentName`；`ISch_Document` 没有 `FileName`，读它会卡住执行器（实测，`lookup` 会说明）。
- 只要顶层对象：`Iter.SetState_IterationDepth(eIterateFirstLevel)`。
- 按区域：`Doc.ChooseRectangleInteractively(Rect, ...)` 取矩形（交互），`Iter.AddFilter_Area(Rect.Left, Rect.Bottom, Rect.Right, Rect.Top)`。
- 符号库：`Lib.SchLibIterator_Create` 遍历库里的符号，用 `Lib.SchIterator_Destroy` 销毁。

示例：`SCH/libiterator.pas`、`SCH/SymbolPrimsIterator.pas`、`SCH/FetchParamsOfComp.pas`。

### 库和放置

- **在库里建符号**：`SchServer.SchObjectFactory(eSchComponent, eCreate_Default)`，设 `LibReference`、`Designator.Text`，`AddSchObject` 加矩形和引脚，最后 `Lib.AddSchComponent(Comp)`、`Lib.CurrentSchComponent := Comp`（示例 `SCH/createcomp_in_lib.pas`）。改已有符号的坑见 altium-mcp 的 pcblib-and-eco.md。
- **从库放元件**：`IntegratedLibraryManager.PlaceLibraryComponent('2N3904', 'Miscellaneous Devices.IntLib', 'Orientation=1|Location.X=...|Location.Y=...')`（示例 `SCH/CompReplace/ReplaceSelectedComponent.PAS`），或进程 `IntegratedLibrary:PlaceLibraryComponent`（示例 `Processes/CirWiz.pas`）。
- **字体**：`SchServer.FontManager.GetFontID(Size, Rotation, Underline, Italic, Bold, StrikeOut, FontName)`，结果赋给对象的 `FontID`。

## 工作区和项目

- `Prj := GetWorkspace.DM_FocusedProject; Prj.DM_Compile;` 编译之后才有 `DM_PhysicalDocuments`（层次展开后的图纸）以及其中的元件、网络、引脚；`DM_LogicalDocuments` 是工程里的源文件。示例 `WSM/ProjectReporter.pas`、`SCH/usingWSMInterfaces.pas`。
- **变体**：
  ```
  PV := Prj.DM_CurrentProjectVariant;
  CV := PV.DM_FindComponentVariationByUniqueId(Comp.DM_UniqueId);
  If CV <> Nil Then
      If CV.DM_VariationKind = eVariation_NotFitted Then ...
  ```
- **Messages 面板**：`MM := GetWorkspace.DM_MessagesManager` → `ClearMessages` → `BeginUpdate` → `AddMessage(类别, 文本, 来源, 文档, 回调进程, 回调参数, 图标序号, False)` → `EndUpdate` → `GetWorkspace.DM_ShowMessageView`。
- **打开文档**：`Client.ShowDocument(Client.OpenDocument('PCB', Path))`。不要在脚本里 `DoFileSave`，会弹 "A command is currently active"（altium-mcp）。

## 文件和对话框

- 文本文件：`TStringList` 的 `LoadFromFile`/`SaveToFile`。沙盒里 `SaveToFile` 写出的是 GBK（altium-mcp 实测）。
- 设置：`Ini := TIniFile.Create(ClientAPI_SpecialFolder_AltiumApplicationData + '\MyScript.ini')`，`ReadString`/`WriteString` 等，用完 `Ini.Free`。
- 外部程序：`RunApplication(CommandLine)` 返回错误码，`GetErrorMessage(Code)` 转成文字（示例 `Processes/ShowNetList.pas`）。
- 状态栏：`Client.GUIManager.StatusBar_SetState(0, Msg)`。
- `ShowMessage`、`ConfirmNoYes`、`InputBox` 这类对话框只在完整脚本里用；沙盒里结果写进 `ResultText`。示例里常见的 `InputQuery` 字典里没有，没在 AD23 上试过。

## 没有迁过来的上游说法

| 上游说法 | AD23 |
|---|---|
| `Board.LayerColor[L] :=` 改层颜色 | 只读，写入卡死执行器；用 `PCBServer.SystemOptions.LayerColors_V6[L]`（altium-mcp 实测） |
| `Board.LayerIsDisplayed[L] :=` 切换显示 | 能赋值，不影响显示（altium-mcp 实测） |
| `AddFilter_LayerSet` 按层过滤 | 见上文"遍历" |
| 模板用 `Try/Finally` 保证 `PostProcess`，`Try/Except` 抓错误 | 沙盒里都不可靠（altium-mcp 实测） |
| `DM_VariationType` | 不存在，用 `DM_VariationKind` |
| `eRoomObject` | 不存在，Room 是规则（`eRuleObject`，`eRule_ConfinementConstraint`） |
| `eDrillDrawingLayer` | 不存在，是 `eDrillDrawing` |
| `eJustify_CenterCenter` | 不存在，是 `eJustify_Center` |
| 进度条 `InitStatus`/`UpdateStatus`/`FinishStatus` | 不存在（`UpdateStatus` 只是 `TDataSet` 的同名成员，和进度条无关） |
| Messages 面板图标序号对照表 | 没有出处，没迁 |
| `PCB:PCBLayerSet` 等进程 | 见 `processes.md` 末尾 |

规则和 3D 体上也有几处属性能赋值但不生效，或者算出来的值不对：阻焊外扩只认 `SetState_IsTenting_Top/Bottom`、元件带 3D 体时高度规则只看最大的 `OverallHeight`、Room 的外接矩形不会自动算对。见 altium-mcp 的 rules-and-drc.md 和 pcb-scripting.md "3D 体"。
