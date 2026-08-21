# Byul v0.1 Local Codex Commit / Push Policy

## Status

`EXECUTION_CONTROL / REQUIRED_FOR_LOCAL_CODEX_RUNS`

## Purpose

로컬 Codex 실행이 로컬 파일 생성으로 끝나지 않고, canonical run reservation과 최종 결과를 GitHub `AofSpds/Byul`에 실제 반영하도록 한다.

## Critical Rule

로컬 저장만으로 실행 완료로 취급하지 않는다.

Local Codex run completion requires:

`RESERVE → COMMIT → PUSH RESERVATION → EXECUTE → COMMIT RESULTS → PUSH RESULTS → VERIFY REMOTE`

## 1. Reservation Must Be Remote

RUN_ID 예약은 로컬 `RESERVATION.md` 생성만으로 성립하지 않는다.

예약 확정 조건:

1. `origin/main` 최신 상태를 fetch한다.
2. `versions/v0.1/runs/RUN_NUMBERING.md` 규칙에 따라 다음 후보 RUN_ID를 계산한다.
3. `versions/v0.1/runs/<RUN_ID>/RESERVATION.md`를 생성한다.
4. reservation commit을 만든다.
5. 해당 commit을 GitHub remote에 push한다.
6. remote에서 해당 reservation path가 존재하는 것을 확인한다.

`REMOTE_RESERVATION_CONFIRMED = TRUE`가 되기 전 substantive research를 시작하지 않는다.

## 2. Reservation Collision Handling

동시 실행으로 push가 non-fast-forward 또는 path collision으로 실패하면:

1. `git fetch origin`.
2. 최신 `origin/main`을 기준으로 이미 예약된 RUN_ID를 다시 읽는다.
3. 충돌한 후보 RUN_ID를 포기한다.
4. 다음 free RUN_ID를 새로 계산한다.
5. 새 RUN_ID 경로로 reservation을 다시 생성한다.
6. commit/push를 다시 시도한다.
7. remote 확인 성공까지 반복한다.

이미 remote에 존재하는 RUN_ID를 덮어쓰거나 재사용하지 않는다.

## 3. Result Push

Phase-1 freeze와 Phase-2 완료 후 최소 다음을 자기 run folder에 저장한다.

- `RESERVATION.md`
- `PHASE1_FROZEN.md`
- `RETURN_PACKET.md`
- 필요 시 `notes/`, `artifacts/`

그 다음:

1. 자기 run folder 변경만 stage한다.
2. result commit을 만든다.
3. `git fetch origin` 후 최신 main 변경을 반영한다.
4. disjoint run-folder 변경을 유지한 채 rebase/merge한다.
5. GitHub remote에 push한다.
6. remote `versions/v0.1/runs/<RUN_ID>/RETURN_PACKET.md` 존재를 확인한다.

## 4. Push Retry

최종 push가 다른 run의 동시 push 때문에 거부되면:

`FETCH → REBASE ON LATEST origin/main → PUSH RETRY`

자기 run folder 밖의 shared semantic files를 수정하지 않았다는 전제에서 충돌 없이 재시도하는 것이 기본이다.

실제 content conflict가 발생하면 임의 해결하지 않고 `PUSH_BLOCKED / REVIEW_REQUIRED`로 보고한다.

## 5. Completion States

### COMPLETE

아래가 모두 참일 때만 실행 완료다.

- `REMOTE_RESERVATION_CONFIRMED = TRUE`
- `PHASE1_FROZEN = TRUE`
- `RETURN_PACKET_LOCAL = PRESENT`
- `RESULT_COMMIT_CREATED = TRUE`
- `RESULT_PUSH_SUCCEEDED = TRUE`
- `REMOTE_RETURN_PACKET_CONFIRMED = TRUE`

### INCOMPLETE

로컬 결과는 있으나 remote push/verification이 끝나지 않은 상태.

### PUSH_BLOCKED

권한, 충돌, 인증, network 등으로 remote 반영 실패. 이 경우 로컬 완료를 remote 완료로 가장하지 않는다.

## 6. Never Do

- 로컬 reservation만 만들고 다른 run이 볼 수 있다고 가정
- push 실패를 무시하고 COMPLETE 선언
- 다른 run 폴더 덮어쓰기
- shared baseline/core/research memory를 proposal run에서 수정
- 이미 remote에 예약된 RUN_ID 재사용
- push를 위해 semantic 내용을 임의로 바꾸기

## 7. Return Packet Execution Metadata

RETURN PACKET에는 다음 execution metadata를 추가한다.

- `REMOTE_RESERVATION_CONFIRMED = TRUE/FALSE`
- `RESULT_COMMIT_SHA = <sha or NONE>`
- `RESULT_PUSH_SUCCEEDED = TRUE/FALSE`
- `REMOTE_RETURN_PACKET_CONFIRMED = TRUE/FALSE`
- `PUSH_STATE = COMPLETE/INCOMPLETE/PUSH_BLOCKED`

작성시각: 2026-08-22 04:26 KST
