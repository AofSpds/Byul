# Byul Research Snapshot v0.01

## Identity

- PROJECT: `AAA`
- PRODUCT: `ASSET AGENT ASA`
- CHANNEL: `AAA-ASA-ME`
- PARENT_PERSONA: `AAA-ASA`
- VERSION: `v0.01`
- PREDECESSOR: `versions/v0.00/`
- STATUS: `ACTIVE_WORKING_RESEARCH_SNAPSHOT / NON_NORMATIVE / NOT_VALIDATED`
- IMPLEMENTATION_STATE: `v0.1 EXPERIMENTAL IMPLEMENTATION ACTIVE`

## Current Status File

현재 현황을 가장 먼저 확인할 파일:

`CURRENT_STATUS.md`

보조 locator:

- Core Principles: `memory/11_CORE_PRINCIPLES.md`
- Detailed active log: `memory/10_ACTIVE_CHANNEL_LOG.md`
- Implementation: `../v0.1/README.md`
- Recovery backup: `../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Version Role

`v0.01`은 `v0.00`의 연구상태를 승계한 active research successor다.

- `v0.00`: 최초 분리 snapshot + 상세 context recovery backup. 보존.
- `v0.01`: Owner dialogue / prior-art / routing / lifecycle / simulation / MI initialization 메모와 현황을 관리.
- `v0.1+`: 실제 모델 구현.

## Mandatory Succession Rule

AAA-ASA-ME 채널을 승계할 때는 반드시 이 버전을 기준으로 복원한다.

최소 read order:

1. `CURRENT_STATUS.md`
2. `memory/11_CORE_PRINCIPLES.md`
3. `README.md`
4. `memory/00_CHANNEL_AND_METHOD.md`
5. `memory/01_OWNER_WORLDVIEW_CURRENT.md`
6. `memory/02_CAUSAL_SET_LEARNING.md`
7. `memory/03_MODEL_FAMILY_AND_COMPLEMENTARITY.md`
8. `memory/04_ROUTING_AND_LIFECYCLE.md`
9. `memory/06_MI1_INITIALIZATION_TARGET.md`
10. `memory/07_OPEN_QUESTIONS_AND_NEXT_JOBS.md`
11. 필요 시 `memory/10_ACTIVE_CHANNEL_LOG.md`

맥락 손실·충돌이 의심되면 predecessor의 상세 백업도 읽는다:

`../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Current Strongest Direction

- 고해상도 Owner worldview: `무수한 국소 사상들의 합성망`.
- high-resolution worldview와 implementation abstraction을 분리.
- Byul Core Principles: 변화 가능성, 비고정 실체성, 합성·발현성, 조건·관계 의존성을 현재 원칙으로 채택하며 원칙 개수는 고정하지 않음.
- 위 원칙을 해치지 않는 범위에서 implementation formalism은 열어둠.
- 후보 formalism은 하나의 승자보다 호환성·보완성이 높은 family로 연구.
- `R(S,M,L)` = Situation / Current Model State / Lifecycle Context 기반 model routing 후보.
- model lifecycle simulation과 committee-generated stress scenario 확보 필요.
- MI-1에서 fresh-instance memory reconstruction 시험 가치 높음.

## Research / Implementation Boundary

`v0.01`은 연구·메모·현황 관리용이고, 실제 executable model은 `../v0.1/`에서 관리한다.

작성시각: 2026-08-22 03:08 KST
