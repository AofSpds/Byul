# 14. Round-1 Rerun Safety Correction

## Status

`OWNER_DIRECTION / RESEARCH_EXECUTION_SAFETY / NON_NORMATIVE`

## Owner Direction — 2026-08-22 05:30 KST

Owner decided not to treat the contaminated first Round-1 attempt as the primary experiment. Preserve its quarantine/recovery evidence as history, but rerun the parallel proposal experiment cleanly.

Core correction:

- rerun from the same exact research baseline for comparability;
- every Codex worker must use its own isolated branch/worktree before any mutation;
- no two workers may share a mutable worktree;
- Phase-1 must be frozen, committed, and pushed on the worker's own branch before Phase-2 begins;
- Phase-2 must read an exact pinned implementation commit, never mutable shared working-tree files;
- `KEEP/MODIFY/REPLACE/HYBRID/REFRAME` is a recommendation field only and never authorizes implementation;
- generic `execute` means execute the research packet only; implementation requires a separate explicit implementation-trial authorization packet;
- each worker must persist its report to Git before declaring completion;
- workers never push shared implementation changes or arbitrary branch content to main;
- automatic run numbering must not rely on shared mutable files; reservation must be remotely collision-safe or canonical IDs may be assigned in a later collector step;
- the old contaminated run remains evidence/history, not the clean rerun baseline.

## Rerun Design Direction

Preferred clean rerun pattern:

`ONE WORKER = ONE UNIQUE REMOTE RESERVATION + ONE ISOLATED WORKTREE/BRANCH + ONE PHASE1 FREEZE COMMIT + ONE FINAL REPORT COMMIT`

Phase-1 research baseline remains:

`891e4bd4b999eacc99431ed0db05062901a68dd9`

Safe implementation comparison target should be pinned by exact commit rather than read from a mutable shared worktree.

## Failure Closed

If a worker cannot verify isolated worktree ownership, exact baseline reads, Phase-1 remote freeze, or report push, it must stop with an explicit blocked state rather than continue in the shared workspace.

This note records Owner correction and rerun intent only. It does not select a model, authorize an implementation, or validate any proposal.
