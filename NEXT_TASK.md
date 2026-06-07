# NEXT_TASK

## 当前待执行轮次
HY-R024

## 任务名称
NEXT_TASK 自动读取执行器第一版

## 任务目标
让 Windows Codex 能从公共状态仓库读取 NEXT_TASK.md，识别轮次、任务名称、执行目标和安全边界，生成本地执行报告，但暂不自动执行危险或真实业务动作。

## 建议执行内容
1. 检查公共状态仓库是否可 pull。
2. 读取 NEXT_TASK.md。
3. 解析当前待执行轮次和任务名称。
4. 生成 HY-R024_NEXT_TASK_Reader_Report.md。
5. 更新 AUTO_LOOP_STATUS.json。
6. 提交并 push 公共状态仓库白名单状态文件。

## 禁止事项
- 不读取真实客户文件。
- 不读取宏业数据库。
- 不执行真实报价。
- 不提交 XLSX/PDF/GCFX/数据库/压缩包。
- 不破解、不绕过、不修改 N10。
- 不使用 git add .
- 不 force push。

## 完成后交给 GPT 判断
GPT 根据 HY-R024 报告决定是否进入 HY-R025：自动执行安全白名单任务。
