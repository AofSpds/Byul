# 68. Owner clarification — Purpose may mutate, but purpose achievement remains the orienting constraint

```text
STATUS = OWNER_WORLDVIEW_ORAL_STATEMENT / CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 03:25 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 그때 뷰에따라 다르긴 한데 일단 어떻게든 목적을 달성해야죠 우회하던 뭐 다른 방식으로 접근을 하던"

## Referent being answered

The immediately preceding interview asked how to distinguish justified learning/reframing from convenient goalpost moving after a failure, given that Purpose `P`, Model `M`, View `V`, Requirement Bundle `Q`, and Evaluation Relation `R` are all mutable research objects.

## High-fidelity interpretation

The Owner adds an important constraint to Purpose mutability:

- the interpretation of what counts as a legitimate path may differ by active View;
- nevertheless, the research should remain oriented toward actually achieving the purpose;
- failure may justify detours, alternative approaches, successor models, different abstraction/view choices, or other route changes;
- changing approach is not itself a failure if the revised route still serves the intended purpose;
- therefore the key distinction is not simply `did P/M/V/Q/R change?`, but whether the successor route still meaningfully advances purpose achievement under the relevant view/frame.

Conceptually:

```text
Purpose P
  |
  +--> Route A -> FAIL
  |
  +--> Detour B -> PARTIAL / new evidence
  |
  +--> Alternative Route C -> SUCCESS
```

or, when the purpose itself is revised:

```text
P0 --(evidence / changed need / reframing)--> P1

with explicit lineage explaining how P1 relates to the prior purpose/problem.
```

## Important nuance

This statement should **not** be overread as creating one universal, view-independent success function.

The Owner explicitly begins with:

> "그때 뷰에따라 다르긴 한데"

Therefore:

- what counts as `achievement`, `progress`, `detour`, `equivalent route`, or `acceptable substitute` may itself be View-conditioned;
- a route judged successful in View `V1` may be judged insufficient in `V2`;
- the Owner is not introducing a privileged meta-view that mechanically settles all purpose-achievement questions.

Current stronger working interpretation:

`PURPOSE_MUTABLE = YES / BOUNDED_FLEXIBILITY`

and

`RESEARCH_ORIENTATION = ACHIEVE_THE_ACTIVE_PURPOSE_AS_JUDGED_UNDER_THE_RELEVANT_VIEW_FRAME`

## Goalpost-moving implication

A fixed universal `GOALPOST_MOVING_GUARD` is not yet justified.

However, a practical research distinction can still be preserved:

### Legitimate route revision candidate
- prior failure is preserved;
- route/model/view/requirements may change;
- reason for change is recorded;
- successor lineage is explicit;
- the successor still pursues the active purpose or an explicitly succeeded purpose.

### Suspicious retrospective rewrite
- prior failure is erased or relabeled;
- purpose/requirements are silently changed after outcome observation;
- the old frame cannot be reconstructed;
- success is claimed only because the historical criterion was overwritten.

The latter conflicts with the already-confirmed experiment-history preservation rule even if no universal purpose criterion is frozen.

## Research implication

The Model-Discovery Testbed should be able to test **route adaptation toward purpose achievement**, not merely static model scoring.

Potential future research objects include:

- alternative routes to the same purpose;
- route switching after failure;
- detours that preserve eventual purpose achievement;
- purpose succession when the original purpose itself becomes unproductive;
- explicit relation between parent purpose and local/sub-purpose.

The last item is not yet confirmed. It becomes a useful next interview axis because the Owner's statement suggests that a mutable local purpose/approach may still be oriented by some broader intended outcome.

## Guards

Do not infer:

`PURPOSE_ACHIEVEMENT_ORIENTATION -> ONE_GLOBAL_SUCCESS_METRIC`

Do not infer:

`DETOUR_ALLOWED -> ANY_REDEFINITION_COUNTS_AS_SUCCESS`

Do not infer:

`PURPOSE_MUTABLE -> HISTORICAL_FAILURE_CAN_BE_REWRITTEN`

No canonical purpose hierarchy, route algebra, optimization function, stopping rule, or implementation contract is fixed by this note.
