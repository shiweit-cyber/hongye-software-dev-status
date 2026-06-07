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
- Can enter Windows self-driving mode: True
- Stop reason: No hard blocker. HY-R010 still requires manual Hongye N10 import verification.
- Next round: HY-R010
- Next mode: stop for manual import verification
- Next reason: HY-R007 files and Hongye N10 exist. Tang boss needs to manually test Excel import in Hongye N10.

Safety:
- The runner is one-shot by default.
- It does not run as a background daemon.
- It stops when manual Hongye N10 operation, Git conflict, or safety risk is detected.
