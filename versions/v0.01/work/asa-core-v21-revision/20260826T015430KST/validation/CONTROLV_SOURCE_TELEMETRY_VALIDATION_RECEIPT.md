# CONTROLV Source and Telemetry Validation Receipt — D0

```text
VALIDATOR = CONTROLV
TARGET_ID = D0
TARGET_SHA = 78c1d15e395ad53e04a3ba2388ce049c1355c27b7f9f53e24ab2e9bc00df2a6e
START_KST = 2026-08-26T02:11:11+09:00
CONTEXT_LOAD_END = 2026-08-26T02:12:23+09:00
DIRECT_REVIEW_START = 2026-08-26T02:12:23+09:00
END_KST = 2026-08-26T02:13:27+09:00
CONTEXT_LOAD_DURATION = 72 seconds
DIRECT_REVIEW_DURATION = 64 seconds
GIT_CALLS = 0
FULL_SCAN = NO
REPEATED_WHOLE_TARGET_READ = NO
NEW_SCOPE_REQUEST = NO
BLOCKING_FINDINGS = 2
ADVISORY_FINDINGS = 1
VERDICT = BLOCKED_PENDING_ONE_CONTROL_CORRECTION_BATCH
```

## Exact slice and passed controls

The validator read the three input-control files; R2; the R5 registry plus
five referenced question excerpts; R6; hashes; D0 manifest; and the telemetry
ledgers. Six output hashes, six canonical inputs, `73/10/7` register counts,
all `Q-001..180` dispositions, duplicate targets, five byte-identical input
groups, and the missing-source non-inference boundary passed.

## Frozen findings

1. `CONTROL-B01`: R6's negative Git-locator wording was stronger than the
   source-filename lookup evidence recorded in the Git read ledger.
2. `CONTROL-B02`: E004 remained open and S2–S5/freeze evidence was absent from
   the timeline at dispatch.
3. `CONTROL-A01` (advisory): R6's read order does not explicitly say that the
   index is R6 and the hash manifest is control metadata outside the six
   semantic documents. D0 membership is nevertheless unambiguous.

Recheck is restricted to the R6 evidence-boundary diff and supported timeline
rows. The advisory is preserved for later editorial consideration.
