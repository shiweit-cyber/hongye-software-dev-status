# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 17:39:24

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
标准化解析脚本 V1 已完成。

## 本轮结果
- 解析记录数：2
- 是否本轮生成假数据模板：否
- 报告：04_AI交接/node_reports/Mac_Standardize_Unpriced_Quantity_V1_Report.md
- 脚本：07_scripts/standardize_unpriced_quantity_v1.py

## 请求 GPT 判断
请 GPT 给出下一步最小闭环任务。

建议优先级：
1. 基于 V1 中间结构生成“宏业标准版报价清单草稿 V1”。
2. 若需要更真实数据，请唐老板补充标准无价工程量清单。
3. 强化字段映射规则，提升真实工程量清单解析能力。
4. 准备宏业定额数据库结构扫描，但暂不提交数据库。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
