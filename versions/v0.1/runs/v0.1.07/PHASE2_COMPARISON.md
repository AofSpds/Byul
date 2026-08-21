# Phase 2 Exact-Commit Comparison

ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01
ROUND_SLOT = R06
RUN_ID = v0.1.07
WORKER_ID = 20260822-053853-f6cf4c88

EXACT_COMPARE_COMMIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0
PHASE1_FREEZE_COMMIT = c6bbf180b1ace4c71a4958969267e6e0035fce96
PHASE1_SHA256 = f0e6d2499ee08dfe1610702a7493c2d00893e6d5c50236a573dfe1b88c307eb7
PHASE1_REMOTE_CONFIRMED = TRUE
PHASE2_READ_METHOD = EXACT_GIT_OBJECT_READ_PLUS_READ_ONLY_ARCHIVE
CURRENT_WORKTREE_IMPLEMENTATION_USED = FALSE

## AGREEMENTS

The pinned v0.1 implementation and the frozen proposal agree on important
safety boundaries:

- Raw memory has higher provenance authority than indexes, router output, or
  summaries.
- Derived views must not be promoted to scientific truth or replace sources.
- Unknown intent and exact metric requests fail to `REVIEW_REQUIRED` instead of
  inventing a model or metric source.
- BYUL CORE-A remains a natural-language review obligation and never receives
  an automatic PASS.
- Chronology is described as an order index, not universal physical/logical
  causality.
- No Petri, Causal Set, Event, mapping, or other candidate is made canonical.
- Content digests, source/line provenance, explicit marker extraction,
  lifecycle vocabulary, virtual mutation, invalidation, and snapshot testing
  are useful first scaffolds.
- A small stdlib-only implementation is appropriate for an initial falsifiable
  slice.

## OBSERVED_GAPS

### 1. The declared exact source baseline is not enforced

`SOURCE_BASELINE_COMMIT` is metadata only. `MemoryCorpus.load()` reads
`DEFAULT_MEMORY_ROOT.glob("*.md")` from the process's current filesystem and
never resolves or verifies the declared commit/tree/digests.

Static exact-object evidence:

- Declared source commit memory tree:
  `6294e77ce410a817e8562019ec6db1438cbe2700`.
- Compare-commit memory tree:
  `ddb3e8f1c6deac880f7a29eee78711f256bc8a7c`.
- The compare tree adds `12_PARALLEL_PROPOSAL_ROUND1.md` and
  `13_ROUND1_ACCIDENTAL_IMPLEMENTATION_INCIDENT.md` relative to the declared
  source baseline.

The test threshold `document_count >= 12` passes both, so the suite does not
detect that a runtime silently changed the experiment's DATA target.

### 2. “Raw round-trip” is not byte-exact source reconstruction

`Path.read_text()` decodes text and may normalize platform newlines. The
document `raw_sha256` hashes re-encoded decoded text rather than source bytes.
Blank lines are omitted from atoms; atom text is stripped; and corpus/snapshot
digests pass text through `_norm`, collapsing whitespace. `snapshot()` stores
atoms and the digest but not the original raw bytes/text.

Consequently, `test_raw_snapshot_roundtrip_content_digest` proves internal
agreement between two uses of the same lossy normalization. It does not prove
that an exported snapshot can reconstruct the original Markdown or distinguish
all material byte changes.

### 3. Research change semantics are absent

The model is a snapshot parser, not an evolving research-state model. It has no
immutable events for assertion, classification, supersession, retraction,
contradiction, validation, branch, or merge decision; no actor/activity
provenance; no valid-time versus recorded-time distinction; and no
transformation receipts. A later file silently replaces an earlier state unless
Git is consulted outside the model.

Explicit tags are shallow lexical matches, not the required epistemic classes.
There is no complete representation of `SOURCE_SUPPORTED`, `OWNER_DIRECTION`,
`WORKING_HYPOTHESIS`, `OPEN`, `NON_CONCLUSION`, and `INFERENCE` with authority,
scope, and review state.

### 4. Routing is a static intent lookup, not evidence-backed routing

`Router.route()` does not use its `model` argument. Apart from validating enum
values, preservation demands affect only the special case
`history == EXACT`. Lifecycle phases are not validated; a recognized subset
only adds fixed strings. There is no projection capability catalog,
precondition, measured cost, freshness, source cutoff, transformation path,
per-meaning preservation proof, fallback comparison, or refusal explanation.

`R(S,M,L)` is therefore represented syntactically but not yet tested as a
three-argument decision function.

### 5. Invalidation and lifecycle are simulated by static filenames

`VIEW_DEPENDENCIES` is a manually maintained filename table. Mutation appends a
virtual normalized atom to a copied snapshot and reports views whose static
tuple mentions the filename. It does not derive dependencies from actual
transformation receipts and does not exercise compose, split, divergence,
merge, migration, degraded operation, recovery, rollback, schema succession,
or cumulative drift.

### 6. Several tests are necessary but weak/tautological

- The history graph is constructed as a consecutive chain of chronology items,
  so its acyclicity test cannot expose a cycle in a richer relation model.
- Digest length is tested, not equality to the declared source manifest.
- Views are tested for non-emptiness/keywords, not recall, false positives,
  classification fidelity, provenance closure, or non-conclusion preservation.
- Router tests verify fixed output strings, not correctness versus alternative
  plans or preservation evidence.

## TEST_OR_STATIC_EVIDENCE

The five required files were read with `git show` from the exact compare commit.
For execution, the exact compare-commit code/tests and its exact memory tree
were exported outside the repository, all exported files were marked read-only,
and Python bytecode writes were disabled.

- Documented command:
  `python -m unittest versions/v0.1/tests/test_byul_v01.py`
  -> exit 1 in this Windows/Python 3.13 environment because `v0.1` is parsed as
  a dotted module name (`ModuleNotFoundError: No module named 'versions.v0'`).
- Exact test file invoked directly:
  `python -B versions/v0.1/tests/test_byul_v01.py`
  -> 11 tests run, 11 passed, exit 0.
- Repository status after both executions: clean.
- Writable files in the read-only export: 0.
- Frozen Phase-1 worktree SHA-256 after Phase 2:
  `f0e6d2499ee08dfe1610702a7493c2d00893e6d5c50236a573dfe1b88c307eb7`,
  unchanged from the remotely verified freeze.

Passing tests support the limited implemented claims. They do not close the
gaps above.

## MATERIAL_DELTAS_FROM_CURRENT

1. Add immutable source-byte blobs and enforce an exact source manifest/tree at
   ingestion; fail closed on extra, missing, or changed files.
2. Add append-only, typed, bitemporal research events with actor/source/scope,
   epistemic class, supersession/retraction/contradiction, branch, and merge
   semantics.
3. Add transformation receipts and a per-meaning preservation/loss matrix;
   build invalidation from recorded input dependencies.
4. Keep the useful current views, but register them as versioned projections
   with source cutoff, builder version, capability, freshness, measured cost,
   and validation evidence.
5. Refine `R(S,M,L)` into a typed preservation-first request
   `Plan(Q,P,A,L,C)` while retaining S/M/L as research axes. The router chooses
   derived plans, not truth or authority.
6. Replace normalized self-round-trip claims with byte-exact blob tests,
   deterministic fold-at-cutoff tests, provenance closure, conflict retention,
   migration differentials, and lifecycle/adversarial tests.
7. Correct the portable test command/documentation while preserving direct test
   execution.

These are substantial changes, but the current parser/view/router/test harness
can remain as a migration scaffold. A wholesale replacement is not yet
justified.

RECOMMENDED_DISPOSITION = RECOMMEND_MODIFY_CURRENT

## WHY

The current implementation has the right modest scope and several correct
guardrails, so discarding it would lose useful executable scaffolding. However,
its authoritative representation and tests are too weak for the central Byul
problem: evolving state, exact inputs, epistemic distinctions, semantic loss,
branching lifecycle, and auditable transformations. The frozen proposal adds
those capabilities beneath/around the existing views without canonizing a
domain formalism.

## UNCERTAINTY

Confidence is MEDIUM. The conclusions are strong static findings and the exact
micro-tests ran, but no representative corpus migration, multi-writer branch
workload, performance benchmark, semantic annotation study, or Owner blind
comparison was performed. The event/provenance architecture may be excessive
for a small Git-managed corpus. A separately authorized trial must compare it
against the simpler current baseline before acceptance.

IMPLEMENTATION_AUTHORITY = NONE
IMPLEMENTATION_PERFORMED = FALSE

