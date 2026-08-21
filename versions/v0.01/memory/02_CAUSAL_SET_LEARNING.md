# 02. Causal Set Learning

COPIED_FROM: `versions/v0.00/memory/02_CAUSAL_SET_LEARNING.md`

## Position
Causal Set Theory(인과집합이론)는 final architecture가 아니라 `Event + Causal Order`를 최소 골격으로 두고 좌표·공간·global NOW를 primitive에서 제거하는 강한 prior-art abstraction 후보.

## Core
- Partial order: 어떤 두 사건은 인과적으로 비교 불가능할 수 있음.
- Link: 중간 causal event가 없는 직접 인과 인접. transformation 의미 없음.
- Chain: causal order로 한 줄 정렬 가능한 사건 집합. longest chain은 proper-time-like quantity와 연결.
- Antichain: 서로 causal하게 비교 불가능한 사건 집합. exact simultaneity/absolute NOW 아님.
- Causal Interval/Diamond: `Interval(p,q)={x|p≺x≺q}`. diamond shape 자체는 저장하지 않음.

## Time
- global absolute NOW를 primitive로 두지 않음.
- causal order는 엄밀히 보존.
- exact metric time/coordinates는 별도 문제.

## Reconstruction
`Order + Number ≈ Geometry` 방향.

복원 연구 대상: timelike/spacelike distance, dimension, topology, curvature, manifold-like geometry.

복원 등급 후보:
- EXACT
- ANCHORED
- STATISTICAL
- VIEW-DEPENDENT
- NON-RECOVERABLE

버린 transformation semantics는 복원 불가.
Derived reconstruction을 다시 ground truth처럼 승격해 누적열화시키지 않는 방향 강함.

## Complexity Warning
Link-only도 항상 sparse하지 않으며 구조에 따라 O(N²)에 근접 가능. Causal Set은 자동 경량 storage가 아니라 의미론적 추상화로 평가.

## Cycle
동일 causal event cycle은 금지되지만 state/pattern cycle은 새 occurrence로 전개 가능:
`A0→B1→A2→B3...`

강한 문장 후보:
> Event는 순환하지 않아도 Pattern은 순환할 수 있다.

## Owner Fit
Owner local mapping은 actual transformation semantics를 가질 가능성이 크고 Causal Link는 causal skeleton만 가진다. 따라서 worldview 자체보다 implementation abstraction / causal index / reconstruction prior-art로 현재 가장 매력적.

작성시각: 2026-08-22 02:37 KST
