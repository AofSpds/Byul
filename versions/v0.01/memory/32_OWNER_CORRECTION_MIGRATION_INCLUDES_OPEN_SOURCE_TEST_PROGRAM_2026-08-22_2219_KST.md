# 32. Owner Correction — BYUL Migration Includes Open-Source Test Program — 2026-08-22 22:19 KST

STATUS = OWNER_CORRECTION / BYUL_MIGRATION_SCOPE
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE

## Owner Correction

The previously discussed external/open-source project implementation test program is not a later unrelated follow-on. The Owner intended it to be designed and carried together with the BYUL separation/migration program.

Therefore:

- The open-source workload implementation/validation program remains IN-SCOPE for BYUL migration planning.
- It is not to be discarded or deferred merely because BYUL is being separated.
- The earlier integrated proposal (Memos primary workload, simpler controls such as SilverBullet, generalization workload such as Vikunja, lifecycle torture including MUTATE/SPLIT/MERGE, candidate competition, cold-read/holdout/ablation) remains a planning baseline to be revised against the final migration architecture.
- Current independent BYUL execution that is already running must not be interrupted or re-scoped by this correction. Its completion-dependent questions remain deferred until completion and must be re-asked.
- AAA organization/execution methodology is separately being re-planned. BYUL must wait for that plan before finalizing organization/execution-method details, but the open-source empirical implementation test remains part of the migration program scope.
- Migration planning should therefore distinguish:
  1. BYUL separation/bootstrap/governance/memory/control surface,
  2. BYUL empirical implementation/workload validation program,
  3. organization/execution methodology to be supplied/reviewed later,
  4. current already-running BYUL process whose final state is still pending.

## Correction to Previous Framing

Incorrect framing: treat open-source project implementation as a later optional successor after migration.

Correct framing: treat it as a co-designed workstream of the BYUL separation/migration program, while actual execution timing and final mechanics remain gated by the current running process and the forthcoming organization/execution-method plan.

## AAA Firewall

No AAA code, organization, Persona registry, authority, memory, Shared Contract, release, or production state is modified by this correction.
