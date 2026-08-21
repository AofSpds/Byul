# Phase 1 Frozen Proposal — v0.1.12

ROUND_SLOT = R10
PROFILE = LIFECYCLE_COMPOSITION
EXACT_RESEARCH_BASELINE = 891e4bd4b999eacc99431ed0db05062901a68dd9
PHASE1_IMPLEMENTATION_READ = FALSE
STATUS = INDEPENDENT_RESEARCH_PROPOSAL / NON_NORMATIVE / NOT_VALIDATED

## CURRENT_STATE_RECONSTRUCTION

Byul is an independent research track whose active question is not merely which graph formalism to select. It is how evolving research memory can retain exact sources, epistemic distinctions, lineage, uncertainty, and non-conclusions while supporting reconstruction, transformation, situation-specific views, and long model lifecycles. The baseline records an Owner-adopted but scientifically unvalidated BYUL CORE-A: change/mutability, non-substantiality/derived entity, composition/emergence, and conditional relationality. It explicitly keeps the primitive, canonical representation, model-family choice, routing schema, and preservation semantics open.

The current direction separates raw research memory from derived current/history/open/model-family/lifecycle views, explores a complementary Petri/Occurrence/Event/Causal/LTS family, and proposes `R(S,M,L)`. The strongest routing sub-hypothesis is that Preservation Demand may matter more than a surface phenomenon label. Lifecycle evaluation must cover mutation, composition, split/divergence, merge, migration, degradation, recovery, succession, retirement, cumulative semantic drift, invalidation, and reversibility. Initial-state reconstruction quality is itself a required performance dimension.

The research state contains an important correction: no canonical `P-series` exists in the available record. BYUL CORE-A is a research review layer, not a formal proof oracle and not an automatic PASS mechanism. The baseline states that a v0.1 experimental implementation exists, but Phase 1 has not inspected that implementation and makes no conclusion about its contents.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

- Byul and its active structures are working, non-normative, and unvalidated; production is not authorized.
- BYUL CORE-A is Owner-adopted within Byul research but is neither an AAA canonical requirement nor scientifically validated.
- Exact source/provenance, classification of fact versus hypothesis/open/non-conclusion, lineage, reconstruction reliability, and lifecycle behavior are explicit research concerns.
- Current formalism candidates have complementary intended roles: possible behavior/rules, actual occurrences, causality/concurrency/conflict, and purpose-specific reachability or causal views.
- `R(S,M,L)` and the Situation Fingerprint are candidates. Preservation Demand is a strong candidate axis, not a settled schema.
- The lifecycle target includes create, operate, accumulate, adapt, mutate, compose, split, diverge, merge, migrate, degrade, recover, succeed, and retire.
- Exact, anchored, semantic, statistical, view-dependent, approximate, and non-recoverable reconstruction/loss distinctions appear in the baseline, but their final taxonomy and acceptance thresholds remain open.

### OWNER_DIRECTION

- Preserve the possibility that apparently stable objects, identities, and boundaries are derived persistent patterns rather than primitive substances.
- Prefer succession/history over unqualified same-as identity, and do not impose an absolute global order on causally incomparable events.
- Keep local-to-composed-to-higher-scale lineage available where possible.
- Test lifecycle and transformation costs empirically; solicit scenarios that break models and routing assumptions.
- Maintain PRIOR-ART-FIRST, solution non-locking, uncertainty discipline, and separation of Owner recognition from scientific PASS.

### WORKING_HYPOTHESIS

- Raw source plus provenance can serve as an authority while query-oriented structures remain derived.
- A complementary representation family may outperform one universal model.
- Preservation Demand may be the most important routing feature.
- Event/occurrence histories and possible-behavior models may require separate but linked planes.
- Exact inverses are often unavailable; reverse synthesis may be non-unique and must be loss-classified.

### OPEN

- The minimal primitive or algebra: event, local mapping, interaction, composition, rewrite, typed morphism, or something else.
- Whether one canonical representation, multiple authorities, or an authoritative envelope with multiple internal object types is best.
- The minimal sufficient routing features and whether `R(S,M,L)` has the right argument boundary.
- Executable semantics for principle preservation, semantic equivalence, cumulative drift, and acceptance thresholds.
- Claim granularity, identity through succession, merge authority, scale limits, and the role of valid time for research assertions.
- Whether the proposed Petri/Event/Causal/LTS family is sufficient or useful for research-memory authority rather than simulation views.

### NON_CONCLUSION

- Petri Net, Causal Set, Event Structure, LTS, rewrite systems, or any other named formalism is not canonical.
- One universal model and one canonical representation have not been selected.
- Discarded transformation semantics are not automatically recoverable.
- A causal link is not thereby a local transformation, and a derived reconstruction is not ground truth.
- Global absolute NOW, physical discreteness, a minimum physical unit, and any physics/philosophy equivalence are not established.
- No canonical `P-series` or automatic principle PASS exists.

### YOUR_INFERENCE

- The immediate data problem is primarily an epistemic/provenance/lifecycle problem. Petri/Event/Causal/LTS structures are better treated as derived analysis or simulation views unless a preservation test proves otherwise.
- Preservation Contract must be an input to planning, not only an output of `R(S,M,L)`; otherwise the router can choose a lossy path before knowing what loss is forbidden.
- Lifecycle must be represented as explicit operations with preconditions and postconditions, not merely a context label.
- A commit DAG can preserve partial order, divergence, and succession without imposing a global total order; wall-clock fields can remain metadata with uncertainty.
- General semantic conflicts must remain explicit. CRDT convergence is safe only for substructures whose join or commuting-operation semantics are proven; it must not silently resolve meaning.

## MINIMAL_PROBLEM_DEFINITION

Given exact source artifacts and a stream/DAG of research changes, maintain a reconstructable sequence of scoped research states such that:

1. original bytes, provenance, epistemic status, uncertainty, non-conclusions, and succession relations are not silently overwritten;
2. every derived representation declares its inputs, transformer, fidelity/loss, and invalidation dependencies;
3. branch, composition, split, merge, migration, and recovery are explicit and auditable;
4. queries and lifecycle operations are planned only through transformations permitted by a caller-supplied preservation contract;
5. unknown or unproved preservation fails to review rather than fabricating equivalence; and
6. no implementation representation is promoted into an ontological claim about reality.

This definition intentionally does not require a complete world model, one universal formalism, or automatic semantic conflict resolution.

## PHASE1_PROPOSAL

Adopt a **provenance-backed, event-sourced research ledger with content-addressed snapshots** as the authoritative envelope. It is an implementable composition of established patterns, not a novel physical or philosophical theory.

### 1. Immutable content objects

Store exact source bytes as content-addressed blobs. Store each structured assertion as an immutable version object containing at least:

- stable logical handle distinct from immutable version digest;
- assertion kind: `SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, or `INFERENCE`;
- payload and explicit scope/context;
- exact source-span anchors or an explicit `NO_SOURCE_ANCHOR` reason;
- agent/authority and recorded-at time;
- asserted valid/effective time only when supplied, including precision/unknown state;
- schema identifier, confidence/uncertainty without invented precision, and integrity digest;
- relations such as `supersedes`, `refines`, `contradicts`, `supports`, `derived_from`, `composed_from`, and `same_handle_as`, each typed rather than inferred from adjacency.

Content digests identify versions, not semantic identity or truth. A stable handle is an operational continuity device, not an assertion of substance.

### 2. Immutable transition objects and commit DAG

Every change is an append-only transition object: ingest, classify, propose, correct, retract, supersede, compose, split, merge, migrate, invalidate, recover, or retire. A transition names parent commit(s), input/output object digests, actor, schema/reducer versions, preservation contract, and a transformation receipt. A commit object points to an explicit state manifest and one or more parent commits.

The explicit manifest is the normative state at that commit. Replay of transitions is a verification/reconstruction path, not the sole definition of state; this prevents a later reducer version from silently changing old states. Checkpoints may accelerate replay but must match the committed manifest digest.

### 3. First-class conflict and uncertainty

Correction never deletes history. It appends a successor and a typed relation. Divergent versions are not collapsed by last-write-wins. A merge that cannot prove a deterministic semantic join emits a conflict object containing both alternatives, common ancestor, affected contracts, and required resolver authority. `OPEN`, `UNKNOWN`, and `NON_CONCLUSION` remain values that survive materialization and merge.

### 4. Derived, disposable representations

Build query-specific projections from a pinned ledger commit:

- current-state, chronology, open-question, and core-principle views;
- PROV-compatible provenance/derivation graph;
- causal/occurrence/concurrency graph where source relations justify it;
- full-text, structured-field, embedding, or summary indexes;
- optional Petri/Open Petri/Reconfigurable Petri, Event Structure, Causal, LTS, rewrite, metric, or simulation views;
- lifecycle dependency/invalidation index.

Each view carries source commit, transformer digest/version, preservation profile, dependency set, build time, and stale/valid state. A view may be discarded and rebuilt. No view becomes authoritative merely because it is executable, compact, or convenient.

### 5. Preservation-aware planner

Replace the core decision boundary with:

`Plan(Q, O, P, B, I) -> {view set, transformations, guards, validation, fallback}`

- `Q`: question/workload and observed situation features;
- `O`: explicit lifecycle operation with pre/postconditions;
- `P`: field/relation-level Preservation Contract;
- `B`: compute, storage, latency, maintenance, and review budget;
- `I`: available authoritative commit, views, schemas, lineage, freshness, and known losses.

`R(S,M,L)` can remain a compatibility wrapper where `S` maps mainly to `Q+B`, `M` to `I`, and `L` to `O`. It should not remain the authoritative interface because its current form hides Preservation Demand inside `S` and returns a contract after planning.

### 6. Transformation receipts

Every transformation returns a machine-readable receipt:

`{input digests, output digests, transformer/schema version, declared fidelity by field/relation, omitted information, non-recoverable set, dependencies, checks executed, failures, reviewer status}`.

The planner composes receipts along a path and rejects a path when cumulative fidelity is weaker than `P`, when a required field is unclassified, or when a stale dependency is touched. `UNKNOWN` yields `REVIEW_REQUIRED`; it is never upgraded to semantic or exact preservation by default.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) supplies established entity/activity/agent, derivation, bundle, and provenance-of-provenance concepts. The proposal specializes these for research claims but does not assume provenance establishes truth.
- [Martin Fowler's Event Sourcing pattern](https://martinfowler.com/eaaDev/EventSourcing.html) grounds append-only state changes, rebuild, temporal queries, and alternative histories. The proposal strengthens it with explicit manifests and pinned reducer/schema versions because replay alone is insufficient when transformation code evolves.
- [Git's documented object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects.html) grounds content-addressed blobs, trees, commits, and parent-linked history as a practical physical substrate for immutable snapshots and branching.
- [W3C PROV constraints/semantics family](https://www.w3.org/TR/prov-overview/) supports validating provenance structure while retaining domain-specific extensions.
- [Jensen and Snodgrass on bitemporal intervals](https://www2.cs.arizona.edu/~rts/pubs/TRmerged.pdf) grounds the distinction between when a claim applies and when it is recorded/believed. The proposal permits unknown/indeterminate valid time and does not force all claims into a false clock.
- [Shapiro, Preguica, Baquero, and Zawirski on CRDTs](https://pages.lip6.fr/Marc.Shapiro/papers/CRDTs_SSS-2011.pdf) grounds convergence only where semilattice joins or commuting operations are defined. This is used narrowly for mechanically joinable metadata, not as a semantic-merge oracle.
- [Foster et al. on bidirectional tree transformations/lenses](https://www.cis.upenn.edu/~bcpierce/papers/newlenses-popl.pdf) grounds law-checked get/put transformations. The proposal allows putback only where laws and preservation contracts can be tested; otherwise view edits become new proposals against the ledger.

No cited prior art alone answers Byul's epistemic classification or BYUL CORE-A alignment. The architecture is a conservative combination of their established mechanisms.

## AUTHORITATIVE_REPRESENTATION

The authority is one **Research Ledger Envelope** with four immutable domain object types:

1. exact content blobs;
2. versioned assertion/relationship objects;
3. transition/receipt objects;
4. commit/state-manifest objects.

These are jointly authoritative because content without classification loses research meaning, classification without sources loses evidence, transitions without manifests risk replay drift, and manifests without transitions lose succession and explanation. This is not an uncontrolled multi-authority design: one commit digest names the exact closed state envelope.

Git may provide the prototype's physical content-addressed store and branch transport. Domain semantics must remain explicit in ledger objects rather than being inferred from filenames, commit messages, or Git topology.

## DERIVED_REPRESENTATIONS

Derived representations are selected by capability, not prestige:

- relational/current-state projection for status queries;
- provenance DAG for source, agent, activity, and derivation queries;
- causal/occurrence view only for justified order relations;
- argument/evidence adjacency view without collapsing epistemic class;
- Petri or process view for possible behavior, resource, concurrency, and composition simulation;
- Event Structure view for justified causality/concurrency/conflict analysis;
- LTS/reachability view for state-space questions;
- full-text and embedding indexes for retrieval, with exact source pointers;
- summaries for human handoff, marked lossy;
- metric/clock anchors as a separate view where exact values have external support;
- dependency/invalidation index for incremental rebuild and lifecycle cost.

Multiple views may coexist. A route may choose none and answer from the authoritative ledger when projection cost or loss is unjustified.

## PRESERVATION_CONTRACT

The contract is field- and relation-specific. Minimum fidelity values are:

- `BYTE_EXACT`: original serialized bytes and digest;
- `STRUCTURE_EXACT`: canonical fields/relations and multiplicity preserved;
- `SEMANTIC`: declared equivalence relation plus evidence/test oracle;
- `ANCHORED`: reconstruction constrained by retained exact anchors;
- `APPROXIMATE` or `STATISTICAL`: metric and error/tolerance declared;
- `VIEW_DEPENDENT`: valid only under named context and query;
- `DROP_ALLOWED`: explicit authorization to omit;
- `NON_RECOVERABLE`: omitted and impossible to reconstruct from this output;
- `UNKNOWN`: preservation not established.

Default contract for authority-changing operations requires byte-exact source blobs; structure-exact provenance, epistemic class, uncertainty, scope, authority, typed succession/conflict relations, commit parents, schema/version identifiers, and receipts. Unknown fields cannot be silently dropped. BYUL CORE-A alignment is a named review with evidence and possible `CONFLICT/UNKNOWN`; it cannot automatically return scientific truth.

## LOSS_AND_NON_RECOVERABLE

Always non-recoverable unless separately captured:

- unstated Owner intent, conversational context outside recorded artifacts, and external source state that was never archived;
- transformation semantics, labels, ordering, or conflict relations omitted before ingestion;
- exact source wording from embeddings, clusters, Petri/LTS/event projections, or summaries;
- a unique rule/behavior model synthesized from occurrence traces when alternatives fit the same observations;
- truth from provenance or integrity hashes;
- semantic identity from equal content digests;
- a single correct merge from genuinely contradictory branches without authorized judgment.

Normalization may also destroy whitespace, ordering, precision, and source spans. It is allowed only when the exact blob remains linked and the output receipt names the loss.

## TRANSFORMATION_PATHS

1. `exact source blob -> anchored assertion candidates -> reviewed assertion versions -> ledger commit`.
2. `ledger commit -> declared one-way projection -> indexed/materialized view`.
3. `view edit -> lens putback` only if totality/laws and contract checks pass; otherwise `view edit -> proposed transition -> review -> new ledger commit`.
4. `schema N commit -> migrator N_to_N+1 -> candidate commit + receipt -> dual reconstruction/differential tests -> promotion or rejection`.
5. `commit -> snapshot export -> import under pinned schema/reducer -> manifest and semantic invariant comparison`.
6. `branch heads + common ancestor -> mechanical safe joins -> explicit conflict objects -> authorized resolutions -> merge commit`.
7. `ledger commit -> optional behavior/causal/event/LTS view -> simulation result`; simulation results return as derived evidence, never as automatic Owner Acceptance.

Reverse paths must be classified. Checkout/recovery to an old commit can be exact; inverse projection is commonly non-unique; compensation appends a new transition rather than rewriting history.

## LIFECYCLE_BEHAVIOR

- **Create/ingest:** preserve exact artifact, source anchor, actor, schema, and uncertainty before deriving structure.
- **Operate/accumulate:** append transitions; materialize views incrementally from dependency sets; checkpoint explicit manifests.
- **Mutate/correct:** create a successor version plus typed relation; retain predecessor and downstream invalidation receipt.
- **Compose:** import namespaced ledgers by digest, declare interface/identity mappings, and create a composition commit. Equal labels never imply equal identity.
- **Split:** create child heads from a common commit with explicit selection manifests. Shared history remains referenced, not copied and rewritten.
- **Diverge:** allow independent transitions; causal parentage represents partial order without invented simultaneity.
- **Merge:** perform a three-way merge. Use CRDT joins only on proven joinable fields; preserve semantic disagreements as conflict objects until authorized resolution.
- **Migrate:** transform a pinned source commit with versioned code, receipt, old/new parallel validation, and rollback pointer. Never overwrite old objects.
- **Degrade:** mark unavailable blobs, stale views, failed validators, and reduced guarantees explicitly; planner may answer only within the weakened contract.
- **Recover:** fetch exact objects, verify digests and closure, reconstruct with pinned schema/reducer, and compare the explicit manifest and invariants.
- **Reverse/rollback:** move the active head or append compensation; history remains immutable. External side effects require separate idempotency/compensation records.
- **Successor/retire:** name the successor commit, migration receipt, unresolved conflicts, retained dependencies, and retention policy; retired views may be deleted only if reproducible and not authoritative.

Invalidation is dependency-driven: changing object `x` invalidates exactly views whose recorded input closure contains `x`, plus downstream views. Any broader fallback must be declared and measured.

## ROUTING_POSITION

`R(S,M,L)` captures useful intuitions but is malformed as the authoritative planner interface.

- Preservation Demand is buried in `S` even though it is a hard constraint.
- `L` mixes many operations that require different preconditions, postconditions, and rollback behavior.
- Budget and review authority are absent.
- Returning a Preservation Contract after selecting a path is logically too late.

Use `Plan(Q,O,P,B,I)` as the normative form and retain `R(S,M,L)` only as an adapter for compatibility and hypothesis comparison. Routing is constrained query planning over declared representation capabilities and losses. It may choose several complementary views, the ledger alone, or `REVIEW_REQUIRED`.

## BYUL_CORE_A_ALIGNMENT

- **CHANGE / MUTABILITY:** no in-place metaphysical identity; immutable versions connect through explicit succession and mutation transitions.
- **NON-SUBSTANTIALITY / DERIVED ENTITY:** stable handles are operational references; objects/personas/boundaries can remain materialized views with lineage rather than primitive substances.
- **COMPOSITION / EMERGENCE:** composition commits, namespace/interface maps, and `composed_from` provenance retain local-to-higher-scale lineage without claiming complete reduction.
- **CONDITIONAL RELATIONALITY:** assertions carry scope/context; conflicting or incomparable branches can coexist; no global total order is forced.

Alignment is architectural compatibility, not proof of the worldview or model fitness.

## EXPECTED_FAILURE_MODES

- Missing events or source blobs make exact reconstruction impossible.
- A buggy or non-deterministic reducer disagrees with committed manifests.
- Schema evolution changes meanings while claiming a syntactic migration.
- Claim granularity is too coarse to preserve disagreement or too fine to remain usable.
- Content-addressed identity is mistaken for semantic identity or truth.
- Provenance/receipt volume and index maintenance exceed query benefit.
- Merge conflicts accumulate because semantic resolution is intentionally not automated.
- CRDT rules are applied to non-commuting semantic decisions.
- Putback from a lossy view corrupts authoritative data.
- External sources, tools, or side effects cannot be replayed.
- Dependency declarations are incomplete, causing stale derived views, or overbroad, causing invalidation explosions.
- Classification authority is unclear, allowing an inference to masquerade as source-supported.
- Security, privacy, or deletion duties conflict with immutable retention.
- Git-level integrity is mistaken for authorization, confidentiality, or durability.

## FALSIFICATION_TESTS

Reject or materially revise the proposal if any of these fail:

1. Two identical sentences with different source/context/classification remain distinct while sharing bytes if appropriate.
2. A retroactive correction reconstructs both the state believed then and the corrected current branch without rewriting history.
3. Split two branches, classify the same handle differently, and merge: neither meaning may disappear or win by timestamp.
4. Compose two ledgers with colliding local IDs: namespaces and interface mappings prevent accidental identity collapse.
5. Migrate schema N to N+1, reconstruct with pinned versions, and detect any undeclared field/relation loss.
6. Edit a lossy summary or embedding view: the system refuses direct putback and emits a proposed transition.
7. Remove a source blob during recovery: closure verification fails rather than returning a falsely complete state.
8. Change a reducer implementation: old commit manifest comparison detects replay drift.
9. Inject incomparable events with uncertain times: reconstruction preserves partial order and does not invent a global sequence.
10. Apply merge in both orders on a CRDT-approved metadata field: convergence, associativity, commutativity, and idempotence hold; the same test must reject semantic claim resolution lacking such laws.
11. Mutate one assertion: the measured invalidation set equals the declared dependency closure and unaffected views remain valid.
12. Route a query whose contract forbids known projection loss: the planner chooses a safe alternative or `REVIEW_REQUIRED`.
13. Repeated transform/rebuild cycles do not accumulate undeclared semantic drift over a lifecycle corpus.
14. A fresh instance reconstructs facts, Owner directions, hypotheses, opens, non-conclusions, and inferences without hallucinated commitment.

## IMPLEMENTATION_TEST_PLAN

No implementation is authorized in this run. A later explicit trial should proceed in gates:

1. Define versioned JSON schemas for blobs, assertions, transitions, receipts, manifests, conflicts, and contracts; use deterministic canonical encoding and SHA-256.
2. Use one file per immutable object under a Git-backed prototype; maintain a disposable SQLite/search index keyed by commit and transformer version.
3. Implement pure validators and deterministic materializers before any router optimization.
4. Build fixtures from the exact v0.01 research memory with hand-audited source spans and classifications.
5. Add property-based lifecycle sequences covering create/mutate/compose/split/diverge/merge/migrate/degrade/recover/succeed/retire.
6. Execute T1-T10 behavior scenarios only through derived adapters and compare their receipts against authoritative data.
7. Add golden snapshot closure, replay-versus-manifest, migration differential, round-trip, cumulative-drift, and bounded-invalidation tests.
8. Add adversarial tests for missing events, hash collision simulation, unknown fields, stale indexes, non-deterministic transformers, malicious provenance, ID collision, and invalid CRDT use.
9. Measure storage amplification, replay time, materialization time, merge-review load, invalidation radius, query latency, and human classification cost.
10. Require independent Owner + ASA review; tests do not grant Owner Acceptance or implementation authority.

## OPEN_UNKNOWNS

- What is the smallest useful assertion granularity and relation vocabulary?
- Which BYUL CORE-A checks, if any, can be operationalized without turning research principles into false axioms?
- What evidence establishes `SEMANTIC` preservation for natural-language claims?
- When does research-time/valid-time apply, and how should indeterminate time be represented?
- Who may resolve conflicts, reclassify assertions, authorize loss, or retire authority objects?
- Which metadata fields genuinely form safe CRDTs, and is concurrent offline editing actually required?
- How much domain semantics belongs in PROV specialization versus a separate claim schema?
- Can dependency declarations remain complete and bounded at realistic scale?
- Is the additional ledger ceremony justified compared with disciplined Markdown plus Git?
- What retention, privacy, deletion, signature, access-control, and external-archive requirements apply?
- Which derived formalism family yields measurable value beyond searchable provenance and snapshots?
- How should stable handles survive split, composition, and successor creation without implying substance?

## WHY_THIS_COULD_BE_WRONG

The architecture may over-engineer a small, human-curated research repository. Git plus disciplined Markdown may already provide adequate versioning, while a typed ledger introduces classification labor, schema governance, duplicated metadata, and false precision. Natural-language semantic equivalence and conflict resolution remain human problems, so transformation receipts can document uncertainty without eliminating it. Event sourcing can be brittle when events, reducers, or external dependencies evolve. An authoritative envelope with four object types may be more complex than a carefully designed single document graph. Finally, the present Petri/Event/Causal/LTS family might prove sufficient if the real requirement is simulation rather than epistemic memory, or a future prior-art comparison may identify a simpler established research-knowledge system with stronger tooling.

For those reasons this proposal should first compete on reconstruction fidelity and full lifecycle cost, not be adopted because its audit story is attractive.
