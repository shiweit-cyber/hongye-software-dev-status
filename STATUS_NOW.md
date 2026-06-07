# STATUS_NOW - HY-AUTO

## 时间
2026-06-07 17:45:40

## 运行模式
self-check

## 当前目标路线
HY-R009

## 路线说明
Windows GCFX 样本扫描归类学习 + HY-R008 Excel 导入测试准备

## 本轮结果
- 状态：blocked
- 动作：停止并报告
- 停止原因：HY-R009 缺少 Windows GCFX 样本目录：input/windows_gcfx_samples。
- 是否可进入自主推进模式：no
- 最新参考报告：/Users/tang/Projects/hongye-software-dev/04_AI交接/node_reports/Mac_Template_Field_Analysis_Report.md

## 最高总纲
原始平面图 → 消防 CAD 自动画图 → 自动统计工程量 → 标准工程量清单 → 宏业自动报价 → 定额匹配 → 人工复核 → 最终报价成果。

## 项目方向
宏业自动报价单 / 报价清单生成系统。

## 非目标边界
- 不做 AutoCAD / LISP / DWG / DXF / 图纸测试
- 不改唐老板桌面文件夹摆放

## 下一步建议
补充 Windows GCFX 样本后再继续 HY-R009。

## Git 最新提交
```text
26278ed add_hongye_self_driving_runner
```

## Git 当前状态
```text
 M "04_AI\344\272\244\346\216\245/gpt_bridge/STATUS_NOW.md"
 M 07_scripts/hongye_self_driving_runner.sh
 M 07_scripts/standardize_unpriced_quantity_v1.py
 M README.md
?? "04_AI\344\272\244\346\216\245/node_reports/HY-R005_Bank_Field_Mapping_And_Feedback_Report.md"
?? "04_AI\344\272\244\346\216\245/node_reports/Mac_Auto_Test_Latest_Report.md"
?? "04_AI\344\272\244\346\216\245/node_reports/Mac_Auto_Work_Latest_Report.md"
?? "04_AI\344\272\244\346\216\245/node_reports/Mac_GitHub_First_Push_Report.md"
?? "05_\345\255\227\346\256\265\346\230\240\345\260\204/HY-R005_bank_template_field_mapping.json"
?? "05_\345\255\227\346\256\265\346\230\240\345\260\204/HY-R005_manual_review_feedback_schema.json"
?? "05_\345\255\227\346\256\265\346\230\240\345\260\204/hongye_industry_terms_v2.json"
?? 07_scripts/HY_R005_bank_field_mapping_feedback.py
?? 07_scripts/net_speed_test.py
?? 07_scripts/net_speed_web.py
?? tests/test_HY_R005_bank_field_mapping.py
?? tests/test_HY_R005_manual_review_feedback.py
```
