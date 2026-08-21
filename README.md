# Byul

`Byul`은 `AAA-ASA-ME`에서 진행하는 Owner modeling / World Model / formalism prior-art 연구와 실험 구현을 AAA 본체와 분리해 축적하는 저장소입니다.

## Current State

- ACTIVE RESEARCH MEMORY: `versions/v0.01/`
- PREDECESSOR / RECOVERY: `versions/v0.00/`
- ACTIVE EXPERIMENTAL IMPLEMENTATION: `versions/v0.1/`
- 상태: `NON_NORMATIVE / NOT_VALIDATED / PRODUCTION_NOT_AUTHORIZED`

## Version Boundary

- `v0.00`: 최초 분리 연구 스냅샷 + 상세 context recovery backup.
- `v0.01 ~ v0.0x`: 연구·메모·MI 초기화·상황별 모델 라우팅·lifecycle validation·위원회 simulation scenario 설계.
- `v0.1+`: 실제 모델 실구현.

## v0.1 Data Rule

v0.1의 primary DATA는 외부 toy dataset이 아니라 **현재까지 축적된 Byul `v0.01` memory corpus 자체**다.

`versions/v0.01/memory/*.md`

v0.1은 이 memory를 raw ground representation으로 읽고 history/current/open/model-family/lifecycle 등의 derived view를 만들며 `R(S,M,L)` routing과 mutation/invalidation micro-test를 수행한다.

## Succession Rule

AAA-ASA-ME 채널 승계 시 반드시 `versions/v0.01/README.md`와 `versions/v0.01/memory/00~10`을 읽습니다.

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
- `P-series` exact 원문/번호를 Byul에서 새로 만들거나 재정의하지 않습니다.
- P-series를 보존하는 범위에서 implementation formalism은 열어두는 것이 현재 연구 방향입니다.
- v0.1의 router/index/view 결과는 source memory보다 높은 authority를 갖지 않습니다.

## Entry Points

- Research state: `versions/v0.01/README.md`
- Experimental implementation: `versions/v0.1/README.md`

작성시각: 2026-08-22 02:58 KST
