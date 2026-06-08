# HY-R043 任意 Excel 表头识别增强 V1 报告

- 当前平台: Windows
- 当前轮次: HY-R043
- 本轮结论: completed
- 输入文件路径: C:\Users\Administrator\Documents\宏业软件\28_quote_workbook_template\HY-R042_quote_workbook_v1.xlsx
- 是否使用备用输入: false
- 标准表头测试 Excel: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\sample_standard_headers.xlsx
- 别名表头测试 Excel: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\sample_alias_headers.xlsx
- 乱序表头测试 Excel: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\sample_shuffled_headers.xlsx
- 表头别名配置路径: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\header_alias_rules.json
- 表头识别脚本路径: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\header_recognizer_v1.py
- 自测脚本路径: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\test_header_recognizer_v1.py
- 识别结果 JSON 路径: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\HY-R043_header_recognition_result.json
- 识别结果 CSV 路径: C:\Users\Administrator\Documents\宏业软件\30_header_recognition_v1\HY-R043_header_recognition_result.csv
- 字段识别成功率: 1.0
- 自测结果: passed

## 每份测试 Excel 识别字段
- sample_standard_headers.xlsx: 项目编码, 清单名称, 项目特征, 单位, 工程量, 定额编码, 定额名称, 备注 (8/8)
- sample_alias_headers.xlsx: 项目编码, 清单名称, 项目特征, 单位, 工程量, 定额编码, 定额名称, 备注 (8/8)
- sample_shuffled_headers.xlsx: 工程量, 备注, 清单名称, 定额编码, 单位, 项目特征, 定额名称, 项目编码 (8/8)

## 自测结果
- 输入文件存在: true
- 三份测试 Excel 存在: true
- 识别计数: sample_standard_headers.xlsx=8, sample_alias_headers.xlsx=8, sample_shuffled_headers.xlsx=8
- 错误信息: 无

## 失败原因
无

## 下一步建议
- HY-R044 人工复核清单增强 V1。

## 安全边界确认
- 未读取真实客户文件。
- 未读取宏业数据库。
- 未读取原始 GCFX/XLSX/PDF。
- 未生成真实报价成果。
- 未自动打开 Excel、文件夹、资源管理器、reports/output。
