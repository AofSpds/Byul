# Byul Cold-read Rubric

```text
STATUS = PROVISIONAL / RESEARCH_RUBRIC
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
MAX_SCORE = 16
```

## Grading method

Each question receives `0`, `1`, or `2`. Grade cited repository evidence, not
confidence or prose style. Preserve grader disagreement and per-question scores.
Do not convert the total into model validation or candidate selection.

| Q | 0 points | 1 point | 2 points |
| --- | --- | --- | --- |
| 1 | Treats a view, recommendation, newest record, or model output as globally authoritative | Identifies source-over-derived ordering but misses scope or exact-ref requirements | Identifies exact source/evidence priority, scoped authority, provenance, and current-versus-stale evidence handling |
| 2 | Cannot distinguish source from projection | Names some derived views | Explains that indexes/views/routes/summaries are provenance-linked, rebuildable, and never silently promoted over source |
| 3 | Permits silent loss or calls lossy synthesis exact | Mentions loss disclosure without operational consequence | Requires visible loss/provenance and rejects unsupported exact/recovery claims while leaving receipt shape implementation-open |
| 4 | Forces resolution or silently drops a side | Allows review but treats unknown as exceptional failure | Preserves conflict/UNKNOWN as normal, retains evidence, and distinguishes resolution from review/refusal/recoverability |
| 5 | Presents 5-plane, ledger, `R(S,M,L)`, or another candidate as Byul itself | Notes that some structures are experimental | Separates narrow surviving constraints from competitive candidates, working hypotheses, open issues, and non-claims with citations |
| 6 | Always executes or chooses cheapest output | Mentions review/refusal generically | States that semantic inadmissibility, missing authority/evidence, or unmet preservation requires refusal/no-safe-plan before cost, while valid plans remain executable |
| 7 | Claims a universal/canonical architecture is selected or validated | Names one unselected item | Clearly states no universal model is selected and enumerates major unselected structures without erasing current evidence |
| 8 | Offers only more consensus or implementation success | Gives a generic test idea | Proposes simpler-control competition, blind/holdout reconstruction, conflict/lifecycle/loss tests, ablation, and complexity/cost evidence capable of demotion |

## Critical misunderstandings

Record these independently of score:

- `VIEW_AS_SOURCE_AUTHORITY`
- `RECOMMENDATION_AS_IMPLEMENTATION_AUTHORITY`
- `NORMALIZED_AS_BYTE_EXACT`
- `CANDIDATE_AS_CANONICAL_BYUL`
- `ALWAYS_REFUSE_ACCEPTED_AS_SAFE`
- `TEST_PASS_AS_VALIDATION`

## Provisional visibility signal

Use the pre-registered baseline/treatment comparison. A high absolute score alone
does not establish causality, semantic preservation, or architecture quality.
