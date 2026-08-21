# Byul

`Byul`은 `AAA-ASA-ME`에서 진행하는 Owner modeling / World Model / formalism prior-art 연구와 실험 구현을 AAA 본체와 분리해 축적하는 저장소입니다.

## CURRENT STATUS LOCATOR

README만 열어도 현재 어디를 읽어야 하는지 알 수 있도록 현황파일을 명시합니다.

- **현재 현황파일:** `versions/v0.01/CURRENT_STATUS.md`
- **상세 진행 로그:** `versions/v0.01/memory/10_ACTIVE_CHANNEL_LOG.md`
- **현재 핵심 원칙:** `versions/v0.01/memory/11_CORE_PRINCIPLES.md`
- **현재 연구 스냅샷 안내:** `versions/v0.01/README.md`
- **현재 실험 구현 현황:** `versions/v0.1/README.md`
- **현재 구현 계약:** `versions/v0.1/MODEL_CONTRACT.md`
- **상세 대화/context 복구본:** `versions/v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

새 채널이나 후계 인스턴스는 우선 `versions/v0.01/CURRENT_STATUS.md`를 읽습니다.

## Current State

- ACTIVE RESEARCH MEMORY: `versions/v0.01/`
- CURRENT STATUS FILE: `versions/v0.01/CURRENT_STATUS.md`
- CURRENT CORE PRINCIPLES: `versions/v0.01/memory/11_CORE_PRINCIPLES.md`
- PREDECESSOR / RECOVERY: `versions/v0.00/`
- ACTIVE EXPERIMENTAL IMPLEMENTATION: `versions/v0.1/`
- 상태: `NON_NORMATIVE / NOT_VALIDATED / PRODUCTION_NOT_AUTHORIZED`

## Version Boundary

- `v0.00`: 최초 분리 연구 스냅샷 + 상세 context recovery backup.
- `v0.01 ~ v0.0x`: 연구·메모·MI 초기화·상황별 모델 라우팅·lifecycle validation·위원회 simulation scenario 설계.
- `v0.1+`: 실제 모델 실구현.

## Core Principles

Byul/AAA-ASA-ME의 현재 상위 원칙은 `versions/v0.01/memory/11_CORE_PRINCIPLES.md`에 관리합니다.

현재 원칙은 다음 방향을 포함하며 개수는 고정하지 않습니다.

- 변화 가능성
- 비고정 실체성
- 합성·발현성
- 조건·관계 의존성

이 원칙들은 특정 formalism을 강제하지 않습니다. Causal Set, Petri Net, Event Structure, LTS, Rewrite 등 구현은 열어두되 모델 선택·변환·복원·mutation이 원칙을 암묵적으로 위반하지 않는지 검토합니다.

Byul/AAA-ASA-ME 세계관 원칙에 대한 `P0/P1` 우선순위 표기는 사용하지 않습니다. AAA 전체 governance의 별도 위험등급 체계는 이 문서의 대상이 아닙니다.

## v0.1 Data Rule

v0.1의 primary DATA는 외부 toy dataset이 아니라 **현재까지 축적된 Byul `v0.01` memory corpus 자체**입니다.

`versions/v0.01/memory/*.md`

v0.1은 이 memory를 raw ground representation으로 읽고 history/current/open/model-family/lifecycle/core-principles 등의 derived view를 만들며 `R(S,M,L)` routing과 mutation/invalidation micro-test를 수행합니다.

## Succession Rule

AAA-ASA-ME 채널 승계 시 최소 순서는 다음과 같습니다.

1. `README.md`
2. `versions/v0.01/CURRENT_STATUS.md`
3. `versions/v0.01/memory/11_CORE_PRINCIPLES.md`
4. `versions/v0.01/README.md`
5. 필요한 `versions/v0.01/memory/00~11` 구조화 메모

긴 대화흐름 또는 context 손실 복구가 필요하면:

`versions/v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

를 추가로 읽습니다.

v0.1 구현을 이어갈 때는:

- `versions/v0.1/README.md`
- `versions/v0.1/MODEL_CONTRACT.md`
- `versions/v0.1/data/SOURCE_MANIFEST.md`

도 함께 읽습니다.

## Governance Note

- 이 저장소는 AAA canonical Requirement / Design / Shared Contract / Validation state를 대체하지 않습니다.
- v0.1의 router/index/view 결과는 source memory보다 높은 authority를 갖지 않습니다.
- Core Principles는 Byul 연구·설계 원칙이며 scientific truth 또는 Independent Validation PASS를 의미하지 않습니다.

## Entry Points

- **Current status:** `versions/v0.01/CURRENT_STATUS.md`
- **Core principles:** `versions/v0.01/memory/11_CORE_PRINCIPLES.md`
- Research state: `versions/v0.01/README.md`
- Experimental implementation: `versions/v0.1/README.md`

작성시각: 2026-08-22 03:08 KST
