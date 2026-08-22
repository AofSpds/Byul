# PRO Deep Research Handoff — Open-Source Pilot Workload Selection

STATUS = RESEARCH_HANDOFF / WORKING / NON_NORMATIVE / NOT_VALIDATED
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
AAA_MUTATION_AUTHORIZED = FALSE
EXECUTION_AUTHORIZED = FALSE

## Purpose
Prepare a Pro-mode adversarial deep-research pass to select and design one pilot open-source workload for empirical validation of BYUL. The pilot is part of the BYUL separation program, not a post-migration side project.

## Core Objective
Do not prove BYUL. Try to falsify or narrow it.

The pilot should test whether BYUL can safely and simply represent, mutate, split/fork, diverge, merge or refuse, preserve conflict/uncertainty/loss/provenance, and reconstruct lineage/state on a real external application workload. Compare against simpler structures where relevant. Valid outcomes include KEEP / MODIFY / REPLACE / PARTIAL_ADOPT / REFRAME / NON_CONCLUSION.

## Owner Direction
- Start with one pilot workload before scaling to multiple apps.
- Current preferred candidate from preliminary high-depth search: Grist, but this is NOT frozen and MUST be independently challenged.
- Memos was an earlier proposal, not an Owner-selected workload.
- If another project offers higher information gain per implementation cost, recommend it.
- Organization/execution methodology is deferred until AAA provides a separate plan.
- Any decisions that depend on the separately running BYUL process must be re-asked after that process finishes.

## Prior Proposal Baseline
Existing 26-page working proposal: `Byul_오픈소스앱_구현검증_통합제안서_PMO검토용.docx`.
Original structure:
- primary workload: Memos
- simpler architecture control: SilverBullet
- generalization: Vikunja
- candidate competition: C1 Hardened Git+Markdown / C2 Relational+Audit / C3 Minimal Byul
- lifecycle focus: MUTATE / SPLIT / DIVERGE / MERGE / MIGRATE / RECONSTRUCT
- hard gates, cold-read, holdout, ablation, no automatic canonization of 5-plane/7-object/preservation algebra/planner signature/stable identity.

This baseline is source material, not authority. The Pro review may replace Memos, reorder the ladder, or reject the entire proposed workload strategy.

## Preliminary Search Result — Challenge Required
Current preliminary ranking from Very High search:
1. Grist — strongest first-pilot candidate because fork/copy, common-ancestor comparison, proposal/merge, schema + data mutation, history/restore can generate native lifecycle pressure.
2. TriliumNext — strong identity/context stress: one note can appear under multiple branches/contexts; relations/attributes/history/sync provide lineage ambiguity.
3. Joplin — strong offline divergence/conflict/revision/reconstruction stress.
4. Vikunja — strong typed relation/task-state/generalization and representation-loss pressure.
Controls / secondary references:
- SilverBullet — simple Markdown source-of-truth + rebuildable derived index control.
- Memos — bounded CRUD/relations sanity control.
- Dolt — mature branch/merge database upper-bound reference, but risks testing a system that already embodies version-control semantics.
- AppFlowy — CRDT/concurrent collaboration adversarial ceiling; probably too mature/complex for first pilot.
- Penpot — component/instance inheritance + override/history stress; likely too large for first pilot.

The above ordering is a preliminary hypothesis only. Pro MUST search broadly enough to discover stronger alternatives and must not anchor on Grist.

## Proposed Pilot Shape if Grist Survives
Do NOT rebuild the full app. Define a bounded vertical slice around:
- one document
- table / row / column / reference / formula
- fork/copy into A and B
- A: schema mutation (rename/type/reference)
- B: data + formula mutation
- divergence
- compare/common ancestor
- merge OR safe refusal
- reconstruct original/A/B/final lineage and state

Observed success is NOT "merge always succeeds". Safe refusal, preserved conflict, visible loss, explicit UNKNOWN, reproducible lineage, and reconstruction are valid successes.

## Deep Research Questions
1. Is Grist truly the best first pilot when optimizing information gain / implementation cost / contamination risk?
2. Which native application semantics must be preserved for the pilot to remain a real Grist workload rather than a toy inspired by Grist?
3. What exact upstream commit should be pinned, and why is that commit suitable/stable enough for a pilot?
4. What are the minimal source files / schema / tests / API contracts that define the chosen slice?
5. Does the project license permit the intended experimental implementation and artifact handling?
6. Which lifecycle operations are native vs artificially introduced by us?
7. What counts as identity through fork/split/merge for the upstream app, and where should BYUL be allowed to return UNKNOWN?
8. What conflicts can be safely merged, what conflicts should be preserved, and what must be refused?
9. What native history/revision/reconstruction behavior can serve as reference evidence without turning upstream into a normative oracle for BYUL ontology?
10. What adapter boundary prevents the adapter/harness from silently implementing the semantics being tested?
11. What minimal mechanical observation envelope is candidate-neutral?
12. What fixture pack can create deterministic schema/data/relationship divergence and expected reconstruction outcomes?
13. What exact positive controls are needed so an always-refuse implementation cannot pass?
14. What exact negative/adversarial controls are needed so an always-merge implementation cannot pass?
15. Can simpler Git+manifest or relational+audit approaches satisfy the same slice with materially lower complexity?
16. What ablation would demonstrate that any extra BYUL primitive is actually necessary?
17. What metrics should be hard gates vs descriptive metrics?
18. What is the smallest pilot that still has enough semantic pressure to teach us something real?
19. What is the expected engineering effort, test effort, reasoning effort, and wall-clock if only one pilot is run?
20. What findings would justify stopping after the pilot versus expanding to Trilium/Joplin/Vikunja?

## Required Search Scope
Search GitHub/source/docs/issues/tests/changelogs for at least:
- `gristlabs/grist-core`
- `TriliumNext/Trilium`
- Joplin upstream repository and official technical docs
- Vikunja upstream repository and API/docs
- `usememos/memos`
- SilverBullet upstream repository/docs
- `dolthub/dolt`
- AppFlowy / AppFlowy-Collab
- Penpot

Also search for materially stronger alternatives outside this list. Do not restrict the search to note/task apps.

## Candidate Evaluation Axes
Score only after qualitative analysis. Suggested axes:
- Native lifecycle stress: MUTATE / FORK-SPLIT / DIVERGE / MERGE / RESTORE
- Identity/lineage ambiguity
- Conflict/concurrency richness
- Transformation/reconstruction depth
- Availability of deterministic reference evidence
- Bounded vertical-slice feasibility
- Adapter-shadowing risk
- Implementation/test cost
- License/source clarity
- Overfitting risk / whether upstream already solves the target semantics
- Generalizability beyond its own domain
- Ability to generate both positive and negative controls

Do not let a numeric aggregate hide a fatal weakness.

## Anti-Anchoring Rules
- Grist is a hypothesis, not a selection.
- Memos is historical proposal, not a baseline winner.
- Do not reward apps merely because they already implement Git/CRDT/version-control semantics elegantly.
- Do not choose the most complex app by default.
- Prefer a workload that creates high semantic information with a small executable slice.
- Safe refusal is allowed; always-refuse is not.
- Merge success is useful; always-merge is not.
- Provenance/history visibility does not itself prove semantic correctness.
- Upstream behavior is reference evidence, not BYUL ontology authority.
- Same-model consensus is not independent validation.
- UNKNOWN / NON_CONCLUSION are valid outcomes.

## Existing BYUL Research Constraints To Preserve
Current stronger surviving research constraints are narrower than any architecture proposal:
- source vs derived authority must remain visible
- material loss/provenance should remain observable
- unresolved conflict/uncertainty should not be silently coerced
- semantic admissibility/preservation obligations should constrain cost optimization
- lifecycle/lineage/succession should be explicit enough for audit/reconstruction
- current v0.1 is experimental baseline, not validated World Model
- no fixed 5-plane, 7-object kernel, preservation algebra, planner signature, ledger mandate, or stable essential identity is canonical

## BYUL Separation Context Relevant to This Research
Confirmed earlier:
- BYUL exists to advance AAA, but normal operation is separated; AAA does not routinely depend on BYUL state.
- This migration must not mutate AAA.
- ASA-MI currently handles migration planning/design; ASA-ME is current execution-PMO predecessor. These are temporary migration personas.
- Five Owner-facing interfaces are expected to remain stable while internal BYUL persona organization may split/merge/mutate. Exact organization/execution mechanics are deferred to a later AAA plan.
- BYUL validation/evidence states are its own; AAA PASS/release/production states do not transfer.
- Existing evidence may be preserved; validation status does not automatically transfer.
- BYUL research state/freeze/baseline control uses research lifecycle, not product Release/Production semantics.

## Deferred / Do Not Decide In This Pro Review
Do NOT finalize:
- Persona ↔ Channel binding
- parallel channel policy
- Agent Thread/Work Ultra execution topology
- validator channel topology
- independent-auditor execution method
- current semantic_surface branch migration/freeze/admission/final disposition
- anything dependent on the separately running BYUL process
These must be revisited after AAA provides organization/execution methodology and after the separate BYUL process finishes.

## Execution Boundary
This Pro task is RESEARCH + DESIGN REVIEW ONLY.
Do not implement the pilot, create candidate code, merge branches, alter AAA, or claim validation/selection.

## Required Deliverable
Return a decision-quality research packet with:
1. Executive verdict: best first pilot and confidence.
2. Strongest alternative and why it may be better.
3. Rejected candidates with explicit rejection reasons.
4. Exact upstream repository + recommended pinned commit/tag for top 2 candidates.
5. Architecture/code/data-model/lifecycle map for top 2.
6. Exact minimal vertical slice for the recommended pilot.
7. Native operation trace for MUTATE → FORK/SPLIT → DIVERGE → MERGE/REFUSE → RECONSTRUCT.
8. Reference/oracle boundary and anti-shadow-adapter rules.
9. Minimal fixture/test pack with positive + negative controls.
10. Simpler-control strategy and ablation plan.
11. Integrity/gameability risks and mitigations.
12. Estimated implementation/research/test resource range.
13. Stop/go criteria after the first pilot.
14. OPEN / UNKNOWN / NON_CONCLUSION items.
15. Final recommendation: PROCEED / MODIFY / REPLACE / REFRAME / NON_CONCLUSION.

## Source Locators
- Existing open-source proposal: `Byul_오픈소스앱_구현검증_통합제안서_PMO검토용.docx`
- BYUL repository: `AofSpds/Byul`
- Relevant historical research memory/checkpoints: `versions/v0.01/`
- Current migration decision records are appended under `versions/v0.01/memory/18+`.

## Research Standard
Use the highest available reasoning depth. Prior-art-first. Search broadly, challenge the supplied candidate list, and prefer falsifiable evidence over architectural elegance. The objective is to design the most informative single pilot, not to validate a preferred solution.
