# NEXT_TASK

Round: HY-R040
Task Name: Integrate HY-R039 V4 FIRE_DEFAULT optimizer into main pipeline
Platform: Windows

Task Target:
GPT should confirm whether to connect HY-R039 V4 optimization rules into 13_pipeline and 15_batch_pipeline.

Allowed Actions:
- read_status_files
- update_pipeline_with_desensitized_rules
- generate_node_report
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
