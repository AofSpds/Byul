# 15. Round-1 Clean Rerun — 9 Workers Launched

## Status

`CHECKPOINT / CLEAN_RERUN_ACTIVE / NON_NORMATIVE / NOT_VALIDATED`

## Time

2026-08-22 05:41 KST

## Owner Action

Owner launched 9 Codex workers using the corrected clean-rerun controller after the prior contaminated Round-1 was quarantined and the shared workspace restored.

## Clean Rerun Safety Contract

The corrected rerun requires:

- one worker = one isolated workspace;
- remote Round-slot reservation;
- remote canonical RUN_ID reservation;
- Phase-1 exact research baseline read from `891e4bd4b999eacc99431ed0db05062901a68dd9`;
- Phase-1 commit + push + remote digest verification before Phase 2;
- Phase-2 read-only comparison against exact safe implementation commit `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`;
- recommendation fields are advisory only and grant no implementation authority;
- generic `execute` after completion does not authorize implementation;
- each worker writes only under its own `versions/v0.1/runs/<RUN_ID>/` on its isolated branch;
- proposal workers never push or merge to `main`.

## Current Launch Count

- Owner-reported workers launched: `9`
- Designed Round slots: `R01-R10`
- Expected automatic allocation with 9 successful reservations: nine distinct slots, leaving one slot unfilled.
- Exact assigned slots/RUN_IDs are not assumed until remote reservation refs and completed run branches are verified.

## Interpretation

The previous contaminated experiment remains historical recovery evidence only. The clean rerun is intended to regenerate comparable independent proposals under a reproducible execution protocol.

Do not infer that 9 launches equal 9 completed valid runs. Completion requires each run's own remote Phase-1 freeze and final remote report verification.

## Next Route

1. Allow the 9 workers to run without additional generic execution commands.
2. Verify remote reservations/run branches as they appear.
3. After completion, collect reports from remote branches only.
4. Determine which Round slot remains unfilled.
5. Decide whether to launch the missing profile—especially `R10 LIFECYCLE_COMPOSITION` if it is the unfilled slot—based on remaining execution budget and observed allocation.
6. Blind-normalize valid clean rerun reports before Owner + ASA comparative evaluation.
