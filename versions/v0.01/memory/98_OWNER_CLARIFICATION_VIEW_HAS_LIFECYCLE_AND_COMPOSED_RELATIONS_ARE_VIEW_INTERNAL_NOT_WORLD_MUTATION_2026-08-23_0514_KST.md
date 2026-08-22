# 98. Owner clarification — VIEW has lifecycle; composed relations are View-internal abstractions, not underlying-world mutation

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:14 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "derived 가 뭔가여 문맥상으로는 알겠는데 아 저 영어 약해여 ㅋㅋㅋ VIEW도 당연히 라이프싸이클이 있고 그 VIEW안에서는 그런데, 실제로 바뀔리가요."

## High-fidelity interpretation

The Owner clarifies the persistence semantics of View-conditioned composition.

- `derived relation` means a relation that is **derived / inferred / composed inside a View**, not a claim that the underlying world itself has been changed;
- a View itself has a lifecycle: it can arise, persist for some scope/time, change, and disappear;
- while a View is active, the View may treat a path or relation bundle as a higher-level composed relation;
- that composed relation is valid/visible **within the View and its lifecycle/scope**;
- applying or forming such a View does not by itself mutate the underlying relation world;
- actual world mutation would require a separate action/relation/process that changes the underlying relation network.

Conceptually:

```text
underlying relations:
A --r1--> B --r2--> C

View V, during its lifecycle:
A --r*--> C   # View-internal composed / derived relation

This does NOT imply:
underlying world is rewritten so that r* became an independent world-level relation.
```

## Terminology preference

For Owner-facing Korean discussion, prefer:

- `derived relation` -> `파생 관계`, `도출된 관계`, or `VIEW 내부 합성 관계`

Use English only when it adds precision and pair it with Korean on first use.

## Important guard

Do not infer:

`VIEW-INTERNAL COMPOSITION -> WORLD MUTATION`.

Do not infer:

`VIEW HAS LIFECYCLE -> VIEW OUTPUT MUST BE EPHEMERAL IN IMPLEMENTATION`.

An implementation may cache/materialize/store a View result for performance or audit, but that storage is still an implementation decision and not evidence that the underlying world relation changed.

Do not infer:

`VIEW LIFECYCLE -> ONE FIXED LIFECYCLE MODEL`.

Lifecycle semantics remain View-conditioned and open for research.

## Research consequence

The model should separate at least conceptually:

1. underlying relation-network change;
2. View lifecycle/change;
3. View-internal derived/composed relations;
4. implementation-side materialization/caching/persistence.

These planes may interact but should not be silently collapsed into one another.
