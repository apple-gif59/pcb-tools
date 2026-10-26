# 改封装、原理图符号和 ECO（AD23 实测）

改库、改原理图实例，再把改动同步到 PCB。对话框的 UIA 操作见 `uia-dialogs.md`。

## 先切对焦点文档

- `PCBServer.GetCurrentPCBBoard` 返回的是**当前焦点文档的板子**。焦点在 PcbLib 时它悄悄返回库的板子，迭代规则得到 0 条，不报错。
  会把焦点切到库的操作：沙盒里打开或取库（`OpenDocument('PCBLIB', …)`、`GetPCBLibraryByPath`），以及 MCP 的 `get_footprint_primitives`。
- 每个脚本开头先切焦点，再核对。PCB 的写法见 SKILL.md"沙盒"一节；库用 `Client.OpenDocument('PCBLIB', 路径)`，核对 `PCBServer.GetCurrentPCBLibrary.Board.FileName`。焦点文档也可以读 `Client.CurrentView.OwnerDocument.FileName`（同一对象有 `.Kind`、`.Modified`）。

## PcbLib

### 读和改封装属性
- 遍历：`Lib := PCBServer.GetCurrentPCBLibrary;` 后用 `Lib.ComponentCount`、`Lib.GetComponent(I)`，或
  ```
  Obj2 := Lib.LibraryIterator_Create; Obj2.SetState_FilterAll;
  Obj3 := Obj2.FirstPCBObject; while Obj3 <> nil do begin ... Obj3 := Obj2.NextPCBObject; end;
  Lib.LibraryIterator_Destroy(Obj2);
  ```
  库封装的名字是 `Obj3.Name`（字符串）；PCB 元件是 `Obj3.Name.Text`。
- 改 Height：在 `PCBServer.PreProcess`/`PostProcess` 之间直接写 `Obj3.Height := MMsToCoord(<高度 mm>)`，不用 BeginModify，回读就是新值。Description 同理，中文从 UTF-8 带 BOM 的文件 `LoadFromFile` 读进来再赋值。
- **改 Height、改 3D 体之后，文档不会自动标成已修改**（改图元会，读出 -1）。外部 `SaveObject` 不看这个标志，照样写盘；先手动 `Client.GetDocumentByPath(路径).Modified := True` 再保存也可以。保存后查文件时间，或 grep 磁盘内容（如 `PATTERN=<封装名>|HEIGHT=<值>mil`）确认。

### 改图元：坐标带库板原点
- 封装不是当前封装时，图元读出来是局部坐标；一旦 `Lib.CurrentComponent := X`，同一图元的坐标就带上库板原点（`Lib.Board.XOrigin/YOrigin` = 500000000，即 50000 mil）。按局部坐标写会把图元扔到很远的地方。
  做法：每次读 `Lib.Board.XOrigin/YOrigin`，坐标写成"原点 + 偏移"；关于 Y 轴镜像写成 `x := 2*XOrigin - x`。
  MCP 的 `get_footprint_primitives` 读当前封装时也多出 50000 mil。
  编辑器用 `PCB:FirstComponent`/`NextComponent` 翻到的封装同样算当前封装。拿不准时，不要套固定公式：先读同一封装里一个已知焊盘的坐标，减去它的局部坐标得到基准，新图元按这个基准写。写完回读，确认新图元和焊盘的相对位置；更新到 PCB 后再按元件位置核对一次（基准错了，图元会在 PCB 上偏出 50000 mil）。
- 改图元：
  ```
  PCBServer.PreProcess;
  PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
  Obj1.x := I2 + I2 - Obj1.x;          // I2 = Lib.Board.XOrigin，关于 Y 轴镜像
  Obj1.y := I3 + MMsToCoord(<dy mm>);  // I3 = Lib.Board.YOrigin
  PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
  PCBServer.PostProcess;
  ```
  圆弧改 `XCenter/YCenter`，线改 `x1/y1/x2/y2`。遍历封装的图元用 `Comp.GroupIterator_Create` / `GroupIterator_Destroy`。
- **改焊盘的锡膏外扩要走焊盘缓存**（实测于 PcbLib 的封装焊盘）：直接写 `Pad.PasteMaskExpansion` 会在 ScriptingSystem 里访问越界（弹 TShowException，执行器卡住），读 `IsTopPasteEnabled` 也会卡住；`PasteMaskEnabled`、`PasteMaskExpansionMode` 赋值后回读不变，等于没改。能用的写法：
  ```
  I1 := MMsToCoord(<外扩 mm 的绝对值>); I1 := 0 - I1;     { 负外扩先算好 }
  Obj5 := Pad.GetState_Cache;
  Obj5.PasteMaskExpansion := I1;
  Obj5.PasteMaskExpansionValid := eCacheManual;
  PCBServer.PreProcess;
  PCBServer.SendMessageToRobots(Pad.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
  Pad.SetState_Cache(Obj5);
  PCBServer.SendMessageToRobots(Pad.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
  PCBServer.PostProcess;
  ```
  中心焊盘做分格开窗：把它的锡膏外扩设成比半边长更负（整块锡膏收掉），再在 Top Paste 层加几块填充当窗口。
- **加图元**只调 `Lib.Board.AddPCBObject(Obj)`，再 `PCBServer.SendMessageToRobots(Obj.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, c_NoEventData)`；它会同时进当前封装的组。
  再调一次 `LibComp.AddPCBObject` 会让组里有两个引用。
- **删图元**用"选中 + Clear"：
  ```
  Client.SendMessage('PCB:DeSelect', 'Scope=All', 255, Client.CurrentView);
  Obj1.Selected := True;   { 对每个要删的图元 }
  Client.SendMessage('PCB:Clear', '', 255, Client.CurrentView);
  ```
  `LibComp.RemovePCBObject` 只把图元移出组，库板上还留着一个 `InComponent=0` 的孤儿；`Board.RemovePCBObject` 不起作用。
- 改完用组迭代器和库板迭代器各导出一遍图元，排序后比较，两边应完全一致；保存、关闭、重开后再比一次。

### create_footprints_batch
- 规格文件要 UTF-8 带 BOM，否则中文按 GBK 解析。格式（MCP docstring，单位 mil，层写名字）：
  ```
  FPLIB|<path>
  FOOTPRINT|<name>|<desc>
  PAD|name|x|y|rot|layer|plated|hole_size|hole_type|hole_width|hole_rot|top_x|top_y|top_shape[|corner_pct[|mode|mid_x|mid_y|mid_shape|bot_x|bot_y|bot_shape]]
  TRACK|x1|y1|x2|y2|width|layer
  ARC|cx|cy|radius|start_angle|end_angle|width|layer
  FILL|x1|y1|x2|y2|rotation|layer
  TEXT|x|y|size|width|rotation|layer|mirror|ttf|text
  REGION|layer|kind|x1|y1|x2|y2|...
  ```
  槽孔焊盘：`PAD|<名>|<x>|<y>|<rot>|Multi Layer|1|<孔宽>|2|<槽长>|0|<top_x>|<top_y>|1`（hole_type 2 = 槽，hole_width = 槽长）。
- 用它建的封装**不出现在 PcbLib 编辑器的导航列表里**，直到库保存、关闭、重开。`Lib.CurrentComponent :=` 能切换脚本操作的对象，但不改编辑器显示的封装，也不改 `PCB:UpdateFootprints` 的目标。

### 把库封装更新到 PCB（Update PCB With Current Footprint）
1. 让编辑器真正显示目标封装：库保存后 `Client.CloseDocument`，重新 `OpenDocument` + `ShowDocument`，再 `Client.SendMessage('PCB:FirstComponent', '', 255, Client.CurrentView)`，循环 `PCB:NextComponent` 直到 `Lib.CurrentComponent.Name` 等于目标（列表按字母序，到末尾后 Next 不动）。
2. PcbLib 为焦点时外部命令 `-RPCB:UpdateFootprints`（不带 `Mode=All`；带了就是 Update All）。弹 "Component(s) Update Options"（`TComponentUpdateOptions`，7 个复选框默认全选），用 `uia_click.ps1 -Class TComponentUpdateOptions -Button OK` 点 OK。
3. 核对是否真的更新了：更新前后各导出一次全板元件快照（位号、Pattern、X−XOrigin、Y−YOrigin、Layer、Rotation、Height）和图元按"类型/层/是否属于元件"的计数，再比较。编辑器显示的不是目标封装时，它更新的是显示的那个；那个封装 PCB 上没用到的话，PCB 没有任何变化、也不标已修改，只有快照比对能发现。
4. 更新后脚本读到的元件外框（`BoundingRectangle`、`BoundingRectangleNoNameComment`）还是更新前的旧值，图元已经是新的。对每个更新过的元件做一次空修改（`PCBM_BeginModify`; `MoveByXY(0, 0)`; `PCBM_EndModify`，包在 `PreProcess`/`PostProcess` 里）再读，外框才对；锁定的元件也能这样刷新，位置不变。
- 翻到底层后：Top Paste → Bottom Paste，Top Overlay → Bottom Overlay，成对的机械层换到配对层，不成对的原地不动。

## SchLib 和原理图实例

- 找原理图元件：`SchServer.GetCurrentSchDocument.SchIterator_Create` 加 `AddFilter_ObjectSet(MkSet(eSchComponent))`，按 `Designator.Text` 匹配。
  当前文档类型：`Doc.ObjectId` = 32 是 SchDoc，33 是 SchLib。
- 子对象按类型过滤，每种只读它有的字段：`Comp.SchIterator_Create` 加 `AddFilter_ObjectSet(MkSet(eParameter))` 这类过滤，一次只取要的类型。读到某种子对象没有的字段时执行器卡死：不加过滤遍历全部子对象再读 `Location`，在 eImplementation 上卡住（它没有 Location）；只读 `ObjectId` 不加过滤也安全。
  可读字段：参数 `Name/Text/IsHidden`；模型（eImplementation）`ModelType/ModelName/IsCurrent/DatafileLinkCount/DatafileLink[0].Location/EntityName`；管脚 `Designator/Name/Location/PinLength/Orientation/Electrical`。
  元件的 Comment 也作为名为 `Comment` 的参数出现在 eParameter 里，值和 `Comp.Comment.Text` 相同；位号不是参数，是单独的 eDesignator 子对象。
- 改实例参数、描述、封装模型：
  ```
  SchServer.ProcessControl.PreProcess(Doc, '');
  SchServer.RobotManager.SendMessage(Comp.I_ObjectAddress, c_BroadCast, SCHM_BeginModify, c_NoEventData);
  Comp.ComponentDescription := S3;  Comp.Comment.Text := '...';
  { 每个参数：SendMessage(Param..., SCHM_BeginModify) ; Param.Text := '...' ; SendMessage(Param..., SCHM_EndModify) }
  { 封装模型：Impl.ModelName := '新封装'; Impl.DatafileLink[0].EntityName := '新封装'; Impl.IsCurrent := True; }
  SchServer.RobotManager.SendMessage(Comp.I_ObjectAddress, c_BroadCast, SCHM_EndModify, c_NoEventData);
  SchServer.ProcessControl.PostProcess(Doc, '');
  ```
  DatafileLink 的 Location 为空（Any）时保持不动，ECO 照样能解析到新封装。
- **只改实例、不改符号是隐患**：实例的 LibReference/DesignItemId 仍指旧符号，以后谁做一次 Update From Libraries，参数和封装就被静默改回旧件，再 ECO 时 PCB 封装也被换回去。所以换料要在 SchLib 里建新符号并改链。
- 复制符号（SchLib 为焦点，不用 PreProcess）：
  ```
  Obj5 := Old.Replicate;                        { 管脚、线、参数、模型都挂在元件下，全部复制 }
  Obj5.LibReference := '新名'; Obj5.DesignItemId := '新名';
  { 子对象迭代 eParameter/eImplementation，改 Param.Text、Impl.ModelName、Impl.DatafileLink[0].EntityName }
  Doc.AddSchComponent(Obj5);
  SchServer.RobotManager.SendMessage(nil, c_BroadCast, SCHM_PrimitiveRegistration, Obj5.I_ObjectAddress);
  Doc.GraphicallyInvalidate;
  ```
  遍历库符号用 `Doc.SchLibIterator_Create` 加 `MkSet(eSchComponent)`，销毁用 `Doc.SchIterator_Destroy`。加之前先确认新名字不存在、新旧子对象数相同。回读用 MCP `get_symbol_primitives` 逐条对比新旧符号。
- 改链：在 SchDoc 里对实例做 PreProcess + SCHM_BeginModify，写 `Comp.LibReference := '新名'; Comp.DesignItemId := '新名';`，EndModify、PostProcess、`Doc.GraphicallyInvalidate`。改链前后编译出的网表应完全一致。ECO 里只会多一行 "Change Component Design Item ID"，执行后 PCB 元件的 `SourceLibReference` 变成新名。
- PCB 元件 `IPCB_Component` 没有 `SourceDesignItemID`，读它报 `Undeclared identifier`；能读的是 `SourceFootprintLibrary`、`SourceComponentLibrary`、`SourceLibReference`、`FootprintDescription`。

## ECO（原理图 → PCB）

- 打开：`Client.ShowDocument(Client.OpenDocument('PCB', 路径))` 让 PCB 成为焦点，再外部命令 `-RWorkspaceManager:Compare(ObjectKind=Project|Action=UpdateMe)`，等约 8 秒。焦点是 PcbLib 时报 "Cannot compare a source document against its owner project PCBLIB"。
- 对话框用 UIA 读行、取消勾选、执行，见 `uia-dialogs.md`。执行前一定读一遍全部行，只留想要的改动。
- **ECO 里冒出整批 Remove/Change/Add Rooms**：工程选项 Class Generation 里各页开着 "Generate Rooms"（`.PrjPcb` 里 `ClassGenCCAutoRoomEnabled=1`），而 PCB 上有脚本建的 Room（如外壳 DWG 生成的禁布/限高 Room）。比较器会提议删掉这些 Room、补上图纸 Room；脚本 Room 如果恰好继承了某个图纸 Room 的 UniqueID，还会被改名成图纸 Room，范围变成 `InComponentClass(...)`，这块禁布区就静默失效了。**这些行绝不能执行。**
  根治（要用户批准，改的是 `.PrjPcb`）：
  ```
  Obj1 := GetWorkspace.DM_FocusedProject;
  for I1 := 0 to Obj1.DM_LogicalDocumentCount - 1 do
  begin
    Obj2 := Obj1.DM_LogicalDocuments(I1);
    if Obj2.DM_DocumentKind = 'SCH' then
    begin
      Obj3 := Obj1.DM_DocumentClassGenerationOptions(Obj2.DM_FullPath);
      Obj3.CompClassAutoRoomEnabled := False;     { CompClassAutoEnabled（元件类生成）保持开 }
    end;
  end;
  Obj1.DM_SetDifferenceLevel(11, 0);   { 11 = Extra Room Definitions，0 = 不检查 }
  Obj1.DM_SetDifferenceLevel(21, 0);   { 21 = Changed Room Definitions }
  Obj1.DM_SetModified;
  ```
  先只读跑一遍：`DM_GetDifferenceLevel(n)` 读现值，`GetWorkspace.DM_GetDifferenceTypeDescription(n)` 读差异类型的名字。
  `.PrjPcb` 的 `[Difference Levels]` 里 TypeN 对应枚举值 N−1，所以落盘是 `Type12=0`、`Type22=0`。保存工程：外部命令 `-RWorkspaceManager:SaveObject(ObjectKind=Project|SaveMode=Standard)`。改完再 Compare 应弹 "Comparator Results (No Differences)"。
  在工程说明（CLAUDE.md）里写明这两项是故意关的，不然以后会被当成误设置改回默认。
