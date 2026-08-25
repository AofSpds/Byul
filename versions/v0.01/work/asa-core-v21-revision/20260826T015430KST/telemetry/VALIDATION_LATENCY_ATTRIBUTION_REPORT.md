# Validation Latency Attribution Report

```text
PROGRAM_ID = ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0
RUN_ID = 20260826T015430KST
PROGRAM_START_KST = 2026-08-26T01:54:30+09:00
PROGRAM_END_KST = 2026-08-26T02:25:31+09:00
EXPECTED_ACTIVE_TOTAL = 61-120 minutes
CONDITIONAL_PARALLEL_ENVELOPE = 53-105 minutes
ACTUAL_ACTIVE_TOTAL = 1861 seconds / 31m01s
OWNER_WAIT = 0 seconds
DOCUMENTED_EXTERNAL_OUTAGE_WAIT = 0 seconds
TOTAL_OVERRUN = 0 seconds
VALIDATION_OVERRUN = 0 seconds
CURRENT_RUN_VERDICT = VALIDATING_NOT_PRIMARY / NO_OVERRUN_CURRENT_RUN
HISTORICAL_SLOWDOWN_VERDICT = INDETERMINATE_DUE_TO_EVIDENCE_GAP
```

## 1. Result

This instrumented run did not reproduce a validation-caused overrun. The full
S0–S8 program finished below both the 120-minute conservative upper bound and
the superseded 90-minute dispatch upper bound. Output validation and its
single correction/recheck cycle consumed 489 seconds of non-overlapping
wall-clock, also below the combined S6+S7 expected range of 10–25 minutes.
Including PMOV's S8 calculation review, its bounded correction, and diff-only
recheck, all validation-attributable work was 646 seconds.

This does **not** establish the cause of the earlier slow incident. That event
does not have contemporaneous raw context-load, direct-review, correction,
and wait intervals in this run's evidence set. Its causal classification must
therefore remain `INDETERMINATE_DUE_TO_EVIDENCE_GAP`.

## 2. Stage wall envelopes

| Stage | Observed wall envelope | Expected | Assessment |
|---|---:|---:|---|
| S0 plan admission / telemetry | 7m01s | 5–10m | within range; BYULV split unavailable |
| S1 input freeze / dedup | 23s | 5–10m | below range; automated exact-title/hash work |
| S2 crosswalk / delta map | 5m17s | 8–15m | below range; artifact-time envelope |
| S3 main authoring | 2m25s | 15–25m | below range; overlaps S2/S4 |
| S4 companion sync | 2m54s | 8–15m | below range; overlaps S3 |
| S5 D0 freeze / self-check | 2m50s | 5–10m | below range |
| S6 D0 dispatch through finding freeze | 5m04s | 5–15m | within range; three validators parallel |
| S7 correction through final recheck | 3m05s | 5–10m | below range; one correction batch |
| S8 packaging / verdict | 465 seconds / 7m45s | 5–10m | within range |

S2–S4 envelopes overlap and are not summed as wall-clock or presented as
exact per-worker compute. They are supported by output timestamps, while the
unavailable actor split remains an evidence gap.

## 3. Validation accounting

### Non-overlapping wall-clock

| Component | Wall time | Evidence |
|---|---:|---|
| D0 validator review window | 140s | first context start 02:11:07 → last review end 02:13:27 |
| Finding integration | 74s | 02:13:27 → 02:14:41 |
| Validation-induced correction | 92s | 02:14:41 → D1 freeze 02:16:13 |
| D1 affected-diff recheck window | 45s | 02:17:01 → 02:17:46 |
| Dispatch/context orchestration | 138s | D0 dispatch 90s + D1 diff dispatch 48s |
| S8 calculation review | 86s | PMOV context/direct check 02:21:48 → 02:23:14 |
| S8 finding correction | 63s | three stage cells, coverage note, and freeze timestamp |
| S8 diff-only recheck | 8s | 02:24:17 → 02:24:25 |
| **Validation-attributable total** | **646s / 10m46s** | non-overlapping union |

`VALIDATION_ATTRIBUTABLE_CURRENT_SHARE = 34.7%` of this run's
total active wall-clock. This is a descriptive share, not an overrun
contribution percentage, because `TOTAL_OVERRUN = 0`.

### Validator compute observations

| Measure | Value |
|---|---:|
| Known context-load compute | 122s plus CONTROLV recheck `<1s` |
| Known direct-review compute | 231s |
| MODELV context/direct unsplit | 90s |
| Total validator review compute sum | 481s |
| Initial parallel review wall | 140s |
| Recheck parallel wall | 45s |
| S8 PMOV calculation review + recheck | 94s |

Compute sums are not substituted for wall-clock. MODELV's interface did not
emit context/direct subintervals, so its 85-second D0 review and 5-second D1
recheck remain unsplit.

## 4. Orchestration assessment

```text
VALIDATOR_PARALLELISM = 3-way at D0 and 3-way at affected-diff recheck
FULL_REPOSITORY_SCANS = 0
REPEATED_WHOLE_TARGET_READS = 0
SHA_ONLY_GLOBAL_REVALIDATIONS = 0
NEW_VALIDATORS_OR_DOMAINS = 0
CORRECTION_BATCHES = 1
VALIDATION_ORCHESTRATION_OVERHEAD = 138 seconds
```

The 138 seconds are bounded dispatch/context preparation. The S8 calculation
review and its bounded local correction are reported separately above. No evidence of the
historical failure pattern—serial whole-target rereads, validator co-design,
unbounded correction loops, or SHA-triggered global revalidation—appeared in
this run.

## 5. Telemetry coverage and gaps

```text
TOTAL_ACTIVE_WALL = 1861 seconds
CATEGORIZED_WALL = 1703 seconds
UNCLASSIFIED_WALL = 158 seconds
CATEGORIZED_COVERAGE = 91.5%
AC-20 / AC-19 THRESHOLD = >= 90%
RESULT = PASS
```

The unclassified intervals are a 6-second bootstrap handoff, a 60-second S0
handoff, and a 92-second concurrent plan-validation/crosswalk interval. They
are explicitly retained rather than assigned retrospectively. S0 BYULV's
context/direct split and the earlier historical incident's raw timing are the
material evidence gaps.

Coverage uses macro-category program-wall classification: MODELV E009 is
known to be validation review even though its finer context/direct split is
unavailable and the ledger therefore labels that row `UNCLASSIFIED`. Under a
strict literal-ledger union, four additional seconds would be unclassified;
either convention remains above the 90% threshold and leaves the verdicts
unchanged.

## 6. Cause classification

| Question | Classification | Confidence | Basis |
|---|---|---|---|
| Was VALIDATING the primary cause in this run? | `VALIDATING_NOT_PRIMARY / NO_OVERRUN_CURRENT_RUN` | High | no total or validation-stage overrun; bounded parallel validation |
| What caused the earlier reported slowdown? | `INDETERMINATE_DUE_TO_EVIDENCE_GAP` | High that attribution is unsupported | no contemporaneous historical timing/read-loop evidence |

The current run supports a narrower operational conclusion: risk-adaptive,
role-scoped validation can complete without dominating a small document task.
It cannot prove whether the former delay came from validation itself,
orchestration around validation, task expansion, or another source.

## 7. Recurrence prevention

1. Route `PLAN_REVIEW + NO_MUTATION` to FAST and bounded document changes to
   role-scoped STANDARD validation.
2. Freeze one candidate, dispatch validators in parallel, and freeze findings
   before any correction.
3. Permit one correction batch and recheck only affected diffs; a changed SHA
   alone never triggers a global reread.
4. Record exact source-filename queries and close stage telemetry before
   validator dispatch.
5. Have validator interfaces emit separate context-load and direct-review
   timestamps; leave missing splits unverified.
