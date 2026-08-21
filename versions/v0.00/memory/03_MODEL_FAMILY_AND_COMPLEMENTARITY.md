# 03. Model Family & Complementarity

## Why One Model Is Not Enough

현재 후보 formalism들은 서로 같은 층위가 아니다. 하나를 universal model로 강제하면 어떤 semantics를 잘 보존하는 대신 다른 semantics를 잃을 가능성이 높다.

현재 더 강한 방향은 **상호보완 family + 목적별 projection/view**다.

## Candidate Family

### Behaviour / Rule Plane

#### Petri Net(페트리 네트)
- possible behaviour
- resource / token
- concurrency
- synchronization
- cycle / repeated behaviour
- compact reusable rule structure

핵심 질문: `무엇이 어떤 조건에서 일어날 수 있는가?`

#### Open Petri Net(개방형 페트리 네트)
- input/output interface를 가진 local net
- 작은 모델들의 composition/gluing 후보
- Owner의 `무수한 국소 사상들의 합성망`과 비교 우선순위 높음

#### Reconfigurable Petri Net(재구성 가능 페트리 네트)
- marking/state mutation과 net/model mutation을 분리
- `M0→M1`과 `N0→N1`을 함께 표현
- 함수/규칙/관계 구조 자체가 바뀌는 Owner 직관과 비교 가치 높음

### Occurrence / Concurrency Plane

#### Occurrence Net(발생 네트)
- Petri Net의 반복 가능한 behaviour를 개별 occurrence로 펼치는 bridge
- causal dependence / concurrency / conflict를 occurrence 수준에서 표현

#### Event Structure(사건 구조)
- causality + concurrency + conflict
- 실제/가능 occurrence 의미론에 강함

### Projection / Index / View

#### Causal-order View / Causal Index
- 무엇이 무엇보다 causal하게 앞서는지에 최적화
- Causal Set의 장점 활용
- transformation/resource/conflict 의미를 원본에서 삭제하면 역복원 불가

#### LTS(라벨 전이 시스템) / Reachability View
- state + labelled transition
- 현재 상태에서 어디로 갈 수 있는지 질의에 강함
- Petri marking을 state로 보면 reachability graph/LTS 형태로 전개 가능
- 단순 interleaving은 진정한 concurrency 의미를 약화시킬 수 있음

## Strong Prior-art Transformation Skeleton

`Petri Net → unfolding → Occurrence Net → Event Structure → causal forgetting → Causal-order View`

그리고:

`Petri Net → reachability graph → LTS-like View`

Open Petri는 composition 방향, Reconfigurable Petri는 model mutation 방향을 보강한다.

## Reverse Compatibility

역방향 호환은 전면 불가능하지 않다. 다만 exact inverse보다 reverse synthesis가 많다.

호환/복원 등급 후보:

- `EXACT`
- `SEMANTIC`
- `APPROXIMATE`
- `NON-RECOVERABLE`

예:

- Petri → LTS: 자연스러움.
- LTS → Petri: 특정 조건에서 synthesis 가능, 원본 net 유일성은 보장되지 않을 수 있음.
- Petri → Occurrence: unfolding 가능.
- Occurrence → Petri: folding/synthesis 가능성이 있으나 반복/대칭 때문에 비유일 가능.
- Event Structure → causal order: 쉬움.
- causal order → 원래 Event Structure: conflict/label/resource를 버렸다면 일반적으로 불가.

## Index Complement Concept

Occurrence/Fact 원본에서 목적별 semantic index/view를 유지하는 방향이 매력적이다.

- Causal Index: ancestry / reachability
- Concurrency/Conflict Index: 독립/충돌
- State/Reachability Index: reachable state/action
- Metric/Object/Persona View: 고수준 materialization

그러나 Petri Net은 이미 실제 history를 정리한 index가 아니라 아직 일어나지 않은 possible behaviour까지 가지므로 **Executable Behaviour Model**로 별도 취급한다.

현재 강한 구조 후보:

`Occurrence / Fact Plane ↔ Behaviour / Rule Plane`

그리고 상황에 따라 semantic model/index/view를 선택하는 Router.

## Core Complementarity Insight

Petri와 Causal history는 경쟁 모델이라기보다 질문이 다르다.

- Petri: `무엇이 일어날 수 있는가?`
- Occurrence/Causal history: `실제로 무엇이 일어났는가?`

Event Structure는 그 사이에서 causality/concurrency/conflict를 보존하는 중요한 bridge 후보.

## Non-conclusions

- Petri Net이 canonical model이라는 결론 없음.
- Causal Set을 단순 secondary index로 확정하지 않음.
- 하나의 canonical representation + many views 구조를 강제하지 않음.
- 정보 종류별 authoritative representation이 다를 가능성도 열어둠.

작성시각: 2026-08-22 02:37 KST
