# Reservation — Byul clean rerun v0.1.08

ROUND_ID = `BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01`

ROUND_SLOT = `R04`

RUN_ID = `v0.1.08`

WORKER_ID = `20260822-053736-766d7784`

PROFILE = `NEUTRAL_BLIND`

SLOT_RESERVATION_REF = `refs/heads/byul-reservations/r1-clean/R04`

SLOT_RESERVATION_COMMIT = `f58dc78f5cbf41539bb5719d92b1f2eab2c6e522`

SLOT_REMOTE_VERIFIED = `TRUE`

RUN_RESERVATION_REF = `refs/heads/byul-reservations/run/v0.1.08`

RUN_RESERVATION_COMMIT = `eabb636d1f91b8919c137233a92b029cbe187363`

RUN_ID_CONFIRMED = `TRUE`

RUN_REMOTE_VERIFIED = `TRUE`

Notes:

- R01–R03 were already remotely reserved when this worker fetched the slot namespace, so R04 was the lowest free slot.
- v0.1.04, v0.1.06, and v0.1.07 collided during reservation attempts; each push was rejected without force. A fresh fetch showed v0.1.03–v0.1.07 reserved, so v0.1.08 was the next canonical ID and was verified against the exact remote ref.
- Reservation commits contain this worker ID and were pushed only to the reservation namespaces. No reservation ref was force-pushed.
- These reservations authorize this independent research report only. `IMPLEMENTATION_AUTHORITY = NONE`.

