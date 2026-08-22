# 60. Owner worldview — Sameness of source and target is view-conditioned

```text
STATUS = OWNER_WORLDVIEW_ORAL_STATEMENT / INTERVIEW_MEMORY
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 02:49 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 소스가 같다고 타겟이 같은 경우가 있는지도 궁금하네요.
>
> 사실 같다는 것도 뷰에 따라 달라집니다"

## High-fidelity interpretation

- The Owner questions whether sameness on the source side implies or corresponds to sameness on the target side.
- `same` itself is not treated as an absolute, view-independent predicate.
- Therefore source identity/sameness and target identity/sameness should both be evaluated relative to an active view / relation / criterion.
- The same recorded source may be grouped as one source under one view and distinguished into multiple source identities under another; likewise targets may be collapsed or distinguished differently.
- No implication is established of the form:

```text
SOURCE_SAME -> TARGET_SAME
TARGET_SAME -> SOURCE_SAME
```

## Important guards

Do not infer:

`VIEW_CONDITIONED_SAMENESS -> NO PROVENANCE`

or

`VIEW_CONDITIONED_SAMENESS -> ALL IDENTITIES ARE ARBITRARY`.

A source can still have exact provenance/bytes/history at an implementation layer while the higher-level judgment that two sources or two targets are "the same" remains view-conditioned.

## Research implication

Potentially distinct questions should be kept separate:

1. exact evidence/provenance equality;
2. source sameness under a view;
3. target sameness under a view;
4. whether source/target roles themselves are view-conditioned;
5. whether a source and target may be considered the same entity/relationship under some view.

This may matter for reconstruction, lineage, merge/split interpretation, and identity testing.

## Interview implication

A useful next unresolved question is whether `source` and `target` are themselves fixed roles at the highest-resolution relation level, or whether the same underlying participant/change can be source in one view and target (or collapsed with the other end) in another view.

No identity algebra, equality operator, source/target ontology, or implementation rule is fixed by this note.
