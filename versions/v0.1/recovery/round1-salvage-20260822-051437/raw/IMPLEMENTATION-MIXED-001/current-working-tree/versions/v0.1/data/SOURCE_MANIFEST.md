# v0.1 Data Source Manifest

## Primary corpus

- SOURCE_KIND: `BYUL_RESEARCH_MEMORY`
- SOURCE_ROOT: `versions/v0.01/memory`
- SOURCE_BASELINE_COMMIT: `2a4529b69bc237125a1f012835d7a9b78ce3fec9`
- MACHINE_MANIFEST: `versions/v0.1/data/source_manifest_v001.json`
- SOURCE_STATE: `RESEARCH_MEMORY / NON_NORMATIVE / NOT_VALIDATED`
- DEFAULT_READ_MODE: `EXACT_GIT_TREE`
- WORKTREE_READ_MODE: `WORKING_TREE_UNPINNED / EXPLICIT / FAIL_CLOSED`

The machine manifest declares exactly 12 files at the pinned commit. For every
file it records:

- repository-relative path;
- Git blob object ID;
- original byte length;
- SHA-256 of the original bytes.

The loader compares the manifest to `git ls-tree`, reads the declared Git blobs,
and verifies all four properties. A later working-tree file is not included merely
because it matches `*.md`.

## Exact-versus-derived digest rule

- `raw_sha256`: original source bytes.
- `content_digest`: ordered, length-delimited source names plus original bytes.
- `normalized_digest`: whitespace-normalized non-empty atoms for search/index
  comparison only.
- `manifest_digest`: exact bytes of the machine-readable manifest.

The normalized digest does not prove source reconstruction. Snapshot schema v2
stores original bytes and must round-trip byte-for-byte.

## Authority rule

```text
exact source artifacts and explicitly recorded actions
    > reviewed assertion/context/justification records within their scope
    > contracted derived views with receipts
    > route/reconstruction/summary recommendations
```

`>` denotes provenance authority, not truth value. A source-supported statement
can still be false, outdated, scoped, or later corrected.

## Included memory roles

- channel/method;
- owner worldview;
- Core Principles;
- Causal Set learning;
- model family/complementarity;
- situation routing/model lifecycle;
- simulation/committee design;
- MI-1 initialization target;
- open questions/next jobs;
- chronology;
- version policy;
- active channel log.

`12_PARALLEL_PROPOSAL_ROUND1.md` exists in later repository state but is not part
of this exact v0.1 data baseline. A successor experiment must name a successor
commit/manifest rather than loading it silently.

## Mutation and successor rule

- Never overwrite the baseline manifest to disguise a changed source target.
- Create a new manifest for a material successor target.
- Retain predecessor manifests and migration receipts.
- Do not mix results from different source commits under one digest or run label.
- Unknown fields survive migration as raw payload unless a reviewed rule says
  otherwise.

## Core Principles boundary

Core Principles remain owner-adopted Byul research constraints. They do not force
a formalism, do not create a canonical P-series, and do not receive automatic
scientific or implementation PASS.
