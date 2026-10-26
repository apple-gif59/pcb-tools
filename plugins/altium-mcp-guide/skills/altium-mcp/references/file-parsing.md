# 从磁盘只读解析 PcbDoc / PcbLib（实测）

用途：核对保存后的文件真的是想要的内容（不依赖 AD 内存），比对两个版本只差在哪里，审查时不碰 AD。SchDoc 的读法见 `schematic-viewing.md` 的"数据提取"。

## 基本做法

- 用 `olefile`（纯 Python，`pip install olefile`）。PcbDoc/PcbLib 都是 OLE 复合文档。
- 文本一律按 latin-1 解码，整数是小端。记录文本是 `|KEY=VALUE|KEY=VALUE|...`。
- 文件正被 AD 打开时也能读，但读到的是上次保存的版本。要读某个提交的版本：`git show <commit>:"<文件>" > 临时文件`。
- 只想确认某个值有没有落盘，直接 `grep -a` 或 Python 搜字节就够了，例如 `grep -a -o "MAXVIOLATIONCOUNT=[0-9]*" <文件>.PcbDoc`、`PATTERN=<封装名>|HEIGHT=<值>mil`。

## 脚本（本 skill 的 `scripts\`）

| 脚本 | 作用 |
|---|---|
| `pcbdoc_rules.py <PcbDoc> <out.txt> [--full]` | 导出全部规则（名称、类型、优先级、范围、其余字段）、DRC 选项、类；中文 Comment 已解码 |
| `pcbdoc_rules_cmp.py <前.txt> <后.txt> [忽略字段,...]` | 比较两份规则导出：DELETED / NEW / 逐字段 MOD |
| `pcbdoc_heights.py <PcbLib> <PcbDoc> <out.txt>` | 读库里每个封装和 PCB 上每个元件的 HEIGHT |
| `pcbdoc_diff.py <旧.PcbDoc> <新.PcbDoc>` | 按流比较，记录按多重集比（不管顺序），Texts6 屏蔽字体名填充，ComponentBodies6 单列高度变化 |

## PcbDoc 的流

| 流 | 格式和要点 |
|---|---|
| `Rules6/Data` | `[u16 类型][u32 长度][文本]` 重复。字段 NAME、RULEKIND、PRIORITY、ENABLED、SCOPE1EXPRESSION、SCOPE2EXPRESSION、NETSCOPE 等。有些磁盘字段名和 API 属性名不同：阻焊桥是 `MINSOLDERMASKWIDTH`（API 是 `MinSolderMaskSliver`），Net Antennae 是 `NETANTENNAETOLERANCE`，焊环是 `MINIMUMRING`。Room 规则的顶点和板框同样是 `KINDi/VXi/VYi/...`，绝对坐标 mil；Room 的顶点首尾重复（最后一个等于第一个），和顶点列表比对时先去掉 |
| `Design Rule Checker Options6/Data` | 前 4 字节后是文本：`MAXVIOLATIONCOUNT`、`RULESETTOCHECK`（批量 DRC 检查的规则类型号列表）、`ONLINERULESETTOCHECK`。**不在 Board6 里** |
| `Classes6/Data` | `[u32 长度][文本]` 重复，成员是 `M0=`、`M1=`… |
| `Components6/Data` | `[u32 长度][文本]` 重复。SOURCEDESIGNATOR、PATTERN、X/Y（**绝对坐标**，单位 mil，减去 Board6 的 ORIGINX/ORIGINY 才是相对板原点）、ROTATION、LAYER（TOP/BOTTOM）、SOURCELIBREFERENCE、HEIGHT。Height 为 0 时不写 HEIGHT 键 |
| `ComponentBodies6/Data` | `[u8 类型][u32 长度][数据]`。数据偏移 7 的 u16 是元件索引（Components6 里的顺序号）。文本段有 V7_LAYER、STANDOFFHEIGHT、OVERALLHEIGHT、MODEL.EXTRUDED.MINZ/MAXZ、MODELID、MODEL.CHECKSUM、MODEL.2D.X/Y，后面接二进制顶点。`ShapeBasedComponentBodies6` 同步变化 |
| `Pads6/Data` | `[u8 类型]` 后接 6 个 `[u32 长度][块]`。块 0 去掉第 1 字节是焊盘名。块 4 是 194 字节主块：[0] 层，[7:9] 元件索引（Components6 里的顺序号；不小于元件数的是自由焊盘），[13:17]/[17:21] X/Y（i32），[21:45] 尺寸（i32，依次 TopX、TopY、MidX、MidY、BotX、BotY），[45:49] 孔径（SMD 焊盘为 0），[126:142] 16 字节内部 ID。按"元件位号 + 焊盘名 + X/Y"能把两个版本的焊盘一一对上 |
| `Tracks6`、`Arcs6`、`Vias6`、`Fills6`、`Regions6` 等 | 通用 `[u8 类型][u32 长度][数据]`。数据 [0] 是层号（机械层 N 是 56 + N），[7:9] 是元件索引（0xFFFF = 不属于元件）。坐标是绝对坐标，内部单位（1 mil = 10000） |
| `Tracks6/Data` | [13:33] X1、Y1、X2、Y2、线宽（i32）。按坐标比对脚本建的走线和磁盘记录时，两端先排序：有的走线保存后两端顺序和创建时相反 |
| `Arcs6/Data` | [13:25] 圆心 X、Y 和半径（i32），[25:41] 起角、止角（double，度），[41:45] 线宽（i32） |
| `Regions6/Data` | [18:22] 文本长度，[22:] 文本；文本后面是 u32 顶点数，再接顶点数 × 两个 double（X、Y，内部单位）。Board Cutout 的文本带 `ISBOARDCUTOUT=TRUE`。keepout 区域的限制项是 `KEEPOUTRESTRICTIONS=` 位掩码：31 = 全部限制，只限 SMD 焊盘和通孔焊盘时是 24。文本里没有 `ISKEEPOUT` 字段 |
| `Texts6/Data` | `[u8][u32 长度][数据][u32 长度][字符串]`。字体名是 64 字节 UTF-16 字段（数据偏移 46），名字后面的填充是随机内存；记录长度 ≥123 时，数据偏移 115 的 u32 是 WideStrings 索引 |
| `WideStrings6/Data` | `[u32 索引][u32 长度][UTF-16LE]` 重复，没有文件头 |
| `Board6/Data` | 按 `|` 切。ORIGINX/ORIGINY；层叠在 `LAYER_V8_<n>NAME/COPTHICK/DIELHEIGHT/DIELCONST/DIELTYPE/DIELMATERIAL`，`V9_STACK_*`、`V9_CACHE_*` 跟着变。层的 `LAYERID`：机械层 N 是 `0x1020000+N`；层名 `LAYER_V8_<n>NAME` 含非 ASCII 字符时存成逗号分隔的 Unicode 码点。板框顶点是 `KINDi/VXi/VYi/CXi/CYi/SAi/EAi/Ri`（i 从 0 起，绝对坐标 mil） |
| `T*Violation` | 批量 DRC 和在线 DRC 的结果对象，保存时写进文件。Header 是 u32 条数，Data 是文本（RULEINDEX、PRIM1ID/PRIM1INDEX、DESCRIPTION、LOCATION1.X…）。流名截断到 31 字符，如 `TSilkToSolderMaskClearanceViola`。批量 DRC 报告里某类是 0，但文件里有这类违规流时，以文件为准再查 |

## PcbLib 的流

- 每个封装一个 storage：`Data`、`Header`、`Parameters`、`WideStrings`、`UniqueIDPrimitiveInformation/{Data,Header}`。库级的是 `Library/Data`（DATE/TIME）和 `Library/ComponentParamsTOC/Data`。
- `<封装>/Parameters`：去掉前 4 字节是 `|PATTERN=..|HEIGHT=..mil|DESCRIPTION=..|`。封装名以 PATTERN 为准（OLE 的 storage 名最长 31 字符，长名字会被截断）。
- `<封装>/Data`：开头 `[u32 n][n 字节名字]`，后面是图元记录：类型 2 是焊盘（6 个块，同 Pads6），类型 5 是文字（多一个字符串块），其余都是 `[类型][长度][数据]`；12 是 3D 体。region 记录也带 `V7_LAYER=` 文本但没有 OVERALLHEIGHT，按 `V7_LAYER` 找 3D 体时先判断有没有 OVERALLHEIGHT。

## 中文和其他编码

- 规则 Comment 等字段：`COMMENT=` 是本地代码页（GBK）字节，按 latin-1 解是乱码；同一条记录里的 `UNICODE__COMMENT=116,105,...` 是逗号分隔的 Unicode 码点，用它（`pcbdoc_rules.py` 已处理）。
- PcbLib 的 `DESCRIPTION=` 是 GBK 字节。PcbDoc 的 `FOOTPRINTDESCRIPTION=` 两种存法都有：码点列表（`84,89,80,69,…`），或 GBK 字节。解析器两种都要支持。

## 比对两个版本时的噪声

每次保存都会变、和设计无关的：
- `FileHeaderSix`、`LayerKindMapping`、全部 `T*Violation` 流；
- Board6 的 DATE/TIME、VP.LX/HX/LY/HY、2DCONFIGURATION（图层开关顺序轮换）、HASHKEY#n/HASHVALUE#n；
- Texts6 字体名字段后的填充。

从磁盘重开文档或改过 3D 体之后保存，还会变：
- Pads6 每个焊盘 [126:142] 的内部 ID（新旧一一对应）；
- Tracks6、Arcs6、Texts6、WideStrings6、UnionNames 的记录顺序（集合不变）；
- 改阻焊外扩规则后，所有焊盘缓存的外扩值；
- 改 3D 体后，体的 MODELID、MODEL.CHECKSUM 重新生成；PcbLib 里体的 MODEL.2D.X/Y 从 0 变成相对封装原点的偏移（和 PCB 上一致）。

PcbLib 保存时会重写载入过的封装：没改过的封装也会换 UNIQUEID、换图元顺序。

认版本用 SHA-256，不要用 Board6 的 TIME（几个备份的 TIME 一样）。

## AD 的 History 备份

- 位置：`<工程目录>\History\<文件名>.~(N).<扩展名>.Zip`，PcbDoc、PcbLib、PrjPcb 都有，每个 zip 里只有一个文件。
- **每次保存时生成，里面是这次保存之前的版本**（用 SHA-256 证实）。要拿"上一轮的结果"做比对，就取对应编号解压。
- 按时间排序找最新的：按名字排 `(10)` 会排在 `(2)` 前面。
