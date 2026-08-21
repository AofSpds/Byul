# Byul v0.1 Model Contract

## 0. Status

`EXPERIMENTAL / NON_NORMATIVE / NOT_VALIDATED`

이 문서는 v0.1 executable slice가 무엇을 데이터로 보고 무엇을 파생 view로 보는지 고정하는 **implementation contract**다. AAA canonical Requirement/Design/P-series를 대체하지 않는다.

## 1. DATA

Primary DATA는 다음 경로의 Markdown memory corpus다.

`versions/v0.01/memory/*.md`

원문 문서와 각 non-empty line을 provenance와 함께 `MemoryDocument / MemoryAtom`으로 읽는다.

### Ground properties

- source path
- line number
- section heading
- syntactic kind: heading / bullet / numbered / quote / text / code
- exact text
- explicit marker tags only

v0.1은 자유로운 LLM 추론으로 원문을 FACT/HYPOTHESIS로 재분류하지 않는다. 태그는 `OPEN`, `WORKING_HYPOTHESIS`, `NON_NORMATIVE`, `NOT_VALIDATED`, `P-series`처럼 원문에 명시적으로 존재하는 marker 중심으로만 생성한다.

## 2. Derived Representations

### RAW_CORPUS
가장 높은 provenance authority를 갖는 v0.01 memory source representation.

### HISTORY_ORDER_INDEX
`08_CHANNEL_CHRONOLOGY.md`의 numbered chronology를 순서 index로 전개한다.

이 index는 chronology 문서가 명시한 연구진행 순서를 나타내며, 모든 메모 문장의 물리적/논리적 causality를 추론하지 않는다.

### CURRENT_STATE_VIEW
현행/current/strongest 방향을 찾기 위한 검색 view. Raw source를 대체하지 않는다.

### OPEN_QUESTION_VIEW
OPEN / 미결 / non-conclusion 관련 source를 빠르게 찾기 위한 view.

### MODEL_FAMILY_VIEW
Petri/Event/Causal/LTS 및 routing 후보가 집중된 문서 집합 view.

### LIFECYCLE_VIEW
routing, simulation, MI initialization, version/lifecycle 관련 문서 집합 view.

## 3. R(S,M,L)

### S — Situation Fingerprint
v0.1 최소 입력:

- intent
- preservation demand
- exact metric requirement
- unknown fields

모델 이름 자체를 situation input으로 요구하지 않는다.

### M — Current Model State

- source baseline commit
- corpus digest
- document/atom count
- available derived views

### L — Lifecycle Context

초기 phase vocabulary:

- initialize
- operate
- mutate
- compose
- split
- merge
- migrate
- degraded
- recover
- successor
- retire

### Output

`RoutePlan`

- target views
- required validation checks
- P-series gate state
- notes / unresolved conditions

## 4. P-series Gate

v0.1 repository 안에 P-series exact canonical rule set이 제공되어 있지 않다.

따라서 구현은:

- P-series 내용을 추정/발명하지 않는다.
- `EXTERNAL_NOT_LOADED` 상태를 명시한다.
- P-series 검증이 필요한 semantic mutation/execution 판단을 자체 PASS하지 않는다.
- 향후 canonical adapter를 끼울 interface만 남긴다.

## 5. Reconstruction / Preservation Classes

현재 연구 vocabulary를 구현에서 다음처럼 보존한다.

- EXACT
- ANCHORED
- SEMANTIC
- STATISTICAL
- VIEW_DEPENDENT
- NON_RECOVERABLE
- UNKNOWN

v0.1은 raw memo round-trip에 대해서만 deterministic content preservation을 직접 시험한다. 자연어 의미의 완전한 semantic equivalence 판정을 주장하지 않는다.

## 6. Mutation Simulation

v0.1은 source file을 실제 수정하지 않고 virtual mutation을 만들어 다음을 계측한다.

- content digest change
- affected derived views
- invalidation radius
- recovery by discarding virtual mutation

이 단계는 model lifecycle simulation의 최소 seed다.

## 7. v0.1 Acceptance — Experimental Only

초기 micro-test 통과 조건 후보:

1. v0.01 memory 문서를 모두 load한다.
2. raw export/import 후 content digest가 동일하다.
3. chronology index가 cycle 없이 유지된다.
4. unknown routing intent는 임의 model commitment 대신 REVIEW_REQUIRED를 반환한다.
5. P-series canonical rules가 없으면 PASS를 생성하지 않는다.
6. mutation simulation이 영향을 받는 derived view와 invalidation radius를 계산한다.

통과해도 scientific/model validation PASS가 아니다.

작성시각: 2026-08-22 02:58 KST
