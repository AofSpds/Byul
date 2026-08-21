# BYUL v0.1 Parallel Proposal Round-1 — Phase 1 Frozen

- ROUND_ID: `BYUL-v0.1-PARALLEL-PROPOSAL-R1`
- ROUND_SLOT: `R02`
- RUN_ID: `v0.1.02`
- COHORT: `ROUND1_10_RUN`
- PROFILE: `NEUTRAL_BLIND`
- RESEARCH_BASELINE_COMMIT: `891e4bd4b999eacc99431ed0db05062901a68dd9`
- PHASE1_FROZEN: `TRUE`
- FROZEN_AT: `2026-08-22 04:12:30 +09:00`

## Isolation statement

This proposal was produced from the fourteen controller-listed research files at
the exact research baseline and from the prior-art sources listed below. Before
this freeze, it did not inspect the current `v0.1` README, contract, manifest,
source, or tests, and it did not inspect another run's proposal or return packet.

## 1. Current-state reconstruction and classification

### SOURCE_SUPPORTED

- Byul is an active, non-normative, unvalidated research track separate from the
  AAA mainline. Its implementation data is the accumulated Byul research memory,
  not an external toy domain.
- The current high-resolution worldview hypothesis is a network of many local
  mappings/processes whose compositions may appear at a higher scale as objects,
  selves, personas, protocols, or boundaries. This is a research hypothesis, not
  established physics or philosophy.
- `BYUL CORE-A` currently asks implementations to avoid silently assuming
  permanent immutability or primitive substances; to preserve possible
  composition/emergence lineage; and to retain conditional, relational, and
  causally incomparable states. It is owner-adopted within Byul research, is not
  an AAA canonical requirement, and has not been scientifically validated.
- The research currently considers complementary behaviour/rule,
  occurrence/concurrency, causal, reachability, metric, and reconstruction views.
  Petri/Open/Reconfigurable Petri, Occurrence Nets, Event Structures, causal-order
  views, and LTS are candidates rather than selected answers.
- The strongest routing candidate is `R(S,M,L)`, with preservation demand likely
  more important than a phenomenon label. Transformation quality must include
  semantic loss, reversibility, invalidation, lifecycle drift, and operational
  cost, not compute cost alone.
- `P-series` was an unsupported abstraction and was explicitly corrected. It
  must not be reconstructed as an existing canonical rule set.

### WORKING_HYPOTHESIS

- Causal order is useful as a skeleton/index, but does not retain local
  transformation semantics or guarantee metric/geometry reconstruction.
- Possible behaviour and actual occurrence history need not share one
  authoritative representation.
- A purpose-specific formalism family plus declared transformations is more
  plausible than one universal formalism, but this has not yet been established.
- Preservation demand may be a better routing discriminator than surface
  situation type.

### OWNER_DIRECTION

- Prior-art first; no novelty for novelty's sake.
- Keep fact, owner direction, working hypothesis, open question, non-conclusion,
  and inference distinct. Preserve `UNKNOWN` instead of inventing commitments.
- Treat succession/history as potentially more faithful than permanent identity.
- Evaluate mutation, composition, split/merge, migration, degraded recovery,
  successor/retirement, cumulative drift, and transformation cost with executable
  scenarios.
- Do not claim that Buddhism, quantum mechanics, Causal Set Theory, or a minimum
  physical unit proves the worldview.

### OPEN

- The primitive/minimal algebra, if any.
- Which meanings must be exact, semantic, anchored, statistical, view-dependent,
  or non-recoverable for each workload.
- The minimal sufficient routing input and whether `R(S,M,L)` is necessary or
  sufficient.
- Authority boundaries when multiple representations coexist.
- Safe merge semantics for competing research claims.
- Acceptance thresholds for drift, invalidation, reconstruction, scale, and
  reverse synthesis.

### NON_CONCLUSION

- No canonical Petri model, final Causal Set architecture, universal model,
  single canonical representation, event/mapping primitive, absolute global
  clock, or automatic recovery of discarded semantics has been established.
- A stable identifier, frozen snapshot, or immutable receipt is an operational
  anchor, not a claim of ontological permanence.

### YOUR_INFERENCE

- The minimal implementable problem is primarily an epistemic-state,
  provenance, and transformation-control problem. Selecting a world ontology is
  not required for a useful first architecture.
- Authority should be assigned per semantic field and artifact role. Exact source
  wording, explicit research classifications, authored behaviour rules, metric
  anchors, and derived summaries can have different authorities.
- Convergence of replicas or successful serialization is weaker than semantic
  correctness. Automatic merge must be limited to operations whose algebra is
  known; claim conflicts should remain explicit.

## 2. Minimal implementation problem

Given immutable source artifacts, a set of versioned assertion packets, a catalog
of representations, and a query or lifecycle operation, choose or construct an
answering representation only when a machine-checkable transformation path meets
the request's preservation contract. Every output must retain lineage to its
inputs, disclose losses and introduced interpretations, and refuse with
`UNKNOWN / REVIEW_REQUIRED` when preservation cannot be demonstrated.

For a demand contract `D`, current catalog `C`, lifecycle/operational context `O`,
and transformation registry `T`:

`Plan(D,C,O,T) -> {artifacts, path, guarantees, losses, lineage, validation}`

An admissible path must satisfy all of the following:

1. every required semantic field in `D` meets or exceeds its required preservation
   grade;
2. every derived field is marked derived and linked to inputs and method/version;
3. no `UNKNOWN`, conflict, or non-conclusion is silently collapsed;
4. every dropped or non-recoverable field is declared before execution;
5. reversibility is claimed only when an inverse law is tested or sufficient
   source/witness information is retained.

This is small enough to implement without deciding the universe's primitive
objects or selecting one executable formalism.

## 3. Proposal: Evidence-Preserving Versioned Assertion Architecture

The proposal combines established content-addressing, event sourcing, granular
provenance, materialized views, and typed transformation contracts. It is an
engineering composition of prior art, not a new scientific theory.

### Layer A — Content-addressed evidence store

Store every source document and externally anchored datum as immutable bytes with
a digest, media type, source locator, capture time, and ingestion record. Edits
create successors; they do not replace evidence. A commit is a Merkle-style root
over artifacts and parents. This supplies exact source recovery, branch/split,
common ancestry, and deduplication.

### Layer B — Versioned assertion packets

Represent a research statement as a first-class packet rather than as an
unqualified graph edge:

```text
AssertionPacket {
  id, payload, scope,
  epistemic_class,
  source_spans[], provenance,
  recorded_at, source_time?, validity_scope?,
  supports[], contradicts[], supersedes[], specializes[],
  author_or_process, schema_version
}
```

`epistemic_class` includes at least `SOURCE_SUPPORTED`, `OWNER_DIRECTION`,
`WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, `YOUR_INFERENCE`, and
`RETRACTED_OR_CORRECTED`. `UNKNOWN` is a valid value, not missing data. The exact
source span remains available even when the packet payload is normalized.

The packet shape is nanopublication-like (assertion, assertion provenance, packet
publication information) and its lineage vocabulary should reuse W3C PROV where
it fits. Domain semantics need not be forced into RDF; JSON/SQLite plus explicit
schemas is an acceptable first implementation.

### Layer C — Event-sourced version and lifecycle DAG

All changes are append-only events such as `INGEST`, `CLASSIFY`, `LINK`,
`CORRECT`, `SUPERSEDE`, `BRANCH`, `MERGE_DECISION`, `TRANSFORM`, `INVALIDATE`,
and `RETIRE`. Current state is a deterministic projection of a selected commit and
event prefix. Event order records repository processing order only; causal or
physical order is asserted separately.

Mutability is represented as succession and lineage. Content-addressed immutability
is an audit mechanism and does not imply immutable real-world entities.

### Layer D — Authority registry and sidecar models

There is no universal semantic store. Each artifact declares an authority scope:

- source bytes are authoritative for exact wording;
- reviewed assertion packets are authoritative for explicit classification and
  recorded research position;
- explicitly authored rule/behaviour models may be authoritative only for the
  possible behaviour they declare;
- clock/metric records may be authoritative only for their anchored measurements;
- indexes, summaries, embeddings, causal projections, LTS/reachability graphs,
  simulations, and reconstructions are derived unless separately adopted.

Petri, Event Structure, causal-order, LTS, rewrite, metric, or future formalisms
are sidecar adapters selected for semantics they can actually provide. A sidecar
cannot overwrite its evidence or become ground truth merely because it is easier
to query.

### Layer E — Transformation contract registry

Each adapter publishes a contract:

```text
TransformContract {
  input_schema, output_schema, version,
  requires, guarantees, drops, introduces,
  preservation_grade_by_field,
  deterministic, incremental,
  inverse_kind, retained_witness,
  dependency_rule, cost_model,
  validation_suite
}
```

Grades are field-specific: `EXACT`, `ANCHORED`, `SEMANTIC`, `STATISTICAL`,
`VIEW_DEPENDENT`, or `NON_RECOVERABLE`. For a composed path, guarantees cannot be
stronger than the weakest relevant step and losses accumulate. A reverse path is
not inferred from a forward path.

Views are read-only by default. An edit to a view becomes a proposed patch against
authoritative packets. It is accepted automatically only for an adapter with an
explicitly tested lawful put-back; otherwise it requires review.

### Layer F — Constraint-based planner and evaluation harness

Replace model-name routing rules with a constraint planner. The request declares:

- question/workload;
- required semantics and allowed loss per field;
- current authoritative sources and available derived artifacts;
- lifecycle operation;
- latency, storage, recomputation, audit, and rollback budgets.

The planner filters paths by semantic admissibility before optimizing cost. No
admissible path produces `REVIEW_REQUIRED`, with an explanation of the missing
capability or evidence. The original `S/M/L` distinctions remain useful input
facets, but they are not a complete hard-coded routing algebra.

## 4. Prior-art basis

- W3C PROV distinguishes entities, activities, agents, derivation, use,
  generation, invalidation, and attribution. It supplies a standard lineage
  vocabulary but not Byul's epistemic classes or preservation policy:
  <https://www.w3.org/TR/prov-dm/>.
- Nanopublications package an assertion with assertion provenance and publication
  information at granular scope; Byul can reuse that separation without requiring
  all domain meaning to be RDF: <https://nanopub.net/>.
- Event Sourcing records state changes as events and supports rebuilding derived
  state by replay: <https://www.martinfowler.com/eaaDev/EventSourcing.html>.
- Git demonstrates practical content-addressed objects and parent-linked version
  history: <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>.
- Bidirectional transformation/lens laws motivate testing round trips instead of
  assuming them. The proposal uses the discipline but permits one-way/lossy
  adapters: <https://homepages.inf.ed.ac.uk/perdita/icgt.pdf>.
- CRDT research supplies convergence conditions for selected replicated data
  types. It is intentionally restricted here to safe structural metadata and does
  not auto-resolve semantic claim conflicts:
  <https://arxiv.org/abs/1805.06358>.
- Petri/Open/Reconfigurable Petri, Occurrence Nets, Event Structures, causal-order
  views, LTS, and graph rewriting remain established optional sidecar families
  already identified by the research baseline.

## 5. Alternatives considered

1. **Raw Markdown plus ad-hoc views.** Excellent for exact wording and human use,
   but weak for claim-level authority, contradiction, transformation guarantees,
   and bounded invalidation.
2. **One authoritative knowledge graph.** Queryable and provenance-capable, but
   risks turning extraction/ontology choices into ground truth and needs a
   separate change history anyway.
3. **One executable formalism.** Strong within its semantic domain but forces
   provenance, uncertainty, exact wording, metric anchors, and possible/actual
   behaviour into inappropriate encodings.
4. **Version-control DAG only.** Strong source history and branching, weak
   statement-level epistemic classification and semantic routing.
5. **CRDT merge everywhere.** Provides convergence only under defined algebra;
   it cannot decide whether competing research claims are semantically compatible.
6. **Hard-coded formalism router.** Easy initially, but cannot safely compose
   transformations without field-level preservation, authority, and loss
   contracts.

## 6. Preservation and reconstruction boundaries

### EXACT by contract

- original source bytes, digest, source locator, and captured metadata;
- packet identifiers, explicit payload, classification, scope, provenance links,
  and correction/supersession edges;
- event payloads, parent links, transformation version, declared losses, and
  retained witnesses;
- deterministic snapshot export/import and replay results for the same versions.

### SEMANTIC or ANCHORED only when declared

- normalized labels, equivalent schema migrations, clock/metric conversions,
  lawful view updates, and executable-model translations with tested equivalence
  criteria.

### STATISTICAL or VIEW_DEPENDENT

- embeddings, summaries, inferred clusters, geometry-like reconstruction,
  heuristic routing scores, and simulation estimates.

### NON_RECOVERABLE unless source/witness is retained

- omitted wording; discarded transformation labels; conflict/resource semantics
  removed by causal forgetting; exact clock/space not originally recorded;
  implicit owner intent; unobserved counterfactual behaviour; and a unique reverse
  model after many-to-one projection.

Generated text may propose a reconstruction, but it cannot restore authority or
exactness. It must become a new derived packet with provenance.

## 7. Transformation paths

- `source bytes -> extracted packets`: source remains authoritative; extraction is
  derived and reviewable.
- `packets/events -> current/open/history/core views`: deterministic materialized
  projections with dependency lists.
- `authored behaviour rules -> execution/occurrence -> causal/reachability views`:
  each arrow has a separate loss contract; occurrence cannot recover all possible
  behaviour and causal forgetting cannot recover labels/conflict/resources.
- `view edit -> patch proposal -> reviewed authoritative event`: no silent
  write-back.
- `old schema -> new schema`: preserve old packet, converter version, output,
  loss manifest, and optional inverse witness; compare replayed views.
- `branch A + branch B -> structural merge candidate -> semantic review event`:
  contradictions survive as parallel packets until explicitly resolved.

## 8. Lifecycle behavior

- **Create/ingest:** hash evidence, validate schema, create packets with provenance,
  append event, then build views.
- **Mutate/correct:** append successor/correction; never edit history in place.
- **Compose:** use explicit interface/namespace mappings and authority contracts;
  preserve component lineage and refuse incompatible preservation demands.
- **Split/diverge:** create child commits sharing immutable ancestry; local events
  carry branch identity.
- **Merge:** perform identifier/schema merge first; auto-merge only operations with
  proven algebra; retain semantic conflicts, alternatives, and unknowns.
- **Migrate:** replay through versioned adapters into a new branch, run contract and
  differential tests, then switch the selected head; retain the old readable path.
- **Recover:** rebuild projections from evidence plus events; verify digests and
  deterministic roots; quarantine artifacts whose dependencies are missing.
- **Rollback:** move the selected head or append compensating events. Do not claim
  reversal of external or lossy effects.
- **Compact:** compact derived indexes freely; compact authoritative history only
  when an exact archived replay source remains.
- **Retire/successor:** record successor relation, migration report, unresolved
  losses, and read horizon; do not overwrite the predecessor.

Incremental invalidation follows recorded packet-to-view dependencies. A changed
packet invalidates direct dependents and their transitive materializations, while
global queries may legitimately have a global radius.

## 9. Routing position

`R(S,M,L)` is **modified, not discarded**. Its useful insight is that situation,
current representation, and lifecycle all affect selection. Its weakness is that
the tuple alone does not make preservation compositional or make a path safe.

The proposed planner elevates a demand contract and transformation registry:

`Plan(Demand, Catalog, Operation, TransformRegistry)`.

`S`, `M`, and `L` become normalized parts of these inputs. Semantic admissibility
is a hard gate; cost optimization happens afterward. This makes routing testable
and permits one model, multiple sidecars, a raw-source answer, or refusal.

## 10. BYUL CORE-A alignment

- **Change/mutability:** states are successor commits/events, not overwritten
  essences.
- **Non-substantiality:** stable IDs are handles; object-like projections remain
  declared views unless separately authored.
- **Composition/emergence:** component, transform, and derived-view lineage is
  explicit; higher-level models do not erase lower-level evidence.
- **Conditional relationality:** scope, context, authority, and branch are part of
  assertions; conflicts and incomparable states need not be globally ordered.

Possible tension: immutable evidence objects may look substance-like. The contract
explicitly limits immutability to audit identity and permits successor relations.

## 11. Expected failure modes

- Packetization invents atomic claims or loses rhetorical/contextual meaning.
- Human/LLM classification is wrong even when provenance is complete.
- Fine-grained provenance causes storage and query explosion.
- Transformation contracts overstate semantic equivalence or omit hidden loss.
- Dependency declarations are incomplete, causing stale views.
- Branch merge preserves contradictions but creates unusable clutter.
- Authority scopes overlap or leave gaps.
- Schema evolution breaks deterministic replay.
- Planner search becomes expensive or optimizes an inaccurate cost model.
- Sidecar formalism adapters encode an ontology the source never asserted.
- Content hashes prove byte identity, not truth, quality, or owner intent.
- Event-log order is mistakenly read as domain causality.

## 12. Falsification tests

1. **Correction test:** ingest the historical false `P-series` claim and its later
   correction. A current-state view must not report a canonical P-series, while a
   history view must retain both statements and their relation.
2. **Unknown test:** repeated projection, export/import, branch, and merge must not
   turn `OPEN/UNKNOWN/NON_CONCLUSION` into fact or silently omit it.
3. **Byte fidelity test:** every source snapshot round-trips byte-for-byte with the
   same digest.
4. **Provenance completeness test:** every rendered assertion resolves to source
   spans or to an explicitly identified inference process.
5. **Loss gate test:** request conflict semantics through a causal-only projection;
   the planner must reject the path or declare conflict non-recoverable.
6. **Many-to-one reverse test:** two distinct source models that map to one view
   must not yield a claimed exact reverse without a retained witness.
7. **Concurrent merge test:** branches make opposing classifications of one claim;
   merge must preserve both and require a decision event.
8. **Lifecycle replay test:** create, mutate, compose, split, merge, migrate,
   degrade, recover, and retire; the rebuilt selected state and Merkle root must
   match the pre-failure result.
9. **Invalidation test:** local and global mutations must invalidate exactly the
   declared dependency closure; stale views are a failure.
10. **Scale test:** fan-out, fan-in, dense provenance, long history, and repeated
    schema migration must remain within declared budgets or safely defer.
11. **CORE-A audit test:** detect view/object reification, lost composition lineage,
    context-free identity, and forced total order.
12. **Adversarial extraction test:** ambiguous negation, quotation, historical
    statements, and Korean/English terminology changes must not become unsupported
    current facts.

The proposal is falsified as a safe first architecture if it repeatedly emits an
admissible path that violates a demanded semantic guarantee, cannot reproduce its
selected state from authoritative inputs, or cannot expose the source of a
derived statement.

## 13. Implementation test plan

1. Implement canonical JSON schemas for source artifacts, assertion packets,
   events, authority scopes, demand contracts, and transform contracts.
2. Use a local content-addressed directory plus SQLite indexes and an append-only
   JSONL/SQLite event table. RDF/PROV export is interoperability, not required
   storage.
3. Hand-curate a small baseline packet set with exact source spans; use extraction
   only to propose additions.
4. Build deterministic `current`, `history`, `open`, `classification`, and
   provenance projections.
5. Add a planner that uses finite semantic capability sets before cost scoring.
6. Implement one deliberately lossy causal projection and one exact snapshot
   adapter to prove loss-gating behavior.
7. Add property-based tests for replay determinism, idempotent ingestion,
   branch/merge preservation, loss monotonicity, and supported lens laws.
8. Run T1–T10 plus correction, unknown, conflicting-branch, and schema-migration
   fixtures; record semantic, compute, maintenance, and reversibility metrics.

Initial acceptance requires byte-exact evidence recovery, deterministic replay,
traceability of every view field, zero silent `UNKNOWN` promotion, zero undeclared
loss on accepted paths, and explicit retention of unresolved merge conflicts.

## 14. Open unknowns

- Whether packet granularity can be made consistent enough without excessive
  curation.
- Whether a property graph, RDF dataset, relational schema, or mixed physical
  storage gives the best maintenance/query trade-off.
- Which semantic vocabularies and equivalence tests are sufficient for behaviour,
  conflict, resource, metric, and composition adapters.
- Whether field-level preservation contracts are practical for every transform or
  require conservative coarse contracts.
- Whether a planner is needed at first or a small validated adapter table is safer.
- How owner adoption, scientific support, and later reviewer decisions should be
  represented without conflating authority types.
- Workload and scale distributions; no performance claim is justified yet.

## 15. Why this could be wrong

- The proposal may over-engineer a small Markdown research corpus and impose
  curation cost larger than its retrieval or safety benefit.
- Assertion packets may still smuggle an object-first ontology into claim IDs and
  predicates.
- Authority-by-field may be too complex for humans to understand reliably.
- A simpler document-DAG plus strict citations could achieve most benefits.
- Contract declarations may merely relocate, not solve, semantic judgment.
- The research may later require continuous or process-native semantics that the
  discrete event/assertion substrate represents poorly.
- Neutrality is limited: emphasizing provenance and lifecycle favors an
  audit-ledger framing over other possible problem formulations.

## Phase-1 conclusion

Adopt the Evidence-Preserving Versioned Assertion Architecture as the strongest
implementable first architecture justified by the baseline, with a
content-addressed evidence plane, versioned assertion/provenance packets,
event-sourced lifecycle DAG, authority-scoped sidecar models, and
preservation-constrained transformation planning. The architecture deliberately
does not select a universal model and must return `UNKNOWN / REVIEW_REQUIRED`
whenever a preservation contract cannot be proven.

`PHASE1_FROZEN = TRUE`
