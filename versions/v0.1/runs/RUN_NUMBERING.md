# Byul v0.1 Run Numbering Rule

## Status

`EXECUTION_CONVENTION / NON_NORMATIVE`

## Purpose

어떤 실행 인스턴스가 별도 수동 채번 없이 들어와도 현재 등록된 최신 실행번호를 확인하고 다음 번호를 자동으로 예약할 수 있게 한다.

## Model Version vs Run Number

- MODEL_VERSION = `v0.1`
- RUN_NUMBER = 모델 버전과 별개의 실행 식별자
- RUN_ID 형식 = `v0.1.<RUN_NUMBER>`

예:

- `v0.1.01`
- `v0.1.02`
- `v0.1.03`
- ...
- `v0.1.99`
- `v0.1.100`
- `v0.1.101`

`.01`, `.02`는 version successor가 아니라 독립 실행 번호다.

실행번호가 증가해도 자동으로 `v0.2`가 되지 않는다.

`v0.2`는 Owner/연구자가 material model successor로 명시적으로 승격할 때만 생성한다.

## Canonical Run Namespace

각 실행은 다음 위치를 사용한다.

`versions/v0.1/runs/<RUN_ID>/`

예:

`versions/v0.1/runs/v0.1.01/`

## Automatic Allocation Rule

새 실행은 시작 시 다음 순서를 따른다.

1. `versions/v0.1/runs/` 아래 이미 예약된 `v0.1.N` 실행번호를 조회한다.
2. 숫자 suffix의 최댓값을 구한다.
3. 예약된 번호가 하나도 없으면 `01`부터 시작한다.
4. 다음 후보는 `max + 1`이다.
5. 두 자리 구간은 zero-padding을 사용한다: `01`~`99`.
6. 100 이상은 자연수 그대로 사용한다: `100`, `101`, ...
7. 후보 번호의 폴더에 `RESERVATION.md`를 **먼저 생성해 번호를 예약**한다.
8. 이미 같은 예약이 존재하거나 동시 실행 충돌로 예약에 실패하면 최신 상태를 다시 조회하고 다음 번호로 재시도한다.
9. 한번 성공적으로 예약된 RUN_ID는 재사용·재번호화하지 않는다.

## Concurrency Rule

단순히 `최신번호 + 1`을 계산하는 것만으로는 병렬 실행에 안전하지 않다.

따라서 RUN_ID는 **예약 성공으로 확정**된다.

권장 동작:

`READ LATEST → PROPOSE NEXT → CREATE RESERVATION → IF CONFLICT, REFRESH AND RETRY`

공유 GitHub branch/API를 사용하는 경우 `RESERVATION.md`의 create-only 동작을 원자적 예약점으로 사용한다.

로컬 Git/worktree 기반 실행은 push 충돌 또는 동일 path 충돌이 발생하면 fetch/rebase 후 최신 번호를 다시 계산하고 새 번호를 예약한다.

## Reservation File Minimum Fields

각 `RESERVATION.md`에는 최소 다음을 기록한다.

- `RUN_ID`
- `MODEL_VERSION = v0.1`
- `ROUND_ID` 또는 `UNASSIGNED`
- `RUN_ROLE` 또는 `UNASSIGNED`
- `BASELINE_COMMIT`
- `RESERVATION_STATE = RESERVED`

추가 metadata는 허용하지만 기존 RUN_ID 의미를 바꾸면 안 된다.

## Separation from Research Round IDs

Round ID와 Run ID는 별개다.

예:

- `ROUND_ID = BYUL-v0.1-PARALLEL-PROPOSAL-R1`
- `RUN_ID = v0.1.07`

후속 Round에서도 전역 run number를 계속 증가시키는 것을 기본으로 한다.

예:

Round-1 마지막 실행이 `v0.1.10`이면 Round-2 첫 신규 실행은 기본적으로 `v0.1.11`이다.

필요하면 각 run metadata에 별도로 round-local index를 둘 수 있으나 canonical RUN_ID는 전역 증가값을 유지한다.

## Never Do

- 같은 RUN_ID 재사용
- 실패한 run의 번호를 다른 run에 재할당
- 실행번호를 이유로 model version 자동 승격
- run 번호를 성능 순위 또는 세대 순서로 해석
- 결과가 마음에 들지 않는다는 이유로 번호 삭제 후 압축

## Succession Boundary

`v0.1.*` = v0.1 모델/연구 baseline에 속한 실행들.

새 material model successor가 명시적으로 `v0.2`로 결정되면 새 namespace를 시작할 수 있다.

예:

- `v0.2.01`
- `v0.2.02`

이 경우에도 기존 `v0.1.*` 실행 기록은 그대로 보존한다.

작성시각: 2026-08-22 03:42 KST
