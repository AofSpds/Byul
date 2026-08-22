# 86. Owner major current hypothesis — View identity requires declared scope and temporal abstraction

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:38 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "VIEW 의 속성을 정의해야합니다. 애초에 같다는게 없다는 관점이라서 (물론 여러 학설을 접하고 나니 이건 그냥 현행 가설중 하나) 시간의 흐름을 일정 스코프에서 무시하는 가설이어야 같은 VIEW라는게 가능하지요."

## High-fidelity interpretation

The Owner corrects the previous question `same relations + same View -> same result?` because the phrase `same View` already assumes an identity/equivalence notion that the current hypothesis does not grant globally.

Current major hypothesis:

- absolute sameness is not assumed;
- `same/different` remains View-conditioned rather than globally privileged;
- therefore `same View` must be operationally defined by the View's own declared properties / scope / equivalence assumptions;
- one way a View can remain operationally `the same` across time is by deliberately ignoring temporal change inside some declared scope;
- this is an abstraction decision, not a claim that time literally stopped or that the underlying relations are ontologically identical.

Conceptually:

```text
underlying relation field changes through time
R(t0) -> R(t1) -> R(t2)

View V declares a scope S
and intentionally treats some temporal differences as irrelevant within S

then V(t0), V(t1), V(t2)
may be treated as the "same View"
for the purpose of that scope
```

Thus:

```text
SAME_VIEW
    != ABSOLUTE IDENTITY

SAME_VIEW
    ~= EQUIVALENCE UNDER A DECLARED VIEW/SCOPE
```

## View-property implication

The Owner explicitly states that the properties of `VIEW` now need to be studied/defined.

Candidate property dimensions to investigate, without freezing them as architecture, include:

- scope / boundary: what relations and contexts are included;
- resolution: what detail is represented or collapsed;
- routing/composition rule: how relations/bundles are selected and combined;
- temporal treatment: which temporal changes are represented, ignored, bucketed, or abstracted;
- equivalence/invariance assumption: which differences are intentionally treated as `same enough` for the View;
- purpose/use context: what the View is for;
- lifecycle interpretation: how appearance, persistence, mutation, succession, and disappearance are projected under that View.

These are candidate research axes only.

## Important nuance

The Owner explicitly qualifies the `there is no same` stance as a **current hypothesis**, not a final doctrine, after encountering multiple competing theories.

Do not infer:

`NO ABSOLUTE SAMENESS ASSUMED -> NOTHING CAN EVER BE COMPARED`.

Operational equivalence can be defined under a declared View/scope.

Do not infer:

`SAME VIEW REQUIRES IGNORING TIME -> ALL VIEWS MUST IGNORE TIME`.

A View may instead represent temporal change explicitly. The point is that any persistence/identity claim must state what temporal distinctions it preserves or abstracts away.

Do not infer:

`VIEW PROPERTIES NEED DEFINITION -> ONE UNIVERSAL VIEW SCHEMA IS ALREADY FIXED`.

No canonical View identity rule, temporal model, equivalence relation, scope grammar, or persistence contract is fixed by this note.

## Research consequence

A sharper next research question is:

> **What must a View declare about scope, resolution, temporal treatment, and equivalence/invariance so that its outputs can be interpreted and compared without smuggling in an absolute notion of sameness?**

This should be studied PRIOR-ART-FIRST against temporal databases, bitemporal models, event/process models, observational equivalence, quotient/abstraction methods, graph/query views, and compositional formalisms before inventing a canonical View schema.
