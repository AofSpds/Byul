# PHASE 1 FROZEN — Provenance Event Ledger with Contracted Projections

ROUND_ID = `BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01`

ROUND_SLOT = `R05`

RUN_ID = `v0.1.06`

WORKER_ID = `20260822-053804-83071800`

PROFILE = `NEUTRAL_BLIND`

PHASE1_RESEARCH_BASELINE_COMMIT = `891e4bd4b999eacc99431ed0db05062901a68dd9`

PHASE1_INPUT_METHOD = `EXACT_GIT_OBJECT_READS_ONLY`

CURRENT_IMPLEMENTATION_READ_DURING_PHASE1 = `FALSE`

## CURRENT_STATE_RECONSTRUCTION

Byul is a working, non-normative research track about preserving and operating an evolving research state. The state includes exact source material, Owner directions, working hypotheses, open questions, explicit non-conclusions, provenance, model-family candidates, and lifecycle history. The high-resolution worldview currently explores local mappings/processes composing into persistent higher-scale views, but it is not a scientific or implementation axiom. BYUL CORE-A asks designs to remain compatible with change, non-substantial/derived entities, composition/emergence, and conditional relationality without selecting a formalism.

The baseline is deliberately undecided about primitives and canonical models. Petri/Open Petri/Reconfigurable Petri, occurrence nets, event structures, causal-order views, and LTS/reachability views are candidates with complementary strengths. `R(S,M,L)` is a routing hypothesis, not an accepted law. `Preservation Demand` is a promising situation feature. The required research problem is therefore not merely to store a latest summary or choose a graph type. It is to preserve the evidence and epistemic status from which many purpose-specific models can be reproduced, while making every transformation's loss visible and preventing a derived view from silently becoming ground truth.

The baseline also records an important terminology correction: a canonical `P-series` is not evidenced. BYUL CORE-A and explicit preservation contracts may be reviewed, but an undefined P-series gate must not manufacture a PASS.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

- The exact raw research memos and their provenance are designated primary DATA in the baseline.
- The research state is `WORKING / NON_NORMATIVE / NOT_VALIDATED`; production is not authorized.
- BYUL CORE-A currently includes change/mutability, non-substantial or derived entities, composition/emergence, and conditional relationality; it does not force a formalism.
- The candidate formalism family is intentionally complementary and non-canonical.
- History, hypothesis/fact separation, explicit OPEN and NON_CONCLUSION states, transformation loss, reconstruction class, and lifecycle behavior are required concerns.
- The baseline proposes `R(S,M,L)` and identifies Preservation Demand as a strong candidate feature, while leaving both open to falsification.
- Discarded transformation semantics are not automatically reconstructable.
- A formal canonical P-series is not supported by the baseline evidence.

### OWNER_DIRECTION

- Preserve intent without locking the solution.
- Prefer established prior art and avoid inventing theory when existing models suffice.
- Treat the world-model hypothesis as a research direction, not a proven physics or philosophy claim.
- Keep high-resolution worldview and implementation abstraction distinct.
- Test initial-state reconstruction, lifecycle mutation, transformation cost, cumulative drift, and adversarial scenarios.
- Route by the situation and what must be preserved rather than naming a preferred model in advance.

### WORKING_HYPOTHESIS

- A family of behavior, occurrence, causal, and state views may be more useful than one universal model.
- `R(S,M,L)` may select a target model set, transformation path, preservation contract, and validation plan.
- Preservation Demand may dominate surface situation type in routing decisions.
- Occurrence/fact and behavior/rule planes may need distinct representations.
- A current state may be reconstructable from an exact source baseline plus a complete, ordered history of explicit changes.

### OPEN

- The minimal primitive or algebra: event, mapping, interaction, composition, rewrite, typed morphism, or another basis.
- Which semantics must be exact, semantic, approximate, statistical, view-dependent, or intentionally non-recoverable.
- Whether one representation can be authoritative or different information kinds need multiple authorities.
- The smallest sufficient Situation Fingerprint and whether `R(S,M,L)` has the right arguments.
- Merge semantics for independently evolved, semantically conflicting research branches.
- Acceptance thresholds for drift, round trips, routing, lifecycle recovery, and reconstruction.
- Scale behavior for dense causality, unfolding, view invalidation, and long history.
- How strongly structured claims can become without stripping nuance from source language.

### NON_CONCLUSION

- Petri nets are not the canonical Byul model.
- Causal Set Theory is not the final architecture or proof of the Owner worldview.
- An event, mapping, object, or global clock is not established as the universal primitive.
- One canonical structured graph is not required.
- A derived summary, causal view, reachability graph, or reconstructed geometry is not ground truth merely because it is useful.
- Exact inverse transformation is not presumed; loss and non-uniqueness are normal outcomes.
- BYUL CORE-A does not itself grant scientific validation or Owner Acceptance.

### YOUR_INFERENCE

- The safest authority is not a normalized claim graph or one executable formalism. It is a byte-preserving source store plus an append-only, provenance-bearing semantic event ledger. Normalized claims, causal graphs, Petri/LTS models, summaries, and routing indexes should be reproducible contracted projections.
- Causal order should be explicit through parent/dependency links. Wall-clock time is optional metadata and must not manufacture a total order among independent records.
- Corrections should append revision/retraction/supersession records. They should not overwrite the prior assertion, because a changed research judgment is itself relevant state.
- A router should first prove semantic feasibility against the requested preservation contract, then optimize cost. Model-name selection is downstream of that proof.
- General semantic conflicts cannot safely be CRDT-merged. Automatic convergence should be limited to fields with declared commutative merge laws; unresolved alternatives must remain visible elsewhere.

## MINIMAL_PROBLEM_DEFINITION

Given immutable evidence artifacts `A`, an append-only set of semantic records `E`, a selected causal cut or head set `H`, a query/work request `Q`, and a preservation contract `P`, construct and operate a view `V` such that:

1. every result can identify the exact source artifacts and semantic records that support it;
2. replaying the same accepted records under the same reducer version deterministically reproduces the same state;
3. epistemic class, qualifier, authority scope, conflict, and explicit unknown/non-conclusion are not collapsed;
4. a transformation is rejected when its declared guarantee is weaker than `P` for any demanded field;
5. omitted semantics are recorded as loss and are never inferred back as if recovered;
6. branch, composition, split, migration, recovery, and succession preserve lineage and unresolved alternatives;
7. derived models remain replaceable and rebuildable rather than silently becoming authority.

The minimum sufficient system therefore needs immutable content, immutable semantic changes, causal/provenance relations, deterministic projection rules, preservation/loss contracts, and verification receipts. It does not initially need an ontology of everything, a universal simulation formalism, or an automatic learned router.

## PHASE1_PROPOSAL

Use a **Provenance Event Ledger with Contracted Projections**. This is an implementation composition of established patterns rather than a novel mathematical theory.

### 1. Authoritative source-and-decision ledger

The authority consists of two inseparable stores:

- **Artifact store**: immutable exact bytes for memos, packets, attachments, datasets, code snapshots, and externally captured evidence. Each artifact has a cryptographic content ID, media type, byte length, ingest provenance, and optional human label. Text extraction is derived; the original bytes remain recoverable.
- **Semantic event ledger**: immutable canonical records representing research actions and decisions. Each record contains a schema version, record kind, payload, explicit source references, causal parents, author/agent, authority scope, optional source-valid time, operational record time, and content hash.

Core record kinds should be deliberately small:

- `INGEST`: register an exact artifact and its provenance.
- `ASSERT`: record a claim or direction with its epistemic class and verbatim evidence spans or artifact references.
- `RELATE`: add an explicitly typed relationship such as `supports`, `derived_from`, `depends_on`, `contradicts`, `specializes`, or `alternate_of`.
- `CLASSIFY`: assign or revise an epistemic class without rewriting the referenced content.
- `REVISE`, `RETRACT`, `SUPERSEDE`: record correction while retaining the prior record and reason.
- `BUNDLE`: name a coherent research snapshot/cut or context without copying its members.
- `TRANSFORM`: register a transformation execution and its receipt.
- `MERGE`: name multiple causal parents, the accepted commuting changes, and an explicit unresolved-conflict set.
- `FREEZE` and `SUCCESSOR`: identify immutable evaluation targets and their lineage.

`recorded_at` is an operational audit field, not metaphysical time. `valid_time` or source time is optional and may be unknown or interval-valued. Causal parents, explicit dependencies, and branch heads provide the authoritative partial order. A monotonically assigned local sequence may make storage/replay convenient but must not claim causal precedence between unrelated records.

### 2. First-class epistemic state

Every asserted item carries exactly one current classification as a *view over classification events*, with allowed baseline classes:

`SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, `YOUR_INFERENCE`, and `UNCLASSIFIED`.

The classification is not a truth value. `SOURCE_SUPPORTED` means the cited source supports that wording; it does not certify reality. Confidence, authority scope, and validation status are separate fields. Contradictory claims may coexist. A query may return `CONFLICTED`, `UNKNOWN`, or `REVIEW_REQUIRED` rather than resolve them.

Exact source excerpts are references into immutable artifacts, not substituted summaries. The structured assertion is an interpretation with its own agent and provenance. This preserves nuance and makes a mistaken extraction correctable without altering the evidence.

### 3. Deterministic contracted projections

All query-friendly structures are versioned reducers over a named ledger cut. A projection identity is:

`ProjectionID = hash(projector_id, projector_version, input_heads, parameters, policy_version)`.

The initial projection catalog should include only demonstrated needs:

- current research-state/handoff document;
- classification-indexed claim view;
- source and derivation provenance graph;
- chronology and causal/dependency view;
- open questions, non-conclusions, and conflicts;
- lifecycle/lineage view;
- full-text and embedding/search indexes, clearly marked non-authoritative;
- optional behavior/rule Petri view, occurrence/event-structure view, causal-order view, or LTS/reachability view when a request justifies one.

Materialized projections are caches. Deleting them must not delete authority; replay must rebuild them. A snapshot can accelerate replay only if it includes its exact heads, reducer version, content digest, and verification receipt.

### 4. Transformation contracts and receipts

Every transformation has a versioned `TransformSpec`:

- accepted input/output schemas and preconditions;
- field/relation-level guarantee: `EXACT`, `SEMANTIC`, `APPROXIMATE`, `STATISTICAL`, `VIEW_DEPENDENT`, `DROPPED`, or `UNKNOWN`;
- complement/sidecar required for reverse update or reconstruction;
- deterministic/non-deterministic flag and random seed policy;
- declared inverse or reverse synthesizer, if any;
- validation rules, expected complexity, and invalidation dependencies.

Every execution emits a `TransformReceipt` with exact input/output hashes, spec and code version, parameters, environment, loss report, validation outcomes, and agent. The receipt is ledger data.

Bidirectional lenses are used only where round-trip laws can be stated and tested. A writable derived view requires explicit `get/put` laws and retained complement. Otherwise the view is read-only; changes are submitted as new commands/events against the authority. This prevents an edited summary from overwriting qualifiers that the summary omitted.

### 5. Feasibility-first routing

Retain `R(S,M,L)` only as an externally compatible descriptive envelope, not as a learned oracle or canonical state model. Internally make the routing request explicit:

`Plan(Q, P, A, L, B) -> {feasible plan set, proof obligations, costs, validation plan}`

- `Q`: workload/query intent and output form.
- `P`: field/relation-level preservation demand.
- `A`: available authoritative artifacts, ledger cut, projections, transformation capabilities, and known loss.
- `L`: lifecycle operation such as create, mutate, compose, split, merge, migrate, recover, or retire.
- `B`: operational budgets and scale constraints.

Static feasibility comes first. Compose transformation guarantees along each candidate path; if any demanded item degrades below `P`, reject that path. Rank only feasible paths by compute, semantic risk, maintenance, reversibility, invalidation radius, and query performance. Unknown inputs produce `REVIEW_REQUIRED` or a conservative raw-source plan. Petri, Event Structure, causal, LTS, RDF, relational, and document views appear only as registered capabilities after this check.

In the old notation, `S` carries `Q + P + B`, `M` is the observed `A`, and `L` remains lifecycle context. This decomposition makes Preservation Demand explicit and makes routing falsifiable without asserting that the three-argument notation is necessary.

## PRIOR_ART_BASIS

The proposal composes the following established prior art:

1. **Event Sourcing and materialized read models.** Event sourcing stores changes in an append-only system of record and reconstructs state by replay; CQRS/materialized views separate authority from query-optimized views. The pattern's schema-evolution, replay, ordering, privacy, and complexity costs are acknowledged rather than hidden. Sources: [Microsoft Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing), [Microsoft CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs), and [Martin Fowler's original Event Sourcing description](https://martinfowler.com/eaaDev/EventSourcing.html).
2. **W3C PROV.** PROV-DM supplies entities, activities, agents, derivation, revision, quotation, primary-source, invalidation, bundles, collections, specialization, and alternate relations. PROV Constraints adds uniqueness, event-ordering, impossibility, and type validation. Use this as the interchange vocabulary for provenance projections, not as the entire canonical Byul ontology. Sources: [PROV-DM](https://www.w3.org/TR/prov-dm/) and [PROV Constraints](https://www.w3.org/TR/prov-constraints/).
3. **Content-addressed history DAGs.** Git's official data model demonstrates immutable blobs/trees and commits with zero or more parents, including multi-parent merges. Byul can use the same structural idea while keeping semantic claims and validation outside Git's object semantics. Source: [Git data model](https://git-scm.com/docs/gitdatamodel.html).
4. **Bidirectional transformations/lenses.** Foster et al. formalize `get`/`put` transformations and well-behavedness for view updates, including the need for retained concrete information. This supports the rule that only law-checked projections are writable. Source: [Combinators for Bidirectional Tree Transformations](https://www.cis.upenn.edu/~bcpierce/papers/newlenses-full.pdf).
5. **CRDTs with a strict boundary.** Shapiro et al. show convergence under explicit algebraic/causal conditions. They justify automatic merge for declared set/counter-like metadata but not silent reconciliation of arbitrary research meaning. Source: [Conflict-free Replicated Data Types](https://pages.lip6.fr/Marek.Zawirski/papers/CRDTs-SSS2011.pdf).
6. **Temporal databases.** The distinction between valid time and transaction/record time prevents the ingest timestamp from being confused with when a claim applied in the modeled domain. Source: [Richard Snodgrass, Temporal Databases](https://www2.cs.arizona.edu/~rts/pubs/EDC.pdf).
7. **Canonical serialization.** RFC 8785 provides a concrete JSON canonicalization scheme suitable for stable record hashing, subject to schema restrictions and implementation tests. Source: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html).
8. **Query provenance.** Provenance semirings show that derivation explanations for relational/Datalog queries can be calculated compositionally. This is an optional future technique for structured query projections, not a requirement for the first implementation. Source: [Green, Karvounarakis, and Tannen, Provenance Semirings](https://doi.org/10.1145/1265530.1265535).

The architecture is intentionally conservative: raw evidence plus event history is simpler and more reversible than making RDF, Petri, Event Structure, a property graph, or a vector database authoritative.

## AUTHORITATIVE_REPRESENTATION

The authoritative representation is the union of:

`Authority(H) = ImmutableArtifacts referenced by Ancestors(H) + AcceptedSemanticRecords in Ancestors(H)`.

`H` is one or more named heads. Records are canonical-serialized, content-hashed, append-only, and connected by explicit causal parents. Artifact bytes are independently hashed. A record may reference an artifact without embedding or normalizing it. A `FREEZE` record identifies an evaluation cut.

This is one logical authority with two physical object types, not competing authorities. Artifact bytes are authoritative for what the source contained. Semantic records are authoritative for what an agent classified, asserted, revised, related, or accepted. Neither is automatically authoritative for external truth.

Minimal storage schema for a prototype:

- `artifact(hash, media_type, byte_length, storage_uri, ingest_record)`;
- `record(hash, canonical_json, schema_version, kind, agent, recorded_seq, recorded_at)`;
- `parent(child_hash, parent_hash, relation)`;
- `artifact_ref(record_hash, artifact_hash, selector, role)`;
- `head(name, record_hash)` as mutable operational pointers whose movements are themselves audited;
- immutable triggers preventing record/artifact update or delete;
- rebuildable projection tables keyed by `ProjectionID`.

Stable IDs are handles to immutable occurrences or content, not claims of persistent substance. A named entity/persona/object view may change because it is derived from records and relations at a cut.

## DERIVED_REPRESENTATIONS

- Byte-exact source catalog and provenance report.
- Current-state and handoff prose generated from classified records with citations.
- Claim/classification/conflict graph.
- W3C PROV export for interoperable provenance.
- Causal/dependency DAG and ancestry index.
- Chronology view separating recorded time, source-valid time, and causal order.
- Lifecycle DAG: lineage, revisions, freezes, successors, branches, merges, migrations, invalidations.
- Search views: full-text, lexical facets, embeddings, and retrieval summaries; none grants authority.
- Purpose-specific formal models: Petri/Open Petri/Reconfigurable Petri, occurrence net, event structure, causal-order view, or LTS/reachability graph, each with an explicit transform contract.
- Evaluation views: preservation matrix, loss report, drift history, test receipts, and cost metrics.

No derived representation is required to encode all information. Its contract defines its useful questions and exclusions.

## PRESERVATION_CONTRACT

Each request declares required grades by semantic item, not one grade for the entire transformation. Mandatory default invariants are:

- exact artifact bytes, content hashes, and source selectors: `EXACT`;
- record payload, schema version, causal parents, agent, authority scope, and record kind: `EXACT`;
- epistemic class, explicit OPEN/NON_CONCLUSION, conflict status, and uncertainty: `EXACT` unless the request explicitly permits less;
- provenance and transform-receipt chain: `EXACT`;
- ordering: causal order `EXACT`; wall-clock/valid-time precision only as supplied;
- summaries and normalized claims: at most `SEMANTIC` unless proven byte-exact;
- statistical/embedding retrieval: `APPROXIMATE` and non-authoritative;
- generated formal models: per-relation grades stated in their transform specs.

Transformation composition uses the weakest guarantee along the path. `DROPPED` or `UNKNOWN` never upgrades during reverse synthesis. An apparent reconstruction can be labeled `SYNTHESIZED` or `INFERRED`, never `RECOVERED_EXACT`, unless byte/structure equality and semantic obligations both pass.

## LOSS_AND_NON_RECOVERABLE

The system cannot recover:

- meaning or intention never captured in an artifact or record;
- external truth from the fact that a source asserted something;
- qualifiers, alternatives, ordering, metric anchors, or transformation labels discarded without a complement;
- exact original wording from a summary alone;
- an author's unstated confidence or causal rationale;
- a unique source model from a many-to-one view;
- a silently resolved alternative after its branch/conflict record is deleted;
- precise source-valid time where only ingest time exists;
- semantics from a cryptographic hash alone.

Compression, embedding, causal forgetting, unfolding truncation, state aggregation, anonymization, and legal erasure must each emit explicit loss. Approximate reconstruction is a new derived artifact with lineage, not restoration of the missing original.

## TRANSFORMATION_PATHS

Representative registered paths are:

1. source artifact -> extraction -> assertion candidates -> reviewed semantic records;
2. ledger cut -> classified state/handoff view;
3. ledger cut -> W3C PROV projection -> validated provenance report;
4. rule-bearing records -> Petri/Open-Petri projection -> reachability/LTS view;
5. occurrence records -> occurrence/event-structure projection -> causal-order view;
6. projection edit -> lens `put` with retained complement -> proposed ledger command, only for law-checked writable views;
7. old schema records -> versioned upcast in memory -> new projection, with original record bytes retained;
8. selected subgraph -> export bundle with boundary dependency manifest -> import/compose receipt;
9. divergent heads -> structural union -> semantic conflict detection -> explicit merge record or `REVIEW_REQUIRED`.

Each arrow is independently versioned and receipted. A multi-hop path is rejected if preservation obligations cannot be composed.

## LIFECYCLE_BEHAVIOR

- **Create/ingest:** hash exact artifacts; append ingest and classification records; validate schema and references.
- **Operate/accumulate:** append commands as semantic records; update disposable projections incrementally; periodically replay from zero in verification.
- **Mutate:** append revise/retract/supersede records. Never edit an accepted record in place.
- **Compose:** union content-addressed records and artifacts, preserve namespaces/heads, validate references, and add a bundle/composition record with interface mappings.
- **Split:** select a causal subgraph or semantic bundle; include a boundary manifest for referenced records left outside; label the export closed, open, or incomplete.
- **Diverge:** create new named heads with a shared ancestor. Each branch remains reconstructable without pretending to be a successor generation.
- **Merge:** union immutable records; automatically merge only operations with declared commutative laws; record semantic conflicts and alternatives; append a multi-parent merge decision when reviewed.
- **Migrate:** replay through a versioned adapter into a new store/projection; compare invariant manifests and retain the old authority until verification passes.
- **Degrade/recover:** fail over to raw artifact plus ledger access; rebuild projections; verify digests, parent closure, snapshots, and transform receipts.
- **Successor/retire:** freeze an exact cut, create a successor head with an explicit parent and changed contract, and retain or tombstone the predecessor according to declared retention.
- **Invalidate:** traverse the projection dependency graph from changed record hashes; rebuild only affected projection partitions; periodically compare incremental and full rebuild results.

## ROUTING_POSITION

`R(S,M,L)` is useful as a vocabulary but underspecified as an implementation contract. The proposal therefore **modifies rather than discards** it:

- Preservation Demand is a required first-class input, not a soft feature hidden inside `S`.
- `M` is not one current canonical model; it is the available authority cut, materialized capabilities, known loss, and lineage.
- `L` remains valuable because merge, recovery, migration, and steady-state queries have different acceptable plans.
- The router returns a proof-obligation/loss report as well as a model set and cost.
- Rules begin deterministic and auditable. Learned ranking may be added only after a scenario corpus exists; it cannot waive feasibility gates.

The null route is valid: return exact source records, `UNKNOWN`, or `REVIEW_REQUIRED` when no transformation satisfies the contract.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY:** state is a succession of immutable occurrences and changing heads, not an overwritten timeless object. Correction history remains observable.
- **NON-SUBSTANTIALITY / DERIVED ENTITY:** objects, personas, current state, and boundaries are projections over records at a cut. Stable handles are operational references, not ontological substances.
- **COMPOSITION / EMERGENCE:** bundles and multi-parent composition preserve lineage from local records to higher-scale views. Higher-scale structure is permitted without claiming total reduction.
- **CONDITIONAL RELATIONALITY:** meaning, classification, authority, and behavior are scoped by context, sources, relations, and selected cut. Independent records are not forced into a global order.

Alignment is a review result, not scientific proof. The ledger can also record future challenges or revisions to CORE-A without corrupting earlier evaluation targets.

## EXPECTED_FAILURE_MODES

- Event capture is incomplete, so replay reproduces the recorded history but not the real research process.
- Over-atomizing prose strips context or creates false precision; under-structuring makes useful projections unreliable.
- Event schema evolution and reducer evolution yield divergent replays.
- A supposedly deterministic projector depends on locale, unordered iteration, floating point, network calls, or model nondeterminism.
- Append-only history grows without bound and creates privacy/legal-erasure conflict.
- Content hashes leak equality or enable dictionary attacks against sensitive small artifacts.
- Causal-parent choice is mistaken or omitted, creating false independence or false order.
- Conflict sets accumulate faster than humans can review them.
- Automatic merge laws are applied to fields whose semantics are not actually commutative.
- Projection users treat a convenient summary, embedding, or formal model as authority despite labels.
- Transform specs overclaim `SEMANTIC` or `EXACT` preservation without an executable oracle.
- Routing feature capture costs more than the query gain, or the planner rejects useful approximate work.
- Dense dependencies cause invalidation or ancestry indexes to approach quadratic behavior.
- Snapshot corruption or an unpinned reducer makes recovery appear successful while changing meaning.
- Raw source immutability conflicts with retention requirements; crypto-erasure/tombstones preserve structure but intentionally destroy content.

## FALSIFICATION_TESTS

The proposal should be rejected or materially revised if any of these repeatedly occurs under controlled tests:

1. Two independent conforming replayers produce different projection hashes from the same ledger cut and reducer version.
2. Ingest/export fails byte equality for any supported artifact type.
3. A correction, retraction, or successor makes the earlier assertion or its rationale unreachable.
4. A current-state view silently converts OPEN/NON_CONCLUSION/YOUR_INFERENCE into fact or drops a source qualifier.
5. A derived view cannot identify its ledger heads, projector version, and supporting records.
6. A lossy path is labeled exact, or reverse synthesis resurrects dropped data without marking inference.
7. A branch merge silently selects one semantically conflicting claim or loses the shared ancestor.
8. Incremental projection differs from a clean full replay.
9. Deleting all materialized views prevents recovery from artifacts plus ledger.
10. The router selects a path whose composed guarantees are weaker than the request contract.
11. A simpler immutable-document-plus-version-history design matches preservation/recovery while materially reducing schema, operation, and review cost.
12. Real users cannot reliably distinguish source content, interpretation, authority, and current acceptance despite the schema.

## IMPLEMENTATION_TEST_PLAN

### Prototype scope

Implement only the artifact store, ledger, deterministic projectors, contract checker, and receipts. Use Python with SQLite plus a content-addressed blob directory for the first executable slice. Use RFC 8785 canonical JSON or a strictly tested equivalent; prohibit non-canonical numbers and unknown schema fields. Add database triggers or an application-enforced audit that forbids accepted-record update/delete. Keep RDF, Petri, event-structure, causal, LTS, and embedding support as plugins/projections.

Minimum commands:

`ingest`, `assert`, `classify`, `relate`, `revise`, `retract`, `freeze`, `branch`, `merge`, `project`, `plan`, `verify`, `export`, and `recover`.

### Test layers

1. **Schema/unit:** canonical hash stability, unknown-field rejection, reference closure, epistemic enum separation, optional-time handling, immutable-record enforcement.
2. **Golden replay:** T1 sequence, T2 concurrency diamond, T3 conflict branch, T4 repeating pattern with new occurrences, T6 fan-out/fan-in, T8 reconfiguration, T9 composition, T10 local invalidation.
3. **Property/metamorphic:** replay idempotence; projection deletion and rebuild; equivalent append batch boundaries; commutative merge only for declared CRDT fields; non-commutative semantic edits always conflict.
4. **Transformation:** field-level preservation matrices, round-trip lens laws where applicable, explicit loss injection, repeated conversion drift, inverse non-uniqueness labeling.
5. **Lifecycle:** branch/diverge/merge, split with missing boundary dependency, schema migration, snapshot corruption, partial write, crash recovery, successor freeze, tombstone/erasure.
6. **Differential:** full replay versus incremental projection; two independent reducer implementations; old versus migrated schema results on a fixed corpus.
7. **Adversarial semantic fixtures:** fact/hypothesis/Owner direction mixtures, negated non-conclusions, conflicting sources, changed Owner direction, ambiguous pronouns, missing dates, and summaries that tempt false certainty.
8. **Routing:** enumerate candidate paths for small catalogs, verify feasibility by exhaustive comparison, and ensure UNKNOWN yields conservative routing.
9. **Scale:** measure append, replay, ancestry, dependency invalidation, storage growth, and projection query latency across sparse and dense graphs.
10. **MI-1:** give a fresh instance only the exported authority cut and score state reconstruction, classification separation, open-question preservation, provenance accuracy, and hallucinated commitments.

Initial acceptance gates should be qualitative plus hard invariants: zero byte-loss, zero silent epistemic-class collapse, zero silent conflict resolution, deterministic clean replay, explicit loss for every known lossy transform, and successful projection rebuild. Numeric performance thresholds should be set only after corpus measurements.

## OPEN_UNKNOWNS

- The right granularity for assertion records and evidence selectors.
- Whether canonical JSON is sufficient for every artifact/record type or a binary canonical encoding is needed.
- The minimum relation vocabulary that avoids both ambiguity and ontology sprawl.
- How to express semantic-equivalence oracles for prose transformations without circular LLM judgment.
- Which projection edits deserve lawful lenses and which must remain command-only.
- How to handle confidential evidence, legal erasure, and content-hash leakage.
- Whether valid-time intervals, causal parents, and local recorded sequence are enough for all research chronology cases.
- Which CRDT substructures, if any, are genuinely safe beyond tags and memberships.
- How to bound unresolved conflict growth and human review load.
- Whether provenance semirings or simpler explicit receipt edges are sufficient for the expected query workload.
- Whether preservation-contract authoring becomes too expensive for ordinary research actions.
- How CORE-A conflict review should be operationalized without turning it into an automatic truth gate.

## WHY_THIS_COULD_BE_WRONG

Event sourcing may be unnecessary architecture for a research repository whose material changes are already captured well by Git commits and curated documents. The proposal duplicates some Git behavior and adds record schemas, projectors, and migration obligations. If the main failure is poor writing discipline rather than lost operational history, better document templates and reviews could be stronger and cheaper.

The ledger also assumes that meaningful changes can be captured as events. Research understanding is often continuous, retrospective, and linguistically ambiguous. Forcing every judgment into discrete records may create a false causal story or burden the Owner. Raw artifacts mitigate but do not eliminate this risk.

The split between authority and projections can become dogma. Some formal models may contain constructive semantics that are not derivable from prose and deserve authoritative status. The proposed answer would then need multiple explicitly scoped authorities or to record model authoring itself as authoritative artifacts and semantic events.

Preservation contracts may promise more precision than reviewers can validate, especially `SEMANTIC` equivalence for natural-language summaries. A system can be perfectly reproducible and still reproduce a mistaken extraction. Provenance supports audit, not correctness.

Finally, the feasibility-first router may be too conservative and complex. A small number of explicit workflows could outperform general routing. The architecture should therefore begin with a fixed catalog and null route, and must be replaced if a simpler versioned-document design passes the same falsification and lifecycle tests.

PHASE1_IMPLEMENTATION_PERFORMED = `FALSE`

IMPLEMENTATION_AUTHORITY = `NONE`
