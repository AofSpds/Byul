# Byul Round-1 Contamination Timeline

## Interpretation boundary

This timeline records observable repository evidence and separates it from
inference. Filesystem modification times are low-certainty observations and are
not used as proof of authorship or causal order. Git trees and blobs prove content
existence, not when or by whom it was created.

## Timeline

| Time (KST) | Evidence | Certainty | Interpretation |
|---|---|---:|---|
| 03:44:28 | Commit time for local starting HEAD `ecc3f543...` | High for Git metadata | Control-rule source later named by both reservations. |
| 04:09:19 | Reflog: checkout from `master` to `codex/byul-v0.1-r1`; branch created from then-current `origin/main` | High | One shared visible worktree began at `ecc3f543...`. |
| 04:09:33 | CAPTURE-001 reservation field; file mtime 04:09:44 | Medium | Claimed `RUN_ID=v0.1.01`, slot `R01`, profile `NEUTRAL_BLIND`. |
| 04:10:12 | CAPTURE-002 reservation field; file mtime 04:10:24 | Medium | Claimed `RUN_ID=v0.1.02`, slot `R02`, profile `NEUTRAL_BLIND`. |
| 04:13:20 | CAPTURE-001 `PHASE1_FROZEN.md` mtime | Low | Separate Phase-1 file existed in the recovered filesystem by the observed mtime; ordering is not Git-attested. |
| 04:14:33 | CAPTURE-002 `PHASE1_FROZEN.md` mtime | Low | Same limitation as CAPTURE-001. |
| 04:15:27 | CAPTURE-001 `RETURN_PACKET.md` mtime | Low | Packet includes Phase 2 and `DISPOSITION=MODIFY_CURRENT`. |
| 04:17:06 | CAPTURE-002 `RETURN_PACKET.md` mtime | Low | Packet includes Phase 2 and `DISPOSITION=MODIFY_CURRENT`. |
| after packets, exact time unknown | User/controller reports multiple later `execute` instructions | Medium as supplied recovery context; not repository-attested | Implementation was not production-authorized and must be treated separately from proposals. |
| unknown | Unreachable tree `731e0bec...` contains both run sets and a shared implementation snapshot | High for content; unknown for time/authorship | At least one staged shared implementation state existed. No commit or reflog entry assigns it to a worker. |
| later, exact time unknown | Current README blob changed `eb2d067... -> 82351fd...`; test blob changed `d0f1566... -> f4b3444...` | High for content difference; low for order beyond transient/current relation | Multiple contents existed for overlapping shared paths. Current test adds three receipt assertions; README changes one CLI option. |
| 05:10–05:11 | Two recovery inventories 22 seconds apart matched | High | No active writer was observable at the recovery gate. |
| 05:12:30 | Fetch fast-forwarded `origin/main` from `ecc3f543...` to `8e21fbdf...` | High | Remote main exactly equals declared last-known-safe commit. |
| 05:14:37 | Recovery branch created at original HEAD | High | Recovery began without changing mixed file contents. |
| 05:15–05:16 | Current mixed implementation test suite: 35/35 passed | High | Feasibility evidence only; not proposal selection or validation. |
| 05:18 | Quarantine branch remotely verified at snapshot commit `b20939bb...` | High | Destructive-restoration gate opened. |
| 05:19 | Workspace switched to local `main` tracking `origin/main` at `8e21fbdf...` | High | Shared v0.1 matched the safe remote tree; no untracked residue remained. |
| 05:19 | Restored baseline suite: 11/11 passed | High | Existing v0.1 baseline remained executable without code changes. |

## Contamination boundary

Proposal evidence consists only of the recovered reservation, frozen Phase-1, and
return-packet files. Implementation evidence consists of the shared working-tree
patch, transient staged tree, unreachable blobs/bytecode, implementation modules,
and tests.

The two proposals share many architectural concepts, and both were present beside
the same modified shared files. No repository evidence supports reliable hunk-level
authorship. Accordingly the implementation is classified `MIXED_TRIAL`,
`NON_AUTHORITATIVE`, `NON_SELECTED`, and
`IMPLEMENTATION_FEASIBILITY_EVIDENCE_ONLY`.

No explicit statement containing `concurrent workspace change` or
`those are not my edits` was recoverable from the repository. That absence does
not disprove the controller's report that such a statement existed in a Codex UI.
