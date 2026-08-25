# PMOV S8 Calculation-Integrity Receipt

```text
VALIDATOR = PMOV
MODE = READ_ONLY / PRE-SUBSTITUTION THEN DIFF-ONLY RECHECK
INITIAL_START = 2026-08-26T02:21:48+09:00
INITIAL_CONTEXT_END = 2026-08-26T02:22:26+09:00
INITIAL_END = 2026-08-26T02:23:14+09:00
INITIAL_CONTEXT_LOAD = 38 seconds
INITIAL_DIRECT_REVIEW = 48 seconds
DIFF_RECHECK_START = 2026-08-26T02:24:17+09:00
DIFF_RECHECK_END = 2026-08-26T02:24:25+09:00
DIFF_RECHECK_DURATION = 8 seconds
GIT_CALLS = 0
FULL_SCAN = NO
TARGET_MUTATION = NO
FINAL_BLOCKING_FINDINGS = 0
FINAL_ADVISORY_FINDINGS = 0
FINAL_VERDICT = PASS
```

The validator confirmed the 140s initial validation window, 74s finding
integration, 92s D1 correction, 45s D1 recheck, 138s dispatch orchestration,
and all final-substitution formulas. It found three report-local stage-envelope
errors and requested an explicit macro-category coverage convention. PMO
corrected only those locations; the 8-second diff recheck passed. D1 was not
modified and no global validation was requested.

The later mechanical substitution uses:

```text
ACTUAL = PROGRAM_END - 2026-08-26T01:54:30+09:00
CATEGORIZED = ACTUAL - 158 seconds
COVERAGE = CATEGORIZED / ACTUAL
VALIDATION_SHARE = 646 seconds / ACTUAL
S8 = PROGRAM_END - 2026-08-26T02:17:46+09:00
```
