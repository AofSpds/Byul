# Semantic-surface scenario gameability adversary 01

## Review identity and scope

- Reviewed tree: `versions/v0.01/experiments/semantic_surface_v0/`
- Reviewed repository commit: `d3b328c09e009fb24ede309ffae4fed66d5c680f`
- Evidence baseline claimed by the specification: `8133e3d79c88b582bea6b8a45bc8a1970b261734`
- Review posture: hostile evaluator; assume a candidate author, adapter author, runner, or grader will exploit every literal ambiguity that is not mechanically closed.
- Candidate implementations were not inspected or implemented.

I inspected both JSON Schemas, all eight scenario files and all ten public cases, the pre-registration, the cold-read questionnaire and rubric, the recorded baseline cold read, the holdout rules, all four candidate charters, and the schedule/authorization documents that define how this package is intended to be run. I also resolved every unique public-scenario evidence path at baseline commit `8133e3d...` and compared its Git blob ID with the declared pin. All eleven unique evidence paths resolve, and every declared blob ID is correct. That is a real strength of the package, but it does not cure the gameability and outcome-validity failures below.

## Executive verdict

The specification is not ready to freeze as a discriminating candidate experiment.

The public scenario documents co-locate candidate inputs, control labels, allowed answer vectors, forbidden answers, and the prose that an adapter is supposed to emit. No protocol defines which subset is delivered to a candidate. A generic answer-key reflector can therefore pass without representing any Byul obligation. Even if a future harness withholds the explicit answer fields, the scenario IDs, case IDs, operation names, control labels, boolean field names, and request prose disclose nearly every expected posture. The ten cases are closer to transparent unit examples than adversarial semantic probes.

The prose prohibition on adapter invention is not enforceable through the observation schema. The schema permits `candidate_native_result: null`, empty or content-free evidence containers, nullable/untyped digests, and arbitrary adapted claims with no pointer back to native output. There is no adapter ref, adapter digest, native-result digest, source pointer, or monotonicity rule. Thus the central comparison boundary is asserted but not auditable.

At least one scenario, `08_source_mutation_invalidation_rebuild.yaml`, requires an executable rebuild although the fixture supplies neither a transformation nor output content nor a completeness claim for the dependency graph. Its expected `EXECUTE / SAFE_PLAN` vector is not supported by its inputs or evidence. Several other cases misuse or leave ambiguous the `recoverability` and `plan_status` axes. The per-axis allowed lists also define a Cartesian product, not allowed outcome tuples.

The cold-read treatment is contaminated by a repository-resident rubric and answer-rich scenario tree that the treatment reader can inspect but the baseline reader cannot. The repository README explicitly links the rubric. Required citations make arm blinding impossible. The one recorded baseline response was committed in the same commit as the rubric and pre-registration, lacks several questionnaire-required metadata fields, and has no cryptographic proof that its raw response preceded rubric authoring. The provisional 25%-of-gap threshold has no minimum sample size, rounding rule, treatment aggregation rule, or inter-grader reliability gate.

The holdout rules are directionally sensible but not operationally sufficient to rescue the design. They set no minimum case count, sampling frame, near-duplicate/public-template distance, hidden-answer/input separation, dual-adjudication rule, manifest schema, or common treatment of contaminated/missing cases. Candidate and adapter authors will already have seen all public answer templates before implementing C1/C2.

These are freeze blockers, not editorial polish.

## A concrete pass-without-semantics attack

The scenario schema packages all of the following in the same case object:

1. `given` and `when`;
2. `control_type`;
3. `allowed_outcomes`;
4. `forbidden_behaviors`; and
5. `required_observations`, including the exact prose expected from the result.

Neither `PRE_REGISTRATION.md` nor a schema defines a candidate-input projection. Consequently, the following generic behavior is compatible with the literal file format and is not case-specific branching:

```text
for each case object:
    choose the first member of every allowed_outcomes array
    for every required_observation:
        emit observed=true
        copy requirement into detail
        cite the case object itself as runtime evidence
    copy any named conflict/unknown/loss material from given
    report no forbidden behavior
```

This can be implemented once for every public and similarly encoded holdout case. It need not understand Git identity, authority, preservation, scope, identity, invalidation, or reconstruction. C1 only forbids hard-coding public answers "in the adapter," and C2 forbids "case-specific branches"; a generic answer-key reflector is neither a per-case branch nor necessarily located in the adapter. The broader intent plainly forbids it, but the runner/input contract does not.

Even an empty native candidate can generate a schema-valid adapted record. `observation.schema.json:58-70` does not require any observations, and `candidate_native_result` may be `null` (`:92-94`). A dishonest adapter can add the expected observations afterward. A slightly less obvious candidate can emit the reflected answer as its native result. Nothing in the schema proves which computation happened.

If a future harness sends only `given` and `when`, a shallow, candidate-independent decision tree still solves the published set:

- an explicit authorization boolean is false -> refuse;
- original raw bytes absent plus `BYTE_EXACT` requested -> refuse exactness;
- filter options by `cost <= budget` and set inclusion in `preserves` -> execute/refuse;
- exact scope match -> resolve, null scope -> review;
- null identity policy plus empty equivalence evidence -> unknown;
- equal canonical digests plus all resume booleans -> execute;
- `successor_of` plus a literal `depends_on` list -> stale/rebuild the named affected output and preserve the named unrelated one.

That is generic fixture parsing, not evidence that a candidate preserves the underlying research obligations on real artifacts.

## Schema attack surface

### Scenario schema

1. **No candidate-input schema or answer-key separation.** `given` and `when` are unconstrained objects (`scenario.schema.json:113-114`). Their content, typing, completeness, and relation to adjudication cannot be validated. The same enclosing object contains the expected answer.

2. **No semantic consistency constraints.** The schema does not relate `unresolved_allowed` to `allowed_outcomes`; a case can set `unresolved_allowed: false` while allowing `UNKNOWN` or `CONFLICT`, or set it true while allowing only `RESOLVED`. It does not relate `decision: REFUSE` to a non-null reason, `plan_status: SAFE_PLAN` to an executable decision, or `recoverability: EXACT` to reconstruction evidence.

3. **Allowed axes are independent lists, not allowed tuples.** The public scoring rule accepts a result when each observed axis is a member of its corresponding list. If more than one value is allowed on multiple axes, this admits their entire Cartesian product, including combinations the case author may never have intended. Scenario 08 already allows `RESOLVED / EXECUTE / UNKNOWN / SAFE_PLAN` while demanding a rebuilt output; its separate `unresolved_allowed: false` flag gives no guidance about uncertainty on the recoverability axis.

4. **Control labels have no normative semantics and leak posture.** `PRIMARY`, `NEGATIVE_CONTROL`, `POSITIVE_CONTROL`, and `PAIRED_CONTROL` are merely enums. The schema does not say what must be paired or how controls affect analysis. Scenario 08 labels one compound case `PAIRED_CONTROL` without a paired case. Sending `control_type` to a candidate leaks whether conservatism or execution is expected.

5. **No uniqueness guarantees.** The schema does not require unique `scenario_id` values across files, unique `case_id` values within or across scenarios, or unique required-observation IDs within a case. A harness that keys by an ID can overwrite or conflate records while all individual files remain schema-valid.

6. **Evidence refs prove location, not claim support.** A pin has repository, commit, path, blob, and free-text `claim_scope`, but no extraction range, quoted proposition digest, evidence role, or case link. Correct blob IDs therefore do not establish that the expected outcome follows from the source. This becomes material for scenarios 05-08, whose sources state working research constraints or implementation limitations rather than the unique answer vector in the synthetic fixture.

7. **No fixture integrity or canonicalization.** There is no digest for the candidate-visible input projection, no JSON canonicalization rule, no input version, and no binding from a run to exact case bytes. A run can claim the frozen scenario while feeding a modified object.

### Observation schema

1. **Required observations are not required by the schema.** `observations` may be empty. The schema does not require an entry for every case-level `required_observation`, does not prohibit extra IDs, does not require unique IDs, and does not require `observed: true` for a pass.

2. **`evidence_required` is unenforced.** An observation may have an empty `evidence_refs` array. A runtime evidence item may use any nonempty `kind` and `locator`, a null or arbitrary digest, and an empty description. There is no requirement that a locator resolves, that a digest matches, or that evidence predates the adapted assertion.

3. **Conflict, unknown, and loss records are content-free.** `retained_conflicts`, `retained_unknowns`, and `loss_disclosures` are arrays of arbitrary objects; `{}` is valid. There are no identifiers, sides, scopes, provenance pointers, missing-information fields, or loss classes. Mere array non-emptiness can be staged without retaining the relevant semantics.

4. **Native-to-adapted faithfulness is unobservable.** `candidate_native_result` accepts any JSON value, including `null`, and has no digest or external immutable locator. No observation or outcome has a required JSON Pointer/source span into the native result. The instruction to preserve native output "verbatim" and not improve it is therefore not checkable.

5. **No adapter identity.** There is no `adapter_ref`, adapter commit, adapter blob/digest, adapter configuration, runner ref, or mapping-version field. `adapter_sloc` is not an identity or integrity control. PRE_REGISTRATION's adapter-freeze condition cannot be demonstrated by an observation.

6. **Git refs are syntactic only and under-bound.** `candidate_ref` and `spec_ref` contain only arbitrary repository text and a 40-hex commit. The schema does not require the expected repository, does not bind `spec_ref` to the scenario file bytes, does not bind `candidate_ref` to `candidate_id`, and has no dirty-tree or submodule/dependency state.

7. **Outcome/reason contradictions validate.** `refusal_reason` may be null for `REFUSE` and non-null for `EXECUTE`. `reconstruction_evidence` and `produced_artifacts` may be empty for `EXACT` and `EXECUTE`. Conversely they may be populated for `NON_RECOVERABLE` with no explanation. The authority boundary is a constant boilerplate and does not record scenario-local input authority or the authority supporting an action.

8. **Complexity can be almost entirely unknown or misleading.** All numeric fields may be null. There is no fixture-set ID, measurement method, warm/cold distinction, repeated-trial summary, language rule for SLOC, shared-code allocation, operator-step count, failure-recovery count, or ingest/query/mutation/reconstruction split promised by `PRE_REGISTRATION.md:147-157`. A candidate can report zero implementation files or exclude capabilities supplied by Git, shell tools, a model, or manual adjudication.

9. **No adjudication record.** The schema has no expectation-met label, grader IDs, blinded order, disagreement, evidence sufficiency result, forbidden-behavior findings, or reason for pass/fail. The pre-registration defines a semantic judgment that the schema cannot reproduce or audit.

### Required schema correction

Use at least three separate artifacts with schemas and digests:

- a candidate-visible neutral `case_input` containing randomized opaque IDs and only operational inputs;
- a grader-only `case_key` containing allowed outcome **tuples**, required/forbidden conditions, evidence standards, and adjudication examples; and
- a `run_observation` containing pinned candidate, adapter, runner, input, and native-output refs plus source pointers from every adapted claim to native output/evidence.

Cross-file uniqueness and referential integrity must be checked by the harness, because JSON Schema validation of isolated files is insufficient.

## Outcome-axis ambiguity

The README defines `recoverability` as "What reconstruction claim is supported?" and `plan_status` as "Is an admissible plan available?" The cases do not use those axes consistently.

- Scenario 03 sets `recoverability: EXACT` for equality of already committed local/remote Git blobs. No reconstruction is requested or performed. `NOT_APPLICABLE` is the definition-consistent value unless the axis is renamed to preservation/fidelity.
- Scenario 07 sets `recoverability: UNKNOWN` for a same-identity query. Again no reconstruction is requested. This inflates an unrelated uncertainty into a second unknown axis.
- Scenarios 02 and 04 set `NO_SAFE_PLAN` even though the requested operation is primarily an authorization/certification decision. A safe plan may exist to preserve evidence, request authority, or return a non-exact derivative; it is the requested mutation or certification that must be refused. The specification does not say whether `plan_status` concerns the exact requested action, any remediation plan, or a candidate's internal planner.
- Scenario 08 permits `recoverability: UNKNOWN` while requiring execution and service of rebuilt D. It does not state an acceptance policy under which an output with unknown recovery fidelity is safe to serve.
- `resolution: RESOLVED` is used both when the requested result is available and when the system has conclusively determined that the request is impossible. That can be coherent, but the specification never says whether `resolution` applies to the domain question, feasibility judgment, or operation outcome. Scenario 04 illustrates the ambiguity: reconstruction is impossible but the impossibility judgment is resolved.
- `decision: NOT_APPLICABLE` on query cases and `REVIEW` on identity/scope cases leave unclear whether review is an action posture for queries or only for mutations. There is no positive case that distinguishes legitimate `REVIEW` from legitimate `REFUSE` for missing authority/evidence.

Define the referent of every axis, publish valid tuple invariants, and add examples that disambiguate "question resolved as impossible" from "requested value resolved." Do not score independent axis membership until that is done.

## Per-scenario adversarial assessment

### 01 — stale status versus checkpoint: redesign, do not use as-is

The evidence does support the incident: `CURRENT_STATUS.md` says Round-1 should launch next, while memories 16 and 17 record later state and memory 17 warns that `CURRENT_STATUS.md` may lag. The pins are correct.

The fixture nevertheless gives away the adjudication in `locator_claim`, `later_checkpoint_claim`, `records_must_be_retained`, the title, the case ID `recover_current_state`, and the operation name. It tests whether a candidate repeats a supplied "later checkpoint" label. It does not require computing temporal order from Git history, record metadata, or a declared succession relation. A "memory 17 always wins" rule passes; there is no counter-case where `CURRENT_STATUS` is actually updated/latest, where a later-numbered record is non-authoritative, or where two later records conflict.

Redesign with opaque record IDs and Git-pinned contents. Make the candidate derive ordering from signed/committed succession evidence, and add counter-cases for a repaired current locator, a later but out-of-scope note, and genuinely unresolved recency.

### 02 — recommendation without authority: retain premise, add a positive pair and fix plan semantics

The authority/refusal premise is strongly supported by memories 13 and 14. The test input, however, literally supplies `explicit_implementation_trial_authorization: false` and `explicit_shared_baseline_merge_authorization: false`, while the title and case ID say "without authorization." No authority model is exercised.

There is no positive paired case in which the exact scoped authorization is present and the requested isolated action may execute. Thus an always-refuse authority module passes this entire failure family. `NO_SAFE_PLAN` is also overclaimed: a safe non-mutating plan to preserve evidence and request authorization may exist even though no safe plan to execute the requested shared mutation exists. Scope the plan axis explicitly to the requested operation, or use `NOT_REQUESTED` and make refusal the tested posture.

Add cases for exact authority present, authority present but wrong scope, revoked/superseded authority, and valid trial authorization that still does not authorize mainline merge.

### 03 — canonical Git blob identity: retain incident, redesign the fixture and add failure cases

Memory 15 supports the corrected canonical Git-blob gate and all listed resume conditions. But the fixture supplies the two equal canonical SHA-256 values plus booleans saying remote commit matches, local blob matches, the EOL explanation is true, isolation is confirmed, the artifact is unchanged, safety is confirmed, and Phase 2 was not read. It tests a conjunction of already-decided booleans, not Git evidence verification.

The filename, title, and request disclose that execution is expected. `recoverability: EXACT` is axis misuse. There is no negative pair for a commit mismatch, canonical blob mismatch, unverified EOL cause, changed freeze, lost isolation, or premature Phase-2 read. An always-resume implementation passes this family.

Provide an isolated fixture repository/refs and require the candidate to compute the committed bytes and ref equality. Keep the working-tree digest only as diagnostic input. Add one negative case per resume condition and set reconstruction recoverability to `NOT_APPLICABLE` unless the axis definition changes.

### 04 — normalized is not byte-exact: core refusal is sound, fixture leaks originals and `NON_RECOVERABLE` is too absolute

The code and test evidence support the claim that the current snapshot normalizes/omits source distinctions while retaining only a raw digest and normalized atoms. Refusing an unsupported exact certification is correct.

However, the candidate-visible fixture includes both `source_bytes_a_escaped` and `source_bytes_b_escaped`, the very bytes meant to demonstrate loss. That is answer leakage and can also undermine the phrase "from the snapshot alone" if the runner makes the whole `given` object available. A raw hash is not generally reversible, but `NON_RECOVERABLE` needs a defined source domain and available external evidence. For a small known candidate domain, a retained digest can identify the original; if an exact Git source remains addressable, exact recovery may be possible from outside the snapshot. The invariant is that normalized equality alone cannot certify byte-exact recovery, not that recovery is universally impossible.

Give the candidate only the snapshot and request. Keep reference originals and collision/non-injectivity proof in a hidden oracle. Add a positive case whose snapshot actually includes the original bytes and a case where an external exact source is supplied. Score refusal of unsupported certification separately from global recoverability.

### 05 — scoped authority conflict: the negative case is semantically ambiguous

Two assertions with different authority scopes are not necessarily conflicting. They can both be true within their own scopes. With no query scope, the result is underdetermined/unknown; calling it a conflict is a separate modeling choice. The allowed outcome `CONFLICT` or `UNKNOWN` masks this ambiguity and lets candidates with materially different semantics both pass. The title prejudges them as conflicting while the required observation says the missing scope is the reason resolution is unavailable.

The positive explicit-scope control is useful but trivial because `scope_match_is_unambiguous: true` is supplied. Split this into distinct cases:

- compatible cross-scope assertions plus missing query scope -> `UNKNOWN`, retaining alternatives but not falsely asserting conflict;
- same-scope incompatible assertions with no precedence -> `CONFLICT`;
- explicit matching scope with one assertion -> `RESOLVED`;
- explicit declared precedence/evidence -> resolved under that policy; and
- ambiguous/multiple matching assertions -> conflict/review.

Do not expose a boolean that tells the candidate the match is unambiguous.

### 06 — preservation before cost: useful harness control, weak candidate discriminator

This pair correctly blocks literal always-refuse and cheapest-wins strategies. It is the strongest-formed pair in the package. But `requirements`, `preserves`, `loses`, `cost`, and `budget` directly encode a two-row set-inclusion exercise. A generic constraint filter passes without demonstrating that a candidate can discover, justify, or retain real preservation properties. The required observation even treats the supplied `preserves` list as capability evidence.

Keep it as a harness sanity control, not as strong evidence for a Byul candidate. Add hidden cases with incomplete/contradictory capability claims, unknown cost, a plan whose preservation claim must be verified from an artifact, multiple equally admissible plans, and authorized preservation relaxation. Otherwise C1/C2 can implement exactly this public miniature solver.

### 07 — split/merge identity unknown: missing the decisive counter-case and misusing recoverability

Memory 11 and memory 17 support not forcing timeless same-as identity without a policy. `UNKNOWN` is a defensible resolution. The synthetic lifecycle is not an actual documented incident, and the sources do not uniquely require `decision: REVIEW` rather than refusal to answer under absent policy. `recoverability: UNKNOWN` is unrelated to an identity query and should be `NOT_APPLICABLE`.

All answer cues are explicit: `identity_policy: null`, `equivalence_evidence: []`, `stable_handle_claim: null`, and the case ID `identity_policy_absent`. There is no paired case with a declared, scoped identity policy and sufficient evidence. An identity module that always returns unknown passes.

Add at least: policy/evidence sufficient for scoped SAME; policy/evidence sufficient for DIFFERENT; policy present but out of scope; conflicting policies; and lineage known while equivalence remains unknown. Use opaque event/entity labels and do not expose the expected absence in the case ID.

### 08 — source mutation invalidation/rebuild: remove and replace before freeze

This is the clearest unsupported expected outcome.

The input states that D depended on B0 and U depended on OTHER0, and that B1 succeeds B0. It does not supply:

- B0 or B1 content;
- a transformation capable of producing D from B1;
- an expected D value or oracle;
- a declaration that the dependency graph is complete, sound, and closed-world;
- an impact rule saying every B0->B1 successor affects D;
- a policy under which an unknown-fidelity D may be served; or
- evidence that U has no undisclosed/transitive dependency on S.

Despite that, the case requires `RESOLVED / EXECUTE / SAFE_PLAN`, production or selection of a D rebuilt from B1, and preservation of U as current. A correct conservative candidate may return `REVIEW` or `NO_SAFE_PLAN` because no transformation is available and the dependency graph's completeness is unknown. The case would falsely favor a candidate that invents a rebuild and assumes a closed world.

The cited v0.1 source/test prove that the current code has hard-coded dependencies and a virtual mutation; the source manifest says not to overwrite predecessors and to record exact successor targets. They do not prove this fixture is rebuildable, that absence from a list proves non-impact, or that execution is safe. `recoverability: UNKNOWN` being allowed does not solve the missing transformation.

Remove this case from the frozen set. Replace it with an executable fixture containing exact source bytes, a pinned deterministic transformation, a complete dependency graph with integrity evidence, expected artifact digests, and explicit service policy. Pair affected and unaffected mutations, indirect dependencies, failed/partial rebuild, unchanged-content successor, incomplete graph, and blanket-invalidation attacks. Do not label a single compound case `PAIRED_CONTROL`.

## Missing counter-cases and degenerate strategies

The two positive controls only reject the literal global constants "always conflict/unknown" and "always refuse/no plan." They do not reject family-specific constants or answer-cue rules.

A candidate can use the following degenerate policy and avoid `DEGENERATE_CONTROL_FAILURE`:

- hard-code the two named positive cases to resolve/execute;
- refuse every mutation/certification case;
- return review/unknown for every scope/identity case; and
- copy the required-observation prose.

It passes the two degenerate gates and several negative cases despite lacking usable semantics. More subtly, an operation-name decision table can solve all ten public cases. No metamorphic variant checks whether behavior changes for the right causal reason.

Required counter-case gaps are:

- stale versus actually current locator (01);
- authorization present in the correct scope (02);
- Git mismatch/unsafe resume (03);
- byte-preserving snapshot or external exact source (04);
- true same-scope conflict versus compatible cross-scope facts (05);
- scenario 06 has a basic pair but lacks uncertain/false capability evidence;
- identity policy/evidence present (07); and
- executable, failed, unaffected, indirect, and incomplete-graph rebuild cases (08).

Each failure family needs at least one expectation-reversing pair that differs by one hidden causal feature. Opaque/randomized case IDs and field labels should prevent branch-by-name. Metamorphic generation should vary names, order, irrelevant fields, and serialization while preserving the expected result. A candidate that changes posture on those irrelevant changes must fail.

## Evidence and normativity problem

The exact Git evidence pins are accurate, but several scenario keys convert provisional working hypotheses into unique expected behavior while simultaneously declaring `normative: false` and `validation_claim: NONE`.

- Memories 16 and 17 explicitly call the convergence design evidence, note prompt/model-lineage correlation, and deny final architecture selection.
- Scenario 05 turns a broad scoped-authority constraint into an ambiguous conflict-vs-unknown fixture.
- Scenario 06 turns "preservation before cost" into a toy planner oracle.
- Scenario 07 turns non-forcing identity guidance into a mandatory review vector.
- Scenario 08 turns limitations of the current code and a source-successor rule into a mandatory executable rebuild.

It is legitimate to compare candidates against provisional obligations, but the result must be described as agreement with a chosen hypothesis surface, not independent semantic preservation. Each expected outcome needs a separately adjudicated derivation explaining which part follows deductively from the fixture, which part is Owner direction, and which part is an experimental convention. The current free-text `claim_scope` does not do this.

## Public scoring and candidate-favoring thresholds

1. **All-or-nothing case scoring is not reliable without an evidence rubric.** "Every required observation is evidenced" and "no forbidden behavior occurs" are human semantic judgments, yet there is no adjudication protocol, examples, number of graders, disagreement rule, or evidence-sufficiency threshold.

2. **Cases and families are unequally weighted.** Ten cases give two cases each to scenarios 05 and 06 but one each elsewhere. Authority/scope and preservation/planning dominate, while split/merge identity and real invalidation have one synthetic case each. Scenario 08 has five required observations and scenario 05's cases have two; binary scoring makes their difficulty and information content incomparable.

3. **No candidate selection rule is pre-registered.** The pre-registration says publish vectors and not hide individual failures, but does not define how public cases, holdout cases, degenerate gates, complexity, missing metrics, or cold-read results affect eligibility. A later narrator can favor any candidate by emphasizing its preferred dimension.

4. **Complexity does not have an analysis rule.** H3 says C1 may equal/outperform at lower complexity, but "equal," "outperform," "materially lower," and the complexity tradeoff are undefined. Null measurements are allowed and are merely not imputed. There is no Pareto, dominance, minimum-effect, or cost-normalization criterion.

5. **Development exposure is asymmetric.** C0 was implemented before the public surface; C1 and C2 are explicitly unimplemented and will be built after every public answer is visible. Public success therefore favors the later candidates' opportunity to fit the test. Only a strong holdout could compare them fairly.

6. **C3's gate is subjective and conflicts with holdout freeze.** "ordinary implementation defects," "repeatable catastrophic evidence-loss failure," "causal analysis," and "materially simpler" are undefined. The gate requires failures to persist after fixing ordinary C2 defects, but holdout rules prohibit tuning candidates after exposure. The specification does not say whether a fresh successor holdout is required. This can be gamed either to open C3 or keep it closed.

7. **Candidate-charter boundaries are label-sensitive.** C1 may use Git history and manifests but not a "ledger"; C2 is defined by append-only records. The semantic boundary between an explicit Git log/index and a ledger is not operational. Capability supplied by external Git/shell/model/manual work is only requested as disclosure, not captured in the observation schema.

8. **The pre-registration freeze is under-specified.** `SPEC_FREEZE_COMMIT` remains `UNASSIGNED_UNTIL_COMMITTED`, with an instruction to record it in a future run manifest, but no run-manifest schema/path exists. There is no digest binding scenario inputs, keys, adapters, runner, resource limits, and candidate refs into a single run identity.

## Cold-read instrument is gameable and confounded

### Direct answer-key leakage

The treatment reader receives the commit containing this semantic-surface tree (`PRE_REGISTRATION.md:127-131`). The tree contains `cold_read/RUBRIC.md`, and `spec/README.md:62-71` explicitly tells the reader to open the questionnaire and rubric. The rubric states the desired two-point answers, including the exact candidate/non-claim distinctions and test battery. The scenario titles, allowed outcomes, required observations, and forbidden behaviors provide additional answer prose.

The baseline reader cannot see any of this. A treatment improvement can therefore be caused by access to the grading key, not improved discoverability or comprehension. The rubric must be held outside both repository arms and inaccessible to readers. Treatment readers should receive only the intended user-facing surface, not grader keys, expected outcomes, or candidate charters that directly answer the questionnaire.

### Blinding failure

Readers are required to cite repository paths. Treatment-only paths identify the arm to graders immediately, so grader blinding to study arm is not achievable. Randomizing answer order does not hide citations or vocabulary. Either redact/normalize citations for a first blind content grade and grade evidence separately, or abandon the blinding claim and quantify the resulting bias.

### Baseline provenance failure

`BASELINE_8133E3D_CONTEXT_BLIND_01.md` lives in the same initial commit as the pre-registration, rubric, and scenarios. There is no earlier immutable commit/digest containing the raw baseline response and no external timestamped registration. The report's assertion that the execution tree was not inspected is not independently verifiable.

It also does not fully record the questionnaire-required metadata: no elapsed time, no exact ordered list of every path opened, and no explicit prior-exposure answer. The "read-path finding" is an inferred apparent path, not a navigation log. Its 11/16 table appears self-graded in the same document rather than graded in blinded randomized order by identified independent graders. It should not be used as the pre-registered baseline median.

### Threshold and measurement loopholes

- "At least two model lineages and at least two human readers when feasible" gives no minimum valid sample; "when feasible" can reduce the experiment to one convenient reader.
- The 25%-of-baseline-to-perfect-gap rule does not define whether medians are taken per reader total or per question, how even-sample half-points are handled, what happens at ceiling, or whether the baseline/treatment sample sizes must match.
- With the recorded 11/16 baseline, the stated improvement threshold is 1.25 points, but totals are integral per reader and medians may be half-integral. No rounding or inequality convention is registered.
- "No decline on authority, candidate-status, or refusal questions" does not map those labels unambiguously to questionnaire numbers or say whether decline is individual, median, or aggregate.
- No power analysis, confidence interval, randomization method, exclusion rule, missing-response rule, grader-count rule, or inter-rater agreement floor is specified.
- The treatment may include both semantic-surface files and separately authorized locator/state-map changes. That bundles two interventions and prevents attributing improvement to either.
- Rubric rows are compound and subjective. Q5 and Q7 substantially double-count candidate/non-selection status; Q3 and Q6 overlap loss/refusal; Q1 and Q2 overlap source/derived ordering. A one-point grading change on overlapping language can cross the threshold.
- Critical misunderstandings are recorded but do not block the visibility signal. A reader can improve total score while still committing `TEST_PASS_AS_VALIDATION` or another critical error outside the three vaguely protected questions.

Pre-register a separate, inaccessible grading key; a minimum balanced sample; exact randomization; independent dual grading; an adjudication rule; reliability and critical-error gates; exact threshold arithmetic; and a factorial comparison of locator-only versus semantic-surface-only changes.

## Holdout rules are insufficient against template gaming

The holdout directory correctly contains no cases or answers, and it requires exact source pins, category balance, both refusal/execution and unresolved/resolvable cases, frozen digests, equal inputs, and contamination reporting. Those are useful foundations. They do not yet define a credible holdout experiment.

1. **No minimum size or per-family replication.** "Balance at least four failure families" can be satisfied with four hand-picked cases, one per family. That cannot distinguish general behavior from luck/template matching and gives one selector enormous discretion.

2. **No sampling frame or selection log.** An independent selector chooses cases but no eligible incident population, random sampling method, inclusion/exclusion criteria, difficulty calibration, or rejected-case log is required. Selector discretion can favor a candidate even without implementation authorship.

3. **Independence is too weak.** The selector is barred only from authoring candidate implementations. They may have authored public scenarios, adapters, charters, or the favored architecture; may inspect candidate code/results; and may also grade. Require role separation and conflict disclosure, and blind selection/adjudication to candidate identity where possible.

4. **Near-public clones are allowed.** A "minimal transformation" of a pinned incident may be isomorphic to a public case. Because C1/C2 authors see all public keys before implementation, renamed-symbol clones do not test generalization. Specify structural distance, prohibit reuse of public field names/operation names, and include novel combinations and expectation reversals.

5. **Input/key separation is not stated.** Candidate/adapter authors may access "holdout material" after refs freeze, but the rules do not define separate candidate-visible inputs and grader-only answers. If the same scenario shape is used, `allowed_outcomes`, `control_type`, and required/forbidden prose can be exposed at run time. Freeze does not prevent a generic answer-key reflector.

6. **Private manifest is untyped and unauditable.** No schema, canonicalization algorithm, digest algorithm, custodian, access log, encryption/storage boundary, timestamping service, or post-run audit procedure is defined. The requested extraction range/transformation/loss fields do not exist in the public scenario evidence schema.

7. **Expected answers have no derivation protocol.** The rules do not say who authors expected outcomes, whether they are frozen before candidate results, how many independent adjudicators are required, how ambiguity is handled, or when a case must be discarded before exposure. Public scenario 08 shows why selector-authored answers need adversarial review.

8. **Contamination exclusion can bias comparisons.** The "affected run" is excluded, but it is not specified whether the same case is removed for all candidates, counted as missing/failure, or replaced from a pre-frozen reserve. Candidate-specific exclusion can erase an unfavorable result or leave unequal case sets.

9. **Equal resource limits are undefined.** Different adapters and candidates can use manual adjudication, Git, shell tools, language runtimes, or model calls with no common accounting rule. "Identical inputs" does not imply equivalent information if adapters precompute candidate-specific features.

10. **No holdout success criterion.** There is no minimum accuracy, per-family floor, confidence interval, critical-failure gate beyond the two public controls, or registered relation between holdout and public results. Narrative selection remains possible.

Create a holdout manifest schema and a precommitted encrypted/digested bundle with separate opaque input and key files, dual independent keying, a meaningful minimum number per family, structural novelty rules, expectation-reversing pairs, pre-frozen reserve cases, common exclusion treatment, and an exact analysis plan. Use a custodian who did not author scenarios, candidates, adapters, or grading keys.

## What is presently defensible

The following elements should be preserved while redesigning:

- exact baseline commit and correct Git blob pins;
- explicit non-selection/non-validation boundaries;
- separation of resolution, action posture, reconstruction claim, and plan availability as an intent, after the axes are made precise;
- retention of conflicts, unknowns, loss, provenance, native output, and cost as comparison goals;
- positive-control intent in scenarios 05 and 06;
- candidate isolation and no post-holdout tuning;
- the requirement to publish per-case vectors rather than only an aggregate;
- the simplicity control and C3 richness gate in principle; and
- holdout contamination disclosure rather than silent rerun.

None of those strengths makes the present cases discriminating.

## Ranked mandatory correction list

1. **Separate candidate-visible input from grader-only keys.** Define schemas, canonical bytes/digests, randomized opaque IDs, and a runner-enforced projection. Never give candidates/adapters `allowed_outcomes`, control labels, required observations, forbidden behavior, rubric prose, or answer-revealing filenames.
2. **Remove and replace scenario 08.** Supply a real executable transformation, exact content, complete dependency evidence, output oracle, and affected/unaffected/failed/indirect/incomplete-graph pairs before requiring `EXECUTE / SAFE_PLAN`.
3. **Make adapter faithfulness auditable.** Add exact adapter/runner refs and immutable native-result refs; require every adapted outcome, observation, conflict, unknown, loss, artifact, and evidence claim to point into native output or independently verified runtime evidence. A null/empty native result must not be improvable into a pass.
4. **Define outcome semantics and allowed tuples.** Fix the referent of each axis, use tuple-level allowed outcomes, add cross-field invariants, and correct recoverability/plan-status misuse in scenarios 02, 03, 04, 07, and 08.
5. **Add expectation-reversing counter-cases for every failure family.** At minimum add current-locator, authorized-action, unsafe-Git, raw-preserved/external-source, genuine same-scope conflict, policy-present identity, and executable/failed rebuild pairs. Add metamorphic renaming/reordering variants.
6. **Split and redesign scenarios 04, 05, and 07.** Hide original bytes from the candidate; distinguish refusal of exact certification from universal non-recoverability; separate cross-scope underdetermination from same-scope conflict; and add scoped identity-policy positives. Treat scenario 06 as a harness sanity control unless capabilities are independently evidenced.
7. **Repair the cold-read experiment.** Keep the rubric and all expected-answer content inaccessible to both arms; cryptographically freeze raw baseline responses before authoring/committing the treatment; collect required metadata; make citation grading compatible with blinding; isolate locator versus surface interventions; and define samples, arithmetic, exclusions, reliability, and critical-error gates.
8. **Operationalize the holdout.** Pre-register a manifest schema, role separation, minimum replicated case counts, sampling/novelty rules, input/key separation, dual answer adjudication, access audit, reserve cases, common contamination handling, and exact per-family success thresholds.
9. **Strengthen both schemas and harness-level integrity checks.** Require unique IDs, nonempty/verified evidence, typed conflicts/unknowns/losses, outcome/reason/artifact consistency, input/spec/candidate binding, observation-key coverage, and cross-file referential integrity.
10. **Pre-register candidate comparison and complexity analysis.** Define per-family floors, public-versus-holdout priority, critical failures, uncertainty, Pareto/dominance or minimum-effect rules, complete cost accounting, shared/external capability allocation, and equal development/resource budgets.
11. **Resolve C3 gate contradictions.** Define ordinary defect, catastrophic failure, causal evidence, and materially simpler; prohibit repair on an exposed holdout and require a new pre-frozen successor holdout if C2 changes.
12. **Add an auditable run manifest and expectation derivations.** Bind the spec freeze commit, exact scenario input/key digests, candidates, adapters, runner, resource limits, native outputs, graders, and results. For every key, classify what is source-supported, Owner-directed, experimental convention, or unresolved rather than treating a correct blob pin as proof of the outcome.

SPEC_FREEZE = BLOCKED
