# Phase 1 Frozen Proposal — v0.1.09

ROUND_ID = `BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01`
ROUND_SLOT = `R09`
PROFILE = `MINIMAL_INFORMATION`
PHASE1_RESEARCH_BASELINE_COMMIT = `891e4bd4b999eacc99431ed0db05062901a68dd9`
PHASE1_INPUT_MODE = `EXACT_GIT_OBJECT_READS_ONLY`

This proposal was produced without reading the v0.1 implementation, another
run, a recovery branch, or a reservation branch's contents. The profile
pressure is minimal information: a field or model is admitted only if removing
it breaks a stated reconstruction, preservation, lifecycle, or audit property.

## CURRENT_STATE_RECONSTRUCTION

Byul is an active, non-normative research track, separate from the AAA mainline.
Its immediate technical problem is not yet to choose a universal world model.
It is to preserve and reconstruct an evolving research state while allowing
candidate representations to be tested without silently turning hypotheses,
unknowns, or derived views into facts.

The owner-adopted BYUL CORE-A principles are change/mutability,
non-substantiality/derived entity, composition/emergence, and conditional
relationality. They are research and design principles, not scientific axioms
or AAA-wide canonical requirements. The strongest owner worldview phrase is a
"composition network of countless local mappings," but the primitive algebra
remains open. Event, mapping, interaction, composition, rewrite, and typed
morphism remain competitors.

Petri, Open/Reconfigurable Petri, Occurrence Net, Event Structure, causal-order,
and LTS/reachability representations are current candidates with complementary
roles, not selected answers. Causal Set concepts are attractive as a causal
skeleton and reconstruction prior art, not as the final architecture. The
router `R(S,M,L)` and the priority of Preservation Demand are working
hypotheses. Reverse conversion is expected to be non-unique or lossy in many
cases; discarded semantics must not be hallucinated back into existence.

The most consequential earlier correction is epistemic: a canonical P-series
was never established. The safe authority is BYUL CORE-A plus explicit,
versioned preservation contracts. Any implementation that reports an automatic
principle PASS without separately defined gate semantics would overclaim.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

Within the pinned baseline, the following are documented states of the research:

- Byul is `WORKING / NON_NORMATIVE / NOT_VALIDATED`; production is unauthorized.
- Raw research memory and its provenance are the current primary data; current,
  history, open-question, model-family, and lifecycle structures are views.
- Candidate formalisms have distinct advertised roles, and no one formalism has
  been selected as canonical.
- Exact reconstruction, semantic equivalence, approximation, view dependence,
  and non-recoverability are distinct required loss classes.
- Initial-state reconstruction, lifecycle drift, invalidation radius, and
  transformation cost are explicit evaluation targets.
- The previous P-series abstraction was corrected as unsupported.

`SOURCE_SUPPORTED` here means supported by the supplied research memory, not
independently established truth about physics, philosophy, or the world.

### OWNER_DIRECTION

- Preserve the possibility of change, succession, derivation, composition, and
  context-dependent meaning.
- Do not reify objects, identities, boundaries, or global NOW without need.
- Prefer prior art and testable architecture over premature new theory.
- Preserve uncertainty and distinguish owner hypotheses from validated facts.
- Evaluate representations across mutation, composition, split, merge,
  migration, degraded operation, recovery, and succession.

### WORKING_HYPOTHESIS

- A complementary representation family may be better than one universal model.
- Preservation Demand may be the most important routing input.
- `R(S,M,L)` may choose a target model set, transformation path, preservation
  contract, and validation plan.
- Occurrence/fact history and behaviour/rule models may form complementary
  planes.
- High-scale entities may be derived persistent patterns with preserved lineage.

### OPEN

- The minimal primitive or algebra and whether one is needed at all.
- The minimum sufficient routing features and whether lifecycle requires a
  separate argument.
- Which semantics must be lossless for each workload.
- Translation conditions, reverse-synthesis ambiguity, and acceptance thresholds.
- Whether one or multiple authoritative representations are required.
- How to control replay, view, graph, reachability, and unfolding growth.
- How BYUL CORE-A conflicts are operationally detected without inventing a
  false automatic proof system.

### NON_CONCLUSION

- Petri Net is not canonical.
- Causal Set is not the final architecture.
- An event, mapping, or object is not established as the primitive.
- A causal link does not contain transformation semantics.
- An antichain is not an absolute simultaneity slice.
- A derived reconstruction is not ground truth.
- BYUL CORE-A is not a scientific proof or AAA production acceptance.

### YOUR_INFERENCE

The minimum stable authority should model *research assertions and their
provenance*, not commit to a world ontology. Candidate world/behaviour models
should be reproducible, disposable projections. This is the smallest boundary
that can preserve current meaning while leaving the primitive and model-family
questions genuinely open.

## MINIMAL_PROBLEM_DEFINITION

Given exact source artifacts and a succession of research assertions, maintain
enough immutable information to answer all of the following without invention:

1. What exactly was recorded, by whom or by what process, and from which source?
2. What epistemic force did it have: source-supported, owner direction, working
   hypothesis, open, non-conclusion, or the recorder's inference?
3. What followed, revised, invalidated, contradicted, or derived from what?
4. What is current at a selected branch/head and reducer version?
5. Which target view can answer a query under an explicit loss tolerance?
6. Can that view be rebuilt, audited, migrated, split, merged, and recovered?

Anything not needed for one of those questions is excluded from the authority
layer. In particular, a universal graph ontology, a Petri/Event/Causal/LTS
supermodel, a global total order, dense Situation Fingerprint, numeric truth
score, and automatic BYUL CORE-A theorem prover are not required.

## PHASE1_PROPOSAL

Use a **content-addressed, append-only provenance ledger with rebuildable views**.
It combines established patterns instead of proposing a new foundational
theory.

The authoritative substrate has only two object classes:

### 1. Artifact

An immutable byte sequence addressed by a cryptographic digest, with media type
and optional external locator. Original memos, datasets, model specifications,
code, test results, and metric receipts are Artifacts. Byte content, not a
normalized interpretation, is authoritative.

### 2. Ledger Entry

An immutable, canonically serialized record addressed by its digest:

```text
entry_id      := hash(canonical_entry_without_id)
parents       := zero or more ledger-entry IDs
operation     := ASSERT | RELATE
body          := assertion body, or a typed relation among entries/artifacts
epistemic     := required for ASSERT
provenance    := source anchors, attributed agent/process, recorded_at
valid_time    := optional; present only when the assertion itself is time-scoped
```

`epistemic` uses the supplied distinctions, not a numeric confidence proxy:
`SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`,
`NON_CONCLUSION`, or `YOUR_INFERENCE`. An assertion may quote an Artifact span
exactly or carry a structured interpretation; a structured interpretation must
point to its evidence and cannot inherit truth from the source merely by being
linked to it.

`RELATE` uses a registered, versioned relation vocabulary. The required seed is
small: `DERIVED_FROM`, `REVISION_OF`, `INVALIDATES`, and `CONTRADICTS`.
Additional relations such as `SUPPORTS` are admitted only with defined
semantics. Corrections and retractions are new entries; old assertions are never
edited or deleted. `recorded_at` is audit metadata, not proof of causal order.
Parents form a partial-order succession graph, so concurrent branches need not
be forced into a fictional global NOW.

A named branch/head is an operational reference to a set of reachable entries,
not an ontologically persistent object. A snapshot is `(head IDs, reducer
version, schema/vocabulary versions)`. Current state is a deterministic fold of
reachable entries. If relations leave an unresolved semantic conflict, the fold
returns `REVIEW_REQUIRED`; it never resolves conflict by timestamp or confidence
arithmetic.

The proposal deliberately does not require RDF, a graph database, or Git as the
physical store. JSON Lines plus an object directory and SQLite indexes is a
sufficient first implementation. PROV/RDF or another storage engine can be an
interchange projection if tests show value.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) separates entities,
  activities, and agents and defines derivation, revision, invalidation, and
  provenance bundles. The proposal uses this vocabulary as a mapping target and
  semantic discipline, while keeping the required local schema smaller.
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) records
  every state change as a durable event and rebuilds state or temporal views by
  replay. This supports append-only correction history and disposable views.
- [Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects.html)
  demonstrate a practical content-addressable object store with retained
  versions; [Trusty URIs](https://arxiv.org/abs/1401.5775) show how hashes make
  immutable artifacts and reference trees verifiable. A digest proves content
  identity, not truth.
- [Nanopublication guidelines](https://nanopub.net/guidelines/working_draft/)
  separate an assertion, its provenance, and publication information. Ledger
  assertions follow that separation without requiring every memo to become RDF.
- Snodgrass and Ahn's [Temporal Databases](https://experts.arizona.edu/en/publications/temporal-databases/)
  distinguishes valid time from database/transaction time. Therefore
  `valid_time` is optional and separate from mandatory `recorded_at`.
- Shapiro et al.'s [CRDT report](https://inria.hal.science/inria-00609399)
  justifies deterministic replica convergence under defined conditions. The
  ledger's immutable entry set may use grow-only-set union for transport, but
  CRDT convergence is explicitly not semantic conflict resolution.

The architecture is a conservative composition of these precedents. Its Byul-
specific contribution is only the explicit epistemic classification and
preservation/loss discipline demanded by the supplied problem.

## AUTHORITATIVE_REPRESENTATION

Authority is the pair `(content-addressed Artifacts, immutable Ledger Entries)`
reachable from a selected snapshot. Source bytes remain authoritative for what
was recorded. Ledger entries are authoritative for who classified or related a
claim, when it was recorded, and what lineage was declared. Neither is
automatically authoritative for whether a world claim is true.

The reducer, relation vocabulary, schema, and transformation code are versioned
Artifacts. This prevents a later reducer from silently changing the meaning of
an older snapshot. Stable handles are references only; succession is explicit.

## DERIVED_REPRESENTATIONS

Build only views required by measured queries:

- current research-state view;
- chronology and revision/lineage view;
- open-question and non-conclusion guard view;
- provenance/evidence graph;
- search index and compact initialization packet;
- on-demand Petri, Event Structure, causal-order, LTS, rewrite, metric/clock, or
  other executable/analytical model artifacts.

Every materialized view carries a manifest containing input snapshot IDs,
transform/reducer digest and version, query capability, preserved fields,
omitted fields, loss class, validation receipt, and invalidation dependencies.
A view may be cached or discarded. It becomes research evidence only if
re-ingested as a new assertion with provenance and the correct epistemic class.
It never silently becomes source truth.

## PRESERVATION_CONTRACT

The default is fail closed: an unspecified required semantic is not assumed
preserved.

Always `EXACT`:

- Artifact bytes, media type, digest, and source anchors;
- Ledger Entry canonical bytes, digest, parents, operation, typed relations,
  attribution/process, and recorded time;
- epistemic class, including `OPEN` and `NON_CONCLUSION`;
- explicit revision, invalidation, contradiction, and derivation lineage;
- snapshot head set and schema/reducer/vocabulary versions;
- transformation manifest and declared omissions.

Conditionally `EXACT` or `SEMANTIC`, as declared per transformation:

- normalized statement structure;
- trace, reachability, causality, concurrency, conflict, resource, metric,
  composition, and mutation semantics;
- current-state equivalence under a specified reducer.

`APPROXIMATE`, `STATISTICAL`, or `VIEW_DEPENDENT` is allowed only when the
contract names the field, method, bound/assumption, and consumer. `UNKNOWN` is a
value to preserve, not an invitation to impute.

## LOSS_AND_NON_RECOVERABLE

A digest cannot recover absent bytes or establish truth. Provenance cannot prove
that its source was honest. A text span does not capture unrecorded intent. A
normalized claim may omit rhetoric, ambiguity, typography, or context; the raw
Artifact is therefore retained.

A causal projection cannot recover transformation labels, conflicts, resources,
metric anchors, or alternatives that it discarded. An LTS may lose concurrency;
an occurrence history cannot recover all possible behaviour; a Petri-like model
cannot recover which run actually happened without an occurrence record.
Reverse synthesis may produce several compatible models and must not be labeled
an inverse.

If an Artifact, provenance anchor, relation meaning, or reducer version was
never stored, it is `NON_RECOVERABLE`. If cryptographic objects are physically
deleted, hashes detect the loss but do not repair it. These are hard limits, not
implementation bugs to conceal.

## TRANSFORMATION_PATHS

1. **Ingest:** bytes -> Artifact. This path is byte-exact and hash-verified.
2. **Interpret:** Artifact span -> ASSERT entry. This is a documented human or
   machine interpretation; exact source anchoring does not make the
   interpretation exact.
3. **Evolve:** existing entry -> new ASSERT plus `REVISION_OF` or
   `INVALIDATES`. History remains reachable.
4. **Project:** snapshot -> view plus manifest and validation receipt.
5. **Rebuild:** snapshot + exact reducer/transform -> derived view. A mismatch
   is an error, not an accepted replacement.
6. **Round trip:** export/import Artifacts and Entries -> identical digests and
   heads. Model-view round trips are graded by declared semantics, never by file
   equality alone.
7. **Promote evidence:** view result -> new Artifact/ASSERT with full provenance;
   no direct write-back into old authority records.

Each transform declares a monotone preservation set: semantics claimed at its
output cannot exceed the intersection of semantics present at its inputs and
semantics the transform has demonstrated it preserves. New inferences are
allowed, but are new classified assertions, not recovered facts.

## LIFECYCLE_BEHAVIOR

- **Create:** ingest exact source Artifact; append classified assertions.
- **Operate/accumulate:** append entries; incrementally update disposable indexes.
- **Mutate/correct:** append revision or invalidation relations; never overwrite.
- **Compose:** union immutable object sets under preserved namespaces and source
  anchors; append a multi-parent composition entry.
- **Split/diverge:** create two heads over the same ancestry; subsequent entries
  carry their own parents and provenance.
- **Merge:** set-union entries, then detect incompatible active assertions and
  missing objects. Unresolved semantic conflicts remain explicit and return
  `REVIEW_REQUIRED`; no last-write-wins rule.
- **Migrate:** retain the old snapshot, append a migration receipt naming old/new
  schemas and transformation digest, and verify preservation invariants.
- **Degraded mode:** serve only views whose input objects and manifests verify;
  otherwise expose incompleteness rather than fabricate state.
- **Recover:** verify object hashes, restore a checkpoint, fetch remaining
  entries, replay the pinned reducer, and compare view digests/invariants.
- **Successor/retire:** move operational heads to a successor while retaining
  predecessor lineage; invalidate stale views, not historical evidence.

Compaction may create a verified checkpoint for speed but cannot delete source
objects required by the retention policy. Physical deletion is a separate
governance operation with an explicit non-recoverable-loss receipt.

## ROUTING_POSITION

Do not persist the large candidate `Situation Fingerprint` as canonical state.
Use a smaller capability-matching planner:

```text
Plan(Q, P, A) -> {view set, transformation path, validation plan} | REVIEW_REQUIRED
```

- `Q`: requested query or lifecycle operation, including required service limits.
- `P`: field-level preservation/loss contract; absent requirements fail closed.
- `A`: available authoritative snapshot and registered view capabilities,
  lineage, validity, and cost observations.

This is a compression, not a rejection, of `R(S,M,L)`: map the situation's
question/workload and lifecycle verb into `Q`, its Preservation Demand into
`P`, and current model state into `A`. Add a separate feature only after two
otherwise identical `(Q,P,A)` cases require different safe plans. This gives a
direct ablation criterion for minimum sufficient routing information.

The planner selects existing registered capabilities; it does not infer that a
model preserves a semantic because the model's name suggests it. Unknown
preservation or stale validation returns `REVIEW_REQUIRED`.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY:** corrections are successor entries, not destructive
  mutation; branch heads and current states can change while history persists.
- **NON-SUBSTANTIALITY / DERIVED ENTITY:** stable IDs and materialized objects are
  handles/views, not claims about ultimate substance. No world-object ontology
  is forced into authority.
- **COMPOSITION / EMERGENCE:** multi-parent composition preserves local-to-
  composed lineage; high-level models are derived artifacts whose sources remain
  inspectable.
- **CONDITIONAL RELATIONALITY:** assertions retain scope, provenance, relations,
  and branch context. Concurrent histories remain partially ordered instead of
  receiving an invented total order.

Alignment is reviewable design evidence only. It is not automatic scientific,
owner-acceptance, or production PASS.

## EXPECTED_FAILURE_MODES

- Claim extraction or scope selection may itself distort meaning.
- A vague relation vocabulary can turn the ledger into an unqueryable edge pile.
- Replay and provenance traversal can grow without checkpointing and indexes.
- Canonical serialization or schema evolution bugs can destabilize identifiers.
- A reducer change can alter current-state output unless its version is pinned.
- False or incomplete provenance remains false or incomplete despite hashing.
- Semantic conflict detection may miss contradictions expressed at different
  granularities or in natural language.
- Multi-parent union guarantees object convergence, not epistemic agreement.
- View manifests may overclaim preserved semantics; independent tests are needed.
- Retention, privacy, or legal deletion requirements may conflict with an
  immutable history and need explicit governance beyond this proposal.
- The two-object-class minimum may be too weak for high-volume simulation or
  exact domain metrics, requiring specialized authoritative stores for those
  domains rather than ever larger generic entries.

## FALSIFICATION_TESTS

1. **Initialization challenge:** blind instances reconstruct the pinned state
   from ledger-derived packets. Any promotion of open/non-conclusion to fact is
   a hard failure.
2. **Ablation:** remove, one at a time, exact source bytes, epistemic class,
   provenance, parents, revision/invalidation, or transform loss manifest. If
   removal does not reduce reconstruction or lifecycle safety on the corpus, the
   field is not minimal and should be dropped or made optional.
3. **Router counterexample search:** generate paired scenarios with equal
   `(Q,P,A)` but allegedly different safe plans. A valid pair falsifies the
   compressed planner and identifies a missing input.
4. **Model comparison:** compare flat raw documents, this ledger, a general RDF
   knowledge graph, and a preselected Petri/Event family on the same MI and
   lifecycle scenarios. If the ledger yields no fidelity or audit gain over raw
   documents, its semantic layer is unjustified.
5. **Loss trap:** project away a known field, then request it after a round trip.
   Any exact answer without retained evidence is a hard failure.
6. **Concurrent conflict:** branch from one head, append incompatible claims,
   merge, and verify that both survive and current state is `REVIEW_REQUIRED`.
7. **Reducer drift:** replay one snapshot with two reducer versions. Unannounced
   output differences are a hard failure; announced differences require a
   migration decision.
8. **Tamper and missing-object tests:** mutate one byte or remove one referenced
   object. Verification must fail before a view is served as complete.
9. **Scale tests:** fan-out/fan-in, dense contradiction links, long revision
   chains, and repeated split/merge must stay within declared storage, rebuild,
   query, and invalidation budgets.

## IMPLEMENTATION_TEST_PLAN

No implementation is authorized here. A later authorized trial should begin
with the smallest substrate: SHA-256 object files, canonical JSON Lines entries,
SQLite indexes, a versioned deterministic reducer, and manifest-bearing view
adapters.

Required tests for that trial:

- schema and canonicalization golden vectors across platforms;
- byte-exact artifact export/import and snapshot digest equality;
- deterministic replay from empty state and from checkpoints;
- property tests for append-only history and idempotent set-union merge;
- correction/retraction tests proving predecessor visibility;
- classification tests proving `UNKNOWN`, `OPEN`, and `NON_CONCLUSION` cannot
  become positive assertions through defaulting;
- provenance-anchor tests for byte ranges and source versions;
- transformation contract tests for every claimed preserved semantic;
- stale-view invalidation and bounded incremental rebuild tests;
- branch/split/diverge/merge/migrate/recover scenarios with deliberate conflicts;
- authorization tests separating observation, owner direction, inference, and
  acceptance authority;
- benchmark comparison against raw-file-only and richer-graph baselines.

Acceptance should use hard semantic gates first, then compute/maintenance cost.
No numeric score may compensate for lost epistemic class, invented semantics,
unverifiable provenance, or a false exact-recovery claim.

## OPEN_UNKNOWNS

- The exact statement granularity and anchor format for multilingual Markdown.
- Whether `OWNER_DIRECTION` is an epistemic class, authority class, or two fields
  once more actors and governance layers appear.
- The smallest relation vocabulary that still catches material contradiction.
- Whether optional valid time is needed in the first corpus.
- Which reducer semantics define "current" for partially ordered conflicts.
- Which model-specific semantics merit authoritative rather than derived status.
- What retention/deletion policy is permitted for sensitive source artifacts.
- Quantitative limits for replay latency, object count, invalidation radius, and
  view rebuild cost.
- Whether the compressed planner is sufficient outside the current memory corpus.
- How owner acceptance and independent validation receipts should be represented
  without conflating attribution with truth.

## WHY_THIS_COULD_BE_WRONG

The proposal may optimize the control plane while under-modeling the world-model
problem. Natural-language assertions plus typed relations may be too weak for
simulation, causal discovery, or executable behaviour. A richer formalism might
need to be authoritative for some domain rather than a derived view. Conversely,
the ledger may still be unnecessary: exact versioned documents plus disciplined
human review could outperform it at the present scale.

Event sourcing also moves complexity rather than eliminating it: event schema,
reducer evolution, replay, and invalidation become critical infrastructure. The
proposed relation seed may be insufficient, while a larger vocabulary would
violate the minimal-information pressure. Content addressing verifies identity,
not semantics or trustworthiness. Finally, folding partially ordered assertions
into one current view may itself impose more unity than the research warrants.

The proposal should therefore survive the ablation and competing-baseline tests
before it is treated as a successor architecture. Its strongest claim is narrow:
it is a minimal, implementable authority layer for preserving research meaning,
not a final model of reality.
