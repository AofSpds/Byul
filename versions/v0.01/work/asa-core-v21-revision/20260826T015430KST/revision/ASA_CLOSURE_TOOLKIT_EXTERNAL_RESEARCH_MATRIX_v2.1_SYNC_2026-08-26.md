# ASA CLOSURE TOOLKIT — EXTERNAL RESEARCH MATRIX v2.1 SYNC / HYBRID CORE CANDIDATES

```text
STATUS = V2.1_SYNC / INHERITED RESEARCH SYNTHESIS / NON_FROZEN
PROJECT = AAA / BYUL
PRODUCT = ASSET AGENT ASA
DATE_KST = 2026-08-26
RESEARCH_CUTOFF = 2026-08-25
PURPOSE = ASA INIT PRE-CORE TECHNOLOGY REUSE ANALYSIS
TECHNOLOGY_FREEZE = NONE
NEW_EXTERNAL_RESEARCH_IN_THIS_SYNC = NONE
IMPLEMENTATION_AUTHORIZATION = NONE
```

---

## Synchronization note

이 문서는 2026-08-25 research matrix를 다시 조사하거나 평가하지 않았다.
기존 기술 설명·정성 등급·source set을 보존하면서 v2.1 terminology,
Candidate/Probe cross-reference, status와 authority만 동기화한다.

- `VH/H/M/L`은 inherited qualitative assessment이며 측정 benchmark가 아니다.
- Candidate A-D는 비교용 연구 후보이며 selected architecture가 아니다.
- 이 문서가 `P01..P20`과 공통 metric의 canonical registry를 소유한다.
- Citation key는 이 문서 안에서만 유효한 `R4-Rxx` namespace를 사용한다.
- composition closure, Datalog/fixed-point closure, working product label은 서로 같은 뜻이 아니다.

## 0. 연구 질문의 재정의

이번 채널의 Owner-confirmed protocol에 따라 외부기술 비교 질문도 바뀐다.

```text
잘못된 질문
어느 기술이 ASA World Model의 정답인가?

현재 질문
어느 기술이 다음 Closure Tool capability의 일부를 가장 잘 제공하는가?
```

필요 capability:

```text
- current-resolution directional Relation
- recursive composition and interfaces
- meaning-preserving fold
- View-relative expansion/reconstruction
- VIEW / CONTROL / STATE role distinction
- minimum necessary recompute
- compact lineage and replay
- cycles and dynamic patterns
- alternate composition candidates
- AI/latent control and measurement
- replaceable runtime/reference/search planes
```

평가 기호:

```text
VH = Very High
H  = High
M  = Medium
L  = Low
```

---

# I. COMBINATION IDEA MATRIX

| 연구군 | ASA에 제공하는 부품 | 중복 영역 | v2.1 candidate와의 충돌·주의 | Runtime | Reference | AI/Latent | 잠정 배치 |
|---|---|---|---|---:|---:|---:|---|
| **Nested Relational Model / NRC** | nested collection을 값처럼 다루고 nested→nested transformation을 선언. 접힌 `STATE` 표현과 nested View 계산 참고 | Higher-order graph, JSON/records, provenance traces | nested value가 곧 recursive Relation semantics는 아님. 물리 nesting을 ontology로 고정하면 update granularity가 거칠어질 수 있음 | M | H | H | Folded State representation 및 nested query reference |
| **Datalog** | recursive derivation, least/fixed-point closure, declarative dependency | DBSP, provenance, egglog | predicate vocabulary가 final ontology처럼 굳을 위험. arbitrary dynamic operator mutation은 별 관리 필요 | H | VH | H | Recursive View evaluator / correctness oracle |
| **Soufflé** | Datalog을 semi-naïve/fixed-point relational machine과 optimized parallel C++로 compile; provenance 지원 | Datalog/IVM | persistent live runtime보다 batch/static analysis 성격이 강한 영역도 있음 | H | H | M | compiled recursive View prototype / provenance test |
| **DBSP / IVM** | delta stream, rich query incrementalization, composition chain rule, nested/nonmonotonic recursion | Differential dataflow, Datalog, lenses | 무엇이 의미 있는 View인지 정의하지 않음. large-impact delta는 full recompute가 더 나을 수 있음 | VH | H | M | Minimum necessary recompute runtime 핵심 후보 |
| **Differential Dataflow / DDlog** | iterative dataflow에서 additions/retractions와 incremental fixed point | DBSP, Datalog | logical time/lattice가 ASA semantic time과 동일하다고 가정 금지 | VH | H | M | Alternative delta runtime / cycle probe |
| **Higher-Order Graph DB / Hypergraph** | hyperedge, node tuple, subgraph를 higher-order element로 취급; Relation-on-Relation과 polyadic topology | Wiring diagrams, graph rewriting, nested data | subgraph identity, matching cost, schema lock-in. graph가 final ontology가 되어서는 안 됨 | H~M | VH | H | High-resolution structural backend/reference |
| **Applied Category Theory / Operads / Wiring Diagrams** | interface/port, identity, serial/parallel composition, recursive nesting, substitution | Higher-order graph, process algebra | 수학적 law를 너무 강하게 적용하면 View-relative/non-deterministic semantics를 잃을 수 있음. runtime/store/provenance 별도 | L~M | VH | M | Minimal Relation calculus의 reference algebra |
| **Rewriting Logic / Maude** | State transition, event, protocol, branching search, model checking, fairness, cycles | Graph rewrite, state machine | state-space explosion. rewrite theory를 hot-path DB로 사용하는 것은 과도할 수 있음 | M | VH | M | CONTROL/event/cycle executable oracle |
| **Graph Rewriting (DPO/SPO/SqPO)** | local pattern match와 structure replacement; intermediate structural Control | HO graph, Maude, egraphs | match ambiguity, confluence, termination, incremental matching 비용 | M | H | H | Structural CONTROL semantics / adversarial reference |
| **E-Graph / Equality Saturation** | 여러 equivalent candidate를 동시에 유지, rewrite, extraction | Datalog, graph rewriting, candidate search | e-class equality를 ASA universal identity로 오해하면 안 됨. saturation 폭발 | M bounded | H | VH | Alternate Composition search sidecar |
| **egglog** | Datalog fixed point + equality saturation + lattice analysis | Datalog, egraph | scoped/View-relative equivalence를 별도로 감싸야 함 | M | H | VH | AI/algorithm candidate laboratory |
| **Relational Lenses** | View change를 Source change로 반영하는 명시적 bidirectional law | View/Control, IVM | 모든 View에 inverse/write-back이 있다고 가정 금지. Control과 View를 섞을 위험 | M | H | M | Explicit write-back Control adapter only |
| **Provenance / Lineage / Semirings** | derivation trace, dependency, why/how, replay, impact | Datalog, NRC, event log | naïve proof tree는 재귀에서 폭발. provenance와 event history를 동일시하면 안 됨 | H | VH | H | 모든 후보에 공통 spine; circuit/DAG 우선 |
| **Abstract Interpretation** | concrete/abstract representation, sound over-approximation, refinement | View resolution, static analysis | abstraction/concretization이 자동 inverse가 아님. soundness 정의가 domain별로 필요 | M | VH | H | Resolution semantics / loss guard |
| **Demanded Abstract Interpretation** | demand-driven + incremental analysis, cyclic dependency, on-demand query | DBSP, self-adjusting computation | program analysis domain을 그대로 가져올 수는 없음 | H | H | H | Adaptive deepening / lazy intermediate reference |
| **Self-adjusting Computation / Provenance Traces** | execution trace를 이용한 change propagation과 hindsight query | IVM, lineage | trace 저장비용과 external side effects 처리 필요 | H | H | H | Replay/dependency design 참고 |
| **Program Slicing / Dynamic Dependence** | 특정 output에 영향을 준 최소 input/operation 추적 | provenance, impact analysis | slicing precision 비용, dynamic run 편향 | H | H | H | Minimum impact and explanation probe |
| **Concept Bottleneck / Concept Embedding** | 중간 concept variable과 test-time intervention | latent steering | human concept를 bottleneck으로 강제할 수 있고 hidden info leakage 가능 | M | H | VH | Human-readable latent adapter option |
| **DAS / Distributed Interchange Intervention** | distributed subspace를 causal variable과 align하고 양방향 steering | CBM, causal abstraction | alignment map이 너무 자유로우면 vacuous. OOD/generalization 검증 필요 | M | VH | VH | Non-human-readable latent Control reference |
| **SAE / Activation Steering** | sparse feature addressability와 direct steering | DAS, representation engineering | context/model/dictionary별 side effect, collateral spread | M | H | VH | Latent Control adapter + pre-screening metrics |
| **Causal Abstraction / Intervenable Representation** | high/low level model 사이 intervention consistency | DAS, abstraction | unrestricted nonlinear mapping은 아무 모델을 아무 algorithm에 맞출 수 있는 위험 | L~M | VH | VH | Faithfulness guard, not ontology |

---

# II. 연구군별 심층 판정

## 1. Nested Relational Model / NRC

### 가져올 것

- 복합 collection을 하나의 value/interface처럼 다루는 문법
- nested input/output을 가진 View 계산
- result와 operational trace를 함께 산출하는 provenance semantics
- nested query의 recursive incrementalization 가능성

NRC+ IVM 연구는 flat relational query뿐 아니라 nested collection query도 delta query로 변환할 수 있고, recursive IVM이 nested query에도 적용될 수 있음을 보였다. Provenance Traces는 NRC 실행이 ordinary result와 trace를 함께 산출하고, trace가 실제 실행과의 consistency 및 input 변경에 대한 fidelity를 제공할 수 있음을 보였다. [R4-R06][R4-R07]

### 가져오지 않을 것

- `STATE = 반드시 nested physical value`
- nesting level = semantic resolution이라는 단순 동일시
- nested materialization boundary = recompute boundary

### ASA role

```text
REFERENCE REPRESENTATION
STATE:X의 접힌 nested surface를 표현하는 후보
```

---

## 2. Datalog / Soufflé

### 가져올 것

- recursive rule evaluation
- fixed-point semantics
- monotonic/non-monotonic distinction
- dependency and provenance
- declarative View definitions

Soufflé는 semi-naïve Datalog evaluation을 relational algebra machine으로 옮긴 뒤 optimized parallel C++ executable로 compile한다. recursive View의 baseline/oracle로 유용하다. [R4-R03]

### 충돌

- predicate 이름이 World ontology로 승격될 수 있음
- runtime 중 rule 자체가 AI에 의해 자주 생성·변경되는 경우 compilation/cache strategy 필요
- fixed point만으로 oscillating/dynamic pattern을 충분히 표현하지 못할 수 있음

### ASA role

```text
RECURSIVE VIEW EVALUATOR
NOT THE WORLD MODEL ITSELF
```

---

## 3. DBSP / Incremental View Maintenance

DBSP는 database snapshot stream과 transaction delta stream을 integration/differentiation으로 연결하고, incremental query를 `D ∘ Q ∘ I` 형태로 정의한다. 특히 composite computation의 incrementalization에 chain rule을 제공하며 relational query, grouping/aggregation, nested relations, monotonic/non-monotonic recursion을 모델링한다. [R4-R04]

### v2.1 candidate와의 직접 연결

```text
VIEW = composition
ΔVIEW computation
= incremental versions of component Views composed together
```

이는 Owner의 다음 결정과 매우 잘 맞는다.

```text
작은 Relation change
→ actual dependency impact만 계산
→ semantic State는 크게 바뀔 수 있음
```

### 한계

- 모든 delta가 싸지 않다.
- join/state 유지비용이 크다.
- rule/operator change incrementalization은 data delta보다 어려울 수 있다.
- 의미적 View identity와 reconstruction semantics를 제공하지 않는다.

### ASA role

```text
RUNTIME PLANE PRIMARY CANDIDATE
```

---

## 4. Higher-Order Graph / Hypergraph

2025 Higher-Order Graph Databases 연구는 native hypergraphs, node tuples, subgraphs와 lifting/lowering을 unified API로 다루는 prototype을 제안한다. 이는 `Relation 또는 접힌 Composition 자체가 다시 relation participant/interface가 된다`는 요구와 잘 맞는다. [R4-R02]

### 가져올 것

- polyadic source/target interface
- subgraph/tuple를 higher-order subject로 취급
- high-resolution structural topology
- lifting/lowering as implementation analogy for fold/expand

### 경고

- subgraph identity를 View-relative identity와 섞지 않는다.
- 모든 관계를 graph node/edge로 materialize하면 최소계산 목표와 충돌할 수 있다.
- runtime prototype의 benchmark 결과를 ASA domain 성능으로 일반화하지 않는다.

### ASA role

```text
STRUCTURAL REFERENCE / OPTIONAL BACKEND
```

---

## 5. Applied Category Theory / Operads / Wiring Diagrams

Catlab의 directed wiring diagram은 input/output port가 있는 box들로 구성되며, box 자체가 다시 wiring diagram일 수 있어 재귀적으로 nested된다. operadic composition/substitution은 작은 diagram을 큰 diagram 안의 box에 대입한다. [R4-R01]

### 가져올 것

```text
interface compatibility
identity
composition order
serial / parallel / nested topology
outer boundary
folded box as composable unit
```

Owner의 `현재 해상도 Relation = Source→Target`, `합성 결과도 Relation`, `접기/펼치기`에 가장 가까운 formal reference 중 하나다.

### 주의

- category law를 모든 View/Control에 blanket 적용하지 않는다.
- View-relative equivalence, nondeterminism, inference candidate는 richer/enriched semantics가 필요할 수 있다.
- formal syntax와 physical runtime/store는 분리한다.

### ASA role

```text
REFERENCE ALGEBRA / INTERFACE ORACLE
```

---

## 6. Rewriting Logic / Maude

Maude LTLR는 state predicate와 rewrite event를 함께 다루고 fairness를 검증할 수 있다. LTL logical model checker는 folding abstraction으로 potentially infinite reachable state를 finite approximation으로 만들며 fixpoint, bounded verification, real/spurious counterexample 결과를 구분한다. [R4-R08][R4-R09]

### 가져올 것

- CONTROL을 executable state transition으로 시험
- protocol/event의 mixed property
- branch search
- cycle/fairness/budget
- spurious reconstruction/counterexample 구분

### 주의

- 전체 ASA State space를 Maude에 상시 materialize하지 않는다.
- search explosion과 rewrite confluence를 probe한다.

### ASA role

```text
CONTROL / EVENT / CYCLE REFERENCE ORACLE
```

---

## 7. Graph Rewriting

DPO/SPO/SqPO rewriting은 local match와 replacement를 interface-preserving construction으로 표현한다. Computational category-theoretic rewriting은 C-set과 typed graph를 대상으로 pushout complement, pullback complement 기반 rewrite를 구현한다. [R4-R10]

### 가져올 것

- intermediate State 내부의 특정 topology를 target으로 하는 Control
- local rewrite의 precondition/postcondition
- deleted/preserved/created parts의 명시
- concurrency와 critical pair analysis 참고

### ASA role

```text
STRUCTURAL CONTROL SEMANTICS
```

---

## 8. E-Graph / egglog

egglog은 Datalog의 fixed-point incremental execution과 equality saturation의 congruence closure·rewrite·extraction을 결합한다. E-Graphs With Bindings는 hierarchical hypergraph와 DPO rewriting으로 binding을 가진 구조까지 확장한다. [R4-R11][R4-R12]

### 가져올 것

- 여러 composition 후보를 조기 삭제하지 않는 표현
- rewrite search
- cost/metric-based extraction
- AI proposal과 symbolic candidate의 결합

### 강한 Guard

```text
e-class equality
!=
ASA universal relation identity
```

ASA에서는 equality를 다음에 scoped한다.

```text
View
resolution
purpose
scope
operator laws
```

### ASA role

```text
BOUNDED SEARCH PLANE
NOT CANONICAL STATE STORE
```

---

## 9. Relational Lenses

Incremental Relational Lenses는 View update를 Source table의 잠재적으로 작은 change로 전달한다. [R4-R13]

### 가져올 것

- explicit read/write-back pair
- lens law
- small View delta → small Source delta
- ambiguity handling

### 가져오지 않을 것

- 모든 View가 Control inverse를 가진다는 가정
- View에서 보이지 않는 것이 Source에서 삭제됐다는 가정
- branch experiment와 operational write-back의 혼동

### ASA role

```text
EXPLICIT BIDIRECTIONAL CONTROL ADAPTER
```

---

## 10. Provenance / Lineage / Semirings

Datalog semiring provenance 연구는 recursive provenance polynomial을 compact circuit/formula로 표현하는 복잡도를 다룬다. Provenance Traces는 result와 trace의 consistency/fidelity를 정의한다. [R4-R07][R4-R14]

### 가져올 것

```text
why/how derivation
backtrace
forward impact
replay
candidate evidence
incremental invalidation
```

### 설계 판정

```text
NAIVE PROOF TREE = 위험
FACTORIZED DAG / CIRCUIT = 우선 후보
```

Event log는 “무슨 일이 발생했는가”이고 provenance는 “왜 이 State가 성립했는가”이므로 분리한다.

### ASA role

```text
CROSS-CANDIDATE SHARED SPINE
```

---

## 11. Abstract Interpretation / Demanded Analysis

Demanded Abstract Interpretation은 program edit, query, abstract evaluation을 evolving dependency graph에서 함께 다루고, loop/widening으로 생긴 cyclic dependency에서도 demand-driven + incremental computation을 결합한다. [R4-R15]

### 가져올 것

- View-relative abstraction
- on-demand expansion
- adaptive refinement
- cyclic dependency
- batch-equivalent demanded result라는 correctness target

### 주의

- ASA의 high-resolution reconstruction은 abstract interpretation의 concretization과 동일하지 않다.
- soundness의 의미를 View/Probe별로 정의해야 한다.

### ASA role

```text
ADAPTIVE RESOLUTION / DEEPENING REFERENCE
```

---

## 12. Latent Intervention / Intervenable Representation

2026 CDAS 연구는 distributed alignment search와 distributed interchange intervention을 사용해 bi-directional steering을 제안하며, 단순 preference optimization과 다른 distribution matching objective를 사용한다. 동시에 2026 SAE steering side-effect 연구는 같은 feature steering이 context, model, SAE dictionary에 따라 안정성과 collateral spread가 달라짐을 보인다. [R4-R16][R4-R17]

### 가져올 것

- human-readable concept 없이 addressable latent target
- bidirectional steering 후보
- target/off-target measurement
- pre-intervention screening
- model/version-specific Control identity

### 경고

2025 causal abstraction critique는 alignment map을 unrestricted nonlinear function으로 두면 임의 model을 임의 algorithm에 맞출 수 있어 abstraction이 vacuous해질 수 있음을 보인다. [R4-R18]

따라서 ASA latent View/Control은 다음을 함께 시험한다.

```text
intervention accuracy
alignment complexity
stability
collateral effects
OOD generalization
model/version drift
```

### ASA role

```text
LATENT CONTROL ADAPTER
NOT FINAL SEMANTIC ONTOLOGY
```

---

# III. REVISED HYBRID CORE CANDIDATES

## Candidate A — Minimal Relation Interpreter

### 구성

```text
Relation IR
- source interface
- target interface
- identity
- ordered composition refs
- VIEW / CONTROL / STATE discriminator

In-memory executor
- serial/parallel candidate topology
- identity relation
- fold/expand recipe
- basic branch

Append-only trace
- event
- lineage
- replay inputs
```

### 목적

- v2.1 candidate 문법이 특별한 database 없이도 일관되는지 검증
- 다른 engine의 semantic oracle
- FOLD/VIEW/CONTROL 경계 test

### 교체 가능성

가장 높음.

### Scale

낮음. 의도적으로 correctness baseline이다.

### Kill criterion

최소 interpreter조차 View/Control/State를 표현하려면 계속 새로운 primitive를 추가해야 하면 v2.1 candidate kernel을 재검토한다.

---

## Candidate B — Relational Delta Runtime

### 구성

```text
Minimal Relation IR
+ Datalog/Soufflé-style recursive View rules
+ DBSP or differential incremental execution
+ factorized provenance circuit
+ branch/replay store
```

### 강한 capability

```text
recursive closure
relation-level insert/delete/update
minimum necessary recompute
incremental fixed point
lineage
scale
```

### 약점

- high-order topology를 flat tuple/rule로 표현할 때 의미 손실 가능
- structural Control이 우회적으로 표현될 수 있음
- rule/schema vocabulary lock-in

### Test focus

- `-r2 +r5`가 실제 downstream 최소 work로 전파되는가
- deep View composition의 incremental chain rule
- delete/negation/recursive change
- provenance size

---

## Candidate C — Higher-Order Wiring / Rewrite Reference

### 구성

```text
Catlab-style wiring/interface IR
+ higher-order graph representation
+ DPO/SqPO rewrite prototype
+ Maude protocol/cycle model
+ provenance bridge
```

### 강한 capability

```text
recursive nested interface
Relation-on-Relation
structural intermediate addressability
CONTROL topology rewrite
cycles / events / fairness
```

### 약점

```text
matching cost
state-space explosion
subgraph identity
runtime operational complexity
```

### Test focus

- Candidate B가 flattening으로 잃은 structure가 있는가
- FOLD outer interface가 내부 substitution과 일치하는가
- structural Control을 local rewrite로 표현할 수 있는가

---

## Candidate D — Split Runtime / Reference / Search Envelope

### 구성

```text
                         ASA Protocol Contract
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
      Delta Runtime        Structural Reference      Candidate Search
      DBSP/Datalog         Wiring/HO Graph/Maude     egglog/AI
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                         Provenance / Replay
                                  ▼
                         Latent Control Adapter
```

### 권고 이유

이 후보는 기술을 많이 쓰자는 production architecture가 아니다.

> **동일한 Relation/View/Control/State contract를 서로 다른 formalism에 넣고 어디서 의미가 달라지는지 비교하는 연구 envelope**다.

### 가장 큰 정보이득

- runtime simplicity와 structural fidelity를 직접 비교
- egraph equality가 View-relative equivalence와 어디서 충돌하는지 확인
- high-resolution reconstruction을 symbolic/AI/structural candidate로 교차검증
- latent Control을 동일 measurement/replay envelope에 연결

### 현재 Pro-mode probe 권고

```text
Proposed probe order if separately authorized:
A → B → C shadow reference → D envelope
```

A 없이 B/C/D부터 만들면 semantic baseline을 잃을 가능성이 있다.

---

# IV. COMMON PROBE / TEST PLAN

## P01 — Basic Directional Relation

```text
A → B
```

검증:

- direction
- source/target roles
- stable identity
- same endpoint different relation
- identity relation

## P02 — Recursive Composition

```text
A → B → C → D
```

검증:

- order
- interface continuity
- result relation reuse
- nested Composition

## P03 — FOLD / EXPAND

```text
A → B → C → D
FOLD → A → D
EXPAND → candidate paths
```

검증:

- meaning-preserving witness
- exact/inferred/unknown
- multiple candidates

## P04 — VIEW / CONTROL Separation

```text
STATE:A --VIEW:X→ STATE:X
STATE:A --CONTROL:Y→ STATE:A'
```

검증:

- read/configuration vs intentional change
- observation back-action
- branch preservation

## P05 — Promotable Intermediate

중간 B를 저장하지 않은 상태에서 요청한다.

검증:

- reconstruction latency
- addressability
- Control target
- replay

## P06 — Alternate Composition

```text
A→B→D
A→C→D
```

검증:

- separate identity
- low-resolution equivalence
- no permanent merge
- candidate comparison

## P07 — Relation-level Delta

```text
-r2
+r5
```

검증:

- impact graph
- touched work
- full recompute equivalence
- adaptive fallback

## P08 — Small Change / Global State Shift

작은 condition/relation 하나가 전체 View State를 크게 변화시키는 fixture.

검증:

- semantic shift detection
- compute amplification
- new View candidate genesis

## P09 — Protocol + Event

out-of-order event, invalid transition, late correction.

검증:

- event/state separation
- replay
- fairness
- temporal lineage

## P10 — Cycle / Pattern

stable, periodic, chaotic-like/diverging, budget stop fixtures.

검증:

- stop policy
- Pattern State
- nested composition
- Control effects

## P11 — View Resolution

LOW/HIGH structural, temporal, semantic views.

검증:

- distinction preservation
- information loss
- reconstruction coverage
- view-relative disagreement

## P12 — Inferred Composition Reuse

INFERRED intermediate를 다음 Composition에 사용.

검증:

- uncertainty lineage
- automatic deepening
- candidate explosion

## P13 — Scoped Control

same Control under one View, multiple Views, branch, operational scope.

검증:

- isolation
- actual vs counterfactual
- minimal propagation

## P14 — Control Composition

continuous compatible Controls와 discrete conflicts를 각각 시험.

검증:

- typed composition
- order
- conflict detection
- branch candidates

## P15 — AI Candidate Discovery

AI가 View, Control, reconstruction path를 제안.

검증:

- formal validity
- evidence grounding
- novelty/diversity
- candidate yield
- promotion gate

## P16 — Latent Control

model/layer/subspace/SAE feature intervention.

검증:

- target effect
- collateral spread
- stability
- model drift
- replay

## P17 — Lineage / Provenance

동일 State에 여러 paths가 도달.

검증:

- path separation
- compact circuit
- backtrace
- forward impact

## P18 — Privacy Deletion

Evidence 삭제 후 derived State/branches/replay.

검증:

- invalidation
- recomputation
- tombstone audit
- non-recoverability

## P19 — Backend Swap

Candidate A/B/C에서 동일 fixture를 실행.

검증:

- semantic interchange
- View-relative equivalence
- trace comparison
- migration cost

## P20 — Scale

```text
relation count
composition depth
branch count
update rate
cycle size
provenance size
AI candidate rate
```

검증:

- p50/p95 latency
- memory/storage
- update amplification
- replay/recovery time
- candidate pruning loss

---

# V. METRIC MATRIX

| Metric | 정의 | 필요한 Probe |
|---|---|---|
| Controllability | target change 대비 off-target change | P04, P13, P14, P16 |
| Measurability | 전후 효과를 안정적으로 수치화/trace하는 능력 | 전 Probe |
| Repeatability | 동일 envelope에서 semantic behavior 재생 | P05, P09, P15, P16, P17 |
| Intermediate Observability | 생략된 중간을 address/measure하는 범위와 비용 | P03, P05, P12 |
| Reconstruction Precision | 복원 후보가 evidence/actual trace와 맞는 정도 | P03, P12 |
| Reconstruction Coverage | 필요한 내부 path 중 복원 가능한 범위 | P03, P11 |
| Update Amplification | input delta 대비 touched computation | P07, P08, P20 |
| View Equivalence Error | low View에서 합쳤으나 high View에서 잘못 합친 비율 | P06, P11, P19 |
| Provenance Coverage | output derivation을 끝까지 추적 가능한 비율 | P17 |
| Branch Cost | candidate 하나 추가 시 추가 compute/storage | P13, P15, P20 |
| Candidate Yield | AI proposal 중 valid/measurable/improving 비율 | P15 |
| Candidate Diversity Loss | pruning으로 다른 path를 잃은 정도 | P03, P15 |
| Latent Collateral Spread | target 밖 representation/behavior 변화 | P16 |
| Promotion Safety | promotion 후 regression/incident rate | P15, P16 |
| Backend Replaceability | 같은 contract를 다른 engine이 보존하는 정도 | P19 |

---

# VI. RECOMMENDED RESEARCH SEQUENCE

```text
STEP 1
Minimal Relation Interpreter와 fixture 정의

STEP 2
FOLD / VIEW / CONTROL / STATE semantic tests

STEP 3
Compact provenance + replay spine

STEP 4
Datalog/DBSP runtime으로 minimum recompute probe

STEP 5
Wiring/HO graph reference로 structural fidelity 비교

STEP 6
Maude/graph rewrite로 cycle, event, Control reference

STEP 7
egglog/AI를 bounded alternate candidate search에 연결

STEP 8
Latent Control adapter와 off-target measurement 연결

STEP 9
Backend interchange and scale tests

STEP 10
ASA INIT Gate threshold를 baseline distribution에서 설정
```

절대 threshold를 외부 benchmark만 보고 먼저 고정하지 않는다.

---

# VII. RESEARCH CONCLUSIONS

## 1. 현재 가장 강한 기술적 결론

- `VIEW/CONTROL/STATE`는 하나의 database type family가 아니라 protocol surface role로 두는 편이 안전하다.
- Category/operad/wiring은 composition reference에 강하지만 runtime 정답이 아니다.
- DBSP는 minimum recompute에 가장 강한 후보 중 하나지만 World Model을 정의하지 않는다.
- Higher-order graph는 high-resolution topology를 잘 표현하지만 모든 State를 물리 graph로 만들 이유는 없다.
- Maude/rewriting은 Control·event·cycle을 시험하는 oracle로 강하다.
- E-graph/egglog은 alternate candidate search에 강하지만 equality를 scope해야 한다.
- lenses는 explicit write-back에만 사용해야 View와 Control을 혼동하지 않는다.
- provenance는 모든 후보의 공통 spine이다.
- demanded/incremental analysis는 “평소 접고 필요할 때 깊게 본다”는 Owner 결정에 가장 직접적인 계산 연구 근거 중 하나다.
- latent intervention은 human readability 없이도 가능하지만 off-target measurement와 model-version identity가 필수다.

## 2. 현 시점 권고

```text
DO NOT SELECT ONE TECHNOLOGY

SELECT:
- one shared protocol
- one minimal oracle
- one delta runtime candidate
- one structural counter-model
- one bounded search sidecar
```

## 3. 현재 Pro-mode 비교 envelope 권고

```text
Candidate D Split Envelope
```

단, 별도 구현 승인이 있을 경우 첫 probe는 Candidate A에서 시작하는
순서를 권고한다. 이 문서는 구현을 승인하지 않는다.

---

# VIII. SOURCES — R4 LOCAL NAMESPACE

접근일 2026-08-25. 2026 preprint는 emerging research로만 사용한다.

- **[R4-R01] Catlab.jl — Wiring Diagrams.** Recursive nested diagrams, ports, operadic composition. https://algebraicjulia.github.io/Catlab.jl/latest/apis/wiring_diagrams/
- **[R4-R02] Besta et al. Higher-Order Graph Databases. 2025.** https://arxiv.org/abs/2506.19661
- **[R4-R03] Soufflé — Synthesis.** https://souffle-lang.github.io/translate
- **[R4-R04] Budiu et al. DBSP: Automatic Incremental View Maintenance for Rich Query Languages.** https://arxiv.org/abs/2203.16684
- **[R4-R05] Feldera/DBSP publications.** https://docs.feldera.com/literature/papers/
- **[R4-R06] Koch, Lupei, Tannen. Incremental View Maintenance For Collection Programming.** https://arxiv.org/abs/1412.4320
- **[R4-R07] Cheney, Acar, Ahmed. Provenance Traces.** https://arxiv.org/abs/0812.0564
- **[R4-R08] Maude LTLR Model Checker.** https://maude.cs.illinois.edu/tools/tlr/
- **[R4-R09] Maude LTL Logical Model Checker / folding abstraction.** https://maude.cs.illinois.edu/tools/lmc/
- **[R4-R10] Brown et al. Computational category-theoretic rewriting.** https://arxiv.org/abs/2111.03784
- **[R4-R11] Zhang et al. Better Together: Unifying Datalog and Equality Saturation.** https://arxiv.org/abs/2304.04332
- **[R4-R12] Tiurin, Ghica, Hu. E-Graphs With Bindings. 2025.** https://arxiv.org/abs/2505.00807
- **[R4-R13] Horn, Perera, Cheney. Incremental Relational Lenses.** https://arxiv.org/abs/1807.01948
- **[R4-R14] Fan, Koutris, Roy. Circuits and Formulas for Datalog over Semirings. PODS 2025.** https://arxiv.org/abs/2504.08914
- **[R4-R15] Stein, Chang, Sridharan. Demanded Abstract Interpretation.** https://arxiv.org/abs/2104.01270
- **[R4-R16] Bao et al. Faithful Bi-Directional Model Steering via Distribution Matching and Distributed Interchange Interventions. 2026 preprint.** https://arxiv.org/abs/2602.05234
- **[R4-R17] Duan. Pre-Intervention Prediction of Sparse Autoencoder Steering Side Effects. 2026 preprint.** https://arxiv.org/abs/2606.08365
- **[R4-R18] Sutter et al. The Non-Linear Representation Dilemma. 2025.** https://arxiv.org/abs/2507.08802
- **[R4-R19] Olteanu. Recent Increments in Incremental View Maintenance. PODS 2024.** https://arxiv.org/abs/2404.17679
- **[R4-R20] Chmielewski et al. The Role of Semirings in Incremental View Maintenance. 2026 preprint.** https://arxiv.org/abs/2606.07795
- **[R4-R21] AlgebraicDynamics.jl — compositional hierarchical dynamical systems.** https://algebraicjulia.github.io/AlgebraicDynamics.jl/
