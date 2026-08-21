# Semantic Surface v0 — Consolidated S4 Gate Decision

## Decision

```text
REVIEW_TARGET = AofSpds/Byul@d3b328c09e009fb24ede309ffae4fed66d5c680f
REVIEW_CLASS = SAME_MODEL_LINEAGE / CORRELATED_INTERNAL_ADVERSARIES
SCHEDULE_REVIEW = REORDER
SPEC_FREEZE = BLOCKED
CANDIDATE_TRIAL_GATE = CLOSED
S5_HARNESS_IMPLEMENTATION = NOT_STARTED
C1_C2_IMPLEMENTATION = NOT_STARTED
CURRENT_ROUTE = PRESERVE_V0 / DESIGN_SUCCESSOR_SPEC / RE_REVIEW
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
MAIN_MERGE_AUTHORIZED = FALSE
PRODUCTION_AUTHORIZED = FALSE
```

The three reviews are correlated internal adversarial evidence, not independent
expert validation. Their unanimous gate closure is nevertheless binding for the
current schedule because the schedule itself made S4 a pre-implementation stop
gate.

## Raw reviews

- `raw/SCHEDULE_GATE_ADVERSARY_01.md`
- `raw/SCENARIO_GAMEABILITY_ADVERSARY_01.md`
- `raw/CANDIDATE_FAIRNESS_ADVERSARY_01.md`

## Convergent blockers

1. Candidate-visible stimuli and grader-only answers are co-located. No frozen
   input projection prevents an answer-key reflector from passing.
2. The observation envelope cannot prove native-output preservation, adapter
   fidelity, required-evidence coverage, or stopped/contaminated run state.
3. Adapters can implement missing semantics and become shadow candidates.
4. The recorded cold-read pilot is useful but cannot be claimed as an
   independently frozen or blinded H1 baseline. The treatment tree also exposes
   the rubric and completed answer.
5. C0 is an archival specimen created before the questions, whereas C1/C2 would
   be written after all public expectations are visible. It is not an equal
   ranking entrant.
6. C0 code and its declared data baseline are not pinned together: unchanged
   code reads a live filesystem corpus while reporting an older constant.
7. C1 and C2 have no operational boundary; Git-native additive records can
   silently recreate the C2 capability shape.
8. Candidate effort, dependencies, SLOC, tool calls, runtime resources,
   repetitions, repair rounds, and budget-exhaustion behavior are not frozen.
9. The holdout is a policy description, not an executable sealed experiment. It
   lacks an independent custodian, private bundle, commitment, access log,
   minimum balanced cases, and frozen oracle adjudication.
10. C3's repair/activation rule conflicts with the prohibition on tuning after
    holdout exposure. C3 must be successor-experiment-only.
11. Scenario outcome axes are not fully defined as tuples. Several cases use
    recoverability/plan status outside a clear referent.
12. Scenario 08 requires execution/rebuild without supplying a deterministic
    transformation or proof that the dependency graph is complete.
13. The schedule weakens the post-incident isolation rule from mandatory unique
    branch/worktree ownership to "where possible."
14. Mechanical checks and semantic adjudication are not separated or blindable.
15. Integrity blockers can currently be waived as generic residual risk, which
    defeats the stop rule.

## Preserved value from v0

- exact baseline commit and Git-blob evidence pins;
- explicit non-selection/non-validation boundaries;
- the research-state visibility surface and corrected active locators;
- eight real incident families as development probes;
- separate outcome-axis intent, after their referents are corrected;
- conflict, unknown, loss, provenance, refusal, native output, and cost as
  observable comparison goals;
- positive-control intent;
- C1 simplicity pressure and C3 evidence-trigger principle;
- per-case evidence preservation and no silent rerun.

## Binding corrections for the successor experiment

The successor must, before candidate implementation:

1. split candidate-visible stimulus, grader-only oracle, and mapping contracts;
2. use opaque randomized IDs and runner-enforced access separation;
3. use allowed outcome tuples with explicit axis referents and invariants;
4. pin input, oracle, runner, harness, candidate, adapter, environment, resources,
   native bytes, mappings, and run state by exact digest/ref;
5. support `BLOCKED`, `STOPPED`, `CONTAMINATED`, `INVALID`, `INCOMPLETE`, and
   `BUDGET_EXHAUSTED` as non-scoreable states;
6. freeze malicious/dummy harness fixtures before harness code;
7. restrict adapters to auditable mechanical mapping with native-field/byte
   lineage and explicit unsupported/unmappable states;
8. reclassify C0 as archival calibration and define a result-blind operational
   C1/C2 boundary;
9. declare symmetric numeric build/execution budgets and a complete cost manual;
10. add expectation-reversing and metamorphic development pairs, including a
    real deterministic invalidation/rebuild fixture;
11. separate cold-read baseline/treatment artifacts from rubrics, prior answers,
    candidate code, and results;
12. operationalize an externally sealed holdout before candidate construction,
    or explicitly downgrade the run to a public rehearsal that can only return
    `INSUFFICIENT_EVIDENCE`;
13. make C3 a successor-experiment trigger requiring a fresh holdout;
14. require mandatory unique isolation and a simultaneous candidate/result
    freeze barrier;
15. freeze two-stage mechanical and blind semantic adjudication; and
16. obtain a new adversarial gate review against exact successor refs.

## Non-waivable route

An Owner choice to run without the corrections may authorize a separately named
`CONTAMINATED_PUBLIC_REHEARSAL`, but it cannot reopen this experiment's S5 gate
or inherit H1/H3, holdout, superiority, narrowing, validation, or selection
claims.
