# Byul v0.1 Parallel Proposal Round-1 — Workspace Contract

## Status

`EXECUTION_CONTROL / RESEARCH / NON_NORMATIVE / NOT_VALIDATED`

## Purpose

Round-1 parallel runs may execute concurrently only if each run has an isolated write workspace and a deterministic output folder. This contract prevents cross-run contamination, file collisions, and accidental mutation of the shared research baseline.

## Exact Baseline

- REPOSITORY: `AofSpds/Byul`
- ROUND_ID: `BYUL-v0.1-PARALLEL-PROPOSAL-R1`
- BASELINE_COMMIT: `891e4bd4b999eacc99431ed0db05062901a68dd9`

## Mandatory Isolation

Preferred execution mode:

`ONE RUN = ONE ISOLATED BRANCH OR WORKTREE = ONE OUTPUT FOLDER`

Recommended branch/worktree names:

- `byul-r1-r01`
- `byul-r1-r02`
- ...
- `byul-r1-r10`

Every isolated branch/worktree MUST originate from the exact baseline commit above.

If isolated branches/worktrees are unavailable, parallel repository writes are NOT considered safe. In that case runs may execute in parallel only if they are read-only and return results externally for later controlled persistence.

## Deterministic Output Routing

Each run may write only under its own directory:

`versions/v0.01/experiments/round1/runs/<RUN_ID>/`

Canonical mapping:

- `v0.1-R01` → `versions/v0.01/experiments/round1/runs/R01/`
- `v0.1-R02` → `versions/v0.01/experiments/round1/runs/R02/`
- `v0.1-R03` → `versions/v0.01/experiments/round1/runs/R03/`
- `v0.1-R04` → `versions/v0.01/experiments/round1/runs/R04/`
- `v0.1-R05` → `versions/v0.01/experiments/round1/runs/R05/`
- `v0.1-R06` → `versions/v0.01/experiments/round1/runs/R06/`
- `v0.1-R07` → `versions/v0.01/experiments/round1/runs/R07/`
- `v0.1-R08` → `versions/v0.01/experiments/round1/runs/R08/`
- `v0.1-R09` → `versions/v0.01/experiments/round1/runs/R09/`
- `v0.1-R10` → `versions/v0.01/experiments/round1/runs/R10/`

## Required Files Per Run

Each run persists at minimum:

- `RUN_MANIFEST.md`
- `PHASE1_FROZEN.md`
- `PHASE2_DELTA.md`
- `RETURN_PACKET.md`

Optional artifacts must go only under:

`versions/v0.01/experiments/round1/runs/<RUN_ID>/artifacts/`

## Write Prohibitions

A run MUST NOT modify:

- `versions/v0.00/`
- `versions/v0.01/CURRENT_STATUS.md`
- `versions/v0.01/README.md`
- `versions/v0.01/memory/`
- `versions/v0.01/experiments/round1/ROUND1_*`
- `versions/v0.1/`
- another run's directory
- repository-wide governance/control files

A run is an experiment author, not a baseline maintainer.

## Run Manifest Minimum Fields

`RUN_MANIFEST.md` must include:

- ROUND_ID
- RUN_ID
- COHORT
- PROFILE
- BASELINE_COMMIT
- BRANCH_OR_WORKTREE_ID
- OUTPUT_DIRECTORY
- PHASE1_FROZEN_STATE
- PHASE1_FREEZE_COMMIT_OR_DIGEST
- PHASE2_COMPLETED_STATE
- RETURN_PACKET_SHA256 if available
- STARTED_AT
- COMPLETED_AT

## Phase-1 Freeze Rule

Before reading `versions/v0.1/`, the run must persist `PHASE1_FROZEN.md` in its own output folder.

Phase 2 may append a delta file but MUST NOT rewrite the Phase-1 frozen artifact.

## Collection Rule

Do not let run branches merge arbitrary changes into main.

After all runs finish, a collection step should import only the approved per-run output directories into the Round-1 result set. Shared baseline files remain unchanged.

Recommended collection layout on main:

`versions/v0.01/experiments/round1/runs/R01/...R10/`

The collector preserves raw run artifacts byte-for-byte where practical and creates any normalized/blinded evaluation copies separately.

## Safety Result

Parallel execution is considered safe only when BOTH are true:

1. write workspace isolation exists; and
2. deterministic per-run output routing is enforced.

Unique folder paths alone are not sufficient protection when multiple workers concurrently mutate the same Git branch.

작성시각: 2026-08-22 03:40 KST
