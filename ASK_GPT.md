# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 17:47:45

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
报价清单 Excel 样式优化已完成，字段映射规则已强化。

## 本轮结果
- 生成记录数：2
- 输出文件：output/宏业标准版报价清单草稿_v1.xlsx（不提交 GitHub）
- 报告：04_AI交接/node_reports/Mac_Hongye_Quote_Draft_V1_Styled_Report.md
- 脚本：07_scripts/generate_hongye_quote_draft_v1.py
- 字段映射脚本：07_scripts/standardize_unpriced_quantity_v1.py

## 请求 GPT 判断
请 GPT 给出下一步最小闭环任务。

建议优先级：
1. 唐老板补充标准无价工程量清单后，做真实输入验证。
2. 准备宏业定额数据库结构扫描，但暂不提交数据库。
3. 设计定额匹配接口 V1，用占位数据替代真实数据库。
4. 继续强化字段映射规则。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
