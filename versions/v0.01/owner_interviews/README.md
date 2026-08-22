# Byul Owner Interviews — High-Resolution Primary Evidence

PROJECT = AAA
PRODUCT = ASSET AGENT ASA
TRACK = BYUL / AAA-ASA-ME
ARCHIVE_CLASS = OWNER_PRIMARY_INTERVIEW_RECORD
STATUS = NON_NORMATIVE / NOT_VALIDATED / PRIMARY_RESEARCH_EVIDENCE

## Purpose

이 디렉터리는 일반 `memory/`, `context/`, `experiments/`와 분리된 **Owner 주요 인터뷰 1차 기록 전용 공간**이다.

Owner directive (2026-08-23 KST):

> "이 채널 대화록은 대단히 중요한 대화록입니다. 다른 채널의 대화록과 같은 취급하지 마시고 추상화 최대한 배제하고 높은 해상도로 오너와의 주요 인터뷰 기록으로 따로 BYUL에 기록해두세요. 폴더 구분법 다 따로 따게 됩니다."

따라서 이 폴더의 기록은 아래 규칙을 따른다.

## Preservation Rules

1. **Owner wording first**
   - 가능한 경우 Owner의 실제 발화를 철자·말투·망설임·수정·반복까지 보존한다.
   - 읽기 좋게 만들기 위해 의미를 정리하거나 매끈하게 고치지 않는다.

2. **Minimal abstraction**
   - 일반 연구 메모처럼 핵심만 요약하지 않는다.
   - hypothesis가 형성되기 전의 의문, 되돌림, 자기수정, 반례 제기, "아직 모르겠다"는 상태를 보존한다.

3. **Chronology matters**
   - 후대의 정리된 결론으로 과거 발화를 덮어쓰지 않는다.
   - 발화 당시의 질문과 직전 맥락을 가능한 한 함께 둔다.

4. **Raw evidence != derived interpretation**
   - `OWNER_RAW`와 `ASA_CONTEXT / INTERPRETATION`을 명시적으로 분리한다.
   - 후속 summary/spec/core-principle은 이 원문을 참조할 수 있으나 원문을 대체하지 않는다.

5. **Do not merge into generic chat memory**
   - 이 폴더는 일반 채널 요약/승계 메모와 동일 취급하지 않는다.
   - `memory/`의 구조화 문서는 derived view이며, 충돌 또는 의미 미세차이 확인 시 이 인터뷰 기록을 먼저 대조한다.

6. **No false verbatim reconstruction**
   - 실제 live transcript에서 현재 접근 가능한 Owner turn은 `VERBATIM_OWNER_TURN`으로 보존한다.
   - 과거 raw transcript가 직접 보이지 않고 Git memo/context만 남은 경우 `RECOVERED_CONTEXT_NOT_VERBATIM`으로 표시한다.
   - 모델이 빈 구간을 자연스럽게 재구성하여 "원문"처럼 쓰는 것을 금지한다.

7. **Authority boundary**
   - Owner interview evidence는 Owner worldview/intent 연구의 중요한 1차 증거이나, 그 자체가 AAA Requirement, Design Contract, Shared Contract, Freeze, Release, Validation PASS를 만들지 않는다.

## Current Interview Sets

### 2026-08-21 ~ 2026-08-22 — World Model / Mapping / Time / Causal Set

Path:

`2026-08-21_22_world_model_causal_set/`

Files:

- `00_INDEX_AND_PROVENANCE.md` — 출처·범위·보존 상태
- `01_OWNER_TURNS_VERBATIM.md` — 현재 live transcript에서 직접 보존 가능한 Owner 발화 원문
- `02_INTERVIEW_EXCHANGE_HIGH_RESOLUTION.md` — 질문→Owner 응답→즉시 해석/열린 문제를 고해상도로 연결
- `03_GIT_SOURCE_LINEAGE.md` — AAA 기존 research memo/commit lineage와 연결

## Use Rule

Owner worldview fidelity, primitive 선택, time/causality, mapping/interactions, Persona lifecycle의 의미가 쟁점이 될 경우:

1. 먼저 이 `owner_interviews` 원문을 확인한다.
2. 그 다음 `memory/`의 구조화된 current view를 확인한다.
3. 둘이 다르면 자동 합성하지 않고 `INTERPRETATION_REVIEW_REQUIRED`로 남긴다.

작성시각: 2026-08-23 00:19 KST
