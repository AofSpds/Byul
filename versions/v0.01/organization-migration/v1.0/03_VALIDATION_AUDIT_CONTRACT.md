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

Validator input defaults to exact target, acceptance criteria, source refs and required context only. Author persuasive narrative is not default preload.

Owner D3 WP9 activation establishes the organization and this contract as current runtime governance. It does not itself assert any paired or independent Validation PASS.
