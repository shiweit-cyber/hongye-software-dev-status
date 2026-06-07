# NEXT_TASK

Round: HY-R041
Task Name: Pending GPT confirmation after HY-R040
Platform: Windows

Task Target:
GPT should decide whether to add V2 entries into the auto control console or continue reducing the remaining FIRE_DEFAULT rows.

Allowed Actions:
- read_status_files
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
