# Byul v0.1 Parallel Proposal Round-1 — Evaluation Packet

## Status

`OWNER_ASA_REVIEW_SPEC / RESEARCH / NON_NORMATIVE / NOT_VALIDATED`

## Purpose

Evaluate independent Round-1 proposals without rewarding mere agreement with the current v0.1 implementation and without discarding valuable minority alternatives.

## Inputs

- Round launch spec: `ROUND1_LAUNCH_PACKET.md`
- Exact proposal baseline: `891e4bd4b999eacc99431ed0db05062901a68dd9`
- Submissions: `v0.1-R01 ... v0.1-R10`

## Review Preparation

1. Verify each packet reports the exact baseline and run identity.
2. Separate Phase-1 frozen proposal from Phase-2 current-v0.1 comparison.
3. Remove run identity/profile labels from the substantive proposal before first comparative review where practical.
4. Normalize all returns into the same fields.
5. Do not merge proposals before evaluation.

## Fail / Review Gates

Flag a proposal `FAIL_GATE` or `REVIEW_REQUIRED` if it materially:

- invents unsupported facts as certain;
- erases OPEN/UNKNOWN/non-conclusion states;
- assumes current v0.1 or current formalism family is canonical without argument;
- claims lossless reverse reconstruction after discarding required semantics;
- hides semantic loss, authority drift, or lifecycle failure;
- treats a philosophical or physical analogy as proof;
- ignores prior art without demonstrating a real gap;
- changes BYUL CORE-A meaning without explicitly proposing and justifying that change;
- evaluates itself as validated/PASS.

A gate flag does not automatically delete the proposal from the research archive. Interesting failure modes are evidence.

## Comparative Axes

Use qualitative ratings first: `STRONG / ADEQUATE / WEAK / UNKNOWN` plus evidence notes.

- `STATE_RECONSTRUCTION_FIDELITY`
- `FACT_HYPOTHESIS_UNKNOWN_DISCIPLINE`
- `OWNER_INTENT_FIDELITY`
- `BYUL_CORE_A_FIT`
- `PROBLEM_DEFINITION_QUALITY`
- `PRIOR_ART_GROUNDING`
- `REPRESENTATION_FITNESS`
- `SEMANTIC_PRESERVATION`
- `LOSS_DISCLOSURE`
- `COMPOSITION_QUALITY`
- `LIFECYCLE_ROBUSTNESS`
- `REVERSIBILITY_RECOVERY_DISCIPLINE`
- `ROUTING_JUSTIFICATION`
- `SIMPLICITY_VS_POWER`
- `FALSIFIABILITY_TESTABILITY`
- `IMPLEMENTATION_FEASIBILITY`
- `MIGRATION_COST`
- `USEFUL_NOVELTY`

Do not collapse these into one weighted score in Round-1 unless later evidence shows a clear need.

## Pairwise Review

Prefer pairwise decisions over absolute rank.

For each compared pair record:

- which proposal better preserves the research problem;
- which proposal makes fewer unsupported commitments;
- which proposal has stronger lifecycle behavior;
- where each dominates the other;
- whether they are actually complementary rather than substitutes.

Allowed pairwise outcomes:

- `A_DOMINATES`
- `B_DOMINATES`
- `TRADEOFF`
- `COMPLEMENTARY`
- `INSUFFICIENT_EVIDENCE`

## Diversity Preservation

After initial comparisons, preserve at least:

- strongest current-compatible proposal;
- strongest replacement/reframe proposal;
- strongest lifecycle/composition proposal;
- one minority proposal that is materially different and not fail-gated for hallucination/semantic cheating.

Do not select finalists only by majority convergence.

## Round-1 Synthesis Outputs

Owner + ASA should produce:

1. `COMMON_CONVERGENCE` — structures independently rediscovered across runs.
2. `MEANINGFUL_DIVERGENCE` — disagreements that matter to representation or lifecycle.
3. `NEW_PRIOR_ART_CANDIDATES` — repeated or strong outside candidates.
4. `CURRENT_V0_1_STRENGTHS`.
5. `CURRENT_V0_1_FAILURES_OR_GAPS`.
6. `ROUTING_EVIDENCE` — evidence for/against situation-dependent representation selection.
7. `CORE_A_PRESSURE_POINTS` — where proposals expose ambiguity in BYUL CORE-A interpretation.
8. `FINALISTS` — normally 3–4.
9. `MINORITY_KEEP` — at least one useful non-finalist when justified.
10. `ROUND2_PRESSURE_TESTS` — tests that discriminate finalists.

## Important Boundary

Round-1 evaluation is research selection, not scientific validation, production approval, or canonical architecture freeze.

작성시각: 2026-08-22 03:37 KST
