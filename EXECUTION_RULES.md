# EXECUTION_RULES

## 执行原则
1. 每轮只执行 NEXT_TASK.md 指定任务。
2. 每轮执行时间建议控制在 3 到 5 分钟。
3. 每轮必须生成报告、状态文件、下一步建议。
4. 每轮必须保持安全边界。
5. 任何不确定、冲突、授权、真实文件、安全风险，都写入 ASK_GPT.md 等 GPT 判断。

## Git 规则
- 允许 pull。
- 允许只 add 白名单状态文件。
- 禁止 git add .
- 禁止 force push。
- 禁止删除远端提交。
- 禁止提交真实报价成果、数据库、图纸、压缩包、敏感凭据。

## 允许自动执行
- 读取状态文件。
- 读取脱敏样本。
- 执行自研脚本。
- 生成脱敏模拟输出。
- 生成报告。
- 更新公共状态文件。

## 禁止自动执行
- 读取真实客户文件。
- 读取宏业数据库。
- 破解、绕过、修改 N10。
- 生成或声称真实报价成果。
- 修改系统网络、代理、防火墙。
- 长期后台运行。

## 报告格式
每轮结束必须输出：
- 当前平台
- 当前轮次
- 本轮结论
- 输出文件
- 测试结果
- git status
- 最新 commit hash
- push 是否成功
- 安全边界确认

## No Foreground Window Rule - 2026-06-08 00:20:55

- Automation scripts must not open folders or files by default.
- Do not call explorer, Invoke-Item, Start-Process, os.startfile, or start to open output/reports/summary unless Tang Boss explicitly asks.
- Keep optional open behavior behind `-OpenOutput` or `--open-output`.
- Default behavior: generate files, write reports, and print/copy paths only.
