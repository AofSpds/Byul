# Phase 2 Comparison — v0.1.05

EXACT_COMPARE_COMMIT = 8e21fbdf597d38bb831834fc83cd3a53bcb180e0
PHASE1_FREEZE_COMMIT = 7fafb16a01d00840a50b6d28ecbb0d49caded598
PHASE1_SHA256 = 0f71b087101c9995b8ff97223a59a1e8a56937c2ac814b0826bc87dfc508d65c
PHASE1_UNCHANGED_AFTER_FREEZE = TRUE

Only the five packet-enumerated files were read from the exact compare commit.
The checked-out implementation, main, recovery state, and other run branches were not
used. The comparison is analysis only.

## AGREEMENTS

- The v0.1 implementation correctly makes Byul's research memory the primary data and
  assigns raw memory higher provenance authority than indexes, routing outputs, and
  summaries.
- `MemoryAtom` retains source path, line number, section, syntactic kind, text, and
  explicit marker tags. The parser deliberately avoids free-form LLM reclassification.
- Derived history/current/open/model/lifecycle/core-principle views are not presented
  as canonical world models.
- Unknown intents, unknown fields, exact metric requests without an external source,
  and natural-language Core Principles evaluation remain `REVIEW_REQUIRED` rather
  than receiving invented commitments or automatic PASS.
- The implementation exposes a preservation vocabulary and includes source digest,
  virtual invalidation, chronology, and JSON snapshot probes.
- It explicitly rejects Petri, Causal Set, event/mapping, or Core Principles as
  automatically canonical/scientifically validated.

These are substantial architectural agreements with the frozen proposal and are good
reasons to evolve the implementation instead of discarding it wholesale.

## OBSERVED_GAPS

1. **The source commit is declared but not enforced.** `SOURCE_BASELINE_COMMIT` is a
   constant returned in model metadata, while `MemoryCorpus.load()` reads a filesystem
   glob. The code does not prove that loaded bytes came from that commit. A caller can
   supply another root and still receive the fixed baseline value.
2. **The advertised raw round-trip is not byte-exact.** `snapshot()` stores parsed
   non-empty atoms plus each document's `raw_sha256`, but not raw document bytes/text.
   `content_digest()` and `snapshot_content_digest()` hash normalized atom text,
   collapsing whitespace and omitting blank lines. The test JSON-encodes and decodes
   the already parsed snapshot; it does not reconstruct or verify the source corpus.
3. **Epistemic state is too weak for the research target.** Substring tags capture a
   few explicit markers, but there is no authoritative distinction among
   source-supported claims, Owner direction, working hypotheses, open questions,
   non-conclusions, and worker inferences. There are no claim revisions,
   supersession/correction edges, contexts, or authority scopes.
4. **Current-state reconstruction is lexical, not lifecycle-aware.** The current view
   selects lines containing words such as `current`, `현재`, or `direction`. It cannot
   reliably apply a later correction to an earlier claim while preserving both in
   history. The baseline's P-series correction is a concrete counterexample.
5. **Lifecycle is vocabulary and simulation seed, not a lifecycle model.** Virtual
   mutation deep-copies a snapshot and appends one atom. Compose, split, divergence,
   merge, migration, recovery, succession, conflict, and rollback do not have state
   transition semantics or persistent lineage.
6. **`R(S,M,L)` is only partially exercised.** Intent maps to hard-coded views;
   preservation affects only the special case `history=EXACT`; the `model` argument is
   unused; lifecycle adds checks for a subset of phase names. There is no transform
   catalog, field-level preservation proof, loss receipt, measured cost, path
   composition, or route abstention based on catalog insufficiency.
7. **Invalidation is manual and coarse.** Dependencies are a static filename table.
   The radius is the fraction of named derived views matched by a changed filename,
   not semantic or transitive invalidation. Undeclared dependencies are invisible.
8. **Several tests are structurally weak.** The chronology graph is constructed as a
   consecutive list, so acyclicity is almost guaranteed by construction. Snapshot
   round-trip compares two calculations over the same parsed atoms. Tests do not
   challenge whitespace loss, source-commit mismatch, correction, conflicting
   contexts, branching/merge, transform loss, or recovery.

## TEST_OR_STATIC_EVIDENCE

- Read-only syntax compilation directly from the pinned Git blobs succeeded for
  `versions/v0.1/src/byul_v01.py` and `versions/v0.1/tests/test_byul_v01.py` under
  Python 3.13.14.
- Static inspection found eleven `unittest` cases covering corpus loading, principle
  view presence, parsed-snapshot digest equality, chronology acyclicity, known and
  unknown routes, exact-metric review, lifecycle validation labels, virtual mutation,
  and invalid preservation levels.
- The test suite was not executed because its class setup reads the live/default
  `versions/v0.01/memory/*.md` corpus, while this Phase-2 packet authorized exact
  object reads of only the five enumerated compare files. Static evidence is used to
  preserve the input boundary.
- The frozen Phase-1 file remained byte-identical after comparison: SHA-256
  `0f71b087101c9995b8ff97223a59a1e8a56937c2ac814b0826bc87dfc508d65c`.

## MATERIAL_DELTAS_FROM_CURRENT

- Replace filesystem-baseline metadata with verified, content-addressed evidence
  artifacts and exact commit/blob receipts.
- Add an append-only research-operation ledger so corrections, classification,
  branching, merging, migration, recovery, and succession are replayable rather than
  inferred from the latest Markdown snapshot.
- Add nanopublication-like claim revisions with explicit epistemic class, polarity,
  authority scope, context, provenance, valid/transaction time, and relations.
- Treat current/history/model views as deterministic materializations with declared
  dependencies; keep the current parser and views as useful seed projections.
- Replace hard-coded routing with a catalog-backed planner that checks field-level
  preservation contracts, composes transform losses/costs, and returns
  `REVIEW_REQUIRED` when no admissible path exists.
- Upgrade digest and round-trip tests to source-byte preservation and add correction,
  conflict, split/compose, diverge/merge, migration, recovery, lens-law, and
  invalidation-oracle tests.

## RECOMMENDED_DISPOSITION

RECOMMENDED_DISPOSITION = RECOMMEND_MODIFY_CURRENT

## WHY

The current implementation has the right experimental center of gravity: raw memory
precedence, derived views, explicit uncertainty, no automatic principle PASS, and a
small stdlib-only executable slice. Those choices align with the frozen proposal and
provide reusable ingestion, atomization, view, CLI, and test scaffolding.

The gaps are nevertheless material for the stated research question. The existing
system cannot reconstruct semantic correction and branch history, enforce its own
source pin, prove raw byte preservation, or perform the lifecycle and transformation
contracts it names. Modification should therefore be architectural rather than
cosmetic, but replacement would throw away useful aligned work without evidence that
a fresh stack is necessary.

## UNCERTAINTY

- Only the packet-enumerated files at the exact compare commit were inspected; dynamic
  behaviour against an exact exported corpus was intentionally not tested.
- Claim-level structure may cost more human annotation and maintenance than it saves.
- The minimum viable ledger may be smaller than the Phase-1 design; raw Git-tracked
  Markdown plus correction metadata could win the comparative test.
- Recommendation strength is medium until reconstruction/lifecycle fixtures compare
  the current slice, the proposed modification, and a simpler baseline.

IMPLEMENTATION_AUTHORITY = NONE
IMPLEMENTATION_PERFORMED = FALSE

