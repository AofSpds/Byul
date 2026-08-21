# Byul Round-1 Pre-Recovery Inventory

## Recovery identity

- RECOVERY_ID = `byul-round1-salvage-20260822-051437`
- RECOVERY_START_TIME = `2026-08-22 05:14:37 +09:00`
- ORIGINAL_BRANCH = `codex/byul-v0.1-r1`
- ORIGINAL_HEAD = `ecc3f5431ac967383027de7173bf2541cf87f2c5`
- QUARANTINE_BRANCH = `recovery/byul-round1-salvage-20260822-051437`
- REPOSITORY_ROOT = `C:/Users/ms1pk/OneDrive/문서/ChatGPT/E6`
- ORIGIN_URL = `https://github.com/AofSpds/Byul.git`
- ORIGIN_MAIN_SHA_AT_AUDIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`
- LAST_KNOWN_SAFE_MAIN_COMMIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`
- EXACT_RESEARCH_BASELINE_COMMIT = `891e4bd4b999eacc99431ed0db05062901a68dd9`
- REMOTE_MAIN_STATE = `SAFE_OR_RUN_ARTIFACT_ONLY`

Both declared commits resolve to commit objects. After `git fetch --prune origin`,
`origin/main` equaled the last-known-safe commit exactly. Therefore the comparison
range `8e21fbd..origin/main` contained no commits or changed paths.

## Writer-stability gate

Two complete inventories were taken 22 seconds apart before any repository
mutation. Both reported the same branch, HEAD, status, diff statistic, worktree,
branch inventory, and Round-1/v0.1 changed paths. No material change was observed.

- Inventory 1: original branch `codex/byul-v0.1-r1`, HEAD `ecc3f543...`
- Inventory 2: original branch `codex/byul-v0.1-r1`, HEAD `ecc3f543...`
- DIFF_STAT_BOTH = `5 files changed, 1305 insertions(+), 439 deletions(-)`
- WRITER_STABILITY = `STABLE_AT_GATE`

## Git status before recovery files were created

Staged diff was empty.

Tracked working-tree modifications:

```text
M versions/v0.1/MODEL_CONTRACT.md
M versions/v0.1/README.md
M versions/v0.1/data/SOURCE_MANIFEST.md
M versions/v0.1/src/byul_v01.py
M versions/v0.1/tests/test_byul_v01.py
```

Untracked files:

```text
.gitignore
versions/v0.1/data/source_manifest_v001.json
versions/v0.1/runs/v0.1.01/PHASE1_FROZEN.md
versions/v0.1/runs/v0.1.01/RESERVATION.md
versions/v0.1/runs/v0.1.01/RETURN_PACKET.md
versions/v0.1/runs/v0.1.02/PHASE1_FROZEN.md
versions/v0.1/runs/v0.1.02/RESERVATION.md
versions/v0.1/runs/v0.1.02/RETURN_PACKET.md
versions/v0.1/src/epistemic_ledger.py
versions/v0.1/src/transformation_contracts.py
versions/v0.1/tests/test_cli.py
versions/v0.1/tests/test_epistemic_ledger.py
versions/v0.1/tests/test_transformation_contracts.py
```

## Local topology before quarantine branch creation

```text
worktree C:/Users/ms1pk/OneDrive/문서/ChatGPT/E6
HEAD ecc3f5431ac967383027de7173bf2541cf87f2c5
branch refs/heads/codex/byul-v0.1-r1

local branch:
refs/heads/codex/byul-v0.1-r1 ecc3f5431ac967383027de7173bf2541cf87f2c5

remote branches after fetch:
refs/remotes/origin/HEAD 8e21fbdf597d38bb831834fc83cd3a53bcb180e0
refs/remotes/origin/main 8e21fbdf597d38bb831834fc83cd3a53bcb180e0

stashes: none
local commits not reachable from origin/main: none
```

The reflog showed the original branch created from `origin/main` at
`ecc3f5431ac967383027de7173bf2541cf87f2c5` at 04:09 KST and the audit fetch
fast-forwarding `origin/main` to `8e21fbdf...` at 05:12 KST.

## Round artifacts found on the visible filesystem

Two complete three-file artifact sets were found:

```text
versions/v0.1/runs/v0.1.01/{RESERVATION.md,PHASE1_FROZEN.md,RETURN_PACKET.md}
versions/v0.1/runs/v0.1.02/{RESERVATION.md,PHASE1_FROZEN.md,RETURN_PACKET.md}
```

No `RUN_MANIFEST.md`, `PHASE2_DELTA.md`, `IMPLEMENTATION_EXECUTION.md`, or
`IMPLEMENTATION_TRIAL*` file was present. Only one visible worktree existed.

## Git object findings

`git fsck --full --unreachable --no-reflogs` found no unreachable commit, but did
find transient trees and three unreachable blobs. Tree
`731e0bec1a17a19f076ba4d4a63522d2491451c7` preserves a staged implementation
snapshot containing both run artifact sets and the shared v0.1 implementation.
Its `README.md` and `tests/test_byul_v01.py` blobs differ from the later working
tree, proving multiple historical contents for those paths.

Relevant unreachable blobs:

```text
eb2d067c1d3d4b3ef69f17e9b551495116bb23fd  versions/v0.1/README.md
d0f15669aace9b41b1ed46d07c1c361f7e2f7c78  versions/v0.1/tests/test_byul_v01.py
11fbdd33bb9daf2dfce17f419215f1ea71ed4343  versions/v0.1/src/__pycache__/byul_v01.cpython-313.pyc
```

The unreachable blobs contained no `[RETURN PACKET]`, `PHASE1_FROZEN`, or
`DISPOSITION` marker. The transient tree is implementation/execution evidence,
not an additional proposal capture.

## Collision and contamination indicators

- Claimed RUN_ID collision on the visible filesystem: `NONE` (`v0.1.01` and
  `v0.1.02` are distinct).
- Independent submissions found: `2`.
- Shared implementation files were extensively modified and untracked modules and
  tests were added.
- Both proposals independently request closely overlapping ledger, exact-source,
  preservation-contract, transformation-planner, and lifecycle mechanisms.
- No repository evidence identifies which worker authored each shared hunk.
- The transient index tree and later working tree differ at two shared paths.
- File timestamps were recorded only as weak observation data and are not treated
  as causal proof.

## Credential screening

The changed/untracked path inventory contained no `.env`, credential, private-key,
or token path. Recovery staging is restricted to the Byul v0.1/Round-1 evidence,
the root `.gitignore`, and the recovery records.
