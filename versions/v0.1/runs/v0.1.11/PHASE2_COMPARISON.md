# Phase 2 Comparison — v0.1.11

## EXACT_COMPARE_COMMIT

`8e21fbdf597d38bb831834fc83cd3a53bcb180e0`

Only the required implementation files were inspected through exact Git-object reads from this commit. Tests were run from a temporary read-only export of this commit with bytecode writes disabled. No implementation file was edited.

## AGREEMENTS

- Raw research memory is assigned higher provenance authority than derived indexes, router output, or summaries.
- Derived views are explicitly non-authoritative and purpose-specific.
- The implementation avoids unconstrained LLM reclassification and limits tags to syntactic marker heuristics.
- Unknown intent, unknown fields, and exact metric requests can force `REVIEW_REQUIRED` rather than unsupported commitment.
- Core Principles are exposed for review but never receive automatic PASS.
- Preservation vocabulary includes `EXACT`, `ANCHORED`, `SEMANTIC`, `STATISTICAL`, `VIEW_DEPENDENT`, `NON_RECOVERABLE`, and `UNKNOWN`.
- The code pins a declared source baseline, records per-document SHA-256, provides snapshot/content digests, and models derived-view dependencies.
- Virtual mutation changes a digest, reports affected views, and gives an invalidation-radius seed.
- The implementation is deliberately experimental and does not claim Petri, Causal Set, Event/Mapping, or any derived view as canonical.

## OBSERVED_GAPS

1. **Exact-source preservation is not demonstrated.** `MemoryCorpus.load` reads the filesystem rather than verifying content against the declared Git commit. `_parse_markdown` drops blank lines and stores `stripped` lines; the snapshot contains atoms and a raw digest but not raw document bytes. `content_digest` normalizes whitespace and hashes only source plus normalized atom text. The round-trip test therefore proves normalized atom-text stability, not reconstruction of exact source files, provenance fields, tags, section structure, or line endings.
2. **Epistemic state is mostly search heuristics.** There is no first-class typed claim, support, correction, supersession, retraction, contradiction, scope, or non-conclusion lineage. `_explicit_tags` uses substrings, so terms such as “Open Petri” can be confused with epistemic OPEN depending on casing/content.
3. **The `R(S,M,L)` decomposition is not operationally validated.** The `model` argument is not used by `Router.route`. Preservation levels other than exact history are validated syntactically but do not influence the plan. Lifecycle phases only add a generic lifecycle view/check bundle for a hard-coded subset; unknown lifecycle strings are accepted. The router is primarily an intent-to-view lookup.
4. **Lifecycle operations are names, not semantics.** Compose, split, merge, migrate, recover, successor, and retire do not manipulate representations or preserve lineage. Virtual mutation deep-copies a snapshot and appends a synthetic atom; recovery is described as discarding the mutation.
5. **Invalidation is coarse and declared, not observed.** Dependencies are hard-coded by filename. Invalidation radius measures membership in this table, with no field/claim dependency receipts, no false-negative detection, and no incremental rebuild verification.
6. **Transformation loss is vocabulary only.** There is no transformation receipt, field-level contract enforcement, loss propagation, equivalence checker, reverse-synthesis grading, or capability descriptor for materializers.
7. **Several tests are weak by construction.** A chronology graph constructed only as consecutive forward edges is necessarily acyclic. Corpus count uses lower bounds rather than an exact manifest. The mutation test asserts only nonzero/bounded radius and one included view. No tampering, source-commit mismatch, conflicting merge, migration replay, stale-view, or transitive-loss test exists.

## TEST_OR_STATIC_EVIDENCE

- Pinned read-only test execution: `11 tests passed` in `0.139s` at compare commit `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`.
- Static evidence: `VERSIONS_DIR`/filesystem loading is not coupled to a Git-object verification step; `SOURCE_BASELINE_COMMIT` is metadata.
- Static evidence: `_parse_markdown` skips empty lines and stores stripped text.
- Static evidence: `content_digest` and `snapshot_content_digest` hash normalized atom text and source names, not exact files or all atom/provenance fields.
- Static evidence: `Router.route` never reads its `model` parameter.
- Static evidence: only `preservation["history"] == "EXACT"` affects routing; other declared preservation obligations do not.
- Static evidence: lifecycle-specific behavior is a list of validation labels; there are no lifecycle state-transition operations.
- Static evidence: `VIEW_DEPENDENCIES` is a static filename-to-view table.

Passing tests establish consistency with the current micro-contract, not semantic preservation, lifecycle completeness, or scientific/model validity.

## MATERIAL_DELTAS_FROM_CURRENT

- Replace the mutable-filesystem-as-input assumption with exact content-addressed evidence objects and verified source manifests/frontiers.
- Add an append-only typed epistemic operation ledger for claim succession, support, scope, correction, contradiction, split, compose, and merge.
- Preserve exact evidence bytes in authoritative snapshots; treat parsed atoms as derived data.
- Add transformation receipts with field-level guarantees, declared losses, transformer version, dependency set, and validation results.
- Move `M` and observed lifecycle state inside the planner at a pinned frontier; accept query intent, preservation contract, and operational constraints as external inputs.
- Register derived views/materializers by capability and loss profile; return `REVIEW_REQUIRED` when no path proves obligations.
- Replace filename-only invalidation with receipt/dependency-driven invalidation and false-negative tests.
- Implement branch/merge/migration/recovery semantics before claiming lifecycle coverage.
- Strengthen tests around exact byte round-trip, baseline tampering, epistemic corrections/conflicts, loss transitivity, deterministic replay, and migration.

## RECOMMENDED_DISPOSITION

`RECOMMEND_MODIFY_CURRENT`

## WHY

The current slice already has the right safety posture: raw-over-derived authority, no automatic principle PASS, explicit unknown/review behavior, preservation vocabulary, and a small stdlib-only testable core. Those foundations can be retained. However, its central claims are currently weaker than their names suggest: “raw round-trip” is a normalized atom digest, `R(S,M,L)` is not genuinely three-argument planning, and lifecycle support is a virtual invalidation sketch. The proposal therefore recommends evolving the slice into a content-addressed evidence-and-claim ledger with receipts and a capability planner, not discarding the entire codebase or implementing a model-family replacement.

## UNCERTAINTY

The comparison is strong about what the pinned code currently does, but the proposed ledger/planner has not been implemented or benchmarked. It may introduce excessive schema, receipt, replay, and conflict-review cost. A fuller `R(S,M,L)` implementation could also outperform the proposed boundary if future lifecycle intent cannot be derived from ledger state. Recommendation confidence is therefore `MEDIUM`, pending the falsification and implementation test plan in the frozen Phase 1 report.

## IMPLEMENTATION_AUTHORITY

`NONE`
