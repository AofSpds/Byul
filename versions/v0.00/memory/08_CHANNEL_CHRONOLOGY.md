# 08. Channel Chronology — How the Hypothesis Changed

이 파일은 결론 요약보다 **가설이 어떻게 바뀌었는지**를 복원하기 위한 연대기다.

## Phase 1 — Mapping First

Owner는 `A=>B`에서 값보다 `=>` 자체가 중요하다는 직관을 강하게 제시했다. 함수/사상이 다른 함수에 영향을 줄 수 있고, 여러 사상이 합성되며, Object는 projection일 수 있다는 가능성을 열었다.

이때 `f:A→B`가 A/B Object를 미리 전제한다는 Hidden-Object Problem이 발견됐다.

## Phase 2 — Interaction-first

`상호작용이 먼저일 수 있다`가 강한 후보로 올라왔다. 관측도 외부 meta-operation이 아니라 세계 내부 interaction/mapping으로 볼 가능성을 탐색했다.

## Phase 3 — Opposite-direction Bundles

A→B와 B→A를 각각 여러 mapping의 bundle로 표현하는 후보가 매우 매력적으로 보였다. 역함수/대칭일 필요는 없고 서로 다른 속도를 가진 coupling으로 생각했다.

## Phase 4 — Time Correction

Owner가 `1ms전의 나는 없습니다`, `동시는 동시가 아니다`라고 지적하면서 단일 bidirectional primitive에 의문이 생겼다.

`A↔B`보다 `A0→B1→A2→B3...` 같은 future-directed history가 더 고해상도일 수 있다는 가설이 등장했다.

Reciprocity는 primitive relation보다 time-extended causal pattern일 가능성이 생겼다.

## Phase 5 — Micro-mapping Composition Network

Owner가 다시 correction:

> A/B 두 객체와 두 방향 bundle로 묶는 것 자체도 이미 낮은 해상도일 수 있다. 실제 세계관은 무수한 작은 함수/사상이 합성된 망에 더 가깝다.

현재 strongest worldview phrase인 `무수한 국소 사상들의 합성망`이 자리잡았다.

## Phase 6 — Primitive Resolution

Owner는 primitive search에서는 가능한 높은 해상도를 선호하지만 물리적 최소단위 존재는 전제하지 않는다고 명시했다.

`minimum effective local mapping`은 hypothesis로 유지.

## Phase 7 — Causal Set Discovery

Causal Set Theory가 매우 흥미로운 prior-art로 부상.

매력:
- space/global clock를 primitive로 강하게 요구하지 않음
- event + causal order
- partial order
- link / chain / antichain
- order+number를 통한 geometry reconstruction

중요한 연구 분리:

`HIGH_RESOLUTION_WORLDVIEW_HYPOTHESIS != IMPLEMENTATION_ABSTRACTION`

Owner는 실제 worldview를 그대로 구현하지 않고 causal skeleton 같은 과감한 추상화를 쓰는 발상에 강한 매력을 느낌.

## Phase 8 — Link / Chain / Antichain Clarification

Link는 최소 국소 사상과 같지 않다는 차이를 확인.

- Link: direct causal-order adjacency
- local mapping: actual transformation semantics 가능

Chain에서는 longest chain이 proper-time-like quantity와 연결됨을 학습.

Antichain에서 Owner correction:

> 비교할 필요가 없음이 아니라 비교불가.

절대 NOW를 primitive로 두지 않는 방향을 강하게 이해.

## Phase 9 — Causal Diamond / Reconstruction

Owner는 causal diamond와 기존 추상화 아이디어가 유사하다고 느낌.

Order + Number에서 geometry를 복원한다는 아이디어에 큰 매력을 느낌.

곧바로 중요한 반론 제기:

> 어디까지 복원이 가능한가? 복원 신뢰성이 없고 열화된다면?

이 질문으로 Causal Set의 한계가 더 선명해짐.

## Phase 10 — Reconstruction Classes / Anchors

복원을 EXACT / ANCHORED / STATISTICAL / VIEW-DEPENDENT / NON-RECOVERABLE로 분리할 후보가 생김.

버린 transformation semantics는 복원할 수 없다는 점을 명확히 함.

복원값을 다시 ground truth처럼 써 누적열화를 만드는 것을 피하고 anchor/checkpoint를 두는 보완 방향이 제안됨.

## Phase 11 — Complexity Warning

Owner가 `potentially O(N²) relations ?????`라고 강하게 반응.

중요 correction:

- Link-only 표현도 항상 sparse하지 않음.
- Causal Set은 자동 경량 storage가 아니라 의미론적 추상화.

또 `시간의 엄밀성이 필요없을 때 유리`라는 표현을 수정:

- causal order는 엄밀히 보존.
- exact metric time/absolute NOW/coordinates가 필요 없는 상황에 유리.

## Phase 12 — Complementary Model Need

Owner가 열화 보완과 상호보완 모델 필요성을 명시.

Causal Set 하나로 World Model 전체를 맡기기보다 transformation/state/resource/cycle 등을 잘 표현하는 기존 formalism을 비교하기 시작.

## Phase 13 — Petri / Event / LTS / Rewrite Family

Petri Net:
- possible behaviour
- resource
- concurrency
- cycle

Occurrence/Event:
- actual occurrence
- causality/concurrency/conflict

LTS:
- state transition view

Reconfigurable Petri / graph rewrite:
- model structure 자체 mutation

Open Petri:
- local composition

이때 기존 후보를 단순 나열하지 말고 **상호호환/보완성이 높은 family**로 재조직해야 한다는 Owner 요구가 강해짐.

## Phase 14 — Index Complement

Owner가 모델을 `index의 보완 개념으로 볼까?`라고 제안.

현재 구분:

- Causal/Event/LTS 일부는 source record에 대한 semantic index/view처럼 볼 수 있음.
- Petri는 possible behaviour를 가지므로 단순 index가 아니라 executable behaviour model.

Occurrence/Fact Plane ↔ Behaviour/Rule Plane의 이중 구조 후보가 등장.

## Phase 15 — Reverse Compatibility

Owner 질문: 역방향 호환 불가능한가?

답:
- 전면 불가능 아님.
- exact inverse보다 synthesis가 많음.
- 호환성을 EXACT / SEMANTIC / APPROXIMATE / NON-RECOVERABLE로 봐야 함.

Round-trip loss와 preservation contract가 중요해짐.

## Phase 16 — P-series / Routing

Owner clarification:

> P-series 원칙을 벗어나지 않으면 구현은 열려 있다.

또:

> 후보 모델은 P-series 원칙과 잘 맞고 상호 mutating이 쉬울 것.
> 후보 모델에 어울리는 상황을 미리 식별 가능한 기준 필요.

`Situation Fingerprint`가 핵심 연구후보로 등장.

Owner는 `상황별 모델 라우팅 개념`을 매우 좋다고 평가.

## Phase 17 — R(S,M,L)

Owner가 3개의 인자를 가진 함수/map가 필요하다고 지적.

현재 후보:

`R(Situation, Current Model State, Lifecycle Context)`

P-series는 routing input보다 external invariant gate 후보.

## Phase 18 — Lifecycle Validation / Committee Scenarios

Owner 요구:

- model lifecycle validation simulation 확보 필요.
- transformation cost를 실제 simulation으로 측정 필요.
- 필요하면 다양한 scenario를 위원회에 공모 가능 여부 검토.

위원회 blind generation / model attack / coverage gap 구조 후보가 생김.

## Phase 19 — MI-1 Initialization

Owner:

> MI-1안으로 테스트 해볼 가치가 있다.

첫 목표는 solution generation이 아니라 fresh instance가 현재 memory로 연구상태를 정확히 복원하는지 평가하는 것.

초기상태 복원 자체가 모델 성능축.

## Phase 20 — Byul Repository Separation / Version Boundary

Owner가 현재까지 메모한 모든 내용을 별도 GitHub `AofSpds/Byul`에 분리 정리 요청.

버전 결정:

- `v0.00`: 최초 research/context backup.
- `v0.01`: v0.00 successor copy, 이후 active memo 진행.
- `v0.1부터 모델 실구현`.

즉 v0.0x는 연구·메모·초기화·검증설계 단계이며 실제 구현은 v0.1+에서 시작.

작성시각: 2026-08-22 02:37 KST
