# Validation & Audit Contract

STATE = ACTIVE_CONTRACT / POST_BOOTSTRAP_QA_QUEUED
VALIDATION_CLAIM = NONE_BY_ACTIVATION

Principles:
- Every substantive persistent author/executor has a paired validator.
- Author/Executor cannot self-grant final validation PASS.
- Validator cannot materially edit the normative target and PASS it in the same validation act.
- AUTHORING, EVIDENCE, PAIRED_VALIDATION, INDEPENDENT_AUDIT, OWNER_ACCEPTANCE and runtime activation remain distinguishable states.
- PMOV is independent from PMO but is not IVA.
- IVA remains organization-external.
- Validation depth follows the **current action and material risk**, not alarming words or future steps merely described inside a document.
- Hash/SHA identifies an exact target. `SHA_CHANGED` alone is not a validation-depth trigger.
- All active Personas load `11_COMMON_EXECUTION_VALIDATION_GUARD.md`; that guard governs shared planning, read-scope, progress, readback, correction, telemetry and persistence discipline without lowering this contract.

## Risk-adaptive routing

### FAST — default for plan/document review without mutation

Use FAST when the current task is document review, plan refinement, WBS/progress/arithmetic completion, or similar analysis and no repository/production/release/freeze/cutover/deletion/publication action is actually being executed.

Default rule:

`PLAN_REVIEW + NO_MUTATION => FAST`

The presence of `migration`, `public`, `production`, `deletion`, `cutover`, `rollback`, `Git`, or similar terms in the reviewed document does not itself escalate the current task.

FAST validation scope is limited to the acceptance criteria actually needed for the output, normally:
- source-plan misinterpretation;
- material omission or contradiction;
- sequencing errors;
- arithmetic / effort / compute / weight / progress consistency;
- authority or Owner-right overclaim;
- clearly material factual mismatch against exact refs that the output itself relies on.

FAST operating rules:
- choose only validators materially relevant to the acceptance criteria; PMOV is the natural paired validator for PMO scope, but other relevant validators may be used when needed;
- when multiple validators are useful, prefer independent parallel role-scoped checks over serial whole-target re-reading;
- correction loops default to one targeted correction + one targeted recheck unless a material issue requires more;
- recheck after nonmaterial correction is changed diff / affected acceptance criteria only;
- repository-wide history/object scan is not default and is prohibited unless an acceptance criterion specifically requires it;
- specialist validators are added only for a material changed domain, not because that domain is merely mentioned in the plan.

All active Personas use task-specific stage estimates and Owner-check limits from the common guard rather than a universal fixed duration.

### STANDARD — bounded real mutation

Use STANDARD when the current action actually mutates bounded code/docs/Git state or another operational artifact but is reversible and not a high-impact release/destructive action.

Defaults:
- validators are chosen only from materially affected domains;
- diff-first validation;
- bounded correction loops declared for the task;
- exact-state/repository checks are scoped to the changed surface and acceptance criteria.

### FULL — high-impact execution

Use FULL for actual high-impact actions such as:
- private-to-public publication/cutover;
- source deletion or destructive decommission;
- production/release/freeze activation;
- security/privacy/legal high-impact mutation;
- material authority or organization cutover;
- other explicitly required independent-audit gates.

FULL may use multiple paired validators and IVA when the active gate requires them. Before expanding an existing FAST/STANDARD task into FULL, the responsible Persona/PMO reports the escalation reason, validators required, and additional work to the Owner unless an emergency/standing Owner authorization explicitly permits immediate escalation.

## Frozen-target and finding discipline

For bounded substantive validation, prefer:

`AUTHORING -> D0 FREEZE -> ROLE-SCOPED VALIDATION -> FINDING FREEZE -> BOUNDED CORRECTION -> AFFECTED-DIFF RECHECK`

Do not keep moving the target while independent validators are reviewing different versions.

## Revalidation rule

- `NONMATERIAL_CHANGE => DIFF_ONLY_RECHECK`.
- A new SHA invalidates byte-identical identity of an earlier receipt but does not automatically invalidate unaffected semantic findings.
- Full revalidation is required only when the changed content can materially affect previously validated acceptance criteria, authority, execution safety, or exact-state conclusions.
- `MATERIAL_LOCAL` changes route to affected domains/criteria.
- `MATERIAL_GLOBAL` changes require a broader-validation proposal before silent expansion.

## Validator role guard

Validators identify defects against the target acceptance criteria. They may provide advisory improvement suggestions, but a suggestion does not become a blocking requirement unless it is required by current authority/contract, the declared acceptance criteria, or a newly authorized scope change.

Validators must not become routine co-designers of the target under validation. New control architectures, publication gates, rollback schemes, branch-protection regimes, or similar mechanisms discovered during review are advisory unless the current task actually requires them.

## Context-efficiency and current-state rule

Validator input defaults to exact target, acceptance criteria, source refs and required context only. Author persuasive narrative is not default preload. Prefer delta packets, role-scoped context and lazy history loading; do not repeatedly reload full project/repository history when a narrower exact context is sufficient.

Narrow-first reading does not permit stale completion. For substantive frozen/persistent outputs, perform bounded current-state readback before candidate freeze and completion as defined by the common guard.

## Telemetry and completion states

Substantive validation should separate, when available:
- context loading;
- direct review;
- finding integration;
- correction;
- recheck;
- parallel compute sum from non-overlapping wall-clock.

Missing splits remain unverified rather than retrospectively invented.

Keep `AUTHORING_COMPLETE`, `VALIDATION_COMPLETE`, `PERSISTENCE_COMPLETE`, `OWNER_ACCEPTED`, and `ACTIVATED` distinct. Local output or a progress bar at 100% does not itself establish persistent completion or validation PASS.

Active post-bootstrap routes:
- CONTROLV + PMOV: source/decision/preserve integrity.
- BYULV + CONTROLV: organization-registry and topology review.
- each paired validator: paired authority-contract review; CONTROLV checks shared invariants.
- CONTROLV + relevant validators + IVA: validation/audit architecture review.
- CONTROLV + ENGV: selector/memory/bootstrap runtime correctness.
- paired validators: predecessor-context succession and independence preservation.
- ENGV + CONTROLV technical fresh-channel validation; BYULV + PMOV + MODELV semantic recovery validation.
- PMOV + CONTROLV: PMO execution-control surfaces.
- all relevant paired validators + IVA: bootstrap/rollback package audit.
- PMOV + CONTROLV + IVA: WP9 active-pointer/post-switch audit.

These post-bootstrap routes describe their relevant QA/gate surfaces; they are not a blanket requirement to invoke all listed validators for unrelated FAST work.

Owner D3 WP9 activation establishes the organization and this contract as current runtime governance. It does not itself assert any paired or independent Validation PASS.

Owner tuning directions on 2026-08-25 and 2026-08-26 establish the risk-adaptive and all-Persona common operating rules above. These policy changes do not create a Validation PASS for any prior artifact.
