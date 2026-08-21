# 07. Open Questions & Next Jobs

## Open Questions

### OQ-01 Primitive / Minimal Algebra
`Event`, `Local Mapping`, `Interaction`, `Composition`, `Rewrite` 중 무엇을 primitive로 볼지 미결. 하나의 primitive가 아니라 최소 algebra/문법일 수 있음.

### OQ-02 Transformation Semantics
Causal skeleton만으로 충분하지 않은 상황에서 실제 transformation 의미를 어떤 formalism이 가장 손실 없이 보존하는가.

### OQ-03 Model Family Compatibility
Petri/Event/LTS/Causal/Reconfigurable 계열의 정확한 forward/reverse translation 조건, 손실 등급, 비유일성.

### OQ-04 Situation Fingerprint
어떤 상황에서 어떤 model/view를 선택해야 하는지 사전에 식별하는 최소 feature set은 무엇인가.

### OQ-05 Routing Function
`R(S,M,L)`이 충분한가. 추가 인자가 필요한가. 어떤 부분을 deterministic rule로 두고 어떤 부분을 learning/optimization 대상으로 둘 것인가.

### OQ-06 P-series Gate
P-series exact canonical semantics를 훼손하지 않으면서 routing/mutation 결과를 어떻게 검증할 것인가.

### OQ-07 Lifecycle Drift
여러 세대의 conversion/mutation/merge/migration 후 cumulative semantic drift를 어떻게 정의·계측할 것인가.

### OQ-08 Reconstruction Reliability
EXACT / ANCHORED / STATISTICAL / VIEW-DEPENDENT / NON-RECOVERABLE을 어떤 acceptance 기준으로 운용할 것인가.

### OQ-09 Canonical vs Multi-authoritative Representation
하나의 canonical model + views가 필요한가, 아니면 정보 종류별로 서로 다른 authoritative representation을 허용해야 하는가.

### OQ-10 Scale
Causal links, Petri reachability, unfolding/event structures가 각각 어느 조건에서 폭발하는가. incremental index/partial materialization이 가능한가.

### OQ-11 Model Mutation
Reconfigurable Petri / graph rewrite 계열이 Owner의 `함수/구조 자체가 변함`을 충분히 표현하는가.

### OQ-12 Committee Scenario Quality
위원회가 만든 scenario 자체의 coverage, bias, realism, difficulty를 어떻게 검증할 것인가.

## Next Jobs — Current Priority

1. `v0.01` active research snapshot 생성 및 이후 메모 승계.
2. MI-1 initialization/reconstruction 시험 구조 확정.
3. 위원회 시나리오 외주용 `Lifecycle + Routing Simulation Challenge Requirements` 작성.
4. scenario corpus의 blind/model-attack/coverage-gap generation 설계.
5. 모델 lifecycle benchmark acceptance metrics 정교화.
6. `v0.1` 구현 전 exact implementation target 결정.

## Version Boundary

- `v0.00/v0.01~v0.0x`: 연구·메모·검증설계.
- `v0.1+`: 실제 모델 구현 시작.

## Do Not Prematurely Decide

- Petri canonical model
- Causal Set final architecture
- one universal model
- one canonical representation
- Event/local mapping primitive
- automatic semantic reconstruction from discarded data

작성시각: 2026-08-22 02:37 KST
