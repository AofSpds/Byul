# 03. Model Family & Complementarity

COPIED_FROM: `versions/v0.00/memory/03_MODEL_FAMILY_AND_COMPLEMENTARITY.md`

## Current Direction
하나의 universal model보다 상호보완 family + 목적별 projection/view를 연구.

### Behaviour / Rule
- Petri Net: possible behaviour, resource, concurrency, synchronization, cycle.
- Open Petri Net: local composition/gluing.
- Reconfigurable Petri Net: state mutation과 model/net mutation을 함께 다루는 후보.

### Occurrence / Concurrency
- Occurrence Net: Petri behaviour를 occurrence history로 unfolding하는 bridge.
- Event Structure: causality + concurrency + conflict.

### Projection / Index / View
- Causal-order View / Causal Index: ancestry/causal reachability.
- LTS / Reachability View: state transition/reachability.

## Strong Prior-art Skeleton
`Petri → unfolding → Occurrence → Event Structure → causal forgetting → Causal-order View`

`Petri → reachability graph → LTS-like View`

## Reverse Compatibility
전면 불가능하지 않음. exact inverse보다 synthesis가 많고 비유일성 가능.

등급 후보:
- EXACT
- SEMANTIC
- APPROXIMATE
- NON-RECOVERABLE

## Index Complement
Occurrence/Fact 원본에서 목적별 Causal/Concurrency/State/Metric/Object view를 만들 수 있음.

Petri는 possible behaviour까지 포함하므로 단순 index가 아니라 executable behaviour model.

현재 후보 구조:
`Occurrence / Fact Plane ↔ Behaviour / Rule Plane`

## Complementarity Insight
- Petri: 무엇이 일어날 수 있는가?
- Occurrence/Causal history: 실제로 무엇이 일어났는가?
- Event Structure: 그 사이의 causality/concurrency/conflict bridge 후보.

## Non-conclusions
- Petri canonical model 확정 아님.
- Causal Set secondary index 확정 아님.
- one canonical representation 강제 아님.
- 정보 종류별 authoritative representation이 다를 가능성 열림.

작성시각: 2026-08-22 02:37 KST
