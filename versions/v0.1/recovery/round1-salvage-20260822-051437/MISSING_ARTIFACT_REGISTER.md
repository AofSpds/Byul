# Byul Round-1 Missing Artifact Register

## Recoverability result

The round design defines slots R01 through R10. The supplied recovery context says
nine parallel proposals were launched. Two proposal sets (R01 and R02) were found
in the repository. Therefore at least seven reported proposal/return-packet sets
are `NOT_RECOVERED_FROM_REPOSITORY`.

The repository does not establish which one of the designed R03–R10 slots was not
launched, nor whether any unrecovered worker claimed a colliding canonical RUN_ID.
The seven missing submissions are consequently not assigned invented identities.

```text
MISSING-001 through MISSING-007
STATUS = NOT_RECOVERED_FROM_REPOSITORY
EXPECTED_SOURCE = Codex UI/chat, independent worktree, overwritten local path, or unpushed branch
SUBSTANTIVE_CONTENT_RECONSTRUCTED = FALSE
CLAIMED_RUN_ID = UNKNOWN
CLAIMED_ROUND_SLOT = UNKNOWN (within designed R03-R10 set)
PROFILE = UNKNOWN
```

## Auxiliary records absent for recovered captures

Neither recovered capture included:

- `RUN_MANIFEST.md`
- `PHASE2_DELTA.md`
- `IMPLEMENTATION_EXECUTION.md`
- `IMPLEMENTATION_TRIAL*`

These absences are recorded but are not added to the seven proposal-level missing
count because repository evidence cannot prove that every worker created each
optional or contract-expected file before the workspace was mixed.

No standalone text containing `Executed the MODIFY_CURRENT disposition` or an
explicit `concurrent workspace change` statement was recovered. The shared patch,
transient tree, tests, and unreachable bytecode provide implementation evidence,
but not the missing UI narration.

## Manual recovery route

Owner may later add exact Codex return packets as new provenance-bound captures.
They must not be reconstructed from architectural similarities in the mixed code.

