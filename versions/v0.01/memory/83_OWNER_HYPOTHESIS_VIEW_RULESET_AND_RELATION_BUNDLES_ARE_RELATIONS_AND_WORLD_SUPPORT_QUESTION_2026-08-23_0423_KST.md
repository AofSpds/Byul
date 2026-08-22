# 83. Owner hypothesis — View/Ruleset may themselves be relations; relation bundles may have object-like properties

```text
STATUS = OWNER_WORLDVIEW_ORAL_STATEMENT / CURRENT WORKING HYPOTHESIS / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:23 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statements

> "네 맞습니다. 룰셋도 VIEW도 그냥 관계의 일종이 아닐까요. 아 재밋는 질문인데 일단 제 직관은 그렇습니다. 모든 관계와 관계다발은 굳이 말하자면 객체처럼 속성이 있다는 그런 느낌이지요."

> "우리가 어떤 관계를 어떻게 지원해야 세상을 구현할수 있을지가 궁금하긴 합니다."

## High-fidelity interpretation

The Owner's current intuition goes one level deeper than the previous relation-centric correction.

The current working hypothesis is that:

- View need not be an external meta-object outside the relation world;
- Ruleset need not be an external meta-object outside the relation world;
- both may themselves be representable as relations or relation bundles;
- a relation bundle may itself participate in higher-level relations;
- relations and relation bundles may have object-like attributes/properties in an implementation sense without requiring object-first ontology.

Conceptually:

```text
relation r1
relation r2
relation r3
   -> bundle B

B may itself enter another relation r4

View V may itself be represented as a relation / relation bundle
Ruleset S may itself be represented as a relation / relation bundle
```

This suggests a potentially recursive/reflective relation model in which the distinction between `data relation`, `View`, `Ruleset`, `Persona bundle`, and `organization` may be a role distinction under context rather than a permanently separate ontology class.

## Important nuance

The Owner says `굳이 말하자면 객체처럼 속성이 있다` as an intuition.

Do not overread this into either extreme:

- `everything must be encoded only as pure binary edges with no metadata`;
- `relations are secretly ordinary objects after all`.

The implementation question remains open: object-like properties may be supported through first-class relation records, metadata, relations-about-relations, hyperrelations, qualified relations, or another prior-art-grounded mechanism.

## New central research question

The Owner explicitly raises:

> **What kinds of relations, and what relation capabilities, must the system support in order to implement enough of the world for ASA Persona Orchestration?**

This reframes the research target from defining a universal object schema to discovering a sufficiently expressive but practical relation substrate.

Candidate capability questions to investigate empirically/prior-art-first include:

- can a relation target/qualify another relation or relation bundle?
- must n-ary / hyper-relations be first-class?
- how are roles/endpoints expressed without freezing object identity?
- how are time, succession, validity, and lifecycle represented when lifecycle is View-conditioned?
- how are composition and recursive abstraction represented?
- how are provenance/evidence/conflict/uncertainty represented?
- how can a View/Ruleset itself be expressed, applied, revised, and related to other Views/Rulesets?
- how much structure is required before practical world domains such as contract/asset/schedule/fitness can be represented without domain-specific object ontologies taking over the core?

These are research candidates only, not an approved relation algebra or implementation contract.

## Current concise hypothesis

```text
RELATION = CURRENT PRIMITIVE/MINIMAL MODELING CANDIDATE
VIEW ≈ RELATION / RELATION BUNDLE (OWNER INTUITION)
RULESET ≈ RELATION / RELATION BUNDLE (OWNER INTUITION)
RELATION BUNDLE MAY PARTICIPATE IN HIGHER RELATIONS
OBJECT-LIKE PROPERTIES OF RELATIONS/BUNDLES = IMPLEMENTATION POSSIBILITY, NOT OBJECT-FIRST ONTOLOGY
```

## Guard

Do not infer a final universal relation ontology, one canonical graph model, one canonical rule language, or one mandatory persistence representation from this note.

PRIOR-ART-FIRST remains active: the next design step should compare existing relation/graph/hypergraph/category/event/rule formalisms before inventing a new algebra.
