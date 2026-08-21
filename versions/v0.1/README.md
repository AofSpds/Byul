# Byul v0.1 — Memo-Driven Experimental Model

## Identity

- PROJECT: `AAA`
- PRODUCT: `ASSET AGENT ASA`
- ORIGIN_CHANNEL: `AAA-ASA-ME`
- VERSION: `v0.1`
- PREDECESSOR_RESEARCH: `versions/v0.01/`
- SOURCE_BASELINE_COMMIT: `b43c47aea56f39374b9817f6a5bff27dd6a0066d`
- STATUS: `EXPERIMENTAL_IMPLEMENTATION / NON_NORMATIVE / NOT_VALIDATED`
- OWNER_ACCEPTANCE: `NOT_PERFORMED`
- INDEPENDENT_VALIDATION: `NOT_PERFORMED`
- PRODUCTION_AUTHORIZED: `FALSE`

## Critical Data Decision

**v0.1의 DATA는 우리가 지금까지 메모한 Byul `v0.01` 연구 메모 자체다.**

외부 toy-world를 primary data로 두지 않는다.

Source corpus:

`versions/v0.01/memory/*.md`

v0.1은 이 메모 corpus를 읽어 현재 연구상태를 보존·색인·라우팅·복원하는 첫 executable slice다. 따라서 초기 구현의 성능은 "세계를 얼마나 잘 흉내 내는가"보다 먼저 다음으로 평가한다.

1. 메모 원문과 provenance를 잃지 않는가.
2. 현재 상태 / 역사 / OPEN / 후보모델 / lifecycle view를 재구성할 수 있는가.
3. `R(S,M,L)` routing 후보가 실제 입력 구조로 작동하는가.
4. UNKNOWN/미결을 임의의 결론으로 채우지 않는가.
5. mutation 후 어떤 derived view가 무효화되는지 추적할 수 있는가.
6. export/import round-trip에서 원문 content digest가 보존되는가.
7. P-series exact 원문이 없는 상태에서 임의 규칙을 발명하지 않는가.

## Minimal Architecture

```text
v0.01 Markdown Memory Corpus
            │
            ▼
      Raw Memory Plane
  exact text + source + line
            │
     ┌──────┼───────────────┐
     ▼      ▼               ▼
 History   Current/Open   Topic/Model
 Index       Views          Views
     └──────┬───────────────┘
            ▼
       R(S, M, L)
 Situation / Model State / Lifecycle
            │
            ▼
       Route Plan
 target views + validation requirements
            │
            ▼
    External P-series Gate
 canonical rules not bundled here
```

## What v0.1 deliberately does NOT claim

- Petri Net이 canonical World Model이라는 주장 없음.
- Causal Set이 canonical storage/index라는 주장 없음.
- Event/Mapping이 primitive라는 주장 없음.
- 현재 메모의 해석을 scientific truth로 승격하지 않음.
- P-series의 exact semantics를 Byul에서 새로 만들지 않음.
- derived reconstruction을 raw memory와 동일한 authority로 취급하지 않음.

## Files

- `src/byul_v01.py` — stdlib-only executable model.
- `tests/test_byul_v01.py` — preservation / routing / lifecycle micro-tests.
- `MODEL_CONTRACT.md` — v0.1의 data/representation/routing contract.

## Run

Repository root에서:

```bash
python versions/v0.1/src/byul_v01.py summary
python versions/v0.1/src/byul_v01.py route --intent history --lifecycle initialize
python versions/v0.1/src/byul_v01.py route --intent open_questions --lifecycle operate
python versions/v0.1/src/byul_v01.py simulate-mutation --source 10_ACTIVE_CHANNEL_LOG.md
python -m unittest versions/v0.1/tests/test_byul_v01.py
```

## v0.1 Success Criterion

첫 성공은 "좋은 World Model 완성"이 아니다.

> `v0.01 memory → v0.1 representations → route/mutate/export → reconstruction` 과정에서 원본 메모와 중요한 상태구분을 보존하면서, 어떤 view/representation이 어떤 질의에 유리한지 실제 계측 가능한 상태를 만드는 것.

작성시각: 2026-08-22 02:58 KST
