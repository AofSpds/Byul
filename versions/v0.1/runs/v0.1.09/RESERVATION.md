# Reservation — Byul Clean Rerun v0.1.09

ROUND_ID = `BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01`
ROUND_SLOT = `R09`
RUN_ID = `v0.1.09`
WORKER_ID = `20260822-053814-d91c9e34`
PROFILE = `MINIMAL_INFORMATION`

SLOT_RESERVATION_REF = `refs/heads/byul-reservations/r1-clean/R09`
SLOT_RESERVATION_COMMIT = `24bed63e338a18671eb4f0cbd8f2510f9cd47bc6`
SLOT_REMOTE_VERIFIED = `TRUE`

RUN_RESERVATION_REF = `refs/heads/byul-reservations/run/v0.1.09`
RUN_RESERVATION_COMMIT = `c60d4d59b89a9cc80beda76bb64b448e29e32367`
RUN_ID_CONFIRMED = `TRUE`

Both reservation refs were created by non-force pushes of unique commits whose
messages contain this `WORKER_ID`. Each remote ref was then read back and found
to equal the corresponding local reservation commit.

No reservation ref was deleted, rewritten, or force-pushed.
