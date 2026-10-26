# 规则、DRC 和模拟检查（AD23 实测）

## 建规则和改规则

- 新建：`Obj4 := PCBServer.PCBRuleFactory(种类号)` → 设 `.Name`、`.Scope1Expression`、`.Scope2Expression`、数值属性、`.DRCEnabled := True`、`.Comment` → `PCBServer.PreProcess; Obj1.AddPCBObject(Obj4); PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj4.I_ObjectAddress); PCBServer.PostProcess;`。
  规则参数多时放进 TSV（`种类 名字 范围1 范围2 min max pref`），一个脚本建完。
- 改现有规则：按名字迭代 `eRuleObject`，收进 `TInterfaceList`，**先核对数量对不对**，再 `PreProcess` → 每条 `PCBM_BeginModify` → 赋值 → `PCBM_EndModify` → `PostProcess`，最后读 `Descriptor` 核对。
- 删规则：收集后在 `PreProcess`/`PostProcess` 之间 `Obj1.RemovePCBObject(规则)`。删掉临时规则后，原有规则的优先级自动恢复。PCB 会被标成已修改。
- Comment 写中文：说明文字存成 UTF-8 带 BOM 的文件（每行 `规则名<TAB>说明`），`LoadFromFile` 后按名字取出赋给 `.Comment`。磁盘上的存法见 `file-parsing.md`。
- 快照和比对：内存里用 `scripts\rules_mem.pas`（把 `@@OUT@@` 换成输出路径，注意 `pcb-scripting.md` 里替换路径的坑）；磁盘上用 `scripts\pcbdoc_rules.py`，前后两份用 `pcbdoc_rules_cmp.py` 比。规则改动后，建、删、改的条目应该和预期一一对上。
- 种类号（`PCB.TRuleKind`，也能写常量名如 `eRule_MaxMinHeight`）：0 Clearance、1 ParallelSegment、2 Width、9 RoutingLayers、11 RoutingVias、13 SolderMaskExpansion、14 PasteMaskExpansion、15 ShortCircuit、16 UnRoutedNet、19 MinimumAnnularRing、20 PolygonConnect、22 Room（ConfinementConstraint）、24 ComponentClearance、42 HoleSize、48 LayerPairs、50 Height（MaxMinHeight）、52 HoleToHoleClearance、53 MinimumSolderMaskSliver、54 SilkToSolderMaskClearance、55 SilkToSilkClearance、56 NetAntennae、59 SilkToBoardRegion、63 BoardOutlineClearance。
- 各类规则的属性名（赋值实测过）：

  | 种类 | 属性 |
  |---|---|
  | Clearance 0 | `Gap`、`NetScope`（0 DifferentNets、1 SameNetOnly、2 AnyNet） |
  | Width 2 | **按层索引**：`MinWidth[eTopLayer]`、`FavoredWidth[...]`、`MaxWidth[...]`，每个铜层都要设，只改 Top 不影响 Bottom |
  | RoutingVias 11 | `MinHoleWidth/PreferedHoleWidth/MaxHoleWidth/MinWidth/PreferedWidth/MaxWidth` |
  | SolderMaskExpansion 13 | `Expansion`；盖油见下面"盖油" |
  | ShortCircuit 15 | `Allowed := True` |
  | MinimumAnnularRing 19 | `Minimum`（磁盘 `MINIMUMRING`） |
  | PolygonConnect 20 | `ConnectStyle`（0 Relief、1 Direct）、`ReliefConductorWidth`、`ReliefAirGap`、`ReliefEntries`、`PolygonReliefAngle`（0 = 45°、1 = 90°、2 = 0°、3 = 135°）。新建的规则默认是 90°，要 45° 显式写 0 |
  | ComponentClearance 24 | `Gap`、`VerticalGap`、`CollisionCheckMode` |
  | HoleSize 42 | `MinLimit/MaxLimit`（另有 `AbsoluteValues`、`Min/MaxPercent`） |
  | Height 50 | `MinHeight/MaxHeight/PreferedHeight` |
  | HoleToHole 52 | `Gap`、`NetScope`（默认是 DifferentNets，同网络的孔对不查） |
  | MinimumSolderMaskSliver 53 | `MinSolderMaskSliver`（磁盘 `MINSOLDERMASKWIDTH`；写成 `MinSolderMaskWidth` 报 `Undeclared identifier`） |
  | SilkToSolderMask 54 | `SilkToMaskGap`、`IsClearanceToExposedCopper` |
  | BoardOutlineClearance 63 | `Gap`（反射只看到 `GetState_Gap`，但 `.Gap :=` 能赋值） |

- 停用规则：`DRCEnabled := False`。

## 优先级

- **`Rule.Priority` 只读**，赋值会让执行器卡死（板上的规则、刚建还没加板的规则都一样）。
- 对规则做任何一次修改（哪怕是中间什么都不改的 `PCBM_BeginModify`/`PCBM_EndModify`），或者移除再加回，这条规则都会变成同种类里的优先级 1。优先级是按规则种类分别排的。新建一条规则（含 Room）也排在 1，同种类的其他规则依次后移。
- 所以靠"宽松的先建"排好的顺序，会被之后的修改打乱。**所有改动做完后，再按目标优先级从低到高，逐条做一次空修改**，最后做的那条就是 1。改了某条默认规则后，本该排在它前面的规则要再空修改一次，把它压回去。
- Room 的修改（包括空修改、改范围）每条要几秒，批量处理 Room 时按条数估时长，传足够大的 `timeout_seconds`。
- 脚本在改优先级中途崩溃时，崩溃前已执行的修改会保留；下一个脚本开头先补一句 `PCBServer.PostProcess`。

## 范围表达式和查询关键字

- 排除个别元件：`... and Not (InComponent('<位号1>') or InComponent('<位号2>'))`。写成 `not (Name = 'X' or ...)` 不生效，还会弹框。
- 实测能用：`IsSMTPin`、`IsThruPin`、`IsVia`、`IsPad`、`IsRegion`、`IsKeepOut`、`OnCopper`、`OnMultiLayer`、`InPolygon`、`InNet('...')`、`InNetClass('...')`、`InPadClass('...')`、`InComponent('...')`、`HasFootprint('...')`、`WithinRoom('...')`、`TouchesRoom('...')`。
  - `OnCopper` 和 `OnSignal` 都包括过孔和 keepout 区域；只要铜就写 `OnCopper and Not IsKeepOut`。
  - `HasFootprint('X')` 除了元件本身，还匹配该封装里的图元（走线、圆弧、丝印）。
  - 非金属化孔：`IsPad and (PadIsPlated = 'False') and OnMultiLayer`（或 `and Not IsSMTPin`）正好选中自由 NPTH 焊盘和元件里的 NPTH。只写 `PadIsPlated = 'False'` 会把 SMD 焊盘也选进来。
- **非法关键字**（`IsSMDPad`、`Plated`、`IsPlated` 等）在表达式求值时（如 `Scope1Includes`）弹 "Undeclared identifier: IsPlated at Line:..., Char:... Continue execution?" 框。v0.5.1 把它当运行时错误：按 Cancel 停掉脚本，返回 `"error": "run-time error"`，`altium_message` 里有关键字名（实测）。
  **同一个 AD 会话里，同一个关键字只在第一次弹框**：再跑一次同样的脚本不弹框、照常跑完，表达式变成**几乎全选**（实测 5 个焊盘匹配 5 个）。所以表达式里的关键字要先用下面的临时规则测过；如果某次报过这种 `run-time error`，这个关键字以后的计数都作废。（v0.5.0 是每次弹一个标题为 "X2" 的框，MCP 关掉后脚本照常跑完。）
- 测一个表达式选中了哪些对象：
  - 建一条临时规则（如 `PCBRuleFactory(0)`），`Scope1Expression := 表达式`，**`DRCEnabled := True`**，加到板上并发 BoardRegisteration，再迭代对象调 `Rule.Scope1Includes(Obj)` 计数，最后删掉规则。临时规则 `DRCEnabled := False` 时，`Scope1Includes`/`CheckUnaryScope` 恒为 False，连 `All` 都选不中。
  - 或者用 `FindDominantRuleForObjectPair(对象, 参照对象, eRule_Clearance)` 看主导规则是不是这条临时规则。
- 有缺口的 Room：对象不完全落在 Room 里时 `WithinRoom` 判不中，用 `TouchesRoom`。

## Room

- 新建：`PCBRuleFactory(22)`，设置 `.Name`、`.Kind`（1 = Keep objects outside；0 = 只作区域）、`.Layer`、`.Scope1Expression`、`.Comment`、`.DRCEnabled`。
- 多边形顶点：先 `Obj3 := TPolySegment; Obj3.Kind := ePolySegmentLine;`，再 `.PointCount := n`，逐个设置 `Obj3.vx/.vy`，然后 `Room.Segments[i] := Obj3`。
- **外接矩形不会自动算对**：它是"顶点 + 位置点 X/Y"的并集，位置点默认在 (25.4mm, 25.4mm)，DRC 会用到这个矩形。新建时的正确顺序：
  1. 加到板上；
  2. 单独一个 `PCBM_BeginModify/EndModify` 块里，把 `X/Y` 设为多边形左下角；
  3. 再开一个修改块，重新写一遍 `PointCount` 和 `Segments`。
  直接给 `BoundingRectangle` 赋值会让执行器卡死。位置点已经设好的 Room，改形状时在一个修改块里重写 `PointCount` 和 `Segments` 就够了。
- **Room 的 Layer 不限制检查哪一面的元件**，顶层 Room 也会报底层元件。要在范围里写 `IsComponent and OnTopLayer` 或 `OnBottomLayer`。
- Room 按**元件的外接框**判断。贴着区域边的元件，外框碰到区域就报，必要时给 Room 开缺口。`Comp.BoundingRectangle` 包含位号和注释文字；`Comp.BoundingRectangleNoNameComment` 不包含。
- 元件间距（ComponentClearance，默认规则磁盘上 `COLLISIONCHECKMODE=3`）同样按两个元件 `BoundingRectangleNoNameComment` 矩形之间的距离判断，不看焊盘铜和 3D 体。封装的丝印框、封装里多余的文字都会把外框撑大。离线预排时按外框矩形算间距并留 0.02 mm 左右余量，放完用下面"模拟检查"确认。
- 把 Room 自身的 DRC 关掉（`DRCEnabled := False`，Descriptor 带 "(Disabled)"）后，它仍然可以给 `WithinRoom`/`TouchesRoom` 当区域用。
- Room 的 Descriptor 和磁盘记录里的坐标是绝对坐标（mil 或 mm），不是相对板原点。
- 改 Room 很慢，估时长的办法见上面"优先级"一节。

## 高度规则

- `PCBRuleFactory(50)`，设置 `.MaxHeight/.MinHeight/.PreferedHeight`。
- **元件有 3D 体时，检查的是所有 3D 体里最大的 OverallHeight，`Height` 属性不起作用**；没有 3D 体才看 `Height`。改高度时两处一起改（3D 体的写法见 `pcb-scripting.md`），否则改了 `Height` 也白改。
  实测：`Height` 0、3D 体 1.5 的元件，临时 Height 规则 Max 1.0 报 "Actual Height = 1.5mm"；`Height` 4.18、3D 体 4.03 的元件，Max 4.10 不报，把 3D 体改成 4.18 后再测就报了。
- Min 是 0 时，高度为 0（未知）的元件永远能通过限高规则。要让"高度未知的元件放进限高区"报错，就把 Min 设成 0.01，同时给本来就零高度的件（测试点、Mark 点、铜皮天线）建一条优先级最高的豁免规则，否则它们一放进去就误报。
- 规则名单里的元件"整条规则豁免"等于没有上限；需要放宽时，给它们单独建一条带上限的 Height 规则。

## 各类规则的坑

- **BOC（Board Outline Clearance）和 Room 规则不按优先级覆盖**，每条都单独检查。给某个元件开例外，除了建例外规则，还要把它从默认规则的范围里排除。
- **BOC**：
  - Descriptor 永远显示 `Gap=0mm`，DRC 报告的规则标题也是。真实值读 `Rule.Gap`，或看磁盘 `GAP=`、DRC 明细里的 "(Collision < 0.2mm)"。
  - 范围写 `All` 会把丝印、文字和 keepout 区域也和板边比；只查铜写 `OnCopper and Not IsKeepOut`。
  - 距离正好等于间距也报（"0.2mm < 0.2mm"），正好卡在限值的件要给一个略小的例外值。
- **Clearance**：keepout 区域自己会被当成铜来查（封装自带的 keepout 盖住自己焊盘也会报）。AD 默认 Clearance 规则的 "→Hole" 各列是 0，铜到非金属化孔实际只按焊盘那一列查；要管 NPTH 周围的铜，单独建规则。
- **盖油（SolderMaskExpansion 的 Tenting）**：只有 `Rule.SetState_IsTenting_Top(True)` / `SetState_IsTenting_Bottom(True)` 生效（新规则在加板前调、已有规则在修改块里调都行）。直接赋值 `IsTenting_Top := True` 不报错但不生效，`IsTentingTop`（不带下划线）会卡死。磁盘上只看得到 `ISTENTINGTOP`，底面的标志存在别处，要在内存里用 `GetState_IsTenting_Bottom` 回读确认。过孔对象自己的 `IsTenting_*` 读出来是 False，不代表规则没生效。
- **SilkToSolderMask**：开了 `IsClearanceToExposedCopper` 时按"到裸露铜"测，改阻焊外扩不影响这类违规。
- **阻焊桥豁免**只想对一个元件内部生效时，两侧范围都写 `InComponent('<位号>')`；范围 2 写 `All` 会连它和旁边元件之间也不查。
- **NetAntennae**：范围 `Not HasFootprint('<封装名>')` 能排除某种封装里的走线（如导电胶按键的梳状触点）。
- **AD 默认的两条平行线段规则**（`Default Parallel Segment Same Layer`、`Default Parallel Segment Adjasent`，原文就拼错了）在布线后会大量报，不需要时停用，并从批量检查集合里去掉。

## 批量 DRC

- 调用：`B1 := Obj1.RunBatchDesignRuleCheck(报告路径, 1, False, False);`（1 = 文本报告），传 `timeout_seconds: 400`。返回 0，但报告正常生成，不弹窗，文档不变成已修改。
- 报告格式：纯 ASCII、CRLF。开头 `Warnings|Total|0`、`Violations|Total|N`；每条规则一行汇总 `Rule Violations|<规则描述>|<条数>`；明细行 `<规则描述>|||<违规文字>`。
  Room 规则描述里的 `Bounding Region = (…)` 是绝对坐标，明细里的坐标相对板原点。比较两份报告：按 `'|||'` 切出明细，空白规整后去重，再求差集；规则描述里的 Bounding Region 先换成占位符。
- **违规数到上限（`MAXVIOLATIONCOUNT`，默认 500）时，给的是任意子集**：同一条违规这次在、下次不在，各类计数互相挪动。上限下的前后对比没有意义；可信的只有没到上限的报告，或下面的模拟检查。
- 上限和批量检查集合（`RULESETTOCHECK`，值是上面的种类号列表；在线 DRC 的是另一个字段 `ONLINERULESETTOCHECK`，grep `RULESETTOCHECK=` 会先匹配到它）存在 PcbDoc 的 `Design Rule Checker Options6` 流里，脚本 API 拿不到（反射有 `IPCB_DesignRuleCheckerOptions`，但没有取得它的方法），只能用 UIA 在 DRC 对话框里改（`uia-dialogs.md`）。
  默认的批量集合不含 ComponentClearance、RoutingLayers、RoutingViaStyle、LayerPairs；AD23 的 DRC 对话框里**根本没有 SilkToBoardRegion** 这一项。测试点类规则勾上后每个网络都报"缺测试点"，按需勾。
- 批量 DRC 的结果作为违规对象留在文档里，保存时写进 `T*Violation` 流（对话框 Report Options 里默认勾着 "Create Violations"）。同一条违规会在报告里出现多次，比对前先去重。在线 DRC 的结果流里有、批量报告里是 0 的类别，以前者为线索再查。
- 没设网络的临时对象会报 "Dead Copper - Net Not Assigned"（算在 Un-Routed 类里）。

## 模拟检查（不跑 DRC，也不受上限影响）

- 单对象规则（Room、Height 等）：
  ```
  { 先把要查的规则收进 Obj5 := TInterfaceList.Create（如 RuleKind 为 22 或 50 且 DRCEnabled 的） }
  for I1 := 0 to Obj5.Count - 1 do
  begin
    Obj4 := Obj5.Items[I1];
    if Obj4.Scope1Includes(Obj3) then
    begin
      Obj4 := Obj4.ActualCheck(Obj3, nil);       { 非 nil 就是违规 }
      if Obj4 <> nil then S1 := S1 + Obj5.Items[I1].Name + #9 + Obj3.Name.Text + #9 + Obj4.Description + #13#10;
    end;
  end;
  ```
  违规对象的 `.Description` 直接给出实测值（如 "Actual Height = 1.5mm"），能看出规则用的是哪个高度。前提：规则在板上且 `DRCEnabled = True`。
- 主导规则：`Board.FindDominantRuleForObject(Obj, 种类号)` 返回实际套用的那条（能读 `.Name`），再 `ActualCheck(Obj, nil)`。
  对**不是**主导的规则直接 `ActualCheck`，可以看"如果没有豁免会不会报"。批量 DRC 只按主导规则判。
- 成对规则（Clearance、丝印到阻焊、阻焊桥、孔到孔等）：用空间迭代器找邻近对象，两个方向各查一次：
  ```
  Obj2 := Obj1.SpatialIterator_Create;
  Obj2.AddFilter_ObjectSet(MkSet(ePadObject, eTrackObject, eArcObject, eFillObject, eRegionObject, eTextObject, eViaObject));
  Obj2.AddFilter_LayerSet(AllLayers);
  Obj2.AddFilter_Area(R.Left - MMsToCoord(0.6), R.Bottom - MMsToCoord(0.6), R.Right + MMsToCoord(0.6), R.Top + MMsToCoord(0.6));
  { 对每个邻近对象 Obj4（跳过 Obj4.I_ObjectAddress = Obj3.I_ObjectAddress 的自己）： }
  DbDoc := Obj1.FindDominantRuleForObjectPair(Obj3, Obj4, B1);   { B1 = 种类号 }
  if DbDoc <> nil then if DbDoc.DRCEnabled then
    if DbDoc.ActualCheck(Obj3, Obj4) <> nil then ...            { 违规，.Description 有原文 }
  Obj1.SpatialIterator_Destroy(Obj2);
  ```
  机械层对象（Layer 57～72）排除掉。同一处违规会出现多次（两个方向，加上两边都是被查对象），按 `(规则名, 排序后的对象对)` 去重。
- 元件间距（ComponentClearance）：把全部元件收进 `TInterfaceList`，对要查的元件两两 `FindDominantRuleForObjectPair(Comp, Other, 24)` + `ActualCheck(Comp, Other)`。
- 全板模拟和 DRC 的同类结果应该逐条一致；对不上时先看 DRC 报告是不是到了违规数上限。
