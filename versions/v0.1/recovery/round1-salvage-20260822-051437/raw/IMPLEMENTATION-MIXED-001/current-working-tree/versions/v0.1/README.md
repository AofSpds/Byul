# Byul v0.1 — Exact-Source Epistemic Memory Model

## Identity

- PROJECT: `AAA`
- PRODUCT: `ASSET AGENT ASA`
- ORIGIN_CHANNEL: `AAA-ASA-ME`
- VERSION: `v0.1`
- PREDECESSOR_RESEARCH: `versions/v0.01/`
- SOURCE_BASELINE_COMMIT: `2a4529b69bc237125a1f012835d7a9b78ce3fec9`
- STATUS: `EXPERIMENTAL_IMPLEMENTATION / NON_NORMATIVE / NOT_VALIDATED`
- OWNER_ACCEPTANCE: `NOT_PERFORMED`
- INDEPENDENT_VALIDATION: `NOT_PERFORMED`
- PRODUCTION_AUTHORIZED: `FALSE`

## Current implementation

v0.1 treats Byul research memory as its primary data. It now separates three
roles:

```text
Exact Git source tree
  raw bytes + SHA-256 + Git blob + byte anchors
                  |
                  v
Append-only epistemic ledger and lifecycle DAG
  claims + contexts + justifications + corrections + branch/merge lineage
                  |
                  v
Contracted derived views
  current/open/history/model/lifecycle/principle views + loss receipts
```

The exact source tree and recorded research actions are authoritative only for
what was stored or asserted. A claim record is not proof that the proposition is
true. Derived views never outrank their source.

## Exact-source boundary

Default ingestion reads the pinned Git tree, not the mutable working directory.
The machine-readable manifest is:

`data/source_manifest_v001.json`

It declares the exact 12 source paths, Git blob IDs, byte lengths, and SHA-256
digests at `2a4529b...`. Loading fails if the commit, file set, blob, length, or
digest differs. `12_PARALLEL_PROPOSAL_ROUND1.md`, which exists later in the
working tree, is therefore not silently mixed into this implementation target.

`--source-mode worktree --memory-root <path>` remains available for explicit worktree experiments. It is marked
`WORKING_TREE_UNPINNED`, and the safe planner fails closed when exact-baseline
authority is required.

Snapshots contain the original bytes as Base64 plus their hashes and exact
byte-range atoms. Import verifies all bytes, derived atoms, and the corpus digest.
The normalized search digest is separate and is never labeled raw fidelity.

## Epistemic ledger

`src/epistemic_ledger.py` provides:

- hash-chained append-only JSONL events;
- typed claim, context, and justification records;
- `SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `WORKING_HYPOTHESIS`, `OPEN`,
  `NON_CONCLUSION`, `YOUR_INFERENCE`, `UNKNOWN`, and corrected/retracted classes;
- separate valid time and transaction time;
- support/attack/refine/specialize/alternate/compose relations;
- explicit correction, supersession, review, transformation, and lifecycle events;
- immutable lifecycle commits with branch refs;
- persisted split, compose, conflict-preserving merge, migration, recovery, and
  retirement.

Merge performs union first and does not auto-resolve competing semantic variants.
Unknown fields survive schema migration under `PRESERVE_RAW` policy.

## Safe view planning

The earlier `R(S,M,L)` idea is implemented as a preservation-constrained planner:

`PLAN(Q,K,P,L)`

- `Q`: explicit question/intent.
- `K`: available authority, exact-baseline state, views, and invalidation state.
- `P`: field-level preservation demands.
- `L`: lifecycle and operational context.

Each transformation contract declares inputs, target views, guarantees, losses,
introduced interpretation, dependencies, inverse kind, and cost class. The
planner checks semantic admissibility before route selection. An unsupported
field such as `conflict=EXACT` through a chronology-only view returns
`REVIEW_REQUIRED`; it is not ignored.

Materialized views emit derivation receipts containing source/target digests,
contract and view-definition digests, guarantees, losses, dependencies, and
reverse classification.

## Core Principles boundary

The implementation keeps the current Byul principles visible:

- change/mutability;
- non-substantiality/derived entities;
- composition/emergence;
- conditional relationality.

It does not automatically validate their natural-language meaning and never emits
a scientific or Core-Principles PASS. The gate remains `REVIEW_REQUIRED`.

## Files

- `src/byul_v01.py` — exact corpus, derived views, integration, receipts, and CLI.
- `src/epistemic_ledger.py` — append-only epistemic records and lifecycle DAG.
- `src/transformation_contracts.py` — field-level contracts, loss composition, and safe planner.
- `src/transformation_contracts.py` — field-level contracts, composition, receipts, and safe planning.
- `data/source_manifest_v001.json` — exact machine-readable baseline manifest.
- `data/SOURCE_MANIFEST.md` — authority and ingestion contract.
- `MODEL_CONTRACT.md` — representation, preservation, routing, and lifecycle contract.
- `tests/test_byul_v01.py` — source/byte/view/planner regression tests.
- `tests/test_epistemic_ledger.py` — ledger, conflict, lifecycle, migration, and recovery tests.
- `tests/test_transformation_contracts.py` — admissibility, monotone loss, and receipt tests.
- `tests/test_cli.py` — documented snapshot and persisted-ledger command tests.

## Run

From the repository root:

```bash
python -B versions/v0.1/src/byul_v01.py summary
python -B versions/v0.1/src/byul_v01.py route --intent history --preserve history=EXACT
python -B versions/v0.1/src/byul_v01.py route --intent history --preserve conflict=EXACT
python -B versions/v0.1/src/byul_v01.py materialize --view OPEN_QUESTION_VIEW
python -B versions/v0.1/src/byul_v01.py simulate-mutation --source 10_ACTIVE_CHANNEL_LOG.md
python -B versions/v0.1/src/byul_v01.py export --out snapshot.json
python -B versions/v0.1/src/byul_v01.py verify-import --input snapshot.json
python -B -m unittest discover -s versions/v0.1/tests -p "test_*.py" -v
```

Minimal persisted-ledger example:

```bash
python -B versions/v0.1/src/byul_v01.py ledger-init --root ledger-demo --branch main
python -B versions/v0.1/src/byul_v01.py ledger-claim --root ledger-demo --branch main --claim-id q1 --text "Primitive remains open" --epistemic-class OPEN --actor owner
python -B versions/v0.1/src/byul_v01.py lifecycle-split --root ledger-demo --source main --target alternative
python -B versions/v0.1/src/byul_v01.py lifecycle-recover --root ledger-demo --branch main
```

## Experimental success criterion

Success means the implementation can prove which exact bytes it loaded, rebuild
the selected recorded state, trace every derived result, expose transformation
loss, preserve competing/unknown states, and fail closed when a requested semantic
guarantee is unavailable. Passing tests is implementation evidence only; it does
not establish scientific validation, owner acceptance, or production readiness.
