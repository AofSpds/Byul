# 09. Version Policy

COPIED_FROM: `versions/v0.00/memory/09_VERSION_POLICY.md`

## Version Meaning

### v0.00
- 최초 분리 연구 스냅샷.
- 현재까지의 AAA-ASA-ME 대화 흐름, Owner worldview, prior-art 학습, 후보모델·라우팅·lifecycle·simulation 아이디어를 복원 가능하게 백업.
- 모델 실구현 없음.

### v0.01 ~ v0.0x
- 연구·메모·초기화·검증설계 successor 단계.
- 후보 formalism 비교, Situation Routing, lifecycle validation, simulation scenario design, MI 초기화 시험, 위원회 외주 요구사항을 정교화.
- 모델 실구현 없음.
- 개념 pseudocode/수학적 예시는 가능하나 reference implementation/model engine/router 구현은 시작하지 않음.

### v0.1+
- 실제 모델 구현 시작점.
- v0.1 exact target은 v0.0x 연구결과와 승인된 구현 scope를 입력으로 새로 정의.
- model representation / router / transformation / simulation harness 등 실제 코드·실행 artifact를 만들 수 있음.
- v0.00/v0.01 연구 메모를 덮어쓰지 않음.

## Mandatory Succession Rule
- v0.00은 복구 기준 predecessor snapshot으로 보존.
- 현재 연구 메모는 v0.01 successor에서 계속 진행.
- 채널 승계 시 반드시 `versions/v0.01/README.md`와 v0.01 structured memory를 읽음.
- context loss가 의심되면 v0.00 detailed context backup과 chronology로 복구.

## Authority Note
Byul 내부 연구 버전 정책이며 AAA canonical release/version authority를 대체하지 않음.

작성시각: 2026-08-22 02:37 KST
