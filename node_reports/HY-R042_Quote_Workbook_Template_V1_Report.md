# HY-R042 报价工作簿模板 V1 报告

- 状态: completed
- 输入文件: C:\Users\Administrator\Documents\宏业软件\13_pipeline\output_v2\HY-R040_pipeline_v2_quote_result.json
- Excel 工作簿: C:\Users\Administrator\Documents\宏业软件\28_quote_workbook_template\HY-R042_quote_workbook_v1.xlsx
- 本地模板报告: C:\Users\Administrator\Documents\宏业软件\28_quote_workbook_template\HY-R042_quote_workbook_template_report.md
- 状态 JSON: C:\Users\Administrator\Documents\宏业软件\28_quote_workbook_template\HY-R042_status.json
- 生成时间: 2026-06-08T14:12:23

## 验收结果
- 工作表: 封面, 分部分项清单, 人工复核清单, 费用汇总, 说明
- 分部分项清单行数: 300
- 人工复核清单行数: 11
- FIRE_DEFAULT 数量: 11
- 合价总计: 39293506.93
- 价格来源: simulated_for_test

## 自测结果
- 自测脚本: C:\Users\Administrator\Documents\宏业软件\28_quote_workbook_template\test_quote_workbook_template_v1.py
- 自测状态: passed
- Excel 存在: true
- 工作表齐全: true
- 分部分项清单行数: 300
- 人工复核清单行数: 11
- 费用汇总表存在: true
- 未发现自动打开 Excel/文件夹调用: true

## 安全边界
- 未读取真实客户文件。
- 未读取宏业数据库。
- 未读取原始 GCFX/XLSX/PDF。
- 未生成真实报价成果。
- 未自动打开 Excel、文件夹、reports/output。

## 失败原因
无
