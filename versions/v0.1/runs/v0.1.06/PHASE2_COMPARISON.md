# PHASE 2 — Exact Read-Only Comparison

EXACT_COMPARE_COMMIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`

COMPARE_METHOD = `EXACT_GIT_OBJECT_READS + TEMPORARY_READ_ONLY_EXACT-COMMIT_EXPORT`

PHASE1_REMOTE_GATE_PASSED = `TRUE`

PHASE1_FREEZE_COMMIT = `4ae448994e3f7ae1f6a76c6ceff4bc68547ae7c4`

PHASE1_SHA256_BEFORE_COMPARISON = `f8da0cc50ca10f71c48c663b6e068472bdf6552c1f1e3f9dd70b92b23067d622`

IMPLEMENTATION_EDITED = `FALSE`

## AGREEMENTS

The pinned v0.1 implementation and the frozen proposal agree on several important foundations:

- Raw research memory has greater provenance authority than derived indexes, router recommendations, or summaries.
- Derived views must not replace source memory or manufacture scientific truth.
- Source baseline identity, source path, line number, section, syntactic kind, and text provenance are relevant.
- Explicit UNKNOWN and unfamiliar intent should produce `REVIEW_REQUIRED`, not invented model commitment.
- Exact metric requests need an external authoritative metric/clock source.
- BYUL CORE-A does not force a formalism and must not receive an automatic PASS.
- `R(S,M,L)` is a useful first routing vocabulary; model names are not situation inputs.
- Lifecycle vocabulary and invalidation radius belong in the experimental scope.
- Exact/anchored/semantic/statistical/view-dependent/non-recoverable/unknown grades are useful.
- The implementation is correctly labeled experimental, non-normative, unvalidated, and non-production.

These agreements make an evolutionary modification more defensible than a total rewrite from an unrelated basis.

## OBSERVED_GAPS

### 1. The exact source baseline is declared but not enforced

`SOURCE_BASELINE_COMMIT` is a constant, while `MemoryCorpus.load()` reads `DEFAULT_MEMORY_ROOT` from the current filesystem using `glob("*.md")`. It does not read Git objects from the declared commit, verify a manifest of expected paths/hashes, or reject a dirty/divergent corpus. `CurrentModelState` can therefore report the pinned commit even when the bytes came from another state.

### 2. The tested round trip is not byte-exact raw preservation

Files are read with `Path.read_text`, which normalizes platform newlines. Parsing drops blank lines and strips leading/trailing whitespace. `content_digest()` applies `_norm()`, collapsing all whitespace. `snapshot()` stores `raw_sha256` and parsed atoms, but not the raw bytes/text needed to reconstruct the source. `snapshot_content_digest()` recomputes only from normalized atom text and does not validate `raw_sha256`.

Consequently, the passing `test_raw_snapshot_roundtrip_content_digest` proves stability of a normalized atom projection, not byte-exact source export/import. Blank lines, line endings, spacing, and some formatting can change without failing that test.

### 3. Epistemic classification is too weak and can be false-positive

`_explicit_tags()` uses substring heuristics. For example, `"OPEN" in upper` also tags lines containing `Open Petri` as epistemically OPEN. The implemented tags do not represent the required distinctions among source-supported material, Owner direction, working hypothesis, explicit non-conclusion, and the system's own inference. There are no revision, retraction, supersession, conflict, or authority-scope records.

### 4. There is no authoritative change/decision history

The authoritative state is a mutable directory plus parsed documents. The only history edges are a synthetic linear chain over numbered items in one chronology memo. There is no append-only event ledger, causal parent graph, branch/head/freeze identity, semantic merge, provenance activity, or correction lineage. The current test for acyclicity is therefore a check on a constructed list, not on actual research-state causality.

### 5. Preservation levels do not constrain most routing

`SituationFingerprint.validate()` checks that level names are known, but `Router.route()` consults only `preservation["history"] == "EXACT"`. Other semantic fields and grades have no effect. The `model` parameter is unused; `mutation_scope` is unused; lifecycle values are not validated; lifecycle phases only add a fixed view/check list. There is no transformation catalog, guarantee composition, loss report, feasibility proof, or cost comparison.

### 6. Transformations and views lack reproducibility receipts

Views are file lists and keyword filters without projector version, input-head identity, output digest, transform receipt, field-level loss, dependency receipts, or independent rebuild comparison. Snapshot JSON is not canonicalized or schema-versioned. Import/recovery is not implemented; export only writes a JSON projection.

### 7. Lifecycle simulation is narrower than its labels

Virtual mutation deep-copies an in-memory snapshot, appends a synthetic atom, and uses a static file-to-view map for invalidation. It does not exercise compose, split, divergence, merge, migration, degraded recovery, successor freeze, schema evolution, conflict preservation, or cumulative semantic drift.

### 8. The tests are valuable but shallow

All tests use the default mutable memory directory and assert broad properties such as `document_count >= 12`, rather than an expected path/hash manifest from the declared source commit. The routing tests confirm conservative fallback and fixed validation labels, but do not prove the labels were executed. There are no negative corruption tests, independent replay tests, incremental-versus-full comparisons, or semantic-loss fixtures.

## TEST_OR_STATIC_EVIDENCE

- The five required implementation files were read only from `8e21fbdf597d38bb831834fc83cd3a53bcb180e0` using exact Git-object reads.
- The implementation and test plus the exact commit's `versions/v0.01/memory` corpus were exported to a separate temporary directory. All exported files were marked read-only and Python bytecode writes were disabled.
- Result: `11 tests run / 11 passed / 0 failed / 0 errors` in approximately `0.049s`.
- No runtime write (`__pycache__` or implementation mutation) was observed in the export.
- Static evidence: `content_digest()` hashes normalized atom rows; `snapshot()` omits raw source bytes; `snapshot_content_digest()` trusts atom payloads; `Router.route()` uses only the history preservation field; `MemoryCorpus.load()` reads a working-tree path rather than the declared commit.

Passing these tests confirms that the intended minimal implementation behaves as authored. It does not invalidate the gaps because the tests do not assert the stronger preservation and lifecycle claims.

## MATERIAL_DELTAS_FROM_CURRENT

1. Make immutable exact artifacts plus append-only semantic records the authority; retain the current document/atom views as projections.
2. Enforce the source baseline with exact Git-object reads or a path/hash manifest, and refuse mismatch.
3. Preserve source bytes independently of normalized atoms; distinguish byte digest, structured projection digest, and semantic claims.
4. Add first-class classification, revision, retraction, supersession, conflict, causal parents, branch/freeze, and provenance scope.
5. Replace label-only preservation with field/relation-level transform contracts, receipts, weakest-link composition, and fail-closed feasibility.
6. Version projector code/input heads/policies; make materialized views disposable and independently rebuildable.
7. Expand lifecycle tests to branch/merge/split/migrate/recover/successor, schema evolution, corruption, drift, and full-versus-incremental replay.
8. Keep the conservative null route and CORE-A review discipline; do not auto-select a canonical formalism.

## RECOMMENDED_DISPOSITION

`RECOMMEND_MODIFY_CURRENT`

## WHY

The current v0.1 is directionally aligned and intentionally minimal, so replacing every concept would discard useful conservative choices. However, its present authority and round-trip mechanism cannot satisfy the stronger requirement to reconstruct evolving research state without semantic or byte loss. The most defensible next trial is a bounded modification that keeps the raw/derived hierarchy, conservative routing, and non-automatic CORE-A review while introducing exact source pinning, append-only decision lineage, and executable preservation contracts.

This recommendation is advice only. It does not authorize any code or implementation change.

## UNCERTAINTY

`MEDIUM`

The exact-code evidence makes the preservation gaps high-confidence. The full ledger architecture remains a proposal: it may be heavier than necessary, semantic-equivalence checks for prose remain difficult, and a simpler Git-plus-manifest design could win the falsification tests. Comparative review should distinguish confidence that modification is needed from confidence that every proposed mechanism is needed.

IMPLEMENTATION_AUTHORITY = `NONE`

IMPLEMENTATION_PERFORMED = `FALSE`
