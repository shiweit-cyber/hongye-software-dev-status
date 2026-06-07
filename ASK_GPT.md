# ASK GPT - Hongye Quote Generator

## 时间
2026-06-07 13:19:50

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
DB3 字段映射配置 + 人工复核 Excel V1 已完成。

## 本轮结果
- 字段映射配置：05_字段映射/hongye_db3_field_mapping_v1.json
- V3 脚本已增强：07_scripts/match_hongye_quota_v3_db3_query.py
- 人工复核脚本：07_scripts/generate_hongye_manual_review_v1.py
- 测试：tests/test_hongye_manual_review_v1.py
- 报告：04_AI交接/node_reports/Mac_Hongye_Manual_Review_V1_Report.md
- 复核行数：2
- 需要人工复核：2
- 每条最多展示候选：3
- 本地复核 JSON：output/hongye_quota_manual_review_v1.json（不提交）
- 本地复核 Excel：output/宏业定额匹配人工复核_v1.xlsx（不提交）

## 关键能力
- DB3 字段映射配置固定 debh / demc / xmmc / mc / dw / fbmc
- 禁止价格字段：rgf / clf / jxf / price / cost / fee / 单价 / 合价 / 价格 / 人工费 / 材料费 / 机械费
- V3 输出 best_match / candidates / match_score / match_confidence / confidence_gap / review_required / review_reasons
- 人工复核 Excel 展示前三候选、置信度差距、复核原因，并预留人工确认列

## 请求 GPT 判断
请 GPT 判断下一步最小闭环。

建议优先级：
1. 等唐老板提供标准无价工程量清单后做真实输入验证。
2. 若要接真实 DB3，请由唐老板本机设置 HONGYE_DB3_PATH，不要把路径写入代码或报告。
3. 用真实输入跑 V3 查询匹配 + 人工复核 Excel，但仍不提交 output 和 DB3。
4. 根据人工复核结果优化关键词和置信度规则。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
