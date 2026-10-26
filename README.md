# pcb-tools

Claude Code 插件商店：Altium Designer 自动化（MCP 服务和实战经验）、外壳 DWG 导入、立创数据手册查询、PDF 和图片阅读。

所有插件都只能在 **Windows** 上用，包括 Claude Code 命令行和桌面版 Code 标签页里的本地会话。claude.ai 网页版和云端会话不加载本机插件，用不了。

安装时要用 `git` 从 GitHub 克隆本仓库，以及 `altium-mcp` 的上游仓库，所以机器上要装有 git，并且能访问 GitHub。

大部分插件要用 **Python**，`altium-mcp` 要 3.10 以上。Claude Code 和桌面版都不自带 Python，没装的先装一个，比如：

```bash
winget install Python.Python.3.13
```

也可以从 python.org 下载安装，安装时勾选「Add python.exe to PATH」。

## 插件

| 插件 | 内容 | 会连带安装 | 另需准备 |
|---|---|---|---|
| `altium-mcp` | Altium Designer 的 MCP 服务 `altium`，安装上游 [coffeenmusic/altium-mcp](https://github.com/coffeenmusic/altium-mcp) 的最新提交 | — | Altium Designer（实测 AD23）、Python 3.10+ |
| `altium-script` | skill `altium-script`：AD23 的 DelphiScript API 字典（从 AD23 脚本引擎提取的成员签名、属性是否只读、常量和枚举的实际值、进程名和参数），附 `lookup.py` 查询脚本、写法模式和 Altium 官方示例脚本 | — | Python 3（`lookup.py` 只用标准库） |
| `altium-mcp-guide` | skill `altium-mcp`：使用 altium MCP 的实测经验，包括沙盒限制、出错和卡死后的恢复、用 UIA 处理模态对话框、规则/Room/DRC、封装库和 ECO、从磁盘解析 PcbDoc | `altium-mcp`、`altium-script` | 解析 PcbDoc 的脚本要 `pip install olefile` |
| `enclosure-dwg-import` | skill：把外壳 DWG 里的板框、挖空、通孔、禁布区、限高区、印碳区转进 Altium PCB，附整套脚本 | `altium-mcp-guide` 及其依赖 | AutoCAD（要用其中的 accoreconsole）、Python 3.11+；`compare_pcbdoc.py` 要 `olefile` |
| `doc-image-viewing` | skill：把 PDF 任意页渲染成 PNG、裁剪放大图片、解析旧版 .doc/.xls | — | 解析 .doc/.xls 要 `pip install olefile xlrd` |
| `lcsc-datasheet` | skill：按立创 C 编号或型号查料，下载数据手册 | `doc-image-viewing` | 能访问立创网站和 pcbparts.dev |
| `pcb-all` | 本身不含内容，装它就会装上以上全部插件 | 全部 | 同上 |

注意区分：**插件** `altium-mcp` 是 MCP 服务；**skill** `altium-mcp` 是使用说明，在 `altium-mcp-guide` 插件里，装好后显示为 `altium-mcp-guide:altium-mcp`。

## 安装

**Claude Code 终端会话里**（`/plugin` 只能在终端交互会话里用）：

```
/plugin marketplace add apple-gif59/pcb-tools
/plugin install pcb-all@pcb-tools
```

执行 `/plugin install` 后先弹出详情面板，选好安装范围（一般选 user）才会安装。只需要部分功能时，把 `pcb-all` 换成对应的插件名，依赖会一起装上。比如只想看 PDF，就装 `doc-image-viewing`。

**终端里：**

```bash
claude plugin marketplace add apple-gif59/pcb-tools
```

```bash
claude plugin install pcb-all@pcb-tools --scope user
```

终端安装不会问 Python 路径。`--config` 只对命令里写的那个插件生效：直接装 `altium-mcp` 时可以加 `--config python=<python.exe 的完整路径>`；装 `pcb-all`、`altium-mcp-guide`、`enclosure-dwg-import` 时，`altium-mcp` 是作为依赖装上的，`--config` 不会传给它（CLI 会提示 `--config not applied`）。这时装完再单独设置（路径用正斜杠，反斜杠在 JSON 里要写成 `\\`）：

```bash
echo '{"python":"C:/Python313/python.exe"}' | claude plugin configure altium-mcp@pcb-tools --values-stdin
```

不带 `--values-stdin` 执行 `claude plugin configure altium-mcp@pcb-tools` 可以查看当前是否已设置。装完或改完后重开 Claude Code，或者在会话里执行 `/reload-plugins`。

**桌面版 Code 标签页：** 点输入框旁的 **+** → **Add plugins**，在插件浏览器里选插件和安装范围。浏览器里只列出已添加商店里的插件。官方文档没写桌面版怎么添加商店。可以在装了 Claude Code 命令行的终端里，执行上面的 `claude plugin marketplace add`，终端和桌面版本地会话用的是同一份设置。（这条未实测。）

## altium-mcp 的 Python 和首次启动

- `altium-mcp` 的 **Python 解释器**是必填项，每台机器各填各的，存在本机 `%USERPROFILE%\.claude\settings.json` 的 `pluginConfigs` 里。命令行里的 `python` 能用就填 `python`。全新的 Windows 11 上，`python` 可能只是一个打开微软商店的占位程序，什么都跑不起来。这种情况请填 Python 3.10+ 的 `python.exe` 完整路径。在终端会话里用 `/plugin` 安装时会让你填。终端安装、作为依赖安装、桌面版安装可能不会问，装好后用 `/plugin configure altium-mcp@pcb-tools`，或者上面终端里的 `claude plugin configure` 命令补上。
- 这一项没填时，`altium` MCP 不会启动。以前没设成必填时，配置项里的默认值并不会代入命令，Claude Code 会把 `${user_config.python}` 这串字面量当程序去执行，报「不是内部或外部命令」，界面上只显示 `Connection closed`（Claude Code 2.1.308 实测）。MCP 日志在 `%LOCALAPPDATA%\claude-cli-nodejs\Cache\<项目目录>\mcp-logs-plugin-altium-mcp-altium\`。
- 第一次启动时，`start_server.py` 会在 `%USERPROFILE%\.altium-mcp\venvs\` 下建虚拟环境，并下载依赖（`mcp`、`pillow`、`pywin32`），一般要一两分钟，会超过 Claude Code 30 秒的连接超时。建环境的是一个分离出去的进程，但 Claude Code 超时结束 MCP 进程时，它也可能被一起结束（`claude mcp list` 的健康检查实测如此）。这时虚拟环境只建了一半，`%USERPROFILE%\.altium-mcp\build.log` 里最后只有一行时间戳，没有 `ready in N s`。遇到这种情况，就在终端里手动建一次（不受超时限制，`<版本>` 是 `altium-mcp` 下唯一的那个目录）：

  ```bash
  python "$USERPROFILE/.claude/plugins/cache/pcb-tools/altium-mcp/<版本>/start_server.py" --build
  ```

  输出 `ready in N s` 就是装好了，然后在 `/mcp` 里重连。这里的 `python` 要和 MCP 配置的解释器是同一个，否则建出来的虚拟环境对不上。
- AD 的安装路径会自动查找，结果存在 `%USERPROFILE%\.altium-mcp\config.json`。这个目录在插件目录外面，插件更新时不受影响。

## 更新

`altium-mcp` 跟随上游仓库，其余插件跟随本仓库的提交。这些插件都没写 `version`，所以每次提交就是一个新版本。

第三方商店默认不自动更新。建议打开自动更新：在 `/plugin` 的 **Marketplaces** 标签里选 `pcb-tools`，再选 **Enable auto-update**。不打开的话，就在同一处选 **Update marketplace** 手动更新，或者在终端执行：

```bash
claude plugin update altium-mcp@pcb-tools
```

`claude plugin marketplace update` 只负责刷新商店清单。要更新已经装好的插件，用上面的 `claude plugin update <插件名>@pcb-tools`，或者用面板里的 **Update marketplace**。

## 以前手动装过的，先清掉

如果以前手动注册过 altium MCP，或者把这些 skill 直接放进了 `%USERPROFILE%\.claude\skills\`，装插件前先删掉，否则会出现两份同名的东西。

- 手动注册的 `altium` MCP：

  ```bash
  claude mcp remove altium -s user
  ```

  两个版本的 altium MCP 共用 `%USERPROFILE%\.altium-mcp`。依赖不同时，一方新建虚拟环境，会删掉另一方的虚拟环境，所以不要同时保留。
- `%USERPROFILE%\.claude\skills\` 下的 `altium-script`、`altium-mcp`、`doc-image-viewing`、`enclosure-dwg-import`、`lcsc-datasheet`：删掉或移到别处。
- 装了 `altium-script` 插件后，不要再用 MCP 的 `ensure_altium_script_skill(install=True)` 装一份。这个工具只检查 `~/.claude/skills/altium-script/SKILL.md` 在不在，插件装在 `~/.claude/plugins/cache/` 下，名字一样也检测不到，所以会报告没装；这时传 `install=True` 会把上游 coffeenmusic/altium-scripts-skill 的另一套字典克隆进去，和插件版重复。

## 仓库结构（维护用）

```
.claude-plugin/marketplace.json     商店清单；altium-mcp 条目直接指向上游仓库
plugins/<插件名>/.claude-plugin/plugin.json
plugins/<插件名>/skills/<skill 名>/SKILL.md 及脚本
plugins/pcb-all/                    只有 plugin.json，用 dependencies 列出全部插件
```

- 改了 skill，提交推送就行，不用改版本号。`claude plugin validate` 报 "No version specified"，是因为故意没写 `version`。
- 校验命令：`claude plugin validate .`，以及 `claude plugin validate plugins/<插件名>`。
- `altium-mcp` 条目里的 `mcpServers` 和 `userConfig` 之所以生效，是因为上游仓库没有 `.claude-plugin/plugin.json`。上游哪天自己加了 `plugin.json`，这两项就会被忽略，以上游的清单为准，到时要重新检查。
- 上游的每个提交都会直接推给用户。想锁定版本，就在 `source` 里加 `"ref": "<tag>"`。

## 许可

- `altium-mcp`：上游采用 MIT 许可证。
- `altium-script`：字典（`data/`、`references/api/`）从 AD23 安装目录提取，`scripts/` 和 `patterns.md`、`processes.md` 由本仓库作者编写（后两个从 coffeenmusic/altium-scripts-skill 的说明里挑选、改写）。`references/scripts/` 是 Altium 官方的 DelphiScript 示例，来自官方文档 Scripting Examples Reference 页面的 Examples.zip，文件头写有 Altium 的版权声明。`references/overview.md`、`summaries.md` 复制自 coffeenmusic/altium-scripts-skill，上游仓库没有许可证文件。
- 其余插件由本仓库作者编写。
