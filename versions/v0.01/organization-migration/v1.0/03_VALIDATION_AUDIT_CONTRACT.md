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

FAST operating budget:
- paired validator: normally `0..1`; PMO output normally routes to PMOV only;
- target validation latency: `<= 5 minutes`;
- correction loops: one targeted correction + one targeted recheck by default;
- recheck after nonmaterial correction: changed diff / affected acceptance criteria only;
- repository-wide history/object scan: not default and prohibited unless an acceptance criterion specifically requires it;
- specialist validators are added only for a material changed domain, not because that domain is mentioned in the plan.

If a correct FAST conclusion cannot be reached inside the 5-minute validation target because a material defect or unresolved exact-state dependency is discovered, the validator/PMO must stop scope expansion and report the reason, additional validator need, and expected extra work before continuing into STANDARD/FULL.

### STANDARD — bounded real mutation

Use STANDARD when the current action actually mutates bounded code/docs/Git state or another operational artifact but is reversible and not a high-impact release/destructive action.

Defaults:
- validators: `1..2`, chosen only from materially affected domains;
- diff-first validation;
- one correction loop by default;
- exact-state/repository checks are scoped to the changed surface and acceptance criteria.

### FULL — high-impact execution

Use FULL for actual high-impact actions such as:
- private-to-public publication/cutover;
- source deletion or destructive decommission;
- production/release/freeze activation;
- security/privacy/legal high-impact mutation;
- material authority or organization cutover;
- other explicitly required independent-audit gates.

FULL may use multiple paired validators and IVA when the active gate requires them. Before expanding an existing FAST/STANDARD task into FULL, PMO reports the escalation reason, validators required, and additional work to the Owner unless an emergency/standing Owner authorization explicitly permits immediate escalation.

## Revalidation rule

- `NONMATERIAL_CHANGE => DIFF_ONLY_RECHECK`.
- A new SHA invalidates byte-identical identity of an earlier receipt but does not automatically invalidate unaffected semantic findings.
- Full revalidation is required only when the changed content can materially affect previously validated acceptance criteria, authority, execution safety, or exact-state conclusions.

## Validator role guard

Validators identify defects against the target acceptance criteria. They may provide advisory improvement suggestions, but a suggestion does not become a blocking requirement unless it is required by current authority/contract, the declared acceptance criteria, or a newly authorized scope change.

Validators must not become routine co-designers of the target under validation. New control architectures, publication gates, rollback schemes, branch-protection regimes, or similar mechanisms discovered during review are advisory unless the current task actually requires them.

## Context-efficiency rule

Validator input defaults to exact target, acceptance criteria, source refs and required context only. Author persuasive narrative is not default preload. Prefer delta packets, role-scoped context and lazy history loading; do not repeatedly reload full project/repository history when a narrower exact context is sufficient.

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

Owner tuning direction on 2026-08-25 establishes the risk-adaptive routing above to prevent validation scope overexpansion and small-task latency regression. This policy change does not create a Validation PASS for any prior artifact.