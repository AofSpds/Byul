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

Exact source baseline commit:

`2a4529b69bc237125a1f012835d7a9b78ce3fec9`

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

## Parallel Proposal & Evaluation Direction

v0.1의 다음 실험은 하나의 정답을 강제하지 않는다.

동일한 exact baseline / DATA / BYUL CORE-A / 연구 목표를 여러 독립 인스턴스에 주고, 각 인스턴스는 다음 중 어느 것이든 제안할 수 있다.

- 현재 v0.1 구조를 유지하고 개선
- 일부 표현/라우팅/수명주기 구조를 교체
- 현재 후보 formalism family 밖의 prior-art 제안
- 복수 formalism 조합 또는 다른 representation strategy 제안
- 현재 문제정의 자체에 대한 반론 및 대체 formulation 제안
- 충분한 근거가 없으면 UNKNOWN / REVIEW_REQUIRED 유지

핵심 조건:

- 서로의 결과를 보기 전 독립적으로 작업.
- 현재 Petri/Event/Causal/LTS 후보를 정답처럼 전제하지 않음.
- PRIOR-ART-FIRST를 유지하되 실제 gap이 있으면 확장안을 제시할 수 있음.
- run ID는 version이 아니라 독립 실행 식별자: `v0.1-R01`, `v0.1-R02`, ...
- 공통 결과 schema로 반환해 Owner + ASA가 비교·평가.
- 평가자는 결과 작성과 분리하여, 어떤 run도 자기 결과에 PASS를 부여하지 않음.

권장 2단 구조:

1. `Neutral Blind Cohort`: 동일한 중립 prompt로 여러 독립 제안 생성. 자연스러운 분산/수렴을 관찰.
2. `Alternative Search Cohort`: 현재 구조 밖의 prior-art, 최소표현, lifecycle, composition, adversarial failure 등 서로 다른 탐색각을 부여해 coverage를 확대.

평가 관점 후보:

- memory/state reconstruction fidelity
- fact/hypothesis/unknown/non-conclusion preservation
- BYUL CORE-A alignment/conflict
- representation/model choice quality
- semantic loss / invented semantics
- routing rationale
- lifecycle robustness
- explanatory coherence
- novelty without unsupported commitment
- implementation/testability
- migration/reversibility cost

## Current Open Work — Byul

1. v0.1 병렬 proposal cohort 설계 및 실행.
2. v0.1 실제 test execution 및 첫 결과 수집.
3. 병렬 결과를 Owner + ASA가 비교평가하고 finalist/alternative family를 정리.
4. Transformation Preservation Matrix 설계.
5. Situation Fingerprint 최소 충분 feature 검증.
6. lifecycle PASS/FAIL acceptance threshold 설계.
7. 위원회 외주용 `Lifecycle + Routing Simulation Challenge Requirements` 정리.
8. MI-1 fresh-instance initial-state reconstruction 시험.
9. 후보 모델 간 forward/reverse conversion cost / semantic loss / invalidation radius 시뮬레이션.

## Immediate Next Step

`Byul v0.1 Parallel Proposal Round-1`을 설계한다.

첫 Round는 단순히 현재 구현을 재실행하는 것이 아니라, 동일한 메모 DATA와 BYUL CORE-A를 이해한 독립 인스턴스들이 현재 구조를 평가하고 필요하면 더 좋은 모델/표현/라우팅/수명주기 대안을 제안하도록 한다.

Owner + ASA는 결과를 받은 뒤:

- 현행 구조 보존 후보
- 강한 대안 후보
- 상호보완 가능한 후보
- 탈락/반례 후보
- 추가 검증이 필요한 미결 후보

로 분류하고 다음 simulation 대상을 선택한다.

## Detailed History / Recovery

- 상세 진행 로그: `memory/10_ACTIVE_CHANNEL_LOG.md`
- 구조화 메모: `memory/00~11`
- 긴 context 복구본: `../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Read Order for Successor

1. `CURRENT_STATUS.md`
2. `memory/11_CORE_PRINCIPLES.md`
3. `README.md`
4. 필요한 구조화 메모
5. 필요 시 `memory/10_ACTIVE_CHANNEL_LOG.md`
6. context 손실 시 v0.00 recovery backup

작성시각: 2026-08-22 03:31 KST
