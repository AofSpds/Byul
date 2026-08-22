# Rollback Package — Pre-Cutover

STATE = READY_AS_PRE_CUTOVER_NOOP / VALIDATION_PENDING
PREVIOUS_STATE = AofSpds/Byul main@993d6707ecd4deab25a5cb51909056379aefddea
NEW_ACTIVE_POINTER = NONE
MAIN_MUTATED = FALSE
CURRENT_POINTER_MUTATED = FALSE

Before WP9, rollback means abandon/close the candidate migration branch and retain main/current state unchanged.

Future WP9 must add before activation:
- exact candidate activation commit;
- exact previous active pointer/ref;
- pointer switch receipt;
- immediate fresh-channel readback;
- deterministic restore/readback instructions;
- archive/succession evidence for predecessor.

Any failed readback after a future cutover triggers immediate restoration of the exact previous pointer/state.