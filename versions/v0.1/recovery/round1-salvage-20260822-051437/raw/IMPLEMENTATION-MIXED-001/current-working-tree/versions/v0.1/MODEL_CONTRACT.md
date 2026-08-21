# Byul v0.1 Model Contract

## 0. Status

`EXPERIMENTAL / NON_NORMATIVE / NOT_VALIDATED`

This is an implementation contract. It does not replace AAA canonical
requirements and does not assert scientific truth, owner acceptance, or production
authorization.

## 1. Authority planes

### A0 — Exact evidence

Primary data is the exact Git tree:

- commit: `2a4529b69bc237125a1f012835d7a9b78ce3fec9`
- root: `versions/v0.01/memory`
- manifest: `data/source_manifest_v001.json`

The loader verifies the exact path set, Git blob IDs, byte lengths, and SHA-256
digests before parsing. Source artifacts retain:

- original bytes and encoding;
- raw SHA-256 and Git blob ID;
- baseline commit and manifest digest;
- exact line and byte-range anchors;
- syntactic structure and only explicitly visible marker tags.

The default source is the Git object database. A mutable working-tree glob is not
an exact baseline. Worktree mode must be requested explicitly and is labeled
unverified.

### A1 — Recorded epistemic actions

The append-only ledger is authoritative for the fact that an actor or process
recorded an action. It is not authoritative for universal truth.

Record types include:

- claim packet;
- context/assumption environment;
- justification hyperedge;
- classification, correction, supersession, retraction, and review;
- transformation and lifecycle action.

A claim packet carries exact text, optional structured form, polarity, epistemic
class, source anchors, context, assumptions, actor, valid time or `UNKNOWN`,
transaction time, and schema version. Event IDs form a verified append-only hash
chain.

Epistemic classes are:

- `SOURCE_SUPPORTED`
- `OWNER_DIRECTION`
- `WORKING_HYPOTHESIS`
- `OPEN`
- `NON_CONCLUSION`
- `YOUR_INFERENCE`
- `UNKNOWN`
- `RETRACTED_OR_CORRECTED`

Structured extraction from A0 is only a proposed derived result until a reviewed
A1 event adopts it.

### Derived plane

Current, open, history, model-family, lifecycle, principles, summary, causal,
Petri, Event Structure, LTS, metric, entity, persona, embedding, and routing
representations are derived unless separately authored and assigned a narrow
authority scope. Deleting them must not destroy A0/A1 reconstructability.

## 2. Exactness and digests

`raw_sha256` hashes each original file. `content_digest` hashes the ordered,
length-delimited source names and original bytes. `normalized_digest` supports search/index
comparison and is never evidence of byte fidelity.

Snapshot schema v2 stores original bytes as Base64. Import must verify:

1. every raw digest;
2. deterministic atom derivation and byte anchors;
3. the corpus digest;
4. byte equality after restoration.

Any formatting, blank-line, whitespace, or newline change changes the raw digest,
even when normalized text remains equivalent.

## 3. Transformation contracts and receipts

Every derived view has a versioned contract declaring:

- required source artifacts;
- target view(s);
- field-level guarantees;
- dropped semantics;
- introduced interpretation;
- dependency set;
- inverse/replay class;
- operational cost class.

Preservation vocabulary:

- `EXACT`
- `ANCHORED`
- `SEMANTIC`
- `APPROXIMATE`
- `STATISTICAL`
- `VIEW_DEPENDENT`
- `NON_RECOVERABLE`
- `UNKNOWN`

The receipt contains contract/version/digest, source and target digest,
view-definition digest, guarantees, losses, introduced values, dependencies,
inverse kind, and validation result. `CONTRACT_CHECKED` means the implementation
checked the declared contract mechanics; it is not scientific PASS.

Loss is monotone across a composed path. A downstream transform cannot restore a
discarded field unless an independent authoritative source or retained witness is
explicitly used. Reverse compatibility is claimed only for exact replay, an
implemented inverse, or a tested lens on its declared domain.

## 4. PLAN(Q,K,P,L)

Routing is a safe view-planning problem:

- `Q`: explicit question or workload intent;
- `K`: source authority, available views, exact-baseline status, and invalidation
  state;
- `P`: field-level preservation/loss demand;
- `L`: lifecycle and operational context.

Semantic admissibility is checked before cost. Every demanded field must be
provided at an allowed grade. Unknown questions, unknown fields, unverified source
mode, missing metric/clock authority, or unmet preservation demands yield
`REVIEW_REQUIRED` with an explicit unmet-demand list.

The earlier `R(S,M,L)` remains compatible as shorthand only if the situation
contains explicit question and preservation demand and the model state contains
epistemic authority. A Situation Fingerprint is derived routing input, not source
authority.

## 5. Lifecycle contract

Lifecycle commits are immutable content-addressed records. Mutable branch refs
select heads but never erase commits.

- **CREATE:** create an initial branch head over selected ledger events.
- **MUTATE:** append events and a successor commit.
- **COMPOSE:** union selected events, retain all parents, record interface mappings,
  and expose conflicts.
- **SPLIT:** share a parent, optionally record an explicit exclusion manifest.
- **MERGE:** union first; do not last-write-win semantic variants; record competing
  active claims for review.
- **MIGRATE:** retain source parent/events, transformer version, target schema, and
  `PRESERVE_RAW` policy for unknown fields.
- **DEGRADED:** expose missing event/dependency IDs rather than fabricating state.
- **RECOVER:** verify commits and event chain, replay selected events, and report a
  state root plus unresolved conflicts.
- **RETIRE/SUCCESSOR:** record successor and unresolved loss while keeping the
  predecessor readable.

Automatic merge is allowed only for operations with a separately proven algebra.
The current implementation performs no automatic semantic conflict resolution.

## 6. Dependency and invalidation contract

Every view declares source dependencies. Mutation invalidates every directly
dependent view plus its recorded transitive projection closure. The current
Markdown slice records source-to-view dependencies; future transforms must add
view-to-view edges before claiming incremental invalidation.

Global invalidation is valid when the view definition has global dependencies.
An unexpectedly small radius is not automatically better and may indicate a
missing dependency.

## 7. Core Principles review

The implementation must review compatibility with:

- change/mutability;
- non-substantiality/derived entities;
- composition/emergence;
- conditional relationality.

Content-addressed immutability is an audit identity, not an ontological substance.
Stable IDs are handles. Contexts and conflicts remain scoped. Parentage and
justification preserve composition lineage. No natural-language principle receives
automatic PASS.

## 8. Experimental acceptance

The automated suite must verify at least:

1. exact file set, commit, blob, byte length, and SHA-256;
2. byte-for-byte snapshot export/import and tamper detection;
3. exact source anchors;
4. explicit worktree-unverified failure behavior;
5. admissible and rejected preservation demands;
6. derivation receipts and disclosed losses;
7. append-only ledger replay and tamper detection;
8. separate valid/transaction time;
9. correction without predecessor destruction;
10. conflict-preserving split/compose/merge;
11. migration, recovery, retirement, and readable predecessors;
12. dependency-closure invalidation.

Passing these tests is implementation evidence only. It is not scientific/model
validation, independent review, owner acceptance, or production approval.
