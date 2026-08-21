# Phase 1 Frozen Proposal — v0.1.11

## Scope and epistemic status

This proposal was produced under the `ADVERSARIAL_REFRAME` profile. It uses only the required research files read as Git objects from `891e4bd4b999eacc99431ed0db05062901a68dd9`. It does not inspect or infer from the current v0.1 implementation. It is research advice, not implementation authority.

## CURRENT_STATE_RECONSTRUCTION

Byul is a non-normative research track concerned with reconstructing an evolving body of memory without silently converting facts, Owner direction, hypotheses, open questions, or explicit non-conclusions into one another. Its current high-resolution worldview hypothesis treats objects, identities, boundaries, and personas as potentially persistent views over changing compositions rather than permanent primitive substances. Succession and lineage are therefore more important than equality-by-handle, local composition may produce higher-scale structures, and meaning may depend on relations and context.

The current research direction explores a complementary family: Petri/Open/Reconfigurable Petri representations for possible behaviour and resources, occurrence/event structures for realized history, causality, concurrency, and conflict, causal-order views for ancestry, and LTS-like views for reachability. `R(S,M,L)` is a working routing candidate in which a situation fingerprint, current model state, and lifecycle context choose target models, transformations, preservation obligations, and validation. None of these formalisms, the multi-model arrangement, the router, a universal primitive, or a canonical representation has been accepted as the answer.

The authoritative research input is natural-language memory with provenance. That creates an unavoidable asymmetry: exact bytes can be preserved, but extraction into a formal graph or executable model is interpretive. A safe architecture must retain the source evidence and explicitly account for every semantic projection, loss, uncertainty, and later correction. Lifecycle behaviour and initial-state reconstruction quality are first-class evaluation targets, not secondary operational details.

## STATE_CLASSIFICATION

- `SOURCE_SUPPORTED`: The baseline explicitly records exact source/provenance preservation, fact/hypothesis/open/non-conclusion separation, transformation-loss discipline, lifecycle validation, and the named candidate model family.
- `OWNER_DIRECTION`: BYUL CORE-A is Owner-adopted within this research track: change/mutability, non-substantial or derived entities, composition/emergence, and conditional relationality. The Owner also requires lifecycle simulation and transformation-cost measurement. These are not scientific validation or AAA canonical acceptance.
- `WORKING_HYPOTHESIS`: The “network of innumerable local mappings,” a complementary formalism family, preservation-demand-first situation routing, and `R(S,M,L)` are strong candidates but remain unvalidated.
- `OPEN`: The primitive/minimal algebra, authoritative representation policy, minimum sufficient routing features, reconstruction acceptance thresholds, semantic-drift measurement, and model-family compatibility remain unresolved.
- `NON_CONCLUSION`: Petri is not canonical; Causal Set is not the final architecture; one universal model and one canonical representation have not been selected; discarded semantics are not automatically recoverable; the worldview does not prove physics.
- `YOUR_INFERENCE`: The model-family-first framing and `R(S,M,L)` expose too much derived machinery as if it were primary. A smaller evidence-and-claim ledger can be authoritative while all executable or analytic formalisms become disposable, capability-declared materialized views. This inference is the proposal to falsify, not a baseline fact.

## MINIMAL_PROBLEM_DEFINITION

Maintain an auditable succession of source evidence and typed research claims such that, at any pinned revision, a consumer can:

1. reconstruct what was recorded, who or what supported it, its epistemic class, scope, and lineage;
2. distinguish correction, retraction, refinement, conflict, and open uncertainty without erasing history;
3. derive fit-for-purpose views without claiming that omitted semantics can be recovered;
4. compose, branch, merge, migrate, and recover the record with bounded and explainable invalidation; and
5. test whether each derivation satisfies an explicit preservation contract.

This is an evidence/claims lifecycle problem before it is a Petri, event-structure, causal-set, or routing problem.

## PHASE1_PROPOSAL

Adopt a **Content-Addressed Epistemic Operation Ledger (CEOL)** as the single authoritative representation envelope.

CEOL has two inseparable strata:

1. **Evidence objects**: immutable, content-addressed source artifacts preserving exact bytes, path/locator, ingest time, source revision, media type, and digest.
2. **Epistemic operations**: an append-only sequence/DAG of typed operations over claims and relationships. Operations include `ASSERT`, `CLASSIFY`, `ANNOTATE`, `SUPERSEDE`, `RETRACT`, `CONTRADICT`, `REFINE`, `SPLIT`, `COMPOSE`, `MERGE`, `DECLARE_OPEN`, `DECLARE_NON_CONCLUSION`, `ATTACH_EVIDENCE`, and `DECLARE_LOSS`.

A claim record contains a stable handle but never treats the handle as an immutable substance. It carries content, epistemic class, scope/context, supporting evidence spans or artifact references, author/agent, transaction time, optional valid/research time, confidence only when sourced, and edges such as `derived_from`, `supersedes`, `conflicts_with`, `depends_on`, `part_of`, and `composed_from`. The current state is a deterministic reduction of a pinned ledger frontier, not a mutable row that destroys predecessors.

Every transformation emits a **transformation receipt** containing input frontier and hashes, transformer identity/version, declared capabilities, assumptions, preservation contract, output hashes, dependency set, validation results, and field-level loss declarations. No view is authoritative merely because it is executable or convenient.

The proposal deliberately does not make Petri/Event/Causal/LTS models co-authoritative. They are optional derived materializations selected only when their declared capabilities satisfy a request. The first implementation slice should not implement those models; it should prove exact evidence round-trip, epistemic-state replay, correction/succession, loss receipts, and dependency invalidation.

The proposed planning boundary is:

`PLAN(QueryIntent, PreservationContract, OperationalConstraints; pinned_frontier) -> Plan | REVIEW_REQUIRED`

Current representation state and lifecycle state are read from the pinned ledger and materialization catalog, not supplied independently by a caller. Thus `M` and `L` remain real internal state but are rejected as independent external arguments. This removes stale or contradictory caller descriptions. A large situation fingerprint is also rejected unless tests show a field changes plan choice; query intent plus field-level preservation obligations should carry most semantic demand.

## PRIOR_ART_BASIS

The proposal composes established ideas rather than inventing a new theory:

- **Event sourcing / append-only logs** for reconstructing state from an immutable succession of operations.
- **Content-addressed storage and Merkle-DAG lineage** for exact identity, integrity, branching, and reproducible frontiers.
- **Bitemporal databases** for separating when a claim applies from when it was recorded or corrected.
- **W3C PROV-style provenance graphs** for entities, activities, agents, derivation, and attribution.
- **Truth-maintenance and justification systems** for tracking supports, contradictions, retractions, and dependent conclusions.
- **Datalog/relational materialized views** for deterministic derivation, dependency tracking, and incremental invalidation.
- **Schema evolution and event upcasting** for migrations that preserve old events and record transformation versions.
- **Three-way version-control merge and CRDT discipline**: use automatic convergence only for operations proven commutative/associative/idempotent; represent semantic conflicts explicitly otherwise.
- **CQRS/materialized-view architecture** for separating authoritative writes from query-specific projections.

Petri nets, event structures, causal orders, and LTS remain valid prior art for particular derived questions. This proposal narrows their authority rather than dismissing their utility.

## AUTHORITATIVE_REPRESENTATION

The authoritative unit is the pair `(evidence object store, epistemic operation ledger)` at a named content-addressed frontier. Neither the reduced “current state” nor any analytic model is authoritative alone.

Minimum authoritative invariants:

- evidence bytes and digest are immutable;
- operations are append-only and content-addressed;
- every semantic claim can cite zero or more evidence objects, with zero-support claims visibly marked as inference/open rather than source-supported;
- epistemic class changes occur through new operations, never in-place rewriting;
- lineage and scope/context are explicit;
- reductions are deterministic for a declared reducer version;
- loss declarations cannot be deleted by downstream projection;
- unknown and conflict states are representable without forced resolution.

## DERIVED_REPRESENTATIONS

- Current-state index by epistemic class, scope, and validity.
- Chronology and succession views.
- Provenance/justification graph.
- Dependency and invalidation graph.
- Search/full-text/vector indexes, each explicitly non-authoritative.
- Causal-order or event-structure views when causality/concurrency/conflict are supported by evidence or declared inference.
- Petri/Open/Reconfigurable Petri views for possible behaviour, resources, interfaces, or rule mutation when those semantics are explicitly modeled.
- LTS/reachability views for bounded transition questions.
- Metric/clock/spatial views only with explicit anchors.
- Object/persona/boundary materializations as scoped persistent-pattern views with composition lineage.

Each derived representation publishes a capability descriptor: accepted input semantics, queries supported, guarantees, known losses, complexity limits, incremental-update support, and reverse-conversion status.

## PRESERVATION_CONTRACT

Contracts are field- and relation-specific, not one label for an entire transformation. Allowed obligations are:

- `EXACT`: byte/value and relevant ordering/identity preserved; verified by digest or canonical comparison.
- `SEMANTIC`: declared equivalence relation preserved; equivalence checker named.
- `ANCHORED`: reconstruction is tied to retained exact anchors.
- `STATISTICAL`: distributional property only; method, error bounds, and seed/data revision recorded.
- `VIEW_DEPENDENT`: meaning holds only under named scope/query/view assumptions.
- `NON_RECOVERABLE`: information is intentionally discarded and cannot be synthesized back.
- `UNKNOWN`: guarantee is not established; planner must not silently weaken it.

Mandatory exact items for the initial architecture are source bytes/digests, operation content/order constraints, epistemic labels as recorded, evidence links, provenance, scope, lineage, explicit corrections/retractions, conflict/open/non-conclusion markers, transformation receipts, and prior loss declarations.

## LOSS_AND_NON_RECOVERABLE

Formal extraction from natural language cannot guarantee complete semantic capture; omitted nuance remains recoverable only because exact source evidence is retained, not because the formal claim graph can reconstruct it. A causal-order view loses transformation labels, resources, alternatives, and metric information unless separately anchored. Reachability graphs can lose concurrency and compact rule structure. Unfoldings can explode or require cutoffs. Petri synthesis from traces/LTS is generally non-unique and may introduce or omit structure. Vector/search indexes are approximate retrieval aids and cannot reconstruct exact claims. Automatic merge cannot resolve genuine semantic contradiction without policy or review.

Every such loss must appear in the receipt and propagate transitively. Reverse synthesis produces a new hypothesis/materialization, never restoration of discarded ground truth.

## TRANSFORMATION_PATHS

`Evidence -> extracted claim candidates -> reviewed/typed operations -> reduced epistemic state -> query-specific materialization -> answer with receipt`

Rules:

- Evidence-to-claim extraction always yields candidate/inference status until supported classification is explicitly justified.
- Each path is pinned to an input frontier and transformer version.
- Composition joins ledgers by content identity plus explicit correspondence/interface operations; it does not conflate equal text or handles automatically.
- Projection requires a contract and returns both materialization and receipt.
- Reverse transformation is allowed only with a declared inverse grade and must retain the forward receipt.
- Any path encountering an unmet `EXACT` or `UNKNOWN` obligation returns `REVIEW_REQUIRED` rather than choosing a “closest” model.

## LIFECYCLE_BEHAVIOR

- **Create**: ingest evidence, verify digest, append initial classification/claim operations.
- **Operate/accumulate**: append operations; incrementally update only materializations whose dependency predicates match.
- **Mutate/correct**: append `SUPERSEDE`, `RETRACT`, or `REFINE`; preserve predecessor and justification.
- **Compose**: union content-addressed histories, then add explicit interface/correspondence and composition operations.
- **Split/diverge**: create frontiers sharing ancestry; no data copy is logically required.
- **Merge**: perform three-way operation/claim merge. Auto-merge only proven-safe operations; emit first-class conflict records otherwise.
- **Migrate**: retain original operations, apply versioned upcasters/reducers, and emit migration receipts with round-trip or invariant checks.
- **Degraded operation**: allow exact evidence append where safe; mark unavailable classifiers/materializers and forbid guarantees they would supply.
- **Recover**: verify object hashes, replay operations with the recorded reducer version, rebuild disposable views, and compare state/materialization digests.
- **Reverse/rollback**: append compensating operations or select an earlier frontier; never erase history.
- **Successor/retire**: create a successor frontier/schema with ancestry and migration contract; freeze retired reducers/artifacts needed for replay.

## ROUTING_POSITION

`R(S,M,L)` is a useful checklist but is likely malformed as a public function and premature as a fixed research decomposition.

Reasons:

1. `M` and `L` are not independent facts; both are projections of ledger history and deployed materialization state. Caller-supplied copies can disagree with the pinned revision.
2. `S` risks becoming an unbounded description of the world and can encode model names indirectly, creating circular routing.
3. Target-model selection is subordinate to preservation feasibility. A model with the right “situation” label is invalid if it cannot meet a field-level contract.
4. Many requests need no model-family route: ledger queries and ordinary derived indexes may suffice.
5. A fixed target model set encourages architecture before evidence that the query workload requires it.

Keep `S/M/L` as explanatory dimensions inside plan traces and evaluation, but implement a constraint/capability planner whose external inputs are query intent, preservation contract, operational constraints, and an exact frontier. If no registered materializer proves the obligations, return `REVIEW_REQUIRED`.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY**: current state is a reducible frontier; corrections and succession are explicit operations, not identity-preserving overwrite.
- **NON-SUBSTANTIALITY / DERIVED ENTITY**: handles are operational references; object/persona/boundary records are materialized patterns with scope and lineage, not primitive substances.
- **COMPOSITION / EMERGENCE**: local evidence and operations can compose into higher-scale views while retaining `composed_from` lineage and without asserting complete reducibility.
- **CONDITIONAL RELATIONALITY**: claims, identity, and behaviour are scoped; incompatible or causally incomparable relations are not forced into a single global order.

Alignment is reviewable design fit, not proof of the worldview or scientific validation.

## EXPECTED_FAILURE_MODES

- Claim extraction creates a false sense that natural-language meaning is fully formalized.
- The ledger schema becomes an overgrown universal ontology.
- Append-only history grows without bounded compaction and replay checkpoints.
- Transformation receipts are present but too vague to test.
- Dependency declarations are incomplete, producing stale derived views.
- Content hashes are mistaken for semantic equality.
- Conflict volume overwhelms human review during composition/merge.
- Planner capability declarations are optimistic or incomparable.
- Bitemporal and scope semantics become too complex for authors.
- A single ledger service becomes an operational bottleneck or governance centralization point.
- Derived behaviour models are generated from insufficient semantics and then treated as predictive truth.
- Reducer/schema migration breaks deterministic replay.

## FALSIFICATION_TESTS

Reject or materially revise this proposal if any of the following holds:

1. A representative corpus cannot reconstruct baseline epistemic classes, corrections, open questions, and non-conclusions from ledger replay without hidden out-of-band rules.
2. Two independent reducers produce different state for the same frontier and declared version.
3. A model-family-first architecture answers the same benchmark queries with equal preservation and materially lower complexity/cost across lifecycle scenarios.
4. Explicit `S`, `M`, or `L` adds routing accuracy on held-out cases beyond query + preservation + operational constraints, after accounting for features derivable from the ledger.
5. Dependency-based invalidation repeatedly misses affected views or approaches global invalidation under ordinary local changes.
6. Three-way semantic merge loses provenance, silently resolves conflict, or cannot represent divergence without copying/relabeling history.
7. Evidence retention does not permit reviewers to detect extraction loss in practice.
8. Receipt propagation permits a downstream representation to claim a stronger guarantee than its weakest required input.
9. Schema evolution cannot replay old operations or requires rewriting authoritative history.
10. The smallest useful implementation still requires most Petri/Event/LTS semantics in the authoritative layer, falsifying the “derived-only” claim.

## IMPLEMENTATION_TEST_PLAN

Research-only proposed sequence; no implementation is performed in this run.

1. Define a minimal operation/event schema, evidence object schema, preservation-contract schema, capability descriptor, and transformation receipt.
2. Encode a fixture corpus containing sourced facts, Owner direction, working hypotheses, open questions, non-conclusions, correction, contradiction, refinement, scope change, and unsupported inference.
3. Test exact evidence byte/digest round-trip and deterministic ledger replay at pinned frontiers.
4. Test branch/split/diverge/three-way merge, including conflicts that must not auto-resolve.
5. Test bitemporal correction: prior-revision reconstruction must remain exact while current state reflects succession.
6. Build only simple current-state, provenance, chronology, and dependency views; measure incremental invalidation radius.
7. Inject transformer loss and verify receipt transitivity and planner refusal when `EXACT` is required.
8. Register mock materializers with declared capabilities; compare constraint planning against `R(S,M,L)` on T1–T10 plus adversarial unknown/mixed-semantics cases.
9. Add one real causal/event view and one behaviour/reachability view only after the ledger tests pass; measure whether they deliver query value beyond ordinary indexes.
10. Exercise migration, reducer versioning, damaged-index recovery, unavailable-service degraded mode, and successor retirement.
11. Blindly score reconstructed state for source/hypothesis/open/non-conclusion fidelity and hallucinated commitment count.
12. Record compute, semantic, maintenance, and reversibility costs separately; do not collapse them into an unsupported scalar score.

## OPEN_UNKNOWNS

- Minimum claim/operation vocabulary without creating a universal ontology.
- Whether valid-time semantics are meaningful for all research claims or must be optional/scoped.
- Who may assign or change epistemic class and under what authority model.
- How evidence spans remain stable across source-format migration.
- How to express semantic equivalence checkers for each domain.
- Which merge operations are safe to automate and whether any CRDT subset is worthwhile.
- How much ledger history may be checkpointed or compacted without weakening audit/replay.
- Whether content-addressed evidence is legally/operationally retainable in every deployment.
- Which query workloads justify Petri/Event/Causal/LTS materializations.
- Whether planner capability descriptors can be verified rather than trusted.
- Acceptance thresholds for cumulative drift, invalidation radius, replay time, and human review burden.

## WHY_THIS_COULD_BE_WRONG

The evidence-and-claim ledger may solve auditability while underspecifying the deeper model problem. Natural-language claims might be too weak to support meaningful simulation, causality, or composition; pushing all formal semantics into views could merely postpone essential modeling decisions. The “single authoritative envelope” may also be semantic wordplay because evidence bytes and typed operations have different authority. A carefully designed complementary model family could encode behaviour and occurrence more faithfully, with less receipt bureaucracy. Finally, `R(S,M,L)` may outperform the proposed planner because lifecycle intent is not always derivable from current history and because human callers can supply future context that no ledger contains. Those are empirical questions, so the proposal should survive only if the falsification tests distinguish it from the current direction.
