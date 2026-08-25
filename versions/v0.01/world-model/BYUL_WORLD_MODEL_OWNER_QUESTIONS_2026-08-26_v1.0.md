# BYUL World Model — Owner 질문 및 결정 등록부

**Version:** v1.0  
**Date:** 2026-08-26  
**Persona:** BYUL  
**State:** OWNER DECISION SUPPORT / NON-NORMATIVE / NOT VALIDATED / NOT FROZEN  
**Related review:** `BYUL_WORLD_MODEL_DEEP_DESIGN_REVIEW_2026-08-26_v1.0_CANDIDATE.md`  
**Related roadmap:** `BYUL_WORLD_MODEL_ROADMAP_2026-08-26_v2.0_CANDIDATE.md`

## 0. 사용법

모든 질문에 지금 답할 필요는 없다. 다음 설계와 probe 범위를 바꾸는 질문부터 정리했다.

- **우선순위 0:** 계층형 아키텍처와 최초 probe 확정 전 결정할 사항
- **우선순위 1:** Port/FOLD/Execution Profile과 prototype 과정에서 결정할 사항
- **우선순위 2:** CATALOG와 실험 증거가 성숙할 때까지 OPEN으로 유지할 사항

각 질문의 권고 기본값은 연구 지속을 위한 임시값이며 채택·동결된 Owner 결정이 아니다.

# 1. 우선순위 0 — 아키텍처 결정 질문

## Q0-1. BYUL의 최종 제품 정체성은 무엇인가?

**질문:** BYUL은 World Model 연구체계, 사람이 작성하는 Modeling/Programming Language, Compiler/IR, Runtime/Execution Platform 중 무엇인가? 또는 이들을 명시적으로 분리한 하나의 프로젝트인가?

**왜 중요한가:** 하나의 표현을 ontology, 작성 문법, compiler IR, runtime layout로 동시에 사용하면 의미와 실행비용이 서로 발목을 잡을 위험이 가장 크다.

**권고 기본값:** 하나의 프로젝트 안에서 다음 층을 명시적으로 분리한다.

```text
World Semantics
  -> Authoring / Analysis
  -> Executable Composition IR
  -> Lowering / Optimization
  -> Runtime
```

`OWNER DECISION = ____________________________________________`

## Q0-2. FOLD된 Composition 내부에 native/opaque 구현을 허용할 것인가?

**질문:** 모든 실행단위가 끝까지 BYUL Relation으로 EXPAND 가능해야 하는가? 아니면 typed interface와 계약을 만족한다면 C/Rust 코드, GPU kernel, DB query, 외부 service, legacy library를 내부 구현으로 허용할 것인가?

**왜 중요한가:** 완전 전개 강제는 통합성과 성능을 제한하고, 무계약 opacity는 추적성·검증·최적화를 무너뜨릴 수 있다.

**권고 기본값:** typed FOLD contract 뒤에서 허용한다. Ports/types, effects, time/resource behavior, determinism, failure semantics, lineage/evidence를 선언하고 가능한 경우 reference semantics 또는 witness를 둔다.

`OWNER DECISION = ____________________________________________`

## Q0-3. Higher-order Composition에 PORT/INTERFACE를 의무화할 것인가?

**질문:** 큰 Composition을 FOLD했을 때 외부와의 모든 상호작용은 명시적이고 typed된 Port/Interface를 거쳐야 하는가?

**왜 중요한가:** 경계가 없으면 FOLD는 안전한 추상화가 아니라 시각적 숨김이 된다. Routing, effects, resource ownership, scheduling과 최적화 가능성을 보존하기 어렵다.

**권고 기본값:** 실행 가능한 FOLD에는 의무화한다. 다만 지금 곧바로 ontological Primitive로 동결하지 않는다.

`OWNER DECISION = ____________________________________________`

## Q0-4. 서로 다른 Composition 영역이 서로 다른 실행 의미를 가져도 되는가?

**질문:** 한 영역은 static dataflow, 다른 영역은 synchronous control, 다른 영역은 async process/actor, 또 다른 영역은 bounded dynamic graph rewrite로 동작하도록 허용할 것인가?

**왜 중요한가:** 같은 topology도 blocking, queue, clocked, event-driven, continuous semantics에 따라 전혀 다른 프로그램이 된다. 단일 universal scheduler는 유연성이나 성능을 크게 희생할 수 있다.

**권고 기본값:** 허용한다. 영역별 Explicit Execution Profile/Model of Computation을 지정하고 경계에는 typed adapter를 둔다.

`OWNER DECISION = ____________________________________________`

## Q0-5. 실행을 위한 Operational State를 명시적으로 둘 수 있는가?

**질문:** 고수준 State가 View/Condition에 의존한다는 가설을 유지하면서 runtime history/progress/state를 별도로 표현할 수 있는가?

**왜 중요한가:** K-of-N join, quorum, timeout, retry, cancellation, feedback, incremental computation과 resource ownership에는 실제 이력과 진행상태가 필요하다.

**권고 기본값:** 허용한다. Interpreted/ontological State와 operational execution State를 분리한다.

`OWNER DECISION = ____________________________________________`

## Q0-6. Dynamic topology는 전역 자유인가, 표시된 capability인가?

**질문:** 어떤 Relation/Composition도 언제든 topology를 바꿀 수 있는가, 아니면 topology-changing behavior는 marked dynamic region/capability 안에서만 허용할 것인가?

**왜 중요한가:** 전역 arbitrary topology mutation은 scheduling, memory planning, static analysis, reproducibility와 accelerator lowering을 매우 어렵게 한다.

**권고 기본값:** Dynamic topology는 허용하되 marked region에 국소화한다. 실행 hot path의 기본은 static 또는 bounded-dynamic region으로 둔다.

`OWNER DECISION = ____________________________________________`

## Q0-7. Determinism의 기본정책은 무엇인가?

**질문:** BYUL 실행은 기본 deterministic인가, 기본 nondeterministic인가, 아니면 region별 선언인가?

**왜 중요한가:** routing, race, concurrency, distributed execution은 scheduler 순서에 따라 결과가 달라질 수 있다. 명시하지 않으면 재현성·테스트·최적화 계약이 모호해진다.

**권고 기본값:** region별로 명시한다. Static dataflow와 synchronous control은 deterministic을 기본으로 하고 async/dynamic 영역은 보장 수준을 선언한다.

`OWNER DECISION = ____________________________________________`

## Q0-8. VIEW는 기본적으로 분석용인가, 실행을 바꾸는 요소인가?

**질문:** View 선택은 projection/interpretation만 바꾸는가, 아니면 실제 route와 behavior도 바꾸는가?

**왜 중요한가:** 모든 View가 runtime-active라면 최적화와 재현성이 어려워지고, 언제나 문서용이면 적응형 관측·제어를 표현하기 어렵다.

**권고 기본값:** VIEW는 기본적으로 analysis/projection이다. 실행에 영향을 주는 View는 operational relation/condition/transform으로 명시적으로 materialize한다.

`OWNER DECISION = ____________________________________________`

## Q0-9. 최초 성능 목표 workload 두 개는 무엇인가?

후보:

- CPU control/orchestration
- numeric/dataflow CPU
- GPU/tensor
- distributed service/agent Composition
- database/query
- real-time embedded

**왜 중요한가:** 고성능에는 단일 지표가 없다. Throughput, latency, determinism, memory footprint와 distribution cost가 workload마다 다르다.

**권고 기본값:** 최초 두 목표를 `static dataflow 또는 numeric/signal pipeline`과 `reactive/coordination workflow`로 둔다. Bounded dynamic topology는 세 번째 stress target으로 두고 첫 inner-loop benchmark로 삼지 않는다.

`OWNER DECISION = ____________________________________________`

## Q0-10. FIRST BYUL은 무엇을 증명해야 하는가?

**질문:** 완결된 thermostat 하나면 충분한가, 아니면 서로 다른 semantic region, FOLD 경계와 lowering witness까지 보여야 하는가?

**권고 기본값:** FIRST BYUL을 단일 데모가 아니라 다음 acceptance suite로 둔다.

- static/timed Composition 1개;
- reactive/coordination Composition 1개;
- 둘 사이의 FOLD/Port 경계;
- async 또는 bounded-dynamic 경계 1개;
- micro-to-macro traceability;
- handwritten/reference baseline과 비교한 lowering 측정.

`OWNER DECISION = ____________________________________________`

# 2. 우선순위 1 — Interface와 실행 질문

## Q1-1. Relation/Port를 통해 무엇이 흐를 수 있는가?

후보: value, event/token, stream/future, resource/capability reference, control dependency, backend memory handle.

**권고 기본값:** 하나의 untyped payload로 뭉개지 말고 typed kind를 명시한다.

`OWNER DECISION = ____________________________________________`

## Q1-2. 최초 communication discipline은 무엇인가?

후보: synchronous call/rendezvous, blocking/nonblocking channel, buffered queue, push/pull stream, latest-value/lossy signal, broadcast/multicast, backpressure.

**권고 기본값:** profile별로 작은 초기 집합만 지원한다. 모든 discipline을 하나의 Relation primitive에 넣지 않는다.

`OWNER DECISION = ____________________________________________`

## Q1-3. Time은 어떻게 표현할 것인가?

후보: physical time, logical tick, event timestamp, partial-order progress, profile별 clock과 cross-domain adapter.

**권고 기본값:** profile/region별 time semantics를 두고 경계에서 변환 계약을 명시한다. Universal Time Primitive는 서두르지 않는다.

`OWNER DECISION = ____________________________________________`

## Q1-4. Effect와 resource를 어느 정도까지 명시할 것인가?

**질문:** Executable Transform은 read/write, allocation, I/O, external call, resource conflict를 선언해야 하는가?

**권고 기본값:** 실행영역에서는 명시한다. FOLD 경계에는 coarse summary를 허용하되 EXPAND로 refinement할 수 있어야 한다.

`OWNER DECISION = ____________________________________________`

## Q1-5. Ownership/copy semantics는 무엇부터 지원할 것인가?

후보: immutable copied value, shared reference, linear/owned resource, borrowed resource, backend-specific handle.

**권고 기본값:** immutable value + explicit resource handle로 시작한다. Zero-copy와 안전성의 실익이 확인되는 곳에 linear/borrow semantics를 추가한다.

`OWNER DECISION = ____________________________________________`

## Q1-6. Interface가 호환되지 않을 때 무엇을 할 것인가?

후보: static rejection, explicit adapter Composition, runtime negotiation, best-effort coercion.

**권고 기본값:** static rejection 또는 explicit adapter를 기본으로 한다. Runtime negotiation은 marked dynamic region에서만 허용한다.

`OWNER DECISION = ____________________________________________`

## Q1-7. Adapter가 보장을 바꿀 때 어떻게 표시할 것인가?

**권고 기본값:** determinism, ordering, timing, failure, delivery 보장이 보존·약화·변환되는지를 adapter contract에 명시한다.

`OWNER DECISION = ____________________________________________`

## Q1-8. Performance Profile은 권고인가, 강제 가능한 계약인가?

**질문:** `STATIC/HIGH-PERFORMANCE`로 지정된 영역이 dynamic behavior 때문에 보장을 만족하지 못하면 compiler가 거부할 수 있는가?

**권고 기본값:** 거부할 수 있다. Profile은 hint가 아니라 검증 가능한 contract로 둔다.

`OWNER DECISION = ____________________________________________`

## Q1-9. 모든 고수준 operation에 decomposition witness가 필요한가?

**권고 기본값:** core/standard operation에는 필요하다. Native/opaque component는 완전한 Relation 전개 대신 typed reference contract와 external proof/evidence를 제공할 수 있다.

`OWNER DECISION = ____________________________________________`

## Q1-10. 최적화 후 source lineage를 어떻게 유지할 것인가?

**권고 기본값:** lowered/optimized node는 source Relation/Composition과 many-to-many provenance link를 유지한다. 이를 형이상학적 동일성으로 해석하지 않는다.

`OWNER DECISION = ____________________________________________`

# 3. 우선순위 2 — 당분간 OPEN으로 둘 기초 질문

## Q2-1. CONDITION은 Primitive인가, guard/contract facet인가, derived Relation인가?

Synchronization/time/state probe 전에는 동결하지 않는다.

## Q2-2. TRANSFORM은 universal Primitive인가, pure/effect/state/topology-rewrite operation family인가?

Executable IR과 effect modeling을 시험한 뒤 판단한다.

## Q2-3. VIEW는 ontology의 일부인가, 주로 meta-level projection인가?

현재 권고 기본값은 materialize되지 않는 한 meta-level이다.

## Q2-4. Orientation은 유용한 derived property로 남는가?

Multi-target routing, distribution, stochastic/cyclic network를 시험한 뒤 판단한다.

## Q2-5. BYUL에서 Causality는 무엇인가?

계속 OPEN으로 둔다. Ordered endpoint를 cause/effect와 동일시하지 않는다.

## Q2-6. 서로 다른 Execution Profile/MoC 아래에 공통 추상화가 있는가?

Semantic-region 실험 뒤 연구한다. 단순 합집합이 공통 모델이라고 가정하지 않는다.

## Q2-7. Self-modification과 learning은 정확히 무엇을 바꾸는가?

값, policy, route, topology, grammar, model 자체를 구분한다. 각각 검증과 성능 의미가 다르다.

## Q2-8. Security/authority semantics는 언제 도입하는가?

Dynamic component, external tool, resource capability에는 결국 권한과 책임경계가 필요하다.

## Q2-9. Uncertainty와 probability를 어떻게 구분할 것인가?

Probabilistic policy, uncertain belief, random execution, unknown information을 분리한다.

## Q2-10. Object/Persona boundary는 어떻게 생성·계승·종료되는가?

Composition-first 철학을 유지하면서 interface, memory, authority의 실용적 경계를 정의해야 한다.

# 4. 임시 권고 기본 패킷

Owner 답변 전까지 연구는 다음 기본값으로 진행할 수 있다. 이는 freeze가 아니다.

```text
BYUL = layered World Model + language/IR/tooling project
Opaque/native component = typed FOLD contract 뒤에서 허용
PORT/INTERFACE = folded executable Composition에 의무
Execution Profile/MoC = 명시적이고 계층적으로 조합 가능
Operational state/effect = 명시
Dynamic topology = marked region에 국소화
Determinism = region별 선언
VIEW = 기본적으로 analysis/projection
최초 성능 target = static dataflow + reactive coordination
FIRST BYUL = multi-region acceptance suite + measured lowering witness
```

# 5. Owner 응답 양식

```text
Q0-1 =
Q0-2 =
Q0-3 =
Q0-4 =
Q0-5 =
Q0-6 =
Q0-7 =
Q0-8 =
Q0-9 =
Q0-10 =

Priority-1에서 권고 기본값과 다르게 할 항목 =
추가 제약 또는 반드시 지킬 목표 =
```

답하지 않은 우선순위 1·2 질문은 OPEN으로 유지하고 임의로 동결하지 않는다.

**Owner action now:** 우선순위 0 중 다음 probe의 범위를 바꾸는 항목부터 결정  
**Validation claim:** `NONE`  
**Ontology freeze:** `FALSE`
