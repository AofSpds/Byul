[RETURN PACKET]

ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01
ROUND_SLOT = R06
RUN_ID = v0.1.07
WORKER_ID = 20260822-053853-f6cf4c88
PROFILE = NEUTRAL_BLIND

EXECUTION_CONTROL_BASE_COMMIT = 68815178d104b74f56b6ab071dd24226862c079d
PHASE1_RESEARCH_BASELINE_COMMIT = 891e4bd4b999eacc99431ed0db05062901a68dd9
PHASE2_IMPLEMENTATION_COMPARE_COMMIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0

ISOLATED_WORKSPACE_VERIFIED = TRUE
PRIMARY_WORKTREE_UNTOUCHED = TRUE

PHASE1_FROZEN = TRUE
PHASE1_SHA256 = f0e6d2499ee08dfe1610702a7493c2d00893e6d5c50236a573dfe1b88c307eb7
PHASE1_FREEZE_COMMIT = c6bbf180b1ace4c71a4958969267e6e0035fce96
PHASE1_REMOTE_CONFIRMED = TRUE

CURRENT_STATE_RECONSTRUCTION = Byul is a non-normative research track for
preserving and evaluating changing research memory. BYUL CORE-A keeps
mutability, derived/non-substantial entities, composition/emergence, and
conditional relationality visible without canonizing a formalism or scientific
claim. Current Petri/Event/Causal/LTS and R(S,M,L) directions are candidates;
provenance, preservation, reconstruction grade, lifecycle, and routing evidence
remain open.

STATE_CLASSIFICATION = SOURCE_SUPPORTED: complementary formalisms answer
different questions and transformations can lose meaning; OWNER_DIRECTION:
preserve succession, composition, situation sensitivity, and prior-art-first;
WORKING_HYPOTHESIS: preservation demand and complementary views may be central;
OPEN: minimal grammar, loss thresholds, routing value, and acceptance criteria;
NON_CONCLUSION: no canonical Petri/Causal/Event/primitive/universal model and no
automatic recovery; YOUR_INFERENCE: separate immutable evidence of what was
recorded from revisable interpretations and derived models.

MINIMAL_PROBLEM_DEFINITION = Deterministically reconstruct what was recorded,
by whom, from which source, scope, authority and epistemic state; expose how
every derived view was produced and what it lost; preserve conflict and
unknowns; and choose optional projections only under explicit preservation and
cost contracts.

PHASE1_PROPOSAL = Use an append-only bitemporal provenance ledger with
contracted projections: immutable source blobs, immutable typed research
events, and immutable transformation receipts are authoritative for recorded
history. Current state is a policy-versioned fold. Concurrent event sets may
converge by union, but semantic conflict requires an explicit attributed merge
decision. Specialized models remain regenerable views unless separately
promoted as non-derivable rule sources.

PRIOR_ART_BASIS = W3C PROV-DM for entity/activity/agent/derivation/revision and
invalidation; event sourcing for replayable state change; bitemporal databases
for valid versus recorded time; Git-style content-addressed immutable objects
and lineage; CRDTs only for convergent record-set storage; materialized-view
and data-provenance practice for dependency-tracked projections. This is a
prior-art composition, not a new theory.

AUTHORITATIVE_REPRESENTATION = Immutable source-byte blobs plus typed research
events plus transformation receipts. Authority means evidence of what the
research process recorded, not truth. Stable subject handles express succession
without claiming immutable substance.

DERIVED_REPRESENTATIONS = Current/open/non-conclusion dossier, bitemporal
history, provenance/argument graph, dependency/invalidation graph,
explicit-causal occurrence view, workload-specific behaviour/reachability
models, search indexes, and human snapshots. Every view carries source cutoff,
builder version, dependencies, freshness, loss grade, and validation evidence.

PRESERVATION_CONTRACT = Per meaning record authority source, required/actual
grade, verifier, allowed loss, recovery source, and invalidation dependency.
Preserve source bytes/digests, attribution, scope, epistemic/authority class,
unknown/non-conclusion, revision/retraction/contradiction, lineage, and receipt
metadata exactly. Do not claim semantic or approximate projections are exact.

LOSS_AND_NON_RECOVERABLE = Summaries cannot restore omitted qualifiers;
causal/reachability views cannot restore discarded rule, resource, label, or
conflict semantics; occurrences underdetermine behaviour; timestamps do not
recover causality; CRDT convergence is not semantic agreement; redaction/source
loss/key destruction and lossy migrations may be intentionally or permanently
non-recoverable.

TRANSFORMATION_PATHS = Source bytes to verified blob; blob to span-linked
reviewable claim events; events to deterministic state-at-cutoff; state/events
to contracted projection; projection to freshness/loss-labelled answer; old
schema to receipt-backed differential migration; verified snapshot to replayed
state. Never silently reverse a lossy projection into authority.

LIFECYCLE_BEHAVIOR = Mutation appends correction/supersession/retraction;
composition unions records with explicit interfaces; split includes provenance
closure; divergence retains a common frontier; merge retains both histories and
explicit decisions; migration dual-reads/replays; degraded mode marks views
stale/refuses unsafe answers; recovery verifies snapshot plus replay; successor
and retirement preserve readers or declare loss.

ROUTING_POSITION = R(S,M,L) is a useful research mnemonic but an insufficient
executable contract. Lower it to Plan(Q,P,A,L,C), separating workload,
per-meaning preservation, authoritative roots/cutoffs, lifecycle, and a
capability/cost/freshness/evidence catalog. The router chooses derived plans,
never truth, and refuses when obligations cannot be proven.

BYUL_CORE_A_ALIGNMENT = Append-only succession supports mutability; handles are
separate from event-specific entities; explicit composition retains local to
higher-scale lineage; scope/context/relations remain visible and no total order
is forced. This is a testable review claim, not automatic acceptance.

EXPECTED_FAILURE_MODES = Capture/schema overhead, incorrect claim atomization,
provenance mistaken for truth, replay cost, privacy/deletion conflicts,
unresolved-conflict growth, leaked total ordering, subject/content ID confusion,
stale projections, router cost or weak evidence, mishandled authoritative rules,
and cryptographic/schema/tool obsolescence.

FALSIFICATION_TESTS = Compare against Git plus raw Markdown; blind MI-1
reconstruction; retraction/revival and conflicting branches; transaction-order
shuffle causality trap; forced-loss reverse-synthesis refusal; full lifecycle
torture; corruption/staleness detection; S/M/L counterexamples; and scale tests
until a simpler baseline wins.

IMPLEMENTATION_TEST_PLAN = Under separate authorization only: implement the
smallest blob/event/receipt schema and deterministic fold; ingest exact pinned
memory with span links; add one provenance and one explicit workload projection;
property-test immutability, idempotence, replay, convergence, conflicts,
cutoffs, provenance closure, and refusal; then benchmark lifecycle semantics,
compute, maintenance, and reversibility against the current minimal baseline.

OPEN_UNKNOWNS = Atomic claims versus span bundles, minimal relation vocabulary,
valid-time use for non-temporal claims, semantic equivalence measurement,
promotion authority, privacy/redaction, actual need for concurrent writers,
workloads requiring formal projections, and router thresholds/domain transfer.

WHY_THIS_COULD_BE_WRONG = Git-versioned Markdown plus small explicit indexes may
be sufficient and safer. Structured capture can force ambiguous prose into
premature categories; PROV/bitemporal/event/CRDT machinery can exceed the
corpus's needs; and provenance preserves representation history, not meaning,
source quality, Owner intent, or theory validity.

PHASE2_CURRENT_V0_1_COMPARISON = Current v0.1 has good authority ordering,
derived views, UNKNOWN/REVIEW_REQUIRED behavior, no automatic principle PASS,
digest scaffolding, and 11 passing direct tests. It does not enforce its
declared source commit; its snapshot round-trip normalizes/omits source bytes;
it lacks change/branch/provenance receipts; routing is a static lookup that does
not use M; lifecycle/invalidation are filename simulations; and the documented
unittest command is not portable in the tested environment.

RECOMMENDED_DISPOSITION = RECOMMEND_MODIFY_CURRENT

MATERIAL_DELTAS_FROM_CURRENT = Enforce byte-exact pinned ingestion; add typed
bitemporal events and transformation receipts; make projections versioned and
dependency-backed; refine routing to Plan(Q,P,A,L,C); implement actual lifecycle
operations; and strengthen exactness, conflict, migration, adversarial, and
portable execution tests while retaining the useful current scaffold.

TOP_3_REASONS = 1) Exact source authority and raw reconstruction are currently
not enforced. 2) Evolving epistemic state, transformations, conflict, and
lifecycle cannot be reconstructed from normalized snapshot atoms. 3) A typed
preservation/evidence contract can extend the existing cautious views/router
without an unsupported wholesale replacement or canonical formalism.

CONFIDENCE = MEDIUM: exact static inspection and 11 direct tests support the
findings, but no corpus migration, representative lifecycle workload,
performance benchmark, semantic review study, or blind Owner comparison was
performed; the proposed machinery may be excessive for this corpus.

IMPLEMENTATION_PERFORMED = FALSE
IMPLEMENTATION_AUTHORITY = NONE
SHARED_IMPLEMENTATION_FILES_MODIFIED = FALSE
