# 29. PRO Deep Research — Single Open-Source Pilot Verdict — 2026-08-22

```text
STATUS = RESEARCH_VERDICT / NON_NORMATIVE / NOT_VALIDATED
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
TASK = SINGLE_OPEN_SOURCE_EMPIRICAL_PILOT_SELECTION
IMPLEMENTATION_AUTHORIZED = FALSE
AAA_MUTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
SELECTION_STATE = WORKING_RECOMMENDATION
FINAL_ROUTE = PROCEED_WITH_MODIFIED_GRIST_PILOT
CONFIDENCE = MODERATE_HIGH / 0.76
```

## 0. Executive verdict

첫 파일럿은 **Grist**를 유지하되, 선행 가설을 크게 수정한다.

Grist를 선택하는 이유는 “native merge가 가장 완성되어 있기 때문”이 아니다. exact source review 결과 Grist proposal patch 경로는 스스로 `Incomplete and naive`라고 명시하며, structural rename을 처리하지 못하고 formula/hidden column을 건너뛰며, 부분 적용 가능성이 있다. 따라서 Grist native apply 결과를 semantic correctness oracle로 사용하면 안 된다.

그럼에도 Grist는 다음을 한 bounded workload 안에서 제공한다.

- real application state: table / row / typed column / formula / reference
- document fork
- common-ancestor/action-history comparison
- trunk/fork divergence
- proposal creation and application
- undo-linked actions
- exact upstream tests and deterministic API fixtures

따라서 Grist는 **정답 구현**이 아니라, BYUL 후보와 simpler control의 merge/refusal/conflict/lineage/reconstruction 능력을 구별할 수 있는 **high-information fixture generator + adversarial calibration surface**로 가장 적합하다.

## 1. 선행 결론에서 수정된 핵심

이전 탐색의 `Grist = 94/100, strongest native merge workload` 평가는 과도했다.

수정된 판단:

```text
GRIST NATIVE FORK / HISTORY / DIFF = STRONG
GRIST NATIVE PATCH / SEMANTIC MERGE = LIMITED / PARTIAL / NOT ORACLE
GRIST AS FIRST PILOT = STILL RECOMMENDED, BUT ONLY AFTER REFRAME
```

Grist는 BYUL이 upstream merge를 복제하는 실험이 되어서는 안 된다. Upstream Grist가 생성한 exact state/action/diff를 candidate-neutral envelope로 공급하고, 각 후보가 독립적으로 다음을 결정해야 한다.

- MERGE
- SAFE_REFUSAL
- CONFLICT
- UNKNOWN
- INVALID / INCOMPLETE

## 2. Exact source pack — First recommendation

### Grist

```text
REPOSITORY = gristlabs/grist-core
LICENSE = Apache-2.0
PINNED_RELEASE = v1.7.17
PINNED_COMMIT = fe672818f879c86d2d145f3f30cb30f106e15f1a
```

Key source locators:

- `test/server/lib/Proposals.ts`
  - local TestServer fixture
  - document creation, fork, proposal, diff, apply
  - trunk table/column rename followed by proposal application
  - formula-derived result and added-row behavior
- `app/common/DocState.ts`
  - action-history comparison
  - common parent
  - `same / left / right / both / unrelated`
  - truncated history may make related documents appear unrelated
- `app/server/lib/Patch.ts`
  - explicitly `Incomplete and naive`
  - table/column structural changes rejected
  - metadata ignored
  - formula and hidden columns skipped
  - row/cell patch application
- `app/server/lib/ActiveDoc.ts`
  - proposal comparison/rebase/application route
- `test/nbrowser/ProposedChangesPage.ts`
  - real UI workflow for work-on-copy, suggest, retract, accept
  - multiple proposals
  - trunk rename after proposal
  - reference/reference-list changes

## 3. Exact source pack — Strongest alternative

### Joplin

```text
REPOSITORY = laurent22/joplin
DEFAULT_LICENSE = AGPL-3.0-or-later, subject to subtree LICENSE files
PINNED_RELEASE = Desktop v3.6.15
PINNED_COMMIT = c61572660382863595c6b51ccf2263e3d2c4bfce
```

Key source locators:

- `packages/lib/services/synchronizer/utils/handleConflictAction.ts`
  - material note conflict creates conflict copy
  - remote state replaces local active state
  - remote deletion can delete local active state
- `packages/lib/services/synchronizer/handleConflictAction.test.ts`
  - verifies conflict duplicate creation and remote-active/local-preserved behavior
- `packages/lib/services/RevisionService.ts`
  - title/body text patches
  - metadata object patches
  - revision-chain reconstruction
  - restore as a new note in `Restored Notes`
- `packages/lib/Synchronizer.ts`
  - offline-first item synchronization

Joplin is the stronger first choice only when the primary question is:

> “Can BYUL preserve conflict, UNKNOWN, and reconstruct history without unsafe merge?”

It is weaker than Grist for a first pilot centered on explicit SPLIT/FORK → DIVERGE → MERGE because Joplin has replication/conflict but no equivalent native branch/proposal merge path.

## 4. Candidate disposition

| Candidate | Disposition | Reason |
|---|---|---|
| Grist | FIRST PILOT / MODIFIED | strongest combined fork/history/schema/data fixture; native merge not oracle |
| Joplin | STRONGEST ALTERNATIVE | conflict preservation and revision reconstruction; weak positive merge surface |
| TriliumNext | SECOND-PHASE IDENTITY STRESS | same note under multiple parents; branch identity unstable; clones do not natively diverge as separate content |
| Dolt | UPPER-BOUND CALIBRATION | mature branch/merge/conflict, but answer leakage: product is explicitly Git-for-data |
| SilverBullet | SIMPLER-CONTROL PRIOR ART | Markdown source of truth + disposable/rebuildable derived index |
| Memos | LOW-COST SANITY CONTROL | bounded CRUD/relation/API; insufficient lifecycle pressure |
| Vikunja | LATER GENERALIZATION | typed task relations, workflow/domain shift, transformation-loss opportunities |
| AppFlowy | ADVERSARIAL CEILING | CRDT stack already solves concurrency; too complex for first pilot |
| Penpot | LATER INHERITANCE/OVERRIDE STRESS | component/instance/override/history but high implementation surface |

## 5. Why Trilium is not first

Trilium exact code provides an unusually strong identity case:

- Branch is parent-note ↔ child-note relationship.
- One note may have multiple parents.
- Branch identity can change on move; noteId is the more stable referent.
- Deleting the last strong branch deletes the note; weak branches do not preserve it.
- `createClone` creates another branch to the same note.

This is excellent for relation-dependent identity and context. However, Trilium cloning is not a native content fork: clones point to the same note. A true `SPLIT → independent MUTATE → MERGE` test would require duplicate-note or synthetic merge semantics. That would increase adapter shadowing and reduce upstream-grounded falsifiability.

## 6. Why Dolt is not first

Dolt covers branch, merge, conflicts, cherry-pick, revert, clone, schema and data. It is a strong calibration reference.

However its product thesis already encodes the version-control solution. A BYUL candidate can appear successful merely by re-expressing Dolt/Git semantics. This is useful as an upper-bound reference but weak as the first falsification workload for a general world model.

## 7. Modified Grist pilot — minimum meaningful slice

### 7.1 Upstream role

```text
GRIST = FIXTURE GENERATOR + NATIVE CALIBRATION
GRIST NATIVE APPLY = NOT SEMANTIC ORACLE
```

### 7.2 Base document

Two related tables:

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

Base state `S0` is frozen by exact state/action hash.

### 7.3 Lifecycle trace

```text
S0
├─ TRUNK A
└─ FORK B

A MUTATE
B MUTATE

A' + B'
↓
COMPARE
↓
MERGE / SAFE_REFUSAL / CONFLICT / UNKNOWN
↓
RECONSTRUCT S0, A', B', RESULT
```

## 8. Required fixture pack

### Positive controls — always-refuse must fail

1. **Disjoint row updates**
   - trunk changes row 1
   - fork changes row 2
   - expected: deterministic merge

2. **Resolvable rename rebase**
   - fork edits a cell under column `A`
   - trunk renames `A → AA`
   - expected: change follows explicit rename lineage and applies to `AA`

### Negative/adversarial controls — always-merge must fail

3. **Same-cell incompatible changes**
   - trunk and fork write different values
   - expected: conflict/refusal unless an explicit policy and scope exists

4. **Delete referenced entity vs create/modify reference**
   - trunk deletes Category row
   - fork adds Item reference to it
   - expected: unsafe/conflict; no dangling silent merge

5. **Formula/input dependency ambiguity**
   - one side mutates formula/input schema
   - other side mutates dependent data
   - expected: explicit unsupported/loss/conflict where semantics cannot be proven

6. **Proposal-side structural mutation**
   - fork renames table/column or changes type
   - expected: explicit unsupported/refusal; no silent skip

7. **Mixed valid + invalid patch**
   - one row update valid, one operation invalid
   - expected: predeclared atomicity; partial success may not masquerade as full apply

8. **Missing/truncated common history**
   - common ancestor cannot be proven
   - expected: UNKNOWN/unrelated; no fabricated lineage

9. **Replay/reconstruction**
   - reconstruct all states from S0 + accepted receipts
   - exact output hashes must match

## 9. Critical upstream risk to test in preflight

The exact Grist patch implementation calculates pre/post cell values but writes post without an obvious precondition check. Structural changes are rejected; formula columns are skipped; `applied` is true if any non-failing change exists.

These imply three hypotheses that MUST be empirically tested before candidate implementation:

```text
H-G1 same-cell divergence may be overwritten rather than surfaced
H-G2 mixed patch may partially apply while reporting applied=true
H-G3 proposal structural/formula semantics may be skipped or rejected
```

These are source-supported risk hypotheses, not yet executed pilot results.

## 10. Candidate competition for the first pilot

Do not run the full original C1/C2/C3 tournament immediately.

First pilot has only two implementation candidates:

### S0 — Simpler control

```text
content-addressed snapshots
+ immutable operation/receipt log
+ explicit preconditions
+ deterministic reducer
+ conflict/unknown state
```

This is intentionally smaller than a full Git system and smaller than a rich ledger.

### B1 — Minimal BYUL candidate

Only currently justified capabilities may be included:

- visible provenance
- explicit loss
- conflict/UNKNOWN preservation
- lifecycle lineage
- semantic admissibility before cost
- deterministic reconstruction

No automatic assumption of:

- fixed 5-plane architecture
- fixed object count
- mandatory ledger
- canonical planner signature
- stable essential identity

The simpler control must be allowed to win.

## 11. Adapter purity

The adapter may only:

- serialize exact Grist state/actions
- map identifiers mechanically
- preserve native fields/bytes
- declare unsupported/unmappable data

The adapter may NOT:

- detect or resolve conflicts
- infer lineage
- choose merge order
- repair references
- calculate semantic admissibility
- synthesize missing history

Any of those behaviors makes the adapter a shadow candidate and invalidates the comparison.

## 12. Observation contract

Every run records:

- exact upstream repository/commit
- exact fixture version/hash
- base/trunk/fork state IDs and hashes
- native action sequence
- candidate version/hash
- decision: MERGE / REFUSE / CONFLICT / UNKNOWN / INVALID
- preserved fields
- disclosed loss
- unresolved conflict
- lineage edges
- output state hash
- replay result
- runtime/cost/operation count
- non-scoreable state: BLOCKED / STOPPED / CONTAMINATED / INCOMPLETE / BUDGET_EXHAUSTED

## 13. Anti-gaming

- resolvable positive controls defeat `ALWAYS_REFUSE`.
- incompatible/unknown controls defeat `ALWAYS_MERGE`.
- candidate-visible stimulus and grader-only oracle are separated.
- candidate IDs are opaque during semantic adjudication.
- candidate output is captured before any interpretation adapter.
- reruns are not silent; every run and failure remains visible.
- cost/build budgets are symmetric and frozen before candidate results.

## 14. Ablation plan

Remove one capability at a time:

1. lineage edges
2. provenance/content hash
3. explicit loss receipt
4. explicit conflict state
5. reconstruction reducer
6. semantic precondition/admissibility check

If removal causes no measurable regression in the frozen fixture set, that capability is not justified by this pilot.

## 15. Preflight gate before full pilot

Before any candidate implementation, run only upstream Grist and add three adversarial tests:

1. same-cell incompatible edit
2. mixed valid/invalid partial patch
3. proposal-side structural/formula mutation

Preflight output:

- deterministic fixture generation confirmed or failed
- exact native behavior captured
- build/test cost measured
- candidate-neutral envelope feasibility assessed

### Preflight stop conditions

STOP / REFRAME if:

- pinned upstream cannot be run deterministically;
- action/state extraction requires semantic logic in adapter;
- fewer than three cases discriminate meaningful candidate behavior;
- harness implementation is larger than both candidate implementations combined;
- the simpler control cannot be specified without importing BYUL assumptions.

## 16. Resource estimate — planning estimate, not measured fact

### Preflight only

- source/build verification: 0.5–1.0 day
- three adversarial upstream tests: 0.5 day
- fixture/envelope feasibility note: 0.25–0.5 day

Total: **0.5–1.5 engineer-days**.

### Full first pilot after GO

- upstream fixture generator: 1–2 days
- neutral harness/envelope/replay: 2–4 days
- simpler control: 1–2 days
- minimal BYUL candidate: 3–6 days
- adversarial fixture/test completion: 2–4 days
- evaluation/report: 1–2 days

Total: **8–15 engineer-days**, likely **5–9 wall-clock days** with safe parallelization, excluding independent validation and excluding the deferred organization/execution-topology work.

## 17. Stop / go after pilot

### STOP BYUL expansion

- simpler control matches/exceeds B1 on all material fixtures;
- B1 adds complexity without measurable failure reduction;
- adapter/harness dominates semantics;
- results remain non-discriminating.

### ITERATE GRIST

- pilot exposes at least one repeatable, BYUL-relevant distinction;
- harness remains candidate-neutral;
- uncertainty is caused by insufficient Grist cases rather than domain mismatch.

### ADD JOPLIN

- unresolved question is conflict preservation, offline divergence, or revision reconstruction.

### ADD TRILIUM

- unresolved question is entity/context identity, clone/branch lineage, or deletion under multiple parents.

### ADD VIKUNJA

- BYUL survives data/note-domain pilots and cross-domain generalization becomes the next question.

## 18. Claims allowed and forbidden

### Allowed

- the pilot method is or is not feasible;
- specific candidate behavior on frozen cases;
- comparative implementation/cost evidence;
- a failure atlas;
- justified successor questions.

### Forbidden

- BYUL is a validated universal World Model;
- a fixed architecture is canonical;
- a ledger/planner/object set is proven necessary;
- production readiness;
- AAA adoption;
- scientific proof from one application pilot.

## 19. Deferred boundaries

This research does not decide:

- Persona ↔ Channel binding
- Work Ultra / Agent Thread topology
- validator execution surface
- independent auditor execution mechanism
- current separate BYUL process branch/baseline/merge/successor treatment

Those remain deferred to the Owner-directed AAA organization/execution plan and completion of the separately running BYUL process.

## 20. Final route

```text
FIRST PILOT = GRIST v1.7.17 @ fe672818f879c86d2d145f3f30cb30f106e15f1a
ROUTE = PROCEED / MODIFY
PRECONDITION = UPSTREAM-ONLY ADVERSARIAL PREFLIGHT
NATIVE GRIST APPLY = CALIBRATION, NOT ORACLE
STRONGEST ALTERNATIVE = JOPLIN v3.6.15
NEXT SPECIALIST = TRILIUMNEXT v0.104.1
IMPLEMENTATION_AUTHORIZED = FALSE
```

The recommendation may be superseded by the preflight result. A failed preflight is a successful research outcome if it prevents a contaminated or non-discriminating full implementation.
