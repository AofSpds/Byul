# v0.01 Context Inheritance

## Strategy

`v0.01`은 `v0.00`의 active successor다. 대용량 상세 context backup을 여러 버전에 중복 복제해 서로 다른 사본이 drift하는 위험을 피하기 위해 **copy-on-write inheritance**를 사용한다.

## Immutable Recovery Source

Exact predecessor detailed context:

`versions/v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`

이 파일은 v0.00의 복구 기준본으로 유지한다.

## v0.01 Independent Copy

v0.01은 다음 structured memory를 독립 파일로 보유한다.

- `memory/00_CHANNEL_AND_METHOD.md`
- `memory/01_OWNER_WORLDVIEW_CURRENT.md`
- `memory/02_CAUSAL_SET_LEARNING.md`
- `memory/03_MODEL_FAMILY_AND_COMPLEMENTARITY.md`
- `memory/04_ROUTING_AND_LIFECYCLE.md`
- `memory/05_SIMULATION_AND_COMMITTEE.md`
- `memory/06_MI1_INITIALIZATION_TARGET.md`
- `memory/07_OPEN_QUESTIONS_AND_NEXT_JOBS.md`
- `memory/08_CHANNEL_CHRONOLOGY.md`
- `memory/09_VERSION_POLICY.md`
- `memory/10_ACTIVE_CHANNEL_LOG.md`

즉 v0.01의 일상 복원은 자체 structured memory로 가능하며, 더 긴 대화 흐름이나 누락 의심이 있을 때만 v0.00 detailed context backup으로 내려간다.

## Succession Requirement

새 AAA-ASA-ME instance는:

1. v0.01 README + memory 00~10을 먼저 읽는다.
2. context mismatch / missing detail / chronology uncertainty가 있으면 v0.00 detailed backup을 읽는다.
3. 새로 생긴 내용은 v0.01 active log에 기록하고 필요한 structured memory에 승격한다.
4. 승계 전에 반드시 active log를 최신화한다.

## Implementation Boundary

v0.01에서는 research/memory/validation design만 진행한다. 실제 model implementation은 v0.1부터 시작한다.

작성시각: 2026-08-22 02:37 KST
