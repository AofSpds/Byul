# Phase 2 Read-Only Comparison — v0.1.08

EXACT_COMPARE_COMMIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`

PHASE1_REMOTE_CONFIRMED_BEFORE_READ = `TRUE`

PHASE1_FREEZE_COMMIT = `a8a4a0803de7351030bcced5d894fa28f2140d3a`

PHASE1_SHA256 = `9c283878bc86fc85a607ffaf613a7f630656f9e8df4c36606bfb546cc29ceda9`

PHASE1_UNCHANGED_BEFORE_AND_AFTER_COMPARISON = `TRUE`

IMPLEMENTATION_AUTHORITY = `NONE`

IMPLEMENTATION_PERFORMED = `FALSE`

## AGREEMENTS

The pinned v0.1 and the blind Phase-1 proposal agree on several important boundaries.

1. **Raw source outranks derived views.** The README, model contract, and source manifest explicitly keep the Markdown corpus above indexes, routing output, and summaries in provenance authority.
2. **No formalism is canonical.** The implementation does not promote Petri, Causal Set, Event, Mapping, or another candidate to a universal world model.
3. **Uncertainty is not silently filled.** Unknown intent, unknown fields, and exact-metric requests are routed to `REVIEW_REQUIRED` or an external-source requirement.
4. **Core principles do not auto-pass.** The router returns `CORE_PRINCIPLE_REVIEW` and a constant `REVIEW_REQUIRED` principle state rather than claiming natural-language verification.
5. **Derived views are purpose-specific.** History, current/open, model-family, lifecycle, and principles are separated instead of being presented as one canonical representation.
6. **Lifecycle cost is at least visible.** Virtual mutation changes a digest, names affected views, and computes a coarse invalidation radius without editing the source files.
7. **The implementation is modest about its status.** All required documents label the slice experimental, non-normative, not validated, and not production-authorized.

These agreements make the current slice a useful prototype and migration source rather than something that should be discarded wholesale.

## OBSERVED_GAPS

### 1. Claimed raw/exact preservation is not reconstructive

`MemoryCorpus.load()` computes a per-document `raw_sha256`, but `_parse_markdown()` stores only non-empty `line.strip()` values. Blank lines, leading/trailing whitespace, original newline form, and some layout distinctions are discarded. `snapshot()` exports the digest and parsed atoms, not the raw document bytes. Therefore an exported snapshot can detect that a known raw file differed, but cannot reconstruct the raw file it claims to preserve.

`content_digest()` and `snapshot_content_digest()` both normalize whitespace again and hash `(source, normalized atom text)`. The round-trip test compares these two derived digests. It does not compare raw bytes, canonical document serialization, or the stored `raw_sha256` values after an import. The CLI has an `export` command but no import path.

### 2. The exact source baseline is declared but not enforced

`SOURCE_BASELINE_COMMIT` is a string constant. `MemoryCorpus.load()` reads `DEFAULT_MEMORY_ROOT` from the filesystem with `glob("*.md")`; it does not read Git objects from the declared commit, require an exact manifest of paths/digests, or reject extra/missing changed files. The test only requires at least 12 documents and more than 100 atoms. Running the same code in a later worktree can therefore mix a newer corpus with the old baseline identifier.

### 3. Epistemic state remains substring search, not a preserved state machine

`_explicit_tags()` uses substring checks for markers. `CURRENT_STATE_VIEW` searches words such as `current`, `현재`, `strongest`, and `방향`; `OPEN_QUESTION_VIEW` searches tags/text. This is conservative compared with free-form LLM inference, but it cannot represent explicit assertion identity, scope, support, contradiction, qualification, supersession, retraction, or correction. Historical mentions and corrected statements can appear in a “current” result simply because they contain a keyword.

### 4. Provenance is too thin for transformation accountability

Atoms retain filename, line number, section, syntactic kind, text, and tags. There is no agent/role, evidence span object, valid time vs recorded time, source commit per artifact, derivation activity, transform version, parameter set, loss declaration, validation receipt, or policy version. Derived outputs therefore cannot explain their complete transformation path.

### 5. `R(S,M,L)` is mostly an interface shape

`Router.route()` accepts `model` but never reads it. It recognizes only `preservation["history"] == "EXACT"`; every other preservation field/level is merely syntactically validated and ignored. `LifecycleContext.mutation_scope` is unused. Lifecycle values are not validated, and the listed mutate/compose/split/merge/migrate/recover phases only add generic validation names and the lifecycle view.

Consequently the router does not yet select based on available representation, freshness, lineage, loss state, scale, cost, or capabilities. It cannot prove that a target view satisfies the requested preservation demand.

### 6. Lifecycle operations are not modeled

There is no append-only change ledger, predecessor/successor relation, branch, merge conflict, schema migration record, composition boundary, split closure, rollback, or recovery reconstruction. The virtual mutation deep-copies a snapshot and appends an atom, but does not update the document `raw_sha256`; the simulated snapshot is internally inconsistent if interpreted as raw authority. “Recovery” is a returned string saying the virtual copy can be discarded, not a verified rebuild.

### 7. Invalidation and tests are file-name heuristics

`VIEW_DEPENDENCIES` is a static filename map. Invalidation does not follow actual atom/claim/derivation dependencies, and `RAW_CORPUS` is always affected. The invalidation-radius test checks only that a ratio lies in `(0,1]` for one file and that one expected view is named. It does not test false-negative or false-positive invalidation.

The chronology acyclicity test is weak because `history_edges()` constructs a simple consecutive list; barring identifier aliasing, that construction is acyclic by definition. The tests do not exercise contradictory branches, status correction, source-baseline mismatch, raw reconstruction, migration, compose/split/merge, cumulative drift, or reverse synthesis.

### 8. Operational handles risk being mistaken for semantic identity

`atom_id` is the first 20 hex characters of a hash over source, normalized text, and duplicate occurrence count. Whitespace-only edits intentionally collapse, while insertion/reordering of duplicate lines can change occurrence identities. No explicit identity policy says when two atoms are the same claim, new occurrences, or merely textually equivalent.

## TEST_OR_STATIC_EVIDENCE

EVIDENCE_KIND = `STATIC_READ_ONLY_ANALYSIS`

The five mandated files were read only through `git cat-file` from the exact compare commit. No working-tree v0.1 file, recovery implementation, mixed trial, or other run was used.

Dynamic test execution was not required to establish the gaps above and was deliberately not mixed with an unpinned working-tree memory corpus. The test source itself was inspected. The following observations are direct from the pinned code/tests:

- `MemoryCorpus.load()` uses `Path.glob` and `Path.read_text` on the filesystem, while the baseline commit constant is never used for loading or verification.
- `_parse_markdown()` skips empty lines and stores `line.strip()`.
- `snapshot()` omits raw document text; `snapshot_content_digest()` ignores stored raw digests.
- `test_raw_snapshot_roundtrip_content_digest` compares normalized atom-derived digests.
- `Router.route()` never dereferences its `model` argument.
- Preservation logic has a single special case for exact history.
- The lifecycle test checks the presence of validation labels, not mutation lineage or recovery.
- The exact-source test uses lower bounds rather than an exact path/digest manifest.

These are architectural/static findings; they do not claim runtime failure of the eleven authored micro-tests.

## MATERIAL_DELTAS_FROM_CURRENT

The Phase-1 proposal would retain the current parser and simple views as prototype adapters but change the authority and lifecycle layers materially.

| Concern | Pinned v0.1 | Phase-1 proposal |
|---|---|---|
| Source authority | live filesystem Markdown plus declared commit string | immutable evidence bytes/locators with exact digest manifest and commit-bound ingest |
| Structured state | normalized lines and marker tags | typed assertion/change events with scope, epistemic class, authority, evidence refs |
| Change | virtual copied snapshot | append-only assert/qualify/supersede/retract/open/resolve events |
| Time | line order/chronology | recorded time plus valid time/unknown, and explicit causal relation only |
| Provenance | source/line/section | evidence, agent, derivation activity, transform version, loss and validation receipt |
| Current state | substring-filtered view | deterministic fold over snapshot plus versioned resolver policy |
| Routing | `R(S,M,L)` shape, hard-coded intent map | `Plan(Q,O,A,C,L)` capability/obligation planner; `R(S,M,L)` retained as intake shorthand |
| Preservation | enum validation and exact-history special case | field/relation obligations composed across every transformation |
| Lifecycle | labels and one virtual mutation | branch, compose, split, merge conflict, migrate, recover, successor/retire records |
| Reverse/reconstruction | normalized snapshot digest | exact/complement-assisted/synthesis/none contract with explicit non-recoverable loss |
| Tests | eleven micro-tests | raw-byte reconstruction, corrections, contradictory branches, loss injection, invalidation precision, cold recovery, router counterfactuals |

## RECOMMENDED_DISPOSITION

RECOMMENDED_DISPOSITION = `RECOMMEND_MODIFY_CURRENT`

IMPLEMENTATION_AUTHORITY = `NONE`

## WHY

The current v0.1 is a disciplined and useful seed: it preserves source location, avoids unsupported semantic classification, exposes multiple views, fails unknown requests to review, and does not auto-pass Core-A. Those pieces can remain.

However, its stated success criterion centers on preservation, mutation, routing, and reconstruction, while its current data model cannot reconstruct raw source, represent corrections/branches, account for derivations, or use most routing inputs. These are not merely additional features; they are the semantic safety mechanisms needed for the research question.

Modification is preferred over replacement because the existing stdlib parser, view vocabulary, route output shape, CLI, and micro-tests can be adapted into ingestion/projection components. The authority layer should move from normalized atoms alone to evidence + assertion/change + derivation + commit records, and the router should become a contract checker rather than a filename/intent selector.

This recommendation is advice only. It does not authorize changing any current file.

## UNCERTAINTY

CONFIDENCE = `MEDIUM`

The static gaps are high-confidence observations from the exact pinned code. The architectural recommendation is medium-confidence because no comparative implementation or benchmark has yet shown that the added ledger and contract machinery improves reconstruction fidelity enough to justify its complexity. A smaller Markdown+Git convention may outperform it operationally at current scale. The proposed modification must therefore be tested as a separately authorized trial and compared against the current minimal slice.

IMPLEMENTATION_PERFORMED = `FALSE`

IMPLEMENTATION_AUTHORITY = `NONE`

