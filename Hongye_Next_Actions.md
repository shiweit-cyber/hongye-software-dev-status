# Hongye Next Actions

## 最高总纲
原始平面图 → 消防 CAD 自动画图 → 自动统计工程量 → 标准工程量清单 → 宏业自动报价 → 人工复核 → 最终报价成果。

## 当前建议
1. 开发标准 BOQ v1 CSV 校验器。
2. 校验表头严格匹配 v1。
3. 校验 quantity、unit、item_name、system_type。
4. 输出人工复核优先级清单。
5. 暂不连接真实宏业数据库。
6. DB3 真实路径选择继续等待 GPT/唐老板确认，不自动选择。

## 当前限制
HONGYE_DB3_PATH 未设置；目前有 4 个高置信候选，未自动选择。

## 安全要求
不提交真实 DB3 路径、DB3、output、真实价格数据、原始 XLSX、token/key/密码；不处理 CAD/LISP/DWG/DXF。
