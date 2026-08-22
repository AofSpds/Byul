# 81. Owner correction — Relation is the primitive; whether a View itself must be stored is not the core question

```text
STATUS = OWNER_WORLDVIEW_ORAL_STATEMENT / CORRECTION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:19 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "VIEW 잖아요. 그때 그때 다른데 우리의 PRIMITIVE는 원래 관계라 VIEW가 저장이 되어야 하는가는 맞는 질문인가 싶습니다. 당연히 물론 라이프싸이클은 뷰에 따라 다릅니다."

## Correction to the immediately preceding question

The previous question asked whether an event record and its interpretation under a View should be separately stored.

The Owner corrects the framing:

- in the current worldview hypothesis, the primitive is **relation**;
- View is the way relation bundles are interpreted/abstracted at a given time/purpose/context;
- therefore asking `must the View itself be stored?` may already assume too much about View as a persistent object;
- the more fundamental concern is how relations and their View-conditioned projections/lifecycles can be reconstructed, interpreted, or re-derived when needed.

## Current working distinction

```text
RELATION = primitive / foundational modeling unit candidate
VIEW = context/purpose-conditioned way of seeing/composing relation bundles
LIFECYCLE = View-conditioned
```

Therefore:

```text
STORE_VIEW_AS_OBJECT = NOT ESTABLISHED
VIEW_PERSISTENCE_REQUIREMENT = OPEN
```

Possible future implementations may preserve a View definition, reference, version, provenance, or materialized projection when useful for reproducibility, audit, or continuity, but none of those is implied as a universal requirement by the worldview itself.

## Lifecycle implication

The same underlying relation bundle may have different lifecycle interpretations under different Views.

For example, one View may describe a relation bundle as:

- created -> active -> retired

while another View over the same or overlapping relations may describe:

- split -> succeeded -> merged

or another lifecycle entirely.

Thus lifecycle should not be treated as one globally intrinsic property of a Persona/Object/Relation bundle unless separately justified.

## Important guards

Do not infer:

`VIEW_CHANGES -> VIEW_MUST_BE_PERSISTED_AS_A FIRST-CLASS OBJECT`.

Do not infer:

`RELATION_PRIMITIVE -> VIEW_IS UNIMPORTANT`.

Do not infer:

`LIFECYCLE_VIEW_DEPENDENT -> HISTORY CAN BE REWRITTEN`.

Do not infer:

`RELATION_PRIMITIVE -> ONE FIXED RELATION TYPE OR GLOBAL RESOLUTION`.

## Research consequence

A better future question is not simply:

> "Do we store the View?"

but:

> **What minimal information must be preserved so that a past or current View-conditioned relation/lifecycle can be reproduced, audited, or re-derived when that is required?**

The answer may differ by View and purpose.

No canonical persistence schema, materialized-view strategy, lifecycle ontology, or provenance contract is fixed by this note.
