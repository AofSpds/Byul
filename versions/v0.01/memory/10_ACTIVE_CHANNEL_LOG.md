# 10. Active Channel Log — v0.01

## Purpose

이 파일은 `AAA-ASA-ME`의 **현재 진행 중 메모**를 append-like 방식으로 축적하기 위한 active log다.

구조화된 안정 상태는 00~09 문서로 승격하고, 새 대화에서 생긴 가설·수정·Owner correction·다음 작업은 먼저 이 파일에 기록한다.

## Mandatory Rule

- 채널 승계 전 반드시 현재 active log를 갱신한다.
- 승계 successor는 `v0.01/README.md`와 00~10을 읽어야 한다.
- material하게 정리된 내용은 적절한 structured memory 문서로 승격한다.
- v0.1 전에는 모델 실구현을 시작하지 않는다.

## Initial Active State — 2026-08-22 02:37 KST

- Byul 저장소 분리 완료 진행 중.
- v0.00: 최초 context/memory backup snapshot.
- v0.01: active research successor.
- v0.1부터 model implementation 시작.
- 다음 주요 잡 후보: `Lifecycle + Routing Simulation Challenge Requirements`를 위원회 외주용으로 정리.
- MI-1에서 fresh-instance initial-state reconstruction 시험 가치 높음.
- current strongest routing candidate: `R(S,M,L)`.
- current strongest worldview phrase: `무수한 국소 사상들의 합성망`.
- 후보 model family는 Petri/Open Petri/Reconfigurable Petri + Occurrence/Event + Causal/LTS projection의 상호보완성 중심으로 재검토 중.

## Research Reconstruction — 2026-08-22 02:49 KST

현재까지의 구조화 메모를 하나의 연구 흐름으로 재구성하면 다음과 같다.

1. **Owner high-resolution worldview**
   - 현행 strongest phrase는 `무수한 국소 사상들의 합성망`.
   - Object/Self/Persona/Boundary는 primitive 확정이 아니라 높은 scale에서 materialize되는 persistent pattern/view일 가능성을 탐구.
   - `Me_T0 = Me_T1`보다 `Me_T0 → Me_T1`의 succession/history 관점이 강함.
   - global absolute NOW를 primitive로 두지 않고, reciprocity는 `A0→B1→A2...`의 time-extended causal pattern일 가능성을 유지.
   - Event / Local Mapping / Interaction / Composition / Rewrite / typed morphism 등 primitive/minimal algebra는 OPEN.

2. **Causal Set prior-art finding**
   - Causal Set은 worldview 정답이 아니라 `Event + Causal Order` causal skeleton/reconstruction prior art로 매력적.
   - Link/Chain/Antichain/Causal Interval을 통해 global NOW와 coordinate를 primitive에서 제거할 수 있음.
   - `Link→causal order`는 exact reconstruction 가능하지만 geometry reconstruction은 조건부·통계적이며, 버린 transformation semantics는 복원 불가.
   - Link-only 표현도 구조에 따라 O(N²)에 근접할 수 있어 자동 경량 storage라는 결론은 금지.
   - 동일 causal event cycle과 반복되는 state/pattern cycle을 구분: `Event는 순환하지 않아도 Pattern은 순환할 수 있다.`

3. **Complementary model family**
   - Behaviour/Rule Plane: Petri Net, Open Petri Net, Reconfigurable Petri Net.
   - Occurrence/Concurrency Plane: Occurrence Net, Event Structure.
   - Purpose-specific projection/index/view: Causal-order View, LTS/Reachability View.
   - Petri는 `무엇이 일어날 수 있는가`, occurrence history는 `실제로 무엇이 일어났는가`, Event Structure는 causality/concurrency/conflict bridge라는 현재 해석.
   - one universal/canonical model은 결정하지 않음.

4. **Compatibility / mutation principle**
   - 후보 formalism 간 forward/reverse translation은 binary compatible/incompatible가 아니라 `EXACT / SEMANTIC / APPROXIMATE / NON-RECOVERABLE` 등급으로 관리할 필요.
   - exact inverse보다 reverse synthesis가 현실적인 경우가 많고 비유일성 가능.
   - round-trip semantic delta와 cumulative semantic drift를 장기 검증해야 함.

5. **Situation-based routing candidate**
   - 현재 strongest routing candidate: `R(S,M,L) → {Target Model Set, Transformation Path, Preservation Contract, Validation Plan}`.
   - S=Situation Fingerprint, M=Current Model State, L=Lifecycle Context.
   - P-series exact semantics는 canonical source에 있고 Byul은 새로 정의하지 않으며, 현재 연구에서는 routing/mutation 결과가 통과해야 하는 상위 gate로 해석.

6. **Lifecycle validation requirement**
   - create→operate→accumulate→adapt→mutate→compose→split/diverge→merge→migrate→degraded→recover→successor/retire 전 과정을 검증해야 함.
   - compute cost뿐 아니라 semantic cost, maintenance cost, reversibility를 분리.
   - 주요 지표 후보: P-series preservation, cumulative drift, round-trip delta, size blow-up, runtime, peak memory, reverse synthesis, invalidation radius, query gain/latency.

7. **Simulation / committee outsourcing**
   - T1~T10 toy/lifecycle scenario와 Petri→LTS→Petri′, Petri→Occurrence→Event→Causal Index 등의 micro-probe 후보 존재.
   - 위원회는 좋은 모델 제안보다 모델/routing assumptions를 깨뜨릴 stress scenario를 공모.
   - Blind Generation / Model Attack / Coverage Gap 세 그룹 구조가 현재 후보.
   - 다음 주요 잡 후보는 `Lifecycle + Routing Simulation Challenge Requirements`.

8. **MI-1 initialization test**
   - fresh instance에게 해결책을 먼저 요구하지 않고 현재 memory만으로 연구 상태를 얼마나 정확히 재구성하는지 평가.
   - initial-state reconstruction quality 자체를 성능축으로 봄.
   - 사실/가설/OPEN/non-conclusion 분리와 hallucinated commitment를 주요 평가 대상으로 둠.

9. **Version boundary**
   - v0.00 = recovery snapshot.
   - v0.01~v0.0x = research/memory/initialization/validation-design.
   - v0.1+ = actual model implementation.

이 재구성은 기존 메모의 working synthesis이며 새로운 normative design 또는 model selection이 아니다.

## Situation Fingerprint v0.01 Research Candidate — 2026-08-22 02:56 KST

목표: `Situation Fingerprint`는 특정 formalism을 직접 지명하는 router rule이 아니라, 현재 상황에서 **무엇을 질의하고 무엇을 잃으면 안 되는지**를 model-agnostic하게 기술하는 입력이어야 한다.

### Core Design Discipline
- Fingerprint 내부에 `Petri`, `Causal Set`, `Event Structure` 같은 모델명을 넣지 않는다. 그렇지 않으면 routing이 순환논리가 됨.
- `feature exists`와 `feature must be preserved`를 구분한다.
- UNKNOWN/UNRESOLVED를 정상값으로 허용한다. 모르는 특성을 억지로 분류하지 않는다.
- P-series는 Fingerprint 필드가 아니라 routing/mutation 결과가 통과해야 하는 외부 gate로 유지한다.
- 정확한 schema/enum은 아직 확정하지 않는다. v0.01에서는 최소 분해축의 적합성을 검증한다.

### Candidate Situation Fingerprint Components

1. **Question / Workload Intent**
   - history/ancestry
   - possible behaviour
   - reachability/state transition
   - concurrency/independence
   - conflict/exclusion
   - resource/capacity
   - composition/interface
   - model/topology mutation
   - metric/time/space
   - reconstruction/materialization

2. **Preservation Demand** — 가장 중요한 후보 축
   - 반드시 lossless로 보존해야 하는 의미
   - semantic equivalence까지 허용되는 의미
   - approximate/statistical reconstruction 허용 의미
   - 버려도 되는 의미
   - UNKNOWN/UNRESOLVED 의미
   - 후보 예: causal history, transformation label, resource constraint, conflict relation, rule lineage, exact timestamp, spatial coordinate, authority/provenance 등

3. **Dynamics / Structural Character**
   - acyclic / cyclic-pattern
   - sequential / concurrent
   - deterministic / branching
   - conflict-bearing
   - resource-constrained
   - compositional/open-boundary
   - topology/rule mutation
   - fork/merge
   - transient/persistent

4. **Scale / Update Shape**
   - entity/event count
   - relation density
   - fan-out/fan-in
   - update frequency
   - local vs global mutation
   - expected growth
   - history depth
   - streaming vs batch

5. **Precision / Reconstruction Tolerance**
   - EXACT required
   - ANCHORED allowed
   - SEMANTIC allowed
   - STATISTICAL allowed
   - VIEW-DEPENDENT allowed
   - NON-RECOVERABLE prohibited/acceptable by field

6. **Operational Constraints**
   - query latency target
   - mutation latency target
   - storage budget
   - conversion budget
   - rollback/recovery need
   - audit/explainability need
   - incremental recomputation requirement

### Current Strong Hypothesis
Situation routing에서 단순한 `현상 유형`보다 `Preservation Demand`가 더 우선적일 가능성이 높다. 같은 cycle/concurrency 상황이라도 무엇을 반드시 보존해야 하는지에 따라 적합 model set과 transformation path가 달라질 수 있기 때문이다.

예: 두 상황 모두 cycle이 있어도,
- 실제 발생 history가 핵심이면 occurrence/history 보존이 우선,
- 가능한 반복 behaviour가 핵심이면 compact behaviour representation이 우선,
- exact timestamp가 핵심이면 별도 metric/clock anchor가 추가로 필요할 수 있음.

### Routing Boundary
현재 3인자 후보는 그대로 유지:
`R(S, M, L)`

- `S`: 위 Situation Fingerprint.
- `M`: 현재 representation / authoritative source / anchors / loss class / lineage / size-density / invalidation state.
- `L`: create/operate/mutate/compose/split/merge/migrate/recover 등 lifecycle context.

Situation Fingerprint 내부 구성은 향후 simulation/committee scenario를 통해 feature importance와 최소 충분성을 검증해야 한다.

### Immediate Validation Questions
- 위 6개 축 중 실제 routing decision에 중복되는 축은 무엇인가?
- 어떤 축이 빠지면 잘못된 model selection이 반복되는가?
- Preservation Demand만으로 상당 부분 routing이 가능한가?
- Situation Fingerprint가 너무 커져 사실상 세계 전체 description이 되는 지점은 어디인가?
- UNKNOWN이 많아도 safe routing/defer가 가능한가?
- fingerprint 자체의 생성 비용이 routing 이득보다 커지지 않는가?

본 항목은 research candidate이며 Requirement/Design 확정이 아니다.

작성시각: 2026-08-22 02:56 KST
