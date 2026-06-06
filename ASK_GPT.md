# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 17:52:08

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
宏业标准版报价清单 V2 准备完成。

## 本轮结果
- 标准化 JSON 记录数：2
- 核心字段缺失记录数：0
- 是否可生成 V2 草稿：是
- 报告：04_AI交接/node_reports/Mac_Hongye_Quote_V2_Prepare_Report.md
- V2 准备脚本：07_scripts/prepare_hongye_quote_v2.py
- 定额数据库扫描计划：05_字段映射/hongye_quota_db_scan_plan_v1.json

## 请求 GPT 判断
请 GPT 给出下一步最小闭环任务。

建议优先级：
1. 设计定额匹配接口 V1，用本地占位定额数据模拟匹配，不读取真实数据库。
2. 唐老板提供标准无价工程量清单后做真实输入验证。
3. 准备宏业定额数据库结构扫描脚本，但默认只输出结构报告，不提交数据库。
4. 继续强化字段映射规则。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
