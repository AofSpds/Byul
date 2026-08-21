# Phase 2 Read-Only Comparison — v0.1.09

EXACT_COMPARE_COMMIT = `8e21fbdf597d38bb831834fc83cd3a53bcb180e0`
COMPARE_MODE = `EXACT_GIT_OBJECT_READS + READ_ONLY_ARCHIVE_EXPORT`
PHASE1_REMOTE_CONFIRMED_BEFORE_COMPARE = `TRUE`
IMPLEMENTATION_AUTHORITY = `NONE`

The comparison used only the five packet-authorized paths at the exact commit.
The archive export was marked read-only; Python bytecode writes were disabled.
The current worktree, main, recovery data, other branches, and other run outputs
were not used.

## AGREEMENTS

The current implementation and the frozen proposal agree on several important
boundaries:

- v0.01 research memory is primary data; derived views and router output have
  lower provenance authority.
- No Petri/Event/Causal/LTS formalism is declared canonical.
- Core Principles remain a review requirement rather than an automatic PASS.
- Unknown intent and exact metric requests fail toward `REVIEW_REQUIRED` rather
  than fabricated model or metric commitments.
- Raw provenance, source baseline identity, content digests, derived views, and
  invalidation are appropriate concerns for the first executable slice.
- Chronology is treated as the order asserted by its source document, not as a
  universal causal order.
- The implementation is stdlib-only, small, readable, and usable as an
  experimental scaffold.

## OBSERVED_GAPS

### Authority and exactness

The implementation stores a `SOURCE_BASELINE_COMMIT` constant but loads
`DEFAULT_MEMORY_ROOT` from the checked-out filesystem. It does not prove that
loaded bytes came from that commit. A changed worktree can therefore be reported
under the pinned constant.

The advertised raw/exact preservation is weaker than byte exactness:
`Path.read_text()` decodes text, the parser drops blank lines and applies
`line.strip()`, and the corpus digest normalizes whitespace. `raw_sha256` is
included in snapshots, but the tested round-trip digest recomputes only from
normalized atom text and does not validate every `raw_sha256` or original file
byte sequence. Exact typography, line endings, trailing spaces, encoding errors,
and some structural context are outside the tested guarantee.

### Epistemic state and succession

Classification is substring tagging of explicit markers. It does not encode the
full required state classes, source evidence, revision scope, invalidation,
contradiction, or current-state precedence. For example, the singular matcher
for `NON_CONCLUSION`/`NON-CONCLUSION` does not necessarily tag a natural-language
plural heading such as `Non-conclusions`. Earlier statements and later
corrections may coexist in the current-state search view without a machine-
auditable supersession relation.

There is no append-only assertion/event ledger, parent DAG, branch head,
revision relation, deterministic current-state fold, or conflict-preserving
merge. Consequently the code cannot yet reconstruct why one assertion is
current while another is historical without rereading natural language.

### Transformations, views, and routing

Views are fixed filename dependency lists plus lightweight filters. They do not
carry input snapshot IDs, transform digests, semantic capability claims,
preserved/omitted fields, validation receipts, or measured costs. `R(S,M,L)` is
mostly a dispatch table: only exact history is inspected from the preservation
map; `CurrentModelState` is passed but not used for selection; most lifecycle
verbs append the same validation strings. No transformation path is constructed
or verified.

The Phase-1 `Plan(Q,P,A)` compression would preserve the useful fail-closed API
while making preservation requirements and registered artifact capabilities the
actual decision inputs. The existing `R(S,M,L)` surface can remain as an adapter
during migration.

### Lifecycle depth

`simulate_virtual_mutation` deep-copies a snapshot, appends a synthetic atom,
and computes affected views from static filename dependencies. This is a valid
micro-seed, but it does not execute persistent mutation lineage, composition,
split, divergent edits, semantic merge conflict, schema migration, degraded
operation, checkpoint replay, or object recovery. Its recovery claim is a
descriptive string rather than a tested restore.

## TEST_OR_STATIC_EVIDENCE

All evidence below is from commit
`8e21fbdf597d38bb831834fc83cd3a53bcb180e0`.

### Executed tests

- The README command
  `python -m unittest versions/v0.1/tests/test_byul_v01.py` failed on the pinned
  read-only Windows export with `ModuleNotFoundError: No module named
  'versions/v0'`; the dot in `v0.1` is interpreted as a module separator.
- Direct execution
  `python versions/v0.1/tests/test_byul_v01.py` passed all 11 tests in 0.049 s.
- The export remained read-only, produced no `__pycache__`/`.pyc`, and the
  isolated run branch remained clean after testing.

These passing tests establish the behaviors they name, not the stronger exact-
source, semantic-preservation, or lifecycle claims proposed for a successor.

### Static anchors

- `src/byul_v01.py:19` declares the source commit; `:169` reads the filesystem
  path without resolving that commit.
- `src/byul_v01.py:182-185` forms `content_digest` from normalized atom text;
  `:312` strips each line.
- `src/byul_v01.py:245-268` serializes `raw_sha256` but computes the round-trip
  digest from atom texts; the corresponding test begins at
  `tests/test_byul_v01.py:35`.
- `src/byul_v01.py:82-100` implements marker substring tagging.
- `src/byul_v01.py:348-395` implements routing; the model parameter appears at
  `:351`, while only exact history, exact metric, unknowns, and a lifecycle verb
  set materially affect the plan.
- `src/byul_v01.py:273-305` is the virtual mutation implementation.
- `README.md:113` contains the platform-failing unittest command.

## MATERIAL_DELTAS_FROM_CURRENT

1. Make source Artifacts byte-addressed and verify the exact baseline object
   rather than trusting a constant beside a mutable path.
2. Add immutable classified assertion/relation entries with provenance,
   revision/invalidation/contradiction links, parent DAG, branch heads, and a
   versioned deterministic reducer.
3. Replace normalized-text round-trip as the strongest guarantee with byte-exact
   artifact and canonical-entry round trips; retain normalized digests only as
   search/index aids.
4. Give each derived view an input/transform/preservation/loss/validation
   manifest and explicit invalidation dependencies.
5. Make routing capability- and preservation-driven through `Plan(Q,P,A)`, with
   `R(S,M,L)` retained only as a compatibility adapter until ablation tests
   justify extra routing inputs.
6. Expand lifecycle tests from virtual local mutation to persistent
   correct/revise, compose, split, diverge, merge-conflict, migrate, checkpoint,
   degraded-read, and recovery scenarios.
7. Preserve the present parser, CLI shape, fail-closed gates, view concepts, and
   tests as bootstrap assets where their contracts are narrowed accurately.

## RECOMMENDED_DISPOSITION

RECOMMENDED_DISPOSITION = `RECOMMEND_MODIFY_CURRENT`

This is advisory only.

## WHY

The current implementation already embodies the correct experimental posture,
authority ordering, raw/view split, unknown handling, and no-auto-PASS rule. A
full replacement would discard useful, tested scaffolding. However, its current
data and lifecycle semantics are not strong enough to support the reconstruction
and preservation claims that matter most. The authority substrate, reducer,
view contracts, and router evidence need material modification, not cosmetic
patches.

## UNCERTAINTY

Confidence in the static gaps is high because they are directly visible in the
pinned code and tests. Confidence that the frozen proposal is the best successor
is medium: it has not been implemented or benchmarked, raw versioned documents
may be sufficient at the current scale, and a richer formal representation may
prove necessary for simulation-heavy workloads. The recommendation should be
tested against raw-file-only and richer-graph alternatives before acceptance.

IMPLEMENTATION_AUTHORITY = `NONE`
IMPLEMENTATION_PERFORMED = `FALSE`
