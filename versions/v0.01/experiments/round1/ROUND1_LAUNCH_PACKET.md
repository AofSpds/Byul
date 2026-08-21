# Byul v0.1 Parallel Proposal Round-1 — Launch Packet

## Status

`EXECUTION_SPEC / RESEARCH / NON_NORMATIVE / NOT_VALIDATED`

## Exact Research Baseline

- REPOSITORY: `AofSpds/Byul`
- ROUND_ID: `BYUL-v0.1-PARALLEL-PROPOSAL-R1`
- EXACT_BASELINE_COMMIT: `891e4bd4b999eacc99431ed0db05062901a68dd9`
- RELATION: `INDEPENDENT_PARALLEL_RUN`
- ORDERING: `NONE`
- RUN IDs: `v0.1-R01` ... `v0.1-R10`

The run ID is not a model version or rank.

## Purpose

Use the same Byul research memory and BYUL CORE-A to obtain independent reconstructions and model/representation proposals. Do not assume the existing v0.1 implementation is correct. The objective is to observe natural convergence, meaningful divergence, better prior-art alternatives, and useful reframings.

## Common Input — Phase 1 Blind

Read from the exact baseline commit:

1. `versions/v0.01/CURRENT_STATUS.md`
2. `versions/v0.01/memory/00_CHANNEL_AND_METHOD.md`
3. `versions/v0.01/memory/01_OWNER_WORLDVIEW_CURRENT.md`
4. `versions/v0.01/memory/02_CAUSAL_SET_LEARNING.md`
5. `versions/v0.01/memory/03_MODEL_FAMILY_AND_COMPLEMENTARITY.md`
6. `versions/v0.01/memory/04_ROUTING_AND_LIFECYCLE.md`
7. `versions/v0.01/memory/05_SIMULATION_AND_COMMITTEE.md`
8. `versions/v0.01/memory/06_MI1_INITIALIZATION_TARGET.md`
9. `versions/v0.01/memory/07_OPEN_QUESTIONS_AND_NEXT_JOBS.md`
10. `versions/v0.01/memory/08_CHANNEL_CHRONOLOGY.md`
11. `versions/v0.01/memory/09_VERSION_POLICY.md`
12. `versions/v0.01/memory/10_ACTIVE_CHANNEL_LOG.md`
13. `versions/v0.01/memory/11_CORE_PRINCIPLES.md`
14. `versions/v0.01/memory/12_PARALLEL_PROPOSAL_ROUND1.md`

### Phase-1 Blindness Rule

Do **not** read `versions/v0.1/` implementation files before freezing the Phase-1 proposal.

The point is to prevent anchoring on the current executable slice.

## Common Research Constraints

- PRIOR-ART-FIRST.
- Do not invent a new theory unless a real gap remains after examining known formalisms.
- Preserve `UNKNOWN`, `OPEN`, competing hypotheses, and non-conclusions.
- Separate source-supported state from your inference.
- BYUL CORE-A is a high-level modeling constraint, not a claim of proven physics.
- Do not treat Buddhism, quantum mechanics, Causal Set Theory, Petri Nets, or any other formalism as proof of the worldview.
- Current Petri/Event/Causal/LTS candidates are references, not answers.
- A single universal model is not required.
- You may recommend KEEP / MODIFY / REPLACE / HYBRID / REFRAME / INSUFFICIENT_EVIDENCE.
- Explicitly state what your proposal cannot preserve or reconstruct.
- Do not silently turn derived reconstruction into ground data.

## Research Question

Design the strongest implementable representation/model architecture you can justify for Byul's current research problem:

> How should evolving research memory/state be represented, composed, transformed, routed, reconstructed, and evaluated while preserving the meanings that must not be lost and remaining compatible with BYUL CORE-A?

You are free to reject the current framing if a better formulation is justified.

## Cohorts

### Neutral Blind — R01 to R06

All six receive exactly the same instructions. No extra solution pressure is added.

Goal: observe natural convergence/divergence from the same state.

### Alternative Search — R07 to R10

All common instructions remain. Apply only the additional pressure assigned below.

- `R07 — OUTSIDE_PRIOR_ART_SEARCH`: actively look beyond the currently discussed Petri/Event/Causal/LTS family for established formalisms or representation strategies that may fit better.
- `R08 — ADVERSARIAL_REFRAME`: try to falsify the current problem decomposition, `R(S,M,L)`, multi-model routing, and current assumptions. Propose a simpler or fundamentally different framing if justified.
- `R09 — MINIMAL_INFORMATION`: seek the smallest representation/algebra sufficient to preserve required semantics. Treat unnecessary state, objecthood, indexing, and model multiplicity as costs to be justified.
- `R10 — LIFECYCLE_COMPOSITION`: optimize for long-lived mutation, composition, split/merge, migration, recovery, reversibility, and bounded invalidation. Challenge any design that works only as a static snapshot.

Alternative pressure is not an instruction to reach a predetermined answer.

## Phase 1 Required Work

1. Reconstruct the current research state in your own words.
2. Separate:
   - `SOURCE_SUPPORTED`
   - `WORKING_HYPOTHESIS`
   - `OWNER_DIRECTION`
   - `OPEN`
   - `NON_CONCLUSION`
   - `YOUR_INFERENCE`
3. Identify the minimal problem that an implementation actually needs to solve.
4. Propose your best architecture/formalism/model family.
5. Explain why it is preferable to plausible alternatives.
6. Specify authoritative data vs derived views.
7. Specify transformation/reconstruction boundaries.
8. Specify lifecycle behavior.
9. Specify failure modes and falsification tests.
10. Freeze the proposal as `PHASE1_FROZEN` before Phase 2.

## Phase 2 — Current v0.1 Contrast

Only after `PHASE1_FROZEN`, read:

- `versions/v0.1/README.md`
- `versions/v0.1/MODEL_CONTRACT.md`
- `versions/v0.1/data/SOURCE_MANIFEST.md`
- `versions/v0.1/src/byul_v01.py`
- `versions/v0.1/tests/test_byul_v01.py`

Then compare the frozen independent proposal against the current implementation.

Choose one disposition:

- `KEEP_CURRENT`
- `MODIFY_CURRENT`
- `REPLACE_CURRENT`
- `HYBRID_MULTI_MODEL`
- `REFRAME_PROBLEM`
- `INSUFFICIENT_EVIDENCE`

Do not rewrite Phase 1 after seeing v0.1. Record deltas separately.

## Required Return Schema

Return exactly one `[RETURN PACKET]` Markdown fenced code block and no text after it.

The packet must contain:

- `ROUND_ID`
- `RUN_ID`
- `COHORT`
- `PROFILE`
- `BASELINE_COMMIT`
- `PHASE1_FROZEN = TRUE/FALSE`
- `CURRENT_STATE_RECONSTRUCTION`
- `STATE_CLASSIFICATION`
- `MINIMAL_PROBLEM_DEFINITION`
- `PHASE1_PROPOSAL`
- `PRIOR_ART_BASIS`
- `AUTHORITATIVE_REPRESENTATION`
- `DERIVED_REPRESENTATIONS`
- `PRESERVATION_CONTRACT`
- `LOSS_AND_NON_RECOVERABLE`
- `TRANSFORMATION_PATHS`
- `LIFECYCLE_BEHAVIOR`
- `ROUTING_POSITION`
- `BYUL_CORE_A_ALIGNMENT`
- `EXPECTED_FAILURE_MODES`
- `FALSIFICATION_TESTS`
- `IMPLEMENTATION_TEST_PLAN`
- `OPEN_UNKNOWNS`
- `WHY_THIS_COULD_BE_WRONG`
- `PHASE2_CURRENT_V0_1_COMPARISON`
- `DISPOSITION`
- `MATERIAL_DELTAS_FROM_CURRENT`
- `TOP_3_REASONS`
- `CONFIDENCE = LOW/MEDIUM/HIGH` with explanation

## Prohibited Behaviors

- Reading other run outputs before submitting your own.
- Claiming scientific/validation PASS.
- Treating current v0.1 as canonical.
- Hiding semantic loss.
- Filling missing evidence with invented certainty.
- Conflating an implementation convenience with a worldview truth.
- Replacing prior-art search with unnecessary theory invention.

## Owner/ASA Evaluation Boundary

Run authors do not rank themselves or other runs. Owner + ASA will blind-normalize and evaluate submissions afterward. Minority proposals with unique explanatory value must not be discarded merely for lack of consensus.

## Recommended Run Allocation

- R01–R06: `NEUTRAL_BLIND`
- R07: `OUTSIDE_PRIOR_ART_SEARCH`
- R08: `ADVERSARIAL_REFRAME`
- R09: `MINIMAL_INFORMATION`
- R10: `LIFECYCLE_COMPOSITION`

작성시각: 2026-08-22 03:37 KST
