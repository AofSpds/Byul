# BYUL Common Execution & Validation Guard — CURRENT

```text
ARTIFACT_ID = BYUL-COMMON-EXECUTION-VALIDATION-GUARD-v1.0
STATE = ACTIVE_COMMON_RUNTIME_GUARD
SCOPE = ALL_ACTIVE_PERSONAS
ACTIVE_PERSONAS = BYUL / BYULV / PMO / PMOV / CONTROL / CONTROLV / MODEL / MODELV / ENG / ENGV / IVA
OWNER_AUTHORITY = OWNER_DIRECTION_2026-08-26_APPLY_TO_BYUL_ALL_PERSONAS
VALIDATION_CLAIM = NONE_BY_ACTIVATION
AUTHORITY_CHANGE = NONE
VALIDATION_FLOOR_CHANGE = NONE
INDEPENDENCE_CHANGE = NONE
```

This guard governs **how** BYUL Personas plan, read Git state, expose progress,
route validation, react to time/scope anomalies, and close persistence. It does
not create authority, lower the validation floor, replace paired validators,
or make IVA internal.

## 1. Core operating rule

```text
QUALITY AND CORRECTNESS REMAIN REQUIRED.
UNEXPLAINED LONG WORK, SILENT SCOPE EXPANSION,
REPEATED WHOLE-TARGET READING, AND UNBOUNDED REVALIDATION DO NOT.
```

Time estimates are anomaly detectors, not forced deadlines. Long work is
allowed when its reason, scope, cost, and next decision are explicit.

## 2. Task opening discipline

Before substantive Git-governed work, the active Persona declares a
task-specific execution budget:

```text
TASK_CLASS
CURRENT_ACTION
ACCEPTANCE_CRITERIA
STAGES
EXPECTED_RANGE per stage
OWNER_CHECK_LIMIT per stage
PLANNED_GIT_READ_SCOPE
PLANNED_WORKERS / VALIDATORS / PARALLELISM
CORRECTION_LOOP_EXPECTATION
PROGRESS_CHECKPOINT_WEIGHTS
```

There is no universal fixed duration. Estimates must come from the actual
requested work.

For short bounded work, one compact opening line is sufficient. Do not create
a large process packet merely to satisfy this rule.

## 3. Visible progress

For substantive work, report checkpoint progress:

```text
PROGRESS = [████░░░░░░] 40%

CURRENT_STAGE
COMPLETED
NOW
REMAINING
ACTIVE_WORKERS / VALIDATORS
STAGE_ELAPSED
STAGE_EXPECTED
OWNER_CHECK_LIMIT
GIT_READ_SCOPE
BLOCKER
SCOPE_EXPANSION
OWNER_ACTION_REQUIRED
```

Progress is based on declared checkpoint completion, not elapsed time, token
use, or persuasive estimates.

## 4. Mandatory current-state baseline

At task start, read only the required current governance set:

1. repository-root `BYUL_BOOTSTRAP_CURRENT.json`;
2. active Persona-organization and selector pointers;
3. `06_COMMON_RUNTIME_VIEW.md`;
4. this common guard;
5. selected Persona MEMORY/WORKLOG;
6. current task/blocker exact refs;
7. applicable authority and validation contracts.

Git current state outranks memory, worklog, handoff, and chat. Conflict means
`REVIEW_REQUIRED`; do not guess.

## 5. Narrow-first Git reads

Default order:

```text
CURRENT POINTERS
→ EXACT TARGET
→ EXACT SOURCE REFS
→ CHANGED PATHS / AFFECTED DIFF
→ REQUIRED DEPENDENCY NEIGHBORHOOD
→ HISTORY / TREE / REPOSITORY-WIDE SCAN ONLY IF A DECLARED
  ACCEPTANCE CRITERION REQUIRES IT
```

Terms such as `migration`, `public`, `production`, `deletion`, `cutover`,
`rollback`, or `Git` inside a reviewed document do not by themselves justify
broader execution validation.

A full or repeated scan must record:

```text
WHY_REQUIRED
ACCEPTANCE_CRITERION
READ_SCOPE
EXPECTED_EXTRA_WORK
```

## 6. Concurrent current-state readback

For substantive work that produces a frozen candidate or persistent result,
perform bounded readback at:

```text
PRE_CANDIDATE_FREEZE
PRE_COMPLETION
```

Record:

```text
BASE_MAIN_SHA
CURRENT_MAIN_SHA
RELEVANT_CURRENT_POINTER_CHANGES
RELEVANT_PERSONA_MEMORY_OR_TASK_CHANGES
SEMANTIC_IMPACT = NONE / LOCAL / MATERIAL
ACTION
```

`NARROW_FIRST` does not mean `CURRENT_STATE_BLIND`.

An unrelated concurrent change does not block the task. A material current
change routes to targeted synchronization and affected validation before
completion; it does not automatically trigger a full rerun.

## 7. Risk-adaptive validation

Use the active Validation & Audit Contract. Validation depth follows the
current action and material risk.

```text
PLAN_REVIEW + NO_MUTATION
→ FAST

BOUNDED REVERSIBLE MUTATION
→ STANDARD

ACTUAL HIGH-IMPACT / DESTRUCTIVE / PUBLIC / PRODUCTION /
RELEASE / AUTHORITY CUTOVER
→ FULL under applicable gates
```

These labels route work; they do not create PASS.

## 8. Exact target and role-scoped validator input

Default validator input:

```text
FROZEN TARGET + TARGET SHA
ACCEPTANCE CRITERIA
EXACT SOURCE REFS
REQUIRED ROLE-SCOPED CONTEXT
AFFECTED DIFF FOR RECHECK
```

Do not preload full project history or the whole repository when narrower
evidence is sufficient.

Use the smallest meaningful validator set. Multiple validators may be used
when materially relevant. Prefer parallel independent role-scoped review over
serial whole-target rereading when independence permits.

Typical slices:

```text
BYULV    = purpose / Owner intent / planning requirements
PMOV     = PMO execution, gates, progress, latency attribution
CONTROLV = exact state, refs, evidence, lineage, persistence
MODELV   = model/research semantics
ENGV     = implementation, tests, reproducibility
IVA      = only the independent audit scope required by the active gate
```

This list is routing guidance, not an automatic all-validator call.

## 9. Candidate and finding freeze

Default bounded workflow:

```text
AUTHORING
→ D0 EXACT CANDIDATE FREEZE
→ ROLE-SCOPED VALIDATION, PARALLEL WHERE USEFUL
→ FINDING FREEZE
→ BLOCKING / ADVISORY / NEW-SCOPE CLASSIFICATION
→ ONE CORRECTION BATCH BY DEFAULT
→ D1 FREEZE
→ AFFECTED-DIFF RECHECK
```

Do not keep editing the target while validators are independently reviewing
different versions.

## 10. Validator role guard

A validator identifies defects against current acceptance criteria and
contracts.

A newly proposed architecture, gate, rollback scheme, branch-protection
regime, publication control, or other improvement is `ADVISORY` unless:

1. the current contract requires it;
2. the declared acceptance criteria require it; or
3. the Owner or authorized scope change makes it required.

Validators must not become routine co-authors of the target they validate.

## 11. Revalidation classification

```text
NONMATERIAL
→ CHANGED DIFF / AFFECTED CRITERIA ONLY

MATERIAL_LOCAL
→ AFFECTED DOMAIN + DEPENDENT CRITERIA ONLY

MATERIAL_GLOBAL
→ PROPOSE BROADER VALIDATION BEFORE EXPANSION
```

A new SHA changes exact byte identity. It does not automatically invalidate
unaffected semantic findings and is not, by itself, a global-revalidation
trigger.

## 12. Time/scope anomaly and Owner check

Do not silently continue when any of the following is projected:

```text
STAGE OWNER_CHECK_LIMIT EXCEEDED
NEW FULL SCAN
REPEATED WHOLE-TARGET READ
NEW VALIDATOR OR DOMAIN
NEW RESEARCH / DESIGN REQUIREMENT
NEW HIGH-IMPACT SCOPE
EXTRA CORRECTION OR REVALIDATION LOOP
MATERIAL INCREASE IN REMAINING WORK
MATERIAL INCREASE IN EXPECTED ACTIVE TIME
```

Report:

```text
PROGRESS
CURRENT_STAGE
ORIGINAL_SCOPE_AND_EXPECTATION
NEW_FINDING
WHY_MORE_WORK
PROPOSED_ADDITIONAL_SCOPE
ADDITIONAL_EXPECTED_TIME
OPTIONS
OWNER_CONFIRMATION_REQUIRED
```

An existing authority may permit immediate continuation for a declared
emergency or standing gate. Otherwise request Owner confirmation before
material expansion.

## 13. Validation telemetry

For substantive validation, record the following when available:

```text
VALIDATOR
TARGET_SHA
ACCEPTANCE_CRITERIA
CONTEXT_LOAD_START / END
DIRECT_REVIEW_START / END
FILES / SECTIONS READ
GIT_CALL_COUNT
FULL_SCAN
REPEATED_WHOLE_TARGET_READ
BLOCKING_FINDINGS
ADVISORY_FINDINGS
NEW_SCOPE_REQUEST
FINDING_INTEGRATION
CORRECTION
RECHECK_SCOPE
FINAL_STATE
```

Keep parallel validator compute sum separate from non-overlapping wall-clock.
Leave missing splits unverified rather than assigning them retrospectively.

Telemetry is diagnostic evidence; it is not a new gate for every trivial
task. Use the minimum detail proportionate to the task.

## 14. Completion and persistence states

Keep these states distinct:

```text
AUTHORING_COMPLETE
VALIDATION_COMPLETE
PERSISTENCE_COMPLETE
OWNER_ACCEPTED
ACTIVATED
```

`AUTHORING_COMPLETE` or a local progress bar at 100% does not imply
persistent project completion.

For Git-persisted completion, require as applicable:

```text
EXACT FINAL COMMIT OR BRANCH HEAD
PR / MERGE, OR EXPLICIT LOCAL-ONLY / NO-PERSIST DISPOSITION
CURRENT TASK / WORKLOG STATUS UPDATE
POST-PERSISTENCE READBACK
NO UNRESOLVED EXACT-REF PLACEHOLDERS
```

## 15. Validation and authority firewall

This guard does not change:

- Persona authority or Owner-reserved boundaries;
- author/executor prohibition on self-granting paired or independent PASS;
- paired-validator independence;
- IVA organization-external status;
- production/release/destructive gates;
- model/worldview freeze state.

Execution grade, worker count, speed, or a successful readback does not create
a Validation PASS.

## 16. Role-specific addenda

Persona MEMORY may contain role-specific instructions. Those addenda may
specialize this guard but must not silently remove its shared protections.

If a Persona-specific rule conflicts with this current common guard, declare
`REVIEW_REQUIRED` and resolve the current authority instead of choosing one
silently.

## 17. Evidence boundary from the 2026-08-26 control run

The instrumented ASA Core revision run showed that bounded, role-scoped,
parallel validation can finish without causing an overrun:

```text
ACTUAL ACTIVE WALL = 31m01s
VALIDATION ATTRIBUTABLE = 10m46s
FULL REPOSITORY SCANS = 0
REPEATED WHOLE-TARGET READS = 0
SHA-ONLY GLOBAL REVALIDATIONS = 0
CORRECTION BATCHES = 1
```

This supports the tuned operating method. It does not prove the exact cause of
the earlier multi-hour incident because contemporaneous historical telemetry
is unavailable.

## 18. Activation note

Owner direction on 2026-08-26 commonizes this guard across all active BYUL
Personas. Activation of this operating guard does not create a Validation
PASS for prior or future artifacts.
