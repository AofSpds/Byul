# 90. Owner clarification — Purpose arises with a person relation-bundle and may select a View

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:55 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "목적은 사람이라고 부르는 또다른 관계다발이 필요해서 어떤 VIEW를 선택해서 쓸수는 있겠습니다."

## High-fidelity interpretation

The Owner clarifies that `Purpose` should not currently be treated as an intrinsic defining property of VIEW.

Current intuition:

- `person` is itself another relation bundle under the relation-first hypothesis;
- a purpose/need may arise in or be associated with that person relation-bundle;
- given such a purpose, that relation-bundle may select or use a VIEW that is useful for the purpose;
- therefore a VIEW can in principle exist independently of a specific current purpose and later be selected/reused under different purposes;
- purpose-to-View linkage is itself naturally representable as a relation or relation bundle rather than as a fixed field inside a View object.

Conceptually:

```text
Person relation-bundle H
      + Purpose / Need P
             |
             +-- selects / uses --> View V

View V
  need not be ontologically defined by P
```

## Important nuance

Do not infer:

`PURPOSE BELONGS ONLY TO HUMANS`.

The Owner used `person` as the present explanatory relation-bundle. Whether other agent/persona/system relation-bundles can instantiate analogous purpose relations remains open.

Do not infer:

`PERSON HAS PURPOSE -> PURPOSE IS A FIXED PROPERTY OF PERSON`.

Under the broader hypothesis, person, purpose, selection, and View may all vary through time and context.

Do not infer:

`VIEW INDEPENDENT OF PURPOSE -> PURPOSE NEVER SHAPES VIEW`.

A purpose may influence View selection, View construction, routing, scope, resolution, evaluation, or revision even if purpose is not constitutive of View-ness.

## Research consequence

The previous binary question `does VIEW require Purpose?` should currently resolve toward:

```text
PURPOSE_IS_REQUIRED_FOR_VIEW_EXISTENCE = NOT ASSUMED
PURPOSE_CAN_SELECT_OR_CONDITION_VIEW_USE = YES / CURRENT HYPOTHESIS
```

A useful next research axis is to examine how the selecting relation is represented and how View choice changes when the person/purpose relation bundle changes over time, without prematurely fixing a selector architecture or utility function.
