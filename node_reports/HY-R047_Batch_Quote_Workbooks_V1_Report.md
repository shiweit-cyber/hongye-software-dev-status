# HY-R047 批量报价工作簿生成 V1 报告

- 当前平台: Windows
- 当前轮次: HY-R047
- 本轮结论: completed
- 输入目录: C:\Users\Administrator\Documents\宏业软件\15_batch_pipeline\input
- 批量索引表路径: C:\Users\Administrator\Documents\宏业软件\34_batch_quote_workbooks_v1\HY-R047_batch_quote_index.xlsx
- 输出工作簿目录: C:\Users\Administrator\Documents\宏业软件\34_batch_quote_workbooks_v1\workbooks
- 识别样本数量: 3
- 成功工作簿数量: 3
- 失败样本数量: 0
- 自测结果: passed

## 样本结果
- 样本文件名: HY-R022_batch_sample_001.xlsx
  - 状态: completed
  - 输入路径: C:\Users\Administrator\Documents\宏业软件\15_batch_pipeline\input\HY-R022_batch_sample_001.xlsx
  - 输出工作簿路径: C:\Users\Administrator\Documents\宏业软件\34_batch_quote_workbooks_v1\workbooks\HY-R047_HY-R022_batch_sample_001_quote_workbook_v1.xlsx
  - 分部分项行数: 300
  - 人工复核行数: 11
  - FIRE_DEFAULT 数量: 11
  - 合价总计: 39293506.93
  - 失败原因: 无
- 样本文件名: HY-R022_batch_sample_002.xlsx
  - 状态: completed
  - 输入路径: C:\Users\Administrator\Documents\宏业软件\15_batch_pipeline\input\HY-R022_batch_sample_002.xlsx
  - 输出工作簿路径: C:\Users\Administrator\Documents\宏业软件\34_batch_quote_workbooks_v1\workbooks\HY-R047_HY-R022_batch_sample_002_quote_workbook_v1.xlsx
  - 分部分项行数: 300
  - 人工复核行数: 11
  - FIRE_DEFAULT 数量: 11
  - 合价总计: 39293506.93
  - 失败原因: 无
- 样本文件名: HY-R022_batch_sample_003.xlsx
  - 状态: completed
  - 输入路径: C:\Users\Administrator\Documents\宏业软件\15_batch_pipeline\input\HY-R022_batch_sample_003.xlsx
  - 输出工作簿路径: C:\Users\Administrator\Documents\宏业软件\34_batch_quote_workbooks_v1\workbooks\HY-R047_HY-R022_batch_sample_003_quote_workbook_v1.xlsx
  - 分部分项行数: 300
  - 人工复核行数: 11
  - FIRE_DEFAULT 数量: 11
  - 合价总计: 39293506.93
  - 失败原因: 无

## 失败原因
无

## 安全边界确认
- 只扫描项目目录内 15_batch_pipeline/input。
- 未读取 Desktop / Downloads 文件。
- 未读取真实客户文件。
- 未读取宏业数据库。
- 未生成真实报价成果。
- 未自动打开 Excel 或文件夹。
- 未使用 git add .。
