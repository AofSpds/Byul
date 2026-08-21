# Byul Research Snapshot v0.01

## Identity

- PROJECT: `AAA`
- PRODUCT: `ASSET AGENT ASA`
- CHANNEL: `AAA-ASA-ME`
- PARENT_PERSONA: `AAA-ASA`
- VERSION: `v0.01`
- PREDECESSOR: `versions/v0.00/`
- STATUS: `ACTIVE_WORKING_RESEARCH_SNAPSHOT / NON_NORMATIVE / NOT_VALIDATED`
- IMPLEMENTATION_STATE: `NOT_STARTED`

## Version Role

`v0.01`은 `v0.00`의 연구상태를 승계한 active successor다.

- `v0.00`: 최초 분리 snapshot + 상세 context recovery backup. 보존.
- `v0.01`: 이후 Owner dialogue / prior-art / routing / lifecycle / simulation / MI initialization 메모를 계속 갱신하는 현재 작업본.
- `v0.1+`: 실제 모델 구현 시작. v0.01에서는 모델 실구현 금지.

## Mandatory Succession Rule

AAA-ASA-ME 채널을 승계할 때는 반드시 이 버전을 기준으로 복원한다.

최소 read order:

1. `README.md`
2. `memory/00_CHANNEL_AND_METHOD.md`
3. `memory/01_OWNER_WORLDVIEW_CURRENT.md`
4. `memory/02_CAUSAL_SET_LEARNING.md`
5. `memory/03_MODEL_FAMILY_AND_COMPLEMENTARITY.md`
6. `memory/04_ROUTING_AND_LIFECYCLE.md`
7. `memory/06_MI1_INITIALIZATION_TARGET.md`
8. `memory/07_OPEN_QUESTIONS_AND_NEXT_JOBS.md`
9. `memory/10_ACTIVE_CHANNEL_LOG.md`

맥락 손실·충돌이 의심되면 predecessor의 상세 백업도 읽는다:

`../v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

## Current Strongest Direction

- 고해상도 Owner worldview: `무수한 국소 사상들의 합성망`.
- high-resolution worldview와 implementation abstraction을 분리.
- P-series를 보존하는 범위에서 implementation은 열어둠.
- 후보 formalism은 하나의 승자보다 호환성·보완성이 높은 family로 연구.
- `R(S,M,L)` = Situation / Current Model State / Lifecycle Context 기반 model routing 후보.
- model lifecycle simulation과 committee-generated stress scenario 확보 필요.
- MI-1에서 fresh-instance memory reconstruction 시험 가치 높음.

## No Implementation Before v0.1

`v0.01~v0.0x`에서는 다음만 수행한다.

- requirements-like research questions
- prior-art comparison
- situation routing criteria
- lifecycle validation design
- benchmark/scenario design
- MI initialization test design
- committee challenge requirements

실제 model/router/transformation engine/reference implementation 코드는 `v0.1+` exact implementation target에서 시작한다.

작성시각: 2026-08-22 02:37 KST
