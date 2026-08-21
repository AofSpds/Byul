# Phase 1 Frozen Proposal — v0.1.04

ROUND_SLOT = `R03`

PROFILE = `NEUTRAL_BLIND`

PHASE1_RESEARCH_BASELINE_COMMIT = `891e4bd4b999eacc99431ed0db05062901a68dd9`

BLIND_INPUT_CONTROL = `Only the packet-specified v0.01 files were read through exact Git-object reads from the pinned baseline. No current v0.1 implementation, recovery output, reservation branch content, or earlier proposal output was inspected.`

IMPLEMENTATION_PERFORMED = `FALSE`

IMPLEMENTATION_AUTHORITY = `NONE`

## CURRENT_STATE_RECONSTRUCTION

Byul is a non-normative research track whose active question is not which single formalism is universally correct, but how changing research memory and model state can preserve source meaning, epistemic status, lineage, and explicitly permitted loss while supporting purpose-specific reconstruction and lifecycle change. BYUL CORE-A currently asks implementations to avoid treating state, identity, object, or boundary as permanently fixed; to retain succession and lineage; to permit composition and emergence; and to keep meaning conditional on relations and context. These are Owner-adopted research principles, not validated physical or philosophical axioms.

The source memory distinguishes a high-resolution Owner worldview hypothesis (a composition network of local mappings/processes) from implementation abstractions. Candidate Petri, occurrence, event-structure, causal-order, LTS, and rewrite formalisms remain non-canonical. The strongest existing routing hypothesis is `R(S,M,L)`, with Preservation Demand likely more important than a phenomenon label. Exact metric reconstruction, the primitive/minimal algebra, representation authority boundaries, transformation reversibility, lifecycle drift, and the minimal sufficient routing fingerprint remain open.

The v0.01 baseline also records a correction: no canonical “P-series” exists in the available evidence. Any principle gate must therefore refer to BYUL CORE-A and explicit preservation constraints, must not invent missing P-series semantics, and must not automatically return scientific or Owner acceptance.

## STATE_CLASSIFICATION

| Class | Reconstructed state |
|---|---|
| `SOURCE_SUPPORTED` | The pinned memory explicitly records v0.01 as research/memory and v0.1+ as implementation; distinguishes raw research memo data from derived views; identifies provenance, history, open questions, lifecycle, reconstruction classes, and semantic-loss measurement as active concerns; and keeps candidate formalism families non-canonical. |
| `OWNER_DIRECTION` | Preserve evolving meanings; treat continuity as succession/lineage rather than necessary identity; explore local-to-composed structure; avoid privileging a global NOW; validate lifecycle and transformation costs; use prior art first; keep implementation freedom within the Owner-adopted Byul principles. |
| `WORKING_HYPOTHESIS` | A complementary model family may be preferable to one universal model; Preservation Demand may be the strongest routing feature; `R(S,M,L)` may organize routing; causal order can be a useful projection; Petri/Event/LTS-family representations may answer different questions. |
| `OPEN` | Minimal primitive/algebra; exact authority distribution; minimal routing inputs; lawful merge semantics; lifecycle acceptance thresholds; reconstruction reliability by semantic field; scale limits; exact metric anchoring; whether any candidate formalism is necessary. |
| `NON_CONCLUSION` | Petri is not canonical; Causal Set is not the final worldview or architecture; one canonical representation is not required; discarded semantics are not automatically reconstructable; Owner recognition is not scientific PASS; BYUL CORE-A is not a claim about physical truth. |
| `YOUR_INFERENCE` | The safest implementable center is a versioned epistemic provenance ledger with immutable source evidence, append-only semantic revisions, explicit transformation contracts, and rebuildable views. Formal models should be typed projections or executable hypotheses, not the universal authoritative store. |

## MINIMAL_PROBLEM_DEFINITION

Given changing source artifacts and interpretations, maintain enough information to answer four questions without silently upgrading or deleting meaning:

1. What exact evidence existed at a selected revision?
2. What claims, hypotheses, owner directions, unknowns, corrections, and non-conclusions were asserted from it, by whom, in which scope, and with what lineage?
3. Which transformation produced each representation, what did it preserve or discard, and can the required semantics be reconstructed?
4. Which available view or model satisfies a concrete query and lifecycle operation under an explicit preservation contract and cost budget?

Any architecture that cannot answer one of these questions must explicitly return `UNKNOWN`, `REVIEW_REQUIRED`, or `NON_RECOVERABLE`; it must not synthesize certainty.

## PHASE1_PROPOSAL

Adopt a **Versioned Epistemic Provenance Ledger (VEPL)** as the canonical write model, with authority distributed by information type rather than concentrated in one semantic graph.

### 1. Immutable evidence layer

Store each source artifact as immutable bytes plus media type, cryptographic digest, acquisition metadata, and stable source locator. A new or corrected source becomes a successor revision; it does not overwrite the predecessor. Exact byte/span anchors let claim records point back to the evidence that justified them.

### 2. Epistemic revision layer

Represent interpretations as immutable, typed revisions behind operational handles. A minimal claim revision contains:

- `claim_handle` and immutable `revision_id`;
- proposition payload or structured reference;
- classification: `SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, or explicitly marked `INFERENCE`;
- exact evidence spans or an explicit `NO_DIRECT_SOURCE` marker;
- scope/context and applicable schema version;
- author/agent and recorded time;
- predecessor/successor, correction, contradiction, support, challenge, and supersession relations;
- validity status without destructive deletion.

The handle is an operational continuity aid, not an ontological assertion that all revisions are the same substance. Negative meaning—“not concluded,” “retracted,” “unknown,” “comparison prohibited”—is first-class data.

### 3. Provenance activity layer

Every extraction, normalization, summary, merge, migration, simulation, and projection is an activity with immutable input/output revision IDs, actor/tool version, parameters, transformation version, preservation contract, validation evidence, and outcome. This is a constrained subset of W3C PROV concepts, strengthened with semantic preservation grades and executable validation hooks.

### 4. Commit and branch layer

Group operations in commits whose parents form a DAG. Snapshots are named commit cuts. Divergence is represented by different descendants of a shared ancestor. A merge is a new commit with all parents and explicit resolutions; unresolved semantic conflicts remain addressable records. Three-way structural merge may propose candidates, but epistemic conflicts are never auto-resolved solely because syntax merges cleanly.

### 5. Derived-view layer

Current-state documents, chronology, open-question lists, causal indexes, embeddings, search indexes, LTS/reachability graphs, event structures, Petri models, simulations, and dashboards are rebuildable materialized views. Each view declares the input cut, transformation version, query capabilities, staleness state, and per-semantic-dimension preservation grade. A view cannot become source authority merely by being convenient or computationally optimized.

### 6. Constraint-planning router

Replace model-name dispatch with a small constraint planner. The request supplies query intent, mandatory semantic dimensions, tolerated loss, lifecycle operation, freshness, and budget. The catalog supplies source/view capabilities and transformation contracts. The planner selects the lowest-cost valid path only if all mandatory dimensions meet their required grades and authority rules. Otherwise it returns `REVIEW_REQUIRED` with the unsatisfied constraints.

This architecture is implementable with ordinary content-addressed blob storage, an append-only relational/graph ledger, JSON Schema (or equivalent) for versioned record types, deterministic projection workers, and a validation/test registry. It does not require a new mathematical theory.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) supplies established Entity/Activity/Agent, derivation, attribution, and bundle concepts. VEPL narrows these to a validated profile and adds epistemic classification plus field-level preservation contracts; PROV by itself permits descriptions that still require constraint checking.
- [Event Sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) supplies append-only intent-bearing events, compensating corrections, replay, and separately materialized read models. VEPL applies it selectively to research-state changes and keeps immutable evidence blobs alongside events so a faulty extractor does not become the only surviving record.
- [Git’s object and commit model](https://git-scm.com/docs/user-manual) supplies content-named objects, tree snapshots, parented commits, branches, and explicit merge ancestry. VEPL adopts the history shape, not Git’s line-oriented merge as a semantic oracle.
- [Bidirectional transformation lenses](https://www.cis.upenn.edu/~bcpierce/papers/lenses.pdf) supply laws for relating a richer source to a simplified view and expose the difficulty of reconstructing information discarded by a projection. VEPL uses lens-style laws when a transformation truly supports update/round-trip behavior and marks other projections one-way.
- Materialized-view/CQRS practice supports query-specific rebuildable views, but VEPL rejects the assumption that eventual consistency or a cached view is acceptable when a request explicitly demands the exact current authoritative cut.

## AUTHORITATIVE_REPRESENTATION

The authoritative representation is the VEPL write model, but authority is **stratified**:

- source bytes and digests are authoritative for what the captured artifact contained;
- adopted claim revisions are authoritative for who classified or decided what, not for universal truth;
- transformation records are authoritative for declared derivation and measured validation evidence;
- commit ancestry is authoritative for succession, divergence, and merge history;
- derived views are never authoritative for meaning absent an explicit, reviewed promotion event.

This avoids both extremes: raw text alone is insufficient for reliable routing and evaluation, while a normalized graph alone can erase ambiguity, wording, and unmodeled meaning.

## DERIVED_REPRESENTATIONS

Initial derived representations should be few and demand-driven:

1. exact source browser with span-linked classifications;
2. reconstructed “current state” view parameterized by commit cut and policy;
3. chronology and lineage view;
4. open/unknown/non-conclusion safety view;
5. provenance and transformation-loss graph;
6. query-specific formal models (Petri/Event/LTS/causal/rewrite) only when their capability contracts match the request;
7. full-text/vector search indexes explicitly marked as retrieval aids, never evidence or truth;
8. lifecycle audit and invalidation view.

Each materialization key is `(input_commit, transformation_id, transformation_version, parameters, schema_version)`. The key and output digest make stale or mixed projections detectable.

## PRESERVATION_CONTRACT

Every transformation declares a matrix over semantic dimensions. Each cell is one of `EXACT`, `SEMANTIC`, `ANCHORED`, `APPROXIMATE`, `VIEW_DEPENDENT`, `DROPPED_NON_RECOVERABLE`, or `UNKNOWN`. Minimum dimensions include:

- source bytes, ordering, and exact spans;
- agent/authority and provenance;
- epistemic classification;
- uncertainty, negation, non-conclusion, correction, and conflict;
- scope/context and schema version;
- chronology versus causal order distinction;
- transformation labels and parameters;
- branch, succession, and merge lineage;
- rule/behavior alternatives versus observed occurrences;
- concurrency, conflict, resource, metric/time/space anchors where present.

Hard invariants:

- a derived assertion cannot silently become source-supported;
- `UNKNOWN` cannot become a positive preservation claim;
- a correction appends history and keeps the corrected record addressable;
- every derived object reaches its inputs through provenance;
- every accepted lossy path records the authorizing demand/tolerance;
- exact reconstruction claims require digest equality or a domain-specific equivalence oracle;
- views built from different input cuts cannot be mixed without an explicit composition activity;
- CORE-A review records interpretation and evidence but never produces scientific PASS automatically.

## LOSS_AND_NON_RECOVERABLE

The ledger must say plainly what it cannot recover:

- Summaries, embeddings, token indexes, and atomized claim graphs can lose wording, order, ambiguity, tone, omission, and cross-paragraph context. These are recoverable only because the immutable source artifact remains linked.
- Occurrence history cannot reconstruct unobserved possible behavior without a separately preserved rule model. A causal-order projection cannot reconstruct discarded transformation labels, conflict, resources, or metric anchors. LTS-to-Petri or similar reverse synthesis can be non-unique.
- Human intent that was never recorded is non-recoverable. A provenance edge records an assertion about derivation; it does not prove the assertion is correct.
- Destructive source deletion, missing encryption keys, unrecorded external edits, and conflict resolution that discards both alternatives are non-recoverable.
- Schema migrations without retained old bytes, executable transformer identity, and validation evidence cannot support exact historical replay.

## TRANSFORMATION_PATHS

Supported path classes:

- `INGEST`: external artifact → immutable blob + acquisition record;
- `ANNOTATE`: artifact/span → epistemic revision, with human or tool attribution;
- `CORRECT/RETRACT`: existing revision → compensating successor revision;
- `PROJECT`: ledger cut → materialized view with coverage matrix;
- `FORMALIZE`: selected claims/rules → purpose-specific executable or mathematical model, with explicit modeling assumptions;
- `COMPOSE`: multiple namespaces/cuts → composed cut through declared interface mappings;
- `MERGE`: common ancestor + branches → multi-parent commit plus retained conflicts/resolutions;
- `MIGRATE`: old schema/model → new version through a registered transformer, parallel validation, and fallback path;
- `EXPORT/IMPORT`: canonical bundle round trip with manifests and digest verification;
- `RECONSTRUCT`: log + blobs + transformation registry → selected historical/current views.

Reverse paths exist only when a registered inverse, lawful lens, or reviewed synthesis procedure says they do. “Can render a plausible source” is not the same as reconstruction.

## LIFECYCLE_BEHAVIOR

- **Create:** ingest evidence, assign immutable revision IDs, and commit only after schema and provenance validation.
- **Operate/accumulate:** append events and incrementally update disposable views; exact queries pin a commit cut.
- **Adapt/mutate:** add successor or compensating revisions; invalidate only views whose dependency closure intersects changed semantics.
- **Compose:** preserve original namespaces and cuts, add explicit interface/mapping records, and reject type or preservation-contract mismatches.
- **Split/diverge:** branch from a named commit; all descendants retain the shared ancestor and local policy/schema versions.
- **Merge:** use three-way ancestry for candidate structural changes; retain epistemic contradictions and unresolved classifications as first-class conflicts.
- **Migrate:** freeze an input cut, run a versioned transformer, compare preservation matrices and query results, then promote by a new commit; never rewrite the historical ledger.
- **Degraded/recover:** treat views as caches; rebuild them from verified blobs, commits, and activities. If a required transformer is unavailable, report a bounded recovery state rather than improvising.
- **Successor/retire:** point new handles/policies to a successor while preserving predecessor addressability, reasons, and rollback boundaries.

## ROUTING_POSITION

`R(S,M,L)` is useful as a conceptual reminder but should not be a fixed three-record ontology. `S`, `M`, and `L` overlap (for example, freshness, mutation, and reconstruction tolerance can describe both situation and lifecycle), and a maximal Situation Fingerprint risks reproducing the world before answering a query.

Implement routing instead as constrained path planning:

`PLAN(Request, AuthorityState, CapabilityCatalog) -> Path | REVIEW_REQUIRED`

`Request` contains query intent, required semantics, accepted grades, lifecycle operation, exact input cut/freshness, and operational budget. `AuthorityState` contains available authoritative types, schema/transform versions, lineage, invalidation, and conflicts. `CapabilityCatalog` contains registered views and transformations with contracts and costs.

The planner may expose `S/M/L` as a user-facing grouping, but the decision rule is: choose a path only when every mandatory preservation constraint is satisfied; minimize measured compute/maintenance cost second. No model name appears in the situation input. Unknown capability or loss fails closed.

## BYUL_CORE_A_ALIGNMENT

- **Change/mutability:** revisions and append-only corrections model state as succession rather than in-place identity.
- **Non-substantiality/derived entity:** handles, objects, and “current state” are operational views over revisions, not asserted primitive substances.
- **Composition/emergence:** source, claim, activity, and commit structures compose through explicit mappings while retaining lineage from local inputs to larger views.
- **Conditional relationality:** classifications and meanings carry scope/context; conflicts and causal incomparability are retained rather than forced into one global order.

Compatibility is architectural, not proof that CORE-A is true. A review can identify an implicit conflict but cannot issue scientific validation.

## EXPECTED_FAILURE_MODES

1. **Annotation distortion:** atomizing prose into claims can remove ambiguity or create a false boundary.
2. **False provenance confidence:** a detailed derivation graph may look evidentially stronger than its human/tool assertions warrant.
3. **Schema ossification:** early enums may encode the current research framing and obstruct later reframing.
4. **Event-log burden:** replay, upcasting, and long dependency closures may be expensive; bad events remain visible and need compensation.
5. **Conflict overload:** retaining unresolved semantic conflicts can make current-state views indecisive.
6. **Router circularity:** inaccurate capability contracts can make the planner confidently choose a lossy view.
7. **View explosion:** too many query-specific projections recreate multi-model maintenance costs.
8. **Merge limits:** ancestry helps locate divergence but cannot decide substantive truth or Owner intent.
9. **Privacy/deletion tension:** immutable evidence may conflict with legal or operational deletion requirements; cryptographic erasure also makes reconstruction impossible.
10. **Formalization mismatch:** converting narrative research into Petri/Event/LTS/rewrite structures may add assumptions not present in the evidence.

## FALSIFICATION_TESTS

Reject or materially simplify VEPL if any of these hold:

1. A baseline of versioned raw documents plus a small manifest matches VEPL on reconstruction, epistemic-status preservation, and lifecycle tasks at substantially lower maintenance cost.
2. Independent annotators cannot achieve acceptable agreement on claim boundaries/classification, and retaining disagreement does not improve downstream safety.
3. Property tests find a transformation labeled `EXACT` that fails byte/digest or declared semantic equality.
4. A deleted derived store cannot be rebuilt from pinned inputs and registered transformers.
5. Branch/merge scenarios lose a correction, non-conclusion, conflict, or common ancestor.
6. The router selects a path after any mandatory semantic dimension is `UNKNOWN` or below the requested grade.
7. Repeated migrations cause cumulative semantic delta above a predeclared threshold even though each single step passes.
8. Query/lifecycle benchmarks show that provenance and invalidation closures grow too quickly for the intended workload without unsafe pruning.
9. CORE-A reviewers find that operational handles or schemas are treated as fixed entities without explicit revision/succession semantics.

## IMPLEMENTATION_TEST_PLAN

No implementation is authorized or performed in this run. A separately authorized trial should:

1. Define minimal versioned schemas for artifact, claim revision, activity, relation, commit, preservation matrix, and materialized-view receipt.
2. Build only five write operations first: ingest, annotate, correct/retract, branch, and explicit merge; store raw blobs content-addressably and ledger records append-only.
3. Use the pinned Byul memory snapshot as a golden corpus while keeping exact artifact bytes; hand-label a small set of source-supported statements, hypotheses, open questions, corrections, and non-conclusions.
4. Implement three projections: exact source browser, current-state reconstruction, and open/non-conclusion safety view. Add formal-model projections only after a request demonstrates need.
5. Add property tests for immutable history, provenance reachability, deterministic replay, snapshot digest round trip, idempotent projection, invalidation closure, conflict retention, and authority non-escalation.
6. Run lifecycle scenarios for mutate, compose, split, divergent correction, merge, schema migration, transformer loss, cache deletion, rollback, and successor retirement.
7. Compare against the raw-documents-plus-manifest baseline on fidelity, reviewer effort, storage, replay time, update latency, invalidation radius, and query benefit.
8. Treat test success as engineering evidence only; Owner Acceptance and scientific validation remain separate.

## OPEN_UNKNOWNS

- Whether claim-level normalization provides enough benefit over span annotations to justify its interpretive risk.
- The minimal relation and epistemic-status vocabularies, and how they evolve without rewriting history.
- How to express semantic equivalence or preservation oracles for natural-language meaning.
- Whether ordering needs valid time, transaction time, causal partial order, or different combinations per record type.
- Who can promote an inference or owner-direction annotation, and how authority changes are represented.
- Safe pruning/compaction rules when storage or privacy requires forgetting.
- How much routing can be static contract checking versus learned empirical policy.
- Which formal projections, if any, repeatedly outperform generic provenance/temporal queries.
- Quantitative thresholds for cumulative drift, reviewer agreement, scale, and lifecycle acceptance.

## WHY_THIS_COULD_BE_WRONG

VEPL may be over-engineered for a research repository whose best representation remains carefully versioned prose. Claim decomposition can impose sharper semantics than the Owner intended, while a provenance graph records workflow but cannot guarantee truth. Git-shaped ancestry makes divergence visible but does not solve semantic merge. Event sourcing adds replay and schema-evolution obligations. A contract-based router may merely move unsupported judgment into hand-authored capability metadata. Finally, alignment with CORE-A is an interpretation of current research principles, not an empirical validation.

The proposal should therefore begin as a thin ledger around immutable prose, earn each structured field and view through falsification against the simpler baseline, and preserve a reversible exit path back to source artifacts.

