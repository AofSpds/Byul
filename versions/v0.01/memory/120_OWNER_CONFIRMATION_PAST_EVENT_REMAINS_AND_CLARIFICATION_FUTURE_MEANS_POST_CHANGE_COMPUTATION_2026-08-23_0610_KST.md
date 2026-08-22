# 120. Owner confirmation — Past event remains; clarify future as post-change computation, not literal future prediction

```text
STATUS = OWNER_CONFIRMATION / TERMINOLOGY-CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:10 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 맞습니다. 미래는 근데 어떻게 계산하나요"

## Scope

`ASA INIT / DATA GOVERNANCE / HISTORICAL SEMANTICS + FUTURE TERMINOLOGY`

## Confirmed point

The Owner confirms the immediately preceding conceptual proposition:

- a past Persona judgment/action that actually occurred remains a historical event in the model;
- deleting one of its former Source inputs does not rewrite the fact that the past event occurred;
- current/future active Persona state should instead be recomputed without the deleted Source.

## Clarification — what `future` means here

The word `future` should not be read as "the system calculates future events in advance."

The intended distinction is:

```text
PAST EVENT
= already occurred historical event; preserve as history/lineage subject to later legal/data-policy handling

CURRENT ACTIVE STATE
= invalidate/recompute affected derived states now

FUTURE COMPUTATION
= any Persona/View projection, decision, response, or state computed after the deletion should use the new admissible Source set that excludes the deleted Source
```

Therefore:

```text
Before deletion:
Source {A,B,C} -> View -> Persona/output

Delete C at time t

At/after t:
Source {A,B} -> View -> recomputed current Persona

Later at t+1, t+2, ...:
new incoming relations + retained admissible Source {A,B,...}
    -> View as it exists then
    -> later Persona/output
```

No literal future state is required to exist beforehand.

## Precomputed/materialized future projections

If the implementation has already materialized future-oriented artifacts such as plans, forecasts, scheduled recommendations, simulations, cached projections, or derived expectations that depended on deleted Source C, those artifacts are dependent derived state and should be considered for invalidation/recomputation under the same dependency policy.

This is an implementation consequence, not a claim that the future itself is computed.

## Guards

Do not infer:

`FUTURE PERSONA -> PRECOMPUTED FUTURE WORLD STATE`.

Do not infer:

`PAST EVENT PRESERVED -> DELETED SOURCE MUST REMAIN VISIBLE`.

Do not infer:

`CURRENT/FUTURE RECOMPUTATION -> HISTORICAL EVENT MUST BE REWRITTEN`.

Do not infer:

`HISTORICAL EVENT PRESERVED -> LEGAL RETENTION IS ALWAYS PERMITTED`.

## Research consequence

Future questions should use clearer wording such as `post-deletion computations` or `subsequent Persona/View states` rather than simply `future`, to avoid implying prediction or precomputation.
