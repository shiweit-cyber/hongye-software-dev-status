# HY-R044 人工复核清单增强 V1 报告

- 当前平台: Windows
- 当前轮次: HY-R044
- 本轮结论: completed
- 输入文件路径: C:\Users\Administrator\Documents\宏业软件\13_pipeline\output_v2\HY-R040_pipeline_v2_quote_result.json
- 输入行数: 300
- 复核条目数量: 11
- FIRE_DEFAULT 数量: 11
- 工程量异常数量: 0
- 价格异常数量: 0
- 输出 Excel 路径: C:\Users\Administrator\Documents\宏业软件\31_review_list_v1\HY-R044_review_items_v1.xlsx
- 输出 JSON 路径: C:\Users\Administrator\Documents\宏业软件\31_review_list_v1\HY-R044_review_items_v1.json
- 输出 CSV 路径: C:\Users\Administrator\Documents\宏业软件\31_review_list_v1\HY-R044_review_items_v1.csv
- 自测脚本路径: C:\Users\Administrator\Documents\宏业软件\31_review_list_v1\test_review_list_generator_v1.py
- 自测结果: passed

## 复核原因分类统计
- 定额匹配置信度偏低；规则未能准确分类，需要人工判断: 11

## 建议分类统计
- NEED_MANUAL_CLASSIFY: 11

## 优先级统计
- 中: 11

## 失败原因
无

## 下一步建议
- HY-R045 费用汇总页 V1。

## 安全边界确认
- 未读取真实客户文件。
- 未读取宏业数据库。
- 未读取原始 GCFX/XLSX/PDF。
- 未生成真实报价成果。
- 未自动打开 Excel、文件夹、资源管理器、reports/output。
