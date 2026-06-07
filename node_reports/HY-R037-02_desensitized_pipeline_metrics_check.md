# HY-R037-02 Desensitized pipeline metrics check

## Platform
Windows

## Result
completed

## Target
Verify HY-R034/HY-R035 desensitized pipeline output metrics remain available.

## Safe Executor
- exit_code: 0

## File Checks
- C:\Users\Administrator\Documents\宏业软件\13_pipeline\output: exists, file_count=14
- C:\Users\Administrator\Documents\宏业软件\15_batch_pipeline\output: exists, file_count=44
- C:\Users\Administrator\Documents\宏业软件\17_batch_quality_control\summary: exists, file_count=4
- C:\Users\Administrator\Documents\宏业软件\04_AI交接\node_reports\HY-R035_Desensitized_Pipeline_Archive.zip: exists, size_bytes=444587

## Desensitized Metrics
- pipeline_rows: 300
- pipeline_review: 28
- pipeline_fire_default: 28
- batch_rows: 900
- batch_review: 84
- batch_fire_default: 84
- batch_failed: 0
- qc_rows: 900
- qc_review: 84
- qc_fire_default: 84
- qc_failed: 0

## Missing
None

## Safety
- No real customer files read
- No Hongye database read
- No real quote result generated
- No git add .
- No force push
- auto_loop_enabled=false

Generated at: 2026-06-07 22:50:51