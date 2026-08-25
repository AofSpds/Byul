# ASA Core v2.1 Candidate — Task Scope Lock

```text
PROGRAM_ID = ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0
RUN_ID = 20260826T015430KST
CURRENT_PERSONA_LOCK = PMO
TASK_CLASS = STANDARD / BOUNDED DOCUMENT REVISION + DIAGNOSTIC TELEMETRY
OWNER_AUTHORIZATION = OWNER_MESSAGE_2026-08-26_PMO_PROCEED_AND_DIAGNOSE_VALIDATING
TASK_BRANCH = work/asa-core-revision-validation-attribution-20260826
BASE_COMMIT = e6e0caf97b53627bee8024f701977f6d64e075fa
PROPOSAL_BLOB_SHA = bbb6391dc08733d838c4f39f9eeae88d85bc53ab
PLAN_BLOB_SHA = e6539e2da404f387a051cbc9cd86136a85e9d661
START_KST = 2026-08-26T01:54:30+09:00
DISPATCH_BASELINE = 45-90 minutes
REVISED_CONSERVATIVE_PLANNING_RANGE = 61-120 minutes
PARALLEL_BEST_CASE_ENVELOPE = 53-105 minutes
OWNER_CHECK = projected active wall-clock > 120 minutes
```

## Locked scope

- Revise the exact six-document ASA Core v2.0 packet into a non-final `v2.1 CANDIDATE` successor packet.
- Preserve Owner-confirmed decisions, explicit Open items, Pro-mode implications, and the 180-question ledger without inventing answers.
- Record actual execution and validation timing sufficiently to distinguish direct validation, orchestration overhead, induced rework, and non-validation work.
- Freeze one D0 candidate, collect one parallel finding batch, perform at most one correction batch, and use affected-diff recheck.

## Explicit exclusions

- No repository-wide scan or history audit.
- No external research restart.
- No technology selection, implementation, production authorization, release, source deletion, or World Model freeze.
- No ENG, ENGV, or IVA routing.

## Planned roles

- Authoring: MODEL
- Evidence and inventories: CONTROL
- Plan validation: BYULV
- Output validation: MODELV, CONTROLV, PMOV in parallel and role-scoped
