# 101. Owner confirmation — VIEW performance includes source reconstructability / distinction preservation

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / PERFORMANCE-AXIS CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:24 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "솔직히 중요한 고민이네요. VIEW의 성능중에 많은 항목이 있지만, 이것저것들여다 보니 재현성이 중요하긴 합니다. VIEW의 성능항목중 중요한 부분이겠어요.
>
> {1,2,3...........} 이런걸 넣었는데 타겟이 계속 ASA만 나오면 재현이 안되잖어요."

## High-fidelity interpretation

The Owner identifies **reconstructability / distinction preservation** as an important VIEW performance dimension.

The Korean word `재현성` here is being used in a source-recovery sense rather than merely experimental repeatability.

Example:

```text
1 -> ASA
2 -> ASA
3 -> ASA
...
```

If many distinct source states collapse to the same target representation, the target no longer preserves enough distinction to infer/reconstruct which source state produced it.

This is a many-to-one abstraction and may have low reconstructability at that resolution.

## Important nuance

This does **not** mean every good VIEW must be lossless or invertible.

A low-resolution VIEW may intentionally collapse distinctions. For some purposes that is exactly what makes it useful.

Therefore VIEW performance should be evaluated relative to the View's declared/operational scope, resolution, and use context.

A more precise candidate distinction is:

```text
REPEATABILITY / DETERMINISM
= same operational conditions -> same output behavior

SOURCE RECONSTRUCTABILITY / DISTINCTION PRESERVATION
= how much of the relevant source distinctions can be recovered or traced from the View output
```

The Owner's example is primarily about the second axis.

## Candidate performance interpretation

A View may be assessed by questions such as:

- which source distinctions are preserved?
- which are intentionally collapsed?
- can an output be traced back to candidate source relations?
- how ambiguous is reverse reconstruction?
- under what scope/resolution is reconstruction expected?
- does increased resolution improve reconstruction when needed?

These are candidate evaluation axes only, not a frozen metric set.

## Guard

Do not infer:

`GOOD VIEW -> LOSSLESS BIJECTION`.

Do not infer:

`MANY-TO-ONE VIEW -> BAD VIEW`.

Do not infer:

`RECONSTRUCTABILITY -> COMPLETE REALITY RECOVERY`.

The project already assumes reality cannot be fully represented. Reconstruction is therefore always relative to a chosen View/scope/resolution and the distinctions that View aims to preserve.

## Research consequence

VIEW performance should likely separate at least:

1. usefulness for the active purpose/use;
2. distinction/information preservation;
3. reverse reconstructability / traceability;
4. stability/repeatability where relevant;
5. cost/complexity/resolution tradeoff.

The current Owner clarification elevates reconstructability/distinction preservation as an important performance axis, not as the sole criterion for VIEW-ness.
