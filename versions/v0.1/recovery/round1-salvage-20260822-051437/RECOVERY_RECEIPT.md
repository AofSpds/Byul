# Byul Round-1 Recovery Receipt

```text
RECOVERY_ID = byul-round1-salvage-20260822-051437
RECOVERY_COMPLETED_AT = 2026-08-22 05:21:35 +09:00

QUARANTINE_BRANCH = recovery/byul-round1-salvage-20260822-051437
QUARANTINE_COMMIT_SHA = b20939bbec9a06f4f097ee4f5f0c999569133761
QUARANTINE_REMOTE_CONFIRMED = TRUE

REMOTE_MAIN_STATE = SAFE_OR_RUN_ARTIFACT_ONLY
ORIGIN_MAIN_SHA_AT_AUDIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0

CAPTURES_FOUND = 2
GREEN_COUNT = 0
YELLOW_COUNT = 2
RED_COUNT = 0

MISSING_ARTIFACT_COUNT = 7 reported proposal/return-packet sets minimum; auxiliary absent records are uncounted because existence cannot be proven

SHARED_WORKSPACE_RESTORED = TRUE
RESTORED_BRANCH = main
RESTORED_HEAD = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0
BASELINE_TEST_STATE = PASS (11/11)

REMOTE_MAIN_REMEDIATION_REQUIRED = FALSE
RECOVERY_STATE = COMPLETE
```

## Verification

- Remote quarantine branch was confirmed by `git ls-remote` at the snapshot SHA
  before restoration.
- Local `main`, `origin/main`, and the declared last-known-safe commit all resolve
  to `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`.
- `git diff origin/main -- versions/v0.1` was empty after restoration.
- No recovery command changed `versions/v0.00/` or `versions/v0.01/` research
  semantics; the restored worktree is identical to `origin/main`.
- No tracked or untracked accidental implementation file remained on restored
  `main`.
- Raw capture blobs on the quarantine branch retain the original Git blob IDs:
  CAPTURE-001 Phase 1 `fcbb184a...`, packet `479ca319...`; CAPTURE-002 Phase 1
  `2b4ddbc6...`, packet `66b4ccf5...`.
- The quarantine snapshot is not merged into `main`.
- The existing safe-baseline command
  `python -B -m unittest discover -s versions/v0.1/tests -p "test_*.py" -v`
  ran 11 tests successfully.

The receipt records evidence integrity and workspace restoration only. It does
not authorize production, select a proposal, or validate the mixed implementation.
