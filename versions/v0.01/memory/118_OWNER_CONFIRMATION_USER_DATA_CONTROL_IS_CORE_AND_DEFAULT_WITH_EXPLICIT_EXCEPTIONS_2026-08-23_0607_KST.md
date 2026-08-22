# 118. Owner confirmation — User data control is core and default, with explicit exceptions

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / DATA-GOVERNANCE CORE CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:07 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "당연하죠 괜히 모델링을 이제까지 찾겠습니까요 ㅋㅋ
> 다른 프로젝트 같으면 대충 디비에 때려넣던가 했겠지요.
> 핵심 오브 핵심입니다.
>
> 네 맞습니다."

## Scope

`ASA INIT / DATA GOVERNANCE / USER AUTHORITY`

The Owner confirms the immediately preceding scoped proposition:

- the user should have primary/default authority over their own Persona/experience/legacy source data;
- user-facing controls should include at least visibility/use control, reset, and deletion as conceptually distinct operations;
- explicit exceptions may exist for legal retention, security, safety, contractual, system-integrity, or similar requirements;
- those exceptions should be modeled explicitly rather than silently overriding user control.

## High-fidelity interpretation

The Owner treats data governance as a **core-of-core reason for doing the model research at all**, not as a later database implementation detail.

A conventional application could simply store records in a database and add access/deletion flags. ASA/BYUL instead needs a richer model because data participates in Persona/View formation and evolution through relations such as:

```text
source exists
    !=
source is visible to this View
    !=
source is active in current Persona projection
    !=
source is retained as legacy/lineage
    !=
source is reset from active use
    !=
source is deleted
```

These distinctions affect:

- Persona formation;
- View selection and abstraction;
- lineage and reconstructability;
- later reinterpretation;
- user autonomy;
- legal/privacy compliance;
- derived state invalidation and recomputation.

## Design consequence

User authority should be treated as a first-class relation/policy dimension in the data model rather than a UI-only setting.

The architecture should be able to express, for a piece/set of source data or relation bundle:

- who may see it;
- which Views may use it;
- whether it may participate in current Persona formation;
- whether it remains retained as historical/legacy source;
- whether it is reset/hidden/archived/deleted;
- which explicit exception or legal basis, if any, constrains user authority.

No fixed legal schema, storage engine, permission model, or jurisdiction-specific policy is selected here.

## Important guards

Do not infer:

`USER CONTROL DEFAULT -> USER CAN OVERRIDE EVERY LEGAL OR SECURITY REQUIREMENT`.

Do not infer:

`EXPLICIT EXCEPTIONS -> SYSTEM MAY SILENTLY IGNORE USER CHOICE`.

Do not infer:

`DATA GOVERNANCE CORE -> EVERYTHING MUST BE STORED FOREVER`.

Do not infer:

`DATABASE IMPLEMENTATION -> CONCEPTUAL DATA LIFECYCLE IS FULLY SOLVED`.

## Research consequence

A high-value next question is not whether user control is important; that is now confirmed.

A sharper implementation/data-model issue is **dependency propagation**:

> if a user hides, resets, or deletes a source relation that previously contributed to a derived/common/Persona View result, how should dependent derived states be invalidated, recomputed, retained as historical evidence, or made inaccessible?

This should be asked under scope `ASA INIT / DATA GOVERNANCE / DERIVED DEPENDENCY`, because it directly connects user authority with View provenance, caching/materialization, and Persona evolution.
