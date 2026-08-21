# Byul Current Status

## Identity

- PROJECT: `AAA`
- CHANNEL: `AAA-ASA-ME`
- ACTIVE_RESEARCH_VERSION: `v0.01`
- ACTIVE_IMPLEMENTATION_VERSION: `v0.1`
- STATUS: `WORKING / NON_NORMATIVE / NOT_VALIDATED`
- PRODUCTION_AUTHORIZED: `FALSE`
- RESEARCH_STATE_MAP: `../../BYUL_RESEARCH_STATE.yaml`
- LATEST_CHECKPOINT: `memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`
- CHECKPOINT_COMMIT: `8133e3d79c88b582bea6b8a45bc8a1970b261734`
- ACTIVE_EXPERIMENT: `SEMANTIC_SURFACE_V0 / FEATURE_BRANCH_TRIAL`
- TRIAL_AUTHORIZATION: `experiments/semantic_surface_v0/OWNER_TRIAL_AUTHORIZATION.md`
- MAIN_MERGE_AUTHORIZED: `FALSE`

## Operating Split

### AAA Mainline

AAA 본선의 기본구조 작업은 완료된 것으로 보고, 별도 신규 설계 과제로 계속 확장하지 않는다.

현재 기본 루프:

`MODEL RUN → EVALUATION → FAILURE ANALYSIS → SUCCESSOR IF NEEDED`

즉 본선은 필요한 모델을 실행하고 평가하며, 결과가 successor를 요구할 때만 다시 설계 작업을 연다.

### Byul / AAA-ASA-ME

이 채널의 능동 연구 트랙이다.

- 세계관/모델링 원칙
- memory/state reconstruction
- 상황별 representation routing
- model lifecycle / mutation / reconstruction
- 상호보완 formalism family
- simulation / committee stress scenarios

AAA 본선 실행을 막지 않는 독립 연구선으로 운영한다.

## Current Core

Canonical Byul research locator:

`memory/11_CORE_PRINCIPLES.md`

현재 상위 원칙군은 `BYUL CORE-A`로 지칭하며, 원칙 개수는 고정하지 않는다.

`BYUL CORE-A`는 Owner가 채택한 현재 연구·설계 지침이다. scientific truth, validated invariant 또는 특정 formalism의 선택 authority가 아니다.

현재 포함 방향:

- 변화 가능성
- 비고정 실체성
- 합성·발현성
- 조건·관계 의존성

Byul/AAA-ASA-ME 세계관 원칙에 대한 `P0/P1` 우선순위 표기는 폐지한다. AAA 전체 governance의 위험등급 P0/P1은 별도 체계다.

## Current Worldview / Research Direction

- 고해상도 세계관 가설: `무수한 국소 사상들의 합성망`.
- high-resolution worldview와 implementation abstraction을 분리.
- 하나의 universal model을 고정하지 않고 상호보완 formalism family를 탐구.
- Behaviour/Rule 후보: Petri / Open Petri / Reconfigurable Petri.
- Occurrence/Concurrency 후보: Occurrence Net / Event Structure.
- Purpose-specific view 후보: Causal-order / LTS-Reachability.
- 현재 routing 연구 shorthand: `R(S,M,L)` = Situation / Current Model State / Lifecycle Context. canonical planner signature로 선택되지 않았다.
- Situation Fingerprint에서는 특히 `Preservation Demand`가 핵심 축일 가능성을 검토 중.
- 하나의 universal/canonical World Model은 선택되지 않았다.

## Current Implementation — v0.1 C0 Baseline

Classification:

`C0_EXPERIMENTAL_BASELINE / NOT_BYUL_DEFINITION / NOT_SELECTED / NOT_VALIDATED`

Primary DATA:

`versions/v0.01/memory/*.md`

Implemented experimental slice:

- raw memo ingestion + provenance
- history/current/open/model-family/lifecycle/core-principles views
- `R(S,M,L)` route plan
- UNKNOWN → REVIEW_REQUIRED
- exact metric request → external metric source requirement
- virtual mutation / digest change / invalidation radius
- snapshot content round-trip check
- BYUL CORE-A review requirement; automatic principle PASS 없음

Implementation files:

- `../v0.1/README.md`
- `../v0.1/MODEL_CONTRACT.md`
- `../v0.1/data/SOURCE_MANIFEST.md`
- `../v0.1/src/byul_v01.py`
- `../v0.1/tests/test_byul_v01.py`

Current implementation state:

`IMPLEMENTED_SCAFFOLD / TESTS_AUTHORED / NOT_VALIDATED / NOT_SELECTED`

Known material limitations:

- filesystem source reading rather than enforced Git-object pinning;
- normalized text comparison rather than byte-exact round-trip;
- heuristic marker/tag extraction;
- static routing in which the declared current model state does not yet determine the route;
- lifecycle vocabulary without substantive state-transition semantics;
- hard-coded invalidation dependencies.

Test execution or pass evidence is scaffold evidence only. It is not semantic-preservation proof, model validation, Owner Acceptance or production authorization.

## Run Numbering / Parallel Reservation

Canonical numbering rule:

`../v0.1/runs/RUN_NUMBERING.md`

Execution numbering is global within the current model version. The original serial numbering locator remains preserved, but `memory/14_ROUND1_RERUN_SAFETY_CORRECTION.md` governs clean parallel work where shared mutable reservation is unsafe.

Examples:

- `v0.1.01`
- `v0.1.02`
- `v0.1.03`
- ...
- `v0.1.100`

Rules:

- a serial execution may read the latest reserved `v0.1.*` number and propose the next integer;
- parallel workers must not coordinate through one shared mutable file or worktree;
- clean parallel reservation must be remotely collision-safe, or canonical IDs must be assigned later by a collector;
- reserved numbers are never reused or compressed;
- run numbers are not ranks, generations, or successor versions;
- increasing run numbers never automatically promotes the model to `v0.2`;
- `v0.2` is created only by an explicit material successor decision;
- Round-local slot IDs such as `R01` and canonical run IDs such as `v0.1.17` are separate identifiers.

Canonical run namespace:

`versions/v0.1/runs/<RUN_ID>/`

## Parallel Proposal & Evaluation State

Research design:

`memory/12_PARALLEL_PROPOSAL_ROUND1.md`

Execution packet:

`experiments/round1/ROUND1_LAUNCH_PACKET.md`

Owner + ASA evaluation packet:

`experiments/round1/ROUND1_EVALUATION_PACKET.md`

Round-1 exact proposal baseline:

`891e4bd4b999eacc99431ed0db05062901a68dd9`

Executed clean-rerun allocation:

- `R01–R06`: Neutral Blind — same exact prompt, no solution pressure.
- `R07`: outside-current-family prior-art search.
- `R08`: adversarial reframe / falsification.
- `R09`: minimal-information / minimal-representation search.
- `R10`: lifecycle / composition / reversibility pressure.

Important anti-anchoring design:

1. Phase 1 reads the v0.01 research state but **does not read the existing v0.1 implementation**.
2. Each run freezes an independent proposal as `PHASE1_FROZEN`.
3. Only then does Phase 2 inspect current v0.1 and choose KEEP / MODIFY / REPLACE / HYBRID / REFRAME / INSUFFICIENT_EVIDENCE.
4. Phase-1 proposal may not be rewritten after v0.1 exposure; deltas are recorded separately.

The clean-rerun controller required independent isolated branches/worktrees and no cross-run output exposure before submission.

Evaluation uses fail/review gates + blind qualitative pairwise comparison before any aggregate numeric score. Consensus is not sufficient for selection; useful minority proposals are preserved.

Latest persisted research evidence:

- `memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`
- `memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`

Current Round-1 state:

- R01–R06 and R08–R10 have remotely persisted proposal artifacts according to checkpoint evidence.
- R07 has a remotely frozen Phase-1 proposal; its EOL/hash-gate defect was corrected by using canonical committed Git-blob bytes. Exact branch evidence must be checked before claiming final Phase-2 completion.
- strong same-lineage convergence was observed around exact/content-addressed evidence, scoped authority, rebuildable views, visible preservation/loss, lifecycle lineage and preservation-before-cost;
- this convergence is correlated design evidence, not independent expert replication, final architecture selection or validation;
- hardened Git + Markdown/control-manifest remains the required simpler counter-hypothesis.
- no proposal recommendation authorizes implementation.

## Current Open Work — Byul

1. Keep the current exact Git checkpoint as the pre-change cold-read baseline.
2. Expose surviving-constraint candidate / hypothesis / competitive candidate / OPEN / NON_CLAIM distinctions through the non-normative `../../BYUL_RESEARCH_STATE.yaml` locator.
3. Pre-register candidate-neutral conformance scenarios, positive/negative controls and hidden holdouts from actual Byul incidents.
4. Define a common observation envelope without forcing every candidate into one internal API or ontology.
5. Compare C0 current v0.1, C1 hardened Git+Markdown/control-manifest and C2 minimal content-addressed ledger under the same evidence and complexity gates.
6. Permit C3 richer ledger machinery only if pre-declared evidence shows C2 insufficient.
7. Revisit `R(S,M,L)`, preservation representations, planner surfaces and identity policy from observed evidence; do not promote them by terminology or consensus.
8. Preserve UNKNOWN / OPEN / NON_CONCLUSION when evidence does not support selection.

## Immediate Next Step

Do not relaunch the already executed clean Round-1 as if it were pending.

The immediate research transition is:

`FROZEN COLD-READ BASELINE → NON-NORMATIVE RESEARCH-STATE SURFACE → PRE-REGISTERED SCENARIOS/CONTROLS → BLIND C0/C1/C2 COMPETITION`

The Owner has explicitly authorized the isolated S0–S9 research and implementation trial recorded in `experiments/semantic_surface_v0/OWNER_TRIAL_AUTHORIZATION.md`. This authorization is limited to the feature-branch experiment and draft review surface. It does not authorize a `main` merge, production use, model selection, validation claim or Owner Acceptance.

## Detailed History / Recovery

- 상세 진행 로그: `memory/10_ACTIVE_CHANNEL_LOG.md`
- 핵심 원칙: `memory/11_CORE_PRINCIPLES.md`
- Round-1 설계: `memory/12_PARALLEL_PROPOSAL_ROUND1.md`
- accidental implementation incident: `memory/13_ROUND1_ACCIDENTAL_IMPLEMENTATION_INCIDENT.md`
- clean-rerun safety correction: `memory/14_ROUND1_RERUN_SAFETY_CORRECTION.md`
- canonical Git-blob hash correction: `memory/15_ROUND1_CLEAN_RERUN_EOL_HASH_GATE_CORRECTION.md`
- clean-rerun convergence checkpoint: `memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`
- latest succession checkpoint: `memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`
- machine-readable research state: `../../BYUL_RESEARCH_STATE.yaml`
- Round-1 실행: `experiments/round1/ROUND1_LAUNCH_PACKET.md`
- Round-1 평가: `experiments/round1/ROUND1_EVALUATION_PACKET.md`
- 실행 채번 규칙: `../v0.1/runs/RUN_NUMBERING.md`
- 구조화 메모: `memory/00~12`
- 긴 context 복구본: `../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Read Order for Successor

1. `../../README.md`
2. `../../BYUL_RESEARCH_STATE.yaml`
3. `CURRENT_STATUS.md`
4. `memory/11_CORE_PRINCIPLES.md`
5. `memory/12_PARALLEL_PROPOSAL_ROUND1.md`
6. `memory/13_ROUND1_ACCIDENTAL_IMPLEMENTATION_INCIDENT.md`
7. `memory/14_ROUND1_RERUN_SAFETY_CORRECTION.md`
8. `memory/15_ROUND1_CLEAN_RERUN_EOL_HASH_GATE_CORRECTION.md`
9. `memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`
10. `memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`
11. `../v0.1/README.md`
12. `../v0.1/MODEL_CONTRACT.md`
13. `../v0.1/data/SOURCE_MANIFEST.md`
14. 필요 시 이전 구조화 메모, `memory/10_ACTIVE_CHANNEL_LOG.md` 및 v0.00 recovery backup

작성시각: 2026-08-22 07:34 KST
