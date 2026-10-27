---
name: enclosure-dwg-import
description: 把外壳结构 DWG（板框、挖空、通孔、禁布区、限高区、印碳区）转进 Altium PCB：scripts 里有整套脚本（accoreconsole 转 DXF 并炸开填充、按工程配置对齐正面/背面视图、重建填充区域、生成机械层图形、Board Cutout、非金属化孔、Room 和高度规则、导入 AD 的 .pas、和 PcbDoc 离线比对），以及支撑柱、印碳区、天线区的 keepout 和豁免做法。拿到或更新外壳 DWG、重新生成外壳规则时用。
---

# 外壳 DWG → Altium

工程相关的参数（视图位置、图例、机械层、Room 名、豁免、挖空位置）都写在工程自己的配置文件里（TOML，格式见下文），脚本里没有工程的值。

## 脚本（`scripts\`）

| 脚本 | 作用 |
|---|---|
| `dwg2dxf.ps1 -Dwg <dwg> -Out <工作目录> [-AcCore <accoreconsole.exe>]` | 把 DWG 复制进工作目录，用 accoreconsole 输出 `outline.dxf`（DXFOUT），再在另一份副本上炸开全部 HATCH，图案线按填充的句柄写进 `hatchlines.txt`。不碰原 DWG |
| `survey.py <工作目录> [板框图层]` | 第一次看图：图层和颜色、各图层图元范围、填充、文字、板框图层的分组（每组是一个视图），`survey.png` 是全图 |
| `shell_import.py <配置.toml> <工作目录>` | 主流程：展开 INSERT → 找视图 → 机械层图形 → 填充区域重建 → Room/高度规则 → 挖空和通孔；输出见下 |
| `compare_pcbdoc.py <工作目录> <PcbDoc> [结果.txt]` | 把输出和磁盘上的 PcbDoc 逐项比对（只读，要 `olefile`）；还会列出导入时会被删、但不会重建的规则 |
| `pas\import_drawing.pas`、`import_cutouts.pas`、`import_rules.pas` | 导入 AD 的模板，`shell_import.py` 填好路径后写进工作目录 |
| `dxflib.py`、`regions.py`、`canvas.py` | DXF 读取和 HATCH 边界解析、填充区域重建、PNG 预览 |

- 要 Python 3.11 以上（用 `tomllib`），只用标准库；`compare_pcbdoc.py` 另要 `olefile`。PowerShell 脚本用 PowerShell 7 跑：`pwsh -NoProfile -ExecutionPolicy Bypass -File ...`。
- 工作目录放临时目录（scratchpad），路径只能是 ASCII（写进 `.scr` 里）。中间数据不要放进工程，也不要放 MCP 的交换目录。
- accoreconsole 默认取 `C:\Program Files\Autodesk\AutoCAD *\accoreconsole.exe` 里最新的一个。

`shell_import.py` 的输出（坐标都是 mm，相对板原点）：

| 文件 | 内容 |
|---|---|
| `report.txt` | 板框分组和选中的视图、每个视图里各（图层, 颜色, 类型）的数量和去向、填充列表、每个区域的 Room（面积、范围、豁免）、被丢掉的碎片、挖空和通孔、视图附近的文字（只供阅读，不导入）、警告 |
| `front.png`、`back.png` | PCB 坐标下的预览：轮廓线按机械层颜色，Room 半透明填充 |
| `drawing.txt` | `L 层号 名称 颜色` / `T 层 x1 y1 x2 y2 线宽` / `A 层 cx cy r 起角 止角 线宽` |
| `cutouts.txt` | `C 点数` 加若干 `V x y`（一个 Board Cutout）/ `H x y 孔径 名称` |
| `rules.txt` | `D 前缀`（导入前删掉同前缀的规则）/ `R 名称 层 DRC 范围 注释 minx miny 点数` 加若干 `V x y` / `H 名称 max min 范围 注释` / `P 名称`（优先级） |
| `import_*.pas` | 填好 PcbDoc 路径和数据路径的导入脚本 |

## 流程

1. `dwg2dxf.ps1` 转换。
2. 新工程先跑 `survey.py`，读图例文字和 `survey.png`，弄清视图摆法、颜色含义，**和用户核对**后写配置。
3. 跑 `shell_import.py`。读 `report.txt`：警告、每个视图的图层/颜色去向（有没有该进区域却归到元器件的）、被丢掉的小块、Room 列表；看两张预览图。
4. 离线比对：`git show <版本>:<文件>.PcbDoc > <副本>`，`compare_pcbdoc.py <工作目录> <副本>`。DWG 改版时差异就是改版内容加上编号变化；每处差异都要说得清来源再导入。
   "导入时会被删、但不会重建的规则"那一行必须是 none，否则说明有手建规则用了生成规则的前缀。
5. 导入 AD（先读 altium-mcp skill）：
   - 导入规则之前，工程如果开着"原理图生成 Room"，先按 altium-mcp skill 的 `references/pcblib-and-eco.md` 关掉生成和比较 Room（原因见下文"导入 AD"）。
   - 依次把 `import_drawing.pas`、`import_cutouts.pas`、`import_rules.pas` 的内容交给 `run_altium_script`，`timeout_seconds` 给 600。每个脚本先切到配置里的 PcbDoc、核对文件名，不对就不动。
   - 按 altium-mcp skill 的方法保存，再用 `compare_pcbdoc.py` 比对保存后的文件，应当没有差异。
6. 在生成结果上手改过的地方，要么做成配置项（范围后缀、Min、豁免），要么记进工程文档，并确认它不会被第 5 步的清理删掉。

导入脚本各自先删什么（都能重复执行）：

| 脚本 | 先删除 |
|---|---|
| `import_drawing.pas` | `drawing.txt` 的 L 行列出的机械层上，所有不属于元件的走线、圆弧、文字（这些层归导入所有） |
| `import_cutouts.pas` | 所有不属于元件的 Board Cutout（Descriptor 含 "Board Cutout"，AD 内部那块板形区域不删）；名称和 H 行相同的、不属于元件的非金属化焊盘 |
| `import_rules.pas` | 名称以 D 行前缀开头的规则。规则建完后按 P 行顺序逐条空修改，最后一条排到同种类的优先级 1 |

keepout 区域、其他名称的规则、元件都不动。

## 配置文件格式

放在工程里（例如 `docs\`），随工程提交。相对路径相对配置文件所在目录。

```toml
pcbdoc = "../<板>.PcbDoc"                # 导入脚本切到这个文档并核对

[dwg]
outline_layer = "<板框图层>"             # 板框和通孔所在的图层
skip_layers = ["<注释图层>"]             # 这些图层的线和文字不导入；它们上面的填充仍按颜色归类
legend_default = "comp"                 # 图例里没有的颜色归这一类
legend = { <ACI> = "keepout", <ACI> = "carbon", <ACI> = "hlow" }   # ACI 颜色号 → 类别（类别名自定）

[views]
pcb_outline_min = [<x>, <y>]            # 板框外接框左下角的 PCB 坐标
margin = 12                             # 图元外接框在"视图板框外接框外扩 margin"以内才算这个视图（默认 12）
group_gap = 3                           # 板框图元分组的间隙（默认 3）
front = { box = [x0, y0, x1, y1] }      # DWG 坐标的大致范围，里面只能有一组板框图元
back = { box = [x0, y0, x1, y1], mirror = true }   # 按背部视角画的视图要左右镜像
sides = [[x0, y0, x1, y1]]              # 侧视图：完整落在框里的图元按正面视图平移，放到 mech.side 层

[layers]                                # 用到的每个机械层：名称和颜色（$00BBGGRR）
<n> = { name = "<名称>", color = "$00BBGGRR" }

[mech]                                  # 每一面：类别 → 机械层号；side 是侧视图的层
side = <n>
front = { comp = <n>, keepout = <n>, ... }
back = { comp = <n>, keepout = <n>, ... }

[widths]                                # 线宽：DWG 线条、炸开的图案线、SOLID 填充的边、侧视图
line = 0.1
pattern = 0.05
solid_edge = 0.06
side = 0.1

[[region]]                              # 一面的一个类别 → 一组 Room，名称 = room + 两位序号（按面积从大到小）
room = "<前缀>"
face = "front"                          # front / back
category = "keepout"
layer = "top"                           # Room 的层：top / bottom
drc = true                              # false：只作区域，给高度规则的 TouchesRoom 用
scope = "IsComponent and OnTopLayer"
suffix = ""                             # 接在范围最后（例如排除零高度铜皮元件）
comment = "<注释>"
min_area = 0.05                         # 比这小的碎片丢掉（mm²）

[[height]]                              # 高度规则：scope and (TouchesRoom(该前缀的全部 Room)) [and Not (exclude)] + suffix
name = "<规则名>"
rooms = "<region 的 room 前缀>"
max = 1.0
min = 0.01                              # 0.01 让高度未知（0）的元件也报错
scope = "IsComponent and OnBottomLayer"
exclude = ["<位号>"]
comment = "<注释>"

[[exempt]]                              # 只在一个 Room 里豁免的元件
room = "<前缀>01"                       # 期望的 Room 名
at = [x, y]                             # 该 Room 内的一点（PCB 坐标）；生成时核对这点所在的 Room 就是 room，否则报错
parts = ["<位号>"]

[cutouts]
boxes = [[x0, y0, x1, y1]]              # PCB 坐标；每个框里正面视图板框层的线要连成一个闭环
margin = 0.1                            # 默认值，下同
arc_tol = 0.002                         # 圆弧拆成直线的弦高
chain_tol = 0.005                       # 首尾相接的容差

[holes]                                 # 正面视图板框层上、挖空框以外的整圆
min_radius = 0.6
name = "NPTH"

[rules]
priority_order = ["<最宽>", "...", "<最紧>"]   # 导入后逐条空修改，可以包含手建的规则
```

- Room 编号按面积排序。DWG 改版后编号可能变，`exempt` 的核对会报出来；别的规则（例如按 Room 名找区域的间距规则）引用了 Room 名时，同样要查。
- 区域重建：以该面、该类别的线和填充自带的边界环为边界，炸开的图案线为种子，栅格（0.025 mm）填充 → 吸收边界 → 补对角接触 → 从洞开缝到外面 → 追踪像素边 → Douglas-Peucker。SOLID 填充没有图案线，用边界环内合成的线当种子。

## 读图

- 先弄清三视图的摆法。常见的是：正面视图与板框平移后完全重合；背面视图按背部视角绘制，**要左右镜像**后才能和板框对齐。
  两个视图的板框有一边缺了一段（被元件挡住没画）时，完整外形以另一边为准；两边外接框尺寸不同时，`shell_import.py` 会警告。
- 按图例确认颜色/图层的含义，导入前和用户核对。
- 注释图层的引线和文字先问用户要不要导入（脚本不导入文字，`skip_layers` 管引线）。注释图层上的色块同样按图例归类，不要当成注释丢掉。
- **填充区域以 `EXPLODE` 炸开后的图案线为准**，那是图上实际显示的内容。HATCH 自带的边界环（flag 32 等）不保证闭合，只当附加边界用。
- accoreconsole 的 `(load "x.lsp")` 会被 SECURELOAD 拦截（临时目录不受信任）。不要改这个安全设置，LISP 直接写在 `.scr` 里。
- `ssget "X"` 选不到块定义里的实体，块里的填充不会被炸开；`shell_import.py` 遇到这种填充会警告。
- 提取板内挖空时剔除悬空线段（比如外框开槽处的缺口线会混进来），重复的边只取一条。圆弧按弦高拆成直线。

## 导入 AD

API 写法见 altium-mcp skill 的 `references/pcb-scripting.md`、`references/rules-and-drc.md`。

- 挖空建 Board Cutout，通孔建非金属化焊盘（焊盘尺寸 = 孔径）。注意孔径是否超出现有 HoleSize 规则。
- 工程开着"原理图生成 Room"时，ECO 会提议删掉脚本建的 Room；脚本建的 Room 继承了某张图纸 Room 的 UniqueID 时，ECO 还会把它改回那张图纸的 Room，这块禁布区就静默失效了。所以导入规则前先关掉生成和比较 Room。
- 区域转规则：
  - 禁布区、印碳区建 Keep-out Room，参与 DRC；范围写明 `IsComponent and OnTopLayer` 或 `OnBottomLayer`。零高度的铜皮元件（如印制天线）要从范围里排除（`suffix` 加 `and Not InComponent('<位号>')`），否则它挨着禁布区就报。
  - 限高区建 DRC 关闭的 Room 只作区域，再建高度规则，范围是"该面元件 + TouchesRoom(...)"。限得越紧的规则优先级越高。
    新建或修改规则都会把它排到同种类的优先级 1，所以排序要放在最后做（`priority_order`）。
  - 高度兜底：限高规则的 Min 设 0.01，再加一条覆盖全部背面元件的兜底高度规则（Min 0.01），这样高度为 0（未知）的元件一放进限高区或背面就报错。测试点、Mark 点这类纯铜元件另建一条优先级最高的例外。
  - DWG 自己画在区域里的元件（壳下按键、导光窗里的 LED、印碳区上的导电胶按键、图上指定高度的开关）只在所在区域豁免，其他元件照常检查。整条高度规则豁免的元件等于没有上限，要另给一条带上限的高度规则。
- 只靠 Room 管不到走线、过孔和焊盘的区域，用 keepout 区域加规则实现（脚本不生成，手建后记进工程文档）：
  - **外壳支撑柱**：背面 keepout，限制项只选 SMD 焊盘和通孔焊盘。走线、过孔不受限；过孔会被柱子压到，靠盖油规则保证不露铜。
  - **印碳区**：顶层 keepout（全部限制项），再加一条间距 0 的 Clearance 豁免：`IsKeepOut and WithinRoom('<印碳 Room 名>')` 对"本键元件，或本键网络的走线和圆弧（`Not InPolygon`）"。这条规则靠 Room 名找区域，重新生成时 Room 名不能变。
  - **天线区**：两面各一块同形 keepout（限制过孔、走线、铺铜、焊盘），一个禁元件的 Room，再加 Clearance 和 ShortCircuit 豁免天线自身。Room 为了让开旁边元件的外框开了缺口时，keepout 不再完全落在 Room 里，豁免范围要用 `TouchesRoom`，`WithinRoom` 判不中；这时挨着天线 Room 的其他 keepout 也会被算进豁免，两者要留出间隙。
  - keepout 区域在 AD 里没有名字，只能按位置识别。
- 默认的板边间距（BOC）规则范围用 `OnCopper and Not IsKeepOut`，不要用 All。贴着板框画的 keepout 和伸出板外的 keepout、丝印、文字，都会被报。
- 不要用 sed 或 Python 字符串字面量往 `.pas` 里填 Windows 路径（反斜杠会被转义）；`shell_import.py` 已经填好。
