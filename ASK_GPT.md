# ASK GPT - Hongye Quote Generator

## 时间
2026-06-06 18:25:58

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
真实宏业定额数据库结构扫描 V1 已完成。

## 本轮结果
- 候选文件数：21
- 数据类型：Excel 16、旧版 Excel 1、SQLite/DB3 4
- 结构报告：04_AI交接/node_reports/Mac_Hongye_Quota_DB_Structure_Scan_Report.md
- 脱敏结构 JSON：05_字段映射/hongye_quota_db_structure_scan_v1.json
- 本轮只读取结构：表名、字段名、字段类型、行数统计
- 未导出真实价格数据
- 未提交数据库文件

## 关键发现
SQLite/DB3 中发现可用于真实定额匹配的字段：
- 定额编号类：debh
- 定额名称类：demc / xmmc
- 单位类：dw
- 人工类：rgf
- 材料类：clf
- 机械类：jxf
- 章节/分部类：fbmc / mc

## 请求 GPT 判断
请 GPT 判断下一步是否进入“真实定额匹配接口 V2”。

建议下一轮最小闭环：
1. 只基于结构 JSON 建立字段映射配置。
2. 读取 DB3 时只做匹配查询，不批量导出价格库。
3. 生成多候选匹配结果，带置信度和人工复核标记。
4. 输出本地 `output/` 测试文件，但不提交。

## 安全边界
- 不提交原始 XLSX
- 不提交 output XLSX/JSON/CSV
- 不提交宏业数据库
- 不提交真实报价成果
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
