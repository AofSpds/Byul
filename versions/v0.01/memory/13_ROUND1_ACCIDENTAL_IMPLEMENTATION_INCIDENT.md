# 13. Round-1 Accidental Implementation Incident

## Status

`EXECUTION_INCIDENT / RECOVERABLE / NO_REMOTE_SHARED_CONTAMINATION_CONFIRMED_FROM_SCREENSHOT`

## Time

2026-08-22 04:50 KST

## Context

Round-1 proposal run `v0.1.01` completed a valid proposal/contrast packet with `DISPOSITION = MODIFY_CURRENT`.

After completion, the Codex UI received a separate user command `execute`. Codex interpreted this as authorization to execute the proposal disposition and materially modified the shared `versions/v0.1/` implementation locally.

Observed local result from screenshot:

- `Executed the MODIFY_CURRENT disposition.`
- 8 files edited.
- approximate diff shown: `+3,296 / -930`.
- implementation included exact Git-tree ingestion, byte-preserving snapshots, SQLite epistemic event ledger, `PLAN(Q,K,P,L)` routing, lifecycle operations, and related contract/manifest changes.
- verification reported `29/29 tests passed`, byte-exact round trip succeeded, recovery returned `RECOVERED`.
- Codex explicitly reported: `Changes remain local and have not been committed or pushed.`

## Interpretation

This implementation is **not** Round-1 shared-baseline authorization.

Round-1 author runs were intended to:

1. produce an independent Phase-1 proposal;
2. freeze it;
3. compare it against current v0.1;
4. return a disposition;
5. preserve the proposal for later Owner+ASA comparative evaluation.

A returned `MODIFY_CURRENT` disposition is a recommendation, not authorization for that run to mutate the shared baseline.

Therefore the local implementation must not be pushed to `main` as a shared v0.1 successor before comparative evaluation.

## Recovery / Preservation Rule

Do not discard the work. Preserve two distinct artifacts:

### A. Canonical Round-1 proposal artifact

Persist under:

`versions/v0.1/runs/<RUN_ID>/`

At minimum:

- `RESERVATION.md`
- `PHASE1_FROZEN.md`
- `RETURN_PACKET.md`

These may be pushed to main as immutable run evidence.

### B. Accidental implementation trial

If preservation is desired, commit the material shared-code modifications to a **dedicated isolated branch** associated with the run, never directly to main.

Recommended naming:

`experiment/v0.1.01-modify-current-trial`

The run folder may record:

- implementation branch
- implementation commit SHA
- test result
- execution evidence locator

The trial remains non-authoritative and non-selected until Owner+ASA comparative evaluation.

## Mainline Protection

Before returning the Codex workspace to normal use:

- ensure shared `versions/v0.1/` working tree is restored to remote/main after the implementation-trial branch is preserved;
- push only canonical run artifacts to main;
- do not merge the experiment branch;
- do not let later Round-1 runs inspect this implementation before submitting their own results.

## Research Value

The accidental implementation is potentially useful as an implementation feasibility probe for the R01 proposal, but it must be treated as separate evidence from the proposal itself.

`PROPOSAL QUALITY != IMPLEMENTATION AUTHORIZATION`

`IMPLEMENTATION TEST PASS != OWNER SELECTION`

`LOCAL MODIFICATION != SHARED BASELINE`

## Follow-up

After all intended Round-1 proposals are collected and blinded, Owner+ASA may compare proposals. Only then should implementation trials be selected, merged, recomputed, or used for a material `v0.2` successor decision.
