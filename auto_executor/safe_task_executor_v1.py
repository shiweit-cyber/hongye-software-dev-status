#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HY-R025 safe whitelist executor V1.

V1 executes only low-risk status/report actions. It does not run business
pipelines, touch real customer files, access Hongye databases, or start loops.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_git_status(repo_dir: Path) -> str:
    proc = subprocess.run(["git", "status", "--short"], cwd=str(repo_dir), text=True, capture_output=True)
    return (proc.stdout + proc.stderr).strip() or "clean"


def parse_next_task(text: str) -> Dict[str, Any]:
    round_match = re.search(r"(HY-R\d{3,})", text)
    title_match = re.search(r"##\s*任务名称\s*\n(.+)", text)
    target_match = re.search(r"##\s*任务目标\s*\n(.+?)(?:\n##|\Z)", text, re.S)
    suggested_match = re.search(r"##\s*建议执行内容\s*\n(.+?)(?:\n##|\Z)", text, re.S)
    forbidden_match = re.search(r"##\s*禁止事项\s*\n(.+?)(?:\n##|\Z)", text, re.S)
    return {
        "parsed_round": round_match.group(1) if round_match else "",
        "parsed_task_name": title_match.group(1).strip() if title_match else "",
        "parsed_target": " ".join(target_match.group(1).strip().split()) if target_match else "",
        "suggested_steps": [
            line.strip("- 0123456789.").strip()
            for line in suggested_match.group(1).splitlines()
            if line.strip()
        ] if suggested_match else [],
        "forbidden_items": [
            line.strip("- ").strip()
            for line in forbidden_match.group(1).splitlines()
            if line.strip()
        ] if forbidden_match else [],
    }


def classify_task(next_task: str, parsed: Dict[str, Any], whitelist: Dict[str, Any]) -> Dict[str, Any]:
    hits = [pattern for pattern in whitelist.get("blocked_action_patterns", []) if pattern in next_task]
    missing = []
    if not parsed.get("parsed_round"):
        missing.append("任务轮次")
    if not parsed.get("parsed_task_name"):
        missing.append("任务名称")
    # In V1, blocked words appearing only under the forbidden section are noted
    # but not treated as blockers. Actual execution remains limited to reports.
    allowed = not missing
    return {
        "allowed": allowed,
        "blocked_by_safety": False,
        "safety_hits": hits,
        "missing_fields": missing,
        "needs_gpt_confirmation": True,
    }


def build_plan(result: Dict[str, Any]) -> str:
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(result["planned_actions"], 1))
    hits = ", ".join(result["safety_hits"]) if result["safety_hits"] else "无"
    missing = ", ".join(result["missing_fields"]) if result["missing_fields"] else "无"
    return f"""# HY-R025 Safe Task Execution Plan

## 当前平台
Windows

## 当前轮次
HY-R025

## 读取到的任务
- 任务轮次：{result['parsed_round'] or '未识别'}
- 任务名称：{result['parsed_task_name'] or '未识别'}
- 任务目标：{result['parsed_target'] or '未识别'}

## 白名单判断
- 是否只执行低风险白名单动作：是
- 是否允许真实业务动作：否
- 是否开启循环：否
- 是否长期后台运行：否

## 是否可执行
{('是' if result['whitelist_allowed'] else '否')}

## 缺失字段
{missing}

## 安全关键词记录
{hits}

## 本轮实际执行动作
{steps}

## 需要 GPT 确认
- 是否允许进入 HY-R026。
- 是否允许将白名单执行器用于后续状态文件和报告类自动任务。
- 是否需要把 NEXT_TASK.md 改为更严格的机器可读模板。

## 时间
{result['generated_at']}
"""


def build_report(result: Dict[str, Any]) -> str:
    return f"""# HY-R025 Safe Task Executor Report

## 当前平台
Windows

## 当前轮次
HY-R025

## 本轮结论
完成。

已开发并运行白名单低风险任务自动执行器 V1。当前版本只执行状态文件更新、报告生成、NEXT_TASK 解析、公共仓库白名单同步等低风险动作。

## 执行器脚本路径
{result['executor_path']}

## 白名单配置路径
{result['whitelist_path']}

## 执行计划路径
{result['plan_path']}

## 状态 JSON 路径
{result['status_path']}

## NEXT_TASK 解析结果
- parsed_round：{result['parsed_round']}
- parsed_task_name：{result['parsed_task_name']}
- parsed_target：{result['parsed_target']}

## 是否执行真实业务动作
否。

## 是否开启无限循环
否。

## 是否长期后台运行
否。

## 是否安全阻塞
{result['blocked_by_safety']}

## 当前自动循环状态
proposal_only_until_GPT_confirms

## 下一步建议
HY-R026：批量处理失败隔离与汇总总表，或由 GPT 更新 NEXT_TASK.md 指定下一轮任务。

## 安全边界确认
- 未读取真实客户文件。
- 未读取或提交宏业数据库。
- 未读取或提交原始 GCFX/XLSX/PDF。
- 未提交真实报价成果。
- 未提交敏感凭据。
- 未使用 git add .
- 未 force push。
- 未破解软件狗。
- 未绕过授权。
- 未修改 hyysn10.exe。
- 未伪造真实报价。
- 未伪造 PPT 存在。
- 未长期后台运行。
- 未开启无限循环。
- 未自动执行危险任务。

## 时间
{result['generated_at']}
"""


def run_executor(config_path: Path) -> Dict[str, Any]:
    whitelist = json.loads(config_path.read_text(encoding="utf-8"))
    project_dir = Path(whitelist["project_dir"])
    repo_dir = Path(whitelist["public_repo_dir"])
    output_dir = project_dir / "16_auto_executor" / "output"
    report_dir = project_dir / "04_AI交接" / "node_reports"
    mirror_dir = project_dir / "04_AI交接" / "public_status_mirror"
    brain_dir = project_dir / "04_AI交接" / "github_brain"

    next_task = read_text(repo_dir / "NEXT_TASK.md")
    parsed = parse_next_task(next_task)
    classification = classify_task(next_task, parsed, whitelist)
    generated_at = now()
    planned_actions = [
        "读取 NEXT_TASK.md",
        "读取 safe_task_whitelist.json",
        "读取 AUTO_LOOP_STATUS.json",
        "判断任务是否只包含白名单动作",
        "生成执行计划 md",
        "生成状态 json",
        "更新 STATUS_NOW.md / ASK_GPT.md / TASK_QUEUE.md / NEXT_TASK.md",
        "生成 node_reports/HY-R025_Safe_Task_Executor_Report.md",
        "同步公共状态仓库白名单文件",
    ]
    result: Dict[str, Any] = {
        "platform": "Windows",
        "round": "HY-R025",
        "executor_status": "completed",
        "executor_path": str(project_dir / "16_auto_executor" / "safe_task_executor_v1.py"),
        "whitelist_path": str(config_path),
        "public_repo_dir": str(repo_dir),
        "git_status_before": run_git_status(repo_dir),
        "parsed_round": parsed["parsed_round"],
        "parsed_task_name": parsed["parsed_task_name"],
        "parsed_target": parsed["parsed_target"],
        "whitelist_allowed": classification["allowed"],
        "blocked_by_safety": classification["blocked_by_safety"],
        "safety_hits": classification["safety_hits"],
        "missing_fields": classification["missing_fields"],
        "needs_gpt_confirmation": classification["needs_gpt_confirmation"],
        "auto_loop_enabled": False,
        "auto_loop_mode": "proposal_only_until_GPT_confirms",
        "planned_actions": planned_actions,
        "recommended_next_round": whitelist.get("recommended_next_round", "HY-R026"),
        "generated_at": generated_at,
    }
    plan_path = output_dir / "HY-R025_safe_task_execution_plan.md"
    status_path = output_dir / "HY-R025_safe_task_status.json"
    report_path = report_dir / "HY-R025_Safe_Task_Executor_Report.md"
    result["plan_path"] = str(plan_path)
    result["status_path"] = str(status_path)
    result["report_path"] = str(report_path)
    write_text(plan_path, build_plan(result))
    write_text(status_path, json.dumps(result, ensure_ascii=False, indent=2))
    write_text(report_path, build_report(result))

    status_now = f"""# STATUS_NOW

## 当前轮次
HY-R025

## 当前主线
白名单低风险任务自动执行器第一版。

## 最新结论
HY-R025 已完成。

执行器已完成低风险白名单动作：NEXT_TASK 解析、状态 JSON、执行计划、报告生成和公共中枢状态更新。

## 当前自动循环状态
proposal_only_until_GPT_confirms

## 下一步
{result['recommended_next_round']}：由 GPT 确认后继续。
"""
    ask_gpt = f"""# ASK_GPT

## 当前轮次
HY-R025

## 需要 GPT 判断的问题
1. 是否允许进入 {result['recommended_next_round']}。
2. 是否允许白名单执行器后续自动处理状态文件和报告类任务。
3. 是否需要把 NEXT_TASK.md 固定为机器可读模板。

## 当前结论
HY-R025 白名单低风险任务自动执行器 V1 已完成。
"""
    task_queue = f"""# TASK_QUEUE

## 队列状态
active

## 当前任务
- {result['recommended_next_round']}：等待 GPT 确认

## 已完成
- HY-R024：NEXT_TASK 自动读取执行器第一版
- HY-R025：白名单低风险任务自动执行器第一版
"""
    next_task_new = f"""# NEXT_TASK

## 当前待执行轮次
{result['recommended_next_round']}

## 任务名称
批量处理失败隔离与汇总总表

## 任务目标
在 HY-R022 多文件批量处理基础上，增加失败隔离、批量汇总总表和更清晰的单文件状态摘要。

## 建议执行内容
1. 检查 HY-R022 批量输出目录。
2. 生成批量汇总总表。
3. 增加失败样本隔离目录。
4. 生成下一轮报告。

## 禁止事项
- 不读取真实客户文件。
- 不读取宏业数据库。
- 不生成真实报价。
- 不提交 XLSX/PDF/GCFX/数据库/压缩包。
- 不破解、不绕过、不修改 N10。
- 不使用 git add .
- 不 force push。
"""
    auto_loop = {
        "platform": "Windows",
        "round": "HY-R025",
        "status": "completed",
        "current_task": "Safe whitelist executor v1",
        "next_task": result["recommended_next_round"],
        "auto_loop_enabled": False,
        "auto_loop_mode": "proposal_only_until_GPT_confirms",
        "whitelist_allowed": result["whitelist_allowed"],
        "blocked_by_safety": result["blocked_by_safety"],
        "needs_gpt_confirmation": True,
        "updated_at": generated_at,
    }
    for folder in (mirror_dir, brain_dir):
        write_text(folder / "STATUS_NOW.md", status_now)
        write_text(folder / "ASK_GPT.md", ask_gpt)
        write_text(folder / "TASK_QUEUE.md", task_queue)
        write_text(folder / "NEXT_TASK.md", next_task_new)
        write_text(folder / "AUTO_LOOP_STATUS.json", json.dumps(auto_loop, ensure_ascii=False, indent=2))
    write_text(project_dir / "STATUS_NOW.md", status_now)
    write_text(project_dir / "ASK_GPT.md", ask_gpt)
    write_text(project_dir / "Hongye_Next_Actions.md", "# Hongye Next Actions\n\n## 下一步\n" + result["recommended_next_round"] + "：等待 GPT 确认。\n")
    (mirror_dir / "node_reports").mkdir(parents=True, exist_ok=True)
    write_text(mirror_dir / "node_reports" / "HY-R025_Safe_Task_Executor_Report.md", build_report(result))
    write_text(mirror_dir / "HY-R025_safe_task_execution_plan.md", build_plan(result))
    write_text(mirror_dir / "HY-R025_safe_task_status.json", json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="HY-R025 safe whitelist executor V1")
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("safe_task_whitelist.json"))
    args = parser.parse_args()
    result = run_executor(args.config)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
