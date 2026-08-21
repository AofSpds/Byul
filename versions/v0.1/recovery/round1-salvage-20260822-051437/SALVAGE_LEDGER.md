# Byul Round-1 Salvage Ledger

## Ledger scope

This ledger evaluates evidence integrity only. It does not rank proposal quality,
select an architecture, or authorize any implementation.

## Canonical mapping

Two distinct submissions were recovered and their claimed IDs do not collide.
Normalized copies therefore retain their original IDs:

| Capture | Claimed RUN_ID | Canonical RUN_ID | Normalized path |
|---|---|---|---|
| CAPTURE-001 | `v0.1.01` | `v0.1.01` | `normalized/v0.1.01/` |
| CAPTURE-002 | `v0.1.02` | `v0.1.02` | `normalized/v0.1.02/` |

The normalized artifact copies have the same SHA-256 values as their raw sources.
Raw bytes were not rewritten.

## CAPTURE-001

```text
CAPTURE_ID = CAPTURE-001
CLAIMED_RUN_ID = v0.1.01
CANONICAL_RUN_ID = v0.1.01
CLAIMED_ROUND_SLOT = R01
CLAIMED_PROFILE = NEUTRAL_BLIND

SOURCE_WORKTREE = C:/Users/ms1pk/OneDrive/문서/ChatGPT/E6
SOURCE_BRANCH = codex/byul-v0.1-r1
SOURCE_COMMIT_OR_BLOB = untracked-at-recovery; PHASE1 blob fcbb184a673e22cee2314003eba83077188ff53d; RETURN_PACKET blob 479ca31906c1c3ebc61e7197df5cf3998ef7b51f

PHASE1_RECOVERED = TRUE
PHASE1_SHA256 = ae7f8032370660c7ec2cfc482597a0c30ac52685f1c734b9fef36ec0215fe908
PHASE1_STATE = PARTIAL

RETURN_PACKET_RECOVERED = TRUE
RETURN_PACKET_SHA256 = 751bd27654f3807bf7c4c22d64014b95564240ae95a5b3d602bb229e03c00fdb

PHASE2_STATE = CONTAMINATION_POSSIBLE

IMPLEMENTATION_FOUND = TRUE (shared evidence; not uniquely attributable)
IMPLEMENTATION_STATE = MIXED_TRIAL
IMPLEMENTATION_PATCH_SHA256 = 224655494bb8575cbcc3c123e47e6185e8b19aa02af95022ba771798a6c61cae
TEST_RESULT = 35/35 current mixed-trial tests PASS; packet separately reports 11/11 pre-execute baseline tests PASS
EXECUTION_EVIDENCE = shared modified/new implementation files; transient staged tree 731e0bec1a17a19f076ba4d4a63522d2491451c7; unreachable Python bytecode blob; authored tests; recovery-controller test run

CROSS_RUN_REFERENCE_FOUND = FALSE in proposal artifacts
SHARED_FILE_OVERLAP_FOUND = TRUE in implementation evidence
TIMING_CERTAINTY = LOW

SALVAGE_VERDICT = YELLOW

EVAL_USABLE_PART = Frozen Phase-1 proposal, with explicit provenance limitation
LIMITATIONS = The file identifies the exact research baseline and asserts pre-Phase-2 freeze, and its blob is stable across recovered transient/current states. No pre-exposure commit, isolated worktree, or independent execution log proves the freeze ordering; Phase 2's exact read state is also not provable.
UNKNOWN_ITEMS = Exact Phase-1 creation ordering; exact Phase-2 read tree; hunk authorship; execute time; whether UI-only execution messages contained additional evidence.
```

## CAPTURE-002

```text
CAPTURE_ID = CAPTURE-002
CLAIMED_RUN_ID = v0.1.02
CANONICAL_RUN_ID = v0.1.02
CLAIMED_ROUND_SLOT = R02
CLAIMED_PROFILE = NEUTRAL_BLIND

SOURCE_WORKTREE = C:/Users/ms1pk/OneDrive/문서/ChatGPT/E6
SOURCE_BRANCH = codex/byul-v0.1-r1
SOURCE_COMMIT_OR_BLOB = untracked-at-recovery; PHASE1 blob 2b4ddbc61345640bf5d2bff4b0af5cf8c131df78; RETURN_PACKET blob 66b4ccf5c8bbfe274d8643b9a4d4061ebbaa21df

PHASE1_RECOVERED = TRUE
PHASE1_SHA256 = 097d1fb5adb87a35e165365fdee9c4f63cfa307e3217825b3bc27caba1570d5d
PHASE1_STATE = PARTIAL

RETURN_PACKET_RECOVERED = TRUE
RETURN_PACKET_SHA256 = 9907f208cfcbdd859b78ce59aeceb9e672dd5737d73f4bd29684e18e42fd9f52

PHASE2_STATE = CONTAMINATION_POSSIBLE

IMPLEMENTATION_FOUND = TRUE (shared evidence; not uniquely attributable)
IMPLEMENTATION_STATE = MIXED_TRIAL
IMPLEMENTATION_PATCH_SHA256 = 224655494bb8575cbcc3c123e47e6185e8b19aa02af95022ba771798a6c61cae
TEST_RESULT = 35/35 current mixed-trial tests PASS; packet separately reports 11/11 pre-execute baseline tests PASS
EXECUTION_EVIDENCE = shared modified/new implementation files; transient staged tree 731e0bec1a17a19f076ba4d4a63522d2491451c7; unreachable Python bytecode blob; authored tests; recovery-controller test run

CROSS_RUN_REFERENCE_FOUND = FALSE in proposal artifacts
SHARED_FILE_OVERLAP_FOUND = TRUE in implementation evidence
TIMING_CERTAINTY = LOW

SALVAGE_VERDICT = YELLOW

EVAL_USABLE_PART = Frozen Phase-1 proposal, with explicit provenance limitation
LIMITATIONS = The file identifies the exact research baseline and asserts pre-Phase-2 freeze, and its blob is stable across recovered transient/current states. No pre-exposure commit, isolated worktree, or independent execution log proves the freeze ordering; Phase 2's exact read state is also not provable.
UNKNOWN_ITEMS = Exact Phase-1 creation ordering; exact Phase-2 read tree; hunk authorship; execute time; whether UI-only execution messages contained additional evidence.
```

## Aggregate verdict

```text
CAPTURES_FOUND = 2
GREEN_COUNT = 0
YELLOW_COUNT = 2
RED_COUNT = 0
```

`PARTIAL` is not promoted to `VERIFIED` from file timestamps or self-attestation.
The two YELLOW results may be evaluated only with their stated evidence-integrity
limitations. The mixed implementation must not influence proposal scoring by
default.

