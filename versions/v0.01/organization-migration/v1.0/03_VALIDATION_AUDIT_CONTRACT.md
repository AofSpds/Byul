# Validation & Audit Contract

STATE = CANDIDATE / NOT_VALIDATED

Principles:
- Every substantive persistent author/executor has a paired validator.
- Author/Executor cannot self-grant final validation PASS.
- Validator cannot materially edit the normative target and PASS it in the same validation act.
- AUTHORING, EVIDENCE, PAIRED_VALIDATION, INDEPENDENT_AUDIT, OWNER_ACCEPTANCE, CUTOVER are separate states.
- PMOV is independent from PMO but is not IVA.

Mandatory routes for this migration:
- WP0: CONTROLV + PMOV source/decision/scope review.
- WP1: BYULV + CONTROLV.
- WP2: each paired validator validates its paired authority contract; shared invariants also CONTROLV.
- WP3: paired validation plus IVA independent audit MANDATORY.
- WP4: CONTROLV + ENGV.
- WP5: paired validators for each rematerialized context.
- WP6: ENGV + CONTROLV technical validation AND BYULV + PMOV + MODELV semantic recovery validation.
- WP7: PMOV + CONTROLV.
- WP8: all relevant paired validators plus IVA independent audit MANDATORY.
- WP9: not authorized; if later authorized, PMOV + CONTROLV + affected validators + IVA MANDATORY.

Validator input defaults to exact target, acceptance criteria, source refs, and required context only. Author persuasive narrative is not default preload.