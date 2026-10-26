---
name: altium-script
description: Altium Designer 23 的 DelphiScript API 字典、写法模式和官方示例脚本。字典从 AD 安装目录里脚本引擎的注册表提取，包括接口和类的全部成员签名、属性是否只读、继承链、全局函数、常量和枚举的实际值，以及进程（菜单命令）名和参数。写 AD 脚本（run_altium_script 或 .pas）时用来查调用顺序、找参考示例、查成员是否存在、能不能赋值、签名、常量值和进程参数；AD 升级后重新生成字典。
---

# AD23 脚本 API 字典和示例

字典来自 `<AD 安装目录>\System\ScriptingSystem.dll` 里脚本引擎的注册表（AD 23.1.1.15，2026-10-25 提取）。脚本里能用的接口成员、全局函数、常量，都是这张表里注册过的。
本 skill 回答"有什么、签名是什么、值是多少、有没有现成的例子"。脚本怎么跑、出错怎么恢复、哪些 API 能调用但不生效，看 altium-mcp skill。

下文的 `lookup` 指 `python -X utf8 <本 skill 目录>/scripts/lookup.py`（只用标准库；在 Bash 里路径要用正斜杠，反斜杠会被吃掉）。

## 写脚本的流程

1. **找写法和示例**：调用顺序（撤销、新建/修改/删除、遍历、编译工程）先看 `references/patterns.md`；要调 AD 菜单命令（缩放、选择、出报告、发布 PDF）看 `references/processes.md`。再找 2～5 个相关的官方示例：先看下文"按功能找"的表；没有就按关键词 Grep `references/summaries.md`（一个脚本或一个多文件工程一段说明）和 `references/overview.md`（每条一句话，顺序和 summaries 基本相同）。这两个索引只覆盖 `PCB/`、`SCH/`、`Processes/`；`General/`、`DXP/`、`FPGA/`、`WSM/` 只有 "to be added" 占位，这几个目录直接 Grep `references/scripts` 的源码（加 `-i` 忽略关键词的大小写；glob 本身区分大小写，写成 `*.{pas,PAS,Pas}`）。
   summaries 的小节标题多数是文件名，用 Glob `references/scripts/**/<文件名>` 找源码。Glob 区分大小写，扩展名有 `.pas`、`.PAS`、`.Pas` 三种，文件名照索引里的写法抄；自己拼的名字找不到时改成 `**/<不带扩展名的文件名>.*`。也有不是文件名的标题：PCB 遍历和层的 17 节写的是功能（如 "Count pads"），源码在 `PCB/PCB Iterators/`、`PCB/PCB Layers/`；标 "(Project)" 的是工程名，和目录名、工程文件名不一定一样：Glob `references/scripts/**/*.{PrjScr,PRJSCR,PrjPCB}` 列出全部工程文件，去掉空格和下划线、不分大小写和标题比对（如 `PCB_Picture_Creator` 是 `PCB/CreateRegionsFromBitmap/PCBPictureCreator.PRJSCR`），19 个工程标题里 16 个能这样对上，其余找名字相近的（`NetInfo` 是 `NetInfoPrj.PrjPCB`）。源码在工程文件的同一目录。正文里写的过程名不一定和源码一致，不要靠它找。
2. **查 API**：脚本里用到的每个成员、全局函数、常量、进程名都用 `lookup` 查到过，才算写完。字典里本来就没有、不用查的只有两类：沙盒预置的变量、过程和常量（`ResultText`、`S1`、`Obj1`、`SandboxLog`、`REPLACEALL` 等，见 altium-mcp skill），记录类型的字段（`Location.X`，字典只有记录类型名）。`Inc`、`Break`、`Length`、`Nil`、`Result` 这类语言自带的名字，`lookup` 会说明。
   - `lookup PCBServer.GetCurrentPCBBoard.LayerColor`：按调用链逐段查，每段沿父接口链找，输出定义在哪一层和签名。点号前也可以直接写接口名（`lookup IPCB_Board.LayerColor`）。
   - 迭代器和工厂返回的是基类型：`FirstPCBObject`、`PCBObjectFactory` 返回 `IPCB_Primitive`，`FirstSchObject`、`SchObjectFactory` 返回 `ISch_BasicContainer`。调用链查到这里再往下，`Width` 这类成员在基类型上没有，`lookup` 会列出定义它的下层类型和继承它的类型（如 `IsHidden` 定义在 `ISch_ComplexText`，`ISch_Parameter` 继承它）；改查对象实际的类型，如 `lookup IPCB_Track.Width`。按下层类型接着往下查的链返回 1，改成具体类型再查一次才返回 0。
   - 属性行尾有 `// read-only` 的不能赋值。例如 `IPCB_Board.LayerColor` 是只读的，赋值会卡死执行器；层颜色改用 `IPCB_SystemOptions.LayerColors_V6`。
   - 查不到时看输出：如果别的接口上有同名成员，只是"可能能用"（见下文"字典怎么读"），要先在 AD 里试；如果哪个接口上都没有，就换一种写法。例外是已经实测过的：`Client.SendMessage`、`SchServer.ProcessControl` 能用，`lookup` 直接说明并返回 0；`ISch_Document.FileName` 读它会卡住执行器，`lookup` 会说明改用 `DocumentName`。
   - `var`/`out` 参数必须传变量。
   - `lookup PCB:Zoom`：进程名写错时 `RunProcess` 不报错、什么也不做，所以进程名也要查到才用。
   - 签名里的类型名（`TCoord`、`TLayer`）引擎没有单独注册，`lookup TCoord` 会说明这一点，不用再追。
3. **在 AD 里验证**：名字都查到只说明存在，行为对不对要在 AD 里跑。用 `run_altium_script` 先拿几行的小脚本逐条试，再组装成循环（见 altium-mcp skill 的沙盒规则）。

## lookup.py

| 用法 | 作用 |
|---|---|
| `lookup IPCB_Track` | 列出接口或类的全部成员，包括继承来的，按定义的层分组 |
| `lookup IPCB_Track.Layer` | 查单个成员。查不到时，先列出定义这个成员的下层类型和继承它的类型；下层类型也没有，再列出别的有同名成员的接口 |
| `lookup PCBServer.GetCurrentPCBBoard.LayerColor` | 从返回接口的全局函数（`PCBServer`、`SchServer`、`Client`、`GetWorkspace` 等）开始，按调用链逐段查。中间一段只在别的接口上有、而且这些接口给出的类型相同时（如 `SchServer.ProcessControl`），按这个类型接着查 |
| `lookup ShowMessage` / `lookup eMetric` / `lookup TUnit` | 查全局函数、常量、变量、记录类型或枚举类型。`rfReplaceAll` 这类集合元素会注明要写 `MkSet(...)` |
| `lookup TCoord` | 只在签名里出现的类型名：说明它没有单独注册，并举几处用例 |
| `lookup Inc` | 语言自带的名字（`Inc`、`Dec`、`Break`、`Exit`、`Length`、`Copy`、`Delete`、`Ord`、`Abs`、`Round`、`Trunc`、`Assigned`、`Include`、`Nil`、`Result`）：字典里没有，说明它是语言自带的，给出示例里的用法（除 `Result` 外都在 AD23 沙盒里实测过）。`Exit`、`Result` 在 `run_altium_script` 的语句体里不能用，`lookup` 会提醒 |
| `lookup Width` | 只是成员的名字：说明它要写成 `对象.Width`，列出有它的接口（返回 1） |
| `lookup PCB:Zoom` | 查进程，列出 AD 菜单传给它的全部参数组合 |
| `lookup -s "Layer.*Color"` | 按正则搜索所有名字（成员和类的字段、全局函数、常量、枚举和记录类型、进程名和菜单文字），不区分大小写。成员既按成员名、也按 `接口名.成员名` 匹配，所以 `-s "^LayerColor$"` 能搜到 `IPCB_Board.LayerColor` |

查到返回 0，已实测能用的 `Client.SendMessage`、`SchServer.ProcessControl` 也返回 0（`Exit`、`Result` 返回 0 只说明名字存在，语句体里仍不能用）；查不到返回 1，只在别的接口上有（可能能用）也返回 1；`-s` 没有匹配返回 1；参数写错（没有参数、空的名字、不认识的选项、多余的参数、空的一段、空的或写错的正则）返回 2。

## 示例脚本

`references/scripts/` 是 Altium 官方的 DelphiScript 示例，来自官方文档 Scripting Examples Reference 页面上的 Examples.zip（`Scripts\Delphiscript Scripts\`），共 228 个文件，其中 147 个 .pas。文件头的版权年份是 2003～2009 年，都是老版本 AD 的示例。`overview.md` 和 `summaries.md` 是 coffeenmusic/altium-scripts-skill 为这些脚本写的英文索引，原样复制，只改了和源码对不上的地方：summaries.md 里 pcbcolor、pcblayer、PlacePCBPolygon 三段写错的进程名（AD23 都没有这几个命令）、两个小节标题的大小写，以及两个索引末尾重复的 "Process Scripts" 占位。

和 AD23 可能对不上的地方：

- 示例里常见 `Client.SendMessage`、`SchServer.ProcessControl`：它们不在声明类型的接口上，但 altium-mcp 实测在 AD23 能用，`lookup` 会说明这两点。
- 有的示例用到同名冲突的常量（见下文"同名常量"），或者字典里没有的名字（如 `InputQuery`），照抄前先 `lookup`。
- 名字对得上，不代表行为没变。示例里的做法和 altium-mcp skill 的实测结论冲突时，以 altium-mcp 为准，例如：沙盒里 `Try/Finally` 不保证执行 `PostProcess`；脚本里调用 `DoFileSave` 会弹框。
- 示例是完整程序（`Var` 声明、`ShowMessage`、窗体）。`run_altium_script` 只接受语句体，要改成用沙盒的预置变量，`Exit` 改成 `if ... then ... else`。

| 目录 | .pas 数 | 内容 |
|---|---|---|
| `PCB/` | 62 | PCB 对象创建、遍历、层、规则、输出，以及几个带窗体的小工具 |
| `SCH/` | 44 | 原理图对象、参数、库、遍历、连接关系 |
| `Processes/` | 13 | 用 `RunProcess` 和参数调用内置命令 |
| `DXP/`、`WSM/` | 9、6 | 客户端/服务器接口、集成库、工作区和项目（网表、报告） |
| `General/`、`FPGA/` | 11、2 | 窗体、文件读写、ini、压缩包；FPGA 约束 |

按功能找：

| 功能 | 示例 |
|---|---|
| 创建 PCB 对象 | `PCB/CreatePCBObjects.PAS`、`PCB/CreateAVia.pas`、`PCB/CreateComponentOnPCB.pas` |
| 规则 | `PCB/CreateRules.pas`、`PCB/PCB Rules/ModifyWidthRules.pas`、`PCB/PCB Rules/IterateRules.pas` |
| 层和层叠 | `PCB/PCB Layers/Layers_Info.pas`、`QueryLayerStack.pas`、`ValidateLayerStack.pas` |
| 遍历 | `PCB/PCB Iterators/`（`Count_Pads.pas`、`IterateNets.PAS`、`SpatialIterator.Pas`、`LibraryIterator.pas` 等） |
| 元件、封装 | `PCB/SwapOrRotateComponents/SwapComponentsUnit.pas`、`PCB/CreateFootprintInLibrary.pas` |
| 输出、检查 | `PCB/PCB Outputs/PCBOutputGenerator.pas`、`Violations.pas`、`PCB/Unique Object Checker/`、`PCB/Values Checker/` |
| 网络 | `PCB/NetObjectAssign.pas`、`PCB/UnRoute Net Class/` |
| 区域、铺铜 | `PCB/PCB Iterators/IterateRegions.pas`、`IteratePolygons.pas`、`PCB/CreateRegionsFromBitmap/` |
| 原理图对象 | `SCH/CreateSchObjects.pas`、`SCH/PlaceSchObjects.PAS`、`SCH/UsingSchInterfaces.pas` |
| 原理图库 | `SCH/createcomp_in_lib.pas`、`SCH/libiterator.pas`、`SCH/SymbolPrimsIterator.pas` |
| 参数 | `SCH/FetchParameters.pas`、`SCH/FetchParamsOfComp.pas`、`SCH/UserDefinedParameters/` |
| 项目、网表 | `WSM/ProjectReporter.pas`、`WSM/Netlister.pas`、`SCH/usingWSMInterfaces.pas` |
| 调用内置命令 | `Processes/SimpleExample.pas`、`Processes/pcbcolor.pas`、`Processes/PublishToPDFScript.pas` |

## 常用入口

| 入口 | 签名 |
|---|---|
| PCB | `function PCBServer: IPCB_ServerInterface;` → `GetCurrentPCBBoard: IPCB_Board`、`PreProcess`/`PostProcess`、`PCBObjectFactory(AObjectId, ADimensionKind, ACreationMode)`、`SystemOptions` |
| PCB 遍历 | `Board.BoardIterator_Create` → `AddFilter_ObjectSet(MkSet(eTrackObject, ...))`、`AddFilter_AllLayers` → `FirstPCBObject`/`NextPCBObject` → `Board.BoardIterator_Destroy(Iter)`；按区域查用 `SpatialIterator_Create` |
| 原理图 | `function SchServer: ISch_ServerInterface;` → `GetCurrentSchDocument: ISch_Document` → `SchIterator_Create` → `FirstSchObject`/`NextSchObject` → `SchIterator_Destroy` |
| 工作区、客户端 | `function GetWorkspace: IWorkspace;`、`function Client: IClient;`、`function IntegratedLibraryManager: IIntegratedLibraryManager;` |
| 运行进程 | `ResetParameters;` → `AddStringParameter(Name, Value);` → `RunProcess('PCB:Zoom');`，见 `references/processes.md` |
| 单位换算 | `MilsToCoord`、`MMsToCoord`、`CoordToMils`、`CoordToMMs`（1 mil = 10000 内部单位） |

`MkSet`、`CreateObject` 是可变参数函数。字典里的签名 `(cArgs: Integer; pArgs: PVariantArgList)` 是它们内部实现的形式，脚本里把参数逐个写在括号里，如 `MkSet(eTrackObject, eViaObject)`。`CreateObject` 要什么参数字典里看不出，官方示例里也没有调用。

## 字典怎么读

- **成员不只看声明类型**：DelphiScript 不管变量的声明类型。实测 `Client.SendMessage` 能用，可 `SendMessage` 注册在 `IProcessLauncher` 上，不在 `IClient` 上；`SchServer.ProcessControl` 也能用，它注册在 `IServerModule`、`IClient` 上。看起来对象实现的其他接口上的成员也能调用，但引擎内部怎么查找没有确认过。所以按两种情况处理：
  - 名字在哪个接口、类上都没有：一定不能用。例如 `SourceDesignItemID`，读它会卡死执行器。
  - 不在预期类型的继承链上，但别的接口上有：可能能用，先用小脚本试。
- **继承**：md 里只把成员列在声明它的那一层，每节第一行给出继承链。`IPCB_Track.Layer` 定义在 `IPCB_Primitive`。
- **只读**：属性注册时没有 setter，就是只读。反过来，能赋值不代表一定生效：`IPCB_Board.LayerIsDisplayed` 能赋值，但不影响显示（见 altium-mcp）。
- **getter/setter**：属性写成 `read GetState_X write SetState_X`，这两个方法也注册了，可以直接调用。
- **参数**：签名不显示默认值，带默认值的参数可以省略（`FileExists` 字典里有两个参数，实测只传路径也能用），哪些能省字典看不出。参数类型也不一定是实际传的：`SchServer.RobotManager.SendMessage` 字典里的参数类型是 `ISch_BasicContainer`，示例和 altium-mcp 实测都传 `I_ObjectAddress`、`c_BroadCast`、`nil`。类型对不上时以示例和实测为准。
- **类**：显式注册的方法和属性，加上 RTTI 里的 published 属性（窗体控件的属性和事件）。带下标的类属性只知道下标个数，写成 `Index: ?`。
- **常量**：集合常量写成元素序号的集合，如 `SignalLayers = [1..32]`。`INVALID_HANDLE_VALUE`、`sLineBreak`、`kDiameterSymbolANSI`、`kDegreeSymbol` 这 4 个常量没解出值，写成 `?`。

## 同名常量

有 19 个常量名被不同单元注册了不同的值，脚本里拿到的是第一次注册的值（其中 18 个整数常量在 AD23 里逐个实测过，另一个是集合常量 `Numbers`）。完整的表在 `references/api/Constants.md` 开头；`lookup` 这些名字时会提示另一个单元注册的值。

例如脚本里 `eMetric = 1`、`eImperial = 0`，这是原理图 `TUnitSystem` 的值；PCB 的 `TUnit` 定义里是 `eMetric = 0`、`eImperial = 1`（SDK 反射也是这样）。但实测 `CoordUnitToString(MilsToCoord(100), eImperial)` 输出 `100mil`，结果是对的。可见不能凭枚举定义推断这些名字传进某个函数或属性后的效果，用之前先在 AD 里用小脚本试。

## 文件

- `references/api/`：`API_Map.md`（数量汇总、所有接口按单元列出）、`PCB_Interfaces.md`、`SCH_Interfaces.md`、`Other_Interfaces.md`、`Classes.md`、`Global_Functions.md`（含记录类型、全局变量）、`Constants.md`（同名冲突表、按枚举类型分组的常量、其他常量）。
- `references/patterns.md`、`processes.md`：调用顺序、语言要点和进程用法，从上游手写说明迁来并按 AD23 核对过，文末列出对不上的上游说法。
- `references/scripts/`、`overview.md`、`summaries.md`：示例脚本和两个索引。
- `data/api.json`：API 提取结果；`data/processes.json`：进程名和菜单参数，从 AD 的 `System\*.ins`、`*.rcs` 提取。
- `scripts/`：`lookup.py`；重新生成用的 `extract_api.py`、`extract_processes.py`、`gen_docs.py`、`pe_lite.py`、`x64lite.py`。

## 可信度

- 提取时和网上流传的另一份 API 字典（coffeenmusic/altium-scripts-skill，导出自更新的 AD 版本）逐条比对过：两边共有的 22059 个成员一致，15358 条方法签名相同。那份字典里多出的 299 个接口、1367 个成员，AD23 都没有。
- 签名里的参数名和类型来自 AD 自己的 RTTI，`const`/`var`/`out` 也照 RTTI 写。

## AD 升级或换机器后

AD 版本变了，字典就要重新生成。步骤和容易出问题的地方见 `references/regenerate.md`。
