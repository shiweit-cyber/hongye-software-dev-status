# ASK GPT - Hongye Quote Generator

## 时间
2026-06-07 13:09:51

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
真实 DB3 查询型匹配 V3 已完成。

## 本轮结果
- V3 脚本：07_scripts/match_hongye_quota_v3_db3_query.py
- V3 测试：tests/test_match_hongye_quota_v3_db3_query.py
- V3 报告：04_AI交接/node_reports/Mac_Hongye_Quota_Match_V3_DB3_Query_Report.md
- 匹配成功记录数：2
- 多候选匹配数量：2
- 需要人工复核数量：2
- 每条最多候选数：10
- 本地匹配结果：output/hongye_quota_match_result_v3_db3.json（不提交）
- 本地 V3 匹配草稿：output/宏业标准版报价清单草稿_v3_db3_matched.xlsx（不提交）

## 关键能力
- DB3 路径只从 HONGYE_DB3_PATH 环境变量读取
- 使用 SQLite 只读模式连接
- 每条工程量清单最多查询 10 条候选
- 禁止 SELECT *
- 禁止查询或输出价格字段
- 支持多候选、match_score、match_confidence、match_reasons、needs_manual_review

## 请求 GPT 判断
请 GPT 判断下一步最小闭环。

建议优先级：
1. 建立 DB3 字段映射配置文件，固定 debh/demc/xmmc/dw/fbmc/gcnr 等安全字段。
2. 增强人工复核 Excel：显示前三候选、置信度差距、复核原因。
3. 等唐老板提供标准无价工程量清单后做真实输入验证。
4. 若要接真实 DB3，请由唐老板本机设置 HONGYE_DB3_PATH，不要把路径写入代码或报告。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
