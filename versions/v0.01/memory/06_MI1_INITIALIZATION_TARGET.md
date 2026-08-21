# 06. MI-1 Initialization Target

COPIED_FROM: `versions/v0.00/memory/06_MI1_INITIALIZATION_TARGET.md`

## Owner Decision
MI-1안으로 테스트할 가치가 있음.

## Primary Goal
fresh instance에게 해결책을 먼저 요구하지 않고, 현재 메모만으로 연구상태·Owner 가설·working hypothesis·미결·후보모델 관계를 얼마나 정확히 재구성하는지 평가.

`initial-state reconstruction quality` 자체를 모델 성능축으로 본다.

## Required Initialization Content
1. Owner worldview state
2. P-series와 implementation freedom
3. candidate model map
4. `R(S,M,L)` routing candidate
5. lifecycle/transformation validation targets

## First Response Test
- current research state 재구성
- OWNER_STATED / PRIOR_ART_FACT / WORKING_HYPOTHESIS / OPEN / NON_CONCLUSION 분리
- 후보 formalism 역할/상호보완 관계 재현
- strongest direction 및 금지된 premature conclusion 재현
- memory에 없는 부분을 UNKNOWN/OPEN으로 보존

## Scoring Candidates
- Owner Intent Fidelity
- Hypothesis/Fact Separation
- Non-conclusion Preservation
- Model-family Relation Accuracy
- P-series Authority Discipline
- Open-question Preservation
- Hallucinated Commitment Count
- Missing Critical Context Count

## Stage 2
초기상태 복원이 충분한 이후에만 independent model proposal / critique / routing challenge / scenario design으로 넘어감.

## Exact Target Rule
MI-1 실행 시 `v0.01`의 어느 exact snapshot/commit을 사용했는지 고정해야 함. 실행 이후 material memory change는 successor target으로 처리.

작성시각: 2026-08-22 02:37 KST
