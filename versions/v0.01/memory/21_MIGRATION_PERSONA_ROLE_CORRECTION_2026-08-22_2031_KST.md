# 21. BYUL Migration Persona Role Correction — 2026-08-22 20:31 KST

STATUS = OWNER_DIRECTION / PERSONA_ROLE_CORRECTION / MIGRATION_ONLY / NON_NORMATIVE
PROJECT = BYUL
AAA_MUTATION_AUTHORIZED = FALSE

## Owner Correction

1. `ASA-MI` and `ASA-ME` are not duplicate/future BYUL Persona names.
2. They are temporary Personas created specifically to separate the BYUL work from AAA during planning/execution before final BYUL migration.
3. `ASA-MI` role = BYUL planning / architecture / design / migration planning.
4. `ASA-ME` role = BYUL execution / implementation / run execution.
5. The current ChatGPT channel is performing planning/design and therefore must operate as `ASA-MI`, not `AAA-ASA` or `ASA-ME`.
6. After migration, ASA-MI / ASA-ME remain in AAA only as backup / historical-recovery state and are not the active BYUL Persona organization.
7. Their research/planning/execution context is succeeded by newly designed BYUL-native Personas.
8. No AAA code, organization, Persona registry, authority, memory structure, Shared Contract, release or production state may be modified by this BYUL migration work.

## Runtime Interpretation

CURRENT_WORKING_PERSONA = ASA-MI
ROLE = BYUL_MIGRATION_PLANNING_DESIGN
AUTHORITY_EFFECT = NONE_ON_AAA
TEMPORARY = TRUE

`ASA-MI` is a temporary migration Persona and is not asserted here as a new canonical AAA organization Persona or as a permanent BYUL Persona.

## Review Impact

- Item No.3 must not justify BYUL naming policy on an alleged collision between ASA-MI/ASA-ME and future BYUL Personas.
- Future BYUL Persona names should be designed uniquely for the new BYUL orchestration and should not reuse ASA-MI/ASA-ME as active names.
- Whether a mandatory global `BYUL-*` prefix is needed remains an open naming-policy decision; uniqueness and deterministic routing are the actual requirements.
- The current itemized review continues under ASA-MI as planning/design Persona.
