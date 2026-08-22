# 31. BYUL Persona Organization Plan & Migration Execution — Final Candidate — 2026-08-23

```text
STATUS = OWNER_REVIEW_FINAL_CANDIDATE / NON_NORMATIVE / NOT_VALIDATED
CURRENT_PERSONA = ASA-MI
PROJECT = BYUL
TASK = PERSONA_ORGANIZATION_PLAN_AND_MIGRATION_EXECUTION
AAA_MUTATION = PROHIBITED
RUNTIME_CUTOVER = NOT_AUTHORIZED
ACTIVE_BYUL_PROCESS_DEPENDENCY = REASK_REQUIRED_AFTER_COMPLETION
```

## Owner-confirmed organization decisions

- AAA organization/operating skeleton is inherited, but BYUL does not copy AAA mechanically.
- CORE A / CORE B grouping is removed.
- Initial Primary Personas: `BYUL`, `PMO`, `CONTROL`, `MODEL`, `ENG`.
- Every internal Primary Persona has a paired Validator: `BYULV`, `PMOV`, `CONTROLV`, `MODELV`, `ENGV`.
- `IVA` exists outside the organization as Independent Auditor and is not a paired Validator.
- `BYUL` is the Owner avatar / planning-design Persona and successor to `ASA-MI`.
- `PMO` manages all actual execution and is successor to `ASA-ME`.
- `CONTROL` owns current state/evidence/artifact/authority/memory/continuity/registry/bootstrap/control.
- `MODEL` owns World Model/hypothesis/architecture/evaluation design/scientific interpretation.
- `ENG` owns implementation/test/tooling/reproducibility.
- `RES` is not created initially; it is a future split-test target and must be paired with `RESV` if created.
- Owner-facing stable interfaces: `BYUL`, `BYULV`, `PMO`, `PMOV`, `IVA`.
- Internal Persona organization may CREATE / SPLIT / MERGE / MUTATE / RETIRE with explicit lineage.

## Deep-review verdict

```text
ORGANIZATION_DESIGN = READY_FOR_OWNER_APPROVAL
EXECUTION_PLAN = READY_FOR_STAGED_EXECUTION_APPROVAL
CUTOVER = BLOCKED
BLOCKER = CURRENT_SEPARATE_BYUL_PROCESS_COMPLETION_AND_EXACT_RECONCILIATION
INDEPENDENT_VALIDATION_CLAIM = NONE
```

No new blocking design contradiction was found in the proposed initial organization. The recommended minimum is 5 Primary Personas + 5 paired Validators + 1 organization-external Auditor. A full AAA clone was rejected as over-organization; BYUL+PMO-only was rejected as insufficient separation of control/model/engineering authority and validation.

## Final document identities

### Organization plan

```text
FILE = BYUL_조직기획_v1.0_2026-08-23.docx
SHA256 = 9a5ea68c5d84bfde44feb16365a5a36657e81fbeeac31a2195fab439225f8156
STATUS = OWNER-REVIEW FINAL CANDIDATE / NOT ACTIVE
PAGES_RENDERED_AND_VISUALLY_REVIEWED = 9
```

### Migration execution plan

```text
FILE = BYUL_조직이관실행_v1.0_2026-08-23.docx
SHA256 = 2fe5449ca3aaab5816df7a86da7cd4fdc955095ccec5a01a63d8b0459ef243b1
STATUS = OWNER-REVIEW FINAL CANDIDATE / EXECUTION NOT AUTHORIZED
PAGES_RENDERED_AND_VISUALLY_REVIEWED = 9
```

## Execution route

1. Owner approves organization and staged execution plans.
2. Pre-cutover control-plane skeleton may be built without activating current selectors/pointers.
3. Current separate BYUL process must finish first.
4. After completion, read exact branch/commit/status and re-ask Owner for reconciliation/baseline decisions.
5. Materialize Organization Manifest, Persona/Selector Registries, Memory Index, Persona Contracts, Common/Persona Memory and Worklogs.
6. Materialize succession: `ASA-MI → BYUL`, `ASA-ME → PMO`; predecessor aliases remain false.
7. Run continuity/selector/dispatch/isolation/rollback dry-runs.
8. Obtain paired validation receipts, PMOV execution audit and IVA cutover audit or explicit Owner disposition.
9. Owner approves exact cutover manifest.
10. Activate BYUL-native selectors/pointers, archive predecessors, and run stabilization observation.

## Hard boundary

This checkpoint does not authorize implementation, selector activation, branch reconciliation, cutover, validation PASS, release, production, or any AAA mutation.
