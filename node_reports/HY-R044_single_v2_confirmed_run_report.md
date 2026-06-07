# HY-R044 Corrected Confirmed Run Report

- Platform: Windows
- Round: HY-R044
- Status: done
- Menu task: run_single_desensitized_pipeline_v2
- Correction note: previous failed status was caused by UnicodeEncodeError while printing console JSON in GBK terminal; the V2 task was rerun after UTF-8 stdout fix and passed.
- Request cleared: True

## Metrics
- Single rows: 300
- Single FIRE_DEFAULT: 11
- Single review: 11
- Batch rows: 900
- Batch FIRE_DEFAULT: 33
- Batch review: 33
- QC success files: 3
- QC failed files: 0

## Safety
- No real customer files were read.
- No Hongye database was read.
- No real quote result was generated.
- No infinite loop was started.
- git add . was not used.
- force push was not used.