# Semantic Surface v0 — Execution Schedule Gate Adversary 01

```text
REVIEW_TARGET = d3b328c09e009fb24ede309ffae4fed66d5c680f
TARGET_BRANCH = asa-me/research-surface-conformance-v0.1
REVIEW_ROLE = ADVERSARIAL_EXECUTION_SCHEDULE_GATE
DISPOSITION = REORDER
CANDIDATE_IMPLEMENTATION_OBSERVED = FALSE
MAIN_MERGE_AUTHORITY = NONE
```

## Decision

Do not begin S5.

The present schedule does not have a reproducible S4 pass. Its own S5 entry
condition is absent, its isolation rules regress the correction recorded in
memory 14, its harness exit test has no frozen fixtures, its observation schema
cannot demonstrate adapter fidelity or verbatim native-output preservation, and
its S6 stop rule refers to resource caps that do not exist. The cold-read and
candidate-comparison tracks are also ordered as though they were one dependency
chain even though this creates both leakage and avoidable invalidation routes.

This is a `REORDER`, not permission to implement while paperwork catches up.
The corrected schedule and protocol artifacts must be committed and reviewed as
one new freeze before any harness code is written.

## Evidence boundary

The review used the target commit and the following in-tree controls:

- `EXECUTION_SCHEDULE.md`;
- `OWNER_TRIAL_AUTHORIZATION.md`;
- `spec/PRE_REGISTRATION.md` and `spec/README.md`;
- all current scenario, schema, charter, cold-read, and holdout protocol files;
- memories 13, 14, both memory-15 records, 16, and 17; and
- the S1/S2 locator and research-state artifacts at the target commit.

The target commit is the direct child of baseline
`8133e3d79c88b582bea6b8a45bc8a1970b261734`. All scenario evidence paths and
declared Git blob IDs resolve at that baseline. That only establishes that the
pins exist. It does not establish the missing freeze, validation, isolation, or
adjudication gates below.

No S5 harness, C1 implementation, or C2 implementation is present at the target
commit. Therefore there is still time to correct the design without invalidating
candidate results.

## Gate matrix

| Gate | Required by current schedule | State at target commit | Result |
| --- | --- | --- | --- |
| S0 raw response frozen before treatment disclosure | S0 exit | Baseline report, rubric, treatment surface, and locator edits first appear in one commit; no independently frozen raw-response ref or blinded grade | `FAIL / ORDER UNPROVEN` |
| Frozen S0–S3 input to S4 | S4 exact input and entry | S4 dependency calls them “drafts”; no freeze manifest exists | `FAIL` |
| Recorded scenario/spec freeze | S5 entry | `SPEC_FREEZE_COMMIT = UNASSIGNED_UNTIL_COMMITTED`; no run manifest found | `FAIL` |
| Candidate result unavailable to reviewer | S4 isolation | No C1/C2 candidate implementation or result is present | `SATISFIED` |
| Leakage resolved | S4 stop rule | Treatment-visible tree contains the questionnaire, scoring rubric, and completed baseline answer; holdout custody is not operationalized | `FAIL` |
| Negative controls sufficient to test harness | S4/S5 | Scenario-level controls exist, but no frozen harness oracle or malicious/degenerate adapter fixture exists | `FAIL` |
| Bounded candidate scope and effort | S4/S6 | S6 cites time/LOC/dependency caps, but no such caps are declared | `FAIL` |
| One worker, one isolated workspace | memory 14 failure-closed rule | Schedule weakens it to separate workers “where possible” and permits one shared feature branch | `FAIL` |
| Stop/contamination results recordable | preregistration section 11 | Observation schema only accepts `status = OBSERVED`; there is no frozen run-state manifest schema | `FAIL` |
| Blind qualitative review | S7 and holdout rules | Required observation contains candidate identity/ref and native result; no sanitized packet or re-link protocol exists | `FAIL` |

## Blocking findings

### B1 — S4 has no immutable input and S5 has no valid entry token

`PRE_REGISTRATION.md` still says:

`SPEC_FREEZE_COMMIT = UNASSIGNED_UNTIL_COMMITTED`

It instructs a future runner to record the commit in a run manifest, but no run
manifest, freeze receipt, or digest set exists. `EXECUTION_SCHEDULE.md` then
requires “frozen S0–S3 artifacts” as S4 input while its dependency column calls
them “drafts,” and S5 requires “Scenario freeze digest recorded.” These states
cannot all be true.

Commit `d3b328c...` cannot be silently inferred as the freeze token because this
review requires blocking changes to the schedule, schemas, and protocols. Any
such correction creates a successor spec. S5 against the old schema followed by
post-review schema repair would be exactly the outcome-aware harness/spec change
the schedule claims to prevent.

Failure consequence: there is no exact object against which a harness run can
set `spec_ref`, no proof that the reviewed files equal the executed files, and
no machine-checkable way to distinguish a dry run from an experiment run.

### B2 — S0 ordering and independence are asserted, not evidenced

The baseline cold-read report first appears in the same commit as all S1–S3
edits, the questionnaire, the rubric, and the preregistration. It combines the
purported raw answer with self-scoring. There is no earlier immutable raw-response
blob, prompt digest, session/context provenance, start/end timestamp, reader ID,
grader ID, answer-order randomization record, or separate blind grade.

The report may be a useful pilot, but the commit graph cannot prove the S0 exit
claim that the response was frozen before repository edits were disclosed. The
same-lineage/context-blind assertion is not an isolation control. This matters
because memory 13 and 14 exist precisely because a textual assertion about what
a worker was supposed to do did not prevent scope crossing.

The existing report must not be counted as an uncontaminated H1 baseline unless
independent execution evidence is supplied. The safe default is
`BASELINE_ISOLATION_UNVERIFIED` and a fresh baseline arm.

### B3 — The treatment arm contains its answer key and completed answer

The treatment reader is told to explore a future repository commit normally.
That commit currently contains:

- `spec/cold_read/QUESTIONNAIRE.md`;
- `spec/cold_read/RUBRIC.md`, whose two-point cells state the desired answers;
  and
- `spec/cold_read/results/BASELINE_8133E3D_CONTEXT_BLIND_01.md`, which answers
  all eight questions and cites the intended evidence.

The baseline commit does not contain these files. Thus a treatment reader can
improve by reading the grading key or the completed answer rather than by using
the semantic surface under test. Randomized A/B labels do not repair unequal
artifact access. The proposed 25% visibility signal would be uninterpretable.

S8 is also positioned after S7 on a shared feature branch. Unless the treatment
commit is explicitly the pre-candidate surface commit, candidate code and result
artifacts can become additional treatment-only cues. If an S8 failure then sends
execution “back to S1–S3,” the schedule has no rule preventing retroactive
mutation of the spec already used for S5–S7.

### B4 — The visibility study and candidate experiment have false dependencies

S3 does not logically require a cold-read score. It requires verified incident
evidence and a frozen scenario design. S5 does not logically require H1 to be
supported. Conversely S8 does not require candidate evaluation; it requires a
pinned pre-candidate treatment surface.

The single S0→…→S9 chain makes a contaminated visibility arm block unrelated
harness work while also delaying the visibility test until after candidate work
can pollute its treatment. It also makes an S8 readability failure appear to
authorize rewriting the candidate spec after results exist.

Split the plan into two frozen branches of evidence:

1. visibility: S0 → S1/S2 surface freeze → clean treatment arm/S8; and
2. conformance: baseline-ref verification → S3 → S4 → S5 → S6 → S7.

S9 may synthesize both, but a missing or failed visibility arm must remain a
missing/failed H1 result, not a reason to rewrite a completed conformance run.

### B5 — The schedule weakens the explicit post-incident isolation contract

Memory 14 requires one worker per unique branch/worktree and failure-closed
verification before mutation. The schedule instead says:

- globally, “Make all changes on” one feature branch;
- in S6, use separate candidate workers “where possible”; and
- use candidate-specific “directories/worktrees,” without requiring unique
  branches, immutable bases, or mutually exclusive write scopes.

This is not equivalent. Two worktrees cannot safely check out and mutate the
same branch concurrently. Two directories in one mutable worktree provide no
isolation. Publishing candidate branches before the global freeze can also let
other candidate workers inspect them even if the controller asks them not to.

The schedule lacks a controller manifest that records worktree path, unique
branch, base commit, permitted write prefix, actor, start/end refs, remote ref,
and canonical blob verification. It also lacks a global barrier requiring all
candidate implementations and adapters to freeze before any cross-candidate
artifact becomes visible.

Given the exact incident history, “where possible” is a gate bypass. Isolation
must be mandatory or the candidate must stop `BLOCKED_ISOLATION`.

### B6 — The observation envelope cannot establish what the preregistration claims

The current `observation.schema.json` is syntactically an envelope, not an
evidence contract:

- `candidate_native_result` is an arbitrary parsed JSON value. It has no byte
  digest, media type, encoding, immutable locator, or capture method, so it
  cannot prove “preserved verbatim beside the common envelope.”
- There is no `adapter_ref`, adapter digest, adapter version, invocation record,
  or mapping receipt, despite frozen adapters being a core isolation gate.
- There is no scenario-input blob/digest, harness ref, environment ref, random
  seed, resource-limit record, or start/end time.
- `retained_conflicts`, `retained_unknowns`, and `loss_disclosures` accept
  arbitrary objects, including empty objects.
- `observations[*].evidence_refs` may be empty even when the scenario says
  `evidence_required: true`; `detail` may be empty; required observation IDs are
  not required to be present or unique.
- runtime evidence permits a null digest, so a locator string can satisfy schema
  validation without immutable evidence.
- the schema cannot encode `BLOCKED`, `STOPPED`, `CONTAMINATED`, `INVALID`, or
  `INCOMPLETE`, although the schedule requires these outcomes to be preserved.
- operator steps and failure-recovery steps are preregistered cost measures but
  absent from the complexity object. Missing runtime dependencies cannot be
  represented as `UNKNOWN`; an empty list is ambiguous between none and not
  measured.

As a result, a schema-valid adapter can invent all expected observations, put an
empty or rewritten value in `candidate_native_result`, omit immutable evidence,
and still hand the scorer a superficially valid envelope. S5 cannot repair this
after implementation without changing the frozen experiment contract.

### B7 — S5’s own exit test is undefined

S5 says the harness must wrap C0 and “dummy positive/negative controls,” but no
dummy candidate definitions, exact inputs, expected native outputs, expected
envelopes, or expected verdicts are frozen. Scenario cases labelled
`POSITIVE_CONTROL` and `NEGATIVE_CONTROL` are not a harness conformance suite.
They do not prove that the loader rejects a forged adapter, loss-erasing mapping,
missing required observation, wrong candidate ref, or contaminated run.

Without a pre-code oracle, the engineering worker will define the harness and
the test of the harness simultaneously. That is an unchecked pass/fail mapping,
which is the hidden-solution risk named in the S5 row.

At minimum the frozen harness suite needs:

- one mechanically valid candidate for each positive-control route;
- always-`UNKNOWN`, always-`CONFLICT`, and always-`REFUSE` candidates;
- a schema-invalid output;
- a schema-valid but semantically incomplete output;
- a native/envelope digest mismatch;
- an adapter that erases a required conflict or loss;
- a wrong spec/candidate/adapter ref; and
- a stopped/contaminated run that must remain non-scoreable.

### B8 — The adapter is an unbounded second implementation

The public scenarios expose their expected outcomes before C1/C2 are built. An
adapter is allowed to translate candidate output, but there is no transport
contract or audit rule that distinguishes translation from implementing the
scenario answer. Only some charters prohibit case-specific hard-coding, and no
enforcement or review gate checks it.

The harness needs a representation-neutral transport boundary, not a common
ontology: immutable scenario/case bytes in, captured native bytes out, then a
separately pinned mapping. The adapter must not branch on scenario/case identity
except for declared dispatch needed to invoke a native capability. Its source,
SLOC, dependencies, mapping table, and native-field-to-envelope evidence must be
audited and frozen before holdout exposure.

If a candidate has no native support for an observation, the adapter must emit
unsupported/unknown evidence; it may not compute the answer. The current schema
and schedule do not make that distinction testable.

### B9 — S6 is explicitly unbounded

S6 stops when a “Time/LOC/dependency cap” is exceeded, but neither the schedule
nor the charters declares any such cap. “2–4 h total, parallelizable” is an
estimate, not a per-candidate limit. “Permitted dependencies frozen” is an entry
gate, but the C1 and C2 charters contain no dependency allowlist or maximum.

The charters also use unbounded terms such as “small,” “minimal,” “deterministic
way,” and “observable ... evidence.” They do not freeze an implementation plan,
fixture count, supported operation set, or maximum adapter effort. C2 is named a
“leading candidate family” in the builder-visible state index while C1 is a
control. That is an anchoring and unequal-effort route even if no result yet
exists.

Before implementation, freeze per-candidate:

- exact base commit and permitted write paths;
- supported scenario operations and native I/O contract;
- implementation and adapter worker-hours/token ceilings;
- maximum non-test SLOC/files and direct runtime dependencies, or an explicit
  reason a measure is report-only rather than a stop gate;
- allowed libraries/services/network access;
- identical CPU/memory/time limits per case;
- common fixture set and repeat count; and
- a rule for incomplete candidates that does not relax another candidate’s cap.

If complexity is only observational, delete “cap exceeded” from the stop rule.
The schedule may not simultaneously claim a hard cap and leave it undefined.

### B10 — The holdout is aspirational and optional in the execution path

`holdout/README.md` describes desirable handling but assigns no selector,
custodian, storage boundary, digest witness, minimum case count, minimum cases
per family, access-log mechanism, or release condition. The schedule has no
step, dependency, budget, or output for selecting and sealing it. S7 weakens it
further to “hidden holdout when available.”

That makes the principal defense against public-case overfitting optional.
Candidate workers can implement directly against all published expectations,
and an adapter can encode those expectations. Public-case success alone then
measures benchmark fitting, not general behavior. H3 explicitly mentions
holdout behavior, and C3’s activation gate requires an uncontaminated holdout;
those claims cannot be reached through an “if available” branch.

The holdout must have an operational step before S6 starts: independent selector
and custodian, external access-controlled storage, sealed manifest digest and
witness, balance/count assertions, identical resource envelope, access log, and
an explicit `HOLDOUT_UNAVAILABLE` route. If unavailable, S7 may run as a public
rehearsal but must output `INSUFFICIENT_EVIDENCE`; it cannot support H3, candidate
superiority, or C3 activation.

### B11 — C3’s repair route conflicts with holdout non-tuning

C3 requires C2 failures to persist “after fixing ordinary implementation
defects.” The holdout protocol forbids tuning candidates or adapters after
holdout exposure. The schedule provides no second unseen set or public
reproduction route that could distinguish a defect from structural
insufficiency without reusing leaked holdout cases.

The current C3 gate can therefore be opened either by tuning on holdout or by
asserting, without a clean retest, that a failure was structural. Both are
invalid. Any C2 repair after holdout exposure must receive a new ref and adapter
and may be tested only on public reproductions plus a fresh successor holdout.
The original holdout result remains frozen. If no successor holdout exists, C3
stays closed.

### B12 — Adjudication is not preregistered enough to be blind or reproducible

Scenario requirements and forbidden behaviors are prose. The preregistration
says a case passes when every requirement is evidenced, but it does not define
who makes that judgment, how disagreements are resolved, whether the grader sees
native output, what is mechanically checked, or what constitutes sufficient
evidence. S7 names an “evaluation runner plus blind reviewer” but does not assign
roles for adapter audit versus semantic adjudication.

The required envelope itself contains `candidate_id`, `candidate_ref`, cost
fields, and candidate-native result. Giving it directly to the grader is not a
blind review. Random order does not hide identity when file paths, record shapes,
or dependency names identify the candidate.

Freeze a two-stage verdict protocol before S5:

1. mechanical checks: refs, digests, schema, required IDs, evidence presence,
   stop/contamination state, and resource limits; and
2. semantic adjudication: sanitized packets with opaque candidate/run labels,
   a frozen rubric, at least two graders or an explicit single-grader limitation,
   disagreement preservation, and re-link only after verdict freeze.

No aggregate or qualitative winner is permitted if a mandatory control fails,
holdout is absent/contaminated, material effort is unequal, or graders cannot be
blinded.

### B13 — Authority fields conflate trial execution with promotion authority

The Owner authorization explicitly authorizes C1/C2 implementation trials under
the schedule, while the preregistration, charters, and observation schema state
or force `IMPLEMENTATION_AUTHORITY = NONE`. Read literally, every authorized
trial result must falsely report that implementation authority is absent.

The intended boundary appears to be that the experiment has trial-execution
authority but grants no selection, merge, production, or canonical
implementation authority. Encode those as separate fields. At minimum:

- `trial_execution_authority`: exact authorization ref and scope;
- `shared_baseline_mutation_authority`: false;
- `main_merge_authority`: false;
- `production_authority`: false; and
- `selection_or_promotion_authority`: none.

Do not use one overloaded `implementation_authority` constant for all of them.

### B14 — S4 contains a waiver that defeats its own stop rule

S4 exits when corrections are resolved “or Owner explicitly accepts residual
risk,” while the same row says any unresolved leakage, non-neutral metric,
missing negative control, or unbounded scope blocks S5. Those statements
conflict. A generic residual-risk acceptance cannot turn contaminated or
unbounded work into the preregistered experiment.

Classify findings as either non-waivable integrity blockers or advisory risks.
The blockers in this review may be changed only by correcting and refreezing the
protocol. If the Owner authorizes execution without them, it must be a separately
labelled contaminated rehearsal with no H1/H3, comparative, holdout, or
selection-supporting claim. It is not an S4 pass for this experiment.

### B15 — Compute accounting cannot enforce the stated stop rules

The duration section mixes wall-clock hours, compute hours, worker time, human
availability, and parallel execution. S5 (0.75–1.5 h), S6 (2–4 h), and S7
(1–2 h) alone total 3.75–7.5 worker-hours before holdout custody, repetitions,
grader work, failures, or reruns, while the narrative calls S5–S7 about 3–6
wall-clock hours. There is no maximum total spend or per-step exhaustion route.

Record wall time, worker-hours, model calls/tokens or another available compute
unit, test repetitions, and human-review time separately. Set a hard experiment
ceiling and a per-candidate ceiling. On exhaustion, freeze partial outputs and
return `BUDGET_EXHAUSTED / INSUFFICIENT_EVIDENCE`; do not give the unfinished
candidate extra effort after seeing another candidate’s result.

## Hidden canonization risk

The experiment repeatedly says it is candidate-neutral, but its public surface
is constructed from same-lineage convergence and then requires all candidates
to emit the surface’s four outcome axes. The state index labels C2 a leading
candidate family, public cases are concentrated on known C0 weaknesses, and C2
is described more concretely than the simpler control. These choices may be
reasonable for a conformance probe, but they do not produce architecture-neutral
selection evidence.

The permitted interpretation must therefore be narrowed in the run manifest:

`RESULT = CONFORMANCE_TO_SEMANTIC_SURFACE_V0_UNDER_DECLARED_ADAPTER`

It must not be called proof that the surface claims are true, that its four axes
are a canonical public API, or that a passing candidate is a superior Byul
architecture. Builder-visible labels should use opaque C1/C2 identifiers and
equal-status wording. “Leading” may remain in historical evidence but must not
be an execution priority or resource-allocation instruction.

## Required reorder

Replace the present single chain with the following dependency structure before
implementation:

1. **V0 — cold-read baseline:** rerun/freeze raw baseline responses independently;
   keep instruments, rubric, and prior answers inaccessible to readers.
2. **V1 — visibility surface freeze:** pin only S1/S2 treatment content and its
   exact accessible-path policy.
3. **V2 — treatment/S8:** run against that pre-candidate treatment ref. It may
   proceed in parallel with the conformance track after isolation is audited.
4. **C0 — conformance-spec correction:** repair schemas, charters, holdout
   operations, budgets, adjudication, stop states, and authority vocabulary.
5. **C1 — immutable experiment freeze:** commit a manifest containing every
   spec/blob digest, tool/schema version, schedule-review disposition, and no
   candidate results.
6. **C2 — harness conformance gate (current S5):** only after the new S4 review
   passes; run only frozen oracle/adversarial fixtures.
7. **C3 — global candidate freeze (current S6):** unique branch/worktree per
   candidate; freeze all implementations and adapters before cross-visibility or
   holdout access.
8. **C4 — evaluation (current S7):** mechanical verdict, sealed holdout, then
   blind semantic adjudication.
9. **S9 synthesis:** join whatever valid evidence exists; a failed/missing V2 or
   holdout remains failed/missing and cannot be repaired by rewriting a completed
   conformance version.

This reorder removes S0 as a false dependency of scenario engineering while
also preventing S8 from reading post-candidate artifacts.

## Exact blocking corrections required before another S5 gate review

1. Commit a corrected successor spec and a machine-readable freeze/run manifest.
   The manifest must pin the schedule, preregistration, schemas, scenarios,
   charters, harness fixture pack, holdout-protocol version, rubric, and every
   canonical Git blob; `SPEC_FREEZE_COMMIT` must no longer be unassigned.
2. Mark the current S0 report `BASELINE_ISOLATION_UNVERIFIED` for H1 purposes or
   attach independently frozen raw-response provenance and a separate blind
   grade. Run future baseline and treatment arms with reader-inaccessible
   questionnaire answer keys, rubrics, and prior results.
3. Pin a pre-candidate treatment ref and an enforceable accessible-path policy.
   Move/split S8 as described above; no candidate code/result may be visible in
   the treatment arm, and an S8 failure may only create a successor version.
4. Replace the one-feature-branch/“where possible” language with a mandatory
   controller: unique immutable base, branch, worktree, actor, write scope, and
   remote freeze per harness/candidate/adapter; add a global freeze barrier and
   `BLOCKED_ISOLATION` failure state.
5. Add a frozen run-state manifest/schema supporting `OBSERVED`, `BLOCKED`,
   `STOPPED`, `CONTAMINATED`, `INVALID`, `INCOMPLETE`, and `BUDGET_EXHAUSTED`,
   with non-scoreability rules and explicit no-silent-rerun behavior.
6. Repair `observation.schema.json` to pin scenario input, harness, candidate,
   adapter, environment, and resources; reference byte-exact native output by
   digest/locator; require observation IDs/evidence; structure conflict,
   unknown, and loss records; and represent all preregistered cost fields and
   unknown measurements.
7. Freeze the harness oracle/adversarial fixture pack listed in B7 and its exact
   expected mechanical verdicts before writing harness code.
8. Freeze a representation-neutral transport contract and an adapter-audit
   protocol that detects case-answer logic, native/envelope mismatches, erased
   conflict/loss/unknown, and unsupported observations invented by the adapter.
9. Declare exact, symmetric candidate implementation/adapter effort ceilings,
   write scopes, allowed dependencies/services, runtime limits, repetitions, and
   budget-exhaustion behavior. Remove every stop rule that refers to a cap unless
   that cap is actually declared.
10. Add an executable holdout step before S6 with named independent roles,
    access-controlled external storage, sealed digest/witness, minimum balanced
    counts, access logging, and an explicit no-holdout route that forbids H3,
    superiority, and C3 activation claims.
11. Correct C3 so post-holdout repairs use a new C2 ref and a fresh successor
    holdout; without one, C3 remains closed.
12. Freeze the two-stage mechanical/semantic adjudication protocol, sanitized
    blind packets, grader roles, disagreement handling, and mandatory-control
    precedence before S5.
13. Split trial execution authority from merge, production, selection, and
    promotion authority in the preregistration, charters, run manifest, and
    observation schema.
14. Remove the S4 residual-risk override for integrity blockers. Any knowingly
    uncorrected execution must be renamed a contaminated rehearsal and cannot
    inherit this preregistration’s claims.
15. Recalculate the budget in separate wall-clock, worker/compute, and human
    units; set hard per-candidate and total ceilings with a frozen partial-result
    route.
16. Obtain a new adversarial S4 review against the corrected freeze. S5 opens
    only if that review records every item above as resolved by exact ref, not by
    intention or future work.

S5_GATE = CLOSED
