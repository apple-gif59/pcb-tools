# PCB 对象的脚本写法（AD23 实测）

规则、Room、DRC 和模拟检查见 `rules-and-drc.md`；改库和 ECO 见 `pcblib-and-eco.md`。

## 层

- 层号：Top 1、Bottom 32、Top Overlay 33、Bottom Overlay 34、Top Paste 35、Bottom Paste 36、Mech1～16 = 57～72（MechN = 56 + N）、Multi-Layer 74。16 以上的机械层是 67108864 + N（如 M242 = 67109106）。也能直接写常量名（`eTopPaste`、`eMechanical13`）。
- **`AddFilter_LayerSet(MkSet(eMechanical3, ...))` 不会按机械层过滤**，迭代器照样返回其他层的对象，包括封装里的图元。**`AddFilter_LayerSet(AllLayers)` 又会漏掉 16 以上的机械层**。迭代图元一律用 `Obj2.AddFilter_AllLayers;`，在循环里按 `Obj.Layer` 自己判断。
- 读图元的层用 `Obj.Layer`；`Obj.V7Layer.ID` 会卡死执行器。层对象的 V7 号：`Board.LayerStack_V7.LayerObject_V7[eMechanical1].V7_LayerID.ID`。
- **`Board.LayerColor[...]` 只能读，写入会让执行器卡死。**
  改层颜色用 `PCBServer.SystemOptions.LayerColors_V6[eMechanicalN] := $00BBGGRR;`。写入后 `Board.LayerColor` 会同步变化，再调用 `ViewManager_FullUpdate` 刷新显示。
- 机械层：`Board.LayerStack_V7.LayerObject_V7[eMechanical1 + n - 1]`，可设 `.MechanicalLayerEnabled`、`.Name`。
- `Board.LayerIsDisplayed[...]` 能赋值，但在 AD23 里不影响显示。只看一层：`Client.SendMessage('PCB:SetCurrentLayer', 'LayerName=TopPaste', 255, Client.CurrentView)`，再 `Client.SendMessage('PCB:SetupPreferences', 'SingleLayerMode=Toggle', 255, Client.CurrentView)`。这个开关在几种单层模式和正常显示之间循环，每发一次截图确认当前是哪种。
- 缩放到区域：`Board.GraphicalView_ZoomOnRect(x1, y1, x2, y2)`，再 `PCB:Zoom` 加 `Action=Redraw`。
- 机械层是否成对看 PCB 的层对设置：元件翻到底层时，成对机械层上的图元自动换到配对层，不成对的原地不动。
- 命令的进程名和参数以 AD 菜单用的为准（如 `PCB:UpdateFootprints`、`PCB:Clear`、`SingleLayerMode = Toggle`），用 altium-script skill 的 `lookup PCB:Xxx` 查，它列出 `<AD 安装目录>\System\*.rcs` 里的全部参数组合。
- TrueType 文字：`UseTTFonts := True`、`FontName := 'SimSun'`，中文能正常显示。

## 沙盒里读写文件

- 读：把数据写成 UTF-8（带 BOM）的文本文件，用 `TStringList.LoadFromFile` 读入，中文能正常读出。拆分每一行用第二个 `TStringList`（`Obj5 := TStringList.Create`，`Delimiter := #9`、`StrictDelimiter := True`、`DelimitedText := 行`）。几千个对象一个脚本就能跑完。
- 写：`TStringList.SaveToFile` 写出的是 **GBK**（ANSI），Python 读要 `.decode('gbk')`。
- 大量结果写文件、再用 Python 分析，`ResultText` 只返回条数。循环里不要放 `SandboxLog`，返回的 steps 会被撑得很长。
- 把 Windows 路径填进 `.pas` 模板的占位符时，**不要用 sed 或 Python 普通字符串替换**：反斜杠会被当成转义，路径变成 `C:SERS…` 或报 `\U` 错误。用 Edit 工具改，或者把路径放进单独的文本文件，让脚本 `LoadFromFile` 读。
- 坐标换算：1 mil = 10000 内部单位，`MMsToCoord`/`CoordToMMs`、`MilsToCoord`；相对板原点要减 `Board.XOrigin/YOrigin`。

## 层叠

```
Obj2 := Obj1.LayerStack_V7;  Obj3 := Obj2.FirstLayer;  Obj5 := Obj2.NextLayer(Obj3);   { 两层板：Top、Bottom }
Obj3.CopperThickness := MMsToCoord(<铜厚 mm>);  Obj5.CopperThickness := MMsToCoord(<铜厚 mm>);
Obj4 := Obj3.Dielectric;                     { Top 下面那层芯板 }
Obj4.DielectricHeight := MMsToCoord(<芯板厚 mm>);  Obj4.DielectricConstant := <Dk>;
Obj4.DielectricMaterial := '<材料>';  Obj4.DielectricType := 1;   { 0 无、1 Core、2 PrePreg、3 Surface、4 Film }
{ 两层阻焊：Obj2.DielectricTop / Obj2.DielectricBottom }
```
- 全部赋值放在一对 `PreProcess`/`PostProcess` 里，不用 BeginModify。
- `DielectricType` 是 0（无介质）的芯板，即使厚度、Dk 都有值，MCP 的 `get_pcb_layer_stackup` 也报 "No Dielectric"、不计入总厚。设成 1 后才计入。
- 两层板 Bottom 层的 `.Dielectric` 是一块不存在的介质（能读出值，但 Board6 和层叠管理器里都没有），只改 Top 的 `.Dielectric`。
- AD 的总厚包含两层阻焊（各 0.01016）。芯板厚 = 目标总厚 − 铜 − 阻焊。回读看磁盘 Board6 的 `LAYER_V8_*` 字段，或层叠管理器（`uia-dialogs.md`）。

## 网络类和焊盘类

- 网络类用 MCP 的 `create_net_class(class_name, net_names)`（返回值的坑见 SKILL.md）。
- 焊盘类：
  ```
  PCBServer.PreProcess;
  Obj4 := PCBServer.PCBClassFactoryByClassMember(eClassMemberKind_Pad);
  Obj4.SuperClass := False;  Obj4.Name := '<类名>';
  Obj1.AddPCBObject(Obj4);
  Obj4.AddMemberByName('<位号>-<焊盘名>');
  PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj4.I_ObjectAddress);
  PCBServer.PostProcess;
  ```
  规则范围里用 `InPadClass('<类名>')`。
- 回读类：迭代 `eClassObject`，读 `Name`、`MemberKind`（Net 0、Component 1、Pad 3、Layer 4）、`SuperClass`，再从 0 起读 `MemberName[I]` 直到返回空串。

## 批量修改

- 批量删除：先用 `Obj5 := TInterfaceList.Create` 把要删的对象收集起来，迭代结束后再逐个 `RemovePCBObject`。不要边迭代边删。
  整批删除可以放在同一对 `PreProcess`/`PostProcess` 里，几千个图元一个脚本跑完。
- 删之前和删之后各导出"对象类型\t层\t是否属于元件"的计数，按层和类型做差，确认只少了想删的。

## 元件

- **只读迭代全部元件是稳定的**，每个元件读 `Name.Text`、`Pattern`、X/Y、`Rotation`、`Layer`、`Height`、`BoundingRectangle`，再用 `GroupIterator` 遍历它的焊盘，多次实测都正常。按 `Pattern` 或 `Name.Text` 匹配后修改也正常。读 `Name.Text` 之前先判断 `Name` 不是 nil：`S1 := ''; if Obj3.Name <> nil then S1 := Obj3.Name.Text;`。
- 快照写法（改动前后各导一份再 diff）：
  ```
  Obj2 := Obj1.BoardIterator_Create;
  Obj2.AddFilter_ObjectSet(MkSet(eComponentObject));
  Obj2.AddFilter_LayerSet(AllLayers);
  Obj2.AddFilter_Method(eProcessAll);
  Obj3 := Obj2.FirstPCBObject;
  while Obj3 <> nil do
  begin
    List1.Add(Obj3.Name.Text + #9 + Obj3.Pattern + #9 + IntToStr(Obj3.X - Obj1.XOrigin) + #9 + IntToStr(Obj3.Y - Obj1.YOrigin) + #9 + IntToStr(Obj3.Layer) + #9 + FloatToStr(Obj3.Rotation) + #9 + IntToStr(Obj3.Height));
    Obj3 := Obj2.NextPCBObject;
  end;
  Obj1.BoardIterator_Destroy(Obj2);
  ```
- 按 Pattern 批量写 Height：用 `TStringList` 的 `名=值` 当字典（`IndexOfName`、`ValueFromIndex`），整轮循环放在 `PreProcess`/`PostProcess` 之间，每个元件 `Obj3.BeginModify; Obj3.Height := MMsToCoord(...); Obj3.EndModify;`。PCB 会自动标成已修改。
- 移动、翻面放在同一个修改块里：
  ```
  PCBServer.SendMessageToRobots(Obj3.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
  Obj3.Layer := eBottomLayer;
  Obj3.MoveToXY(Obj1.XOrigin + MMsToCoord(<x mm>), Obj1.YOrigin + MMsToCoord(<y mm>));
  PCBServer.SendMessageToRobots(Obj3.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
  ```
  精确复位用 `MoveToXY(原绝对内部坐标)`。MCP 的 `set_component_position` 有舍入（差几个内部单位，连封装里铜皮 Region 的顶点也会偏）。原始坐标在移动前用脚本读下，或者从保存的文件里读（`file-parsing.md`）。
- 移动位号、注释文字：给 `Comp.Name`（或 `Comp.Comment`）单独开修改块，用 `MoveByXY(目标X - XLocation, 目标Y - YLocation)`。
  直接给 `XLocation/YLocation` 赋值，当场回读是对的，但缓存外框没更新，关闭重开后又回到旧位置。
- 焊盘迭代器（`ePadObject` + `AddFilter_AllLayers`）可读 `HoleSize/HoleWidth/HoleType/Plated/Layer/InComponent/Net.Name/Rotation/Component.Pattern/PasteMaskEnabled/SolderMaskExpansionMode/PasteMaskExpansionMode`。元件里的非金属化孔 `Name` 是空串；`Plated` 对 SMD 焊盘也是 False。
- 板框：`Board.BoardOutline.PointCount`，逐个读 `Segments[i]` 的 `vx/vy/Kind`；`Kind = 1` 是圆弧，带 `cx/cy/Radius/Angle1/Angle2`。

## 3D 体

- **限高规则对有 3D 体的元件按 3D 体检查**（见 `rules-and-drc.md`），改高度要连 3D 体一起改。
- 读（库封装和 PCB 元件写法相同）：
  ```
  Obj4 := Obj3.GroupIterator_Create;
  Obj4.AddFilter_ObjectSet(MkSet(eComponentBodyObject));
  Obj5 := Obj4.FirstPCBObject;
  while Obj5 <> nil do
  begin
    { Obj5.Layer、Obj5.GetStandoffHeight、Obj5.GetOverallHeight、Obj5.Model.ModelType、Obj5.Model.GetState_MinZ / GetState_MaxZ }
    Obj5 := Obj4.NextPCBObject;
  end;
  Obj3.GroupIterator_Destroy(Obj4);
  ```
  一个封装常有多个体（引脚体加主体），取最大的 OverallHeight。
- 改：`Obj5.BeginModify; Obj5.SetOverallHeight(新值); Obj5.EndModify;`。它同时改挤出模型的 MaxZ，StandoffHeight、MinZ 和外接框不变。用"旧值 ±50 内部单位"认出要改的体。
  PCB 上元件外层再包一层 `Obj3.BeginModify`/`EndModify`；库里改完要手动置 Modified（见 `pcblib-and-eco.md`）。
  不要用 Update PCB With Footprint 同步 3D 体，它会用库里的焊盘覆盖 PCB。
- `IPCB_ComponentBody` 的 `.Model`、`.OverallHeight` 字典里有（`lookup IPCB_ComponentBody` 查）。`.Description` 字典里没有（它的继承链上只有 `Descriptor`），但实测能按属性读。反射里这几个都只看得到方法。

## 临时测试对象

为了实测规则，临时放过孔、走线、焊盘、fill，测完删掉。模板 `scripts\make_temp.pas`：读 TSV（每行 `类型 V/T/P/F`、编号、层号、网络名、mm 坐标、尺寸），焊盘统一命名 `TMPTEST`。

- **Net 一定要在 `AddPCBObject` 之前设**：
  ```
  Obj3 := PCBServer.PCBObjectFactory(eViaObject, eNoDimension, eCreate_Default);
  Obj3.X := ...; Obj3.Y := ...; Obj3.HoleSize := ...; Obj3.Size := ...;
  Obj3.LowLayer := eBottomLayer; Obj3.HighLayer := eTopLayer;
  if Obj5 <> nil then Obj3.Net := Obj5;      { Obj5：迭代 eNetObject 按名字找到 }
  PCBServer.PreProcess;
  Obj1.AddPCBObject(Obj3);
  PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj3.I_ObjectAddress);
  PCBServer.PostProcess;
  ```
  先加板、再在修改块里设 Net：`Net.Name` 回读正确，但 `InNet(...)` 范围匹配不到，批量 DRC 还冒出假短路；事后补 `Net.AddPCBObject` 也没用。
- 没设网络的临时走线、过孔会在 Un-Routed 类里报 "Dead Copper - Net Not Assigned"，统计时扣掉。
- 清理：迭代 Track/Arc/Via/Fill/Pad（`AddFilter_AllLayers`），收集 `not InComponent` 且是临时对象的，迭代完逐个 `RemovePCBObject` + `PCBM_BoardRegisteration`。删完数一遍板上不属于元件的铜对象，和预期个数比。
  按"不属于元件的铜"一刀切只在还没布线的板上安全；布线后要给临时对象专门的标记（专用网络、特殊线宽）。

## Keepout 区域

```
Obj3 := PCBServer.PCBContourFactory;
Obj3.AddPoint(Obj1.XOrigin + MMsToCoord(x), Obj1.YOrigin + MMsToCoord(y));   { 逐点 }
Obj2 := PCBServer.PCBObjectFactory(eRegionObject, eNoDimension, eCreate_Default);
Obj2.Layer := eTopLayer;  Obj2.Kind := 0;  Obj2.IsKeepout := True;
Obj2.SetOutlineContour(Obj3);
PCBServer.PreProcess;
Obj1.AddPCBObject(Obj2);
PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
PCBServer.PostProcess;
{ 加到板上之后，另开一个修改块设限制项 }
PCBServer.PreProcess;
PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
Obj2.IsKeepoutForVia := False; Obj2.IsKeepoutForTrack := False; Obj2.IsKeepoutForCopper := False;
Obj2.IsKeepoutForSMDPad := True; Obj2.IsKeepoutForTHPad := True;
PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
PCBServer.PostProcess;
```
- 新建 keepout 的 5 个限制项默认全开。读掩码用 `Region.GetState_KeepoutRestrictions`（31 = 全部）。
- keepout 区域在 AD 里没有名字，只能按位置、层、限制项认。
- keepout 自己会被默认 Clearance 规则当成铜来查（封装自带的 keepout 盖住自己焊盘也会报），BOC 规则也会报它；规则范围要写 `Not IsKeepOut`，或者另建 gap 0 的 Clearance 规则豁免。

## 挖空和非金属化孔

- **Board Cutout**：
  1. `Obj3 := PCBServer.PCBContourFactory;`，再逐点 `Obj3.AddPoint(x, y)`（圆弧要自己拆成直线，例如按 0.002 mm 弦高）；
  2. 用 `PCBObjectFactory(eRegionObject, ...)` 建 Region，设 `.Layer := eMultiLayer`、`.Kind := 3`（3 = BoardCutout，1 = 普通 Cutout）；
  3. 调用 `.SetOutlineContour(Obj3)`，再加到板上。
- 板上总有一个和整板外框一样大的 kind=3 区域，**它不是挖空**，是 AD 内部的板形区域。
  特征：`Descriptor` 为空，真正的挖空会显示 "Board Cutout (Multi-Layer)"。
  删掉后，每次保存都会按板外框自动重建（点数会变）。不要删它；统计挖空时用 `Descriptor` 把它排除掉。
- **非金属化孔**：用 `PCBObjectFactory(ePadObject, ...)` 建焊盘，设置：
  - `.Mode := ePadMode_Simple`
  - Top/Mid/Bot 的 X/YSize 都设为孔径，`.HoleSize` 也是孔径
  - `.Plated := False`、`.Layer := eMultiLayer`
- 规则范围里选中非金属化孔：`IsPad and (PadIsPlated = 'False') and OnMultiLayer`（见 `rules-and-drc.md` 的查询关键字）。

## 查接口和枚举

- 成员、签名、是否只读、常量和枚举的值，用 altium-script skill 的 `lookup` 查。它的字典从 AD23 脚本引擎的注册表提取，就是脚本里实际能用的名字和值。
- 不要用反射 `Altium.SDK.Interfaces.dll` 查枚举值：有 19 个常量名被不同单元注册了不同的值，脚本里拿到的和 SDK 定义不一样（SDK 的 `TUnit` 是 `eMetric = 0`，脚本里 `eMetric = 1`），完整的表在 altium-script 的 `references/api/Constants.md` 开头。反射里 COM 接口也只有方法，没有属性。
