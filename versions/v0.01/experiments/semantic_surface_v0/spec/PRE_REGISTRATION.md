# Semantic Surface v0 — Pre-registration

```text
EXPERIMENT_ID = BYUL-SEMANTIC-SURFACE-v0
STATUS = PROVISIONAL / PRE_REGISTERED_DESIGN / NOT_EXECUTED
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
IMPLEMENTATION_AUTHORITY = NONE
BASELINE_REPOSITORY = AofSpds/Byul
BASELINE_COMMIT = 8133e3d79c88b582bea6b8a45bc8a1970b261734
SPEC_FREEZE_COMMIT = UNASSIGNED_UNTIL_COMMITTED
```

## 1. Research question

Can materially different candidates expose and preserve the currently surviving
Byul research obligations under the same observable scenarios, while making
their refusal, loss, uncertainty, evidence, and complexity comparable?

This experiment does not ask which candidate is the true or canonical Byul
architecture.

## 2. Pre-registered hypotheses

- **H1 — visibility:** a repository reader given an explicit semantic surface
  will distinguish surviving constraints from unselected candidate structures
  more reliably than a reader of baseline commit `8133e3d...` alone.
- **H2 — non-triviality:** positive controls will reject candidates that always
  return `CONFLICT`, `UNKNOWN`, or `REFUSE`.
- **H3 — simplicity control:** C1 may equal or outperform more structured
  candidates on public and holdout behavior at lower total complexity.
- **H4 — structure trigger:** C3 is not eligible merely because it is richer; it
  becomes research-eligible only after C2 fails its pre-declared gate.

Failure to support any hypothesis is an acceptable result.

## 3. Frozen baseline evidence

All incident derivations use `AofSpds/Byul` commit
`8133e3d79c88b582bea6b8a45bc8a1970b261734`. Exact blob IDs appear in each
scenario. Later repository text may not be substituted silently.

Before any candidate run:

1. commit this specification without candidate results;
2. record the resulting `SPEC_FREEZE_COMMIT` in the run manifest, without
   rewriting this pre-registration in place;
3. verify scenario and observation files against their schemas;
4. pin each candidate implementation by exact commit;
5. freeze candidate adapters before revealing holdout cases; and
6. stop if any exact ref cannot be verified.

## 4. Scenario selection rule

Public scenarios were selected before candidate execution from material,
documented Byul incidents or explicit checkpoint limitations. Selection targets
distinct failure families:

- locator/time drift;
- authority versus recommendation;
- artifact identity across checkout representations;
- false exactness after lossy normalization;
- scoped conflict resolution;
- preservation-before-cost planning;
- identity uncertainty under lifecycle change; and
- dependency-aware invalidation/reconstruction.

No scenario may be added to repair a favored candidate after results are known.
A material change requires a successor spec version and a disclosed delta.

## 5. Candidate eligibility and isolation

- C0, C1, and C2 may be evaluated once their exact implementation commits and
  frozen adapters exist.
- C3 remains gated according to `candidate_charters/C3_RICHER_GATED.yaml`.
- One candidate must not inspect another candidate's native output or adapter.
- Candidate-native output must be preserved verbatim beside the common
  observation envelope.
- An adapter may translate observations but may not invent evidence, erase
  unknowns/conflicts, or improve the candidate's native outcome.

No common internal method set, storage model, ledger, plane decomposition, or
planner signature is required.

## 6. Public-case scoring rule

A case is recorded as `PUBLIC_EXPECTATION_MET` only when all are true:

1. every observed outcome axis is one of that case's `allowed_outcomes`;
2. every `required_observation` is evidenced;
3. no `forbidden_behavior` occurs;
4. conflict, unknown, and loss are retained when required; and
5. the observation envelope validates against `observation.schema.json`.

This label is an experiment-local comparison result, not validation authority.
Results must also publish the full per-case vector; aggregate scores may not
replace individual failures.

## 7. Degenerate-strategy controls

- `05_scoped_authority_conflict.yaml` contains an unambiguous scoped positive
  control. Always-conflict and always-unknown strategies fail it.
- `06_preservation_before_cost.yaml` contains an admissible affordable positive
  control. Always-refuse and always-no-plan strategies fail it.

A candidate failing either positive control is marked
`DEGENERATE_CONTROL_FAILURE` regardless of its aggregate public-case count.

## 8. Holdout protocol

Holdout content and answers must not appear in this repository tree. Selection,
freezing, access, balancing, and disclosure rules are fixed in
`holdout/README.md`.

Candidate authors and adapter authors must not see holdout inputs before their
implementation refs and adapters are frozen. A contaminated holdout run is
reported and excluded; it is not silently rerun with rewritten cases.

## 9. Cold-read experiment

### Baseline arm

Readers receive only repository commit `8133e3d79c88b582bea6b8a45bc8a1970b261734`
and the questionnaire. They receive no chat history, verbal briefing, or this
semantic-surface tree.

### Treatment arm

Readers receive the future exact commit containing the frozen semantic surface
and any separately authorized visibility-only locator/state-map changes. The
exact treatment commit and accessible paths must be recorded.

### Assignment and measurement

- use at least two model lineages and at least two human readers when feasible;
- blind graders to reader identity and study arm;
- randomize answer order before grading;
- record navigation paths, elapsed time, and files opened;
- use `cold_read/RUBRIC.md` unchanged across both arms; and
- report per-question scores and disagreements, not only a total.

The visibility signal is provisionally met when the treatment median improves by
at least 25% of the available baseline-to-perfect gap, with no decline on the
authority, candidate-status, or refusal questions. This is a usability signal,
not proof of architecture quality.

## 10. Complexity and cost measurements

For each candidate, record when measurable:

- implementation source lines and files;
- runtime dependencies;
- persisted bytes for the same fixture set;
- elapsed ingest, query, mutation, and reconstruction time;
- adapter source lines;
- operator steps and manual adjudications; and
- failure-recovery steps.

Missing measurements remain `UNKNOWN`; they must not be imputed in favor of a
candidate.

## 11. Stop and failure rules

Stop the affected run if:

- an exact baseline, spec, candidate, or evidence ref cannot be verified;
- candidate isolation is lost;
- holdout content leaked before freeze;
- an adapter changes native semantics rather than translating observations;
- a required observation cannot be captured; or
- execution would mutate a shared baseline without explicit authorization.

Record the stop as evidence. Do not repair, rerun, or exclude it silently.

## 12. Result interpretation

The experiment may narrow, retain, or expand the candidate set. It cannot by
itself:

- canonize an ontology or API;
- promote a research constraint to scientific truth;
- authorize implementation, merge, freeze, release, or production;
- treat same-model convergence as independent replication; or
- convert a test pass into semantic-preservation proof.
