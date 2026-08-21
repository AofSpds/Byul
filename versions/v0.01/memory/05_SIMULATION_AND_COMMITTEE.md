# 05. Simulation, Benchmark & Committee Scenario Outsourcing

COPIED_FROM: `versions/v0.00/memory/05_SIMULATION_AND_COMMITTEE.md`

## Required Simulation Direction
Owner requirement: model lifecycle validation simulation과 transformation cost 실측 필요.

## Initial Scenarios
- T1 sequence
- T2 diamond/concurrency
- T3 exclusive branch/conflict
- T4 repeated cycle
- T5 resource contention
- T6 fan-out/fan-in explosion
- T7 nested cycle+concurrency
- T8 reconfiguration
- T9 Open Net composition
- T10 local mutation/invalidation radius

## Transformation Probes
- Petri → LTS → synthesized Petri′
- Petri → Occurrence → Event Structure → Causal Index
- Petri → Reconfigurable Petri mutation sequence
- Open Petri composition

## Metrics
Semantic: P-series/trace/causality/concurrency/conflict/resource/mutation-history preservation, round-trip delta, cumulative drift.

Compute: size, blow-up ratio, conversion runtime, peak memory, query latency/gain.

Maintenance: invalidation radius, incremental recompute, reverse synthesis, rollback/recovery, successor migration.

## Committee Scenario Outsourcing
위원회에는 좋은 모델이 아니라 **모델과 routing assumptions를 깨뜨릴 상황**을 공모시키는 방향이 강함.

Scenario axes:
- Representation Stress
- Mutation Stress
- Lifecycle Stress
- Scale Stress
- Reconstruction Stress
- Interoperability Stress
- Mixed Semantics
- Adversarial Stress
- Unknown-Unknown
- Realistic Domain

Committee groups:
1. Blind Generation
2. Model Attack
3. Coverage Gap

## Scenario Lifecycle
Scenario도 v1→v2→v3로 mutation 가능. material change 시 exact target 분리.

## Benchmark Output
`S + M + L → candidate fitness/preservation/conversion cost/semantic loss/maintenance/query performance → routing outcome`

이 데이터가 `R(S,M,L)`의 검증자료 후보.

## Next Job
`Lifecycle + Routing Simulation Challenge Requirements`를 위원회 외주용으로 정리하는 것이 다음 주요 잡 후보.

작성시각: 2026-08-22 02:37 KST
