# 117. Owner confirmation — Reset and data deletion should be distinct; legal governance may apply

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / DATA-GOVERNANCE CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:05 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 지금은 별도 선택으로 해야 될듯 합니다. 
> 이건 아마 법적인 문제도 결부될수 있을듯합니다."

## Scope

`ASA INIT / DATA GOVERNANCE / RESET + DELETE`

## High-fidelity interpretation

The Owner confirms that, for the current design direction, user-facing `reset` and actual data deletion should be treated as distinct choices rather than collapsed into one operation.

Conceptually:

- Persona/View reset may change the active Persona projection, Seed configuration, visibility, source-selection policy, or current runtime state without necessarily deleting retained historical data;
- data deletion is a separate lifecycle/governance operation affecting retained source/legacy data itself;
- legal/privacy/compliance obligations may influence retention, deletion, access, reset, backup, audit, consent, and related lifecycle semantics;
- therefore data lifecycle semantics should not be defined only from technical convenience.

## Important distinction

```text
RESET
!=
DELETE
```

and potentially:

```text
inactive / hidden from current View
!=
archived
!=
retained as lineage/source
!=
logically deleted
!=
physically deleted
```

The exact legal semantics are not resolved by this note and will depend on jurisdiction, data class, user role, contract, service architecture, and applicable law/policy.

## Guard

Do not infer:

`LEGAL ISSUE MAY APPLY -> ONE UNIVERSAL LEGAL POLICY IS ALREADY KNOWN`.

Do not infer:

`USER RESET -> LEGAL DELETION REQUEST`.

Do not infer:

`DEFAULT LEGACY RETENTION -> RETENTION IS ALWAYS LEGALLY OR CONTRACTUALLY PERMITTED`.

Do not infer:

`PHYSICAL DELETION -> IMMEDIATE ERASURE FROM EVERY BACKUP / LOG / EXTERNAL PROCESSOR`.

Those are implementation/legal questions requiring later explicit review.

## Design consequence

The architecture should preserve enough separation between:

1. active Persona/View state;
2. source visibility/admissibility;
3. retained historical/legacy data;
4. deletion state;
5. audit/provenance state;
6. external or legally constrained copies/records;

so that later legal/privacy requirements can be mapped onto the system without forcing a redesign of the conceptual Persona/View model.

## Research consequence

The next useful question should move away from `should reset and delete be separate?` because that is now tentatively YES.

A sharper issue is user authority over legacy data: which operations should be directly user-controlled versus constrained by safety, contractual, legal-retention, or system-integrity requirements.

This should be asked under scope `ASA INIT / DATA GOVERNANCE / USER AUTHORITY`, while keeping legal specifics open for later jurisdiction-specific review.
