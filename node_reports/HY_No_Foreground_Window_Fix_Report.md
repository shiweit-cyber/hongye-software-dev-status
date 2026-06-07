# HY No Foreground Window Fix Report

?????2026-06-08 00:20:55

## ????
Windows

## ????
?????????????????????????? output/reports/summary ????????????????????????????

## ????
- `13_pipeline`
- `15_batch_pipeline`
- `17_batch_quality_control`
- `19_multi_round_safe_loop`
- `20_low_risk_business_queue`
- `21_auto_control_console`
- `23_hongye_autoqueue`
- `24_future_autoqueue_plan`
- `25_test_queue`
- `04_AI??/node_reports`

## ???????????
- 13_pipeline/run_pipeline_v2.ps1: Invoke-Item .\output_v2
- 13_pipeline/run_pipeline_v2.bat: start .\output_v2
- 15_batch_pipeline/run_batch_pipeline.ps1: Start-Process $OutputDir
- 15_batch_pipeline/run_batch_pipeline_v2.ps1: Invoke-Item .\output_v2
- 15_batch_pipeline/run_batch_pipeline_v2.bat: start .\output_v2
- 17_batch_quality_control/run_quality_control.ps1: Start-Process summary
- 17_batch_quality_control/run_quality_control.bat: start summary
- 17_batch_quality_control/run_quality_control_v2.ps1: Invoke-Item .\summary_v2
- 17_batch_quality_control/run_quality_control_v2.bat: start .\summary_v2
- 19_multi_round_safe_loop/run_three_round_safe_loop.ps1/.bat: open reports
- 20_low_risk_business_queue/run_low_risk_business_queue.ps1/.bat: open reports
- 21_auto_control_console/run_auto_control_console.ps1/.bat: open reports
- 23_hongye_autoqueue/run_hongye_autoqueue.ps1/.bat and generator template: open reports

## ??????
- `13_pipeline/run_pipeline_v2.ps1`
- `13_pipeline/run_pipeline_v2.bat`
- `15_batch_pipeline/run_batch_pipeline.ps1`
- `15_batch_pipeline/run_batch_pipeline_v2.ps1`
- `15_batch_pipeline/run_batch_pipeline_v2.bat`
- `17_batch_quality_control/run_quality_control.ps1`
- `17_batch_quality_control/run_quality_control.bat`
- `17_batch_quality_control/run_quality_control_v2.ps1`
- `17_batch_quality_control/run_quality_control_v2.bat`
- `19_multi_round_safe_loop/run_three_round_safe_loop.ps1`
- `19_multi_round_safe_loop/run_three_round_safe_loop.bat`
- `20_low_risk_business_queue/run_low_risk_business_queue.ps1`
- `20_low_risk_business_queue/run_low_risk_business_queue.bat`
- `21_auto_control_console/run_auto_control_console.ps1`
- `21_auto_control_console/run_auto_control_console.bat`
- `23_hongye_autoqueue/run_hongye_autoqueue.ps1`
- `23_hongye_autoqueue/run_hongye_autoqueue.bat`
- `23_hongye_autoqueue/run_hongye_autoqueue_v1.py`

## ???????
- PowerShell?`-OpenOutput`
- BAT?`--open-output`
- ?? false???????????

## ?????????????
?????????? `Invoke-Item / Start-Process / start` ??????????

## ??????
- ??????????
- ?????????
- ????????
- ??? git add .?
- ? force push?
- ????????
- ????????
- ??????????