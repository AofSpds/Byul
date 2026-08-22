# 37. Owner Clarification — SPLIT / MERGE are derived views, not required primitives

```text
STATUS = OWNER_CLARIFICATION / BYUL_CORE_CONCEPT_RECONFIRMATION
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-22 23:41 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

During Joplin candidate discussion, the Owner explicitly reconfirmed:

> "BYUL의 기본컨셉이 후자입니다."

The referenced contrast was:

1. `SPLIT` / `MERGE` as explicit world primitives or mandatory operations, versus
2. recording lower-level local transition / predecessor-successor / relation / lineage first, and treating `SPLIT`, `MERGE`, `FORK`, `SUCCESSION`, etc. as higher-level derived views/interpretations when supported by the observed relation/history structure.

Owner confirms **the latter is already a basic BYUL concept**.

## Interpretation for the current pilot discussion

This is not a newly discovered architectural direction from Joplin. Joplin is valuable insofar as it can empirically pressure-test this already-adopted BYUL direction.

The pilot should therefore ask whether a candidate can:

- preserve local transitions / relation / lineage without requiring an invented explicit `SPLIT` event;
- recognize retrospective divergence from shared predecessor/history when evidence supports it;
- preserve `UNKNOWN` where exact divergence timing or relation cannot be proven;
- derive higher-level lifecycle views without silently rewriting lower-level evidence;
- distinguish graph/topological convergence from semantically admissible merge.

## Important semantic caution

`A -> C` and `B -> C` may support a topological/convergence view, but this alone does not prove that `C` is a semantically correct merge of A and B. Semantic merge requires separate preservation/admissibility evidence and may validly resolve to `MERGE`, `CONFLICT`, `SAFE_REFUSAL`, or `UNKNOWN`.

## Alignment with existing BYUL principles

This clarification is consistent with existing adopted research principles in `11_CORE_PRINCIPLES.md`:

- NON-SUBSTANTIALITY / DERIVED ENTITY
- COMPOSITION / EMERGENCE
- local -> composed -> higher-scale view lineage preservation
- no automatic promotion of a convenient high-level representation into ultimate ontology

## Current consequence

For open-source candidate selection, Joplin should be evaluated as a **falsification workload for derived lifecycle interpretation**, not as a source of a new BYUL primitive design.

No implementation, freeze, canonical architecture promotion, or validation claim is created by this note.
