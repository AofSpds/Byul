# Byul Current Status

## Identity

- PROJECT: `AAA`
- CHANNEL: `AAA-ASA-ME`
- ACTIVE_RESEARCH_VERSION: `v0.01`
- ACTIVE_IMPLEMENTATION_VERSION: `v0.1`
- STATUS: `WORKING / NON_NORMATIVE / NOT_VALIDATED`
- PRODUCTION_AUTHORIZED: `FALSE`

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
- 현재 routing 후보: `R(S,M,L)` = Situation / Current Model State / Lifecycle Context.
- Situation Fingerprint에서는 특히 `Preservation Demand`가 핵심 축일 가능성을 검토 중.

## Current Implementation — v0.1

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

`IMPLEMENTED / TESTS_AUTHORED / TEST_EXECUTION_NOT_YET_CONFIRMED / NOT_VALIDATED`

## Automatic Run Numbering

Canonical numbering rule:

`../v0.1/runs/RUN_NUMBERING.md`

Execution numbering is global within the current model version.

Examples:

- `v0.1.01`
- `v0.1.02`
- `v0.1.03`
- ...
- `v0.1.100`

Rules:

- a new execution reads the latest reserved `v0.1.*` number and proposes the next integer;
- it first reserves that number; if another parallel execution already took it, refresh and retry with the next available number;
- reserved numbers are never reused or compressed;
- run numbers are not ranks, generations, or successor versions;
- increasing run numbers never automatically promotes the model to `v0.2`;
- `v0.2` is created only by an explicit material successor decision;
- Round-local slot IDs such as `R01` and canonical run IDs such as `v0.1.17` are separate identifiers.

Canonical run namespace:

`versions/v0.1/runs/<RUN_ID>/`

## Parallel Proposal & Evaluation Direction

Research design:

`memory/12_PARALLEL_PROPOSAL_ROUND1.md`

Execution packet:

`experiments/round1/ROUND1_LAUNCH_PACKET.md`

Owner + ASA evaluation packet:

`experiments/round1/ROUND1_EVALUATION_PACKET.md`

Round-1 exact proposal baseline:

`891e4bd4b999eacc99431ed0db05062901a68dd9`

Recommended allocation:

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

All runs are independent and do not see other run outputs before submission.

Evaluation uses fail/review gates + blind qualitative pairwise comparison before any aggregate numeric score. Consensus is not sufficient for selection; useful minority proposals are preserved.

## Current Open Work — Byul

1. Launch Round-1 parallel proposal cohort using automatic canonical run numbering.
2. Collect exact `[RETURN PACKET]` outputs from assigned Round slots.
3. Blind-normalize returns and run Owner + ASA comparative evaluation.
4. Preserve finalists 3–4 plus justified minority alternatives.
5. Design Round-2 pressure tests from observed convergence/divergence.
6. Run v0.1 executable micro-tests separately.
7. Derive Transformation Preservation Matrix from proposal/simulation evidence.
8. Revisit Situation Fingerprint and `R(S,M,L)` from observed routing evidence.

## Immediate Next Step

Execute `experiments/round1/ROUND1_LAUNCH_PACKET.md` across independent runs.

Each execution automatically reserves the next canonical `v0.1.*` RUN_ID before substantive work. Round slots only assign cohort/profile behavior.

The first Round is not a vote for the current design. It is a structured search for:

- independent convergence;
- meaningful divergence;
- stronger prior art;
- valid replacement/reframe proposals;
- evidence for or against multi-model routing;
- lifecycle and semantic-preservation failure modes.

## Detailed History / Recovery

- 상세 진행 로그: `memory/10_ACTIVE_CHANNEL_LOG.md`
- 핵심 원칙: `memory/11_CORE_PRINCIPLES.md`
- Round-1 설계: `memory/12_PARALLEL_PROPOSAL_ROUND1.md`
- Round-1 실행: `experiments/round1/ROUND1_LAUNCH_PACKET.md`
- Round-1 평가: `experiments/round1/ROUND1_EVALUATION_PACKET.md`
- 실행 채번 규칙: `../v0.1/runs/RUN_NUMBERING.md`
- 구조화 메모: `memory/00~12`
- 긴 context 복구본: `../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Read Order for Successor

1. `CURRENT_STATUS.md`
2. `memory/11_CORE_PRINCIPLES.md`
3. `memory/12_PARALLEL_PROPOSAL_ROUND1.md`
4. `experiments/round1/ROUND1_LAUNCH_PACKET.md`
5. `../v0.1/runs/RUN_NUMBERING.md`
6. `README.md`
7. 필요한 구조화 메모
8. 필요 시 `memory/10_ACTIVE_CHANNEL_LOG.md`
9. context 손실 시 v0.00 recovery backup

작성시각: 2026-08-22 03:42 KST
