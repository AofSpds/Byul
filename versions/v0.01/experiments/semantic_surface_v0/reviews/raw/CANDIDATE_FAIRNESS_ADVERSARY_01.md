# Candidate Fairness Adversarial Review 01

```text
REVIEW_TARGET = AofSpds/Byul@d3b328c09e009fb24ede309ffae4fed66d5c680f
REVIEW_ROLE = CANDIDATE_FAIRNESS_ADVERSARY
REVIEW_SCOPE = SCHEDULE / C0-C3 CHARTERS / OBSERVATION ENVELOPE / HOLDOUT / C0 CODE AND TESTS
RESULT_ACCESS = NO C1/C2/C3 IMPLEMENTATION OR SCENARIO RESULT ACCESSED
DISPOSITION = CANCEL CURRENT S5-S7 ROUTE / REVISE AND RE-FREEZE
```

## Executive decision

The candidate trial is not fair enough to enter implementation. Preserve the
preparation artifacts, but cancel the current S5-S7 route and reopen the design
gate. This is not a recommendation to cancel the research question. It is a
recommendation to stop a comparison whose construction can determine its result
before candidate behavior does.

The dominant problems are structural:

1. C0 is a frozen historical specimen, while C1 and C2 are prospective systems
   whose authors can build directly against a public answer key. C0 is useful as
   an archival calibration control, but it is not an equal competitor.
2. Each public scenario file co-locates executable inputs with allowed outcomes,
   required observations, and forbidden behaviors. Nothing in the schedule
   prevents a candidate process or adapter from receiving that oracle at run
   time, and nothing prevents C1/C2 authors from designing to it before freeze.
3. The allegedly neutral envelope and fixtures impose a fairly rich comparison
   ontology. The fixtures arrive pre-parsed as assertions, authority scopes,
   preservation capabilities, lineage events, dependencies, successors, and
   loss declarations. That shape is substantially closer to C2's charter than
   to C0's native interface.
4. C1 and C2 have no falsifiable capability boundary. Git commits plus additive
   Markdown/control records, derived indexes, explicit conflict/loss records,
   and rebuildable views can be an append-only content-addressed ledger in all
   operational respects. The current labels cannot tell whether C1 has quietly
   implemented C2.
5. Equal material effort, resource limits, SLOC limits, dependency limits,
   adapter limits, and completeness criteria are named but not numerically or
   operationally defined.
6. The holdout does not yet exist and has no custodian, sealed storage, public
   commitment, access log, minimum size, or adjudication protocol. A public Git
   repository cannot keep a committed holdout secret; deletion would not repair
   Git-history disclosure.
7. C3's activation gate requires failures to persist after ordinary defect fixes,
   while the holdout rules prohibit candidate or adapter tuning after exposure.
   Reusing the exposed holdout after a fix contaminates it. C3 therefore cannot
   fairly join this trial; at most, a trigger can authorize a successor trial
   with a fresh holdout.

The public scenarios are valuable diagnostic probes. They are not, in their
current form, a fair ranking instrument.

## Evidence and checks performed

The review used the exact tree at `d3b328c09e009fb24ede309ffae4fed66d5c680f`.
The C0 implementation, contract, and tests at that commit have the same blobs
named by the C0 charter:

- `versions/v0.1/src/byul_v01.py` ->
  `467396287fa5a1c699b89485348080efac9f7b0e`;
- `versions/v0.1/tests/test_byul_v01.py` ->
  `a39f5d3bdd91e865fdd3c98f17b688d7533df7a1`; and
- `versions/v0.1/MODEL_CONTRACT.md` ->
  `8b7fb404c41a13e09de55d3adac8d309bf0352e3`.

The existing C0 micro-tests were run without bytecode writes:

```text
PYTHONDONTWRITEBYTECODE=1 python3 versions/v0.1/tests/test_byul_v01.py
11 tests passed in 0.034 s
```

That pass is evidence only about the existing micro-tests. No semantic-surface
scenario was executed. In particular, the tests do not establish an exact input
corpus, byte-exact reconstruction, generic scenario handling, persisted
invalidation, rebuild correctness, authority conflict handling, or candidate
fairness.

## Blocking findings

### CF-01 — C0 is an archival control, not an equal entrant

**Attack.** Freeze one entrant before the questions exist, then let two other
entrants be designed after the questions and answer keys are published. Report
the resulting case counts as a candidate comparison.

**Evidence.** C0 is explicitly `EXISTING_EXPERIMENTAL_BASELINE` and must be used
"without semantic repair" (`C0_CURRENT_V01.yaml:10-28`). C1 and C2 are
`PROPOSED_UNIMPLEMENTED` and may be designed after all eight public cases,
allowed outcomes, and required observations are visible
(`C1_HARDENED_GIT_MARKDOWN.yaml:10-46` and
`C2_MINIMAL_CONTENT_ADDRESSED.yaml:10-47`). S6 nevertheless groups C0, C1, and
C2 as comparison candidates (`EXECUTION_SCHEDULE.md:40`).

C0's native surface consists of corpus loading/views, a small router, virtual
mutation, and snapshot export (`byul_v01.py:159-303,347-476`). It has no native
operation for the scenario protocol's scoped assertion query, option planning,
Git-remote equality decision, split/merge identity judgment, or persisted
successor/rebuild flow. An adapter that supplies those behaviors would be a new
candidate implementation, not a translation.

**Why it biases the result.** C0 can only lose unsupported cases or receive a
semantically active adapter. C1/C2 can expose exactly the required axes. Neither
outcome is an equal comparison.

**Required correction.** Reclassify C0 as `ARCHIVAL_CALIBRATION_ONLY`, run it on
the same stimuli only to measure coverage and historical distance, and exclude
it from winner, dominance, and C3-trigger claims. If a maintained version of the
current design is desired, create a new candidate ID (for example C0M), give it
the same result-blind build packet and resource budget as C1/C2, and never
rewrite the archival C0 ref.

### CF-02 — C0's code ref and data ref are not actually frozen together

**Attack.** Run the exact C0 source blob in a later worktree. Its default glob
silently consumes whatever Markdown files are present, while its output claims
an older source baseline. Attribute data drift to candidate behavior.

**Evidence.** C0 hard-codes `SOURCE_BASELINE_COMMIT = 2a4529...`, but derives
`DEFAULT_MEMORY_ROOT` from the executing worktree and loads every `*.md` found
there (`byul_v01.py:19-21,165-177`). The contract also calls `2a4529...` the
exact source baseline (`MODEL_CONTRACT.md:15-19`). Seven memory files 12-17 were
added between `2a4529...` and the charter's implementation commit `8133e3d...`.
At the reviewed tree, the unchanged C0 code reports 19 documents and 1,013 atoms
while still reporting `source_baseline_commit = 2a4529...`.

The test accepts any document count greater than or equal to 12 and does not pin
file names or blobs (`test_byul_v01.py:23-27`). The normalized content digest
also collapses whitespace (`byul_v01.py:74-80,182-186`), and its round-trip test
only compares that normalized digest (`test_byul_v01.py:35-42`).

**Why it biases the result.** C0's apparent input and its declared input can
diverge, whereas C1/C2 will have explicit trial refs. The trial could also
accidentally give C0 more or less corpus context than the other candidates.

**Required correction.** The run manifest must pin C0's code commit, source-data
commit, complete memory path/blob manifest, adapter commit, and execution
worktree separately. Run the archival specimen in a detached `8133e3d...`
worktree if the intended measurement is behavior at that ref, and record the
stale `2a4529...` metadata as a C0 limitation. Do not patch C0 to make the test
look cleaner. If the intended data target is actually `2a4529...`, state that
instead and accept that incidents 12-17 are outside C0's native corpus.

### CF-03 — Public stimuli and answer keys are the same artifacts

**Attack.** Give a candidate or its adapter the whole scenario object. It can
copy `allowed_outcomes`, emit every `required_observation.id`, negate the
`forbidden_behaviors`, and pass without exercising a candidate-native semantic
capability.

**Evidence.** The scenario schema places `given`, `when`, `allowed_outcomes`,
`forbidden_behaviors`, and `required_observations` in the same required case
object (`scenario.schema.json:97-127`). The pre-registration defines success by
matching those exact fields (`PRE_REGISTRATION.md:85-97`). There is no separate
input schema, oracle bundle, runner ACL, or rule saying that candidates and
adapters receive only `given` and `when`.

The prohibition on hard-coding is prose in the charters; it is not enforced.
Freezing after authors have read the answers prevents post-run tuning but does
not prevent pre-run overfitting.

**Required correction.** Split every case into an input-only stimulus artifact
and a grader-only oracle artifact with separate digests and access controls. The
candidate process and adapter may receive only the stimulus. They must not
receive `control_type`, allowed outcomes, forbidden behaviors, required
observation IDs/text, or candidate-specific expected results. The harness must
demonstrate this with an access test. Treat public cases as development and
diagnostic evidence only; comparative performance claims must be based on the
sealed holdout using the same frozen refs.

### CF-04 — The comparison surface induces an ontology and favors pre-structured candidates

**Attack.** Assert that no ontology is required, but feed all cases in an
ontology-rich representation and require every result to fit a fixed semantic
cross-product. A candidate that accepts structured records appears capable;
one that starts from source evidence pays parsing and mapping costs or is called
unsupported.

**Evidence.** The common envelope requires `resolution`, `decision`,
`recoverability`, and `plan_status`, plus dedicated conflict, unknown, loss,
refusal, artifact, and reconstruction fields
(`observation.schema.json:7-27,47-94`). The fixtures pre-parse the domain into
fields such as `authority_scope`, `observed_sequence`, `preserves`, `loses`,
`lineage_events`, `successor_of`, and `depends_on` (scenarios 05-08). C2's local
shape then promises content-addressed evidence, append-only change records,
deterministic projection, and observable loss/conflict/authorization/
invalidation/reconstruction (`C2_MINIMAL_CONTENT_ADDRESSED.yaml:27-35`).

Calling the ontology "only observable" does not remove its implementation
effect. In addition, the envelope has no `UNSUPPORTED` or `UNMAPPABLE` mapping
state. `status` must be `OBSERVED`; decision has no `UNKNOWN`; and retained
conflict/unknown/loss elements are arbitrary unvalidated objects. This invites
adapters to turn missing native semantics into plausible common values.

**Required correction.** Add representation-balanced, metamorphic stimuli: the
same obligation must appear at least once as raw Git/Markdown evidence and once
as a structured event/assertion payload, with invariant expected behavior.
Record parsing/preparation as candidate cost. Revise the observation contract to
distinguish `NATIVE`, `MECHANICALLY_MAPPED`, `HARNESS_SUPPLIED`, `EVALUATOR_CODED`,
`UNSUPPORTED`, and `UNMAPPABLE` origins. Mapping loss must be explicit and cannot
be converted into a favorable outcome. Do not claim internal-ontology neutrality;
claim only a pre-registered comparison vocabulary whose translation cost is
measured.

### CF-05 — Adapters can become shadow candidates

**Attack.** Keep candidate-native code small, then implement chronology,
conflict handling, preservation classification, planning, or reconstruction in
the adapter. Count the candidate as simple and the behavior as native enough to
pass.

**Evidence.** The adapter is allowed to "translate observations" but no
mechanical/semantic boundary is defined (`PRE_REGISTRATION.md:71-83`). The
observation schema preserves native output but does not require a field-level
lineage from native output to common outcomes (`observation.schema.json:92-94`).
Adapter SLOC is merely reported. There is no adapter file/dependency cap,
branch-on-case prohibition enforceable by the runner, transform log, or
conformance suite.

This burden is especially asymmetric for C0, whose interface is far from the
scenario operations, while a newly written C1/C2 can emit the envelope directly.

**Required correction.** Restrict adapters to invocation, serialization,
renaming, enum lookup, and declarative field mapping. Each mapped semantic value
must cite a native JSON pointer, byte range, exit status, or artifact digest.
Adapters may not infer from scenario facts, branch on scenario/case IDs or
literal fixture values, choose plans, resolve conflicts, classify loss, or
construct evidence that the native candidate did not emit. Semantic adapter code
must be moved into and counted as candidate code. Freeze and audit every adapter
before any public or holdout case runs; use mutation tests with deliberately
contradictory native results to prove the adapter cannot improve them.

### CF-06 — C1 can accidentally become a ledger, and C1/C2 attribution is non-falsifiable

**Attack.** Implement an append-only, content-addressed record graph using Git
commits and Markdown/JSON manifests. Call it "Git plus Markdown" for C1 and call
the same operational shape a "minimal ledger" for C2. Any result can then be
narrated in favor of the preferred label.

**Evidence.** C1 permits exact Git objects, additive Markdown records,
machine-readable control manifests, rebuildable derived indexes, and explicit
conflict/unknown/loss/authorization/invalidation records
(`C1_HARDENED_GIT_MARKDOWN.yaml:27-40`). Git already supplies content addressing,
an append-only-style commit graph, and historical reconstruction. C2 adds
content-addressed evidence, append-only candidate-local change records, and a
deterministic current projection (`C2_MINIMAL_CONTENT_ADDRESSED.yaml:27-35`).
The charters provide no operational test that distinguishes those capabilities.
"No hidden database or ledger" prevents nondisclosure, not ledger behavior.

**Required correction.** Rename C1 as the `GIT_NATIVE_CONTROL` and define the
boundary by observable implementation capability, not by the word ledger:

- C1 may use the repository's existing Git object database/commit graph as its
  only historical store and may materialize a current fixture/control manifest;
  it may not create a candidate-owned generic append-only change journal or a
  replay/reducer that derives arbitrary current state from such a journal.
- C2 may create that candidate-owned append-only change layer and replay-derived
  projection, and must count both it and inherited Git facilities in cost and
  affordance disclosures.
- A result-blind charter auditor must classify the frozen implementation before
  execution. A boundary violation stops the run and requires relabeling in a
  successor spec; it is not waived because tests pass.

If that boundary is not scientifically interesting, collapse C1 and C2 into a
capability continuum and compare measured affordances rather than pretending
they are categorical architectures.

### CF-07 — C2 receives richer affordances without symmetric pressure against them

**Attack.** Select cases for which content addressing, append-only changes,
lineage, dependency tracking, and projection are direct solutions. Measure only
whether those mechanisms help, not whether they create new failure modes.

**Evidence.** Scenarios 03 and 08 directly reward content identity, successor
records, dependency edges, invalidation, predecessor retention, and rebuild
provenance. Scenarios 05 and 07 arrive as structured scoped assertions and
lineage events. C2 is explicitly chartered to represent all of those. The only
counterweight is a weakly specified complexity vector. There are no symmetric
fault cases for missing/corrupt records, interrupted append, schema/version
evolution, branch divergence, replay non-determinism, orphaned evidence,
one-shot small tasks, or operator repair.

**Required correction.** Before candidate work, add candidate-neutral fault and
scale controls that can expose costs of the richer substrate. At minimum include
record corruption/missing-object recovery, interrupted write/restart, divergent
histories, unknown record version, and a small one-shot retrieval for which
setup overhead is visible. Use the same raw and structured representations for
C1 and C2. Any new cases require a successor spec and new freeze; they may not be
added after candidate results.

### CF-08 — Material effort and candidate completeness are undefined

**Attack.** Give the favored candidate extra prompts, repairs, tool calls, or
hours; give another candidate only a first draft. Alternatively, stop a richer
candidate at the shared deadline and score incompleteness as architectural
failure.

**Evidence.** S6 budgets "2-4 h total" and says separate workers "where
possible," then invokes an unspecified time/LOC/dependency cap
(`EXECUTION_SCHEDULE.md:40`). No charter contains a numeric cap. S7 says unequal
material effort stops selection but does not define material effort
(`EXECUTION_SCHEDULE.md:41`). C0 consumes no current build budget, while C1/C2
do. Model lineage, context size, prompt contents, retries, test feedback, and
repair rounds are unrecorded.

**Required correction.** Pre-register one symmetric build protocol for C1/C2
(and C0M if used): identical model class/capability, clean context, build packet,
wall-clock cap, model-token cap, tool-call cap, dependency policy, candidate-code
SLOC cap, test-feedback policy, and number of result-blind repair rounds. Record
actual consumption. Define a charter-completeness checklist independent of
scenario outcomes. A candidate that cannot reach completeness within the cap is
`INCOMPLETE_UNDER_BUDGET`, not a semantic failure. Any optional extension must
be authorized before results and offered symmetrically to every prospective
candidate.

### CF-09 — Complexity measurements are not comparable

**Attack.** Count only the thin candidate module while treating Git, shell
commands, manually maintained manifests, adapter logic, fixtures, and operator
knowledge as free. Measure a warm query for one candidate and cold ingest plus
query for another. Report nulls as simplicity.

**Evidence.** The pre-registration requests source/files, dependencies,
persisted bytes, four kinds of elapsed operation, adapter SLOC, operator steps,
manual adjudications, and recovery steps (`PRE_REGISTRATION.md:147-160`). The
schema collapses time to one `elapsed_ms`, omits operator steps and recovery
steps, mixes static candidate metrics into every case result, cannot distinguish
unknown runtime dependencies from zero dependencies, and supplies no accounting
rules (`observation.schema.json:78-90`). SLOC, file, persistence, timing, and
manual-adjudication scopes are undefined.

**Required correction.** Freeze a measurement manual and split metrics into:

- build-level: candidate source, candidate-specific schemas/configuration,
  adapter source, tests, direct and transitive dependencies, build/setup time,
  and implementation effort;
- fixture-level: source bytes, derived bytes, object-store delta after ingest,
  and incremental bytes per mutation, measured from the same clean fixture;
- operation-level: cold ingest and repeated query/mutation/reconstruction
  distributions on the same machine/container and resource caps; and
- human-level: operator actions, elapsed operator time, adjudications, required
  expertise, and failure-recovery actions/time.

Count candidate-specific adapter logic in total implementation burden. Disclose
inherited Git/repository/service capabilities rather than treating them as zero
cost. Define generated code, comments, tests, vendored code, compression,
filesystem/object-store overhead, warm-up, repetitions, timeout, and null
handling. Report a vector/Pareto comparison; do not invent an unregistered
scalar complexity score.

### CF-10 — Candidate isolation is aspirational and incompatible with the shared branch as written

**Attack.** Let nominally separate workers share a repository, Git object store,
parent context, result directory, or sequential branch. One can inspect another
candidate, adapter, commit, or early result while still claiming separate
worktrees.

**Evidence.** The schedule mandates one feature branch globally
(`EXECUTION_SCHEDULE.md:18-25`) and asks only for candidate-specific
directories/worktrees with separate workers "where possible"
(`EXECUTION_SCHEDULE.md:40`). The pre-registration prohibits cross-inspection
but specifies no technical boundary or access audit (`PRE_REGISTRATION.md:71-80`).
A Git worktree is not an isolation boundary: it normally shares the object store
and can inspect all reachable refs. A forked model context may also inherit the
full public specification and prior candidate discussion.

**Required correction.** Give each prospective candidate a fresh, non-inherited
context and an exported build packet in an isolated repository/container that
cannot read sibling refs, adapters, results, the grader oracle, or the holdout.
Use separate write destinations. Freeze C1/C2 candidate and adapter refs before
any result is made visible to either builder. Record packet digests, context
policy, actor/model, start/stop times, resource usage, and access events. If
technical isolation cannot be provided, label the run contaminated/correlated
and do not use it for candidate comparison.

### CF-11 — Holdout secrecy and adjudication are not executable in the current public-repo protocol

**Attack.** Delay holdout selection until implementations are visible, choose
near-copies of public templates, store the cases in Git and later delete them,
or let the same shared worker act as selector, adapter author, runner, and grader.
The resulting "hidden" score can be chosen or leaked without a detectable trace.

**Evidence.** The holdout directory contains rules only and explicitly contains
no inputs or answers (`holdout/README.md:1-12`). Selection is after scenarios and
charters freeze, but not explicitly before candidate implementation begins
(`holdout/README.md:14-35`). No selector/custodian is named; no storage system,
ACL, salted commitment, access log, minimum case count, oracle review, or grader
disagreement rule exists. S7 permits the hidden holdout merely "when available"
(`EXECUTION_SCHEDULE.md:41`). At least four families can therefore mean one case
per family, and minimal transformations of public incidents can be memorized
templates rather than generalization tests.

**Required correction.** Plaintext holdout inputs, oracles, and salts must never
be committed to this public repository, including on a temporary branch. Before
candidate work, an independent selector and custodian must freeze a canonical
bundle in a separate ACL-controlled store, publish a salted commitment and a
non-secret balance manifest, and begin an access log. Use at least 8 cases, at
least 2 in each of the four declared families, with at least 2 execution-required,
2 refusal-required, 2 resolvable, and 2 unresolved cases. At least half must be
naturalistic or compositionally different from the eight public templates, not
lexical/minimal rewrites. A second independent oracle reviewer must freeze
agreements and disagreements before execution. Candidate/adapter authors may
never receive the bundle. The isolated runner reveals inputs only to frozen
executables and reveals randomized native observations only to blind graders.

A public-only run is allowed as a rehearsal, but it must end
`INSUFFICIENT_EVIDENCE` and may not support "outperform," C3 activation, or
candidate narrowing.

### CF-12 — The scoring and comparison claim are under-specified

**Attack.** Select whichever axis favors a preferred candidate after seeing the
results: public pass count, a convenient complexity field, one severe-looking
case, or qualitative readability. The ban on an aggregate score does not stop
post-hoc narrative weighting.

**Evidence.** Public expectation matching and two degenerate controls are
defined (`PRE_REGISTRATION.md:85-107`), but there is no minimum holdout rule,
severity scheme, definition of "equal or outperform" from H3, missing-capability
treatment, or registered relation between semantic gates and complexity. The
observation schema can be valid with empty conflict/loss arrays and arbitrary
native output; scenario-specific required IDs are not schema-enforced.

**Required correction.** Pre-register an interpretation table before candidate
work. Public cases are diagnostic. Holdout cases report a complete per-case
vector. Degenerate-control failure, oracle contamination, adapter semantic
mutation, or charter violation are gates, not scores. `UNSUPPORTED` and
`INCOMPLETE` remain distinct from incorrect behavior. Among gate-eligible
candidates, report semantic and cost Pareto relations plus uncertainty; define
"outperform" before execution and make `INCOMPARABLE` the default when tradeoffs
cross. No single winner or selection claim is available under the current
`SELECTION_AUTHORITY = NONE` boundary.

### CF-13 — C3's activation logic is adaptive, subjective, and internally inconsistent

**Attack.** Observe C2's public and holdout failures, repair C2, design C3 to the
revealed cases, and reuse those cases to show that C3 solves exactly the failures
that inspired it. Call that causal evidence for richer structure.

**Evidence.** C3 requires an uncontaminated C2 holdout, failures in two broad
categories or one undefined catastrophic loss, persistence after ordinary
defect fixes, causal analysis, and proof C1 cannot satisfy the same cases
(`C3_RICHER_GATED.yaml:29-41`). Yet holdout tuning or ref changes contaminate the
run (`holdout/README.md:31-45`), and the pre-registration says a contaminated run
is excluded rather than silently rerun (`PRE_REGISTRATION.md:109-117`).
"Ordinary defect," "repeatable," "catastrophic," "missing richer structure,"
and "materially simpler" have no adjudication procedure. An ablation cannot by
itself establish the effect of a feature that C2 does not contain.

**Required correction.** C3 must remain outside this trial. Replace the current
effect with a successor-experiment trigger only. A defensible trigger would
require either (a) at least two independently adjudicated, repeatable holdout
failures in each of two predeclared families, or (b) one predeclared catastrophic
source/evidence-loss event reproduced three times under fault injection; all
must survive blind triage against adapter, resource, implementation-completeness,
and scenario-ambiguity causes. No exposed holdout may be reused after a fix.
If triggered, obtain separate authorization, freeze an exact feature-to-failure
charter and complexity cap, create a fresh holdout, and rerun frozen or
equivalently rebuilt simpler comparators in the successor experiment. The
trigger is research eligibility, never evidence that C3 is superior.

### CF-14 — The current order can leak C0-derived answers before prospective candidates freeze

**Attack.** Use real public cases during S5 while wrapping C0, inspect its
failures, then give C1/C2 builders targeted guidance. Even if candidates never
read one another, the harness rehearsal becomes result-aware design input.

**Evidence.** S5 requires the harness to wrap C0 and dummy controls before C1/C2
are built (`EXECUTION_SCHEDULE.md:39-40`). It does not say that C0 dry runs use
synthetic harness fixtures only or that outputs remain sealed. Because several
public cases were explicitly derived from C0 limitations, a real-case C0 run is
an answer-disclosure channel.

**Required correction.** S5 may validate schemas and mechanical adapter behavior
only with synthetic positive, negative, malformed, and contradictory dummy
fixtures whose outputs are unrelated to the eight real cases. Do not run C0,
C1, or C2 on any public or holdout stimulus until all prospective candidate and
adapter refs are frozen. Run the archival C0 calibration at the same sealed
evaluation stage, and do not reveal any candidate's results until all executions
and blind judgments are frozen.

## Required cancellation and replacement order

Cancel S5-S7 as currently authorized. Preserve S0-S4 evidence and do not edit the
frozen v0 specification in place. A material repair should be a successor spec
version with an explicit delta.

Use this order:

1. **F0 — Preserve and declare.** Pin this review, declare v0 unsuitable for
   candidate implementation, and preserve all preparation artifacts without
   claiming candidate failure.
2. **F1 — Re-charter roles and capability boundaries.** Make C0 archival-only;
   decide whether C0M exists; define the operational C1/C2 boundary; make C3 a
   successor-trigger hypothesis only.
3. **F2 — Separate stimulus, oracle, and mapping contracts.** Freeze an
   input-only schema, grader-only oracle schema, mapping-origin rules, adapter
   purity rules, and dummy-only harness conformance suite.
4. **F3 — Balance representations and failure pressure.** Add metamorphic raw/
   structured equivalents and pre-registered fault/scale controls before any
   candidate author sees a result. Freeze the successor spec.
5. **F4 — Select and seal the holdout.** An independent selector/custodian freezes
   the externally stored holdout and oracle, publishes the salted commitment and
   balance manifest, and starts the access log before prospective implementation.
6. **F5 — Freeze measurement and resource manuals.** Record numeric resource,
   effort, adapter, timing, persistence, and completeness rules with no `TBD`.
7. **F6 — Build the harness on dummies only.** Prove oracle non-access, adapter
   non-improvement, evidence lineage, malformed-input behavior, and result
   sealing. No real candidate case is run.
8. **F7 — Build prospective candidates in parallel isolation.** Give C1/C2 (and
   C0M if authorized) symmetric clean packets and budgets. Freeze all candidate
   and adapter refs before any real result is visible. A blind auditor checks
   charter classification and completeness.
9. **F8 — Execute once on frozen refs.** The sealed runner executes holdout and
   public stimuli with the same refs, fixtures, limits, and repetitions. C0 runs
   as archival calibration only. No repair occurs after any real-case exposure.
10. **F9 — Blind grade, disclose, and compare.** Randomize candidate identity,
    freeze judgments, then disclose identities and the complete semantic/cost
    vectors. Apply only pre-registered gate and Pareto language.
11. **F10 — Route C3 separately.** If the pre-registered successor trigger fires,
    close this experiment and open a newly authorized experiment with a fresh
    holdout. Do not append C3 to the already observed trial.

## Exact entry conditions for a candidate trial

Every condition below is mandatory. "Documented later," "when available," and
`TBD` do not satisfy an entry condition.

- **EC-01 — Successor freeze:** A committed successor specification has an exact
  40-hex spec ref, schema/scenario digests, a disclosed delta from v0, and a
  resolved fairness-review matrix. The v0 artifacts remain unchanged evidence.
- **EC-02 — Role parity:** C0 is explicitly archival and comparison-ineligible.
  Any C0M is a new ID built under the same prospective protocol as C1/C2.
- **EC-03 — Code/data pins:** C0's code ref, source-data ref, complete source
  path/blob manifest, adapter ref, and detached execution tree are separately
  pinned. C1/C2 have exact candidate and adapter refs before evaluation.
- **EC-04 — Oracle separation:** Stimulus and oracle are separate artifacts. The
  runtime access test proves candidate and adapter processes cannot read control
  type, allowed outcomes, forbidden behaviors, required observations, holdout
  notes, or grader state.
- **EC-05 — Adapter purity:** A frozen policy and conformance suite proves adapters
  are mechanical and cannot improve contradictory, unknown, unsupported, or
  lossy native results. Every common semantic field records mapping origin and
  native evidence location.
- **EC-06 — Operational C1/C2 boundary:** A result-blind auditor can determine
  from an explicit checklist whether a frozen implementation owns an append-only
  change journal/replay projection. Any boundary failure stops and recharts the
  run before real cases.
- **EC-07 — Symmetric build budget:** One numeric, identical C1/C2 protocol fixes
  model class, clean-context packet, wall-clock, tokens, tool calls, SLOC,
  dependency policy, feedback, and repair rounds. Actual use is logged and
  completeness is judged without scenario outcomes.
- **EC-08 — Symmetric execution budget:** CPU, memory, disk, timeout, network,
  Git facilities, fixture bytes, repetitions, warm-up, and failure policy are
  numeric and identical for every candidate.
- **EC-09 — Comparable cost manual:** Static, fixture, operation, human, adapter,
  inherited-service, and recovery costs have unambiguous scopes; unknown is
  distinct from zero; public reporting is a vector, not an improvised scalar.
- **EC-10 — Representation balance:** Each of the four failure families includes
  a raw-evidence and structured/metamorphic form, and the successor suite includes
  pre-frozen corruption, interrupted-write, divergent-history, unknown-version,
  and small-task overhead controls.
- **EC-11 — Sealed holdout:** Before candidate work, an independent selector and
  custodian freeze at least 8 externally stored cases with at least 2 per declared
  family, at least 2 execution-required, 2 refusal-required, 2 resolvable, and 2
  unresolved cases; at least half are not minimal/lexical public-case rewrites.
  A salted public commitment, non-secret balance manifest, oracle-review record,
  and access log are frozen. No plaintext holdout or salt enters Git.
- **EC-12 — Technical isolation:** Fresh non-inherited candidate contexts and
  isolated repositories/containers cannot read sibling refs, adapters, results,
  grader oracles, or holdout storage. Packet digests and access events are
  recorded. Policy-only isolation is insufficient.
- **EC-13 — Simultaneous result freeze:** All prospective candidate and adapter
  refs pass charter/completeness audit before any C0/C1/C2 public or holdout run.
  S5 used dummies only. Results remain sealed until every run and blind judgment
  is frozen.
- **EC-14 — Interpretation freeze:** Public cases are diagnostic only; holdout
  per-case vectors, degenerate gates, contamination rules, unsupported/
  incomplete treatment, severity, Pareto relation, and the exact meaning of
  "outperform" are committed before execution. `INCOMPARABLE` is permitted.
- **EC-15 — C3 successor-only rule:** C3 cannot be implemented or appended to
  this trial. Its numeric, independently adjudicated trigger authorizes only a
  separately approved successor with a fresh holdout and rerun comparators.
- **EC-16 — Independent gate sign-off:** A reviewer who authored neither a
  candidate nor an adapter verifies EC-01 through EC-15 against exact refs and
  records `PASS` for every item before implementation begins.

CANDIDATE_TRIAL_GATE = CLOSED
