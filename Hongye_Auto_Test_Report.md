# Hongye Auto Test Report

Round: HY-R010 preparation
Platform: Windows
Result: Self-driving runner prepared

Route table:
- HY-R009: GCFX scan and Excel import preparation; AutoAllowed=True; StopCondition=Stop on safety risk or public repo issue
- HY-R010: Hongye N10 import verification recording; AutoAllowed=False; StopCondition=Manual Hongye N10 operation required
- HY-R011: Ask Mac to adjust Excel headers from feedback; AutoAllowed=True; StopCondition=Stop if HY-R010 feedback missing
- HY-R012: GCFX structure deeper metadata probing; AutoAllowed=True; StopCondition=Do not write price details or commit raw GCFX
- HY-R013: Verify save/export GCFX path after successful import; AutoAllowed=False; StopCondition=Manual Hongye N10 operation required

One-shot self-check:
- Can enter Windows self-driving mode: False
- Stop reason: Hongye N10 missing; HY-R007 Excel missing
- Next round: HY-R009
- Next mode: auto scan and wait for import file
- Next reason: HY-R007 Excel file is missing.

Safety:
- The runner is one-shot by default.
- It does not run as a background daemon.
- It stops when manual Hongye N10 operation, Git conflict, or safety risk is detected.
