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

작성시각: 2026-08-22 02:49 KST
