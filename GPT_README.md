# GPT_README - 宏业项目读取入口

## 给 GPT 的说明

当唐老板说“继续宏业”时，请优先读取公共状态仓库中的以下文件：

1. GPT_ENTRY.md
2. STATUS_NOW.md
3. ASK_GPT.md
4. REPORT_INDEX.md
5. LOOP_LOG_TAIL.md
6. Hongye_Next_Actions.md

## 项目方向

宏业自动报价单 / 报价清单生成系统。

核心目标：
导入带工程量的任意格式表格，参考学习范本，结合电脑已有宏业定额数据库，自动输出宏业标准版报价清单。

## 禁止跑偏

不是 CAD 项目。
不做 AutoCAD / LISP / DWG / DXF / 图纸测试。

## GPT 下一步职责

根据 ASK_GPT.md 和最新报告，生成一段可以直接复制给 Codex 执行的下一轮命令。

## 安全边界

- 不提交原始 XLSX
- 不提交 output XLSX
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不 force push
- 不 git add .
