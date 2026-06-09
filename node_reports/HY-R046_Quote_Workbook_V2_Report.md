# HY-R046 完整报价工作簿 V2 报告

- 当前平台: Windows
- 当前轮次: HY-R046
- 本轮结论: completed
- 报价明细输入: C:\Users\Administrator\Documents\宏业软件\13_pipeline\output_v2\HY-R040_pipeline_v2_quote_result.json
- 人工复核输入: C:\Users\Administrator\Documents\宏业软件\31_review_list_v1\HY-R044_review_items_v1.json
- 费用汇总输入: C:\Users\Administrator\Documents\宏业软件\32_cost_summary_v1\HY-R045_cost_summary_v1.json
- 输出 Excel 路径: C:\Users\Administrator\Documents\宏业软件\33_quote_workbook_v2\HY-R046_quote_workbook_v2.xlsx
- 输出状态 JSON 路径: C:\Users\Administrator\Documents\宏业软件\33_quote_workbook_v2\HY-R046_status.json
- 本地报告路径: C:\Users\Administrator\Documents\宏业软件\33_quote_workbook_v2\HY-R046_quote_workbook_v2_report.md
- 节点报告路径: C:\Users\Administrator\Documents\宏业软件\04_AI交接\node_reports\HY-R046_Quote_Workbook_V2_Report.md
- 工作表列表: 封面, 编制说明, 分部分项清单, 人工复核清单, 费用汇总, 分类汇总, 异常说明
- 分部分项行数: 300
- 人工复核行数: 11
- 分类汇总数量: 14
- 合价总计: 39293506.93
- 价格来源: simulated_for_test
- 自测结果: passed

## 失败原因
无

## 安全边界确认
- 未读取真实客户文件。
- 未读取宏业数据库。
- 未生成真实报价。
- 未自动打开 Excel 或文件夹。
- 未使用 git add .。
