# Phase 1 Frozen Proposal

ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01
ROUND_SLOT = R06
RUN_ID = v0.1.07
WORKER_ID = 20260822-053853-f6cf4c88
PROFILE = NEUTRAL_BLIND
PHASE1_INPUT_COMMIT = 891e4bd4b999eacc99431ed0db05062901a68dd9
PHASE1_IMPLEMENTATION_READ = FALSE

## CURRENT_STATE_RECONSTRUCTION

Byul is a non-normative research track for representing a changing research
memory without turning current preferences into canonical truth. Its current
high-resolution worldview is an Owner hypothesis: local mappings/processes may
compose into persistent higher-scale patterns that are viewed as objects,
selves, personas, protocols, or boundaries. Continuity is therefore closer to
succession and lineage than immutable identity. Global absolute NOW, a unique
primitive, a universal model, and automatic recovery of discarded semantics
remain explicitly uncommitted.

BYUL CORE-A currently asks designs to remain compatible with mutability,
non-substantial/derived entities, composition/emergence, and conditional
relationality. These are Owner-adopted research principles, not validated
physics, AAA-wide canonical requirements, or automatic PASS conditions.

The current research candidate is a complementary family: behaviour/rules,
occurrence/concurrency, causal/reachability views, and lifecycle-aware routing
described by `R(S,M,L)`. The memory records Petri/Open/Reconfigurable Petri,
Occurrence/Event Structure, causal-order, and LTS as candidates, not answers.
Preservation demand, provenance, semantic loss, reconstruction grade,
invalidation, mutation history, and long lifecycle sequences are unresolved
design obligations. The memory says an experimental v0.1 slice exists, but
Phase 1 has not inspected it and makes no claim about its actual code.

## STATE_CLASSIFICATION

### SOURCE_SUPPORTED

- Event and causal partial-order abstractions can preserve causal structure
  without imposing a total global order; a causal link alone does not preserve
  transformation semantics.
- Behaviour models, occurrence histories, event/conflict models, and
  reachability views answer different questions and translations among them can
  be lossy or non-unique.
- Provenance, raw wording, epistemic status, explicit unknowns/non-conclusions,
  transformation history, and loss declarations are necessary reconstruction
  inputs according to the pinned memory.
- W3C PROV, event sourcing, bitemporal databases, content-addressed object
  stores, materialized views, and CRDTs provide established pieces of an
  implementable solution; none individually supplies research semantics.

### OWNER_DIRECTION

- Prefer the high-resolution hypothesis of composed local mappings/processes
  while keeping it non-normative and open to falsification.
- Preserve succession/history rather than assuming immutable identity.
- Use situation-sensitive representation and lifecycle simulation; do not let
  one favoured formalism become canonical without evidence.
- Apply BYUL CORE-A as a review lens and keep prior-art-first discipline.

### WORKING_HYPOTHESIS

- Preservation Demand may be the strongest Situation Fingerprint axis.
- A complementary model family may be better than a universal representation.
- `R(S,M,L)` may be a useful research-level routing decomposition.
- A provenance-rich occurrence/fact plane and a behaviour/rule plane may be
  complementary.

### OPEN

- The minimal sufficient record grammar, the exact boundary between source and
  claim, and the necessary relation types.
- Which meanings require byte-exact, semantic, anchored, statistical, or
  intentionally non-recoverable treatment.
- Whether automated routing provides enough benefit to justify its own state,
  classification cost, and failure modes.
- When Petri/Event/Causal/LTS or an outside formalism materially outperforms a
  simpler ledger plus projections.
- Acceptance thresholds for semantic drift, lifecycle preservation, and
  reconstruction.

### NON_CONCLUSION

- Petri is not canonical; Causal Set is not the final architecture; Event or
  local mapping is not an established primitive.
- One canonical representation, one universal model, and exact inverse
  translation are not requirements.
- BYUL CORE-A is not a scientific truth claim and does not authorize automated
  acceptance.
- Chronology is not automatically causality, and antichains are not proof of
  exact simultaneity.

### YOUR_INFERENCE

- The core engineering problem is not primarily selecting a mathematical model.
  It is maintaining an auditable distinction between immutable evidence of what
  was recorded and revisable interpretations of what that evidence means.
- The safest authoritative layer is therefore a small append-only provenance
  event ledger; specialized formalisms should normally be contracted,
  regenerable projections unless a workload requires authoritative behaviour
  rules that cannot be derived from occurrence records.
- Convergent storage and semantic agreement must be separated. Replicas may
  converge by set union while contradictory claims remain deliberately
  unresolved.

## MINIMAL_PROBLEM_DEFINITION

Given a stream of source artifacts, claims, classifications, corrections,
transformations, branch decisions, and lifecycle operations, preserve enough
evidence to answer:

1. What exactly was recorded, by whom, from which source, under which scope and
   epistemic status?
2. How did a requested state or view arise, what did each transformation
   preserve or discard, and which inputs invalidate it?
3. Can a past or branch-specific state be reconstructed without inventing
   meaning, silently resolving conflict, or promoting a derived view to truth?
4. Which optional projection is justified for a query/lifecycle operation under
   an explicit preservation and cost contract?

The minimal success condition is deterministic reconstruction of the recorded
research state and honest declaration of everything not reconstructable. It is
not an ontology of reality and not automatic scientific judgment.

## PHASE1_PROPOSAL

Adopt an **append-only bitemporal provenance ledger with contracted
projections**.

The authoritative store has three layers:

1. **Immutable source blobs.** Preserve original bytes, media type, source
   locator, capture metadata, and content digest. A digest identifies immutable
   content; it is not the stable identity of a changing concept.
2. **Immutable research events.** Append typed events such as `ASSERT`,
   `CLASSIFY`, `RELATE`, `SUPERSEDE`, `RETRACT`, `CONTRADICT`, `BRANCH`,
   `MERGE_DECISION`, `TRANSFORM`, `VALIDATE`, and `SNAPSHOT`. Every event carries
   an event ID, schema version, payload/blob references, subject/scope handles,
   epistemic class, authority/actor, source references, recorded time,
   optional valid-time interval/uncertainty, parent event IDs, and an integrity
   digest.
3. **Transformation receipts.** Every derivation records exact input IDs and
   digests, transformer name/version/code digest, parameters, output IDs,
   declared preservation/loss contract, validation evidence, and dependency
   edges. A receipt is data, not a promise that the transformation is sound.

The ledger is authoritative only for **what the research process recorded**.
It does not make every payload true. Current state is a deterministic,
policy-versioned fold over events at a transaction-time cutoff and optional
valid-time scope. Corrections append events; they never overwrite the original.
An explicit unresolved conflict set is a valid state.

For concurrent branches, replicate the immutable event/blob set by union (a
grow-only convergence mechanism). Do not use last-writer-wins or an automatic
CRDT merge to settle semantic disagreement. Resolution is a new, attributed
`MERGE_DECISION` event that retains both inputs.

Specialized models are registered as projections with capabilities,
preconditions, dependencies, loss class, builder version, cost evidence, and
freshness. A projection may be promoted to an additional authoritative source
only by an explicit governance decision when it contains non-derivable rules
or commitments; promotion creates a new source record rather than mutating the
ledger's history.

## PRIOR_ART_BASIS

- [W3C PROV-DM](https://www.w3.org/2012/10/prov-dm) supplies domain-agnostic
  entities, activities, agents, derivations, revisions, invalidations, bundles,
  and collections. Use it as the interchange/provenance vocabulary, extended
  with Byul epistemic and preservation types.
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) supplies
  the established pattern of storing state changes as events and rebuilding
  state by replay. Byul must add explicit epistemic status, bitemporality,
  provenance, conflict, and loss contracts.
- Snodgrass's [temporal database overview](https://www2.cs.arizona.edu/~rts/pubs/EDC.pdf)
  distinguishes valid time from transaction time. This prevents “when we
  recorded/believed it” from being confused with “when it purportedly held.”
- [Git's content-addressed object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects.html)
  demonstrates immutable blobs/trees and parent-linked snapshots. Byul should
  borrow integrity and lineage mechanics, not assume commits encode domain
  causality or semantic agreement.
- Shapiro et al.'s [CRDT work](https://arxiv.org/abs/1805.06358) establishes
  deterministic convergence after replicas receive the same updates. Byul
  should use this only for convergent event-set storage; semantic conflicts
  remain explicit.
- Materialized-view and data-provenance work motivates regenerable,
  dependency-tracked projections rather than treating every optimized view as
  ground truth.

This proposal is a composition of established patterns, not a new formal
theory.

## AUTHORITATIVE_REPRESENTATION

The authority root is the tuple:

`(immutable source blobs, immutable research events, transformation receipts)`

Minimum event envelope:

```text
event_id, event_type, schema_version
payload_ref/content_digest
subject_handle, scope/context
epistemic_class, authority_class, actor
source_refs, parent_event_ids
recorded_at, valid_time_or_unknown
relation_targets
branch_id, integrity_digest
```

Required epistemic classes include at least `SOURCE_SUPPORTED`,
`OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, and
`INFERENCE`; “unknown” is a value, not missing data. Relation types must
distinguish revision/supersession, retraction/invalidation, contradiction,
support, derivation, quotation, dependency, and mere association. Relation
semantics are never inferred solely from time or adjacency.

A subject handle gives continuity across revisions without claiming an
unchanging substance. Each event-specific entity remains immutable; the handle
is a view over its succession lineage.

## DERIVED_REPRESENTATIONS

- Current research dossier: active claims, classifications, open questions,
  explicit non-conclusions, and unresolved conflicts at a chosen cutoff.
- History/chronology view: transaction and valid-time timelines, without
  silently interpreting order as causality.
- Provenance/argument graph: sources, claims, agents, derivations, support,
  contradiction, revision, and validation evidence.
- Dependency/invalidation graph: exact inputs and downstream artifacts for
  incremental rebuild.
- Causal/occurrence view: only where causal relations are explicitly supported;
  no causal edges inferred from document order alone.
- Behaviour/rule model (Petri, LTS, rewrite, or other): only when possible
  behaviour, resources, conflict, or topology mutation is a real workload and
  rule semantics are supplied.
- Query-specific search/vector/index views: disposable accelerators whose source
  IDs, builder version, freshness, and loss class remain visible.
- Human-readable snapshots and handoff packets: signed/checksummed checkpoints,
  never substitutes for the ledger.

## PRESERVATION_CONTRACT

Every transformation declares a matrix row for each relevant meaning:

`meaning | authority source | required grade | actual grade | verifier |
allowed loss | recovery source | invalidation dependency`

Grades are `BYTE_EXACT`, `STRUCTURAL_EXACT`, `SEMANTIC`, `ANCHORED`,
`STATISTICAL`, `VIEW_DEPENDENT`, and `NON_RECOVERABLE`. A single artifact may
have different grades per meaning.

Hard fail-gate candidates:

- Original bytes/digest, source locator, attribution, scope, and capture record
  are byte/structurally exact.
- Epistemic class, authority class, explicit unknown, explicit non-conclusion,
  supersession/retraction/contradiction, and lineage are structurally exact.
- Transformer identity/version/parameters, input/output IDs, declared loss, and
  validation result are structurally exact.
- No derived view is labelled authoritative or fresh without an explicit
  authority/freshness record.
- Natural-language meaning is not claimed byte-exact after summarization; it
  requires retained source plus semantic or human review.

## LOSS_AND_NON_RECOVERABLE

- A summary cannot recover omitted qualifiers, tone, ambiguity, or wording. The
  retained source blob is the recovery path; without it these are
  non-recoverable.
- A causal/reachability projection cannot recover transformation labels,
  resource rules, conflict semantics, or alternatives that were not encoded.
- Behaviour inferred from observed occurrences is underdetermined; many rule
  systems can explain the same trace.
- Timestamp order cannot recover domain causality or simultaneity.
- Automatic extraction from prose can split or merge claims incorrectly. The
  extraction is derived and must retain spans and review state.
- Set convergence cannot recover semantic agreement. A conflict resolved by
  deletion or last-writer-wins loses a research branch; therefore neither is
  allowed at the authoritative layer.
- Redaction, source disappearance, encryption-key destruction, and legal
  deletion can intentionally make payloads non-recoverable. Preserve a minimal
  tombstone/receipt only when policy permits.
- Schema meaning lost during a migration cannot be recreated by a later schema;
  failed migrations require old readers or explicitly recorded loss.

## TRANSFORMATION_PATHS

1. `source bytes -> immutable blob`: byte-exact digest verification.
2. `blob -> extracted claims/events`: span-linked, derived, reviewable; never
   replaces the blob.
3. `events -> state at cutoff`: deterministic fold with policy/schema version,
   unresolved-conflict preservation, and replay hash.
4. `state/events -> specialized projection`: capability and preservation
   contract, dependency set, builder version, validation receipt.
5. `projection -> query answer`: answer carries projection/source cutoff,
   freshness, uncertainty, and loss grade.
6. `old schema -> new schema`: append migration receipt, retain old events,
   differential replay old/new, and block promotion on unexplained delta.
7. `snapshot -> recovered state -> replay tail`: verify snapshot root, replay
   digest, and state equivalence; snapshot is a cache.

No derived projection is used to synthesize an authoritative source unless a
new human/governance event explicitly accepts that non-unique synthesis.

## LIFECYCLE_BEHAVIOR

- **Mutate/correct:** append classification, supersession, retraction, or new
  version events; invalidate dependent projections by recorded dependency.
- **Compose:** union immutable records, preserve namespace/scope, add explicit
  interface/composition events, and surface collisions/conflicts.
- **Split:** create a scope-selected branch plus transitive provenance closure;
  record omitted dependencies and whether the split is self-contained.
- **Diverge:** branch tips reference a common event frontier; neither branch is
  privileged by time alone.
- **Merge:** union event sets, compute unresolved semantic conflicts, and append
  attributed decisions. Preserve both branch histories.
- **Migrate:** dual-read/replay, compare preservation matrices and query results,
  then append cutover; do not rewrite history.
- **Degraded operation:** accept durable events if safe, mark projections stale,
  and refuse answers whose freshness/preservation contract cannot be met.
- **Recover/rollback:** restore a verified snapshot and replay; rollback is a new
  compensating event/branch selection, not deletion.
- **Successor/retire:** add schema/reader versions and retirement metadata;
  retain a compatibility path or declare exactly what becomes non-recoverable.

## ROUTING_POSITION

`R(S,M,L)` is useful as a research mnemonic but insufficient as an executable
interface. `S` currently mixes workload, preservation, precision, and budgets;
`M` risks mixing authority with cache state; and a router cannot justify a plan
without a capability/cost catalog and validation evidence.

Keep `S/M/L` as observable axes, but lower them into a typed routing request:

`Plan(Q, P, A, L, C) -> {projection set, transforms, proof obligations,
fallback/refusal}`

- `Q`: question/workload.
- `P`: per-meaning preservation/precision contract.
- `A`: authoritative roots and current cutoffs.
- `L`: lifecycle operation/context.
- `C`: registered projection capabilities, preconditions, measured costs,
  freshness, validation evidence, and operational budgets.

The router never chooses which recorded history is true and never replaces the
authoritative ledger. It chooses only derived plans. If required preservation
cannot be proven, it returns `REVIEW_REQUIRED` or refuses the route. This is a
constrained planner/catalog lookup first; learned ranking may only break among
already-valid plans and must expose evidence.

## BYUL_CORE_A_ALIGNMENT

- **Change/mutability:** corrections and lifecycle operations are first-class
  events; no current-state overwrite erases succession.
- **Non-substantiality/derived entity:** stable handles are explicitly separated
  from immutable event-specific entities and materialized object/persona views.
- **Composition/emergence:** local records compose by explicit interfaces and
  retain lineage into higher-scale projections.
- **Conditional relationality:** assertions are scoped; relations, observer/
  actor, authority, valid time, and context remain visible. No global total
  order is forced.

Alignment remains a review claim to be tested, not automatic Owner Acceptance.

## EXPECTED_FAILURE_MODES

- Schema and relation-type proliferation makes capture slower than plain notes.
- Claim extraction atomizes prose incorrectly or creates false precision.
- Provenance completeness is mistaken for truth or quality.
- Event replay becomes expensive; snapshots hide incompatible fold versions.
- The append-only ledger conflicts with privacy, secrecy, or deletion duties.
- Semantic conflicts grow faster than humans can resolve them.
- Implicit total order leaks in through database sequence numbers or timestamps.
- Content/subject identifiers are confused, recreating immutable-object
  assumptions.
- Projection dependencies are incomplete, leaving stale answers marked fresh.
- Router inputs cost more to produce than the query benefit, or evidence is too
  sparse for a defensible route.
- A specialized behaviour model contains non-derivable rules but is incorrectly
  treated as disposable.
- Hash, signature, schema, and reader migrations outlive their tooling.

## FALSIFICATION_TESTS

1. **Minimal-baseline challenge:** compare against immutable raw documents plus
   Git history and a hand-built current index. Reject the proposal if the ledger
   does not materially improve reconstruction, loss visibility, or lifecycle
   safety enough to justify complexity.
2. **MI-1 blind reconstruction:** fresh instances reconstruct fact/Owner
   direction/hypothesis/open/non-conclusion from ledger versus source documents;
   count invented commitments and missing qualifiers.
3. **Retraction revival:** assert A, retract A, add contradictory B, later restore
   A under a narrower scope. Reconstruct every cutoff and require unresolved
   conflicts to remain visible.
4. **Concurrent divergence:** two branches independently reclassify the same
   claim. Event sets must converge without silently resolving epistemic status.
5. **Causality trap:** shuffle transaction order while preserving explicit
   dependencies. Causal projection must remain unchanged.
6. **Loss trap:** remove transformation labels before causal projection; reverse
   synthesis must declare them non-recoverable rather than invent them.
7. **Lifecycle torture:** compose, split, diverge, merge, migrate, degrade,
   recover, and retire across schema versions while checking provenance closure
   and cumulative semantic delta.
8. **Corruption/staleness:** flip blob bytes, omit one dependency, and replay
   from an old snapshot. Digest, invalidation, or freshness gates must fail.
9. **Router counterexample:** construct pairs with identical S/M/L labels but
   different preservation contracts or validated capabilities; any identical
   unsafe route falsifies coarse `R(S,M,L)` sufficiency.
10. **Scale threshold:** measure replay, dependency fan-out, graph density,
    storage, and query latency until the design loses to a simpler baseline.

## IMPLEMENTATION_TEST_PLAN

No implementation is performed in this run. A separately authorized trial
should proceed in gates:

1. Define a small versioned JSON/relational schema for blobs, events, relations,
   receipts, preservation rows, and projection catalog. Reject fields without a
   demonstrated test need.
2. Implement append, deterministic fold-at-cutoff, provenance closure,
   unresolved-conflict view, dependency invalidation, snapshot/replay, and one
   human-readable current-state projection.
3. Ingest the pinned research memory while retaining exact blobs and span links;
   independently review the extracted classifications.
4. Add one causal/provenance graph and one behaviour/reachability projection
   only for explicit benchmark questions.
5. Run property/metamorphic tests for immutability, idempotent ingest, replay
   determinism, branch-union convergence, cutoff reconstruction, and refusal on
   unmet contracts.
6. Run T1-T10 plus the falsification cases above; report semantic, compute,
   maintenance, and reversibility costs separately.
7. Compare with the minimal Git/raw-document baseline before accepting any
   router automation or additional formalism.

## OPEN_UNKNOWNS

- Whether claims should be atomic records, span-anchored bundles, or both.
- The smallest relation vocabulary that preserves meaning without ontology
  sprawl.
- How valid time applies to worldview hypotheses and non-temporal claims.
- How to quantify semantic equivalence without circular human judgment.
- Which authority decisions may promote a derived model to a co-authoritative
  rule source.
- Privacy/redaction policy and cryptographic-agility requirements.
- Whether concurrent multi-writer operation is common enough to justify CRDT
  mechanics beyond ordinary version control.
- Which workloads genuinely need Petri/Event/LTS/causal projections.
- Router acceptance thresholds and how evidence transfers across domains.

## WHY_THIS_COULD_BE_WRONG

Byul's present corpus may be small enough that Git-versioned Markdown plus a
careful status file is safer and more legible. Structured event capture may
force ambiguous research prose into premature categories, while the proposed
ledger/catalog/contract stack creates substantial maintenance surface. W3C
PROV is generic and can become verbose; bitemporal fields may add little for
non-temporal claims; event sourcing makes schema evolution and replay versioning
hard; CRDT convergence may solve a concurrency problem Byul does not have.

Most importantly, a provenance ledger preserves the history of representations,
not the meanings themselves. Human semantic interpretation, source quality,
Owner intent, and theory validity remain outside deterministic replay. If MI-1
and lifecycle tests show no clear advantage over raw-source retention plus
small explicit indexes, the correct conclusion is to keep the simpler system.

PHASE1_RECOMMENDATION_SUMMARY = Use a minimal append-only bitemporal provenance
ledger as authority for recorded history; make specialized models contracted,
regenerable projections; preserve semantic conflict instead of auto-merging it;
and refine `R(S,M,L)` into a typed preservation-first plan request.

IMPLEMENTATION_AUTHORITY = NONE
IMPLEMENTATION_PERFORMED = FALSE
