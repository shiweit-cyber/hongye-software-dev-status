# HY-R046 confirmed quality control V2 run Report

- Platform: Windows
- Round: HY-R046
- Status: done
- Menu task: run_batch_quality_control_v2
- Request cleared: True
- Commit hash: 
- Push success: False

## Metrics
- Single rows: 300
- Single FIRE_DEFAULT: 11
- Single review: 11
- Batch rows: 900
- Batch FIRE_DEFAULT: 33
- Batch review: 33
- QC success files: 3
- QC failed files: 0

## Raw Result
```json
{
  "console_result": {
    "cmd": [
      "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
      "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
      "--run-confirmed"
    ],
    "code": 0,
    "stdout": "{\n  \"platform\": \"Windows\",\n  \"status\": \"completed\",\n  \"request_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\21_auto_control_console\\\\confirmed_task_request.json\",\n  \"request_cleared\": true,\n  \"auto_loop_enabled\": false,\n  \"infinite_loop\": false,\n  \"started_at\": \"2026-06-08 00:08:33\",\n  \"request\": {\n    \"confirmed\": true,\n    \"task_id\": \"run_batch_quality_control_v2\",\n    \"task_name\": \"run_batch_quality_control_v2\",\n    \"requested_by\": \"HY-AUTOQUEUE-01\",\n    \"created_at\": \"2026-06-08 00:08:33\"\n  },\n  \"task_name\": \"run_batch_quality_control_v2\",\n  \"blocked_by_safety\": false,\n  \"risk\": \"safe_simulated_run\",\n  \"entrypoint\": \"17_batch_quality_control/run_quality_control_v2.ps1\",\n  \"requires_gpt_confirmation\": true,\n  \"execution\": {\n    \"returncode\": 0,\n    \"stdout\": \"{\\n  \\\"platform\\\": \\\"Windows\\\",\\n  \\\"round\\\": \\\"HY-R040\\\",\\n  \\\"status\\\": \\\"completed\\\",\\n  \\\"success_files\\\": 3,\\n  \\\"failed_files\\\": 0,\\n  \\\"total_rows\\\": 900,\\n  \\\"total_fire_default\\\": 33,\\n  \\\"total_review_count\\\": 33,\\n  \\\"rows\\\": [\\n    {\\n      \\\"sample\\\": \\\"HY-R022_batch_sample_001\\\",\\n      \\\"input_file\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\input\\\\\\\\HY-R022_batch_sample_001.xlsx\\\",\\n      \\\"output_dir\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\output_v2\\\\\\\\HY-R022_batch_sample_001\\\",\\n      \\\"success\\\": true,\\n      \\\"rows\\\": 300,\\n      \\\"fire_default\\\": 11,\\n      \\\"review_count\\\": 11,\\n      \\\"failed_reason\\\": \\\"\\\"\\n    },\\n    {\\n      \\\"sample\\\": \\\"HY-R022_batch_sample_002\\\",\\n      \\\"input_file\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\input\\\\\\\\HY-R022_batch_sample_002.xlsx\\\",\\n      \\\"output_dir\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\output_v2\\\\\\\\HY-R022_batch_sample_002\\\",\\n      \\\"success\\\": true,\\n      \\\"rows\\\": 300,\\n      \\\"fire_default\\\": 11,\\n      \\\"review_count\\\": 11,\\n      \\\"failed_reason\\\": \\\"\\\"\\n    },\\n    {\\n      \\\"sample\\\": \\\"HY-R022_batch_sample_003\\\",\\n      \\\"input_file\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\input\\\\\\\\HY-R022_batch_sample_003.xlsx\\\",\\n      \\\"output_dir\\\": \\\"C:\\\\\\\\Users\\\\\\\\Administrator\\\\\\\\Documents\\\\\\\\��ҵ����\\\\\\\\15_batch_pipeline\\\\\\\\output_v2\\\\\\\\HY-R022_batch_sample_003\\\",\\n      \\\"success\\\": true,\\n      \\\"rows\\\": 300,\\n      \\\"fire_default\\\": 11,\\n      \\\"review_count\\\": 11,\\n      \\\"failed_reason\\\": \\\"\\\"\\n    }\\n  ],\\n  \\\"security\\\": {\\n    \\\"real_customer_files_read\\\": false,\\n    \\\"hongye_database_read\\\": false,\\n    \\\"real_quote_generated\\\": false\\n  },\\n  \\\"generated_at\\\": \\\"2026-06-08 00:08:33\\\"\\n}\\n\",\n    \"stderr\": \"\"\n  },\n  \"metrics\": {\n    \"files_found\": {\n      \"single\": true,\n      \"batch\": true,\n      \"quality\": true\n    },\n    \"single_rows\": 300,\n    \"single_fire_default\": 11,\n    \"single_review\": 11,\n    \"batch_rows\": 900,\n    \"batch_fire_default\": 33,\n    \"batch_review\": 33,\n    \"quality_success_files\": 3,\n    \"quality_failed_files\": 0,\n    \"checks\": {\n      \"single_rows\": true,\n      \"single_fire_default\": true,\n      \"single_review\": true,\n      \"batch_rows\": true,\n      \"batch_fire_default\": true,\n      \"batch_review\": true,\n      \"quality_success_files\": true,\n      \"quality_failed_files\": true\n    },\n    \"passed\": true\n  },\n  \"finished_at\": \"2026-06-08 00:08:34\"\n}\n",
    "stderr": "",
    "json": {
      "platform": "Windows",
      "status": "completed",
      "request_file": "C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\confirmed_task_request.json",
      "request_cleared": true,
      "auto_loop_enabled": false,
      "infinite_loop": false,
      "started_at": "2026-06-08 00:08:33",
      "request": {
        "confirmed": true,
        "task_id": "run_batch_quality_control_v2",
        "task_name": "run_batch_quality_control_v2",
        "requested_by": "HY-AUTOQUEUE-01",
        "created_at": "2026-06-08 00:08:33"
      },
      "task_name": "run_batch_quality_control_v2",
      "blocked_by_safety": false,
      "risk": "safe_simulated_run",
      "entrypoint": "17_batch_quality_control/run_quality_control_v2.ps1",
      "requires_gpt_confirmation": true,
      "execution": {
        "returncode": 0,
        "stdout": "{\n  \"platform\": \"Windows\",\n  \"round\": \"HY-R040\",\n  \"status\": \"completed\",\n  \"success_files\": 3,\n  \"failed_files\": 0,\n  \"total_rows\": 900,\n  \"total_fire_default\": 33,\n  \"total_review_count\": 33,\n  \"rows\": [\n    {\n      \"sample\": \"HY-R022_batch_sample_001\",\n      \"input_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\input\\\\HY-R022_batch_sample_001.xlsx\",\n      \"output_dir\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\output_v2\\\\HY-R022_batch_sample_001\",\n      \"success\": true,\n      \"rows\": 300,\n      \"fire_default\": 11,\n      \"review_count\": 11,\n      \"failed_reason\": \"\"\n    },\n    {\n      \"sample\": \"HY-R022_batch_sample_002\",\n      \"input_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\input\\\\HY-R022_batch_sample_002.xlsx\",\n      \"output_dir\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\output_v2\\\\HY-R022_batch_sample_002\",\n      \"success\": true,\n      \"rows\": 300,\n      \"fire_default\": 11,\n      \"review_count\": 11,\n      \"failed_reason\": \"\"\n    },\n    {\n      \"sample\": \"HY-R022_batch_sample_003\",\n      \"input_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\input\\\\HY-R022_batch_sample_003.xlsx\",\n      \"output_dir\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\15_batch_pipeline\\\\output_v2\\\\HY-R022_batch_sample_003\",\n      \"success\": true,\n      \"rows\": 300,\n      \"fire_default\": 11,\n      \"review_count\": 11,\n      \"failed_reason\": \"\"\n    }\n  ],\n  \"security\": {\n    \"real_customer_files_read\": false,\n    \"hongye_database_read\": false,\n    \"real_quote_generated\": false\n  },\n  \"generated_at\": \"2026-06-08 00:08:33\"\n}\n",
        "stderr": ""
      },
      "metrics": {
        "files_found": {
          "single": true,
          "batch": true,
          "quality": true
        },
        "single_rows": 300,
        "single_fire_default": 11,
        "single_review": 11,
        "batch_rows": 900,
        "batch_fire_default": 33,
        "batch_review": 33,
        "quality_success_files": 3,
        "quality_failed_files": 0,
        "checks": {
          "single_rows": true,
          "single_fire_default": true,
          "single_review": true,
          "batch_rows": true,
          "batch_fire_default": true,
          "batch_review": true,
          "quality_success_files": true,
          "quality_failed_files": true
        },
        "passed": true
      },
      "finished_at": "2026-06-08 00:08:34"
    }
  },
  "metrics": {
    "files_found": {
      "single": true,
      "batch": true,
      "quality": true
    },
    "single_rows": 300,
    "single_fire_default": 11,
    "single_review": 11,
    "batch_rows": 900,
    "batch_fire_default": 33,
    "batch_review": 33,
    "quality_success_files": 3,
    "quality_failed_files": 0,
    "checks": {
      "single_rows": true,
      "single_fire_default": true,
      "single_review": true,
      "batch_rows": true,
      "batch_fire_default": true,
      "batch_review": true,
      "quality_success_files": true,
      "quality_failed_files": true
    },
    "passed": true
  },
  "passed": true
}
```

## Safety
- No real customer files were read.
- No Hongye database was read.
- No real quote result was generated.
- No infinite loop was started.
- git add . was not used.
- force push was not used.