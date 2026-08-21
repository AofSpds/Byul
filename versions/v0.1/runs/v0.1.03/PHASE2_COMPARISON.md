# Phase 2 Exact-Commit Comparison

EXACT_COMPARE_COMMIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0

PHASE1_REMOTE_GATE_COMMIT = 428f5654798bf0a0d16f0140d4131f47e93f3722

PHASE1_REMOTE_CONFIRMED_BEFORE_PHASE2 = TRUE

PHASE1_UNCHANGED_AFTER_FREEZE = TRUE

IMPLEMENTATION_FILES_READ = versions/v0.1/README.md; versions/v0.1/MODEL_CONTRACT.md; versions/v0.1/data/SOURCE_MANIFEST.md; versions/v0.1/src/byul_v01.py; versions/v0.1/tests/test_byul_v01.py

PHASE2_MODE = READ_ONLY_ANALYSIS

## AGREEMENTS

1. The implementation correctly treats the v0.01 memory corpus as primary data and derived indexes/router output as lower provenance authority.
2. It separates a raw-memory plane from current/open/history/model-family/lifecycle/Core-Principles views, matching the Phase-1 authoritative-substrate/derived-projection direction.
3. It does not canonize Petri, Causal Set, Event/Mapping, or any one formalism.
4. It preserves UNKNOWN/unknown intent as `REVIEW_REQUIRED`, requires an external source for exact metrics, and does not auto-PASS natural-language Core Principles.
5. It records a source-baseline commit, document raw hashes, per-line provenance, view dependencies, preservation vocabulary, and a virtual invalidation probe. These are useful seeds rather than architecture that must be discarded.
6. Its stdlib-only scope and explicit experimental/non-normative status are appropriately small and cautious.

## OBSERVED_GAPS

1. **Pinned-source identity is asserted, not verified.** `MemoryCorpus.load()` reads the current filesystem glob, while `model_state()` always reports the constant `SOURCE_BASELINE_COMMIT`. A different corpus can therefore be labeled as the pinned baseline without any Git-object or manifest verification.
2. **“Raw round-trip” is not byte round-trip.** The snapshot stores atoms and a recorded `raw_sha256`, but not the raw bytes. `content_digest()` and `snapshot_content_digest()` hash normalized, non-empty atom text; whitespace, blank-line, newline, encoding, and other byte differences can collapse to the same digest. The test validates normalized atom content only.
3. **Epistemic classification is a substring heuristic.** `_explicit_tags()` marks any text containing `OPEN` as OPEN; consequently `Open Petri Net` is tagged `OPEN`. Similar marker heuristics cannot preserve source-supported/Owner-direction/hypothesis/non-conclusion distinctions reliably.
4. **Preservation contracts are not enforced.** The router validates that grade names exist but only reacts to `history=EXACT`. An `EXACT` demand for transformation semantics or other dimensions can return `ROUTE_CANDIDATE` without a matching capability or refusal.
5. **Views are unreceipted heuristics.** Outputs have no input checkpoint, projector/schema version, output digest, derivation receipt, loss declaration, staleness marker, or authority boundary in the returned object.
6. **Lifecycle behavior is mostly vocabulary.** Mutation is a deep-copied snapshot plus static file-to-view dependency lookup. Compose, split, divergent branches, semantic merge conflicts, migration, degraded recovery, successor, and retirement are not represented or tested.
7. **History acyclicity test is structurally weak.** The implementation turns an already ordered list into adjacent forward edges; that generated chain is acyclic by construction and does not validate research causality or detect source-order contradictions.
8. **Dependency coverage can be incomplete.** Static view dependencies silently ignore missing documents and do not verify that all data actually used by a projector is registered. `available_views` is reported even if a dependency is absent.
9. **View updates and reverse transformations are absent.** There is no proposal-event boundary, lens/round-trip law, conflict representation, or explicit `NON_RECOVERABLE` path for edits to derived views.
10. **The documented unittest command is not portable to this layout.** On the test environment, `python -m unittest versions/v0.1/tests/test_byul_v01.py` fails because `versions/v0.1...` is interpreted as an import path containing `v0.1`. Direct execution of the same exact test file succeeds.

## TEST_OR_STATIC_EVIDENCE

Exact read-only export:

- implementation and tests: Git objects from `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`;
- memory corpus used by the tests: Git objects from the implementation-declared source baseline `2a4529b69bc237125a1f012835d7a9b78ce3fec9`;
- all five exported implementation blobs were verified against their exact Git blob IDs;
- repository worktree remained clean; bytecode/cache writes were disabled.

Results:

- Documented command: `python -B -m unittest versions/v0.1/tests/test_byul_v01.py` -> FAIL before discovery with `ModuleNotFoundError: No module named 'versions/v0'`.
- Direct pinned test: `python -B .\\versions\\v0.1\\tests\\test_byul_v01.py` -> PASS, 11 tests, 0 failures, 0 errors, 0.088 seconds.
- Static/dynamic probe of the exact pinned module produced:
  - two byte-distinct Markdown inputs with different raw SHA-256 values -> the same `content_digest`;
  - snapshot contains `raw_sha256` but no raw bytes;
  - `_explicit_tags('Open Petri Net')` -> `('OPEN',)`;
  - an arbitrary tiny corpus still reports source commit `2a4529b...`;
  - `preservation={'transformation_semantics':'EXACT'}` with an unregistered lifecycle phase -> `ROUTE_CANDIDATE` with no transformation-semantics validation.

Passing the authored tests demonstrates that the implemented micro-slice behaves as those tests specify. It does not validate the stronger provenance, byte preservation, epistemic meaning, transformation, or lifecycle claims above.

## MATERIAL_DELTAS_FROM_CURRENT

1. Retain the current raw/derived split, but make the ground substrate an exact content-addressed evidence store plus append-only, schema-versioned epistemic event ledger.
2. Replace implicit marker extraction as authority with explicit, reviewable meaning capsules linked to exact spans; automated extraction may only propose.
3. Verify pinned source objects/digests at load time; never report a baseline solely from a constant.
4. Make every projector/transform emit a receipt with exact inputs, code/schema version, output digest, preservation matrix, dependencies, staleness, and known loss.
5. Compile `R(S,M,L)` into a capability-checked planner with first-class preservation, authority/loss catalog, lifecycle operation, cost bounds, and structured refusal.
6. Represent corrections, branch/split, divergent assumptions, typed merge conflicts, migrations, recovery, and successor/retirement as events rather than labels or simulated strings.
7. Preserve current guardrails: no automatic Core-Principles PASS, no metric fabrication, no canonical-formalism claim, and no escalation from a derived view to source authority.

RECOMMENDED_DISPOSITION = RECOMMEND_MODIFY_CURRENT

## WHY

The current implementation's central direction is compatible with Phase 1 and worth keeping: exact-source aspiration, raw-versus-derived authority, cautious routing, unknown preservation, static dependency seeds, and non-canonical formalism policy. Replacement would throw away useful alignment without evidence that a new stack is necessary.

Modification is nevertheless material. The implementation currently proves normalized atom replay and a few routing guardrails, not exact evidence preservation, trustworthy epistemic reconstruction, contract-safe transformations, or lifecycle composition. The smallest justified next trial is to harden the substrate and receipts first, compare against a disciplined Git+Markdown control, and add formal-model adapters only when a measured query requires them.

## UNCERTAINTY

- Phase 1's ledger/capsule/planner design is unimplemented and may be excessive for the corpus scale.
- Natural-language semantic preservation still needs human review; explicit capsules do not solve meaning automatically.
- The current source baseline and exact implementation were tested, but no production workloads, distributed writers, privacy constraints, or real branch/merge corpus were supplied.
- A simpler modification—exact Git-object loading, raw-byte snapshots, explicit metadata, and receipts—may deliver most benefit without a full event-store service or ATMS layer.

CONFIDENCE = MEDIUM-HIGH that current preservation and routing contracts need modification; MEDIUM that the complete CEEL-RP proposal is the best cost-adjusted architecture before comparative prototyping

IMPLEMENTATION_PERFORMED = FALSE

IMPLEMENTATION_AUTHORITY = NONE
