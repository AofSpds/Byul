# D0 to D1 Diff Classification

```text
CORRECTION_BATCH = 1 / 1
D0_TARGET_SHA = 78c1d15e395ad53e04a3ba2388ce049c1355c27b7f9f53e24ab2e9bc00df2a6e
D1_TARGET_SHA = 3feb15cfe33207aa2e158a3b0ad68dc4650a12991ce61e99c2828e623492e161
FINDINGS_ADDRESSED = 5/5
MATERIAL_GLOBAL = 0
NEW_SCOPE = 0
```

| Change | Class | Affected validator / criteria | Recheck boundary |
|---|---|---|---|
| R1 §36 FOLD/State clarification | MATERIAL_LOCAL | MODELV / AC-08 | changed paragraph plus adjacent diagram |
| R1 §45 Probe proposal guard | MATERIAL_LOCAL | MODELV / AC-06, AC-10 | changed introduction only |
| R6 Git-locator evidence boundary | CONTROL/EVIDENCE | CONTROLV / AC-03, AC-12 | changed source-boundary paragraph only |
| Scope-lock proposal/plan blobs | CONTROL/METADATA | PMOV / AC-13, AC-30 | two changed lines only |
| Timeline S1 close and S2–S7 rows | CONTROL/TELEMETRY | CONTROLV + PMOV / AC-16, AC-20, AC-22, AC-25 | appended/changed TSV rows only |

No change was made to R2, R3, R4, R5, the canonical input bytes, or the
Owner/Open/PI/question registries. `SHA_CHANGED` is not used as a reason for
whole-target revalidation.
