# BYUL v0.1 Parallel Proposal Round-1 — Phase 1

## Execution metadata

- ROUND_ID = `BYUL-v0.1-PARALLEL-PROPOSAL-R1`
- ROUND_SLOT = `R01`
- RUN_ID = `v0.1.01`
- COHORT = `ROUND1_10_RUN`
- PROFILE = `NEUTRAL_BLIND`
- RESEARCH_BASELINE_COMMIT = `891e4bd4b999eacc99431ed0db05062901a68dd9`
- PHASE1_FROZEN = `TRUE`
- STATUS = `RESEARCH_PROPOSAL / NON_NORMATIVE / NOT_VALIDATED`

This proposal was produced from the exact research baseline above before reading
the current v0.1 README, model contract, source manifest, implementation, or
tests. It does not rank this or any other run.

## 1. Current-state reconstruction

Byul is an independent research track concerned with representing changing
research memory/state, not a continuation of AAA mainline model design. Its
high-resolution worldview explores a network of composable local mappings in
which objects, identities, boundaries, and personas may be persistent derived
patterns rather than primitive substances. Succession and lineage are therefore
more central than permanent identity, and a global absolute `NOW` should not be
silently imposed.

`BYUL CORE-A` currently contributes four owner-adopted research constraints:
change/mutability, non-substantiality/derived entities, composition/emergence,
and conditional relationality. They constrain modeling assumptions but neither
select a formalism nor prove a scientific or philosophical claim.

The current model-family discussion is deliberately non-final. Petri/Open
Petri/Reconfigurable Petri candidates express possible behaviour, resources,
composition, and rule/topology change. Occurrence nets and event structures can
express occurrence history, causality, concurrency, and conflict. Causal-order
and LTS/reachability structures can be purpose-specific views. Causal-set ideas
are attractive as a causal skeleton and reconstruction precedent, but discarded
transformation meaning cannot be recovered and link storage is not necessarily
sparse. The proposed `R(S,M,L)` router makes situation, current model state, and
lifecycle context explicit; preservation demand may be its most important
situation feature. None of these candidates is canonical.

The active implementation problem is thus not “find the one true world model.”
It is to preserve changing evidence, claims, decisions, uncertainty, lineage,
and loss boundaries while constructing fit-for-purpose models and views that
can be invalidated and rebuilt.

## 2. State classification

### SOURCE_SUPPORTED

- The exact baseline records the Byul project state, candidate formalism roles,
  lifecycle questions, proposed simulations, version boundary, and terminology
  correction.
- The baseline treats partial order, Petri-family behavior, occurrence/event
  structures, reachability views, and reconstruction classes as prior-art
  concepts or candidate uses, not as validated architecture choices.
- The former claim that a canonical `P-series` exists was corrected: no such
  formalized series is evidenced in the available research record.
- The research record itself is non-normative and not scientifically validated.

### OWNER_DIRECTION

- Preserve and apply BYUL CORE-A without treating it as physics or ontology
  proof.
- Prefer succession/history/lineage over an unexplained permanent identity.
- Keep high-resolution worldview exploration separate from implementation
  abstraction.
- Use prior art first, disclose semantic loss, and measure lifecycle and
  transformation behavior.

### WORKING_HYPOTHESIS

- A complementary model family may be better than a universal representation.
- `R(S,M,L)` may be a useful routing decomposition.
- Preservation demand may dominate phenomenon labels when selecting a view.
- Objects and identities may be derived persistent patterns at some scales.
- A fact/occurrence plane and a behavior/rule plane may be complementary.

### OPEN

- The primitive or minimal algebra: event, mapping, interaction, composition,
  rewrite, typed morphism, or a smaller/different grammar.
- Which semantic dimensions must be exact, semantic, approximate, or droppable.
- Whether there should be one or multiple authoritative representations.
- Minimal sufficient routing features and whether `R(S,M,L)` is the right API.
- Translation, reverse synthesis, scaling, mutation, and lifecycle acceptance
  thresholds.
- Whether the worldview has explanatory value beyond research organization.

### NON_CONCLUSION

- Petri is not the canonical model.
- Causal Set is not the final architecture or a physics proof.
- Events, mappings, or objects are not established primitives.
- A derived reconstruction is not ground truth.
- A dropped semantic dimension is not automatically recoverable.
- No global time, exact metric, or total order may be invented from causal
  incomparability.

### YOUR_INFERENCE

- The immediate engineering problem is best formulated as an
  evidence/decision evolution and derived-view problem, rather than as the
  choice of an ontology for reality.
- Authority should be typed by information kind: source bytes, editorial
  decisions, and executable model definitions have different authority and
  must not be collapsed into one “truth” table.
- The safest small kernel is an immutable journal plus content-addressed
  artifacts and explicit provenance; specialized mathematical models should be
  rebuildable projections with declared contracts.

## 3. Minimal implementation problem

Given partially ordered research inputs and editorial/modeling actions, the
system must:

1. reproduce every ingested source artifact byte-for-byte;
2. reconstruct the research state at any committed point;
3. retain the provenance and scoped epistemic class of each claim;
4. preserve explicit unknowns, open questions, disagreements, retractions, and
   supersession without last-write-wins collapse;
5. materialize purpose-specific representations through versioned,
   reproducible transformations;
6. reject a transformation path when it would lose meaning required by the
   request;
7. support branch, merge, composition, schema migration, invalidation,
   rollback, and recovery without rewriting history.

It does **not** initially need to encode the whole world, infer truth from prose,
or make Petri/Event/Causal/LTS structures mutually invertible.

## 4. Phase-1 proposal

### 4.1 Architecture: evidence-preserving ledger with contracted views

Use a small authoritative kernel and a registry of derived views.

#### A. Immutable artifact store

Store raw source bytes under a cryptographic content digest with media type,
ingest metadata, and optional byte/line anchors. A changed document is a new
artifact, never an in-place replacement.

#### B. Append-only decision journal

Store immutable journal records with:

- record ID, record type, schema ID/version, actor/authority scope;
- payload or payload digest;
- causal parent record/commit IDs (zero, one, or many);
- recorded-at time and optional domain/effective time kept as distinct fields;
- referenced artifacts, claims, and source spans;
- explicit operation such as `INGEST`, `ASSERT`, `CLASSIFY`, `DECLARE_OPEN`,
  `SUPERSEDE`, `RETRACT`, `REGISTER_TRANSFORM`, `RUN_TRANSFORM`, `COMMIT`, or
  `MERGE`.

Parent links form a commit/event DAG. They express journal lineage only; they
must not be reinterpreted automatically as physical-world causality. Independent
records need no fabricated total order.

Claims are immutable, addressable payloads. Epistemic class is scoped and
versioned (`SOURCE_SUPPORTED`, `WORKING_HYPOTHESIS`, `OWNER_DIRECTION`, `OPEN`,
`NON_CONCLUSION`, `INFERENCE`, and `UNKNOWN` as needed). Retraction and
supersession add records; they do not erase the earlier claim. Conflicting
classifications can coexist until an explicit, authorized resolution record is
added.

#### C. Provenance and dependency records

Use W3C-PROV-like entity/activity/agent relations, implemented in ordinary
tables or records, to connect every derived result to exact inputs, transform
version, parameters, environment identifier, and output digest. Provenance is
not proof of correctness; it makes derivation inspectable and invalidation
computable.

#### D. Contracted projection registry

Each transformation or view adapter declares:

- accepted input schemas and preconditions;
- semantic dimensions consumed and emitted;
- for each dimension, `EXACT`, `SEMANTIC`, `APPROXIMATE`, `DROPPED`, or
  `UNKNOWN` preservation;
- determinism/reproducibility status;
- authoritative inputs and whether output is cache, index, simulation, or
  reviewed promotion candidate;
- expected cost, invalidation dependency, and reverse operation if one really
  exists.

Transformation paths compose conservatively: the path grade for a semantic
dimension cannot exceed its weakest edge. Once a dimension is `DROPPED`, a
later edge cannot label it reconstructed without a new authoritative/anchored
input. Approximation and reverse synthesis remain visibly non-exact.

#### E. Materialized views and model plug-ins

Build current-state, history, claim, provenance, chronology, causal, knowledge
graph, LTS, Petri, event-structure, metric/clock, or simulation views only when
their query contract justifies them. SQL/Datalog-style declarative projections
are preferred for ordinary research indexes. Specialized formalism plug-ins are
used when their semantics are actually requested.

Every materialization is identified by:

`(input commit digest, transform ID/version, parameter digest, output digest)`.

Derived outputs never modify the ledger. They may be deleted and rebuilt.

#### F. Contract-driven route planner

Replace an opaque model-name dispatch with explicit constraint matching. A
request supplies:

- question/workload;
- required semantic dimensions and acceptable grades;
- current authoritative assets and available anchors;
- lifecycle operation;
- latency/storage/recompute/reversibility constraints.

The planner searches the registered transformation graph and returns only
admissible paths, plus their loss vector, cost estimates, validation plan, and
unresolved preconditions. `R(S,M,L)` remains a useful conceptual decomposition,
but `S`, `M`, and `L` should compile into this explicit query contract rather
than remain free-form classifier features. If no path proves admissible, return
`REVIEW_REQUIRED / UNKNOWN`.

### 4.2 Minimal storage realization

The first implementation can use SQLite or PostgreSQL plus a filesystem/object
blob store. Minimal relations are `artifact`, `journal_record`, `parent_edge`,
`claim`, `claim_source`, `transform_definition`, `transform_run`,
`dependency_edge`, `commit`, and `branch_ref`. N-ary relations can be represented
as addressable assertion entities; a universal hypergraph engine is not needed
at the start.

Current state is a deterministic projection over the ancestor closure of a
commit under a versioned resolution policy. Resolution must preserve unresolved
concurrent operations instead of relying on filesystem order or wall-clock
last-write-wins.

## 5. Prior-art basis and alternatives

This is an integration of established engineering patterns, not a new theory:

- event sourcing for append-only decisions and replayable state;
- content-addressed/Merkle-DAG storage for immutable identity and integrity;
- bitemporal modeling for separating record time from domain/effective time;
- W3C-PROV-style provenance for entity/activity/agent derivations;
- truth-maintenance/assumption-based reasoning ideas for retaining support,
  alternatives, and explicit conflict;
- relational and Datalog materialized views for reproducible projections;
- compiler-like intermediate-representation/pass contracts for transformation
  preconditions, capabilities, and loss;
- Petri/Event/LTS/Causal/metric formalisms as task-specific semantic models.

Plausible alternatives were rejected as the sole kernel:

- **Raw Markdown plus ad-hoc indexes:** excellent human ground material, but
  insufficient alone for typed decisions, dependency invalidation, conflict,
  and machine-checkable transformation loss.
- **One canonical knowledge/property graph:** query-friendly, but tends to hide
  change operations, statement scope, n-ary context, and source-vs-inference
  boundaries unless extensively reified. It is better as a view.
- **Petri or event structure as the canonical store:** strong for behavior or
  concurrency, weak as the sole carrier of source bytes, editorial authority,
  epistemic status, prose anchors, and arbitrary research evidence.
- **Event sourcing alone:** reconstructs operations but does not by itself
  specify semantic preservation, model fitness, or derived-view authority.
- **Automatic CRDT-style semantic merge:** may converge data structures while
  silently choosing the wrong research meaning. Set-union can preserve inputs,
  but semantic resolution must remain explicit.
- **A category-theoretic or typed-morphism universal core:** attractive for
  composition but under-specified by current evidence and costly to validate as
  the minimal operational store. It can later be a view or contract language.

## 6. Authority, preservation, and reconstruction

### Authoritative representations

- Source authority: immutable artifact bytes and their acquisition metadata.
- Decision authority: journaled owner/editor/agent decisions within their
  declared scope; this is authority about what was decided, not proof that the
  decision is universally true.
- Model-definition authority: the exact versioned transform/model contract and
  executable definition for reproducing its outputs.

There is deliberately no single universal authoritative representation.

### Derived representations

Current-state summaries, claim graphs, causal indexes, Petri nets, event
structures, reachability graphs, embeddings, metrics, reconstructed objects,
and simulations are derived unless a separate reviewed decision explicitly
promotes a particular artifact for a limited scope. Promotion records provenance
and does not delete the source/derived distinction.

### Preservation contract

At minimum track these dimensions independently:

- source payload and source span;
- provenance/authority;
- epistemic class and scope;
- claim identity and succession/lineage;
- journal partial order and explicit conflict;
- transformation/rule labels;
- causality/concurrency/conflict;
- resource/capacity constraints;
- composition interface/boundary;
- metric/clock/coordinate anchors;
- schema and transform version.

Each view states its grade per dimension. Exact byte and journal replay checks
are mechanical. Semantic-equivalence checks require a declared equivalence
relation and tests. Approximate reconstruction requires anchors, error measures,
and confidence; it must not be promoted to exactness.

### Loss and non-recoverable information

- A causal-order view cannot recover dropped transformation labels, resource
  constraints, metric coordinates, or excluded alternatives.
- An LTS reachability graph generally cannot uniquely recover the originating
  behavior model or its resource interpretation.
- A summary cannot recreate omitted wording, ambiguity, tone, or source spans.
- A total order imposed for presentation cannot establish actual causality.
- A resolved merge cannot justify deletion of competing inputs or their
  histories.
- Hashes verify identity/integrity, not truth or semantic adequacy.

## 7. Lifecycle behavior

- **Mutate:** append a new assertion, supersession, retraction, classification,
  or transform definition; never mutate old evidence.
- **Compose:** create a commit with multiple parents and explicit interface or
  namespace mappings. Validate contracts before materializing a combined view.
- **Split/diverge:** create branch references to existing commits; common
  history remains shared and exact.
- **Merge:** union immutable histories, surface semantic conflicts, and append
  explicit resolution decisions. Do not silently use last writer wins.
- **Migrate:** register a versioned schema transform and retain old records,
  mapping tables, loss vector, and test evidence. Prefer read adapters before
  irreversible rewrite.
- **Recover:** restore artifacts, journal, commit graph, and transform registry;
  verify hashes; then rebuild disposable views. Recovery is incomplete if a
  non-reproducible external transform lacks a captured output/anchor.
- **Rollback:** move a branch/reference to a prior commit or append a reverting
  decision; never erase the intervening history.
- **Invalidate:** traverse reverse dependency edges from a changed/new decision
  and recompute only affected views. The measured dependency closure is the
  invalidation radius.
- **Retire/succeed:** freeze a model definition and add a successor relation with
  migration and preservation contracts; version increase is not inferred from
  run count.

## 8. BYUL CORE-A alignment

- **Change/mutability:** immutable history records change as succession rather
  than pretending current state is permanent.
- **Non-substantiality:** stable IDs are handles for versioned records or derived
  patterns, not ontological substances.
- **Composition/emergence:** parent DAGs, interfaces, derivations, and view
  lineage expose local-to-composed construction without claiming complete
  reduction.
- **Conditional relationality:** claim scope, context, provenance, conflict, and
  partial order are first-class; no forced global total order or context-free
  meaning is assumed.

This is alignment by explicit implementation choices, not a claim that the
architecture validates CORE-A.

## 9. Expected failure modes

- Artifact/claim granularity may be too coarse for precise provenance or too
  fine for usable maintenance.
- Schema and semantic-dimension registries may grow into an ungovernable
  ontology.
- A transform author can overstate a preservation contract; machine checking
  cannot replace semantic review.
- Nondeterministic models or external services may prevent exact replay.
- Provenance and dependency graphs may grow faster than useful query value.
- Large fan-in merges can preserve every conflict but overwhelm human review.
- Derived-view caches can become stale if dependencies are incomplete.
- A plugin may encode behavior its source evidence does not justify.
- Journal lineage may be mistakenly presented as real-world causal lineage.
- Content hashes can produce false confidence about truth or correctness.
- Sensitive source retention may conflict with deletion/privacy obligations;
  append-only storage therefore needs an explicit redaction/tombstone policy
  with acknowledged loss.
- Route search can become expensive or falsely return no path when contracts are
  incomplete.

## 10. Falsification tests

Reject or materially revise the proposal if any of the following repeatedly
occurs under representative data:

1. An accepted commit cannot reproduce its exact source artifacts and scoped
   current-state classification.
2. Concurrent contradictory decisions collapse without both inputs and an
   explicit resolution being inspectable.
3. A planner admits a path that drops a required semantic dimension.
4. A supposedly exact view changes across identical input/transform/parameter
   digests.
5. A derived claim lacks complete input and transform lineage.
6. A schema migration hides a material delta or prevents reading the prior
   meaning.
7. A dropped dimension is reported as recovered without a new anchor.
8. Lifecycle invalidation routinely approaches full rebuild despite local
   changes and offers no practical benefit over snapshots.
9. Common research questions require so much reification that a simpler
   authoritative graph/document model preserves the same guarantees at lower
   cost.
10. The contract vocabulary cannot express the preservation demands needed by
    Petri/Event/LTS/causal/metric probes without embedding each full formalism in
    the kernel.

## 11. Implementation test plan

1. Ingest the exact baseline files; verify byte digests, stable anchors, and a
   reproducible snapshot manifest.
2. Encode representative source-supported, owner-direction, hypothesis, open,
   non-conclusion, and inference claims; verify scoped status round trips.
3. Create sequential, diamond/concurrent, conflicting, superseding, and
   retracting journal histories; test every historical commit reconstruction.
4. Branch and merge contradictory classifications; verify no silent overwrite.
5. Register current/history/open/provenance views and test deterministic rebuild
   from an empty cache.
6. Register an intentionally lossy causal projection; require rejection when
   transformation labels are mandatory and acceptance with a visible loss
   vector when they are optional.
7. Add a small Petri or LTS plugin for a behavior question; verify that model
   semantics remain derived and provenance-linked.
8. Change one source/decision, compare predicted and actual invalidation radius,
   and check unaffected output digests.
9. Run schema v1-to-v2 migration, reverse-read old records, and verify the
   declared delta.
10. Delete all derived caches and recover from artifacts, journal, commits, and
    transform definitions alone.
11. Measure storage growth, replay time, incremental recompute, query latency,
    merge-review burden, and provenance overhead on T1–T10-style stress shapes.
12. Inject missing anchors, unknown transform semantics, and nondeterministic
    output; require `REVIEW_REQUIRED / UNKNOWN`, never fabricated PASS.

## 12. Open unknowns and why this could be wrong

Open unknowns include the correct claim granularity, governance of scoped
authority, minimal semantic-dimension vocabulary, handling of lawful deletion,
acceptable provenance overhead, equivalent-state definitions, nondeterministic
transform capture, and whether branch/merge semantics should adopt any CRDT
components below the semantic layer.

The proposal could be wrong because it optimizes auditability and loss
discipline more than direct simulation performance; research memory may remain
small enough that Markdown plus manifests is superior; the contract registry may
become a second, harder model; human semantic review may dominate all automated
routing; or the Owner may intend the immediate implementation to test a
world-model formalism rather than a research-memory substrate. Those alternatives
must be decided by the falsification tests and comparative evaluation, not by
the architecture naming itself.

PHASE1_FROZEN = TRUE
