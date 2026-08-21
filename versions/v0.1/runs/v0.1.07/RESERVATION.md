# Clean Rerun Reservation

ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1-CLEAN-RERUN-01
ROUND_SLOT = R06
RUN_ID = v0.1.07
WORKER_ID = 20260822-053853-f6cf4c88
PROFILE = NEUTRAL_BLIND

SLOT_RESERVATION_REF = refs/heads/byul-reservations/r1-clean/R06
SLOT_RESERVATION_COMMIT = 9228e2b86540fce1cae30feca9f5240d20bcecf4
SLOT_REMOTE_VERIFIED = TRUE

RUN_RESERVATION_REF = refs/heads/byul-reservations/run/v0.1.07
RUN_RESERVATION_COMMIT = 256309ff3cb7a61ccef766518e362e3be241982b
RUN_ID_CONFIRMED = TRUE

RESERVATION_METHOD = UNIQUE_COMMIT_PUSH_WITHOUT_FORCE
RESERVATION_BASE_COMMIT = 68815178d104b74f56b6ab071dd24226862c079d
RESERVED_AT = 2026-08-22T05:38:53+09:00

The remote slot ref and canonical run ref were each read back with `git
ls-remote --heads origin <exact-ref>` and matched this worker's unique
reservation commit. No reservation ref was force-pushed.

