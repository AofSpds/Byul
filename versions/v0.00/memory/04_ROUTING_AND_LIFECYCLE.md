# 04. Situation Routing & Model Lifecycle

## P-series Position

Owner clarification:

> P-series에 해당하는 원칙을 벗어나지 않으면 구현은 열려 있다.

현재 해석:

- P-series exact content/numbering은 canonical source에 있으며 Byul이 재정의하지 않는다.
- P-series는 특정 formalism 선택을 지시하는 구현 함수의 입력값보다 **결과가 통과해야 할 상위 gate**로 보는 방향이 강하다.
- P-series를 지키는 범위에서 모델 선택·공존·mutation은 열려 있다.

## Three-argument Routing Candidate

Owner가 `3개의 인자를 가진 함수던 맵이던 가지고 있어야겠다`고 제안.

현재 후보:

`R(S, M, L) → {Target Model Set, Transformation Path, Preservation Contract, Validation Plan}`

### S = Situation Fingerprint
무엇을 표현/질의해야 하는가.

후보 축:
- causality
- actual history
- possible behaviour
- concurrency
- conflict
- resource generation/consumption
- cycle/feedback
- current state
- topology/model mutation
- local composition
- exact metric time/space
- reconstruction tolerance
- query workload
- scale / relation density

### M = Current Model State
현재 어떤 representation/index/anchor/history를 가지고 있는가.

후보 필드:
- existing representations
- authoritative source per information class
- anchors
- loss class
- current size / relation density
- transformation lineage
- invalidation state

### L = Lifecycle Context
현재 모델이 어떤 변화 단계에 있는가.

후보 lifecycle:
`CREATE → OPERATE → ACCUMULATE HISTORY → ADAPT → MUTATE → COMPOSE → SPLIT → DIVERGE → MERGE → MIGRATE → DEGRADED MODE → RECOVER → SUCCESSOR/RETIRE`

## Why S Alone Is Insufficient

같은 질의라도 현재 representation이 무엇인지, 수명주기 어느 단계인지에 따라 최적 경로가 달라진다.

예: causal ancestry 질의가 필요해도 처음 만드는 작은 모델과 1억 event가 쌓인 active model에서 전체 causal index를 새로 만드는 비용은 다르다. migration 중이라면 query speed보다 preservation/rollback이 더 중요할 수 있다.

## Candidate Situation Routing Examples

- causal ancestry / causal dependency → Causal/Event view
- possible behaviour / resource / repeated cycle → Petri
- concurrency + conflict → Event Structure / Petri
- state transition / reachability → LTS view
- local model composition → Open Petri
- topology/model structure mutation → Reconfigurable Petri
- exact clock/space requirement → separate Metric/Clock representation or anchor

## Model Lifecycle Validation

단일 변환 성공보다 장기 lifecycle에서 의미가 누적 열화되는지를 본다.

핵심 지표 후보:

- P-series Preservation at each generation
- Cumulative Semantic Drift
- Round-trip Semantic Delta
- Mutation History Preservation
- Size Blow-up
- Conversion Runtime
- Peak Memory
- Reverse Synthesis Success
- Invalidation Radius
- Maintenance Cost
- Query Gain / Query Latency

중요: 각 단계가 개별 PASS여도 여러 세대 후 semantic drift가 누적될 수 있다.

## Transformation Cost Decomposition

한 숫자로 비용을 표현하면 안 된다.

최소 분리:

1. `COMPUTE COST` — 시간, 메모리, 저장량
2. `SEMANTIC COST` — 무엇을 잃었는가
3. `MAINTENANCE COST` — 원본 mutation 이후 얼마나 재계산/재검증해야 하는가
4. `REVERSIBILITY` — exact/semantic/approximate/non-recoverable

## Strong Current Research Question

> 어느 모델이 세계의 정답인가?

보다:

> 이 상황과 현재 representation/lifecycle에서 P-series를 보존하면서 필요한 질의를 가장 싸고 정확하게 처리할 model set과 transformation path는 무엇인가?

를 우선한다.

작성시각: 2026-08-22 02:37 KST
