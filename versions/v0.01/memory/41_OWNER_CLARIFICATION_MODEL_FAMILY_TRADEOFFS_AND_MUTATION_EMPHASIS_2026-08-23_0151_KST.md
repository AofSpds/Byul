# 41. Owner Clarification — Model-family tradeoffs and mutation emphasis

```text
STATUS = OWNER_CLARIFICATION / RESEARCH_DIRECTION
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 01:51 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 아마 모든 모델이 각기 다 장단이 있을거예요. 그래시 mutating을 강조하고 있긴 해요"

## Interpretation

The Owner's emphasis on `mutating` is connected to an expectation that no single model/representation will dominate across all situations.

Working implications for BYUL research:

- different models may preserve different semantics and expose different strengths/weaknesses;
- model choice should not be assumed static or globally optimal;
- mutation should be studied not only as data/state mutation but also as **model/representation lifecycle mutation**;
- a model may need to adapt, compose with another representation, split, be partially replaced, migrate, degrade, recover, or yield to a successor;
- the empirical probe pool should therefore collect evidence about transition/mutation quality, semantic preservation, reconstruction, invalidation radius, and mutation cost—not only static task performance.

## Important guard

This does **not** establish that multi-model routing or model mutation is always necessary. The empirical program must be allowed to show that a simpler stable model plus views is sufficient for some or many workloads.

`MODEL_FAMILY_TRADEOFF_HYPOTHESIS != EMPIRICAL_REQUIREMENT`

## Alignment with existing BYUL research

This clarification is consistent with existing BYUL directions:

- Core Principle: CHANGE / MUTABILITY;
- model-family complementarity rather than premature universal-model lock-in;
- `R(S,M,L)` lifecycle context including mutate/compose/split/diverge/merge/migrate/degraded/recover/successor-retire;
- lifecycle evaluation dimensions such as semantic drift, mutation history preservation, invalidation radius, reversibility, and maintenance cost.

## Consequence for probe design

The discovery testbed should avoid being only a collection of static before/after tasks. As evidence accumulates, at least some probes should exercise **sequences of representation/model lifecycle change**, for example:

```text
INITIAL MODEL
  -> evidence accumulates
  -> mismatch/failure appears
  -> mutate or route representation
  -> preserve required semantics/history
  -> validate reconstruction/reversibility
  -> continue operation or create successor
```

The purpose is to discover when mutation is actually useful, what it costs, and what must survive the transition.

No architecture freeze, universal-model rejection, benchmark freeze, or production decision is created by this note.
