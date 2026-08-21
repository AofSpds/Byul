# 05. Simulation, Benchmark & Committee Scenario Outsourcing

## Why Simulation Is Required

Owner requirement:

> 모델 라이프싸이클 검증 시뮬레이션 확보 필요.

또한 후보 모델의 변환 비용·보존성·장기 열화를 느낌이 아니라 실제 계측으로 비교해야 한다.

## Initial Micro-benchmark Scenarios

- `T1` Sequence: `A→B→C→D`
- `T2` Diamond / concurrency
- `T3` Exclusive branch / conflict
- `T4` Repeated pattern / cycle: `A↔B`
- `T5` Resource contention: 하나의 resource를 두 transition이 경쟁
- `T6` Large fan-out / fan-in: relation/state explosion
- `T7` Nested cycle + concurrency
- `T8` Reconfiguration: transition/node/rule add/delete
- `T9` Open composition: Open Net A + Open Net B
- `T10` Local mutation: invalidation radius 측정

규모 후보: 10 / 100 / 1,000 / 10,000 events or states, 실행 가능 범위에서 확대.

## Transformation Probes

- Petri → LTS → synthesized Petri′
- Petri → Occurrence Net → Event Structure → Causal Index
- Petri → Reconfigurable Petri mutation sequence
- Open Petri A + B composition → resulting behaviour/history

## Metrics

### Semantic / Preservation
- P-series Preservation
- Trace Preservation
- Causality Preservation
- Concurrency Preservation
- Conflict Preservation
- Resource Preservation
- Mutation History Preservation
- Round-trip Semantic Delta
- Cumulative Semantic Drift

### Compute / Scale
- Representation Size
- Size Blow-up Ratio
- Conversion Runtime
- Peak Memory
- Query Latency
- Query Gain vs source representation

### Maintenance / Lifecycle
- Invalidation Radius
- Incremental Recompute Cost
- Reverse Synthesis Success
- Rollback / Recovery Cost
- Successor migration cost

## Committee Scenario Outsourcing

Owner asked whether multiple simulation scenarios can be commissioned to a committee. Current answer: yes, and it is preferable for confirmation-bias control.

위원회에는 `좋은 모델을 제안하라`보다 **현재 후보와 routing assumptions를 깨뜨릴 상황을 공모**시키는 방향이 좋다.

### Scenario Challenge Axes
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

### Suggested Committee Groups

1. `Blind Generation Group`
   - P-series/연구목표만 제공.
   - 후보 formalism을 가능하면 숨김.
   - 특정 모델에 유리하지 않은 현실적 stress scenario 생성.

2. `Model Attack Group`
   - 후보 formalism과 current assumptions를 공개.
   - 각 모델/변환/routing을 깨뜨리는 adversarial scenario 생성.

3. `Coverage Gap Group`
   - 앞선 scenario corpus를 검토.
   - 빠진 lifecycle/semantics/scale 영역 탐지.

## Scenario Lifecycle

Scenario 자체도 successor revision으로 진화 가능.

예:
- v1: cycle + resource contention
- v2: network partition 추가
- v3: runtime rule mutation 추가

시나리오 변화가 기존 benchmark result를 무효화하는 경우 exact target을 분리한다.

## What the Benchmark Should Produce

단순한 모델 점수표보다 다음 데이터를 생성해야 한다.

`Situation Fingerprint + Current Model State + Lifecycle Context → candidate fitness / preservation / conversion cost / semantic loss / maintenance cost / query performance → actual routing outcome`

이 데이터가 향후 `R(S,M,L)` 후보의 검증 데이터가 된다.

## Next Job Candidate

위원회 시나리오 외주를 위한 `Lifecycle + Routing Simulation Challenge Requirements` 작성이 다음 주요 작업 후보다.

작성시각: 2026-08-22 02:37 KST
