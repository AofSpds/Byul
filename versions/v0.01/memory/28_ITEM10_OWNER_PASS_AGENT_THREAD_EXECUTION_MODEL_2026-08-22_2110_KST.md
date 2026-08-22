# 28. Item 10 Owner PASS — Persona-Injected Agent Thread Execution Model — 2026-08-22 21:10 KST

STATUS = OWNER_DECISION / ITEM_10_PASS / BYUL_MIGRATION_REVIEW
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE

## Owner Decision

Item 10 is PASS.

## Confirmed Execution Model

- Persona and Agent Thread are distinct.
- Persona is the persistent organizational identity / role / responsibility surface.
- Agent Thread is a bounded execution instance created for a specific Work Packet using a frozen Persona revision/snapshot.
- Internal BYUL Personas may split, merge, mutate, specialize, retire, or be created as needed.
- A running Thread retains the Persona revision with which it was instantiated; later Persona mutation does not retroactively rewrite the running Thread identity.
- Thread authority is bounded by both Persona authority and the Work Packet authorized scope.
- Substantive authoring/execution routes through the relevant paired Validator Persona; mechanical sub-operations need not each spawn a separate validator instance if their evidence remains reviewable in the validation chain.
- Each Thread uses a unique append-only Run Journal and, when mutating repository state, a task-specific isolated branch/worktree.
- Parallel Threads do not directly race-write shared Persona Memory/Worklog. They return memory candidates for later consolidation.
- Subthreads are allowed but inherit a scope no broader than the parent Thread.
- COMPLETED and PERSISTED are distinct; a result is not durably complete until result/journal/artifact refs are persisted and remotely verifiable where required.
- BLOCKED / REVIEW_REQUIRED are valid outcomes.
- Agent Threads are internal execution units and are not Owner-facing interfaces by default.

## Compact Principles

`PERSONA != AGENT_THREAD`

`PERSONA_MAY_MUTATE; RUNNING_THREAD_IDENTITY_DOES_NOT`

`THREAD_JOURNAL -> MEMORY_CANDIDATE -> PERSONA_MEMORY`

## AAA Firewall

No AAA code, organization, Persona registry, authority, memory, Shared Contract, release, or production state is modified by this decision.
