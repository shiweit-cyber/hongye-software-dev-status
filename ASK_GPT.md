# ASK GPT - Hongye Quote Generator

## 时间
2026-06-07 13:25:23

## 当前模式
Git 链接稳定版，不使用 OpenAI API。

## 本轮状态
真实 DB3 只读小范围验证 V1 已完成扫描，但未自动选择 DB3。

## 本轮结果
- 候选 DB3/SQLite 文件数：4
- 高置信候选数：4
- 是否自动设置 HONGYE_DB3_PATH：否
- 是否完成真实 DB3 只读查询验证：否
- 是否生成 real_db3 人工复核文件：否
- 原因：多个高置信候选，避免误选，需要唐老板/GPT 确认候选。

## 脱敏候选摘要
- a69c6cf1b41b：score 100，字段 debh/demc/dw/fbmc/mc/xmmc，表 44，非空表 42
- 28dc481b5fb7：score 100，字段 debh/demc/fbmc/mc，表 11，非空表 11
- 2c6ddce842de：score 100，字段 debh/demc/fbmc/mc，表 11，非空表 11
- 46cd0b4dddd9：score 87，字段 mc，表 17，非空表 17

## 请求 GPT 判断
请 GPT 判断下一步最小闭环。

建议：
1. 优先让唐老板确认选择哪个脱敏候选。
2. 如果按字段完整度判断，a69c6cf1b41b 字段最完整。
3. 确认后由本机私有 trace 找到真实路径，写入 ~/.hongye_hongye_db3_env，权限 600。
4. 再运行 V3 查询匹配 + real_db3 人工复核 Excel。

## 安全边界
- 不提交真实 DB3 路径
- 不提交 DB3
- 不提交 output XLSX/JSON/CSV
- 不提交真实价格数据
- 不提交原始 XLSX
- 不提交 token/key/密码
- 不做 CAD/LISP/DWG/DXF
