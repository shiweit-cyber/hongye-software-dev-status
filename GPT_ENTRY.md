# GPT_ENTRY - 宏业项目 GPT 读取入口

## 当前状态

这是宏业自动报价单项目的公共状态入口。

唐老板在 ChatGPT 里说“继续宏业”时，GPT 应读取本仓库以下文件并生成下一轮 Codex 命令：

- STATUS_NOW.md
- ASK_GPT.md
- REPORT_INDEX.md
- LOOP_LOG_TAIL.md
- Hongye_Latest_Status.md
- Hongye_Next_Actions.md

## 项目方向

宏业自动报价单 / 报价清单生成系统。

## 当前协作方式

Git 链接稳定版：
Codex 前台执行一轮 → GitHub 同步状态 → GPT 读取状态 → 生成下一轮命令。

## 注意

不使用 OpenAI API。
不做后台长循环。
不混入 CAD / LISP / DWG / DXF。
