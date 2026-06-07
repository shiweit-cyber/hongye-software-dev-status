# LOOP_LOG_TAIL - HY-R004

## 时间
2026-06-07 15:22:19

## HY-R004 报告摘要

```text
# HY-R004 Bank Template GCFX And Review Loop Report

## 轮次代号
HY-R004

## 最高总纲
原始平面图 → 消防 CAD 自动画图 → 自动统计工程量 → 标准工程量清单 → 宏业自动报价 → 定额匹配 → 人工复核 → 最终报价成果。

## 结论
- 是否找到银行学习范本：是
- Excel 数量：26
- GCFX 数量：6
- GCFX 可识别格式数量：6
- GCFX 可解析结构数量：6
- 银行清单字段结构是否适合学习：是
- 行业词典：已生成 05_字段映射/hongye_industry_terms_v1.json
- A/B/C：{'A': 0, 'B': 2, 'C': 298}
- HY-R004 人工复核 Excel：已生成
- 测试是否通过：是

## 银行 Excel 结构摘要
- e6354752809a | .xlsx | sheets=1 | fields={"quantity": 1}
- b49240acdc98 | .xlsx | sheets=1 | fields={"unit": 1}
- 26489c78e312 | .xlsx | sheets=1 | fields={"quantity": 1}
- e6b97322d748 | .xlsx | sheets=9 | fields={"item_name": 8, "feature": 8, "unit": 8, "quantity": 8, "amount": 8}
- be1386713816 | .xlsx | sheets=24 | fields={"item_name": 11, "amount": 21, "quantity": 11, "feature": 10, "unit": 10}
- ff55acc05ad2 | .xlsx | sheets=1 | fields={"item_name": 1, "feature": 1, "unit": 1, "quantity": 1, "amount": 4}
- a4886d0772f9 | .xls | sheets=0 | fields={}
- d87c00291604 | .xlsx | sheets=1 | fields={"amount": 2}
- 9a5702cf2158 | .xls | sheets=0 | fields={}
- ec18ec1b21b2 | .xls | sheets=0 | fields={}
- 176b51bd1961 | .xls | sheets=0 | fields={}
- 0e9104d27f17 | .xlsx | sheets=24 | fields={"item_name": 11, "amount": 21, "quantity": 11, "feature": 10, "unit": 10}
- 0f69a0bad7a9 | .xlsx | sheets=34 | fields={"unit": 7, "item_name": 10, "amount": 14, "feature": 4, "quantity": 5}
- ae76f9b4532a | .xlsx | sheets=123 | fields={"unit": 7, "item_name": 8, "amount": 14, "feature": 1, "quantity": 2}
- a34ae329a3d7 | .xlsx | sheets=1 | fields={"quantity": 1, "amount": 2}
- b108786ba7d3 | .xlsx | sheets=93 | fields={"item_name": 9, "amount": 12, "unit": 8, "quantity": 5}
- bf1456a0318c | .xlsx | sheets=1 | fields={"unit": 1}
- d71d0deee286 | .xlsx | sheets=19 | fields={"item_name": 6, "amount": 6, "unit": 10, "feature": 4, "quantity": 4}
- 2dabee018cf9 | .xlsx | sheets=123 | fields={"unit": 7, "item_name": 8, "amount": 14, "feature": 1, "quantity": 2}
- 8ca55e920c50 | .xlsx | sheets=2 | fields={"unit": 3, "item_name": 2, "quantity": 1, "amount": 5, "feature": 1}

## GCFX 探测摘要
- 865f585722f4 | head=504b0304140008000800cc3e895c0000 | zip=True | sqlite=False | text=False | extractable=True
- aa7d98e0a670 | head=504b0304140008000800312e9d5c0000 | zip=True | sqlite=False | text=False | extractable=True
- d1749deab467 | head=504b0304140008000800f32a9d5c0000 | zip=True | sqlite=False | text=False | extractable=True
- 47419c8390a8 | head=504b0304140000000800ac4b835a4ab9 | zip=True | sqlite=False | text=False | extractable=True
- a3d1d7033d9b | head=504b0304140008000800433c655a0000 | zip=True | sqlite=False | text=False | extractable=True
- 49671b6612f8 | head=504b0304140008000800740b895c0000 | zip=True | sqlite=False | text=False | extractable=True

## GCFX 建议
- 如果 GCFX 不可直接解析结构，建议用宏业软件导出 Excel/XML/CSV 后再学习。
- 如果 GCFX 可读，本轮也只提取结构，不提取价格数据。

## 安全边界
- 未提交原始 XLS/XLSX/XLSM/GCFX
- 未提交 output XLSX/JSON/CSV
- 未提交 DB3 或真实 DB3 路径
- 未提交真实价格数据或真实报价成果
- 未提交 token/key/密码
- 未处理 CAD/LISP/DWG/DXF
- 未改动唐老板桌面文件夹摆放

## 最高总纲偏离检查
- 未偏离：本轮只加强宏业后端报价引擎的学习范本、行业词典和人工复核闭环。
```
