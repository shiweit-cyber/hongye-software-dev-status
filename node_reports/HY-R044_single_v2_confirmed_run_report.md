# HY-R044 confirmed single V2 pipeline run Report

- Platform: Windows
- Round: HY-R044
- Status: failed
- Menu task: run_single_desensitized_pipeline_v2
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
  "console_result": {
    "cmd": [
      "C:\\Users\\Administrator\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe",
      "C:\\Users\\Administrator\\Documents\\宏业软件\\21_auto_control_console\\auto_control_console_v3.py",
      "--run-confirmed"
    ],
    "code": 1,
    "stdout": "",
    "stderr": "Traceback (most recent call last):\n  File \"C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\auto_control_console_v3.py\", line 208, in <module>\n    main()\n  File \"C:\\Users\\Administrator\\Documents\\��ҵ����\\21_auto_control_console\\auto_control_console_v3.py\", line 204, in main\n    print(json.dumps(payload, ensure_ascii=False, indent=2))\nUnicodeEncodeError: 'gbk' codec can't encode character '\\ufffd' in position 1368: illegal multibyte sequence\n",
    "json": {}
  },
  "metrics": {},
  "passed": false
}
```

## Safety
- No real customer files were read.
- No Hongye database was read.
- No real quote result was generated.
- No infinite loop was started.
- git add . was not used.
- force push was not used.