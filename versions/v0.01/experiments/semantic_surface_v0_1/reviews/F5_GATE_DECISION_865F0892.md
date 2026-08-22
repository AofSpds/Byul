# F5 exact-ref gate decision — manifest 865f0892

```text
MANIFEST_COMMIT = 865f0892fe668e76c7c21822ff9474809b99520d
SOURCE_COMMIT = 78a1a992a2cfecea337a8610112b6dbaa0a7e127
FREEZE_INTEGRITY = PASS / 67 OF 67
DUMMY_TRANSPORT_GATE = CANCEL / REVISE_AND_REFREEZE
CANDIDATE_TRIAL_GATE = CANCEL / LOCAL_AND_EXTERNAL_BLOCKERS
SCHEMA_EXPLOIT_REVIEW = NO_UNBOUND_LISTED_EXPLOIT
HARNESS_IMPLEMENTATION = NOT_STARTED
CANDIDATE_IMPLEMENTATION = NOT_STARTED
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
MAIN_MERGE_AUTHORITY = FALSE
PRODUCTION_AUTHORITY = FALSE
```

The dummy decision is controlled by the stricter review: syntactic and targeted
exploit checks passed, but the actual-side execution fixtures, truncation route,
and F5-D authority scope were not sufficiently frozen. The candidate decision
is independently closed by missing F3-C, V1, F6, holdout, isolation, role,
telemetry, and exact implementation evidence.

## Route

1. Preserve commits `78a1a992...` and `865f0892...` as failed-gate evidence.
2. Add no harness or candidate code.
3. Freeze separately executable actual-side dummy fixtures, event evidence,
   complete binding controls, a truncation vector, and exact F5-D authority.
4. Create a new source/blob manifest and rerun F5-D only.
5. Keep F5-C closed regardless of any later F5-D outcome.

All reviews are correlated internal adversarial evidence, not independent
validation.
