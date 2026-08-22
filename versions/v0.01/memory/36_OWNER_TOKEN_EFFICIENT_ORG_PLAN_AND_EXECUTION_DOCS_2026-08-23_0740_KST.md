# Owner Direction — Token-Efficient BYUL Organization Planning & Execution Documents — 2026-08-23 07:40 KST

STATUS = OWNER_DIRECTION / DOCUMENTATION_COMPLETE_CANDIDATE
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE
IMPLEMENTATION_AUTHORIZED = FALSE

## Owner direction

- BYUL Persona organization migration planning/execution documents should minimize unnecessary token use without reducing correctness, validation independence, or preservation requirements.
- Use a single canonical source/decision register, delta packets, role-scoped validator context, compact runtime views, and lazy history loading rather than repeatedly injecting the full project history.
- The user requested final documentation of both the organization plan and the execution plan.

## Final document set created in current channel

1. `BYUL_Org_Plan_v1.0_2026-08-23.docx`
   - Initial organization: BYUL/BYULV, PMO/PMOV, CONTROL/CONTROLV, MODEL/MODELV, ENG/ENGV, organization-external IVA.
   - CORE A/B removed.
   - RES not created initially; future split-test candidate.
   - ASA-MI -> BYUL; ASA-ME -> PMO.
   - Includes authority boundaries, validation architecture, operating model, RES split rule, memory/succession, token-efficient runtime contract, Owner-reserved boundaries, and deferred cutover conditions.

2. `BYUL_Org_Execution_v1.0_2026-08-23.docx`
   - PMO execution architecture WP0-WP9.
   - WP0-WP8 prepare/validate through CUTOVER_READY.
   - WP9 actual cutover remains Owner-reserved and blocked until the separate running BYUL process completes and exact Git state is re-reviewed.
   - Includes artifacts, fresh-channel verification, risk/rollback controls, Owner gates, resource ranges, and Owner decision block.

## Token-efficient runtime planning targets

- Common Runtime View: approximately <= 1,500 tokens by default.
- Persona Runtime View: approximately <= 1,200 tokens by default.
- Work Packet: approximately <= 1,500 tokens by default.
- Return Packet: approximately <= 1,000 tokens by default.
- PMO Master Status: one page / approximately <= 800 tokens by default.
- These are design targets, not hard limits. P0/high-impact work may expand when required for correctness.

## Important claim limits

- No Validation PASS is created by these documents.
- No cutover is authorized.
- No current running BYUL branch/baseline/evidence disposition is decided.
- No AAA repository, organization, memory, or authority state is modified.

## Next route

Owner reviews the two final DOCX candidates. If accepted, D1 organization-plan approval and D2 authorization for WP0-WP8 may be issued. D3 cutover remains deferred until the separate BYUL execution process completes and exact-state review is performed.
