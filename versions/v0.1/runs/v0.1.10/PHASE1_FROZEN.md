# Phase 1 Frozen Proposal — v0.1.10

## Scope and blindness declaration

This proposal was produced under profile `OUTSIDE_PRIOR_ART_SEARCH`. Internal
research input was restricted to the packet's enumerated paths read as exact Git
objects from commit `891e4bd4b999eacc99431ed0db05062901a68dd9`.
No v0.1 implementation file, run output, recovery output, reservation content,
or other experiment branch was read during Phase 1. External research was
restricted to established prior art and primary standards/papers.

## CURRENT_STATE_RECONSTRUCTION

Byul is a non-normative, unvalidated research track separated from the AAA
mainline. It investigates how changing memory/state and models can retain
meaning across representation, transformation, composition, reconstruction,
routing, and long-lived mutation. Its Owner-adopted research principles, called
BYUL CORE-A, are change/mutability, non-substantial or derived entities,
composition/emergence, and conditional relationality. They constrain review but
do not canonize a formalism or claim scientific truth.

The Owner's high-resolution worldview hypothesis is a network of innumerable
local mappings/processes whose compositions may appear at higher scales as
objects, selves, personas, protocols, and boundaries. Succession and lineage are
therefore stronger starting points than timeless identity; absolute global NOW,
object-first ontology, a physical minimum unit, and a single primitive remain
unsettled.

The research memory currently distinguishes a behaviour/rule plane from an
occurrence/fact plane and considers Petri, Open/Reconfigurable Petri,
Occurrence Nets, Event Structures, causal-order views, and LTS/reachability as
possibly complementary. It does not adopt any of them as canonical. A current
routing sketch is
`R(S,M,L) -> {target models, transformation path, preservation contract,
validation plan}`, where `S` is situation, `M` current model state, and `L`
lifecycle. Preservation demand may be more important than phenomenon labels,
but the fingerprint and router remain hypotheses.

The central unresolved risk is semantic laundering: a source statement,
Owner direction, working hypothesis, open question, non-conclusion, derived
inference, reconstructed view, and executable model can accidentally collapse
into one undifferentiated "current state." Once a lossy projection is treated as
ground truth, discarded transformation semantics, authority, ambiguity, or
context cannot be recovered merely by reversing an edge.

## STATE_CLASSIFICATION

| Class | Reconstructed state |
|---|---|
| `SOURCE_SUPPORTED` | The exact research baseline states the channel/version boundaries, BYUL CORE-A text and status, current candidate formalism family, routing/lifecycle hypotheses, simulation axes, MI-1 reconstruction objective, and explicit non-conclusions. Causal order, Petri/Event/LTS roles, transformation-loss concerns, and prior-art descriptions are source-supported only to the extent recorded in that baseline; this run does not independently validate all of them. |
| `OWNER_DIRECTION` | Explore the high-resolution local-mapping composition worldview; prefer succession/history over assumed timeless identity; use situation-sensitive model choice; validate lifecycle transformations and costs; treat the research memory itself as primary experimental data; run independent proposals without premature convergence. |
| `WORKING_HYPOTHESIS` | Multiple formalisms may be complementary; preservation demand may dominate other situation features; an occurrence/fact plane and a behaviour/rule plane may be useful; `R(S,M,L)` may be a useful router interface; derived reconstructions need explicit reliability classes. |
| `OPEN` | Minimal primitive/algebra; exact transformation semantics; authoritative-representation policy; minimal routing inputs; model-family compatibility; operational CORE-A gates; semantic-drift metric; safe merge/recovery; scale limits; reconstruction acceptance; exact metric/clock treatment. |
| `NON_CONCLUSION` | Petri is not canonical; Causal Set is not the final architecture; one universal model is not required; one canonical representation is not established; local mapping/event is not an established primitive; discarded semantics are not automatically reconstructible; philosophy does not prove physics. |
| `YOUR_INFERENCE` | The smallest defensible authority is not a world-model formalism. It is a typed, immutable evidence/claim/derivation ledger from which world-model views are produced under machine-checkable preservation and loss contracts. A model router is then a constrained query planner over declared capabilities, not the owner of truth. |

## MINIMAL_PROBLEM_DEFINITION

Maintain an evolving body of evidence, claims, assumptions, decisions, and
derivations so that, for any asserted current answer:

1. the exact recorded evidence and responsible activity can be located;
2. epistemic/authority status and context can be reconstructed without
   inventing commitment;
3. incompatible hypotheses can coexist without forced global consistency;
4. every derived representation states what it preserved, approximated, or
   destroyed;
5. mutation, branch, composition, split, merge, migration, invalidation, and
   recovery remain replayable and auditable; and
6. specialized models can be selected for questions without becoming
   ontological ground truth.

Anything beyond this—such as choosing a physical primitive or a universal
behaviour formalism—is a separate scientific/modeling problem.

## PHASE1_PROPOSAL

### Architecture: Provenance-Typed Assumption Ledger (PTAL)

`PTAL` is a descriptive name for an implementable assembly of established
provenance, temporal-database, truth-maintenance, bidirectional-transformation,
database-provenance, abstract-interpretation, and incremental-view techniques.
It is not proposed as a novel theory.

The architecture has four planes:

1. **Evidence plane — immutable receipts.** Store exact source bytes or content
   hashes plus resolvable locators, extraction spans, source version, recorder,
   and ingestion activity. Evidence says what was recorded, not that the content
   is true.
2. **Claim and assumption plane — typed epistemic records.** A `ClaimVersion`
   contains a stable lineage handle, immutable version ID, proposition or quoted
   span, language, epistemic class (`SOURCE_SUPPORTED`, `OWNER_DIRECTION`,
   `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, `INFERENCE`), authority scope,
   assumption context, recorded time, optional valid/effective time, and evidence
   links. Supersession and retraction append events; they never overwrite.
3. **Justification and lifecycle plane — reasons and changes.** Typed edges and
   hyperedges record `supports`, `challenges`, `derives`, `contradicts`,
   `depends_on`, `supersedes`, `specializes`, `composes`, and `invalidates`.
   Assumption-based truth-maintenance labels identify the minimal contexts in
   which a derived claim is active and preserve mutually inconsistent contexts.
   Lifecycle events record create, mutate, compose, split, diverge, merge,
   migrate, recover, successor, and retire.
4. **Derived-model plane — disposable projections.** Current-state summaries,
   chronologies, open-question lists, causal indexes, search/vector indexes,
   LTS/Petri/Event models, simulations, and evaluation dashboards are
   materialized views or plugins. Each output has a `TransformReceipt` containing
   input IDs/hashes, transform implementation and version, parameters, output
   hash, preservation contract, loss certificate, dependencies, and validation
   result. No derived plane silently becomes authoritative.

Records should be content-addressed for integrity and deduplication, but a hash
is not semantic identity. Stable lineage handles relate changing versions;
`same_as` is never inferred from equal labels or similar text. Causal-parent
relations establish a partial order. Wall-clock fields are optional anchors, not
a forced global NOW.

### Minimal logical schema

- `EvidenceArtifact(id, digest, media_type, locator, source_version, bytes_or_ref)`
- `ClaimVersion(id, lineage_id, text_or_term, epistemic_class, authority_scope,
  context_id, recorded_at, valid_interval_or_unknown)`
- `Activity(id, type, agent, tool_version, started_at, ended_at)`
- `Justification(id, conclusion_id, premise_ids, rule_id, assumption_ids)`
- `Relation(id, type, endpoint_ids, context_id)`
- `LifecycleEvent(id, type, parent_event_ids, affected_ids, actor, receipt_id)`
- `TransformReceipt(id, input_ids, transform_id_version, parameters,
  output_ids, preservation_contract_id, loss_certificate, test_result)`
- `DecisionEvent(id, authority, action, target_ids, scope, rationale_evidence)`

The physical first implementation can be relational tables plus a blob store
and reverse-dependency indexes. Datalog or an equivalent rule layer can compute
status and explanations. A property-graph database is optional, not required.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) supplies domain-independent
  entities, activities, agents, derivations, revisions, primary sources,
  invalidation, bundles, and provenance of provenance. PTAL specializes these
  concepts rather than inventing a new provenance ontology.
- Doyle's [A Truth Maintenance System](https://doi.org/10.1016/0004-3702(79)90008-0)
  records reasons for beliefs and revises dependent beliefs. De Kleer's
  [Assumption-Based TMS](https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf)
  adds assumption sets so inconsistent alternatives and multiple potential
  solutions can coexist. PTAL borrows justification/context maintenance, not an
  automatic truth oracle.
- Bitemporal database work distinguishes when a proposition is effective in the
  modeled domain from when the database held it; see Jensen and Snodgrass's
  [temporal database definitions](https://www2.cs.arizona.edu/~rts/pubs/TRmerged.pdf).
  PTAL keeps both optional and allows unknown/indeterminate valid time.
- Green, Karvounarakis, and Tannen's
  [Provenance Semirings](https://www.cs.ucdavis.edu/~green/papers/pods07.pdf)
  shows how query outputs can retain symbolic input lineage. PTAL uses this as a
  basis for compositional derivation explanations where the query fragment
  supports it.
- Foster et al.'s
  [bidirectional transformations](https://doi.org/10.1145/1232420.1232424)
  give `GetPut` and `PutGet` round-trip laws for well-behaved lenses. PTAL permits
  an update through a derived view only when a declared lens and its laws cover
  that view; otherwise the update is a new proposal against the ledger.
- Cousot and Cousot's
  [abstract interpretation](https://doi.org/10.1145/512950.512973) supplies a
  disciplined vocabulary for sound abstraction instead of pretending every
  projection is invertible. PTAL records over/under-approximation direction and
  soundness obligations.
- Shapiro et al.'s
  [Conflict-Free Replicated Data Types](https://inria.hal.science/inria-00609399)
  justify convergent union for carefully selected replicated structures. PTAL
  uses CRDT-style convergence only for immutable event/record sets and explicit
  status operations; convergence is never equated with semantic agreement.
- Budiu et al.'s
  [DBSP](https://www.vldb.org/pvldb/vol16/p1601-budiu.pdf) provides a practical
  path to incremental maintenance of rich derived views. It is an optimization;
  replay from the authoritative ledger remains the recovery oracle.

## AUTHORITATIVE_REPRESENTATION

The append-only PTAL event/record ledger is authoritative, but authority is
**typed by information kind**:

- evidence artifacts are authoritative for exact recorded content and origin;
- claim records are authoritative for what proposition/status/context was
  entered, not for external truth;
- decision events are authoritative only within the stated actor and scope;
- justification records are authoritative for declared reasons and lineage;
- lifecycle/transform receipts are authoritative for which operation produced
  which artifact under which declared contract.

There is no single mutable "truth row." A current state is a reproducible query
over ledger position, authority scope, assumption context, and rule version.
Raw natural-language evidence is retained even after normalization because the
normalization itself is an interpretation.

## DERIVED_REPRESENTATIONS

- evidence/source view and exact quotations;
- current accepted/directed/working/open/non-conclusion views by authority and
  context;
- chronology, succession, composition, and derivation-lineage views;
- contradiction and alternative-context map;
- impact/invalidation and dependency closure indexes;
- full-text, embedding, topic, and similarity indexes, explicitly lossy;
- causal-order, LTS, Petri/Open/Reconfigurable Petri, Event Structure, rewrite,
  metric/clock, simulation, or domain-specific models when a query requires them;
- CORE-A review reports that cite the exact assumptions being checked;
- audit, evaluation, reconstruction, and lifecycle-cost dashboards.

No list item is mandatory forever. A derived representation is replaceable if
its receipts and tests let it be regenerated or explicitly retired.

## PRESERVATION_CONTRACT

Each transform declares field- or relation-level obligations using one of:

- `EXACT`: byte/value/identity and required order preserved;
- `SEMANTIC_EQUIVALENT`: equality under a named, testable equivalence relation;
- `SOUND_OVER_APPROXIMATION`: may add possibilities, must not omit real ones;
- `SOUND_UNDER_APPROXIMATION`: may omit possibilities, must not invent them;
- `ANCHORED`: reconstructed relative to retained authoritative anchors;
- `STATISTICAL`: distributional estimate with method/error metadata;
- `VIEW_DEPENDENT`: meaningful only under a named context/query;
- `NON_RECOVERABLE`: deliberately discarded and impossible to infer from output;
- `UNKNOWN`: guarantee not established; blocks any route that demands a stronger
  level.

A contract also specifies source/target schemas, preconditions, authority and
context boundaries, ordering/identity rules, reverse operation or its absence,
composition rule, loss budget, validation oracle, and failure behavior. Contract
composition chooses the weakest guarantee along a path. If a required field
would become `NON_RECOVERABLE` or `UNKNOWN`, planning fails closed.

For editable derived views, require executable `GetPut` and `PutGet` tests. A
read-only abstraction may instead declare a soundness direction. Exact replay
requires all input evidence, events, rule/transform versions, parameters, and
environment-sensitive dependencies or a sealed execution artifact.

## LOSS_AND_NON_RECOVERABLE

- Natural-language atomization can lose ambiguity, rhetoric, scope, implicature,
  layout, and cross-sentence context. The exact evidence span must remain linked.
- Projection to a specialized model loses every semantic field not represented
  by that formalism unless it is carried as an explicit annotation/anchor.
- Aggregation may lose contributor identity, multiplicity, order, and dissent.
- Embeddings and similarity scores do not reconstruct claims or authority.
- Causal reachability does not reconstruct transformation labels, resource
  constraints, conflict semantics, clock values, or alternative rules.
- A current-state view loses superseded states and alternative contexts unless
  they are deliberately retained in the view.
- A CRDT merge establishes replica convergence, not which hypothesis is correct.
- Equal content digests do not establish same meaning, same authority, or same
  entity; different digests do not prove different meaning.
- Deleted external sources, undocumented human interpretation, missing tool
  versions, and unrecorded environment state may make exact replay impossible.

The system must never synthesize discarded semantics and relabel them as source
facts. Reconstruction from lossy output creates a new inference with its own
uncertainty and provenance.

## TRANSFORMATION_PATHS

1. `source bytes -> EvidenceArtifact`: exact ingestion with digest and locator.
2. `EvidenceArtifact -> ClaimVersion candidates`: extraction/normalization;
   human or authorized-agent review determines epistemic/authority fields.
3. `claims + assumptions + justifications -> contextual status`: TMS/ATMS-style
   derivation with explanation and contradiction labels.
4. `ledger snapshot/context -> query view/model`: declared read transform plus
   receipt, loss certificate, and validation.
5. `edited derived view -> ledger proposal`: use a lawful lens when available;
   otherwise do not mutate authority—append a proposed claim/change for review.
6. `model A -> model B`: route only through registered adapters whose composed
   contract meets the requested preservation level. Reverse synthesis is a new
   activity and may be non-unique.
7. `ledger delta -> maintained views`: incremental update for performance, with
   periodic full replay/differential comparison as the correctness check.

## LIFECYCLE_BEHAVIOR

- **Mutate:** append a new version plus `supersedes`/`retracts` event; compute
  reverse-dependency impact; mark derived outputs stale before recomputation.
- **Compose:** import packages by immutable IDs and explicit namespace/interface
  maps; retain both source bundles and provenance; create higher-order claims as
  derived records with constituent lineage.
- **Split:** export a selected subgraph plus transitive evidence/justification
  closure and a boundary manifest listing intentionally omitted dependencies.
- **Diverge:** branches share immutable ancestors and then append independent
  events/contexts. Succession is recorded; equality is not assumed.
- **Merge:** first union immutable records/events deterministically. Then detect
  epistemic, authority, schema, and ordering conflicts. Preserve conflicting
  contexts; never auto-resolve semantic disagreement merely because storage
  converged.
- **Migrate:** replay into the successor schema/engine, retain old receipts, run
  dual queries and semantic differentials, then issue an explicit cutover event.
- **Recover:** restore evidence/ledger, verify hashes and parent closure, replay
  lifecycle and derivations using pinned rule versions, compare regenerated
  outputs with receipts, and quarantine mismatches.
- **Successor/retire:** create a successor lineage relation and retirement event.
  Stable handles remain operational conveniences, not claims of substance.
- **Bounded invalidation:** reverse-dependency and provenance indexes determine a
  candidate radius; conservative invalidation is allowed, false freshness is not.

## ROUTING_POSITION

`R(S,M,L)` is retained as a useful human-facing intake sketch but is too
unstructured to be the architectural router. It hides the hardest constraint—
field-level preservation—inside `S`, and lets model names become premature
answers.

Compile intake into:

`Plan(Q, Pi, Lambda, C) -> {views/models, adapters, receipts, validation}`

- `Q`: explicit questions and workload operations;
- `Pi`: mandatory field/relation preservation contract and allowed losses;
- `Lambda`: lifecycle operation, authority/context boundary, and operational
  budgets;
- `C`: catalog of available authoritative inputs, derived representations,
  adapter guarantees, freshness, lineage, scale, and measured costs.

The planner solves a constrained path problem: reject capability/guarantee
mismatches first, then minimize measured compute, maintenance, and semantic cost.
Model selection occurs only after the preservation gate. `UNKNOWN` capability or
guarantee yields `REVIEW_REQUIRED`, not a guessed route. This is a refactoring of
the good intent in `R(S,M,L)`, not a claim that routing is unnecessary.

## BYUL_CORE_A_ALIGNMENT

- **Change / mutability:** all meaning-bearing change is explicit succession and
  lineage. Immutable receipts are audit anchors, not ontological immutability.
- **Non-substantiality / derived entity:** handles and claim nodes are operational
  references. Higher-level objects/personas are derived views with traceable
  conditions, never silently promoted to primitive substances.
- **Composition / emergence:** bundles and derived claims retain constituent and
  activity lineage; composition can create higher-order views without claiming
  exhaustive reduction.
- **Conditional relationality:** status is scoped by authority, assumptions,
  context, and time; incompatible contexts coexist; causal incomparability is not
  forced into a total global order.

Alignment is a review hypothesis, not an automatic PASS. CORE-A remains
Owner-adopted research guidance, not a scientific axiom or AAA-wide requirement.

## EXPECTED_FAILURE_MODES

- claim atomization or schema choices erase the nuance the ledger was meant to
  preserve;
- users mistake recorded claim status for external truth or a hash for identity;
- ATMS labels and provenance polynomials grow exponentially under many
  assumptions/derivation paths;
- provenance and receipts cost more than the queries justify;
- authority scopes are underspecified, enabling trust laundering;
- rule/schema evolution makes old derivations incomparable or unreplayable;
- incorrect capability metadata lets the planner approve a lossy route;
- bidirectional lenses cannot be defined for many semantic views;
- conservative invalidation becomes nearly global and operationally useless;
- structural CRDT convergence is misused as semantic conflict resolution;
- natural-language equivalence and semantic drift lack a reliable oracle;
- specialized executable models carry essential rule semantics that claim-level
  normalization cannot adequately express;
- the four-plane separation becomes process-heavy architecture astronautics for
  a small research corpus.

## FALSIFICATION_TESTS

1. In blinded MI-1 trials, PTAL-based reconstruction fails to reduce invented
   commitments or missing critical context versus exact Markdown plus Git.
2. Independent annotators cannot reproducibly assign claim boundaries,
   epistemic classes, authority scopes, or preservation levels.
3. A declared exact/semantic transform fails round-trip, differential, or
   lineage tests, or its loss certificate omits a field later shown necessary.
4. Context/justification labels exceed bounded resource targets on realistic
   branch-conflict corpora without retaining useful explanations.
5. `Plan(Q,Pi,Lambda,C)` does not improve safe-route precision/recall or total
   lifecycle cost over a fixed small set of hand-written views.
6. Compose/split/merge/migrate/recover scenarios cannot reconstruct evidence,
   status, alternatives, and non-conclusions from ledger plus pinned rules.
7. CORE-A reviewers repeatedly find implicit object identity, total time order,
   or context-free meaning introduced by the schema.
8. A malicious or accidental derived claim can obtain Owner-level authority
   without a valid decision event and evidence chain.
9. Full replay and incremental maintenance produce materially different views.
10. Removing PTAL layers yields equal preservation and auditability with much
    lower complexity; if so, adopt the simpler representation.

## IMPLEMENTATION_TEST_PLAN

Research-only plan; no implementation is authorized in this run.

1. **Corpus oracle:** freeze the exact research baseline and build a hand-reviewed
   set of evidence spans, classifications, explicit non-conclusions, and open
   questions. Keep the raw files as the comparison oracle.
2. **Minimal storage spike:** only if separately authorized, use a relational
   database and content-addressed blob directory for the minimal schema. Avoid a
   graph database until measurements require it.
3. **Ingestion tests:** byte/hash round-trip, locator/version integrity,
   duplicate-content/non-identical-authority cases, missing source, multilingual
   span preservation.
4. **Reason-maintenance tests:** support, challenge, retraction, supersession,
   contradictory assumptions, alternative contexts, explanation minimality,
   authority non-escalation.
5. **Transformation tests:** property-based `GetPut`/`PutGet`, abstraction
   soundness counterexamples, compositional loss propagation, missing adapter,
   non-unique reverse synthesis, stale-view rejection.
6. **Lifecycle suite:** sequence, concurrency, conflict, cycle, fan-out/fan-in,
   composition, local mutation, divergence/merge, schema migration, partial
   corruption, rollback, replay, and successor-retire scenarios.
7. **Differential oracles:** full replay versus incremental materialization;
   raw-memory MI-1 versus PTAL MI-1; fixed routing versus contract planner;
   exported split plus boundary manifest versus original dependency closure.
8. **Measures:** reconstruction fidelity, hallucinated commitment, missing
   context, exact/semantic preservation, explanation size, invalidation radius,
   replay time, incremental latency, storage blow-up, merge conflicts, human
   annotation effort, and maintenance cost.
9. **Adversarial gates:** forged authority, digest collision assumptions,
   ambiguous entity labels, cyclic justifications, missing transform versions,
   incompatible schemas, and maliciously understated loss.
10. **Exit criterion:** do not adopt until it beats exact Markdown/Git baselines
    on reconstruction and lifecycle safety with tolerable operational overhead.

## OPEN_UNKNOWNS

- minimum useful claim granularity without destroying narrative meaning;
- formal authority/acceptance semantics and delegation boundaries;
- whether recorded, valid, decision, and observation time need two or more axes;
- stable-lineage identity rules under split, merge, and re-description;
- an operational equivalence oracle for multilingual natural-language claims;
- tractable ATMS/provenance summarization under dense alternative contexts;
- minimum planner inputs and whether `Pi` can be elicited reliably;
- which specialized model semantics require first-class authority rather than a
  derived projection;
- acceptable conservative invalidation and replay thresholds;
- how to version rules while comparing old and new reconstructions fairly;
- whether CORE-A can be tested without turning flexible principles into a rigid
  ontology;
- privacy, deletion, and legal-retention requirements for immutable evidence;
- empirical domain scenarios beyond the current research-memory corpus.

## WHY_THIS_COULD_BE_WRONG

The proposal may solve auditability more strongly than it solves modeling. Git
plus exact Markdown, a small typed manifest, and a few derived indexes may be the
smallest sufficient system. TMS/ATMS originated for propositional reasoning;
qualitative research prose may not admit stable atomic claims or justifications.
The ledger schema itself is object-like and could merely hide, rather than avoid,
an object-first worldview. Natural-language meaning cannot be made lossless by
adding metadata. The proposed planner may be `R(S,M,L)` renamed and expanded,
not genuinely improved. Some executable behaviour/rule model may need to be
co-authoritative because its generative semantics cannot be recovered from
claim records. Finally, all benefits are presently reasoned expectations; no
Byul experiment has yet shown that the extra structure improves reconstruction,
semantic preservation, lifecycle robustness, or Owner usefulness.

The correct response to these risks is an empirical minimal spike and blinded
comparison, not implementation by default.
