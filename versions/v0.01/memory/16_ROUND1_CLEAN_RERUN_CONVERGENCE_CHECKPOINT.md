# Byul Round-1 Clean Rerun — Convergence Checkpoint

DATE_KST = 2026-08-22 06:00
STATE = RESEARCH_CHECKPOINT / NON_NORMATIVE / NOT_SELECTED
ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01

## EXECUTION STATE

- Remote slot reservations exist for R01-R10.
- Clean experiment branches exist for v0.1.03 through v0.1.12.
- R01-R06, R08, R09, R10 have remotely persisted proposal artifacts; R07 has a remotely frozen Phase-1 proposal but its first completion attempt stopped at the EOL hash-gate defect pending corrected resume.
- No proposal recommendation is implementation authority.

## STRONG CONVERGENCE OBSERVED

Across neutral, adversarial, minimal-information, outside-prior-art, and lifecycle-pressure runs, proposals repeatedly converge on the following architecture family:

1. Exact/content-addressed source evidence must remain the lowest authority layer.
2. Evolving epistemic/research changes should be represented append-only with explicit lineage rather than destructive overwrite.
3. Authority is scoped: a source/record is authoritative for what was captured or recorded, not automatically for external truth.
4. Current/history/open/search/causal/Petri/Event/LTS/simulation/etc. should default to derived, rebuildable projections with provenance.
5. Transformations need explicit preservation/loss contracts and receipts; lossy reverse synthesis must not be relabeled as recovered ground truth.
6. Preservation demand should be a hard planner constraint before cost/ranking.
7. Lifecycle operations—correction, branch/split, composition, merge, migration, recovery, successor/retire—must preserve lineage and explicit conflicts.
8. Petri/Event/Causal/LTS remain optional purpose-specific views unless later evidence grants scoped authority.
9. R(S,M,L) is widely retained only as a mnemonic/facade; executable planning is repeatedly reformulated around query/intent + preservation + authoritative/available capabilities + lifecycle/constraints/budget.
10. Current v0.1 is broadly judged MODIFY rather than REPLACE: preserve parser/CLI/view/test scaffolding while replacing weak source/exactness, epistemic, transformation, routing, and lifecycle semantics.

## MOST IMPORTANT DIVERGENCE

The major disagreement is not ledger-versus-no-ledger. It is how much structure belongs in the minimum core.

- Rich proposals include typed claims, assumptions/justifications, bitemporal semantics, receipts, and optional TMS/ATMS support.
- R09 MINIMAL_INFORMATION still retains a ledger, but reduces authority to only two broad classes: content-addressed Artifact + immutable Ledger Entry, with disposable views and a compressed Plan(Q,P,A) interface.
- R08 ADVERSARIAL_REFRAME also keeps the ledger core while rejecting R(S,M,L) as the fixed public decomposition.
- Therefore the immediate successor hypothesis should prefer a minimal ledger core and treat richer epistemic/TMS/CRDT/formal-model machinery as evidence-triggered extensions rather than mandatory first implementation.

## IMPORTANT COUNTER-HYPOTHESIS

All runs acknowledge that disciplined Git + Markdown may outperform a richer ledger at current scale. This remains the strongest simplicity control and must be tested explicitly.

## CURRENT ASA INTERPRETATION

The clean rerun has moved the research from open-ended architecture brainstorming to a comparatively narrow hypothesis set, but it has NOT selected a final architecture.

Best current comparison set for the next experiment:

- C0: current v0.1 baseline.
- C1: hardened Git+Markdown/control-manifest baseline.
- C2: minimal content-addressed Artifact + append-only Ledger Entry + reducer/head + ViewManifest + Preservation/Loss Contract planner.
- C3: richer ledger variant only if C2 fails on reconstruction/conflict/lifecycle cases.

The next decisive evidence should come from blind reconstruction, lifecycle torture, semantic-loss/refusal tests, invalidation accuracy, merge/conflict retention, recovery, and total complexity/cost—not another prose-only consensus round.

## LIMITATIONS

- Ten runs are not statistically independent human experts; they share model lineage and a common prompt/problem framing.
- The prompt itself emphasizes exact evidence, preservation, provenance, lifecycle, and non-canonical formalisms, which can induce correlated architectural convergence.
- Convergence is therefore strong design evidence, not scientific proof or Owner Acceptance.
- R07 Phase-1 contributes to architecture convergence, but its clean final Phase-2 completion remains pending until the EOL verification correction is applied.
