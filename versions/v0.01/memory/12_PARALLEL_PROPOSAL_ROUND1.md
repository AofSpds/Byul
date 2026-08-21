# 12. Parallel Proposal Round-1 Design

## Status

`RESEARCH_DESIGN / NON_NORMATIVE / NOT_VALIDATED`

## Goal

Byul v0.1을 하나의 정답으로 가정하지 않고, 동일한 연구 메모 DATA와 BYUL CORE-A를 여러 독립 인스턴스에게 주어 서로 독립적으로 모델 구조를 제안하게 한다. 현행 구조 유지, 부분 수정, 전면 대체, 복수 모델 조합, 문제정의 반론을 모두 허용한다.

Round-1의 목적은 단순 반복 실행이 아니라 다음을 관찰하는 것이다.

- 독립 인스턴스들이 자연스럽게 어디로 수렴하는가
- 어떤 부분에서 의미 있게 갈라지는가
- 현재 후보군 밖의 prior-art/formalism이 반복 등장하는가
- 상황별로 서로 다른 모델군이 강점을 보이는가
- 현재 R(S,M,L) 또는 Situation Fingerprint 가설이 실제 제안 분산을 설명하는가

## Run Identity

`v0.1-R01`, `v0.1-R02`, ... 형식은 **RUN ID**다.

- MODEL_VERSION = `v0.1`
- RELATION = `INDEPENDENT_PARALLEL_RUN`
- ORDERING = `NONE`
- 각 run은 다른 run의 결과를 보지 않는다.
- run 번호는 우열/세대/후속버전을 의미하지 않는다.

## Common Inputs

모든 run에 공통으로 제공할 것:

1. 동일 exact Byul memory baseline.
2. BYUL CORE-A.
3. 현재 연구목표와 open questions.
4. 현재 후보 formalism은 참고자료일 수 있으나 정답으로 강제하지 않는다.
5. PRIOR-ART-FIRST.
6. UNKNOWN/미결을 임의로 채우지 않는다.

## Cohort Structure

### A. Neutral Blind Cohort

권장 5~7 runs.

동일한 공통 문제만 받고, 특정 해법 방향을 추가로 지시하지 않는다.

목적:
- 자연 수렴 관찰
- 현재 데이터/원칙만으로 어떤 구조가 반복적으로 도출되는지 확인
- 특정 프롬프트 편향 없이 대안의 분산 확인

### B. Alternative Search Cohort

권장 3~5 runs.

공통 문제는 동일하되 대안 탐색 압력만 서로 다르게 준다.

예시 압력:
- 현재 formalism family 밖의 prior-art 탐색
- 현행 v0.1 구조를 최대한 강하게 반박
- 최소 표현/minimal algebra 관점
- composition/open-boundary 중심 관점
- lifecycle/mutation/reversibility 중심 관점
- 현재 routing 가설 자체가 불필요하거나 잘못됐을 가능성 검토

특정 모델명을 답으로 지정하지 않는다.

## Allowed Proposal Classes

각 run은 다음 중 어느 것도 선택할 수 있다.

- KEEP_CURRENT
- MODIFY_CURRENT
- REPLACE_CURRENT
- HYBRID_MULTI_MODEL
- REFRAME_PROBLEM
- INSUFFICIENT_EVIDENCE / UNKNOWN

## Required Return Schema

모든 run은 최소 다음을 반환한다.

- reconstructed current research state
- proposed representation/model architecture
- disposition toward current v0.1
- prior-art basis / references to known formalism families
- what information is preserved exactly
- what information is preserved only semantically/approximately
- what information is lost or non-recoverable
- lifecycle behavior: mutate/compose/split/merge/migrate/recover
- expected failure modes
- implementation/simulation test plan
- unresolved questions / UNKNOWN
- reasons the proposal could be wrong

## Evaluation Design

Round-1에서는 초기부터 복잡한 numeric weight를 고정하지 않는다.

### Fail Gates

다음이 있으면 우선 탈락/재검토 후보:

- memory에 없는 사실을 확정적으로 발명
- BYUL CORE-A를 명백히 위반하면서 설명 없음
- discarded semantics를 자동 복원 가능하다고 주장
- current preferred formalism을 근거 없이 canonical로 고정
- prior-art-first 요구를 무시하고 불필요한 새 이론 발명
- lifecycle/semantic loss 문제를 숨김

### Comparative Review Axes

Owner + ASA가 블라인드 비교한다.

- Owner Intent Fidelity
- BYUL CORE-A alignment
- representation fitness
- semantic preservation
- lifecycle adaptability
- reversibility/reconstruction discipline
- falsifiability/testability
- simplicity vs explanatory power
- prior-art grounding
- uncertainty discipline
- implementation feasibility
- genuinely useful novelty

초기에는 절대점수보다 pairwise comparison / shortlist를 우선한다.

## Blind Review Procedure

1. Proposal authorship/run identity를 숨긴다.
2. Proposal 내용을 공통 schema로 normalize한다.
3. Fail Gate를 먼저 적용한다.
4. Owner + ASA가 pairwise comparison과 qualitative notes를 남긴다.
5. 상위 3~4개와 독특한 minority proposal을 별도 보존한다.
6. 그 후 pressure-test / adversarial review를 수행한다.
7. 필요하면 Round-2 mutation/merge/retest를 연다.

## Important Non-Goal

Round-1에서 단 하나의 winner를 반드시 뽑지 않는다.

가능한 좋은 결과:
- 하나의 강한 공통 구조
- 상황별로 강한 여러 모델군
- routing 필요성에 대한 반례
- 새로운 prior-art 후보
- 현행 문제정의의 수정 필요성

## Link to Future Work

Round-1 결과는 이후 다음 연구자료로 사용 가능하다.

- Transformation Preservation Matrix
- Situation Fingerprint feature importance
- R(S,M,L) validation
- lifecycle simulation scenarios
- committee stress-test design
- MI initialization/reconstruction evaluation

작성시각: 2026-08-22 03:33 KST
