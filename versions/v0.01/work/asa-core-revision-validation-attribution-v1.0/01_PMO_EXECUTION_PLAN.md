# PMO — ASA Core 누적 연구 리비전 및 VALIDATING 원인 규명 작업계획서 v1.0

```text
PLAN_ID =
PMO-ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-EXECUTION-PLAN-v1.0

PARENT_PROPOSAL =
00_BYUL_WORK_PROPOSAL.md

PROJECT = AAA / BYUL
PRODUCT = ASSET AGENT ASA
OWNER_DIRECTIVE_DATE_KST = 2026-08-26
EXECUTION_COMMAND = PMO
PLAN_VALIDATOR = BYULV
SEMANTIC_AUTHOR = MODEL
EVIDENCE / TELEMETRY = CONTROL
OUTPUT_VALIDATORS = MODELV / CONTROLV / PMOV

STATUS = OWNER_AUTHORIZED / READY_FOR_S0
TASK_CLASS = STANDARD / BOUNDED DOCUMENT REVISION + DIAGNOSTIC TELEMETRY
DIRECT_MAIN_MUTATION = PROHIBITED
TASK-SPECIFIC BRANCH = REQUIRED
FULL REPOSITORY SCAN = NOT PLANNED
EXTERNAL RESEARCH RESTART = NOT PLANNED
CORRECTION_BATCH = 1 PLANNED
IVA = NOT PLANNED
```

# 0. PMO 시작 명령

PMO는 새 실행 채널에서 Git current bootstrap을 복구한 뒤 아래 lock을 선언한다.

```text
CURRENT_PERSONA_LOCK = PMO

PROGRAM =
ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0

OWNER_AUTHORIZATION =
OWNER_MESSAGE_2026-08-26_PMO_PROCEED_AND_DIAGNOSE_VALIDATING
```

PMO의 첫 substantive 보고는 다음 형식을 사용한다.

```text
[PMO EXECUTION OPEN]

PROGRESS = [░░░░░░░░░░] 0%

TASK_CLASS =
STANDARD / BOUNDED DOCUMENT REVISION + DIAGNOSTIC TELEMETRY

EXPECTED_ACTIVE_WALL_CLOCK =
61~120분 conservative planning range

DISPATCH_BASELINE =
45~90분 (superseded at S0 after dependency arithmetic review)

PARALLEL_BEST_CASE =
53~105분 only if S4 fully overlaps the eligible late-S3 window

TOTAL_OWNER_CHECK =
120분 초과 전망 시 Owner 확인

PRIMARY_INPUTS =
6-document revision packet
(includes ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.0_2026-08-25.md)

PLANNED_GIT_READ =
current bootstrap/pointers
→ exact task proposal/plan
→ exact primary inputs
→ on-demand secondary sections only

PLANNED_WORKERS =
MODEL / CONTROL

PLANNED_VALIDATORS =
BYULV at S0
MODELV / CONTROLV / PMOV at S6 in parallel

NOT_PLANNED =
ENG / ENGV / IVA / repository-wide scan / external research restart

BLOCKER = NONE or exact blocker
SCOPE_EXPANSION = NO
OWNER_ACTION_REQUIRED = NO
```

PMO는 이 opening report 없이 source 범위를 넓히거나 validator를 dispatch하지 않는다.

---

# 1. 실행 목적

본 계획은 동시에 두 결과를 만든다.

## 1.1 Revision 결과

기존 v2.0 패킷을 successor `v2.1 CANDIDATE` 문서군으로 동기화한다.

핵심은 새 이론 발명이 아니라 다음이다.

- Owner-confirmed decision의 정확한 반영
- Pro-mode implication과 Owner decision의 분리
- Open question의 미결 상태 보존
- v2.0 main / decision register / changelog / matrix / question ledger / index 간 용어와 상태 동기화
- v1.0에서 유지하기로 한 governance/safety contract의 보존
- 기술후보를 research component로 유지하고 하나의 정답으로 freeze하지 않음

## 1.2 Latency 진단 결과

PMO는 실제 wall-clock과 작업범위를 계측하여 다음을 판정한다.

```text
A. VALIDATOR 판단 자체가 느린가?
B. validation context 로딩·반복 read·serial routing·재검증이 느린가?
C. source recovery / authoring / correction / tool wait가 느린가?
D. 복합 원인인가?
```

진단은 실제 실행 timeline과 input/read/finding ledger를 기반으로 한다.

---

# 2. Exact input set

## 2.1 Primary packet

```text
P1 ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.0_2026-08-25.md
P2 ASA_CORE_OWNER_CONFIRMED_DECISIONS_2026-08-25.md
P3 ASA_CORE_WORLD_MODEL_v2.0_CHANGELOG_2026-08-25.md
P4 ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_2026-08-25.md
P5 ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_2026-08-25.md
P6 ASA_CORE_REVISION_PACKET_INDEX_2026-08-25.md
```

중복 업로드는 CONTROL이 byte/content identity를 비교해 canonical input 하나로 정한다.

## 2.2 Expected primary facts

CONTROL은 다음 count를 input freeze에서 확인한다.

```text
OWNER DECISIONS / DIRECTIONS = 73
EXPLICIT OPEN REGISTER = 10
PRO-MODE IMPLICATIONS = 7
OWNER INTERVIEW QUESTIONS = 180
EXTERNAL REFERENCES = 21
HYBRID CANDIDATES = 4
COMMON PROBES = 20
```

Count mismatch는 곧바로 오류로 단정하지 않는다.
문서 revision 차이 또는 duplicate/version 차이인지 먼저 확인한다.

## 2.3 Secondary sources

Primary packet으로 해결할 수 없는 exact conflict에만 해당 section을 읽는다.

```text
ASA_CORE_WORLDVIEW_v1.0_2026-08-24.md
ASA_CORE_WORLDVIEW_v1.0_REVISION_REPORT_2026-08-24.md
ASA_CORE_WORLDVIEW_INTEGRATED_v0.1_2026-08-24.md
BYUL_PRO_MODE_RESEARCH_HANDOFF_PACKET_2026-08-24.md
BYUL exact Owner-confirmation records
```

Secondary source를 열 때 CONTROL ledger에 다음을 남긴다.

```text
WHY_REQUIRED
ACCEPTANCE_CRITERION
EXACT_FILE / SECTION
READ_SCOPE
EXPECTED_EXTRA_TIME
```

## 2.4 Missing source

다음 파일은 현재 `NOT_RECOVERED`로 유지한다.

```text
BYUL_CLOSURE_TOOLKIT_CORE_COMBINATION_NEXT_CHANNEL_PACKET_2026-08-24.md
```

발견되지 않은 내용을 추정하여 채우지 않는다.

---

# 3. Branch와 output structure

PMO는 current task registry에 고정된 task-specific isolated branch를 사용한다.

```text
work/asa-core-revision-validation-attribution-20260826
```

권장 output path:

```text
versions/v0.01/work/asa-core-v21-revision/<RUN_ID>/
├─ inputs/
│  ├─ INPUT_MANIFEST.tsv
│  ├─ DUPLICATE_INPUT_REPORT.md
│  └─ SOURCE_PRECEDENCE.md
│
├─ revision/
│  ├─ ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.1_CANDIDATE_2026-08-26.md
│  ├─ ASA_CORE_OWNER_DECISION_CROSSWALK_v2.1_CANDIDATE_2026-08-26.md
│  ├─ ASA_CORE_WORLD_MODEL_v2.1_CANDIDATE_CHANGELOG_2026-08-26.md
│  ├─ ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_v2.1_SYNC_2026-08-26.md
│  ├─ ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_v2.1_SYNC_2026-08-26.md
│  ├─ ASA_CORE_REVISION_PACKET_INDEX_v2.1_CANDIDATE_2026-08-26.md
│  └─ SHA256SUMS.txt
│
├─ telemetry/
│  ├─ PMO_REVISION_EXECUTION_TIMELINE.tsv
│  ├─ PMO_GIT_READ_SCOPE_LEDGER.tsv
│  ├─ VALIDATION_EVENT_AND_FINDING_LEDGER.tsv
│  └─ VALIDATION_LATENCY_ATTRIBUTION_REPORT.md
│
├─ validation/
│  ├─ BYULV_PLAN_VALIDATION_RECEIPT.md
│  ├─ MODELV_SEMANTIC_VALIDATION_RECEIPT.md
│  ├─ CONTROLV_SOURCE_TELEMETRY_VALIDATION_RECEIPT.md
│  └─ PMOV_EXECUTION_ATTRIBUTION_VALIDATION_RECEIPT.md
│
└─ completion/
   └─ PMO_COMPLETION_PACKAGE.md
```

Original packet bytes를 수정하지 않는다.
Successor outputs만 새로 만든다.

---

# 4. Telemetry contract

## 4.1 Timeline schema

`PMO_REVISION_EXECUTION_TIMELINE.tsv` 필드:

```text
EVENT_ID
STAGE_ID
ACTOR
CATEGORY
START_KST
END_KST
ACTIVE_SECONDS
WAIT_SECONDS
OWNER_WAIT_SECONDS
TOOL_WAIT_SECONDS
INPUT_REF_COUNT
FILES_READ_COUNT
LINES_OR_BYTES_READ
GIT_CALL_COUNT
OUTPUT_REF
NOTES
```

## 4.2 Git read ledger schema

`PMO_GIT_READ_SCOPE_LEDGER.tsv` 필드:

```text
READ_ID
STAGE_ID
ACTOR
REPOSITORY
REF
PATH_OR_QUERY
READ_CLASS = POINTER / EXACT_FILE / SECTION / DIFF / DEPENDENCY / HISTORY / TREE / FULL_SCAN
REASON
ACCEPTANCE_CRITERION
FIRST_READ = YES/NO
REPEATED_READ = YES/NO
START_KST
END_KST
RESULT
```

## 4.3 Validation ledger schema

`VALIDATION_EVENT_AND_FINDING_LEDGER.tsv` 필드:

```text
VALIDATION_EVENT_ID
VALIDATOR
TARGET_ID
TARGET_SHA
ACCEPTANCE_CRITERIA
CONTEXT_LOAD_START
CONTEXT_LOAD_END
DIRECT_REVIEW_START
DIRECT_REVIEW_END
FILES_OR_SECTIONS_READ
GIT_CALL_COUNT
FULL_SCAN = YES/NO
REPEATED_WHOLE_TARGET_READ = YES/NO
BLOCKING_FINDINGS
ADVISORY_FINDINGS
NEW_SCOPE_REQUESTED = YES/NO
CORRECTION_TRIGGERED = YES/NO
RECHECK_SCOPE
FINAL_STATE
```

## 4.4 Category rules

각 active interval은 한 개 primary category로 분류한다.

```text
BOOTSTRAP
SOURCE_RECOVERY
SOURCE_READ
CROSSWALK
AUTHORING
SELF_CHECK
VALIDATION_CONTEXT_LOAD
VALIDATION_DIRECT
VALIDATION_FINDING_INTEGRATION
CORRECTION
REVALIDATION
PACKAGING
TOOL_WAIT
OWNER_WAIT
```

분류가 애매하면 `UNCLASSIFIED`로 남기고 최종 evidence-gap 계산에 포함한다.

## 4.5 Clock rules

- Owner 응답 대기는 active work에서 제외
- connector/tool outage wait는 별도 표시
- 병렬 worker/validator active time은 compute sum과 wall-clock을 각각 기록
- elapsed time을 progress percentage로 사용하지 않음
- 내부 token 사용량은 신뢰 가능한 원인 지표로 사용하지 않음

---

# 5. Work breakdown structure

# S0 — Plan admission, BYULV review, telemetry setup

```text
WEIGHT = 5%
EXPECTED_RANGE = 5~10분
OWNER_CHECK_LIMIT = 15분
LEAD = PMO
VALIDATOR = BYULV
```

## S0 actions

PMO:

1. bootstrap current pointer / PMO memory / current task ref 복구
2. parent proposal과 execution plan exact SHA/path 고정
3. task class, planned sources, outputs, workers, validators 확인
4. telemetry files/header 생성
5. stage clock 시작

BYULV:

- Owner 요청과 proposal/plan 일치
- revision이 repository migration이나 재연구로 변질되지 않았는지
- v2.0 non-frozen status 유지
- validation attribution이 VALIDATING을 원인으로 미리 가정하지 않는지
- expected range / Owner-check / progress model 확인

## S0 inputs

- current Git bootstrap/pointers
- `00_BYUL_WORK_PROPOSAL.md`
- `01_PMO_EXECUTION_PLAN.md`
- BYULV active memory

## S0 outputs

```text
BYULV_PLAN_VALIDATION_RECEIPT.md
TELEMETRY_HEADERS_CREATED = YES
TASK_SCOPE_LOCK.md or equivalent PMO trace
```

## S0 exit

```text
PLAN_ACCEPTANCE = PASS or CORRECTION_REQUIRED
SCOPE = LOCKED
TELEMETRY = ACTIVE
```

## S0 anomaly / stop

- BYULV가 새 architecture를 blocking requirement로 추가
- primary input set 확대 요구
- repository-wide scan 요구
- 15분 초과 전망

S0 완료 progress:

```text
PROGRESS = [█░░░░░░░░░] 5%
```

---

# S1 — Exact input freeze and duplicate disposition

```text
WEIGHT = 10%
EXPECTED_RANGE = 5~10분
OWNER_CHECK_LIMIT = 15분
LEAD = CONTROL
PMO INTEGRATION = YES
```

## S1 actions

1. P1..P6 exact filenames/content identity 기록
2. main v2.0 exact source 확보
3. duplicate upload pair 비교
4. canonical input 지정
5. count expectations 확인
6. source precedence 기록
7. missing-source note 고정

## S1 no-go

- 과거 Git 전체 tree scan
- 21 references online 재검색
- 180 questions semantic resolution

## S1 outputs

```text
INPUT_MANIFEST.tsv
DUPLICATE_INPUT_REPORT.md
SOURCE_PRECEDENCE.md
```

## S1 exit

```text
PRIMARY_INPUT_COUNT = 6
MAIN_DOCUMENT_PRESENT = YES
CANONICAL_DUPLICATE_DISPOSITION = COMPLETE
UNKNOWN_REQUIRED_INPUT = 0 except declared missing source
```

누적 progress:

```text
PROGRESS = [██░░░░░░░░] 15%
```

---

# S2 — Owner decision / definition / document crosswalk

```text
WEIGHT = 15%
EXPECTED_RANGE = 8~15분
OWNER_CHECK_LIMIT = 25분
LEADS = CONTROL + MODEL in parallel
```

## CONTROL lane

- OD-001..073 inventory
- OPEN-01..10 inventory
- PI-01..07 inventory
- 각 항목이 main/changelog/matrix/question/index 어디에 반영됐는지 mapping
- missing / duplicated / contradictory mapping 표시

## MODEL lane

- kernel definition map
- terminology guard map
- v1.0 retained-contract map
- external research role map
- Candidate A/B/C/D and Probe P01..P20 consistency map

## Outputs

```text
OWNER_DECISION_CROSSWALK_DRAFT.tsv or markdown table
DEFINITION_CONSISTENCY_MAP.md
REVISION_DELTA_BACKLOG.md
```

`REVISION_DELTA_BACKLOG` finding class:

```text
D1 MATERIAL OWNER-CONFLICT
D2 MATERIAL SEMANTIC INCONSISTENCY
D3 STATUS/AUTHORITY MISCLASSIFICATION
D4 CROSS-DOCUMENT TERMINOLOGY MISMATCH
D5 REFERENCE/INDEX MISMATCH
D6 EDITORIAL DUPLICATION
D7 OPEN / REQUIRES OWNER DECISION
```

## S2 exit

```text
73 Owner items mapped
10 Open items mapped
7 PI items mapped
unmapped material definition = 0 or explicit backlog
```

누적 progress:

```text
PROGRESS = [███░░░░░░░] 30%
```

## S2 Owner-check

- material Owner conflict 발견
- missing source 없이는 해결 불가
- external research 재조사 필요
- 25분 초과 전망

---

# S3 — Main v2.1 candidate authoring

```text
WEIGHT = 25%
EXPECTED_RANGE = 15~25분
OWNER_CHECK_LIMIT = 35분
LEAD = MODEL
PMO = scope/integration control
```

## S3 authoring rules

MODEL은 original v2.0을 successor 문서로 리비전한다.

### Preserve

- v2.0의 한 문장 정의
- minimal Relation + recursive composition
- VIEW / CONTROL / STATE distinction
- FOLD / EXPAND distinction
- View-relative resolution
- EXACT / INFERRED / UNKNOWN
- branch/replay/promotion control
- minimum necessary recompute
- non-finality
- governance plane separation

### Correct / synchronize

- Owner-confirmed status와 proposal status 혼합
- terminology drift
- `Closure`가 object/finality로 읽히는 문장
- Relation Bundle primitive 재등장
- View result와 STATE 혼용
- Intervention causal primitive 오해
- technology candidate가 selected architecture처럼 읽히는 문장
- missing source를 읽은 것처럼 보이는 문장

### Do not invent

- OPEN-01..10 답변
- 180 question answers
- formal operator laws
- database/schema choice
- prototype result
- benchmark result

## S3 output

```text
ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.1_CANDIDATE_2026-08-26.md
```

## S3 exit

- all critical definitions present
- status legend present
- Owner-confirmed / Pro-mode / Open sections distinguishable
- no implementation authorization
- no technology freeze
- source recovery boundary explicit

누적 progress:

```text
PROGRESS = [██████░░░░] 55%
```

---

# S4 — Companion document synchronization

```text
WEIGHT = 15%
EXPECTED_RANGE = 8~15분
OWNER_CHECK_LIMIT = 25분
LEADS = MODEL + CONTROL in parallel
DEPENDENCY = S2 complete; may overlap late S3 after definition lock
```

## S4A Decision crosswalk

CONTROL finalizes:

```text
ASA_CORE_OWNER_DECISION_CROSSWALK_v2.1_CANDIDATE_2026-08-26.md
```

It does not rewrite Owner decisions.
It records:

- ID
- status
- source wording summary
- R1 section
- retained/corrected/open
- notes

## S4B Changelog

MODEL creates:

```text
ASA_CORE_WORLD_MODEL_v2.1_CANDIDATE_CHANGELOG_2026-08-26.md
```

Separate:

```text
v1.0 → v2.0 foundational breaking changes
v2.0 → v2.1 candidate synchronization changes
semantic changes
status/authority corrections
editorial changes
```

## S4C Matrix sync

MODEL updates only affected terms/links/status in:

```text
ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_v2.1_SYNC_2026-08-26.md
```

No broad external research.

## S4D Open questions sync

MODEL/CONTROL jointly produce:

```text
ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_v2.1_SYNC_2026-08-26.md
```

Each original question is:

```text
RETAINED_OPEN
SUPERSEDED_BY_OWNER_DECISION
DUPLICATE_OF_Qxxx
TERMINOLOGY_UPDATE_ONLY
DEFERRED
```

Question content is not answered unless an exact prior Owner decision already answers it.

## S4E Index

PMO assembles:

```text
ASA_CORE_REVISION_PACKET_INDEX_v2.1_CANDIDATE_2026-08-26.md
```

누적 progress:

```text
PROGRESS = [███████░░░] 70%
```

---

# S5 — Candidate freeze and deterministic self-check

```text
WEIGHT = 10%
EXPECTED_RANGE = 5~10분
OWNER_CHECK_LIMIT = 15분
LEAD = PMO + CONTROL
```

## S5 actions

1. R1..R6 file set freeze
2. hash generation
3. headings / IDs / cross-links check
4. count checks
5. forbidden-state scan
6. candidate D0 exact SHA freeze
7. validation target slices 생성

## Deterministic checks

```text
Owner items mapped = 73
Open items preserved/dispositioned = 10
PI items mapped = 7
Questions dispositioned = 180
External references expected = 21 unless documented source correction
Hybrid candidates = 4
Common probes = 20
FINAL / ACTIVE / FROZEN unauthorized promotion = 0
```

Count mismatch is recorded, not silently forced.

## S5 outputs

```text
SHA256SUMS.txt
CANDIDATE_D0_MANIFEST.md
VALIDATION_SLICE_MANIFEST.md
```

누적 progress:

```text
PROGRESS = [████████░░] 80%
```

S5 marks the end of authoring before independent validation.

---

# S6 — Parallel independent validation and telemetry capture

```text
WEIGHT = 10%
EXPECTED_RANGE = 5~15분
OWNER_CHECK_LIMIT = 25분
LEAD = PMO
VALIDATORS = MODELV / CONTROLV / PMOV in parallel
TARGET = frozen D0
```

## Critical experiment rule

All validators start from frozen D0.
They do not modify the target during review.
Findings are frozen before correction begins.

## MODELV slice

Inputs:

- R1 main revision
- relevant R3 changes
- definition/status slice from R2
- exact acceptance criteria

Checks:

- Owner-confirmed semantics preserved
- minimal Relation / composition / VIEW / CONTROL / STATE / FOLD consistency
- non-finality
- technology candidate status
- Open state preservation
- no unsupported formal claim

MODELV does not read the whole repository.

## CONTROLV slice

Inputs:

- input manifest
- duplicate report
- R2 crosswalk
- hashes
- telemetry ledgers to date
- affected source sections only

Checks:

- exact source/output mapping
- Owner decision vs PI vs Open classification
- duplicate disposition
- source recovery boundary
- telemetry timestamps/read-scope integrity

CONTROLV does not re-author model semantics.

## PMOV slice

Inputs:

- proposal/plan
- PMO timeline
- stage progress
- validator routing
- correction policy
- D0 freeze evidence

Checks:

- scope stayed within revision
- no silent scan expansion
- stage estimates and owner-check handling
- validator independence
- latency attribution method

## Validation output format

Each receipt contains:

```text
VALIDATOR
TARGET_SHA
INPUT_SLICE
START / END
CONTEXT_LOAD_DURATION
DIRECT_REVIEW_DURATION
GIT_CALLS
FULL_SCAN
REPEATED_WHOLE_TARGET_READ
BLOCKING_FINDINGS
ADVISORY_FINDINGS
NEW_SCOPE_REQUEST
VERDICT
```

## S6 exit

```text
all receipts target D0
findings frozen
no validator modifies D0
```

누적 progress:

```text
PROGRESS = [█████████░] 90%
```

## S6 Owner-check

- 25분 초과 전망
- validator가 full repository scan 요청
- validator가 new architecture/control을 blocking requirement로 요청
- additional validator 요구
- D0 전체를 반복 reread해야 한다는 요청

---

# S7 — One correction batch and affected-diff recheck

```text
WEIGHT = 5%
EXPECTED_RANGE = 5~10분
OWNER_CHECK_LIMIT = 15분
LEAD = PMO
AUTHORS = MODEL / CONTROL according to finding
RECHECK = affected validator only
```

## S7 actions

1. blocking findings만 correction backlog에 채택
2. advisory는 별도 recommendations로 보존
3. 한 번의 correction batch 수행
4. D1 candidate freeze
5. D0→D1 diff classification
6. affected acceptance criteria만 recheck

## Change classification

```text
NONMATERIAL
= spelling, formatting, index link, progress notation
→ diff-only recheck

MATERIAL_LOCAL
= one definition/status/crosswalk section
→ affected validator + dependent criteria

MATERIAL_GLOBAL
= core definition or authority state changes broad document meaning
→ stop / Owner review before broad revalidation
```

`SHA_CHANGED`는 global revalidation 사유가 아니다.

## S7 exit

```text
blocking findings = 0
stale target receipt = 0 for affected criteria
correction batches = 1
```

누적 progress:

```text
PROGRESS = [█████████░] 95%
```

S7 Owner-check:

- second correction batch 필요
- material global change
- new validator/domain 필요
- 15분 초과 전망

---

# S8 — Final packaging and VALIDATING cause verdict

```text
WEIGHT = 5%
EXPECTED_RANGE = 5~10분
OWNER_CHECK_LIMIT = 15분
LEAD = PMO + CONTROL
VALIDATION = PMOV checks calculation integrity
```

## S8 calculations

### Total active time

```text
TOTAL_ACTIVE_WALL_CLOCK =
program end - program start
- OWNER_WAIT
- documented external outage wait
```

### Validation wall-clock

```text
VALIDATION_WINDOW =
first validator context load start
→ last validator direct review end
```

### Validation attributable wall-clock

```text
VALIDATION_ATTRIBUTABLE =
non-overlapping VALIDATION_CONTEXT_LOAD
+ non-overlapping VALIDATION_DIRECT
+ FINDING_INTEGRATION
+ correction caused by blocking validation findings
+ revalidation
```

### Validation orchestration overhead

```text
VALIDATION_ORCHESTRATION =
repeated context reload
+ serial wait that could have been parallel
+ whole-target/repository reread
+ unnecessary full rescan
+ SHA-only revalidation
+ validator scope expansion
```

### Overrun

```text
TOTAL_OVERRUN = max(0, ACTUAL_TOTAL - EXPECTED_TOTAL_UPPER)
VALIDATION_OVERRUN = validation-related stage/correction/recheck overrun
```

If `TOTAL_OVERRUN = 0`, overrun contribution percentages are undefined.
Use the required enum `VALIDATING_NOT_PRIMARY` with qualifier
`NO_OVERRUN_CURRENT_RUN`, report category active-time shares only as
descriptive statistics, and do not use this run alone to prove the cause of a
historical incident. Historical attribution without contemporaneous raw timing
evidence remains `INDETERMINATE_DUE_TO_EVIDENCE_GAP`.

## Root-cause classification

```text
VALIDATING_PRIMARY_CAUSE
VALIDATION_ORCHESTRATION_PRIMARY_CAUSE
VALIDATING_CONTRIBUTING_CAUSE
VALIDATING_NOT_PRIMARY
MIXED_CAUSE
INDETERMINATE_DUE_TO_EVIDENCE_GAP
```

The report must include:

1. stage-by-stage actual vs expected
2. direct validation vs context load vs correction vs revalidation
3. files/sections read by each validator
4. repeated reads/full scans
5. validator parallelism
6. tool wait and Owner wait
7. raw formula
8. verdict and confidence
9. specific recurrence-prevention action

## S8 outputs

```text
VALIDATION_LATENCY_ATTRIBUTION_REPORT.md
PMO_COMPLETION_PACKAGE.md
final SHA256SUMS.txt
```

최종 progress:

```text
PROGRESS = [██████████] 100%
```

---

# 6. Stage budget summary

| Stage | Weight | Expected active | Owner check | Primary actor |
|---|---:|---:|---:|---|
| S0 Plan admission / telemetry | 5% | 5–10m | 15m | PMO + BYULV |
| S1 Input freeze / dedup | 10% | 5–10m | 15m | CONTROL |
| S2 Crosswalk / delta map | 15% | 8–15m | 25m | CONTROL + MODEL |
| S3 Main authoring | 25% | 15–25m | 35m | MODEL |
| S4 Companion sync | 15% | 8–15m | 25m | MODEL + CONTROL |
| S5 Freeze / self-check | 10% | 5–10m | 15m | PMO + CONTROL |
| S6 Parallel validation | 10% | 5–15m | 25m | MODELV + CONTROLV + PMOV |
| S7 Correction / diff recheck | 5% | 5–10m | 15m | PMO + affected roles |
| S8 Packaging / verdict | 5% | 5–10m | 15m | PMO + CONTROL |

```text
SERIAL RANGE SUM = 약 61~120분
CONSERVATIVE PLANNING RANGE = 61~120분
PARALLEL BEST-CASE FORMULA = S0 + S1 + S2 + max(S3,S4) + S5 + S6 + S7 + S8
PARALLEL BEST-CASE ENVELOPE = 53~105분
BEST-CASE CONDITION = S4 fully overlaps its eligible late-S3 window after definition lock
OVERRUN BASELINE UPPER = 120분
TOTAL OWNER CHECK = 120분 초과 전망
OWNER WAIT = excluded
```

Parallelism assumptions:

- S2 CONTROL/MODEL parallel
- late S3 and S4 preparation may overlap after definitions lock
- S6 three validators parallel

실제 병렬화가 불가능하면 PMO는 revised wall-clock estimate를 opening report에 표시한다.

---

# 7. Progress report schedule

PMO는 최소 다음 시점에 보고한다.

```text
0% execution open
5% S0 complete
15% S1 complete
30% S2 complete
55% S3 complete
70% S4 complete
80% D0 frozen
90% validation findings frozen
95% correction/recheck complete
100% completion + cause verdict
```

작업이 매우 빠르게 연속 완료되면 인접 checkpoint를 하나의 보고로 합칠 수 있다.
Anomaly report는 checkpoint와 무관하게 즉시 수행한다.

Progress template:

```text
[PROGRESS UPDATE]

PROGRESS = [██████░░░░] 55%
PROGRAM = ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0
CURRENT_STAGE = S3 MAIN REVISION AUTHORING
COMPLETED = S0 / S1 / S2
NOW = ...
REMAINING = ...
ACTIVE_WORKERS = MODEL
ACTIVE_VALIDATORS = NONE
STAGE_ELAPSED = ...
STAGE_EXPECTED = 15~25m
OWNER_CHECK_LIMIT = 35m
GIT_READ_SCOPE = exact primary packet sections
FULL_SCAN = NO
REPEATED_READ = NO or reason
BLOCKER = NONE
SCOPE_EXPANSION = NO
VALIDATION_TELEMETRY_STATE = NOT_STARTED / ACTIVE / COMPLETE
OWNER_ACTION_REQUIRED = NO
```

---

# 8. Scope expansion protocol

다음 중 하나가 발생하면 PMO는 조용히 계속하지 않는다.

```text
NEW_FULL_SCAN
REPEATED_WHOLE_TARGET_READ
NEW_EXTERNAL_RESEARCH
NEW_VALIDATOR
NEW_WORKSTREAM
NEW_ARCHITECTURE_REQUIREMENT
SECOND_CORRECTION_BATCH
GLOBAL_REVALIDATION
MISSING_REQUIRED_SOURCE
OWNER_SEMANTIC_DECISION_REQUIRED
TOTAL > 120m PROJECTION
UNCLASSIFIED_TELEMETRY > 10%
```

Anomaly report:

```text
[TIME / SCOPE REVIEW REQUIRED]

PROGRESS =
CURRENT_STAGE =
ELAPSED =
ORIGINAL_EXPECTATION =
OWNER_CHECK_LIMIT =
NEW_FINDING =
WHY_ORIGINAL_SCOPE_IS_INSUFFICIENT =
PROPOSED_ADDITIONAL_READ / WORK / VALIDATOR =
ADDITIONAL_EXPECTED_TIME =
IMPACT_IF_NOT_EXPANDED =
OPTIONS =
A. continue targeted expansion
B. mark item OPEN/provisional and finish
C. defer to separate program
OWNER_CONFIRMATION_REQUIRED = YES
```

---

# 9. Validation safeguards

## 9.1 No full scan by default

Validator inputs are exact slices.
A repository-wide scan requires a named acceptance criterion that cannot be satisfied otherwise.

## 9.2 No serial whole-target rereads

Multiple validators may be used, but each receives role-specific context.
Shared exact refs/manifests are reused.

## 9.3 No validator co-design as blocking

Validator may suggest improvements.
A new architecture or gate is advisory unless required by the current acceptance criteria or Owner-authorized scope.

## 9.4 One finding freeze

All D0 findings are collected before correction.
This avoids:

```text
validator A → correction → validator B → correction → validator C → correction
```

## 9.5 Diff-only recheck

Nonmaterial and material-local corrections do not restart global validation.

## 9.6 No retrospective conclusion

The latency report may not infer durations from memory after completion when event timestamps were available.
Missing intervals remain evidence gaps.

---

# 10. Program acceptance criteria

## Source and revision

```text
AC-01 exact primary inputs frozen
AC-02 duplicate inputs dispositioned
AC-03 missing-source boundary preserved
AC-04 73 Owner items mapped
AC-05 10 Open items retained/dispositioned as Open
AC-06 7 PI items remain non-Owner proposals
AC-07 180 questions preserved/dispositioned with reason
AC-08 definitions synchronized across outputs
AC-09 v1.0 retained governance/safety contract preserved
AC-10 technology and implementation remain unfrozen
AC-11 external matrix not expanded without new research scope
AC-12 candidate packet hashes/read order correct
```

## Validation process

```text
AC-13 D0 exact target frozen before validation
AC-14 MODELV/CONTROLV/PMOV independence preserved
AC-15 role-scoped validator inputs recorded
AC-16 context load and direct review time separated
AC-17 full/repeated scans recorded
AC-18 one correction batch default respected
AC-19 affected-diff recheck used where applicable
```

## Latency diagnosis

```text
AC-20 >=90% active time categorized
AC-21 direct validation and orchestration overhead separated
AC-22 stage actual vs expected computed
AC-23 validation-related overrun computed
AC-24 explicit cause classification issued
AC-25 raw timeline and formulas included
AC-26 recurrence-prevention recommendations trace to observed cause
```

## Completion

```text
AC-27 PMO completion package produced
AC-28 progress reaches 100% by checkpoint completion
AC-29 Owner action needs clearly stated
AC-30 no validation PASS invented beyond exact receipts
```

---

# 11. Stop / Hold conditions

Immediate `REVIEW_REQUIRED`:

- primary input cannot be recovered
- Owner-confirmed and main v2.0 materially conflict
- exact source precedence cannot resolve a core definition
- missing packet becomes essential
- revision requires new scientific claim
- broad external research required
- question resolution requires Owner interview
- output would imply Final/Active/Frozen status
- validator independence compromised
- telemetry coverage falls below 90%
- latency verdict cannot be supported
- task expands beyond 120-minute Owner-check without approval

---

# 12. PMO completion package

`PMO_COMPLETION_PACKAGE.md` fields:

```text
PROGRAM_ID
OWNER_DIRECTIVE_REF
PROPOSAL_PATH / SHA
PLAN_PATH / SHA
TASK_BRANCH
BASE_COMMIT
FINAL_COMMIT / PR

INPUT_MANIFEST
CANONICAL_INPUTS
DUPLICATES
MISSING_SOURCES

REVISION_OUTPUTS
OUTPUT_HASHES
OWNER_DECISION_MAPPING
OPEN_ITEM_STATUS
QUESTION_STATUS
EXTERNAL_RESEARCH_STATUS

BYULV_PLAN_RECEIPT
MODELV_RECEIPT
CONTROLV_RECEIPT
PMOV_RECEIPT

EXPECTED_ACTIVE_TOTAL
ACTUAL_ACTIVE_TOTAL
OWNER_WAIT
TOOL_WAIT
STAGE_VARIANCES

VALIDATION_CONTEXT_LOAD
VALIDATION_DIRECT
VALIDATION_FINDING_INTEGRATION
VALIDATION_CORRECTION
REVALIDATION
VALIDATION_ORCHESTRATION_OVERHEAD
VALIDATION_ATTRIBUTABLE_TOTAL
TOTAL_OVERRUN
VALIDATION_OVERRUN

VALIDATING_CAUSE_VERDICT
VERDICT_CONFIDENCE
EVIDENCE_GAPS
RECURRENCE_PREVENTION_ACTIONS

FINAL_PROGRESS = 100%
BLOCKING_FINDINGS
OPEN_FINDINGS
OWNER_ACTION_REQUIRED
NEXT_ACTION
```

---

# 13. Exact PMO dispatch

```text
[OWNER-AUTHORIZED BYUL → PMO DISPATCH]

CURRENT_PERSONA_LOCK = PMO

PROGRAM =
ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-v1.0

AUTHORIZATION =
Proceed with the bounded successor revision of the existing ASA Core v2.0 research packet and determine, from instrumented execution evidence, whether VALIDATING was the primary cause of slowdown.

EXECUTE =
S0 through S8 in the approved plan.

FIRST ACTION =
Recover current Git pointers and exact proposal/plan refs,
then issue the PMO EXECUTION OPEN report before broad reads.

REQUIRED =
- task-specific progress bar;
- stage expected ranges and Owner-check limits;
- narrow-first Git reads;
- frozen D0 before validation;
- parallel role-scoped MODELV/CONTROLV/PMOV validation;
- one correction batch;
- affected-diff recheck;
- latency attribution report separating direct validation from orchestration overhead.

DO NOT =
- redo all external research;
- solve all 180 questions;
- select a technology;
- implement a prototype;
- run repository-wide scans without a named need;
- add ENG/IVA or new validation gates silently;
- infer that SHA change requires global revalidation;
- exceed Owner-check limits without reporting;
- claim Final/Frozen/Active/Production status.

RETURN =
revised candidate packet
+ exact validation receipts
+ raw timing/read/finding ledgers
+ explicit VALIDATING cause verdict
+ PMO completion package.
```
