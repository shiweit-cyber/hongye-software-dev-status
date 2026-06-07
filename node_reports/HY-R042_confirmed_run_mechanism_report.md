# HY-R042 confirmed single run mechanism Report

- Platform: Windows
- Round: HY-R042
- Status: done
- Menu task: check_v2_metrics
- Request cleared: True
- Commit hash: 
- Push success: False

## Metrics
- Single rows: 
- Single FIRE_DEFAULT: 
- Single review: 
- Batch rows: 
- Batch FIRE_DEFAULT: 
- Batch review: 
- QC success files: 
- QC failed files: 

## Raw Result
```json
{
  "tests": {
    "unconfirmed_refused": {
      "cmd": [
        "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
        "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
        "--run-confirmed"
      ],
      "code": 0,
      "stdout": "{\n  \"platform\": \"Windows\",\n  \"status\": \"rejected_unconfirmed\",\n  \"request_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\21_auto_control_console\\\\confirmed_task_request.json\",\n  \"request_cleared\": true,\n  \"auto_loop_enabled\": false,\n  \"infinite_loop\": false,\n  \"started_at\": \"2026-06-08 00:07:37\",\n  \"request\": {\n    \"confirmed\": false,\n    \"task_id\": \"check_v2_metrics\",\n    \"task_name\": \"check_v2_metrics\",\n    \"requested_by\": \"HY-AUTOQUEUE-01\",\n    \"created_at\": \"2026-06-08 00:07:37\"\n  },\n  \"blocked_by_safety\": false,\n  \"task_name\": \"check_v2_metrics\",\n  \"finished_at\": \"2026-06-08 00:07:37\"\n}\n",
      "stderr": "",
      "json": {
        "platform": "Windows",
        "status": "rejected_unconfirmed",
        "request_file": "C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\confirmed_task_request.json",
        "request_cleared": true,
        "auto_loop_enabled": false,
        "infinite_loop": false,
        "started_at": "2026-06-08 00:07:37",
        "request": {
          "confirmed": false,
          "task_id": "check_v2_metrics",
          "task_name": "check_v2_metrics",
          "requested_by": "HY-AUTOQUEUE-01",
          "created_at": "2026-06-08 00:07:37"
        },
        "blocked_by_safety": false,
        "task_name": "check_v2_metrics",
        "finished_at": "2026-06-08 00:07:37"
      }
    },
    "real_file_blocked": {
      "cmd": [
        "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
        "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
        "--run-confirmed"
      ],
      "code": 0,
      "stdout": "{\n  \"platform\": \"Windows\",\n  \"status\": \"blocked_by_safety\",\n  \"request_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\21_auto_control_console\\\\confirmed_task_request.json\",\n  \"request_cleared\": true,\n  \"auto_loop_enabled\": false,\n  \"infinite_loop\": false,\n  \"started_at\": \"2026-06-08 00:07:38\",\n  \"request\": {\n    \"confirmed\": true,\n    \"task_id\": \"run_real_customer_file\",\n    \"task_name\": \"run_real_customer_file\",\n    \"requested_by\": \"HY-AUTOQUEUE-01\",\n    \"created_at\": \"2026-06-08 00:07:37\"\n  },\n  \"blocked_by_safety\": true,\n  \"task_name\": \"run_real_customer_file\",\n  \"finished_at\": \"2026-06-08 00:07:38\"\n}\n",
      "stderr": "",
      "json": {
        "platform": "Windows",
        "status": "blocked_by_safety",
        "request_file": "C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\confirmed_task_request.json",
        "request_cleared": true,
        "auto_loop_enabled": false,
        "infinite_loop": false,
        "started_at": "2026-06-08 00:07:38",
        "request": {
          "confirmed": true,
          "task_id": "run_real_customer_file",
          "task_name": "run_real_customer_file",
          "requested_by": "HY-AUTOQUEUE-01",
          "created_at": "2026-06-08 00:07:37"
        },
        "blocked_by_safety": true,
        "task_name": "run_real_customer_file",
        "finished_at": "2026-06-08 00:07:38"
      }
    },
    "safe_read_only_executed": {
      "cmd": [
        "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
        "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
        "--run-confirmed"
      ],
      "code": 0,
      "stdout": "{\n  \"platform\": \"Windows\",\n  \"status\": \"completed\",\n  \"request_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\21_auto_control_console\\\\confirmed_task_request.json\",\n  \"request_cleared\": true,\n  \"auto_loop_enabled\": false,\n  \"infinite_loop\": false,\n  \"started_at\": \"2026-06-08 00:07:38\",\n  \"request\": {\n    \"confirmed\": true,\n    \"task_id\": \"check_v2_metrics\",\n    \"task_name\": \"check_v2_metrics\",\n    \"requested_by\": \"HY-AUTOQUEUE-01\",\n    \"created_at\": \"2026-06-08 00:07:38\"\n  },\n  \"task_name\": \"check_v2_metrics\",\n  \"blocked_by_safety\": false,\n  \"risk\": \"safe_read_only\",\n  \"entrypoint\": \"\",\n  \"requires_gpt_confirmation\": false,\n  \"metrics\": {\n    \"files_found\": {\n      \"single\": true,\n      \"batch\": true,\n      \"quality\": true\n    },\n    \"single_rows\": 300,\n    \"single_fire_default\": 11,\n    \"single_review\": 11,\n    \"batch_rows\": 900,\n    \"batch_fire_default\": 33,\n    \"batch_review\": 33,\n    \"quality_success_files\": 3,\n    \"quality_failed_files\": 0,\n    \"checks\": {\n      \"single_rows\": true,\n      \"single_fire_default\": true,\n      \"single_review\": true,\n      \"batch_rows\": true,\n      \"batch_fire_default\": true,\n      \"batch_review\": true,\n      \"quality_success_files\": true,\n      \"quality_failed_files\": true\n    },\n    \"passed\": true\n  },\n  \"finished_at\": \"2026-06-08 00:07:38\"\n}\n",
      "stderr": "",
      "json": {
        "platform": "Windows",
        "status": "completed",
        "request_file": "C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\confirmed_task_request.json",
        "request_cleared": true,
        "auto_loop_enabled": false,
        "infinite_loop": false,
        "started_at": "2026-06-08 00:07:38",
        "request": {
          "confirmed": true,
          "task_id": "check_v2_metrics",
          "task_name": "check_v2_metrics",
          "requested_by": "HY-AUTOQUEUE-01",
          "created_at": "2026-06-08 00:07:38"
        },
        "task_name": "check_v2_metrics",
        "blocked_by_safety": false,
        "risk": "safe_read_only",
        "entrypoint": "",
        "requires_gpt_confirmation": false,
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
        "finished_at": "2026-06-08 00:07:38"
      }
    },
    "safe_simulated_unconfirmed_refused": {
      "cmd": [
        "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
        "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
        "--run-confirmed"
      ],
      "code": 0,
      "stdout": "{\n  \"platform\": \"Windows\",\n  \"status\": \"rejected_unconfirmed\",\n  \"request_file\": \"C:\\\\Users\\\\Administrator\\\\Documents\\\\��ҵ����\\\\21_auto_control_console\\\\confirmed_task_request.json\",\n  \"request_cleared\": true,\n  \"auto_loop_enabled\": false,\n  \"infinite_loop\": false,\n  \"started_at\": \"2026-06-08 00:07:38\",\n  \"request\": {\n    \"confirmed\": false,\n    \"task_id\": \"run_single_desensitized_pipeline_v2\",\n    \"task_name\": \"run_single_desensitized_pipeline_v2\",\n    \"requested_by\": \"HY-AUTOQUEUE-01\",\n    \"created_at\": \"2026-06-08 00:07:38\"\n  },\n  \"blocked_by_safety\": false,\n  \"task_name\": \"run_single_desensitized_pipeline_v2\",\n  \"finished_at\": \"2026-06-08 00:07:38\"\n}\n",
      "stderr": "",
      "json": {
        "platform": "Windows",
        "status": "rejected_unconfirmed",
        "request_file": "C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\confirmed_task_request.json",
        "request_cleared": true,
        "auto_loop_enabled": false,
        "infinite_loop": false,
        "started_at": "2026-06-08 00:07:38",
        "request": {
          "confirmed": false,
          "task_id": "run_single_desensitized_pipeline_v2",
          "task_name": "run_single_desensitized_pipeline_v2",
          "requested_by": "HY-AUTOQUEUE-01",
          "created_at": "2026-06-08 00:07:38"
        },
        "blocked_by_safety": false,
        "task_name": "run_single_desensitized_pipeline_v2",
        "finished_at": "2026-06-08 00:07:38"
      }
    }
  },
  "checks": {
    "unconfirmed_refused": true,
    "real_file_blocked": true,
    "safe_read_only_executed": true,
    "safe_simulated_unconfirmed_refused": true,
    "request_cleared": true
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