# Hongye Git Bridge Status

## 时间
2026-06-07 13:19:50

## 当前模式
Git 链接稳定版：前台单轮执行 + GitHub 状态同步 + GPT 判断下一步。

## 本轮结论
DB3 字段映射配置 + 人工复核 Excel V1 已完成。

## 本轮结果
- 字段映射配置：05_字段映射/hongye_db3_field_mapping_v1.json
- 人工复核脚本：07_scripts/generate_hongye_manual_review_v1.py
- V3 输出已增强：best_match、top 3 candidates、confidence_gap、review_required、review_reasons
- 复核行数：2
- 需要人工复核：2
- 每条最多展示候选：3
- 本地复核 JSON：output/hongye_quota_manual_review_v1.json（不提交）
- 本地复核 Excel：output/宏业定额匹配人工复核_v1.xlsx（不提交）

## 安全边界
未提交 DB3、output、原始 XLSX、真实价格数据、token/key/密码；未处理 CAD/LISP/DWG/DXF。
