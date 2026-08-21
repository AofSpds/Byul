# 02. Causal Set Learning

## Current Position

Causal Set Theory(인과집합이론)는 현재 가장 흥미로운 prior-art 중 하나지만 final architecture가 아니다. 현재 매력은 세계관의 정답이라기보다 `Event + Causal Order`만 보존하고 좌표·공간·global NOW를 primitive에서 제거한 뒤 고수준 구조를 복원하는 강한 추상화 사례라는 점이다.

## Core Concepts

### Partial Order
`C=(Events,≺)`. `a≺b`는 a가 b의 causal past에 있음을 뜻한다. 어떤 두 사건은 어느 쪽도 앞서지 않을 수 있으며 이는 `비교할 필요 없음`이 아니라 **인과적으로 비교 불가능**함이다.

### Link
`a≺b`인데 중간 `z`가 없으면 Link(직접 인과 연결). Link는 transformation semantics를 저장하지 않는다. Owner의 `최소 국소 사상`과 닮았지만 동일하지 않다.

### Chain
모든 원소가 causal order로 비교 가능한 사건 집합. longest chain은 proper-time-like quantity와 연결된다. chain length 자체는 seconds가 아니다.

### Antichain
서로 causal order로 비교 불가능한 사건 집합. exact simultaneity나 absolute NOW를 뜻하지 않는다. 직관적으로 공간 단면 후보로 볼 수 있으나 동일시 금지.

### Causal Interval / Causal Diamond
`Interval(p,q)={x|p≺x≺q}`. causal set 자체는 diamond geometry를 저장하지 않고 p 이후/q 이전 사건 집합만 보존한다. 연속 시공간에 매립했을 때 causal diamond로 렌더링된다.

## No Absolute NOW

현재 강한 이해:

- 유일한 전역 NOW를 primitive로 두지 않는다.
- 인과적으로 비교 불가능한 두 사건에 절대적 선후를 강제로 주지 않는다.
- causal order와 proper-time-like relation까지 임의적이라는 뜻은 아니다.

## Reconstruction Idea

강한 표어:

- `Order` → causal/conformal shape
- `Number` → spacetime volume scale

즉 `Order + Number ≈ Geometry` 방향.

복원 연구 대상:

- timelike distance
- spacelike distance
- dimension
- topology
- curvature
- manifold-like geometry

Poisson sprinkling은 연속 spacetime → causal set → geometric property recovery를 시험하는 핵심 prior art.

## Reconstruction Reliability Classes

- `EXACT`: causal structure 내부에서 deterministic 복원. 예: Link → full causal order.
- `ANCHORED`: 정확한 timestamp/position/state digest 등의 anchor로 복원오차를 제한.
- `STATISTICAL`: 거시 geometry처럼 통계적/점근적 복원.
- `VIEW-DEPENDENT`: Object/Persona 등 목적별 고수준 materialization.
- `NON-RECOVERABLE`: 원본에서 버린 정보. 예: `A--m-->B`의 m을 버리고 `A≺B`만 남기면 m의 의미는 복원 불가.

중요 원칙 후보: derived reconstruction을 다시 ground fact처럼 쓰며 `추정→추정 기반 추정`을 반복하지 않는다.

## Complexity Warning

`Link-only`가 항상 sparse한 것은 아니다. chain에서는 N-1 Links이지만, 구조에 따라 Link 수 자체가 O(N²)에 근접할 수 있다. 따라서 Causal Set은 자동 경량 storage가 아니라 **의미론적 추상화**로 평가한다.

## Cycle Cut Test

Causal order는 동일 event로 돌아오는 cycle을 허용하지 않는다. 그러나 반복 pattern은 새 occurrence로 펼칠 수 있다.

`A0→B1→A2→B3→A4...`

따라서:

- Causal Event Cycle: 동일 event로 돌아감 → 불가.
- State/Pattern Cycle: 같은 state/pattern이 새 occurrence에서 반복 → 가능.

강한 문장 후보:

> Event는 순환하지 않아도 Pattern은 순환할 수 있다.

## Owner Fit / Difference

Owner worldview에서 국소 mapping은 실제 transformation 내용을 가질 가능성이 크다. Causal Set은 그 내용을 버리고 causal skeleton만 보존한다. 따라서 현재는 `고해상도 worldview`와 `implementation abstraction`을 분리하는 prior art로 가장 매력적이다.

작성시각: 2026-08-22 02:37 KST
