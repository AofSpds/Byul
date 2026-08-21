# 15. Round-1 Clean Rerun — EOL Hash Gate Correction

## Status

`EXECUTION_CONTROL_CORRECTION / RESEARCH_RERUN / NON_NORMATIVE / NOT_VALIDATED`

## Trigger

Clean-rerun worker `v0.1.10` / Round Slot `R07` stopped at the Phase-1 remote-freeze gate even though:

- the expected Phase-1 commit existed remotely;
- the remote commit matched the local freeze commit;
- the remote Git blob matched the committed local Git blob;
- the only mismatch was SHA-256 of pre-commit working-tree bytes versus SHA-256 of canonical committed Git-blob bytes.

Observed local/remote diagnostic:

- working-tree `PHASE1_SHA256 = f88432ef555c284a950fd5a2650a370465723fa059ce935802e21a633827c68c`
- canonical remote blob `SHA256 = e763f2a7d56691da7e15dbf53d6ed5f664e1fb0ad094119c57fc5fc3c84d717d`
- `PHASE1_REMOTE_COMMIT_MATCH = TRUE`
- `PHASE1_REMOTE_BLOB_MATCH = TRUE`

The worker correctly failed closed under the packet as written.

## Root Cause

On Windows/checkouts with Git text normalization, working-tree bytes may use CRLF while the committed Git blob stores normalized LF bytes. Therefore:

`SHA256(WORKTREE_BYTES) != SHA256(COMMITTED_GIT_BLOB_BYTES)`

can be expected even when the committed artifact is exactly the intended repository artifact.

The previous clean-rerun packet incorrectly used working-tree byte SHA-256 as the remote-freeze equality target.

## Correct Canonical Identity Rule

For Git-persisted research artifacts, distinguish:

- `WORKTREE_SHA256` = environment/check-out representation diagnostic only;
- `CANONICAL_GIT_BLOB_SHA256` = SHA-256 over bytes returned by `git show <commit>:<path>` / `git cat-file blob`;
- Git blob object ID = repository object identity under the repository's Git object model;
- remote verification = remote ref resolves to the expected commit AND the canonical blob bytes at that commit match the local committed blob bytes.

The Phase-1 freeze gate MUST compare canonical committed Git-blob bytes, not checkout working-tree bytes.

## Corrected Phase-1 Gate

After writing `PHASE1_FROZEN.md`:

1. Optionally record `PHASE1_WORKTREE_SHA256` before commit as diagnostic provenance.
2. Commit the Phase-1 artifacts.
3. Compute `PHASE1_CANONICAL_BLOB_SHA256` from:
   `git show <PHASE1_FREEZE_COMMIT>:versions/v0.1/runs/<RUN_ID>/PHASE1_FROZEN.md`
4. Push the isolated run branch.
5. Fetch the remote branch/ref.
6. Verify the remote ref equals `PHASE1_FREEZE_COMMIT`.
7. Compute `REMOTE_PHASE1_CANONICAL_BLOB_SHA256` from the fetched remote commit/ref.
8. Require:
   `PHASE1_CANONICAL_BLOB_SHA256 == REMOTE_PHASE1_CANONICAL_BLOB_SHA256`.
9. If the committed Git blob identity/content matches, set:
   `PHASE1_REMOTE_CONFIRMED = TRUE`.
10. A difference between working-tree SHA-256 and canonical Git-blob SHA-256 caused only by line-ending normalization is NOT a freeze failure.

## Resume Rule For Already-Blocked Runs

A run blocked solely by this EOL/hash-gate defect MAY resume from its existing Phase-1 freeze commit without rerunning or rewriting Phase 1 if all are true:

- `PHASE1_REMOTE_COMMIT_MATCH = TRUE`;
- local committed Git blob equals remote committed Git blob;
- Phase-1 artifact has not changed since the freeze commit;
- isolated workspace and primary-worktree safety assertions still hold;
- no Phase-2 input was read before the block.

The run must record the old working-tree digest separately and the canonical Git-blob digest as the authoritative remote-freeze digest.

Do not amend or rewrite the existing Phase-1 freeze commit merely to change line endings.

## Future Packet Rule

All future clean-rerun controllers should use canonical Git-blob hashing for persisted-artifact equality. Working-tree byte hashes may remain as diagnostics but must not be compared directly with normalized repository blobs across environments.

## Boundary

This correction changes execution-verification mechanics only. It does not alter any Phase-1 proposal content, Byul model semantics, Owner selection, validation status, or implementation authority.

작성시각: 2026-08-22 05:50 KST
