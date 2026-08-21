# Byul Current Status

## Identity

- PROJECT: `AAA`
- CHANNEL: `AAA-ASA-ME`
- ACTIVE_RESEARCH_VERSION: `v0.01`
- ACTIVE_IMPLEMENTATION_VERSION: `v0.1`
- STATUS: `WORKING / NON_NORMATIVE / NOT_VALIDATED`
- PRODUCTION_AUTHORIZED: `FALSE`

## Current Core Principles

Canonical Byul research locator:

`memory/11_CORE_PRINCIPLES.md`

현재 원칙은 다음 방향을 포함하며 개수는 고정하지 않는다.

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
- Core Principles review requirement; automatic principle PASS 없음

Implementation files:

- `../v0.1/README.md`
- `../v0.1/MODEL_CONTRACT.md`
- `../v0.1/data/SOURCE_MANIFEST.md`
- `../v0.1/src/byul_v01.py`
- `../v0.1/tests/test_byul_v01.py`

Current implementation state:

`IMPLEMENTED / TESTS_AUTHORED / TEST_EXECUTION_NOT_YET_CONFIRMED / NOT_VALIDATED`

## Current Open Work

1. v0.1 실제 test execution 및 첫 결과 수집.
2. Transformation Preservation Matrix 설계.
3. Situation Fingerprint 최소 충분 feature 검증.
4. lifecycle PASS/FAIL acceptance threshold 설계.
5. 위원회 외주용 `Lifecycle + Routing Simulation Challenge Requirements` 정리.
6. MI-1 fresh-instance initial-state reconstruction 시험.
7. 후보 모델 간 forward/reverse conversion cost / semantic loss / invalidation radius 시뮬레이션.

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

작성시각: 2026-08-22 03:08 KST
