# BYUL Runtime Bootstrap

Before substantive BYUL work:

1. Read repository-root `BYUL_BOOTSTRAP_CURRENT.json`.
2. Follow its current-state and active Persona-organization pointers.
3. Resolve `BYUL/BYULV/PMO/PMOV/CONTROL/CONTROLV/MODEL/MODELV/ENG/ENGV/IVA` through the active selector registry.
4. Load the common runtime view, then the selected Persona MEMORY/WORKLOG and current task/blocker refs.
5. State `CURRENT_PERSONA_LOCK = <BYUL Persona code>` before material work.
6. Git current state outranks memory, worklog, handoff, and chat context. Conflicts => `REVIEW_REQUIRED`.
7. Persona selector does not create authority.
8. Repository mutation requires a task-specific isolated branch/worktree; parallel workers use unique append-only run journals or isolated outputs rather than racing on shared memory/worklog files.
9. Post-bootstrap paired/IVA validation receipts are evidence when they exist; do not invent PASS states.
10. BYUL organization cutover does not imply model/worldview freeze, scientific validation, production authorization, or AAA mutation.

Default Persona when the Owner supplies no explicit selector and no proven BYUL Persona exists: `BYUL`.
