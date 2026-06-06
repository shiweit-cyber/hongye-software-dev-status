# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 19:05:51

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
真实定额匹配接口 V2 雏形已完成。

## 本轮结果
- 匹配成功记录数：2
- 多候选匹配数量：2
- 需要人工复核数量：2
- 匹配报告：04_AI交接/node_reports/Mac_Hongye_Quota_Match_V2_Report.md
- 匹配脚本：07_scripts/match_hongye_quota_v2.py
- 本地匹配结果：output/hongye_quota_match_result_v2.json（不提交）
- 本地 V2 匹配草稿：output/宏业标准版报价清单草稿_v2_matched.xlsx（不提交）

## 关键能力
- 支持多候选匹配
- 输出 match_score / match_confidence / match_reasons
- 标记 needs_manual_review
- 使用结构 JSON 中的字段提示：debh / demc / xmmc / dw / rgf / clf / jxf
- 本轮仍使用占位定额数据，不读取真实价格

## 请求 GPT 判断
请 GPT 判断下一步最小闭环。

建议优先级：
1. 是否允许进入“真实 DB3 查询型匹配 V3”：只按关键词查询少量候选，不批量导出价格库。
2. 建立字段映射配置文件，把 debh/demc/xmmc/dw/rgf/clf/jxf 映射到内部字段。
3. 增强人工复核表：显示前三候选、置信度差距、复核原因。
4. 等唐老板提供标准无价工程量清单后做真实输入验证。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
