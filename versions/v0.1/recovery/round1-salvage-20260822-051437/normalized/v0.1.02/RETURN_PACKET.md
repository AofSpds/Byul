```text
[RETURN PACKET]
ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1
ROUND_SLOT = R02
RUN_ID = v0.1.02
COHORT = ROUND1_10_RUN
PROFILE = NEUTRAL_BLIND
RESEARCH_BASELINE_COMMIT = 891e4bd4b999eacc99431ed0db05062901a68dd9
PHASE1_FROZEN = TRUE

CURRENT_STATE_RECONSTRUCTION =
Byul is an active, non-normative, unvalidated research-memory track. Its current
high-resolution owner hypothesis treats objects, identities, and boundaries as
possibly persistent higher-scale views of composed local processes, while BYUL
CORE-A asks implementations to remain compatible with change, non-substantiality,
composition/emergence, and conditional relationality. The candidate
Petri/Occurrence/Event/Causal/LTS family and R(S,M,L) are research candidates, not
answers. Preservation demand, provenance, lifecycle drift, reconstruction grade,
and UNKNOWN/non-conclusion retention are central. The earlier P-series abstraction
was explicitly corrected and is not a canonical rule set.

STATE_CLASSIFICATION =
- SOURCE_SUPPORTED: Byul status and version boundary; research-memory-as-data;
  owner-stated worldview status; BYUL CORE-A status and content; candidate model
  roles; R(S,M,L) and preservation-demand research direction; lifecycle and MI-1
  evaluation requirements; P-series correction.
- WORKING_HYPOTHESIS: causal order as a useful but lossy skeleton; complementary
  behaviour/occurrence/view formalisms; preservation demand as a primary router
  feature; succession as more faithful than permanent identity in some contexts.
- OWNER_DIRECTION: prior-art first; preserve provenance, uncertainty, corrections,
  non-conclusions, and composition lineage; measure full lifecycle and semantic
  cost; do not claim scientific/philosophical proof.
- OPEN: primitive/minimal algebra; required transformation semantics; authority
  boundaries; minimal routing features; safe merges; drift/reconstruction/scale
  thresholds.
- NON_CONCLUSION: no canonical Petri/Causal/universal model, single canonical
  representation, global clock, or automatic recovery of discarded semantics.
- YOUR_INFERENCE: the smallest useful first problem is epistemic-state and
  transformation control, not selection of a world ontology; authority must be
  scoped by semantic field; replica convergence is not semantic correctness.

MINIMAL_PROBLEM_DEFINITION =
Given immutable source artifacts, versioned assertion packets, a representation
catalog, and a query or lifecycle operation, construct an answer only through a
machine-checkable transformation path that satisfies field-level preservation,
lineage, authority, and loss constraints. Mark every derived or introduced value,
retain conflicts and UNKNOWN, disclose non-recoverable information before
execution, and return UNKNOWN / REVIEW_REQUIRED when no admissible path exists.

PHASE1_PROPOSAL =
Evidence-Preserving Versioned Assertion Architecture (EPVAA):
1. A content-addressed evidence store preserves exact source bytes and immutable
   receipts while successor links represent change.
2. Nanopublication-like AssertionPackets make payload, epistemic class, exact
   source spans, scope, provenance, correction/supersession, contradiction, author
   or process, and schema version first-class.
3. An append-only event log plus parent-linked version DAG represents ingestion,
   classification, correction, branching, merge decisions, transformation,
   invalidation, migration, and retirement. Current state is replayable.
4. An authority registry assigns authority by artifact role/semantic field.
   Behaviour, occurrence, causal, reachability, metric, and other formalisms are
   optional sidecars, not one universal semantic store.
5. Every adapter publishes requires/guarantees/drops/introduces, field-specific
   preservation grades, inverse kind or retained witness, dependencies, cost, and
   validation tests.
6. A constraint planner filters by semantic admissibility before cost. S, M, and L
   remain useful input facets but no hard-coded model-name rule can bypass the
   preservation contract.

PRIOR_ART_BASIS =
- [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/) for entity/activity/agent
  lineage, derivation, generation, use, invalidation, and attribution.
- [Nanopublications](https://nanopub.net/) for granular separation of assertion,
  assertion provenance, and publication information.
- [Event Sourcing](https://www.martinfowler.com/eaaDev/EventSourcing.html) for an
  append-only change history and deterministic state rebuild.
- [Git content-addressed objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
  for practical content identity and parent-linked versioning.
- [Bidirectional transformation/lens laws](https://homepages.inf.ed.ac.uk/perdita/icgt.pdf)
  for tested round-trip discipline without assuming every adapter has an inverse.
- [CRDT research](https://arxiv.org/abs/1805.06358) for narrowly scoped convergent
  structural operations, not automatic semantic conflict resolution.
- The baseline's Petri/Open/Reconfigurable Petri, Occurrence Net, Event Structure,
  causal-order, LTS, and rewrite families remain optional semantic sidecars.

AUTHORITATIVE_REPRESENTATION =
Authority is plural and explicitly scoped: source blobs are authoritative for
exact wording; reviewed assertion packets for recorded classification and research
position; explicitly authored rule models only for the possible behaviour they
declare; anchored metric records only for their measurements; event/commit records
for repository succession and decisions. No derived view gains source authority.

DERIVED_REPRESENTATIONS =
Current/history/open/core-principle views, summaries, embeddings, clusters,
causal-order projections, occurrence unfoldings, LTS/reachability graphs,
simulations, reconstructed geometry, routing scores, and extracted packets before
review. Each carries input IDs, method/version, preservation/loss manifest, and
dependency set. A human-adopted sidecar may acquire only its declared authority
scope through a new event; it does not retroactively become source evidence.

PRESERVATION_CONTRACT =
Each semantic field is graded EXACT, ANCHORED, SEMANTIC, STATISTICAL,
VIEW_DEPENDENT, NON_RECOVERABLE, or UNKNOWN. An accepted composed path cannot
claim more than its weakest relevant step; losses accumulate; introductions are
marked; UNKNOWN/conflict/non-conclusion cannot be collapsed. Reverse compatibility
is claimed only for tested laws or when sufficient source/witness data is retained.
Exact initial obligations include source bytes/digests, packet payload and class,
source spans/provenance, correction and parent edges, transformation version,
declared losses, and deterministic replay for the same inputs.

LOSS_AND_NON_RECOVERABLE =
Unless retained independently: omitted wording; formatting erased by normalization;
discarded transformation labels; conflict/resource semantics removed by causal
forgetting; exact clock/space never recorded; implicit owner intent; unobserved
counterfactual behaviour; and a unique source model after many-to-one projection.
Summaries or generated reconstructions are new derived assertions, never recovery
of original authority.

TRANSFORMATION_PATHS =
- source bytes -> proposed extracted packets -> reviewed packet event;
- packets/events -> deterministic current/history/open/provenance views;
- authored behaviour -> occurrence -> causal/reachability views, with a separate
  loss contract at every arrow;
- view edit -> patch proposal -> review -> authoritative event, never silent
  write-back;
- old schema -> versioned converter -> new branch + differential/round-trip report;
- branches -> structural merge candidate -> explicit semantic decision, retaining
  unresolved alternatives.

LIFECYCLE_BEHAVIOR =
Create hashes and classifies evidence; mutate appends correction/successor events;
compose uses explicit interface and authority mappings; split shares immutable
ancestry; merge auto-combines only operations with proven algebra and preserves
semantic conflicts; migrate replays through versioned adapters into a tested
branch; recover rebuilds views from evidence/events and quarantines missing
dependencies; rollback moves the selected head or appends compensation without
pretending to reverse external/lossy effects; retire records successor, migration
losses, unresolved state, and read horizon. Invalidation follows the transitive
recorded dependency closure and may legitimately be global.

ROUTING_POSITION =
MODIFY R(S,M,L). Preserve its insight that situation, current representation, and
lifecycle matter, but implement Plan(Demand, Catalog, Operation,
TransformRegistry). Demand includes query intent and field-level loss tolerances;
Catalog includes authority and lineage; Operation contains lifecycle and budgets.
Semantic admissibility is a hard gate before cost optimization. Valid outcomes may
be one view, multiple sidecars, raw evidence, or REVIEW_REQUIRED.

BYUL_CORE_A_ALIGNMENT =
- CHANGE: successor commits/events express mutation without overwriting history.
- NON-SUBSTANTIALITY: IDs are operational handles and object-like structures remain
  declared views unless separately authored.
- COMPOSITION/EMERGENCE: component, transformation, and higher-view lineage is
  explicit and lower evidence is retained.
- CONDITIONAL RELATIONALITY: scope, context, authority, branch, conflict, and
  causal incomparability remain representable without a forced total order.
Content immutability is limited to audit identity and is not an ontological claim.

EXPECTED_FAILURE_MODES =
Packetization can invent atomicity or lose context; classification can be wrong;
fine provenance can explode; contracts can overstate equivalence or omit hidden
loss; dependency maps can leave stale views; conflicts can accumulate into clutter;
authority scopes can overlap or gap; schema change can break replay; planning/cost
models can scale poorly; adapters can smuggle an unsupported ontology; hashes prove
identity, not truth; event order can be misread as domain causality.

FALSIFICATION_TESTS =
1. P-series correction: current view rejects the earlier false abstraction while
   history retains both claim and correction.
2. UNKNOWN/non-conclusion survives projection, export, branch, merge, and replay.
3. Source evidence round-trips byte-for-byte with the same digest.
4. Every output field traces to source or an identified inference process.
5. An EXACT-conflict demand through causal forgetting is rejected.
6. Many-to-one projection cannot claim an exact reverse without a witness.
7. Opposing branch classifications survive merge pending a decision event.
8. Full create/mutate/compose/split/merge/migrate/degrade/recover/retire replay
   reproduces the selected state and root digest.
9. Local/global mutation invalidates exactly its declared dependency closure.
10. Dense provenance, fan-out/in, long history, and schema migrations meet budgets
    or safely defer.
11. CORE-A audit detects view reification, lost composition lineage, context-free
    identity, and forced total order.
12. Ambiguous negation, quotation, historical statements, and terminology changes
    do not become unsupported current facts.

IMPLEMENTATION_TEST_PLAN =
Define canonical schemas for evidence, AssertionPacket, events, authority, demand,
and transform contracts. Start with a content-addressed directory, SQLite indexes,
and append-only JSONL/SQLite events; make RDF/PROV an export. Hand-curate a small
baseline packet set with exact source spans. Build deterministic current, history,
open, classification, and provenance projections. Add a finite capability/loss
planner, then one exact snapshot adapter and one deliberately lossy causal adapter.
Use property-based tests for replay, idempotent ingestion, branch/merge retention,
loss monotonicity, and supported lens laws. Run T1-T10 plus correction, UNKNOWN,
conflicting-branch, and schema-migration fixtures. Initial acceptance requires
byte-exact recovery, deterministic replay, traceability, no silent UNKNOWN
promotion, no undeclared accepted loss, and explicit unresolved conflicts.

OPEN_UNKNOWNS =
Practical packet granularity and curation cost; physical storage choice; adequate
semantic vocabularies/equivalence tests; feasibility of field-level contracts;
planner versus conservative adapter table; representation of owner adoption versus
scientific support and reviewer decisions; real workload/scale distributions and
acceptance thresholds.

WHY_THIS_COULD_BE_WRONG =
It may over-engineer a small Markdown corpus; packet IDs and predicates may smuggle
object-first assumptions; authority-by-field may be too complex; a document DAG
plus strict citations may provide most benefit; contracts may relocate rather than
solve semantic judgment; continuous/process-native semantics may fit a discrete
assertion/event substrate poorly; the audit-ledger framing is itself a bias.

PHASE2_CURRENT_V0_1_COMPARISON =
KEEP from current: raw-memory authority over derived views; exact source locator
intent; explicit non-normative status; line provenance; current/history/open/model/
lifecycle/core views; preservation vocabulary; UNKNOWN and exact-metric deferral;
no automatic Core-Principles PASS; a small stdlib implementation and virtual
invalidation seed. Direct execution of `python versions/v0.1/tests/test_byul_v01.py
-v` passed all 11 authored tests on 2026-08-22; this is implementation evidence,
not scientific/model validation. The documented `python -m unittest
versions/v0.1/tests/test_byul_v01.py` command failed because `v0.1` is parsed as a
dotted module path.

CHANGE as deltas only: (a) enforce the declared source commit rather than loading a
mutable working-tree glob; (b) retain and hash original bytes, because the current
snapshot stores normalized non-empty atoms and cannot reconstruct blank lines,
whitespace, newline form, or full original text; (c) replace substring tags and
file-level heuristic views with reviewed assertion packets that cover the required
state classes and correction relations; (d) replace intent-to-view lookup with
field-level capability/loss contracts, since current preservation inputs other than
EXACT history are accepted but not enforced; (e) add append-only lifecycle/version
events, branch/merge/migration/recovery semantics, and dependency-derived
invalidation; (f) keep the existing v0.1 baseline `2a4529b...` distinct and migrate
explicitly to any newer research target; (g) add real import/replay and semantic
loss tests, and correct the test command. Current lifecycle handling remains route
annotations and one virtual append, not lifecycle execution.

DISPOSITION = MODIFY_CURRENT

MATERIAL_DELTAS_FROM_CURRENT =
1. Exact-byte, exact-commit evidence ingestion and verifiable corpus manifest.
2. Reviewed first-class AssertionPackets with provenance, scope, epistemic class,
   correction/contradiction/supersession, plus append-only version/lifecycle events.
3. Authority registry and preservation-constrained transformation planner replacing
   heuristic routing acceptance; explicit adapter loss, inverse/witness, and costs.
4. Real split/merge/migrate/recover/replay plus dependency-closure invalidation.
5. Stronger tests for baseline enforcement, byte fidelity, correction/UNKNOWN,
   undeclared loss, merge conflicts, many-to-one reverse claims, and scale; fix the
   documented unittest invocation.

TOP_3_REASONS =
1. The current raw/derived authority boundary and cautious REVIEW_REQUIRED behavior
   are the right low-risk foundation, so replacement would discard useful working
   code without justification.
2. Current fidelity and routing guarantees are weaker than their labels: normalized
   atoms are not exact source recovery, and arbitrary preservation demands are not
   checked against representation capabilities.
3. The proposal adds the smallest coherent mechanism for the research's central
   unresolved needs: correction-aware epistemic state, explicit semantic loss,
   composable transformations, and full lifecycle lineage.

CONFIDENCE = MEDIUM. The architecture is strongly grounded in mature provenance,
versioning, event-log, and transformation-contract ideas and can be implemented
incrementally on the current slice. Confidence is not HIGH because packet
granularity, semantic equivalence criteria, workload scale, and the benefit/cost of
a planner have not been empirically validated, and no scientific or owner
acceptance is claimed.
```
