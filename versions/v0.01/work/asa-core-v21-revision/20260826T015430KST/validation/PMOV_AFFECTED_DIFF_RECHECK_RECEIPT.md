# PMOV Affected-Diff Recheck — D1

```text
TARGET_SHA = 3feb15cfe33207aa2e158a3b0ad68dc4650a12991ce61e99c2828e623492e161
START_KST = 2026-08-26T02:17:04+09:00
CONTEXT_LOAD_END = 2026-08-26T02:17:16+09:00
END_KST = 2026-08-26T02:17:46+09:00
CONTEXT_LOAD_DURATION = 12 seconds
DIRECT_REVIEW_DURATION = 30 seconds
GIT_CALLS = 2
FULL_SCAN = NO
REPEATED_WHOLE_TARGET_READ = NO
PROPOSAL_PLAN_CONTENT_REREAD = NO
NEW_SCOPE_REQUEST = NO
BLOCKING_FINDINGS = 0
ADVISORY_FINDINGS = 1
VERDICT = PASS
```

Only scope-lock lines 9–14, E004–E015, V001–V003, the D1 manifest, and
proposal/plan byte identities were checked. `PMOV-B01`, `PMOV-B02`, and
`PMOV-A01` are closed. The remaining advisory is that overlapping S2–S4
artifact-time envelopes must not be summed as wall-clock or claimed as exact
per-worker compute; S8 follows that restriction.
