# Phase 1 Frozen Proposal — v0.1.05

ROUND_SLOT = R02
PROFILE = NEUTRAL_BLIND
PHASE1_RESEARCH_BASELINE_COMMIT = 891e4bd4b999eacc99431ed0db05062901a68dd9
PHASE1_INPUT_SCOPE = EXACT_GIT_OBJECT_READS_OF_PACKET_ENUMERATED_BASELINE_FILES

No v0.1 implementation file, recovery output, reservation output, or other proposal
was inspected in producing this document. This is a research proposal, not an
implementation authorization.

## CURRENT_STATE_RECONSTRUCTION

Byul is an active, non-normative research track separated from the AAA mainline.
Its current problem is not merely to choose a graph formalism. It must retain and
reconstruct an evolving research state containing source material, Owner direction,
working hypotheses, open questions, explicit non-conclusions, inferred relations,
and model/lifecycle experiments without silently converting one epistemic class into
another.

BYUL CORE-A currently supplies four research-level review principles: mutability,
non-substantiality/derived entity, composition/emergence, and conditional
relationality. These principles do not choose a formalism and are not scientific or
AAA-canonical axioms. The baseline explores Petri/Open/Reconfigurable Petri,
Occurrence/Event, causal-order, and LTS views as a complementary family; none is
canonical. `R(S,M,L)` is a promising routing sketch, especially because preservation
demand may dominate superficial situation type, but its sufficiency is open.

The baseline also contains an important correction: a formal `P-series` was never
established in the available evidence. Earlier wording that treated it as an external
canonical source is therefore historical error/correction evidence, not a current
requirement. A sound architecture must preserve both the erroneous earlier state and
the later correction while reconstructing the corrected current state.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

- The active research state is working, non-normative, and not validated.
- BYUL CORE-A is Owner-adopted within Byul research, not an AAA canonical rule set.
- The baseline distinguishes possible-behaviour, occurrence/history,
  causality/concurrency/conflict, and reachability views and explicitly leaves their
  authority relationships open.
- Reconstruction grades, semantic loss, cumulative drift, reversibility, and
  invalidation radius are explicit evaluation concerns.
- The formal `P-series` claim was corrected as unsupported in the active log.

### OWNER_DIRECTION

- Use the accumulated Byul research memory itself as primary v0.1 data.
- Measure model lifecycle behaviour and transformation cost through simulation.
- Treat situational model selection as valuable, without turning the current router
  or model family into a fixed answer.

### WORKING_HYPOTHESIS

- The high-resolution worldview may be a composition network of local mappings from
  which stable objects/personas/boundaries emerge as higher-scale views.
- A complementary representation family may be better than a universal model.
- Preservation demand may be the most important part of a situation fingerprint.
- `R(S,M,L)` may be a useful planning abstraction.

### OPEN

- The primitive or minimal algebra; exact transformation semantics; minimum routing
  features; authority split; model-family translation conditions; acceptance
  thresholds; and whether one or multiple authoritative representations are needed.
- Whether time is primitive, whether the substrate is discrete, and whether local
  mappings are fundamental.

### NON_CONCLUSION

- Petri is not canonical; Causal Set is not the final architecture; an event/local
  mapping is not an established primitive; one universal representation is not
  required; discarded semantics are not automatically reconstructable; and no
  scientific truth follows from the Owner worldview.

### YOUR_INFERENCE

- The minimum safe authority is an epistemically typed, provenance-bearing change
  ledger over exact source artifacts. Behaviour, causal, reachability, summary, and
  object/persona structures should initially be rebuildable contracted views, not
  competing silent authorities.
- The executable router should be a preservation-aware query/update planner with a
  catalog of verified transformations and an abstain/review outcome. `R(S,M,L)` is a
  useful label for some inputs, but is too implicit to be the contract itself.

## MINIMAL_PROBLEM_DEFINITION

Given a sequence of research artifacts and changes, reconstruct any declared current
or historical context while preserving source identity, epistemic status, polarity,
authority, provenance, succession, explicit uncertainty/non-conclusion, and declared
semantic loss. Produce task-specific views and lifecycle operations only through
versioned transformations whose preconditions, preserved meanings, losses, and
validation obligations are inspectable. Do not solve a universal world ontology in
the storage layer.

## PHASE1_PROPOSAL

Adopt a **Provenance-Bearing Claim Ledger with Contracted Views**. This is an
implementable composition of established patterns, not a proposed new theory.

The canonical store has two record classes with distinct authority scopes:

1. **Evidence artifacts** — immutable source bytes, locators, media type, source
   commit/version, content digest, acquisition/author information, and stable anchors
   into the bytes. These are authoritative for what the source contained.
2. **Research operations** — an append-only, hash-linked sequence of typed operations
   such as `IntroduceClaim`, `ClassifyClaim`, `RelateClaims`, `SupersedeRevision`,
   `WithdrawClaim`, `OpenQuestion`, `RecordNonConclusion`, `ForkContext`,
   `MergeContext`, `RegisterTransform`, and `RecordEvaluation`. These are authoritative
   for how Byul's declared research state changed.

An independently attributable claim is stored in a nanopublication-like envelope:

- stable logical `claim_id` and immutable content-addressed `revision_id`;
- exact source anchor and optional structured proposition, while retaining the exact
  source wording;
- epistemic class (`SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`,
  `OPEN`, `NON_CONCLUSION`, or explicitly attributed `INFERENCE`);
- polarity/modality separated from confidence and lifecycle status;
- context/environment, attribution, evidence and derivation links;
- valid/claim time when meaningful and transaction/recording time always;
- typed relations including `supports`, `contradicts`, `depends_on`, `refines`,
  `supersedes`, `derived_from`, and `composed_of`.

The current state is a deterministic fold of operations under an explicit context and
as-of time. It is a materialized view, not an independently editable truth table.
Contradictory claims can coexist in named contexts; correction changes current status
by adding a superseding operation rather than erasing history.

The first physical implementation can be deliberately ordinary: canonical JSON
records plus SHA-256, an append-only JSONL event log, and SQLite tables/indexes for
claims, revisions, relations, contexts, provenance, and transform receipts. RDF/PROV
export is an interoperability view, not a requirement to make a triple store the
authority.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) supplies entities, activities,
  agents, derivation, revision, invalidation, bundles, and responsibility. Use it for
  interoperable provenance, while keeping Byul's epistemic classes domain-specific.
- Nanopublications separate an assertion, its provenance, and publication
  information at fine granularity; the four-graph structure is described in the
  [nanopublication literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC7959622/).
  Adopt the envelope idea without requiring every assertion to be RDF.
- Event sourcing records all state changes as a sequence and permits reconstruction
  by replay; [Fowler's account](https://martinfowler.com/eaaDev/EventSourcing.html)
  also states the costs of replay and snapshots. Adopt the reconstruction pattern,
  not the assumption that an event log alone supplies semantic correctness.
- Bitemporal databases distinguish valid time from transaction time; see
  [Snodgrass's temporal database summary](https://www2.cs.arizona.edu/~rts/pubs/EDC.pdf).
  Use both only where a claim's modeled validity is meaningful; never fabricate valid
  time from document chronology.
- de Kleer's [assumption-based TMS](https://doi.org/10.1016/0004-3702(86)90080-9)
  motivates keeping incompatible assumption environments without destructive
  retraction. Use this as an optional context/justification view, not as the source of
  truth and not as a claim that all research reasoning is Horn logic.
- Well-behaved lenses define explicit round-trip laws for bidirectional views; see
  [Foster et al.](https://www.cis.upenn.edu/~bcpierce/papers/lenses.pdf). Only views
  satisfying declared laws may support write-back. Lossy views are read-only or emit
  a new reviewed proposal operation.
- [Provenance semirings](https://www.cs.ucdavis.edu/~green/papers/pods07.pdf) and
  [incremental view maintenance](https://doi.org/10.1145/170036.170066) provide bases
  for explaining derivations and updating views. They are optional optimizations
  after semantic correctness; full provenance polynomials may grow too large.
- Content-bound identifiers such as
  [Trusty URIs](https://arxiv.org/abs/1401.5775) justify verifiable immutable artifact
  identities. Local SHA-256 identifiers are sufficient for an initial implementation.
- RDF named graphs can carry contexts, but the W3C notes that dataset semantics are
  not singularly agreed. Therefore any RDF export must declare what a context graph
  means rather than assuming the graph name creates endorsement; see
  [RDF dataset semantics](https://www.w3.org/TR/rdf11-datasets/).

## AUTHORITATIVE_REPRESENTATION

The authoritative representation is the content-addressed evidence-and-operation
ledger. Evidence artifacts answer "what exact material was available?"; research
operations answer "what classification, relation, correction, branch, merge, or
evaluation was declared?" A deterministic reducer plus schema/transform versions
defines reconstructable state. No summary, embedding, causal index, Petri net, LTS,
or current-state table becomes authoritative merely because it is convenient.

Authority is field-scoped. A source can be authoritative for wording without being
authoritative for truth; an Owner statement can be authoritative for Owner direction
without becoming a scientific fact; a transform receipt can be authoritative for what
the program produced without proving semantic adequacy.

## DERIVED_REPRESENTATIONS

- Current-state views grouped by epistemic class, context, and lifecycle status.
- Succession/history DAG and bitemporal as-of views.
- PROV-compatible derivation/evidence graph.
- Claim dependency, contradiction, support, correction, and invalidation indexes.
- Assumption-environment/justification view for parallel hypotheses.
- Full-text, lexical, embedding, and summary views with explicit lossy labels.
- Query-specific causal-order, concurrency/event, reachability/LTS, Petri/open-net,
  resource, metric/clock, and object/persona materializations when their transform
  contracts apply.
- Evaluation dashboards and preservation matrices derived from transform receipts.

## PRESERVATION_CONTRACT

Every transformation declaration contains its identity/version, accepted input
schema, exact input IDs/digests, output schema, field-level preservation vector,
preconditions, validation tests, reverse/write-back status, dependency set, and an
emitted loss receipt.

The ledger must preserve exactly:

- source bytes/digest/anchor and record schema version;
- claim and revision payloads, epistemic class, polarity/modality, attribution,
  authority scope, context, and explicit unknown/non-conclusion status;
- transaction order, declared valid time, parent/supersession/withdrawal relations,
  branch ancestry, merge decisions, and conflicts;
- transformation version, input/output IDs, validation result, and declared loss.

Hard gates:

- `OPEN` or `NON_CONCLUSION` cannot be emitted as a positive fact without a new,
  sourced reclassification operation.
- Derived output cannot overwrite evidence or ledger records.
- A write-back view must satisfy its declared round-trip laws; otherwise it may only
  propose a new reviewed operation.
- Unsupported or unknown preservation demand returns `REVIEW_REQUIRED`, not a best
  guess.

## LOSS_AND_NON_RECOVERABLE

Natural-language meaning is not made exact by parsing. A paraphrase can be linked and
labeled but cannot replace its exact source. Embeddings, summaries, topic clusters,
flattened graphs, reachability closures, causal projections, and synthesized models
are not invertible in general.

The following losses are non-recoverable unless the omitted authoritative inputs
remain addressable: source wording/anchors, epistemic class, polarity, provenance,
context boundaries, branch/merge decisions, supersession history, transformation
labels, resource/conflict semantics, and discarded metric anchors. No reverse
synthesis may claim uniqueness when multiple source models could produce the view.

## TRANSFORMATION_PATHS

A planner selects a path through a versioned transform catalog. Each edge has
capabilities, preservation claims, costs, and tests. Composition of edges computes the
meet/worst preservation class per demanded field and unions dependencies/losses. A
path is admissible only if every required field meets the request contract.

For a lens-like exact/semantic view, test `GetPut` and `PutGet` over its declared
domain. For partial or lossy projections, provide only forward materialization and a
loss receipt. Reverse synthesis creates a new candidate linked to its source view and
requires evaluation; it never reconstructs missing semantics by fiat.

## LIFECYCLE_BEHAVIOR

- **Create/accumulate:** append artifacts and operations; incrementally refresh only
  dependent views.
- **Mutate/correct:** add a revision and supersession/invalidation event. Stable
  logical handles do not hide immutable revision identities.
- **Compose:** namespace-union claim envelopes and add explicit `composed_of` and
  interface relations; contradictions remain visible rather than canceling.
- **Split:** export a dependency-closed subgraph plus boundary stubs, source digests,
  transform versions, and a split receipt listing excluded dependencies.
- **Diverge:** create a named context with an ancestor ledger position; local claims
  and derivations remain scoped.
- **Merge:** perform three-way operation merge from a common ancestor. Auto-merge
  only independent/commutative operations; classification, polarity, deletion,
  equivalence, and authority conflicts become explicit conflict records.
- **Migrate:** replay into the successor schema, compare preservation receipts and
  state digests, then cut over only after dual-read equivalence on required queries.
- **Degraded/recover:** rebuild from verified ledger plus checkpoint; quarantine a
  corrupted suffix; prove replay determinism and report missing artifacts.
- **Successor/retire:** retain lineage and read support; never reuse identifiers or
  erase a predecessor needed for interpretation.

## ROUTING_POSITION

Keep `R(S,M,L)` as a research shorthand, but do not make it the executable authority.
`S` currently risks mixing the user's question, preservation demand, data shape,
precision, and operational budget; it can grow into a duplicate world description.
The implementable operation is instead:

`Plan(Q, P, M, L; Catalog) -> Sources + Views + TransformPath + LossReceipt + ValidationPlan | REVIEW_REQUIRED`

- `Q`: query/update intent plus required outputs and workload shape;
- `P`: field-level preservation/precision contract and authority policy;
- `M`: current representations, versions, lineage, invalidation and scale state;
- `L`: lifecycle operation and recovery/reversibility need;
- `Catalog`: independently registered view/transform capabilities and measured costs.

This is compatible with `R(S,M,L)` if `S` is treated as a convenient fingerprint for
parts of `Q` and `P`. It is better testable because a route is valid only against an
explicit catalog and contract. The planner may compose several views and must abstain
when no path satisfies the preservation contract.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY:** changes are first-class operations; correction and
  succession do not overwrite history.
- **NON-SUBSTANTIALITY / DERIVED ENTITY:** object/persona/boundary nodes are typed
  materializations with lineage, not mandatory ontological primitives. Stable IDs are
  operational handles, not assertions of immutable substance.
- **COMPOSITION / EMERGENCE:** claim bundles and higher-scale views retain
  `composed_of`/derivation links and boundary receipts; reduction to components is not
  claimed universally.
- **CONDITIONAL RELATIONALITY:** contexts, assumption environments, provenance, and
  valid-time scopes make meaning conditional. Incomparable claims are not forced into
  a global causal order.

Alignment is a review judgment to be tested. It is not automatic principle PASS.

## EXPECTED_FAILURE_MODES

- Human cost and inconsistency in choosing claim granularity and epistemic labels.
- False confidence that structured claims capture the full semantics of prose.
- Event schema evolution makes replay dependent on upcasters and old code.
- Stable claim handles accidentally reify changing referents.
- Context/ATMS labels or provenance expressions grow combinatorially.
- Merge policy treats semantic conflicts as syntactic independence.
- A transform declares preservation it does not actually satisfy.
- Router catalog metadata becomes stale, circular, or more costly than direct work.
- Content hashes prove identity/integrity, not truth or trustworthiness.
- Source artifacts disappear even though their digest remains.
- Incremental invalidation misses an undeclared dependency.
- Too much structure slows research and makes raw, versioned Markdown preferable.

## FALSIFICATION_TESTS

1. **P-series correction test:** ingest the earlier canonical-source wording and later
   correction. Historical reconstruction must show both; current reconstruction must
   not report a formal P-series as established.
2. **Epistemic trap test:** summaries and model views must not turn an `OPEN` or
   `NON_CONCLUSION` statement into `SOURCE_SUPPORTED`.
3. **Replay test:** shuffled storage layout with the same ordered operations must
   yield the same canonical state digest; missing/duplicated operations must fail.
4. **As-of test:** valid time, recording time, and chronology-only order must remain
   distinguishable.
5. **Contradiction test:** two contexts may hold opposing hypotheses without either
   being silently deleted or globally endorsed.
6. **Split/compose test:** split a dependency-rich context and recompose it; omitted
   boundary dependencies and non-recoverable fields must match the receipts.
7. **Diverge/merge test:** independent edits auto-merge; competing classifications or
   authority changes produce reviewable conflicts.
8. **Lens test:** exact write-back views satisfy GetPut/PutGet over generated cases;
   lossy views reject write-back.
9. **Route counterexample test:** construct two situations with the same structural
   fingerprint but different preservation demands; the planner must choose different
   paths or abstain.
10. **Invalidation oracle test:** compare incremental refresh with full recomputation
    after local and high-fan-out mutations.
11. **Recovery test:** corrupt a checkpoint and truncate a log suffix; recovery must
    detect both and never claim a complete state.
12. **Scale test:** measure claims/relations, provenance explosion, view latency,
    replay time, storage, and merge conflict rate at increasing density.

The proposal is falsified for the initial target if it cannot beat raw
content-addressed Markdown plus Git on reconstruction fidelity while remaining within
an agreed annotation and maintenance budget.

## IMPLEMENTATION_TEST_PLAN

1. Define a small, versioned record schema and field-level preservation vocabulary.
2. Build a read/write ledger adapter over canonical JSONL and a SQLite projection;
   retain source bytes by digest.
3. Hand-encode a compact fixture from the exact research baseline, including the
   P-series correction, hypotheses, open questions, and non-conclusions. Do not begin
   with automatic semantic extraction.
4. Implement deterministic replay, as-of/context selection, current/history views,
   dependency invalidation, and preservation/loss receipts.
5. Add property tests for replay idempotence, digest stability, non-promotion of
   epistemic class, merge laws in the declared safe domain, and view lens laws.
6. Implement two clearly different derived views: a provenance/current-state view and
   one causal or reachability view. Measure whether the transform catalog can explain
   their losses and dependencies.
7. Run lifecycle fixtures covering create, correct, compose, split, diverge, merge,
   migrate, corrupt, recover, successor, and retire.
8. Compare against raw Markdown+Git and the alternative of a single property graph on
   fidelity, annotation effort, code size, replay speed, query latency, invalidation
   radius, and reviewer comprehension.
9. Add Petri/Event/LTS materializers only for workloads that demonstrate a need; do
   not implement the whole candidate family by default.

No implementation is performed by this packet.

## OPEN_UNKNOWNS

- Minimum independently attributable claim size and acceptable annotation cost.
- Who may classify or reclassify each epistemic/authority field.
- Whether claim equivalence is asserted, inferred, contextual, or never automatic.
- Precise contradiction, negation, withdrawal, and non-conclusion semantics.
- Which valid-time fields are meaningful for research claims.
- Safe automatic-merge domain and Owner review boundary.
- Necessary retention, privacy, signature, and access-control policy.
- Whether canonical JSON/SQLite remains sufficient at target scale.
- Which BYUL CORE-A checks can become executable invariants without distorting the
  principles.
- Evidence needed to show routing value exceeds catalog/fingerprint maintenance cost.

## WHY_THIS_COULD_BE_WRONG

The proposal may over-structure a small research corpus. Git plus exact Markdown,
careful headings, and a few generated indexes may deliver nearly the same fidelity
with much less machinery. Claim atomization can invent boundaries the Owner did not
intend; structured predicates can look more certain than prose; event sourcing keeps
history but does not solve meaning; and ATMS/provenance techniques can explode in size.
The plan also assumes that field-level preservation contracts can be stated before
the hardest semantic questions are resolved. Finally, replacing the compact
`R(S,M,L)` notation with an explicit planner may merely move complexity into `Q`, `P`,
and the catalog. The decisive evidence must be comparative reconstruction and
lifecycle performance, not architectural elegance.

IMPLEMENTATION_AUTHORITY = NONE
