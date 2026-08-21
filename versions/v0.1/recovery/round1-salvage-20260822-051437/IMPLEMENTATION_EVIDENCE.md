# Mixed Implementation Evidence

## Classification

```text
IMPLEMENTATION_ID = IMPLEMENTATION-MIXED-001
IMPLEMENTATION_STATE = MIXED_TRIAL
AUTHORITY = NON_AUTHORITATIVE
SELECTION = NON_SELECTED
USE = IMPLEMENTATION_FEASIBILITY_EVIDENCE_ONLY
BASE_COMMIT = ecc3f5431ac967383027de7173bf2541cf87f2c5
HUNK_AUTHORSHIP = UNKNOWN
```

## Preserved states

- `RAW_WORKTREE_DIFF.patch` preserves 5 modified and 12 untracked v0.1 paths
  relative to the local execution base. SHA-256:
  `224655494bb8575cbcc3c123e47e6185e8b19aa02af95022ba771798a6c61cae`.
- `raw/IMPLEMENTATION-MIXED-001/current-working-tree/` stores the changed/new
  implementation files as observed at recovery.
- `raw/IMPLEMENTATION-MIXED-001/transient-index-tree-731e....zip` preserves the
  full unreachable staged tree. ZIP SHA-256:
  `a43e94b5802bbf7a0615a1eb00dd5f5409e245fb86c3b9779f0baf70fa5d8cc7`.
- `BASE_TO_TRANSIENT_TREE.patch` preserves the transient implementation patch;
  SHA-256 `5b9398f1a8b7daa526e2c04da050c1ba1dfdb8f3d409fdec6449663a22dc6f69`.
- `TRANSIENT_TREE_TO_CURRENT.patch` preserves the two shared paths that changed
  after the transient tree; SHA-256
  `fc4427e01ee59c914d9371d790ee12153746e29fa8a2d4bbcb8a206a1d129b20`.

The transient and current states differ by one README CLI-option correction and
three additional derivation-receipt assertions. This proves overlapping path
evolution but does not identify its author.

## Test evidence

At recovery, this non-authoritative command was run without bytecode generation:

```text
python -B -m unittest discover -s versions/v0.1/tests -p "test_*.py" -v
Ran 35 tests in 16.609s
OK
```

Both return packets also report that the pre-execute baseline's direct 11-test
suite passed. Those packet statements are preserved as proposal-worker reports,
not independently replayed timing evidence.

Passing tests demonstrate only that the mixed implementation was executable in
the observed environment. They do not validate the model or select either
proposal.
