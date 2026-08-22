# 25. Item 8 PASS — Dual Primary Owner-Facing Structure — 2026-08-22 21:01 KST

STATUS = OWNER_DECISION / BYUL_MIGRATION_REVIEW / ITEM_8_PASS / NON_NORMATIVE
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE

## Owner Decision

Item 8 is PASS.

The prior single-owner-facing-PMO model is rejected for BYUL.

## Confirmed Owner-Facing Top Structure

BYUL shall separate planning/design and execution control at the top level.

Temporary migration roles:

- `ASA-MI` = Channel Pro planning / architecture / design surface.
- `ASA-ME` = ChatGPT WORK Ultra execution PMO surface.

Post-migration BYUL-native structure shall provide distinct functions for:

1. Planning / Design Primary — NAME TBD.
2. Planning / Design Paired Validator.
3. Execution PMO Primary.
4. PMO Paired Validator.
5. Organization-external Independent Validator / Auditor.

All five functions are Owner-facing. Worker Agent Threads are subordinate execution units and are not the normal Owner-facing surface.

## Structural Firewall

- Planning / Design owns research direction, worldview/world-model architecture, experiment design and material design changes.
- PMO owns execution orchestration of approved plans, WORK Ultra parallelization, task/persona assignment, dependency/gate/progress control and consolidation.
- PMO must not silently mutate planning/design semantics during execution.
- Material design changes discovered during execution route back to Planning / Design and its paired Validator, with Owner decision where required.
- Each Primary has its own paired Validator with distinct validation duty.
- The organization-external Independent Validator/Auditor remains outside the BYUL authoring/execution organization and reports independently to Owner.
- Independent audit verdicts may not be rewritten by PMO consolidation.

## Naming Note

Using `BYUL` itself as the permanent Planning / Design Persona name remains open. A separate Persona name is tentatively preferred to avoid ambiguity between project identity and Persona recommendation/decision identity. Final naming remains a later organization-design decision.

## AAA Firewall

No AAA code, organization, Persona registry, authority, memory, worklog, Shared Contract, release or production state is modified by this checkpoint.
