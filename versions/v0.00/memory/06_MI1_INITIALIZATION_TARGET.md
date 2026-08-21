# 06. MI-1 Initialization Target

## Owner Decision

Owner assessment:

> MI - 1안으로 테스트 해볼 가치가 있다.

현재 Byul version policy에 따라 이 초기화 시험은 `v0.0x` 연구단계에서 수행하고, 실제 모델 구현은 `v0.1+`부터 시작한다.

## Primary Goal

첫 fresh instance에게 좋은 해결책을 즉시 요구하지 않는다.

1차 목표는:

> 현재 정리된 메모만 받은 신규 인스턴스가 지금까지 연구상태·Owner 가설·working hypothesis·미결점·후보모델 관계를 얼마나 정확하게 재구성하는가.

이다.

즉 `initial-state reconstruction quality` 자체를 모델 성능축으로 본다.

## Why This Comes First

이 단계를 통과하지 않고 후속 model proposal/위원회 simulation 결과를 보면, 실패 원인이 다음 중 무엇인지 구분하기 어렵다.

- 후보 formalism의 문제
- 초기화/맥락복원의 실패
- 메모 자체의 정보손실
- fresh instance의 임의 보간/추정

## Required Initialization Content

최소 다섯 덩어리:

1. Owner Worldview State
   - `무수한 국소 사상들의 합성망`
   - Object non-primitive 후보
   - succession/계승
   - observation transient state
   - no absolute NOW
   - reciprocity as time-extended causal history 후보

2. P-series / Implementation Freedom
   - P-series exact semantics를 새로 만들지 않음
   - 상위 원칙을 보존하는 범위에서 implementation representation은 열려 있음

3. Candidate Model Map
   - Causal Set / Causal Index
   - Petri / Open Petri / Reconfigurable Petri
   - Occurrence Net / Event Structure
   - LTS / Reachability View
   - 역할·장단점·손실관계

4. Situation Routing Candidate
   - `R(S,M,L)`
   - S/M/L 의미
   - P-series external gate 후보

5. Lifecycle / Transformation Validation
   - preservation
   - reverse synthesis
   - round-trip loss
   - cumulative semantic drift
   - invalidation radius
   - query gain

## First Response Test

신규 인스턴스에게 먼저 요구할 것:

- current research state를 자기 말로 재구성
- `OWNER_STATED / WORKING_HYPOTHESIS / PRIOR_ART_FACT / OPEN / NON_CONCLUSION` 분리
- 후보 formalism의 역할과 상호보완 관계 재현
- strongest current direction과 금지된 premature conclusions 재현
- 기억에 없는 부분을 추정으로 채우지 않고 UNKNOWN/OPEN으로 남김

## Scoring Candidates

- Owner Intent Fidelity
- Hypothesis/Fact Separation
- Non-conclusion Preservation
- Model-family Relation Accuracy
- P-series Authority Discipline
- Open-question Preservation
- Hallucinated Commitment Count
- Missing Critical Context Count

## Second Stage

초기화 재현이 충분히 된 이후에만:

- independent model proposal
- counterproposal
- formalism routing critique
- scenario design
- model lifecycle stress analysis

로 넘어간다.

## v0.00 vs v0.01 Use

- `v0.00`: detailed recovery predecessor / backup.
- `v0.01`: active research memo successor.
- MI-1 실험 target을 고정할 때는 exact snapshot/version을 반드시 명시한다.

작성시각: 2026-08-22 02:37 KST
