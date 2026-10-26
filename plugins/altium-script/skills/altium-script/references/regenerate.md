# 重新生成 API 字典

AD 升级（或要给另一个 AD 版本做字典）时按下面做。全程纯 Python，Windows ARM64 上也能跑（capstone、iced-x86 在 ARM64 上装不了，所以自带了 `x64lite.py` 解码 x64 指令）。

## 步骤

1. 在本目录原地重新生成，旧版本靠 git 找回：先确认工作区干净，用 `git tag -f ad<当前版本>` 把当前版本的 tag 打在最新提交上（AD23 的是 `ad23`；之后还有提交的话 tag 会落后，所以用 `-f` 移过来）。目录名和 SKILL.md 的 `name` 保持 `altium-script` 不变（altium-mcp 的 `ensure_altium_script_skill` 按 `~/.claude/skills/altium-script/SKILL.md` 检查），只改描述和正文里的版本号。
2. 建一个装了 pefile 的虚拟环境（放临时目录即可）：
   ```
   python -m venv <venv>
   <venv>\Scripts\python -m pip install pefile
   ```
3. 提取（约 10 秒）：
   ```
   <venv>\Scripts\python -X utf8 <skill>\scripts\extract_api.py "<AD 安装目录>" <skill>\data\api.json
   ```
   AD 安装目录从注册表 `HKLM\SOFTWARE\Altium\Builds\*` 的 `ProgramsInstallPath` 查，或者取正在运行的 `X2.exe` 所在目录。
4. 核对输出，三条都满足才算提取成功：
   - `registrars:` 一行列出 13 个注册函数（imeth、intf、iprop、iidx、cmeth、proc、cprop、cidx、const、classes、record、var、field），而且没有打印 `warning`。
   - `unresolved {}`。
   - 数量和 AD23 在同一量级。AD23 的数是：接口 1204（方法 12163、属性 3185）、类 990、全局函数/过程 2514、记录类型 389、常量 9810、枚举类型 754、变量 84。
5. 提取进程表、生成文档（只用标准库，不必在虚拟环境里）：
   ```
   python -X utf8 <skill>\scripts\extract_processes.py "<AD 安装目录>" <skill>\data\processes.json
   python -X utf8 <skill>\scripts\gen_docs.py <skill>\data\api.json <skill>\references\api
   ```
   进程表 AD23 是 1372 个命令（`.ins` 里 965 个，只在 `.rcs` 里的 407 个），带参数的 382 个。
   再对 `references/patterns.md`、`processes.md` 里出现的每个 API 名和进程名跑 `lookup`，查不到的在文中标出。
6. 实测同名常量：对 `Constants.md` 开头"同名常量冲突"表里的每个整数常量，在 AD 里用 `run_altium_script` 跑 `ResultText := 'X=' + IntToStr(X) + ...`。结果要和"脚本里的值"一列一致；不一致说明新版本的生效规则变了，改 `extract_api.py` 里"the first registration (lowest address) is the one scripts see"那段。
7. 更新 SKILL.md 里提到的版本号、日期、数量，以及"同名常量"一节的例子。

## 原理

脚本引擎在初始化时调用十几个注册函数，把每个接口、方法、属性、全局函数、类和常量登记进去。参数里带着名字字符串、`_Tnnn` 方法类型的 RTTI（参数名、类型、返回值都在里面）、接口 GUID 或类的 VMT。`extract_api.py` 的做法：

1. 按 `.pdata` 列出所有函数，用 `x64lite.py` 逐条解码，跟踪每个 `call` 前 rcx/rdx/r8/r9 和栈上参数装的是什么（字符串常量、RTTI 指针、GUID 地址、立即数）。
2. 按参数的形状认出注册函数：比如"rcx=GUID 地址、rdx=字符串、r8=方法 RTTI"出现最多的那个函数就是"注册接口方法"。所以不依赖具体地址，换版本也能认。
3. GUID 按 16 字节内容匹配接口（各单元有自己的 GUID 常量副本，地址对不上）。
4. 常量的值是注册前构造的 Variant：按构造函数区分整数、字符串、集合、浮点等。同名常量保留所有注册值，取地址最靠前的那个作为脚本里的值。

## 容易坏的地方

- **类名全是空的、类数量骤减**：Delphi 编译器换了版本，VMT 布局变了。改 `extract_api.py` 开头的 `VMT_TYPEINFO`、`VMT_CLASSNAME`、`VMT_PARENT`（AD23 的编译器 vmtSelfPtr = -200，对应 -168/-136/-120）。可以对一个已知类的 VMT 往前逐 8 字节找指向类名 ShortString 的指针来确定。
- **某个注册函数没找到或打印 warning**：注册函数的参数形状变了。看 `detect()` 里对应的判断条件。
- **常量值大量为 `unknown`**：Variant 构造函数的调用方式变了，看 `const_value()` 和 `x64lite.py` 里跟踪的指令种类。
