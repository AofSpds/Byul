# CONTROLV Affected-Diff Recheck — D1

```text
TARGET_SHA = 3feb15cfe33207aa2e158a3b0ad68dc4650a12991ce61e99c2828e623492e161
START_KST = 2026-08-26T02:17:02+09:00
END_KST = 2026-08-26T02:17:21+09:00
CONTEXT_LOAD_DURATION = less than 1 second
DIRECT_REVIEW_DURATION = 19 seconds
GIT_CALLS = 0
FULL_SCAN = NO
REPEATED_WHOLE_TARGET_READ = NO
NEW_SCOPE_REQUEST = NO
BLOCKING_FINDINGS = 0
ADVISORY_FINDINGS = 0
VERDICT = PASS
```

Only the D1 manifest, R6 source-recovery paragraph, E004–E015 timeline rows,
and six hash rows were rechecked. `CONTROL-B01` and `CONTROL-B02` are closed;
the six mechanical hashes pass. R2, R5, input sources, and unaffected semantic
sections were not reread.
