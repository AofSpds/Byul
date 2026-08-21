# Phase 2 Exact-Commit Comparison — v0.1.04

EXACT_COMPARE_COMMIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`

COMPARE_MODE = `READ_ONLY_GIT_OBJECTS_PLUS_READ_ONLY_ARCHIVE_OF_THE_EXACT_COMMIT`

PHASE1_REMOTE_CONFIRMED_BEFORE_COMPARE = `TRUE`

PHASE1_UNCHANGED_AFTER_FREEZE = `TRUE`

IMPLEMENTATION_PERFORMED = `FALSE`

## AGREEMENTS

The pinned v0.1 implementation already establishes several sound foundations that should be retained:

- raw research memory is ranked above derived indexes, routing recommendations, and summaries;
- v0.1 is explicitly experimental, non-normative, unvalidated, and not production-authorized;
- exact source commit metadata is declared;
- source path, line number, section, syntactic kind, text, and explicit marker tags are captured as a small provenance seed;
- current, history, open-question, model-family, lifecycle, and CORE-A-oriented views are separated from the source plane;
- unknown intent, exact-metric demand without a source, and unknown fields lead toward `REVIEW_REQUIRED` rather than an invented model commitment;
- Core Principles do not automatically produce PASS and do not force Petri, Causal Set, Event Structure, LTS, or another formalism;
- preservation levels, virtual mutation, dependency-based invalidation, snapshot export, and lifecycle vocabulary are useful executable seeds;
- the implementation is stdlib-only, compact, legible, and suitable for a first experiment.

These agreements mean the Phase-1 VEPL proposal can evolve the current slice rather than discarding its useful raw/derived split and fail-closed intent.

## OBSERVED_GAPS

### 1. Declared source pin is metadata, not an enforced input

`SOURCE_BASELINE_COMMIT` is returned in `CurrentModelState`, but `MemoryCorpus.load()` reads `DEFAULT_MEMORY_ROOT` from the active filesystem. It neither reads Git objects from the declared commit nor verifies a tree/file digest manifest. At the compare commit, the memory tree differs from the declared source baseline: `12_PARALLEL_PROPOSAL_ROUND1.md` and `13_ROUND1_ACCIDENTAL_IMPLEMENTATION_INCIDENT.md` are additional paths. The tests still pass because they require only `document_count >= 12`. Thus a runtime can label drifted input with the pinned commit ID.

### 2. “Raw round trip” does not reconstruct raw source

The snapshot stores `raw_sha256` and parsed atoms, but not raw bytes or raw text. `_parse_markdown()` drops blank lines and leading/trailing whitespace, and `content_digest()` normalizes all whitespace. `snapshot_content_digest()` ignores `raw_sha256`, line number, section, kind, tags, and provenance fields. The passing round-trip test therefore proves equality of normalized atom text/order, not exact artifact reconstruction.

### 3. Epistemic and transformation provenance are too thin

Atoms lack immutable source revision, agent, assertion activity, schema/transform version, evidence-span digest, correction/retraction/supersession, contradiction, scope, branch ancestry, and merge state. File/line provenance is useful but cannot represent research-state succession or distinguish a tool extraction from an adopted judgment.

### 4. Explicit-tag parsing creates semantic false positives

`_explicit_tags()` performs substring checks. Existing phrases containing “Open Petri” or “open-boundary” are tagged `OPEN`; the exact corpus produced seven such candidates in the probe. Similar lexical heuristics can confuse mention, negation, headings, and epistemic status.

### 5. Router validates vocabulary but not capability

The router's `model` parameter is unused. Replacing `available_views` with an empty tuple yielded the same route plan. Most preservation demands are accepted syntactically but ignored; only `history=EXACT` has a special branch, and even that adds a validation name without establishing satisfaction. Unknown lifecycle phases are accepted and can return `ROUTE_CANDIDATE`. There is no per-view capability/loss matrix, input-cut freshness check, cost comparison, or path composition.

### 6. Lifecycle behavior is simulated, not represented

Virtual mutation deep-copies an in-memory snapshot, appends an atom, and computes affected hard-coded views. There are no append-only revisions, compensating corrections, compose/split/diverge/merge commits, migrations, transformer lineage, recovery replay, or successor/retirement receipts. `invalidation_radius` is a ratio over a static dependency table, not an observed lifecycle metric.

### 7. Several tests validate construction rather than the promised semantic property

The chronology graph is made as a linear chain from a numbered list, so acyclicity is largely guaranteed by construction. Current/open views are keyword/file filters without precision/recall or authority-escalation tests. The suite lacks negative tests for source drift, exact raw reconstruction, false tags, unavailable views, invalid lifecycle states, repeated migrations, merge conflict retention, and cumulative semantic loss.

### 8. Documented test invocation is not portable to this Windows checkout

The README command `python -m unittest versions/v0.1/tests/test_byul_v01.py` failed because the dotted directory name was treated as an import path (`ModuleNotFoundError: No module named 'versions.v0'`). Direct execution of the exact same pinned test file succeeded.

## TEST_OR_STATIC_EVIDENCE

All evidence below came from a read-only archive of commit `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`, with Python bytecode writes disabled.

- Documented unittest invocation: `EXIT 1`, import-path failure on Windows.
- Direct pinned test execution: `11 tests`, all passed in approximately `0.049s`.
- Probe: `DIGEST_IGNORES_RAW_SHA256=True`.
- Probe: `DIGEST_IGNORES_SURROUNDING_WHITESPACE=True`.
- Probe: `SNAPSHOT_HAS_RAW_TEXT=False`.
- Probe: `FALSE_OPEN_TAG_CANDIDATES=7`.
- Probe: `ROUTE_IGNORES_AVAILABLE_VIEWS=True`.
- Probe: `UNKNOWN_LIFECYCLE_DECISION=ROUTE_CANDIDATE`.
- Git-object comparison: declared source memory tree `6294e77ce410a817e8562019ec6db1438cbe2700`; compare-commit memory tree `ddb3e8f1c6deac880f7a29eee78711f256bc8a7c`; two added memory paths.

Passing tests demonstrate that the intended minimal behaviors execute; they do not close the static gaps above and do not constitute Owner Acceptance or scientific validation.

## MATERIAL_DELTAS_FROM_CURRENT

1. **Authority/write model:** current Markdown filesystem parsing → immutable evidence blobs plus append-only epistemic/provenance revisions and commit ancestry.
2. **Exactness:** normalized atom-text digest → byte-preserving source bundle, manifest verification, exact input commit/tree enforcement, and domain-specific semantic oracles.
3. **Provenance:** source/file/line → agent/activity/schema/transform/contract/evidence-span/revision/branch/merge lineage.
4. **Routing:** intent-to-hard-coded-view lookup → constraint planning across capability and loss matrices, pinned cuts, lifecycle state, and measured costs.
5. **Lifecycle:** virtual deep-copy mutation → durable correction, branch, merge, migration, recovery, and successor events with retained conflicts and rollback boundaries.
6. **Testing:** positive micro-tests → adversarial preservation, drift, false-tag, unavailable-capability, cumulative-loss, conflict-retention, and rebuild tests against a simpler baseline.

## RECOMMENDED_DISPOSITION

`RECOMMEND_MODIFY_CURRENT`

## WHY

The current implementation's raw/derived authority split, conservative review behavior, and minimal executable scaffolding agree with the strongest parts of Phase 1. Replacing it wholesale would discard useful, testable work. However, its present digest, source pin, provenance, router, and lifecycle semantics are too weak to support claims of exact reconstruction or preservation-aware routing. The next separately authorized implementation trial should therefore retain the parser/view prototype as a disposable projection while adding a thin VEPL write model and closing the exactness failures first.

Priority order for any future authorized trial:

1. enforce exact source input and preserve raw bytes with verified manifests;
2. distinguish immutable source, epistemic revision, and transformation activity authority;
3. make view/router capability and loss contracts executable and fail closed;
4. add durable correction/branch/merge/migration/recovery receipts;
5. earn additional formal-model projections through measured query/lifecycle benefit.

## UNCERTAINTY

Confidence is `MEDIUM-HIGH` that modification is necessary because the exactness and input-drift gaps are directly demonstrated. Confidence is only `MEDIUM` that the full VEPL structure is the best long-term architecture: claim-level normalization and event-sourced lifecycle machinery may cost more than they return, and a smaller raw-document-plus-manifest design could win the proposed falsification comparison. No implementation trial, scale benchmark, independent annotation study, or Owner evaluation has yet occurred.

IMPLEMENTATION_AUTHORITY = `NONE`
