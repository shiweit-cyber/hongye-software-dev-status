# Hongye Git Bridge Status

## 时间
2026-06-07 13:48:47

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 最高总纲
原始平面图 → 消防 CAD 自动画图 → 自动统计工程量 → 标准工程量清单 → 宏业自动报价 → 人工复核 → 最终报价成果。

## 当前宏业定位
后端报价引擎，只负责标准工程量清单到报价成果，不处理 CAD 绘图逻辑。

## 本轮结论
真实 DB3 只读验证流程已继续推进，但未自动选择 DB3。

## 本轮结果
- HONGYE_DB3_PATH 是否已设置：否
- 候选 DB3/SQLite 文件数：4
- 高置信候选数：4
- 是否完成真实 DB3 只读验证：否
- 是否生成真实 DB3 验证报告：是
- 是否生成 real_db3 人工复核文件：否
- 原因：多个高置信候选，避免误选，需要唐老板/GPT 确认。

## 脱敏候选摘要
- a69c6cf1b41b：score 100，字段 debh/demc/dw/fbmc/mc/xmmc
- 28dc481b5fb7：score 100，字段 debh/demc/fbmc/mc
- 2c6ddce842de：score 100，字段 debh/demc/fbmc/mc
- 46cd0b4dddd9：score 87，字段 mc

## 最高总纲偏离检查
- 是否服务于最终生产线：是。
- 是否保持宏业项目定位为后端报价引擎：是。
- 是否混入 CAD 绘图逻辑：否。
- 是否把 CAD 项目说成单纯读图算量：否。
- 是否继续推进标准工程量清单到报价成果链路：是。

## 安全边界
未提交 DB3、真实 DB3 路径、output、原始 XLSX、真实价格数据、token/key/密码；未处理 CAD/LISP/DWG/DXF。
