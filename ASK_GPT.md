# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 17:56:13

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
定额匹配接口 V1 已完成，报价清单 V2 草稿已生成。

## 本轮结果
- 匹配记录数：2
- 匹配报告：04_AI交接/node_reports/Mac_Hongye_Quota_Match_V1_Report.md
- 匹配脚本：07_scripts/match_hongye_quota_v1.py
- V2 草稿脚本：07_scripts/generate_hongye_quote_draft_v2.py
- 本地匹配输出：output/hongye_quota_match_result_v1.json（不提交）
- 本地 V2 草稿：output/宏业标准版报价清单草稿_v2.xlsx（不提交）

## 请求 GPT 判断
请 GPT 给出下一步最小闭环任务。

建议优先级：
1. 设计真实宏业定额数据库结构扫描脚本，但默认只输出结构报告，不提交数据库。
2. 增强定额匹配接口：支持多候选、置信度阈值、人工复核标记。
3. 唐老板提供标准无价工程量清单后做真实输入验证。
4. 优化 V2 报价清单模板样式和导出说明。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
