# 04. Situation Routing & Model Lifecycle

COPIED_FROM: `versions/v0.00/memory/04_ROUTING_AND_LIFECYCLE.md`

## P-series
P-series exact content는 canonical source에 있고 Byul은 재정의하지 않는다. 현재 연구적 방향은 특정 formalism을 고정하는 입력값보다 routing/mutation 결과가 통과해야 할 상위 gate로 보는 것.

## Three-argument Routing Candidate
`R(S, M, L) → {Target Model Set, Transformation Path, Preservation Contract, Validation Plan}`

- `S = Situation Fingerprint`: causality, history, behaviour, concurrency, conflict, resource, cycle, state, topology mutation, composition, exact metric, reconstruction tolerance, workload, scale.
- `M = Current Model State`: existing representation, authoritative source, anchors, loss class, size/density, lineage, invalidation state.
- `L = Lifecycle Context`: create/operate/accumulate/adapt/mutate/compose/split/diverge/merge/migrate/degraded/recover/successor-retire.

## Candidate Routing
- causal ancestry → Causal/Event view
- possible behaviour/resource/cycle → Petri
- concurrency/conflict → Event Structure/Petri
- state transition/reachability → LTS
- local composition → Open Petri
- model topology mutation → Reconfigurable Petri
- exact clock/space → separate Metric/Clock representation or anchor

## Lifecycle Validation
- P-series Preservation
- Cumulative Semantic Drift
- Round-trip Semantic Delta
- Mutation History Preservation
- Size Blow-up
- Conversion Runtime
- Peak Memory
- Reverse Synthesis Success
- Invalidation Radius
- Maintenance Cost
- Query Gain / Latency

## Cost Decomposition
- COMPUTE COST
- SEMANTIC COST
- MAINTENANCE COST
- REVERSIBILITY

## Strong Question
`어느 모델이 정답인가?`보다 `이 상황/현재모델/lifecycle에서 P-series를 보존하며 필요한 질의를 가장 싸고 정확하게 처리할 model set과 transformation path는 무엇인가?`

작성시각: 2026-08-22 02:37 KST
