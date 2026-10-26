---
name: lcsc-datasheet
description: 按立创（LCSC/JLC）C 编号或型号查料、下载元器件数据手册 PDF，并渲染成图片阅读。需要查芯片或器件参数、核对 BOM 料号、看数据手册时用。
---

# 下载数据手册

## pcbparts MCP（用 curl 调）

- 托管的 MCP：`https://pcbparts.dev/mcp`，用 curl POST。JSON-RPC over HTTP，响应是 SSE 格式，不需要 API key。
- 请求头带 `Content-Type: application/json` 和 `Accept: application/json, text/event-stream`。
- 先发 `initialize`，再发 `notifications/initialized`。服务端不返回 `Mcp-Session-Id`，是无状态的；后面的请求不带会话 ID 也能用。
- 之后用 `tools/call` 调工具（`jlc_search`、`jlc_get_part` 等）。

## 流程

1. **确认料号**：用 `jlc_search` 找到料号，并且确认后缀和 BOM 完全一致。手册里常常按后缀区分版本，参数也不同（例如 ME4057 的 -A5 版和其他版本，充电电流系数不一样）。
2. **拿 PDF 链接**，按顺序试：
   - GET `https://wmsc.lcsc.com/ftps/wm/product/detail?productCode=C82651`，取 `result.pdfUrl`，直接就是 PDF。
     同一响应里的 `result.alternatePartList[]` 也带 `pdfUrl`，那是替代料，不要拿。wmsc 是立创网站内部接口，没有文档，失效了就用下一种。
   - `jlc_get_part`：参数 `lcsc`（如 `C82651`）时返回里有 `datasheet` 字段。
     参数用 `mpn` 时只返回候选列表（有 `lcsc`、`model`，没有 `datasheet`）：挑 `model` 和 BOM 完全一致的那行，再用它的 `lcsc` 调一次。
     这个 `www.lcsc.com/datasheet/...pdf` 打开其实是 HTML 查看页。用 `curl -L -A "Mozilla/5.0"` 下载后，在页面里找 `datasheet.lcsc.com/datasheet/pdf/<hash>.pdf?productCode=C…`，这个才是真正的 PDF。
   - jlcsearch 的 `/api/easyeda_components/<C编号>` 里，`c_para.link` 也有手册链接，但不一定对应同一个料号（C82651 返回的链接，文件名带的是 C389169），用之前要核对。
3. **下载**：PDF 放在 scratchpad 里单独的新目录。用 Python 读它时加 `-I`。
4. **阅读**：用 skill `doc-image-viewing` 的 `pdf2png.ps1` 渲染各页、`crop.ps1` 裁局部。
