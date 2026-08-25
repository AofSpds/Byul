# D0 Validation Slice Manifest

```text
PROGRAM_ID = ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0
TARGET_ID = D0
TARGET_HASH_MANIFEST_SHA256 = 78c1d15e395ad53e04a3ba2388ce049c1355c27b7f9f53e24ab2e9bc00df2a6e
VALIDATORS = MODELV / CONTROLV / PMOV
DISPATCH_MODE = PARALLEL / ROLE_SCOPED / READ_ONLY
FINDING_FREEZE = BEFORE_ANY_CORRECTION
FULL_REPOSITORY_SCAN = PROHIBITED
WHOLE_TARGET_REREAD = NOT_REQUIRED
```

## MODELV

Read only:

- R1 front matter, §§0–8, §§9–28, §§35–47, §§51–55.
- R3 Part B (`SYNC-001..012`).
- R2 front matter, `OPEN-01..10`, `PI-01..07`, and crosswalk result.
- D0 manifest and the semantic acceptance criteria below.

Check:

- Owner-confirmed semantics and retained safety boundaries are preserved.
- Relation/composition, VIEW/CONTROL/STATE, FOLD, reconstruction, and
  minimum-recompute wording do not close an Open formalization.
- candidates, probes, toolkit, falsification criteria, and INIT capability
  remain proposals with no technology selection or implementation authority.
- the packet remains non-final and unsupported formal claims are absent.

## CONTROLV

Read only:

- `INPUT_MANIFEST.tsv`, `DUPLICATE_INPUT_REPORT.md`, `SOURCE_PRECEDENCE.md`.
- R2 in full, R5 heading/disposition registry, R6 status/count/source sections.
- `SHA256SUMS.txt`, D0 manifest, and both telemetry ledgers as of dispatch.

Check:

- exact input/output mapping, hashes, counts, and duplicate disposition.
- OD versus Open versus PI classification and question-disposition integrity.
- missing-source and narrow Git-locator boundaries.
- timestamps/read-scope claims are supported; unknown intervals remain gaps.

CONTROLV does not re-author model semantics and does not request source
publication or repository-wide history inspection.

## PMOV

Read only:

- the exact proposal and execution plan on the task branch.
- `TASK_SCOPE_LOCK.md`, D0 manifest, this slice manifest.
- the PMO timeline, Git read-scope ledger, and validation ledger as of dispatch.

Check:

- authorized revision scope, task branch, progress, budgets, and owner-checks.
- no silent repository scan, research restart, or validator/domain expansion.
- D0 was frozen before validation; validators are independent and read-only.
- one finding freeze, one correction-batch ceiling, diff-only recheck, and
  latency-attribution formulas are correctly applied.

## Receipt contract

Each validator returns target identity, exact slice read, observed start/end,
separate context/direct durations when its interface exposes them, Git calls,
scan/reread flags, findings, scope requests, and verdict. Unavailable timing
splits must be marked `UNVERIFIED` rather than reconstructed.
