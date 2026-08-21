# Phase 2 Read-Only Comparison — v0.1.12

EXACT_COMPARE_COMMIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0
PHASE1_REMOTE_CONFIRMED_BEFORE_READ = TRUE
PHASE1_UNCHANGED_AFTER_FREEZE = TRUE
PHASE2_USED_EXACT_PINNED_COMMIT = TRUE

## AGREEMENTS

- The implementation correctly treats the v0.01 memo corpus as primary data and derived indexes/views/router output as lower provenance authority.
- It retains source, line, section, syntactic kind, text, and explicit markers in `MemoryAtom`; it avoids unrestricted LLM reclassification.
- It keeps multiple views rather than declaring Petri, Causal Set, Event Structure, LTS, or another formalism canonical.
- Unknown intent and exact-metric requests fail to `REVIEW_REQUIRED` instead of inventing a model or metric source.
- Core Principles are exposed for review and never automatically PASS.
- `SituationFingerprint` includes a preservation map, `CurrentModelState` separates model metadata, and `LifecycleContext` names lifecycle phase.
- Virtual mutation is non-destructive, changes the derived content digest, names affected views, and reports an invalidation ratio.
- The code is a small stdlib-only experimental slice with clear non-normative/non-production status and a useful test scaffold.

## OBSERVED_GAPS

1. **Source preservation is not byte-exact.** `MemoryCorpus.load` uses `Path.read_text` (source line 169), which can normalize newline representation; `_parse_markdown` strips every line and discards blank lines (312-313). The authoritative snapshot stores atoms and a digest but not the original raw bytes (245 onward). `content_digest` normalizes whitespace. Consequently the implemented round-trip cannot reconstruct the exact source artifact it claims to preserve.
2. **The pinned source baseline is declarative, not enforced.** `SOURCE_BASELINE_COMMIT` is a constant (line 19), while `load` reads whichever files exist under the supplied/current directory. There is no Git-object read, manifest closure verification, per-file expected digest set, or failure when the directory differs from the named commit.
3. **No authoritative lifecycle ledger exists.** There are no immutable assertion versions, typed succession/correction/conflict relations, transition objects, commit/state manifests, reducer/schema pinning, checkpoints, or replay-versus-manifest verification.
4. **Epistemic classification is incomplete and heuristic.** Tags are substring markers over stripped lines. For example, any occurrence of `OPEN` can become an `OPEN` tag, so `Open Petri` may be confused with an open question. Source-supported, Owner-direction, hypothesis, inference, non-conclusion, scope, and authority are not first-class records.
5. **Preservation does not constrain general routing.** The router validates level names but consults only `preservation["history"] == "EXACT"` (line 366). Other field/relation demands do not select or reject transformations. There is no input preservation contract, loss composition, budget, capability inventory, or transformation receipt.
6. **Lifecycle phases are labels, not operations.** `LifecycleContext` has only `phase` and `mutation_scope` (line 145). Seven named phases share the same three validation labels (line 379); there are no preconditions/postconditions or compose/split/diverge/merge/migrate/degrade/recover/retire semantics.
7. **Invalidation is hard-coded.** `VIEW_DEPENDENCIES` is a filename table (line 33). Virtual mutation computes affected views from this table but does not update source digest, traverse transformation dependencies, invalidate downstream view versions, or perform recovery.
8. **Bidirectional transformation/reconstruction is absent.** Snapshot export has no import that recreates raw files; no lens laws, reverse synthesis classification, migration mapping, or non-recoverable receipt is implemented.
9. **History acyclicity is structurally trivial.** The history graph is manufactured as a linear chain from numbered chronology items, so its acyclicity test does not validate arbitrary causal/succession data.
10. **Branch and merge safety are untested.** There is no common-ancestor three-way merge, explicit conflict object, CRDT-safe subset, identity mapping for composition, or authorization boundary for semantic resolution.

## TEST_OR_STATIC_EVIDENCE

- Exact read-only export source: commit `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`; only the pinned implementation/test files and their pinned memo input tree were executed outside the repository.
- Runtime: Python 3.13.14 with bytecode writes disabled.
- Result: all 11 authored unit tests passed in 0.081 seconds.
- Passing coverage includes corpus/count loading, Core Principles view presence, normalized snapshot content digest, linear chronology acyclicity, known/unknown routing, exact-metric review, lifecycle validation labels, virtual mutation digest/invalidation ratio, and invalid preservation-level rejection.
- The round-trip test serializes/deserializes the in-memory snapshot and compares a normalized atom digest (test lines 35-43); it does not reproduce or byte-compare source files.
- No authored test pins or verifies `SOURCE_BASELINE_COMMIT`, exercises exact raw-byte closure, changes schemas/reducers, composes or splits histories, performs a merge/migration/recovery, checks cumulative drift, or proves bounded transitive invalidation.
- The first attempted `python -m unittest versions/v0.1/tests/test_byul_v01.py -v` invocation on Windows failed before collection because the slash path was treated as a module name. Direct execution of the pinned test file from the export root then ran all tests successfully; this invocation issue is not an implementation-test failure.

## MATERIAL_DELTAS_FROM_CURRENT

- Preserve the current parser/view/router/test scaffold, but place it behind an immutable content/assertion/transition/manifest ledger rather than treating the current filesystem parse as the authoritative state.
- Store exact bytes and source-span anchors; distinguish stable logical handle from immutable version digest.
- Replace normalized snapshot round-trip as the primary preservation claim with blob closure, exact export/import, pinned schema/reducer replay, and manifest comparison.
- Promote preservation to an explicit input contract and route with `Plan(Q,O,P,B,I)`; retain `R(S,M,L)` only as a compatibility adapter.
- Turn lifecycle names into operations with typed preconditions, outputs, loss receipts, conflict objects, rollback/recovery pointers, and dependency-driven invalidation.
- Keep Petri/Event/Causal/LTS and search/summarization as derived, versioned views with transformer and loss metadata.
- Add three-way semantic merge discipline; use CRDT convergence only for fields with proven algebraic safety.

## RECOMMENDED_DISPOSITION

RECOMMENDED_DISPOSITION = RECOMMEND_MODIFY_CURRENT

## WHY

The current v0.1 has the right experimental posture and reusable seams: exact-source intent, lower-authority derived views, explicit uncertainty, principle review, a model-agnostic situation input, non-destructive mutation, and tests. Replacing it wholesale would discard useful scaffolding. However its central preservation and lifecycle claims are currently much weaker than the research requirement: normalized atoms are not exact source reconstruction, a commit constant does not pin input, and lifecycle labels do not compose or recover state. The smallest credible successor is therefore a staged refactor of the authority and lifecycle core, not a cosmetic extension and not a new model-family commitment.

## UNCERTAINTY

- The comparison covers the exact required files and their authored tests, not workload-scale benchmarks or human reconstruction studies.
- The proposed ledger may be excessive if the corpus remains small and single-writer; disciplined Markdown plus Git could win on total cost.
- Claim granularity, semantic equivalence tests, conflict authority, retention/privacy duties, and actual concurrent editing needs remain open.
- No lifecycle prototype has measured receipt volume, replay cost, merge-review burden, or query gain.

IMPLEMENTATION_AUTHORITY = NONE
IMPLEMENTATION_PERFORMED = FALSE
