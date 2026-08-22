# 119. Owner confirmation — Source deletion requires derived-state recomputation for current/future Persona

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / DATA-GOVERNANCE DERIVED-DEPENDENCY CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:08 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "재계산이지요. 일단 그렇게 해야지요."

## Scope

`ASA INIT / DATA GOVERNANCE / DERIVED DEPENDENCY`

The Owner confirms the immediately preceding question:

> if a user deletes a Source datum/relation that previously contributed to common/intermediate View results, Persona View results, caches, or active Persona state, the current/future Persona should not continue using that deleted Source's derived influence; dependent states should be invalidated and recomputed without it.

## High-fidelity interpretation

Current design direction:

```text
Source E
  -> Common/Intermediate View result
  -> Persona View result
  -> active Persona state / judgment

user deletes Source E
  -> find dependent derived states
  -> invalidate affected results
  -> recompute from remaining admissible Source
  -> current/future Persona no longer uses E's influence
```

This is not merely deletion of the physical Source row/object. Because ASA/BYUL treats data as Source material for View/Persona formation, deletion has dependency consequences through the View pipeline.

## Important distinction

The Owner's confirmation currently applies to **current and future Persona behavior/state**.

It does not yet resolve what should happen to already-executed historical decisions, audit records, historical snapshots, or legal/compliance evidence that were validly produced before the deletion request.

Therefore keep separate:

```text
ACTIVE/FUTURE DERIVED STATE
-> recompute without deleted Source

HISTORICAL RECORD OF PAST STATE/ACTION
-> semantics still open; may require separate policy/legal treatment
```

## Design consequence

A practical architecture will likely need enough dependency/provenance information to determine which derived states depend on which Source relations, directly or indirectly.

Candidate implementation capabilities include:

- Source -> derived dependency tracking;
- invalidation of caches/materialized Views;
- selective recomputation rather than global rebuild when feasible;
- propagation across multi-stage View chains;
- version/freshness checks so stale pre-deletion results do not remain active;
- explicit distinction between active computed state and retained historical evidence.

These are implementation candidates, not a frozen mechanism.

## Guards

Do not infer:

`DELETE SOURCE -> RECOMPUTE ALL DATA GLOBALLY`.

Do not infer:

`RECOMPUTE CURRENT PERSONA -> ERASE ALL HISTORICAL RECORDS`.

Do not infer:

`SOURCE DELETE -> DERIVED STATE CAN NEVER BE RETAINED FOR LEGALLY REQUIRED AUDIT`.

Do not infer:

`DEPENDENCY TRACKING -> ONE SPECIFIC GRAPH DATABASE OR EVENT-SOURCING ARCHITECTURE`.

## Research consequence

A sharper next question is historical semantics after deletion:

> If a past Persona judgment/action was produced using Source E before E was deleted, should that historical event remain as an immutable past event marked with restricted/deleted provenance, or should the historical representation itself also be recomputed/rewritten?

This should be asked under explicit scope `ASA INIT / DATA GOVERNANCE / HISTORICAL SEMANTICS`, keeping legal requirements separate from current/future Persona recomputation.
