# v0.1 Data Source Manifest

## Primary Corpus

- SOURCE_KIND: `BYUL_RESEARCH_MEMORY`
- SOURCE_PATH: `versions/v0.01/memory/*.md`
- SOURCE_BASELINE_COMMIT: `2a4529b69bc237125a1f012835d7a9b78ce3fec9`
- SOURCE_STATE: `RESEARCH_MEMORY / NON_NORMATIVE / NOT_VALIDATED`
- COPY_POLICY: `READ_FROM_PREDECESSOR / DO_NOT_DUPLICATE_AS_SECOND_SEMANTIC_SOURCE`

이 baseline은 `11_CORE_PRINCIPLES.md`가 추가된 시점을 exact source target으로 사용한다.

## Included memory roles

- channel/method
- Owner worldview
- Core Principles
- Causal Set learning
- model family/complementarity
- situation routing/model lifecycle
- simulation/committee design
- MI-1 initialization target
- open questions/next jobs
- chronology
- version policy
- active channel log

## Data Authority Rule

v0.1에서 파생되는 index/view/router output은 source memory보다 높은 authority를 갖지 않는다.

```text
v0.01 raw memory
    > derived index/view
    > routing recommendation
    > reconstruction/summary
```

위 `>`는 truth-value 우열이 아니라 **provenance authority 우선순위**를 뜻한다.

## Core Principles Rule

`11_CORE_PRINCIPLES.md`는 Byul model/routing/mutation의 상위 해석·설계 원칙을 제공한다.

- 특정 formalism을 강제하지 않는다.
- 원칙 개수는 고정하지 않는다.
- 자동 scientific PASS를 생성하지 않는다.
- v0.1은 `CORE_PRINCIPLES_VIEW`와 review requirement만 제공한다.

## Future Data Mutation

v0.01 source baseline을 material하게 바꾸어 새 실험을 할 경우:

- 기존 baseline을 덮어쓰지 않는다.
- successor source commit 또는 successor memory version을 exact target으로 기록한다.
- v0.1 결과와 successor 결과를 같은 data target으로 혼합하지 않는다.

작성시각: 2026-08-22 03:08 KST
