# 109. Owner confirmation — Persona runtime representation is purpose- and resource-conditioned

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / IMPLEMENTATION-CONSTRAINT CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:47 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "음 상황이나 목적에 따라 다를듯 하빈다. 일단 성능이나 메모리 데이터 크기가 중요할듯 합니다."

## High-fidelity interpretation

At scope `IMPLEMENTATION / PERSONA RUNTIME REPRESENTATION`, the Owner does not select one canonical representation such as always-materialized Persona state or always-on-demand reconstruction.

Current implementation intuition:

- the correct representation may vary by situation and purpose;
- runtime performance/latency is an important constraint;
- memory/data size is an important constraint;
- therefore Persona runtime representation may reasonably use different strategies under different operating conditions;
- a hybrid design is plausible: some Persona/View-derived state may be materialized or cached, while other state is recomputed from Source + View + context when needed;
- this implementation choice must not be promoted into the foundational Persona ontology.

Conceptually:

```text
Source + Persona View + Context
        |
        +-- dynamic reconstruction when cost is acceptable
        +-- cached/materialized projection when latency matters
        +-- selective precomputation for frequently used/high-cost portions
        +-- other purpose/resource-conditioned strategies
```

## Important distinction

Do not infer:

`PERSONA CONCEPT -> ONE STORAGE MODEL`.

Do not infer:

`MATERIALIZED PERSONA STATE -> PERSONA IS A FIXED OBJECT`.

Do not infer:

`DYNAMIC RECONSTRUCTION -> ALWAYS BETTER OR MORE FAITHFUL`.

Implementation strategy is a tradeoff among purpose, latency, compute cost, memory/storage footprint, update frequency, consistency/freshness requirements, and reconstruction cost.

## Research consequence

The implementation problem should be framed as an adaptive materialization/cache/reconstruction policy rather than a binary ontology choice.

Useful later evaluation axes include:

- latency to instantiate/use a Persona projection;
- memory/storage footprint;
- recomputation cost;
- freshness/staleness under changing Source/View;
- frequency of access;
- cost of invalidating or updating derived Persona state;
- fidelity to the current View configuration.

No canonical caching policy, materialized-view mechanism, event-sourcing design, or database architecture is selected by this note.
