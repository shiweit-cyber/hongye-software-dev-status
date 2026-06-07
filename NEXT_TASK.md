# NEXT_TASK

Round: HY-R036-03
Task Name: Desensitized pipeline artifact continuity check
Platform: Windows

Task Target:
Check desensitized pipeline, batch, quality-control outputs and HY-R035 archive exist.

Allowed Actions:
- read_next_task
- parse_next_task
- run_safe_task_executor
- check_file_exists
- generate_node_report
- generate_status_json
- update_status_now
- update_ask_gpt
- update_auto_loop_status
- git_status
- git_commit_whitelisted_files
- git_push

Forbidden Actions:
- read_real_customer_file
- read_hongye_database
- submit_real_quote_result
- crack_dongle
- bypass_authorization
- modify_hyysn10
- infinite_loop
- long_background_run
- git_add_dot
- force_push
- dangerous_task

Safety Notes:
- Do not read real customer files.
- Do not read Hongye database.
- Do not submit real quote results.
- Do not crack or bypass dongle authorization.
- Do not modify hyysn10.exe.
- Do not start an infinite loop.
- Do not run as a long background process.
- Do not use git add .
- Do not force push.

Generated At: 2026-06-07 22:44:33
