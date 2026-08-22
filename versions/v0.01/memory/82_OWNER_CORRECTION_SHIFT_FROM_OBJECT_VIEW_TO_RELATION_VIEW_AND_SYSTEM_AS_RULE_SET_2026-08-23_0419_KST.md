# 82. Owner correction — Shift discussion from object-centric View to relation-centric View; system as a rule set

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

## Owner statements

> "저는 시스템 개발자입니다. 시스템은 룰의 집합이라고 봐요."

> "객체 뷰에서 관계 뷰로 바꿔서 이야기하는게 맞을거예요."

## Correction to current framing

The Owner asks that discussion move away from object-centric language where a persistent object is assumed first and Views are treated as properties/interpretations attached to that object.

The preferred current framing is **relation-centric**:

- relation is the current primitive/minimal modeling candidate;
- a View is a rule/criterion/method for selecting, composing, grouping, projecting, or interpreting relations;
- apparent objects, Personas, roles, organizations, purposes, lifecycle states, etc. may be outputs/projections under a View rather than ontologically prior fixed objects;
- a system is understood pragmatically as a **set of rules** that governs how such relations are interpreted/combined/acted upon.

Conceptually:

```text
RELATIONS
   + RULE SET / VIEW
   -> derived relation bundle / Persona / role / organization / lifecycle interpretation
```

rather than:

```text
OBJECT
   + VIEW PROPERTY
   -> interpretation of that already-fixed object
```

## Consequence for persistence questions

The previous question `should View be stored separately from the event/object?` was object-centric and may be malformed under this hypothesis.

A better direction is to ask what relation history and rule/View context are necessary to reproduce or re-derive a useful projection when needed, without presuming a persistent View object or persistent object substrate.

## Lifecycle implication

Lifecycle remains View-conditioned. Under a relation-centric model, lifecycle is better treated as a rule/View-dependent projection over changing relations than as an intrinsic lifecycle property of a fixed object.

## Guards

Do not infer:

`SYSTEM = RULE SET -> ALL RULES ARE STATIC`.

Do not infer:

`RELATION-CENTRIC -> OBJECTS ARE FORBIDDEN`.

Objects may remain useful derived Views/abstractions.

Do not infer:

`VIEW = RULE SET -> ONE CANONICAL RULE LANGUAGE IS FIXED`.

No canonical rule grammar, relation schema, View operator, persistence model, or lifecycle engine is established by this note.
