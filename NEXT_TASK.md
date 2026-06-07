# NEXT_TASK

Round: HY-R038
Subtask: HY-R038-01
Task Name: Single desensitized pipeline rerun
Platform: Windows

Task Target:
Run one low-risk desensitized business module inside the project directory only.

Allowed Actions:
- read_next_task
- parse_next_task
- run_safe_task_executor
- run_pipeline_with_desensitized_sample
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
- process_downloads_or_desktop_non_project_files

Safety Notes:
- Use only existing desensitized samples inside C:/Users/Administrator/Documents/宏业软件.
- Do not read real customer files.
- Do not read Hongye database.
- Do not generate real quote results.
- Do not use git add .
- Do not force push.
- Do not start an infinite loop.
- Do not run as a long background process.
