# Owner Confirmation — Initial BYUL Persona Organization Shape — 2026-08-23 07:07 KST

STATUS = OWNER_DIRECTION
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE

## Confirmed decisions

1. RES is not a required initial persistent Persona. Research is initially absorbed into the existing organization and is a future split/test candidate if need emerges.
2. Independent Auditor exists as a separate role outside the paired Persona structure.
3. Canonical Persona names may use `BYUL`, `PMO`, `CONTROL`, `MODEL`, `ENG` directly; using BYUL as both project and Persona name is explicitly accepted by Owner.
4. Functional boundaries are confirmed:
   - CONTROL = Git/current state/evidence/artifact/authority/memory/control/lineage/governance-oriented domain.
   - MODEL = World Model/hypothesis/architecture/evaluation-design/model-scientific domain.
5. BYUL vs PMO boundary is confirmed:
   - BYUL = Owner-facing alter-ego / Planning-Design Primary / research-direction and model judgment surface.
   - PMO = execution decomposition, dispatch, dependency management, tracking, completion management.
   - conversational planning/research can occur outside PMO; once a task becomes execution, PMO manages execution.

## Initial organization shape

OWNER
  |
  v
BYUL ---- BYUL Validator
  |
  v
PMO ----- PMO Validator
  |
  +-- CONTROL ---- CONTROL Validator
  +-- MODEL ------ MODEL Validator
  +-- ENG -------- ENG Validator

Independent Auditor exists separately and is called when required by inherited governance/risk rules.

## Inherited principles

AAA organization/operating principles are inherited as the baseline, but BYUL is not required to copy AAA's exact Persona inventory or topology. All persistent Personas are paired with validators; Independent Auditor is the explicit external exception. Persona organization may later CREATE/SPLIT/MERGE/MUTATE/RETIRE under inherited governance. RES is the first explicit future split candidate.

## Migration mapping

ASA-MI -> BYUL
ASA-ME -> PMO

## Remaining design work

- Define exact canonical validator names/codes.
- Define detailed authority/scope contracts for BYUL/PMO/CONTROL/MODEL/ENG and validators.
- Define registry/bootstrap/memory paths and cutover artifacts.
- Define exact execution topology under PMO while preserving inherited AAA operating principles.
- Define RES split trigger/test criteria later.

No AAA repository or authority state was modified.
