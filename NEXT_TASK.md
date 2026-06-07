# NEXT_TASK

## 当前建议轮次
HY-R027

## 任务名称
GPT 写 NEXT_TASK 后 Codex 一次性自动执行闭环测试

## 执行模式
safe_whitelist_once

## 本轮说明
HY-R026 已完成批量处理失败隔离与汇总总表。下一轮建议测试 GPT 写入 NEXT_TASK 后，Codex 读取并执行一次低风险白名单任务，执行后立即停止。

## 安全边界
- 不开启无限循环
- 不处理真实客户文件
- 不读取宏业数据库
- 不生成真实报价成果
- 不提交 token/key/password
- 不 force push
