# Byul v0.1 — C0 Memo-Driven Experimental Baseline

> `C0_EXPERIMENTAL_BASELINE / NOT_BYUL_DEFINITION / NOT_SELECTED`
>
> 이 디렉터리는 하나의 실험 구현을 기록합니다. Byul의 최종 identity, canonical World Model, 필수 plane, planner API 또는 선택된 architecture를 정의하지 않습니다.

## Identity

- PROJECT: `AAA`
- PRODUCT: `ASSET AGENT ASA`
- ORIGIN_CHANNEL: `AAA-ASA-ME`
- VERSION: `v0.1`
- PREDECESSOR_RESEARCH: `versions/v0.01/`
- SOURCE_BASELINE_COMMIT: `2a4529b69bc237125a1f012835d7a9b78ce3fec9`
- CANDIDATE_ROLE: `C0_EXPERIMENTAL_BASELINE`
- BYUL_DEFINITION: `FALSE`
- SELECTION_STATE: `NOT_SELECTED`
- STATUS: `EXPERIMENTAL_IMPLEMENTATION / NON_NORMATIVE / NOT_VALIDATED`
- OWNER_ACCEPTANCE: `NOT_PERFORMED`
- INDEPENDENT_VALIDATION: `NOT_PERFORMED`
- PRODUCTION_AUTHORIZED: `FALSE`

## Current Status Locator

- 비규범적 기계 판독 연구상태: `../../BYUL_RESEARCH_STATE.yaml`
- 현재 연구 현황: `../v0.01/CURRENT_STATUS.md`
- 최신 승계 checkpoint: `../v0.01/memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`
- 상세 진행 로그: `../v0.01/memory/10_ACTIVE_CHANNEL_LOG.md`
- 현재 핵심 원칙: `../v0.01/memory/11_CORE_PRINCIPLES.md`
- v0.1 구현 계약: `MODEL_CONTRACT.md`
- v0.1 데이터 기준: `data/SOURCE_MANIFEST.md`

## Critical Data Decision

**이 C0 실험에서 사용하는 DATA는 지금까지 메모한 Byul `v0.01` 연구 메모 자체다.**

외부 toy-world를 primary data로 두지 않는다.

Source corpus:

`versions/v0.01/memory/*.md`

v0.1 C0는 이 메모 corpus를 읽어 현재 연구상태를 보존·색인·라우팅·복원하는 첫 executable slice다. 이 선택은 다른 후보가 따라야 할 ontology가 아니다. 따라서 초기 구현의 성능은 "세계를 얼마나 잘 흉내 내는가"보다 먼저 다음으로 평가한다.

1. 메모 원문과 provenance를 잃지 않는가.
2. 현재 상태 / 역사 / OPEN / 후보모델 / lifecycle / Core Principles view를 재구성할 수 있는가.
3. 당시의 `R(S,M,L)` routing 후보가 C0 입력 구조로 작동하는가.
4. UNKNOWN/미결을 임의의 결론으로 채우지 않는가.
5. mutation 후 어떤 derived view가 무효화되는지 추적할 수 있는가.
6. export/import round-trip에서 원문 content digest가 보존되는가.
7. Core Principles를 특정 formalism의 고정 설계로 오해하거나 자동 PASS 처리하지 않는가.

## Core Principles

현행 원칙은 `../v0.01/memory/11_CORE_PRINCIPLES.md`를 따른다.

현재 포함되는 방향은:

- 변화 가능성
- 비고정 실체성
- 합성·발현성
- 조건·관계 의존성

원칙의 개수는 고정하지 않는다. 특정 formalism을 강제하지도 않는다.

v0.1은 이 원칙을 자연어 의미까지 자동 검증했다고 주장하지 않는다. Router는 필요한 경우 Core Principles view와 검토 항목을 함께 반환하고, 자동 PASS 대신 `REVIEW_REQUIRED` 성격의 gate state를 유지한다.

## C0 Internal Architecture — Non-Canonical

아래 구조는 이 baseline의 관찰 가능한 구현구조일 뿐 Byul의 고정 plane architecture가 아니다.

```text
v0.01 Markdown Memory Corpus
            │
            ▼
      Raw Memory Plane
  exact text + source + line
            │
     ┌──────┼────────────────┐
     ▼      ▼                ▼
 History   Current/Open    Topic/Model
 Index       Views           Views
     │                        │
     └──────────┬─────────────┘
                ▼
          Core Principles View
                │
                ▼
           R(S, M, L)
 Situation / Model State / Lifecycle
                │
                ▼
           Route Plan
 target views + validation requirements
                │
                ▼
        Core Principles Review
```

## What v0.1 deliberately does NOT claim

- Petri Net이 canonical World Model이라는 주장 없음.
- Causal Set이 canonical storage/index라는 주장 없음.
- Event/Mapping이 primitive라는 주장 없음.
- 현재 메모의 해석을 scientific truth로 승격하지 않음.
- Core Principles가 과학적 진리라는 주장 없음.
- derived reconstruction을 raw memory와 동일한 authority로 취급하지 않음.
- `R(S,M,L)`이 canonical planner signature라는 주장 없음.
- ledger가 필연적 core라는 주장 없음.
- 고정 preservation vector 또는 고정 planner API를 선택했다는 주장 없음.
- split/merge 이후 identity policy가 결정되었다는 주장 없음.
- "semantic-preservation framework"가 Byul의 완결된 identity라는 주장 없음.

## Files

- `src/byul_v01.py` — stdlib-only executable model.
- `tests/test_byul_v01.py` — preservation / routing / lifecycle micro-tests.
- `MODEL_CONTRACT.md` — v0.1의 data/representation/routing contract.

## Run

Repository root에서:

```bash
python versions/v0.1/src/byul_v01.py summary
python versions/v0.1/src/byul_v01.py route --intent history --lifecycle initialize
python versions/v0.1/src/byul_v01.py route --intent principles --lifecycle operate
python versions/v0.1/src/byul_v01.py route --intent open_questions --lifecycle operate
python versions/v0.1/src/byul_v01.py simulate-mutation --source 10_ACTIVE_CHANNEL_LOG.md
python versions/v0.1/tests/test_byul_v01.py
```

현재 test suite의 pass는 C0 scaffold 실행 증거일 뿐 byte-exact preservation, semantic equivalence, model validation 또는 Owner Acceptance를 증명하지 않습니다.

## v0.1 C0 Success Criterion

첫 성공은 "좋은 World Model 완성"이 아니다.

> `v0.01 memory → v0.1 representations → route/mutate/export → reconstruction` 과정에서 원본 메모와 중요한 상태구분을 보존하면서, 어떤 view/representation이 어떤 질의에 유리한지 실제 계측 가능한 상태를 만드는 것.

작성시각: 2026-08-22 07:34 KST
