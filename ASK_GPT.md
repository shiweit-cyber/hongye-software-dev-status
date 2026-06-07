# ASK GPT - Hongye Quote Generator

## 时间
2026-06-07 13:48:47

## 最高总纲
原始平面图 → 消防 CAD 自动画图 → 自动统计工程量 → 标准工程量清单 → 宏业自动报价 → 人工复核 → 最终报价成果。

## 当前宏业项目定位
后端报价引擎，只负责标准工程量清单到报价成果，不处理 CAD 绘图逻辑。

## 本轮状态
真实 DB3 只读验证流程已继续推进，但未自动选择 DB3。

## 本轮结果
- 已读取字段映射配置：05_字段映射/hongye_db3_field_mapping_v1.json
- 已读取结构扫描 JSON：05_字段映射/hongye_quota_db_structure_scan_v1.json
- HONGYE_DB3_PATH 是否已设置：否
- 候选 DB3/SQLite 文件数：4
- 高置信候选数：4
- 是否完成真实 DB3 只读验证：否
- 是否生成真实 DB3 验证报告：是
- 是否生成 real_db3 人工复核文件：否
- 原因：多个高置信候选，避免误选，需要唐老板/GPT 确认。

## 脱敏候选摘要
- a69c6cf1b41b：score 100，字段 debh/demc/dw/fbmc/mc/xmmc，表 44，非空表 42
- 28dc481b5fb7：score 100，字段 debh/demc/fbmc/mc，表 11，非空表 11
- 2c6ddce842de：score 100，字段 debh/demc/fbmc/mc，表 11，非空表 11
- 46cd0b4dddd9：score 87，字段 mc，表 17，非空表 17

## 请求 GPT 判断
请 GPT 判断下一步最小闭环。

建议：
1. 优先确认是否选择 a69c6cf1b41b，因为字段最完整。
2. 确认后由 Codex 使用本机 private trace 找到真实路径，写入 ~/.hongye_hongye_db3_env，权限 600。
3. 再运行 V3 查询匹配 + real_db3 人工复核 Excel。
4. 继续禁止提交 DB3、真实路径、output、真实价格数据。

## 最高总纲偏离检查
- 是否服务于最终生产线：是。
- 是否保持宏业项目定位为后端报价引擎：是。
- 是否混入 CAD 绘图逻辑：否。
- 是否把 CAD 项目说成单纯读图算量：否。
- 是否继续推进标准工程量清单到报价成果链路：是。

## 安全边界
- 不提交真实 DB3 路径
- 不提交 DB3
- 不提交 output XLSX/JSON/CSV
- 不提交真实价格数据
- 不提交原始 XLSX
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
