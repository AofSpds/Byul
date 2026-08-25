# S6 D0 Finding Freeze

```text
TARGET_ID = D0
TARGET_SHA = 78c1d15e395ad53e04a3ba2388ce049c1355c27b7f9f53e24ab2e9bc00df2a6e
FINDING_FREEZE_KST = 2026-08-26T02:14:41+09:00
VALIDATORS_COMPLETE = MODELV / CONTROLV / PMOV
UNIQUE_BLOCKING_FINDINGS = 5
ADVISORY_FINDINGS = 2
NEW_SCOPE_REQUESTS = 0
FULL_SCANS = 0
TARGET_MUTATIONS = 0
CORRECTION_BATCH_LIMIT = 1
```

| Consolidated ID | Source finding(s) | Correction class | Adopted action |
|---|---|---|---|
| CF-01 | MODELV-B01 | MATERIAL_LOCAL | Clarify R1 §36: VIEW forms the observed State; FOLD only abbreviates an established representation. |
| CF-02 | MODELV-B02 | MATERIAL_LOCAL | Add local Pro-mode proposal guard to R1 §45. |
| CF-03 | CONTROL-B01 | CONTROL/EVIDENCE | Weaken R6 Git-locator statement to the exact ledger evidence boundary. |
| CF-04 | CONTROL-B02, PMOV-B02 | CONTROL/TELEMETRY | Close E004 and add supported S2–S6 intervals; keep unavailable splits explicit. |
| CF-05 | PMOV-B01 | CONTROL/METADATA | Replace stale scope-lock proposal/plan blobs with S0-accepted identities. |

Advisories are preserved and not promoted into blocking scope: R6 read-order
self-description and timely insertion of S6 receipts. The latter is completed
as ordinary telemetry bookkeeping, not as an extra correction finding.
