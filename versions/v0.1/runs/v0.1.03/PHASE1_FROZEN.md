# Phase 1 Frozen Proposal — Contracted Epistemic Event Ledger with Reproducible Projections

ROUND_SLOT = R01

RUN_ID = v0.1.03

PROFILE = NEUTRAL_BLIND

PHASE1_RESEARCH_BASELINE_COMMIT = 891e4bd4b999eacc99431ed0db05062901a68dd9

PHASE1_INPUT_SCOPE = only the packet-listed Git objects at the exact baseline above, plus the prior-art sources listed below

CURRENT_IMPLEMENTATION_READ_DURING_PHASE1 = FALSE

OTHER_RUN_OUTPUT_READ_DURING_PHASE1 = FALSE

## CURRENT_STATE_RECONSTRUCTION

Byul is a working, non-normative research track whose primary data is the evolving research memory itself. The active questions are how to preserve source text, provenance, epistemic status, open questions, non-conclusions, transformation loss, lineage, and lifecycle history while producing purpose-specific representations. BYUL CORE-A currently names four Owner-adopted research principles—change/mutability, non-substantiality/derived entity, composition/emergence, and conditional relationality—but is neither an AAA canonical requirement nor a scientifically validated axiom.

The baseline's Petri/Open Petri/Reconfigurable Petri, Occurrence Net, Event Structure, causal-order, and LTS candidates are a working complementary family, not selected answers. `R(S,M,L)` and Preservation Demand are working routing hypotheses. The baseline explicitly keeps the primitive/minimal algebra, canonical-versus-multi-authoritative choice, exact preservation semantics, lifecycle drift criteria, reconstruction acceptance, and minimum sufficient routing features open. It also corrects an earlier unsupported “P-series” abstraction: there is no established canonical P-series in the supplied baseline.

The central reconstruction result is that three kinds of thing are currently mixed in Markdown but must remain distinguishable in any model: (1) evidence of what was written and when; (2) explicit judgments about status, scope, authority, and succession; and (3) derived interpretations or computational views. A representation that preserves only document bytes cannot claim to preserve meaning, while a representation that replaces the bytes with extracted triples or a single formal model risks inventing or discarding meaning.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

- The active research state is working, non-normative, not validated, and not production-authorized.
- Primary data is the Byul research memory; exact source snapshots and provenance matter.
- BYUL CORE-A has four currently recorded directions with open count and explicit non-claim status.
- Current formalisms and the one-universal-model choice are not canonical conclusions.
- UNKNOWN, OPEN, OWNER_DIRECTION, working hypothesis, and non-conclusion distinctions must survive reconstruction.
- Transformation loss, round-trip delta, cumulative drift, invalidation radius, migration, recovery, and reconstruction class are named evaluation concerns.
- The baseline corrects “P-series” as an unsupported abstraction and forbids treating discarded semantics as automatically recoverable.

### OWNER_DIRECTION

- Explore a high-resolution worldview of local mappings/processes/interactions composing into persistent higher-scale patterns.
- Prefer succession/history over unexamined same-as identity; do not force global absolute NOW.
- Keep implementation freedom while testing model and transformation choices against BYUL CORE-A.
- Use prior art first, preserve uncertainty, avoid premature convergence, and validate lifecycle/transformation behavior empirically.

### WORKING_HYPOTHESIS

- A complementary model family may be stronger than one universal model.
- `R(S,M,L)` may route by Situation, Current Model State, and Lifecycle Context.
- Preservation Demand may dominate simple phenomenon-type features in routing.
- Raw memo/provenance can serve as ground representation while current/history/model-family/lifecycle structures are derived views.

### OPEN

- The minimal primitive or algebra for the worldview.
- The exact unit and granularity of preserved meaning.
- Whether one or several representations should be authoritative.
- Minimum sufficient routing inputs and whether `R(S,M,L)` is needed.
- Formalism fitness, transformation equivalence, reverse-synthesis acceptance, lifecycle drift thresholds, and scale limits.
- Authority semantics for Owner direction, research adoption, validation, and future acceptance.

### NON_CONCLUSION

- Petri is not canonical.
- Causal Set is not the final architecture.
- One universal model, one canonical semantic representation, and Event/Mapping as primitive are not established.
- Natural-language meaning, discarded transformation semantics, geometry, metrics, or conflicts are not automatically reconstructable from a causal skeleton or a digest.
- A projection, test result, or researcher recommendation is not Owner Acceptance.

### YOUR_INFERENCE

- The immediate engineering problem is better framed as epistemic memory integrity plus reproducible projection, not as selection of a universal world-model formalism.
- One authoritative event/provenance substrate and multiple disposable derived representations can satisfy the current evidence with fewer semantic commitments than making Petri, an event structure, an RDF graph, or `R(S,M,L)` itself canonical.
- Routing should be a constraint-checked view-planning operation driven first by an explicit preservation contract; `S`, `M`, and `L` can remain an input vocabulary but should not be the planner's untyped core.

## MINIMAL_PROBLEM_DEFINITION

Given immutable source artifacts and an evolving, possibly branching stream of explicit research judgments, reconstruct any declared research state or derived model such that:

1. every output can identify the exact evidence, judgment events, assumptions, transformation program, and schema version that produced it;
2. source-supported, Owner direction, working hypothesis, open, non-conclusion, and inference are never silently collapsed;
3. required meanings are preserved at a declared grade or the operation refuses;
4. fork, divergence, correction, supersession, merge, migration, recovery, and retirement do not erase prior states; and
5. no derived view is promoted to ground truth merely because it is convenient or executable.

The problem does not require solving the Owner worldview, discovering a physical primitive, or choosing one formalism for all questions.

## PHASE1_PROPOSAL

Adopt a **Contracted Epistemic Event Ledger with Reproducible Projections (CEEL-RP)**. This is an integration of established patterns, not a new mathematical theory.

### 1. Evidence store

Store every imported source artifact byte-for-byte under a content digest. Record media type, encoding, origin locator, import receipt, and addressable source spans. A digest proves identity/integrity of bytes, not truth or semantic equivalence.

### 2. Append-only epistemic event ledger

Every material change is a new, immutable, schema-versioned event. A minimal envelope contains:

- event ID and content digest;
- event type and schema version;
- recorded time and, when explicitly known, effective/valid time;
- zero or more parent event/checkpoint IDs (a partial order, not forced global simultaneity);
- actor/agent, authority claim, scope/context, and source span references;
- operation payload and explicit supersedes/retracts/qualifies/derives/transforms relations;
- assumption/context identifiers; and
- signatures or repository commit anchors when available.

Event types should stay small and operational: import evidence, assert/qualify status, supersede, retract, derive, transform, branch, merge, checkpoint, redact, and retire. Domain ontologies and formal models belong in versioned payload schemas, not in the immutable envelope.

### 3. Meaning capsules

Important passages may receive explicit, reviewable meaning capsules. A capsule records a natural-language claim or optional typed payload, exact supporting/contradicting spans, epistemic class, scope, assumptions, authority, confidence if stated, validity interval if stated, and successor relations. The capsule is authoritative only for the fact that an authorized actor made that classification; it does not make the proposition true. Machine extraction may draft capsules but cannot silently commit them.

The initial epistemic classes should be the baseline's distinctions rather than a new truth scale: `SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, and `INFERENCE`, with `UNKNOWN` where classification is unresolved.

### 4. Derivation and transformation receipts

Every projection or conversion emits a receipt containing exact input IDs/digests, projector/transformer ID and version, parameters, output digest, declared preservation contract, observed validation results, dependency set, and explicit loss set. Receipts compose: an output's guarantee can never be stronger than the weakest relevant input or transformation guarantee without new anchored evidence.

### 5. Reproducible projections

Current-state summaries, chronologies, provenance graphs, assumption-context graphs, search indexes, causal-order views, RDF/PROV exports, LTS reachability graphs, Petri-family behavior models, and simulation inputs are materialized projections. They are disposable and rebuildable from a pinned ledger checkpoint plus pinned code/schema. A Petri or LTS model that introduces possible behavior not explicitly present in evidence is a labeled model hypothesis, not a lossless view.

Use ATMS-like assumption sets only where incompatible research contexts must coexist. Use CRDT-style set convergence only for replicated immutable IDs and acknowledgments; semantic conflict resolution must remain explicit and must not become last-writer-wins.

### 6. Contract-driven planner

Replace informal model-name routing with a capability registry and constraint-checked planner. Normalize `R(S,M,L)` into:

`PLAN(Intent, PreservationContract, AuthorityAndLossCatalog, LifecycleOperation, ResourceBounds)`

Each projection/transform declares supported queries, required inputs, preservation grades by semantic dimension, lifecycle operations, reversibility, cost observations, and invalidation dependencies. The planner finds a path that satisfies all mandatory grades, otherwise returns `REVIEW_REQUIRED` with the unmet dimensions. `S`, `M`, and `L` remain useful user-facing groupings, but the preservation contract and current authority/loss catalog are first-class rather than hidden fields.

### 7. Storage-neutral implementation boundary

The architecture can begin with content-addressed files plus append-only JSON Lines and SQLite materialized indexes. JSON Schema can version envelopes; a relational or property-graph projection can answer queries. RDF/PROV is an interchange projection, not mandatory internal storage. No distributed log, triple store, Petri engine, or novel algebra is required for the first falsification prototype.

## PRIOR_ART_BASIS

- Event Sourcing stores state changes as an event sequence and supports rebuild, temporal query, and replay; it motivates the authoritative ledger/materialized-state separation. Martin Fowler, [Event Sourcing](https://www.martinfowler.com/eaaDev/EventSourcing.html). Empirical work also reports schema evolution, projection rebuild, learning, and privacy as real difficulties, motivating versioned events and explicit migration tests: Overeem et al., [An Empirical Characterization of Event Sourced Systems and Their Schema Evolution](https://arxiv.org/abs/2104.01146).
- W3C PROV provides interoperable concepts for entities, activities, agents, derivations, and bundles; it grounds provenance receipts without requiring PROV to become Byul's ontology. [W3C PROV Overview and recommendations](https://www.w3.org/TR/prov-overview/).
- Temporal databases distinguish valid/effective time from transaction/recorded time; this grounds the two-time envelope without claiming either is absolute physical NOW. Richard Snodgrass, [Temporal Databases](https://www2.cs.arizona.edu/~rts/pubs/EDC.pdf).
- Assumption-based truth maintenance keeps justifications relative to assumption sets and can represent multiple inconsistent contexts; it grounds scoped alternative research contexts. Johan de Kleer, [An assumption-based TMS](https://doi.org/10.1016/0004-3702(86)90080-9).
- Materialized-view maintenance grounds disposable derived indexes and dependency-based incremental invalidation. Gupta, Mumick, and Subrahmanian, [Maintaining views incrementally](https://doi.org/10.1145/170036.170066).
- Bidirectional lenses make round-trip laws explicit and expose when view updates cannot be safely inverted. Foster et al., [Combinators for Bi-Directional Tree Transformations](https://www.cis.upenn.edu/~bcpierce/papers/newlenses-popl.pdf).
- Provenance semirings show how derivational lineage can be propagated through positive relational queries; they are a possible later implementation for query receipts, not required in the minimal prototype. Green, Karvounarakis, and Tannen, [Provenance Semirings](https://www.cs.ucdavis.edu/~green/papers/pods07.pdf).
- CRDT research grounds deterministic convergence for carefully chosen replicated data types, while not solving semantic conflict in arbitrary claims. Shapiro et al., [Conflict-Free Replicated Data Types](https://inria.hal.science/inria-00609399/document).

## AUTHORITATIVE_REPRESENTATION

The authoritative representation is the pair `(content-addressed evidence store, append-only epistemic event ledger)` at an exact checkpoint. Authority is field-specific:

- evidence bytes are authoritative for what the captured artifact contained;
- ledger events are authoritative for which explicit action/classification was recorded by whom and under what declared authority;
- meaning capsules are authoritative for an explicit classification or statement, not for objective truth;
- external metric/clock/space facts are authoritative only through separately identified anchors;
- no materialized projection is authoritative unless a future policy explicitly promotes a named field, and promotion itself must be an event.

This is one authoritative operational substrate, not one canonical ontology or one claim that all information has the same natural representation.

## DERIVED_REPRESENTATIONS

- current-state and historical-state folds;
- epistemic-status matrix and OPEN/non-conclusion registers;
- provenance and derivation DAG;
- bitemporal timeline and succession graph;
- ATMS-like assumption/context labels;
- full-text/search and semantic indexes;
- causal-order, concurrency, conflict, and reachability views when inputs justify them;
- Petri/Open/Reconfigurable Petri behavior hypotheses when explicit rules/resources/interfaces are available;
- RDF/PROV interchange bundles;
- lifecycle dependency/invalidation graph;
- benchmark and simulation fixtures.

Each carries its checkpoint, generator version, receipt, loss declaration, and staleness state.

## PRESERVATION_CONTRACT

Every transformation declares a grade per semantic dimension: `EXACT`, `SEMANTIC`, `ANCHORED`, `STATISTICAL`, `VIEW_DEPENDENT`, `NON_RECOVERABLE`, or `UNKNOWN`. At minimum track:

- source bytes, encoding, digest, and addressable spans;
- source locator and import provenance;
- actor and declared authority;
- epistemic class and uncertainty;
- scope/context and assumption set;
- recorded time, stated effective time, and their uncertainty;
- parent/succession, supersession, retraction, split, and merge relations;
- supporting, contradicting, and derivation lineage;
- transformation labels, parameters, code/schema versions, and loss declarations;
- conflicts and non-conclusions;
- metric/clock/space anchors where present.

Mandatory contract laws:

1. **No strengthening:** UNKNOWN or loss cannot become EXACT without new evidence and an explicit event.
2. **No silent collapse:** multiple contexts, conflicts, and non-conclusions survive or the transformation refuses.
3. **Loss monotonicity:** composed paths accumulate known loss; they do not erase it.
4. **Deterministic replay:** the same checkpoint, schema, code, and parameters reproduce the same output digest, or nondeterminism is explicitly recorded.
5. **View-update safety:** edits to a derived view create proposed ledger events. Direct put-back is allowed only for a registered transformation with tested round-trip laws and unambiguous authority.
6. **Authority non-escalation:** a projector cannot manufacture Owner Acceptance, validation, or production authority.

## LOSS_AND_NON_RECOVERABLE

- Byte-exact storage cannot guarantee preservation of human pragmatics, unstated intent, ambiguity, irony, or future reinterpretation.
- An extracted claim graph cannot recover omitted context unless the source span remains available.
- Causal order cannot recover transformation labels, resources, conflicts, metrics, or possible behavior that were discarded.
- A Petri/LTS/Event model cannot be synthesized uniquely when evidence underdetermines rules.
- Hashes prove byte identity, not correctness, authorship, truth, or semantic equivalence.
- Redaction or legally required deletion may make source content non-recoverable; a tombstone can preserve that a deletion occurred but not the deleted meaning.
- If old projector code, schema definitions, anchors, or external dependencies are lost, exact historical view reconstruction may become non-recoverable even when the ledger survives.
- Human classification mistakes remain historically recoverable but are not self-correcting; correction requires a successor event.

## TRANSFORMATION_PATHS

1. `artifact -> digest + source spans -> IMPORT event` (byte identity exact; interpretation absent).
2. `source spans -> reviewed meaning capsule` (human assertion with provenance; not automatic truth extraction).
3. `checkpoint + projector -> materialized view + receipt` (rebuildable at declared grade).
4. `view + edit -> proposed event -> validation/authority gate -> successor checkpoint` (no direct hidden mutation).
5. `projection A -> registered transform -> projection B + loss record`; if reverse laws are unavailable, mark one-way/non-recoverable.
6. `checkpoint -> capability planner -> target projection set + transformation path + preservation proof or refusal`.
7. `old schema events -> version-aware decoder/upcaster -> new projection`; preserve old bytes and record the migration receipt.

## LIFECYCLE_BEHAVIOR

- **Mutate/correct:** append qualify, supersede, retract, or replacement events; never overwrite history.
- **Compose:** create a bundle referencing components, interface mappings, scope rules, and derivation receipt; do not flatten namespaces or authority silently.
- **Split:** create child streams from an exact checkpoint with an explicit partition policy; shared evidence remains content-addressed and lineage remains common.
- **Diverge:** allow branches and assumption contexts to evolve independently from a common ancestor.
- **Merge:** perform a three-way merge over events and typed fields. Commuting additions can converge; incompatible classifications, retractions, authority claims, or schema meanings produce an explicit conflict set for review, never last-writer-wins.
- **Migrate:** use versioned readers/upcasters or copy-and-transform into a new derived ledger/checkpoint while retaining the original; compare preservation contracts and digests.
- **Recover:** verify content digests, restore a checkpoint, replay later events, rebuild projections, and compare output receipts.
- **Invalidate:** traverse recorded dependencies from changed/superseded inputs; mark affected projections stale before incremental or full rebuild.
- **Successor/retire:** create a new schema/projector version, dual-run it against pinned fixtures, retain old receipts, then append an explicit retirement event.

## ROUTING_POSITION

`R(S,M,L)` is useful as a descriptive organizer but malformed as a sufficient executable contract because its bags can hide preservation grades, authority, loss, refusal criteria, and resource bounds. Keep it as an API facade if useful, but compile it into the explicit planner inputs proposed above.

The router does not select “the model that is true.” It selects the cheapest registered projection/transform path that can answer the declared intent without violating mandatory preservation grades. If none exists or a required capability is UNKNOWN, it returns a structured refusal and validation plan. A small deployment may use static registry rules; learned routing is premature until labeled scenario evidence exists.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY:** current state is a reproducible fold over successor events; correction changes the active view without pretending the prior state never existed.
- **NON-SUBSTANTIALITY / DERIVED ENTITY:** stable handles and entities are operational references or projections, not ontological substances. The ledger can carry relation- or process-shaped payloads without forcing object-first semantics.
- **COMPOSITION / EMERGENCE:** composed bundles and higher-scale views keep explicit lineage to local inputs and transforms; reducibility is not assumed where evidence is absent.
- **CONDITIONAL RELATIONALITY:** claims and meanings are scoped by context, assumptions, authority, and time; incomparable branches are not forced into a single global order.

Alignment is an engineering interpretation for review, not scientific validation of CORE-A.

## EXPECTED_FAILURE_MODES

- Log growth, slow replay, and projection rebuild cost.
- Event/schema evolution makes old events unreadable or changes meaning.
- Meaning-capsule extraction creates false precision or high curator burden.
- Dependency/provenance graphs explode and make invalidation nearly global.
- Concurrent semantic conflicts accumulate faster than humans resolve them.
- “Append-only” conflicts with privacy, redaction, or secret-removal obligations.
- Projector bugs deterministically reproduce the same wrong view.
- Clock skew or retroactive knowledge is confused with real-world event order.
- Capability declarations overstate preservation and cause unsafe routing.
- The planner grows into an untestable second ontology.
- Formal projections introduce behavior or causality that the notes did not support.
- A single ledger becomes an operational bottleneck or a false canonical ontology despite the design boundary.

## FALSIFICATION_TESTS

1. **MI-1 reconstruction:** encode the exact baseline and ask a fresh implementation to reproduce the classified state. Fail on hallucinated commitments, missing non-conclusions, or authority escalation.
2. **Correction/replay:** insert a retroactive correction with distinct recorded/effective times. Rebuild every checkpoint; fail if an old view mutates or a new view retains stale claims.
3. **Conflicting contexts:** assert incompatible hypotheses under different assumption sets. Fail if either vanishes, becomes globally true, or contaminates an unrelated context.
4. **Loss refusal:** request a view requiring transformation labels after a path that retained only causal order. The planner must refuse; any reconstruction claim falsifies the contract.
5. **Fork/merge:** independently reclassify the same capsule on two branches. The merge must expose a typed conflict, not choose by clock or branch order.
6. **Round-trip laws:** for each declared reversible transform, property-test get/put laws and semantic invariants; downgrade or remove reversibility on a counterexample.
7. **Schema migration:** replay old events through old and new readers on a golden corpus. Preserved dimensions must match, original digests must remain unchanged, and new loss must be explicit.
8. **Invalidation:** mutate one leaf, one shared source, and one schema. Compare calculated versus actual affected views; measure false negatives, false positives, and radius.
9. **Tamper/recovery:** corrupt evidence, events, checkpoints, projector versions, and receipts separately. Recovery must detect the exact broken dependency and never certify an unverifiable state.
10. **Router ablation:** remove each planner input and run T1-T10 plus mixed epistemic scenarios. A field is justified only if its absence creates a repeatable unsafe or materially more expensive plan.
11. **Scale:** benchmark long histories, fan-out/fan-in provenance, high-conflict branches, dense causal views, and repeated schema succession; record storage, replay, rebuild, query, and review costs.
12. **Minimality challenge:** compare CEEL-RP with plain Git+Markdown+manual indexes. If the added structure does not improve reconstruction fidelity, refusal safety, or lifecycle cost enough to justify itself, reject the proposal.

## IMPLEMENTATION_TEST_PLAN

Research-only proposed sequence; no implementation is authorized in this run:

1. Define a small versioned event envelope, meaning-capsule schema, preservation matrix, and capability descriptor.
2. Create a hand-reviewed golden fixture from the exact v0.01 baseline, including contradictory history and the P-series correction.
3. Prototype content-addressed artifacts and an append-only local ledger with deterministic checkpoint/replay.
4. Build only three projections first: current epistemic state, provenance/dependency graph, and chronology/succession view.
5. Add receipt generation, staleness/invalidation, structured refusal, and view-update-as-proposal.
6. Run unit, property-based, metamorphic, migration, tamper, fork/merge, and performance tests described above.
7. Only after baseline falsification tests pass, add one formal-model adapter justified by a real query; compare it with a no-adapter control.
8. Keep blind Owner+ASA evaluation separate from authorship. A test PASS is not Owner Acceptance.

Primary invariants to test are append-only history, idempotent import, deterministic replay, authority non-escalation, non-conclusion preservation, loss monotonicity, conflict visibility, and projection reproducibility.

## OPEN_UNKNOWNS

- The right claim/meaning-capsule granularity: document, section, span, sentence, proposition, or mixed.
- Who may assert each epistemic class and how authority changes across Owner, ASA, researcher, evaluator, and automated extractor.
- Whether Git commit time, author time, effective time, or an external clock has any required semantics.
- How to judge semantic equivalence of natural-language research claims without circular human review.
- Which fields actually require bitemporal treatment and which need only succession order.
- Privacy/redaction requirements and acceptable cryptographic-erasure/tombstone policy.
- Whether distributed/offline concurrent writing is a real requirement; if not, CRDT machinery should be omitted.
- Minimum useful projection set and whether a planner is justified before scale grows.
- Which formal-model adapter, if any, creates measurable query or simulation value.
- Acceptable storage, replay, invalidation, review, and migration costs.
- Whether natural-language evidence plus explicit status metadata is already sufficient, making typed meaning capsules unnecessary.

## WHY_THIS_COULD_BE_WRONG

The proposal may over-engineer a small Git-hosted research corpus. Git+Markdown already provides immutable-ish history, branching, merging, and byte-level recovery; a disciplined document template and generated indexes may deliver most value with far less machinery. Meaning capsules may impose costly annotation while still failing to capture actual meaning. Event sourcing shifts complexity into schema evolution, replay, privacy, and projection operations. ATMS-style contexts and contract planning may be unnecessary until there are many conflicting models or automated consumers. A single operational ledger may also become the very canonical representation the research intends to avoid.

The decisive test is therefore comparative and empirical: CEEL-RP should be rejected or reduced if it does not beat a minimal Git+Markdown baseline on blinded reconstruction fidelity, non-conclusion preservation, safe refusal, lifecycle recovery, and maintenance cost.

PHASE1_IMPLEMENTATION_PERFORMED = FALSE

IMPLEMENTATION_AUTHORITY = NONE

