# 22. BYUL Persona Orchestration Inheritance — 2026-08-22 20:34 KST

STATUS = OWNER_DIRECTION / MIGRATION_DESIGN_INPUT / NON_NORMATIVE
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE

## Owner Direction

1. BYUL shall design its new native Persona organization by studying and reusing the **basic orchestration concepts and operating concepts** of the current AAA Persona organization.
2. This is a transfer of orchestration principles and operating patterns, not a copy or mutation of the AAA organization itself.
3. Important rules that must survive the migration include, at minimum, the **paired validator principle**: substantive authoring/execution Personas are paired with a dedicated Validator Persona.
4. The final BYUL Persona names, role boundaries, and organization shape should be designed for BYUL's world-model / worldview / model empirical-validation mission rather than mechanically cloning AAA role names.
5. `ASA-MI` remains the temporary BYUL migration planning/design Persona and `ASA-ME` remains the temporary execution Persona. They are predecessors, not the final BYUL-native organization.
6. After migration, new BYUL-native Personas succeed the relevant planning/execution context; ASA-MI/ASA-ME remain only as AAA-side backup/historical recovery state.
7. No AAA code, organization, Persona registry, authority, memory structure, Shared Contract, release, or production state may be modified by this migration work.

## AAA Orchestration Principles To Evaluate For BYUL Transfer

The BYUL design review shall explicitly evaluate and preserve or adapt these AAA-derived operating principles:

- Owner final decision authority.
- PMO as orchestration/control surface rather than domain semantic author.
- Author/Executor Persona paired with dedicated Validator Persona.
- Author and Validator remain independent; author cannot self-issue substantive validation PASS.
- Independent audit layer for high-impact / program-critical decisions when warranted.
- `TEST_PASS != VALIDATION_PASS != OWNER_ACCEPTANCE` state separation.
- `Persona != Channel != Branch/Worktree`.
- Default parallel execution through Persona-injected Agent Threads; separate long-lived visible channels are exception-only.
- Task-specific isolation for mutating code-agent work.
- Unique append-only Run Journal per parallel thread; no shared mutable memory/worklog race.
- Persistent Work Packet / Checkpoint / Return Packet / exact artifact refs as communication bus.
- PMO consolidation before Owner escalation; Owner is not a manual relay among worker Personas.
- Persona memory continuity with task-specific memory candidates consolidated after execution.
- Exact target / authorized scope / preserve-others discipline for material changes.
- Uncertainty, blocker, conflict, and non-conclusion states remain explicit rather than being silently resolved.

## Item-3 Review Consequence

Item No.3 should no longer be treated mainly as a namespace-prefix question. The substantive decision is:

`DESIGN A UNIQUE BYUL-NATIVE PERSONA ORGANIZATION USING AAA ORCHESTRATION PRINCIPLES AS THE OPERATING REFERENCE MODEL, WHILE ADAPTING ROLE DOMAINS TO BYUL'S OWN RESEARCH/EMPIRICAL-VALIDATION MISSION.`

Exact Persona names and final domain count remain open for the dedicated BYUL organization-design step.
