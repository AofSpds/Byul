# PMOV Execution and Attribution Validation Receipt — D0

```text
VALIDATOR = PMOV
TARGET_ID = D0
TARGET_SHA = 78c1d15e395ad53e04a3ba2388ce049c1355c27b7f9f53e24ab2e9bc00df2a6e
START_KST = 2026-08-26T02:11:21+09:00
CONTEXT_LOAD_END = 2026-08-26T02:11:59+09:00
DIRECT_REVIEW_START = 2026-08-26T02:11:59+09:00
END_KST = 2026-08-26T02:13:01+09:00
CONTEXT_LOAD_DURATION = 38 seconds
DIRECT_REVIEW_DURATION = 62 seconds
GIT_CALLS = 3
FULL_SCAN = NO
REPEATED_WHOLE_TARGET_READ = NO
TARGET_MUTATION = NO
NEW_SCOPE_REQUEST = NO
BLOCKING_FINDINGS = 2
ADVISORY_FINDINGS = 1
VERDICT = CORRECTION_REQUIRED
```

## Exact slice and passed controls

The validator read the proposal, plan, scope lock, D0/slice manifests, and
three telemetry ledgers. The exact task branch, six D0 hashes, pre-freeze
output order, bounded scope, parallel/read-only routing, correction ceiling,
budget arithmetic, and neutral latency formulas passed.

## Frozen findings

1. `PMOV-B01`: the scope lock retained pre-S0 proposal/plan blob identities.
2. `PMOV-B02`: the timeline had not closed S1 or recorded S2–S5 at dispatch.
3. `PMOV-A01` (advisory): record all three S6 receipts in the validation ledger
   before S7.

Recheck is metadata-only: the two scope-lock lines and supported timeline
additions. D0 semantic status is otherwise unchanged.
