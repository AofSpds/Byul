# 116. Owner confirmation — Data management is core; default legacy retention with user reset option

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / DATA-LIFECYCLE CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:02 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 그래서 DATA의 관리가 핵심이라고 생각했어요. 
>
> 사실 유져가 초기화를 바랄수도 있을거예요. 지금은 넣어주죠 뭐"

## Scope

`ASA INIT / DATA MANAGEMENT / LEGACY RETENTION + RESET`

## High-fidelity interpretation

The Owner confirms that **data management is a core architectural concern** for the ASA/BYUL concept because Persona/View evolution depends heavily on how prior experience, design states, memories, View states, loss/provenance information, and lineage remain available as future source material.

Current practical default:

- prior Seed/View/design/experience legacy should be retained as retrievable source material;
- inactive legacy need not remain active in the current Persona projection;
- retention supports lineage, later reinterpretation, higher-resolution fallback, and diverse future Persona manifestations;
- however, the user may explicitly want an initialization/reset operation;
- for now, reset capability should be included as a supported concept, but its exact semantics are not yet frozen.

## Important distinction

A user-facing `reset` is ambiguous and must not automatically be equated with physical data destruction.

Possible reset semantics include, for example:

```text
1. ACTIVE-PERSONA RESET
   -> clear/reseed current Persona/View projection while retaining source legacy

2. VIEW/CONFIG RESET
   -> restore selected Seed View/configuration while retaining historical source data

3. EXPERIENCE/MEMORY RESET
   -> stop using or remove selected accumulated experience from active source selection

4. HARD DATA RESET / DELETION
   -> actually delete selected or all retained source/legacy data
```

These are candidate semantics only. The Owner has not selected a canonical reset model.

## Core design consequence

Because the system is intentionally lineage-rich and View-driven, data lifecycle must distinguish at least conceptually between:

- `exists in retained source/legacy`;
- `visible to a particular View`;
- `active in the current Persona projection`;
- `archived/inactive`;
- `user-requested reset state`;
- `physically deleted`.

This distinction is especially important because a reset of current Persona behavior may be desirable without necessarily destroying the historical data that explains prior behavior and lineage.

## Guards

Do not infer:

`DEFAULT RETENTION -> USER CAN NEVER DELETE DATA`.

Do not infer:

`RESET -> DELETE EVERYTHING`.

Do not infer:

`LEGACY RETAINED -> LEGACY ALWAYS VISIBLE TO EVERY PERSONA VIEW`.

Do not infer:

`DATA MANAGEMENT IS CORE -> ONE STORAGE TECHNOLOGY OR SCHEMA IS ALREADY SELECTED`.

## Research consequence

A key next design problem is to define reset semantics separately from retention/deletion semantics under a clear user-control model.

The next scoped question should therefore ask whether the Owner conceptually distinguishes:

- resetting the active Persona/View state;
- resetting what historical data may participate as source;
- and permanently deleting retained data.

No retention duration, deletion policy, storage topology, consent UX, backup policy, or reset algorithm is fixed by this note.
