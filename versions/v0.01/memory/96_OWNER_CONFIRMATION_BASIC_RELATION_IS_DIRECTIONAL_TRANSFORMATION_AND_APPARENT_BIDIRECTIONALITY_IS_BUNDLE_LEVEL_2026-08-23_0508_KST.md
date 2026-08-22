# 96. Owner confirmation — Basic relation remains directional/transformation; apparent bidirectionality is bundle-level

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:08 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "관계는 기본적으로 방향이 있다고 생각하는 쪽이었는데, 그래서 관계 다발을 얘기했던거였어요. 양방향이 말이 안되어서 
>
> 그래도 아직 현행가설은 안바꿨습니다. 방향과 변환이 있다고 봅니다. 우리가 관계라고 부르는 것은 대부분 관계 다발이니까 여러 속성이 가능하다."

## High-fidelity interpretation

The Owner confirms that the current major hypothesis has **not changed** on the following point:

- a basic relation is directional;
- a basic relation is transformation/mapping-like rather than a symmetric undirected primitive;
- what appears in ordinary language as a rich or bidirectional relationship is usually better modeled as a **bundle of multiple directional relations**, possibly operating at different times, strengths, scopes, or semantic roles;
- this is one reason the project repeatedly uses `relation bundle` for practical-world constructs even while keeping `relation` as the lower-level worldview unit.

Conceptually:

```text
basic relation candidate:
S --r--> T

apparent two-way relationship:
A --r1--> B
B --r2--> A'
A' --r3--> B'
...

or another composed directional relation-bundle
```

The exact temporal/indexing notation remains open; the key current hypothesis is directional transformation rather than an ontologically symmetric edge.

## Important nuance

The Owner explicitly states this remains a **current hypothesis**, not a finalized ontology.

Do not infer:

`DIRECTIONAL RELATION -> EVERY PRACTICAL WORLD RELATION MUST BE STORED AS ONE SIMPLE EDGE`.

Practical relations are often bundles with many properties/behaviors and may be implemented through objects, records, graphs, hypergraphs, event logs, rules, or other abstractions.

Do not infer:

`NO PRIMITIVE BIDIRECTIONAL RELATION -> NO RECIPROCITY`.

Reciprocity / feedback / mutual influence may emerge from compositions of directional relations.

Do not infer:

`RELATION BUNDLE -> FIXED OBJECT`.

Relation bundles remain View-conditioned, composable abstractions.

## Research consequence

A sharper next question is composition semantics:

> if `A --r1--> B` and `B --r2--> C`, under what conditions may the system derive or treat `A --r*--> C` as a meaningful composed relation?

This should not be assumed automatic. Under the Owner's broader View hypothesis, whether and how such composition is meaningful may itself depend on View, scope, resolution, temporal treatment, and purpose/context.

No canonical category-theoretic composition rule, temporal algebra, graph closure rule, or relation calculus is fixed by this note.
