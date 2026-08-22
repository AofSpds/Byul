# 30. ASA-MI Channel Succession — Open-Source Candidate Discussion / Interview — 2026-08-22 23:16 KST

```text
STATUS = CHANNEL_SUCCESSION_CHECKPOINT / BYUL_MIGRATION_PLANNING / NON_NORMATIVE / NOT_VALIDATED
PROJECT = BYUL
FROM_PERSONA = ASA-MI
TO_PERSONA = ASA-MI
CURRENT_PERSONA_LOCK = ASA-MI
ROLE = BYUL Migration Planning / Architecture / Design
IMPLEMENTATION_AUTHORIZED = FALSE
AAA_MUTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## 0. Owner next-channel intent

- Move to a successor channel under the same temporary migration persona `ASA-MI`.
- The next channel is for **candidate-by-candidate discussion/interview**, not implementation.
- Continue examining open-source empirical pilot candidates without treating the current Grist recommendation as selected/canonical.
- Ask and resolve candidate questions one by one; preserve anti-confirmation-bias posture.

## 1. Current role split during migration

- `ASA-MI` = Channel Pro planning/design surface for BYUL migration and pilot design.
- `ASA-ME` = predecessor execution/PMO surface using ChatGPT WORK Ultra.
- These are temporary migration personas, not permanent BYUL-native personas.
- BYUL-native successor personas will later inherit relevant context.

## 2. BYUL / AAA relationship — settled direction

- BYUL exists to advance AAA through worldview / world-model / model empirical-validation research.
- BYUL normal operation is context/execution separated from AAA.
- AAA routine operation does not need to know BYUL status.
- BYUL planning/design may reference exact persisted AAA artifacts read-only when genuinely needed.
- BYUL migration must not mutate AAA code, organization, persona registry, memory, governance, release, production, or Shared Contract state.
- Any future application of BYUL results to AAA is a separate future AAA-side program.

## 3. Owner-facing interface direction

Current Owner direction is approximately five stable external interfaces:

1. Planning / Design Primary
2. Planning / Design Validator
3. Execution PMO
4. PMO Validator
5. Organization-external Independent Validator/Auditor

These are primarily stable Owner-facing interfaces, not a frozen internal topology.
Internal BYUL personas may CREATE / SPLIT / MERGE / MUTATE / RETIRE as needed.

Exact organization and execution methodology are NOT to be finalized here: Owner will provide a separate AAA-side plan, after which BYUL will re-plan its own organization/execution method.

## 4. Migration-review status relevant to successor

Owner-confirmed/pass items include:

- BYUL purpose-coupled but operationally separated from AAA.
- Zero AAA mutation during migration.
- ASA-MI/ASA-ME are temporary predecessor personas.
- Validation methodology may transfer; AAA validation/authority states do not.
- AAA reference is optional planning-only, read-only exact artifact reference.
- BYUL memory succession should use BYUL persistent Git context; persona identity itself does not migrate.
- BYUL research lifecycle should use lightweight research state/freeze/selected-baseline control, not AAA product release/production authority.
- Owner-facing interfaces are stable while internal personas remain mutable.

Important deferments:

- Persona ↔ Channel binding, parallel-channel policy, visible-channel topology, validator execution surface, independent-auditor execution mechanism, PMO orchestration details, and broader organization/execution methodology are deferred pending Owner's separate AAA plan.
- Item 10 Agent-Thread model has historical PASS evidence, but operational application is deferred pending the new AAA plan.
- Anything dependent on the separately running BYUL process must be re-asked after that process finishes; do not pre-decide branch handling, merge, freeze, baseline admission, successor start point, or evidence disposition.

## 5. Open-source empirical-validation program relation to migration

Owner correction:

- The open-source application test program is not a distant side project after separation.
- It is a workstream of the BYUL separation program itself.
- However actual execution timing must be re-confirmed after current separate BYUL work and after organization/execution methodology is supplied.

Conceptual tracks:

- Track A: BYUL independence / migration
- Track B: external-workload empirical validation
- Track C: organization/execution re-planning after AAA plan
- Track D: reconciliation after current separate BYUL execution completes

## 6. Empirical-validation purpose

Wrong objective:

`reimplement an open-source app using BYUL`

Correct objective:

Use real external application semantics to falsifiably test whether BYUL candidates can safely and simply represent and preserve:

- state
- relation
- mutation
- split/fork
- divergence
- merge
- safe refusal
- conflict
- UNKNOWN
- lineage
- reconstruction

Allowed conclusions include:

- KEEP
- MODIFY
- PARTIAL_ADOPT
- REPLACE
- REFRAME
- NON_CONCLUSION

The experiment must be able to show BYUL is unnecessary or overly complex.

## 7. Owner's special interest

A major target is freedom/quality of:

`MUTATE -> SPLIT/FORK -> DIVERGE -> MERGE -> RECONSTRUCT`

But good behavior is not `ALWAYS_MERGE`.

Valid outcomes may include:

- MERGE
- SAFE_REFUSAL
- CONFLICT
- UNKNOWN
- LOSS_DISCLOSED
- LINEAGE_RECONSTRUCTED

Degenerate candidates to reject:

- ALWAYS_MERGE
- ALWAYS_REFUSE
- ALWAYS_UNKNOWN
- ALWAYS_CONFLICT

Both resolvable and non-resolvable fixtures are required.

## 8. Original proposal baseline

Original PMO-reviewed proposal:

`Byul_오픈소스앱_구현검증_통합제안서_PMO검토용.docx`

Original structure:

- Memos = primary workload
- SilverBullet = simpler architecture control
- Vikunja = generalization workload
- candidate competition = C1 Hardened Git+Markdown / C2 Relational+Audit / C3 Minimal Byul

This proposal remains useful as working prior design, but is not normative or validated.

## 9. Very-High search result before Pro review

Broadened candidate set:

- Grist
- TriliumNext
- Joplin
- Vikunja
- Memos
- SilverBullet
- Dolt
- AppFlowy
- Penpot

Very-High preliminary result promoted Grist and demoted Memos/SilverBullet toward sanity/control roles.

## 10. Pro deep-research verdict — current most important research artifact

Canonical current working research verdict:

PATH =
`versions/v0.01/memory/29_PRO_DEEP_RESEARCH_SINGLE_OPEN_SOURCE_PILOT_VERDICT_2026-08-22.md`

COMMIT =
`f31a51d1ae57573aa136e47b2f9511e36eb0cdd3`

Status:

- RESEARCH_VERDICT
- NON_NORMATIVE
- NOT_VALIDATED
- IMPLEMENTATION_AUTHORIZED = FALSE
- SELECTION_STATE = WORKING_RECOMMENDATION

Current route:

`PROCEED_WITH_MODIFIED_GRIST_PILOT`

Confidence:

`MODERATE_HIGH / 0.76`

## 11. Grist — current first recommendation, NOT selected

Pinned source in Pro review:

```text
REPOSITORY = gristlabs/grist-core
LICENSE = Apache-2.0
PINNED_RELEASE = v1.7.17
PINNED_COMMIT = fe672818f879c86d2d145f3f30cb30f106e15f1a
```

Critical exact-source finding:

- fork/history/common-ancestor/diff/proposal surfaces are strong and real.
- native patch/semantic merge path is limited and partial; it must NOT be treated as semantic correctness oracle.
- source explicitly describes patch implementation as `Incomplete and naive`.
- proposal-side structural rename handling is limited/rejected; formula/hidden behavior and partial apply risks require preflight tests.

Reframed Grist role:

`FIXTURE GENERATOR + NATIVE CALIBRATION`, not `ANSWER/ORACLE`.

Why it remains first:

One bounded real workload can combine:

- table / row
- typed columns
- formulas
- references
- document fork
- common ancestor
- independent mutation
- proposal/diff/apply
- history/reconstruction pressure

## 12. Strongest alternative — Joplin

Pinned source in Pro review:

```text
REPOSITORY = laurent22/joplin
DEFAULT_LICENSE = AGPL-3.0-or-later, subject to subtree licenses
PINNED_RELEASE = Desktop v3.6.15
PINNED_COMMIT = c61572660382863595c6b51ccf2263e3d2c4bfce
```

Joplin is strongest when the primary question is:

`Can BYUL preserve conflict, UNKNOWN, and reconstruct history without unsafe merge?`

Strengths:

- offline divergence
- explicit conflict preservation
- local/remote state separation
- revision-chain reconstruction
- restore behavior

Weakness versus Grist for current Owner interest:

- weaker explicit native `fork -> proposal -> positive merge` path.

## 13. TriliumNext — identity specialist

Current role:

`SECOND-PHASE IDENTITY STRESS`

Important property:

- one note may appear under multiple parents via branches/clones.
- note identity and branch identity differ.
- last strong branch deletion can delete the note.
- clone is the same note under another branch/context, not an independent content fork.

Excellent for context-dependent/derived identity, but weaker as first independent-divergence/merge workload.

## 14. Other candidate dispositions

- Dolt = upper-bound calibration; risk of answer leakage because version-control semantics are the product itself.
- SilverBullet = strong simpler-control prior art; Markdown source of truth + rebuildable derived index pressure.
- Memos = low-cost CRUD/relation sanity control.
- Vikunja = later cross-domain generalization.
- AppFlowy = later CRDT/concurrency adversarial ceiling.
- Penpot = later inheritance/override/component-instance stress.

## 15. Modified Grist pilot hypothesis

Do NOT implement yet.

If Grist remains selected after discussion/interview and required gates:

Base document candidate:

```text
Category
- id
- label

Item
- id
- name
- category_ref -> Category
- amount
- score_formula
```

Lifecycle:

```text
S0
├─ TRUNK A
└─ FORK B

A MUTATE
B MUTATE

A' + B'
-> COMPARE
-> MERGE / SAFE_REFUSAL / CONFLICT / UNKNOWN
-> RECONSTRUCT S0, A', B', RESULT
```

## 16. Required Grist fixture ideas from Pro review

Positive controls:

1. Disjoint row updates -> merge should succeed.
2. Resolvable rename lineage -> fork data edit should follow explicit trunk column rename.

Negative/adversarial controls:

3. Same-cell incompatible writes -> conflict/refusal, no silent overwrite.
4. Delete referenced entity vs add/use reference -> no dangling silent merge.
5. Formula/input dependency ambiguity.
6. Proposal-side structural mutation -> explicit unsupported/refusal, no silent skip.
7. Mixed valid + invalid patch -> partial apply must not masquerade as total success.
8. Missing/truncated common history -> UNKNOWN/unrelated, no invented lineage.
9. Replay/reconstruction hash verification.

## 17. Pro-recommended first-pilot competition

Do not start the full C1/C2/C3 tournament first.

First compare only:

### S0 simpler control

- content-addressed snapshots
- immutable operation/receipt log
- explicit preconditions
- deterministic reducer
- conflict/UNKNOWN state

### B1 minimal BYUL candidate

Only currently justified capabilities:

- provenance visibility
- explicit material loss
- conflict/UNKNOWN preservation
- lifecycle lineage
- semantic admissibility before cost
- deterministic reconstruction

No assumption of:

- fixed 5-plane architecture
- fixed object count
- mandatory ledger
- canonical planner signature
- stable essential identity

The simpler control must be allowed to win.

## 18. Adapter purity

Adapter may only:

- serialize exact upstream state/actions
- map identifiers mechanically
- preserve native fields/bytes
- declare unsupported/unmappable

Adapter must not:

- detect/resolve conflict
- infer lineage
- choose merge order
- repair references
- judge semantic admissibility
- synthesize missing history

Otherwise it becomes a shadow candidate and invalidates the experiment.

## 19. Preflight before any full implementation

Pro recommends Grist upstream-only preflight first, with three adversarial tests:

1. same-cell incompatible edit
2. mixed valid/invalid partial patch
3. proposal-side structural/formula mutation

Preflight stop/reframe if:

- pinned upstream is not deterministic/reproducible;
- semantic logic must be moved into adapter to extract fixtures;
- fewer than 3 meaningful discriminating cases survive;
- harness is larger than both candidates combined;
- simpler control cannot be defined without importing BYUL assumptions.

Planning estimate only:

- preflight: 0.5–1.5 engineer-days
- full first pilot after GO: roughly 8–15 engineer-days / 5–9 wall-clock days with safe parallelization

Organization/Persona/Work-Ultra/independent-validation costs are not included.

## 20. What one pilot may and may not establish

May establish:

- whether the experiment discriminates candidate behavior;
- how a candidate fails on frozen cases;
- whether BYUL adds capability over simpler control;
- whether some capability survives ablation;
- which next workload is needed.

May NOT establish:

- universal World Model validity;
- canonical architecture;
- mandatory ledger/planner/object set;
- production readiness;
- automatic AAA adoption;
- scientific truth.

## 21. Next-channel mission

The next channel should NOT jump to Grist implementation.

Primary mission:

`NEXT CANDIDATE DISCUSSION / INTERVIEW`

Recommended sequence unless Owner directs otherwise:

1. Start with **Joplin** as strongest alternative.
2. Explain its actual workload semantics in intuitive Korean.
3. Ask Owner what part of that behavior is most useful/interesting for BYUL.
4. Compare it directly against Grist only after Owner has formed a view.
5. Then interview **TriliumNext** for identity/context stress.
6. Continue candidate-by-candidate; do not collapse everything into a score too early.

The goal is not to make Owner approve a preselected ranking. The goal is to expose each candidate's distinct failure-information profile so Owner can refine the experiment objective.

## 22. Interview style for successor

- Korean first.
- Explain one candidate at a time.
- Easy intuition -> small concrete example -> deeper semantic implications.
- Avoid excessive English terminology.
- Ask one substantive question at a time when eliciting Owner preference/judgment.
- Distinguish clearly:
  - upstream/source fact
  - current inference
  - working hypothesis
  - Owner direction
  - OPEN / UNKNOWN
- PRIOR-ART-FIRST.
- Never treat Owner recognition as empirical validation.
- Keep solution non-locking.

## 23. Important non-actions

Until Owner explicitly authorizes otherwise:

- no pilot implementation;
- no Grist candidate freeze;
- no branch merge/rebase of current separate BYUL work;
- no AAA mutation;
- no organization/execution topology freeze;
- no claim that Grist is selected/canonical;
- no validation/production/release claim.

## 24. Recovery order for successor ASA-MI channel

Read:

1. `versions/v0.01/memory/29_PRO_DEEP_RESEARCH_SINGLE_OPEN_SOURCE_PILOT_VERDICT_2026-08-22.md`
2. this checkpoint `versions/v0.01/memory/30_ASA_MI_CHANNEL_SUCCESSION_OPEN_SOURCE_CANDIDATE_DISCUSSION_2026-08-22_2316_KST.md`
3. `versions/v0.01/memory/28_PRO_DEEP_RESEARCH_HANDOFF_OPEN_SOURCE_PILOT_2026-08-22_2238_KST.md`
4. migration decisions/checkpoints 18–27 if broader migration context is needed
5. current exact Git state before relying on any stale locator

## 25. Immediate first reply in successor channel

State:

`CURRENT_PERSONA_LOCK = ASA-MI`

Then briefly confirm recovery and begin the next-candidate interview rather than re-summarizing the whole project.

Default next candidate:

`Joplin`, unless Owner names another candidate.

## 26. Compact handoff state

```text
CURRENT_WORK = OPEN_SOURCE_EMPIRICAL_PILOT_CANDIDATE_INTERVIEW
CURRENT_FIRST_RECOMMENDATION = GRIST / WORKING / NOT_SELECTED
STRONGEST_ALTERNATIVE = JOPLIN
IDENTITY_SPECIALIST = TRILIUMNEXT
IMPLEMENTATION = NOT_AUTHORIZED
AAA_MUTATION = FORBIDDEN
ORG_EXECUTION_METHOD = DEFERRED_PENDING_AAA_PLAN
SEPARATE_BYUL_EXECUTION_DEPENDENCIES = REASK_AFTER_COMPLETION
NEXT_ACTION = CANDIDATE_BY_CANDIDATE_OWNER_INTERVIEW
```
