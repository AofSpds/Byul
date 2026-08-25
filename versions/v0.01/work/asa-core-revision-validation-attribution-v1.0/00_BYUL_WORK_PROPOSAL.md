# BYUL — ASA Core 누적 연구 리비전 및 VALIDATING 원인 규명 작업제안서 v1.0

```text
DOCUMENT_ID =
BYUL-ASA-CORE-REVISION-VALIDATION-ATTRIBUTION-WORK-PROPOSAL-v1.0

PROJECT = AAA / BYUL
PRODUCT = ASSET AGENT ASA
PLANNING_PERSONA = BYUL
EXECUTION_COMMAND = PMO
PLAN_VALIDATOR = BYULV
DATE_KST = 2026-08-26

STATUS = OWNER_AUTHORIZED / PMO_DISPATCH_CANDIDATE
TASK_CLASS = STANDARD / BOUNDED DOCUMENT REVISION + EXECUTION TELEMETRY
REPOSITORY_MUTATION = BOUNDED DOCUMENT OUTPUTS ONLY
PRODUCTION_AUTHORIZATION = NONE
WORLD_MODEL_FREEZE = PROHIBITED
TECHNOLOGY_FREEZE = PROHIBITED
IVA_REQUIRED = NO
```

## 0. 제안 요약

이번 작업은 ASA Core에 대해 새 연구를 처음부터 다시 수행하는 프로그램이 아니다.

이미 만들어진 다음 연구 패킷을 하나의 정합적인 successor revision으로 재구성하는 작업이다.

1. `ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.0_2026-08-25.md`
2. `ASA_CORE_OWNER_CONFIRMED_DECISIONS_2026-08-25.md`
3. `ASA_CORE_WORLD_MODEL_v2.0_CHANGELOG_2026-08-25.md`
4. `ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_2026-08-25.md`
5. `ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_2026-08-25.md`
6. `ASA_CORE_REVISION_PACKET_INDEX_2026-08-25.md`

현재 패킷에는 이미 다음이 존재한다.

```text
OWNER-CONFIRMED / CONFIRMED-DIRECTION ITEMS = 73
EXPLICIT OPEN ITEMS = 10
OWNER INTERVIEW QUESTIONS = 180
EXTERNAL RESEARCH REFERENCES = 21
HYBRID CORE CANDIDATES = 4
COMMON PROBES = 20
TECHNOLOGY SELECTION = NONE
IMPLEMENTATION AUTHORIZATION = NONE
```

따라서 PMO의 임무는 다음 두 축이다.

```text
TRACK A — REVISION EXECUTION
기존 연구성과를 재연구하지 않고,
Owner 결정·Pro-mode 제안·Open 상태·기술후보를
정합적인 successor 문서군으로 리비전한다.

TRACK B — VALIDATION LATENCY ATTRIBUTION
이번 실제 작업의 단계별 시간을 계측하여,
VALIDATING이 지연의 주원인인지,
검증 자체가 아니라 검증 오케스트레이션이 원인인지,
아니면 source read / authoring / correction 등 다른 단계가 원인인지
증거로 판정한다.
```

BYUL의 제안 결론은 `GO`이다.

다만 다음 조건을 고정한다.

- 전체 repository 재조사 금지
- 21개 외부 reference 전수 재연구 금지
- 180개 질문 일괄 해결 금지
- v2.0을 Final Ontology로 승격 금지
- 기술 선택 금지
- 구현 착수 금지
- validation을 authoring 중간에 반복 삽입 금지
- validator별 전체 원문·전체 Git 반복 scan 금지

---

# 1. Owner 지시 해석

Owner의 현재 지시는 세 가지다.

## 1.1 PMO가 실제 작업을 진행한다

BYUL은 목적·범위·산출물·판정 기준을 정의하고 PMO에 dispatch한다.
PMO는 현재 authority contract 아래에서 작업을 분해하고 실행한다.

PMO는 World Model 의미를 임의로 재작성하지 않는다.
World Model 본문 authoring은 `MODEL`, Owner 결정·상태 crosswalk와 실행 증거는 `CONTROL`, integration과 시간·progress 관리는 `PMO`가 담당한다.

## 1.2 기존 연구를 리비전한다

`revision`의 정확한 의미는 다음과 같다.

```text
revision =
기존 Owner 결정과 연구결과를 보존하면서
문서 간 정의·용어·상태·참조·우선순위를 동기화하고,
중복·불일치·누락을 successor 문서에서 보정하는 것
```

다음은 revision의 범위가 아니다.

```text
not revision =
모든 외부논문 재검증
모든 과거 Git 문서 전수감사
180개 Open Question 해결
formal calculus 완성
Candidate A/B/C/D 구현
20개 Probe 실제 실행
production architecture 결정
ASA→BYUL repository migration
```

## 1.3 VALIDATING 원인 여부를 확인한다

이번에는 단순히 “검증이 오래 걸린 것 같다”고 추정하지 않는다.

작업 시작부터 종료까지 시간을 다음 category로 분리 기록한다.

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

이를 통해 다음을 분리한다.

```text
VALIDATION_DIRECT
= validator가 실제 acceptance criteria를 판단한 시간

VALIDATION_ORCHESTRATION
= validator context 재로딩, serial dispatch,
  반복 full read, 불필요한 scan, SHA 기반 전체 재검증 시간

VALIDATION_INDUCED_REWORK
= blocking finding으로 인해 실제로 필요한 correction 및 recheck 시간

NON_VALIDATION_WORK
= source recovery, authoring, synchronization, packaging 등
```

최종 보고서는 반드시 아래 중 하나로 결론을 낸다.

```text
VALIDATING_PRIMARY_CAUSE
VALIDATION_ORCHESTRATION_PRIMARY_CAUSE
VALIDATING_CONTRIBUTING_CAUSE
VALIDATING_NOT_PRIMARY
MIXED_CAUSE
INDETERMINATE_DUE_TO_EVIDENCE_GAP
```

---

# 2. Source basis와 우선순위

## 2.1 Primary source set

PMO가 기본적으로 읽는 범위는 위 6개 revision packet 문서뿐이다.

본문 `ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.0_2026-08-25.md`는 현재 패킷의 중심 문서이며 반드시 exact input으로 포함한다.

## 2.2 Source precedence

문서 간 충돌 시 다음 순서를 적용한다.

```text
1. 이번 채널에서 Owner가 직접 확정·정정한 결정
2. Owner-confirmed decision register의 CONFIRMED 상태
3. Owner-confirmed decision register의 CONFIRMED_DIRECTION 상태
4. 기존 v1.0의 유지된 governance / safety contract
5. external research matrix의 source-grounded synthesis
6. Pro-mode implication / recommendation
7. Open question / unresolved candidate
```

`PRO_MODE_IMPLICATION`은 Owner 결정으로 승격하지 않는다.
`OPEN`은 편집 편의를 위해 자동 해결하지 않는다.

## 2.3 Secondary source — on demand only

다음 자료는 primary packet만으로 특정 불일치를 해결할 수 없을 때 해당 section만 읽는다.

- `ASA_CORE_WORLDVIEW_v1.0_2026-08-24.md`
- `ASA_CORE_WORLDVIEW_v1.0_REVISION_REPORT_2026-08-24.md`
- `ASA_CORE_WORLDVIEW_INTEGRATED_v0.1_2026-08-24.md`
- `BYUL_PRO_MODE_RESEARCH_HANDOFF_PACKET_2026-08-24.md`
- BYUL의 exact Owner-confirmation records

이 자료를 읽는다고 해서 전체 파일이나 전체 repository history를 재검증하지 않는다.

## 2.4 Missing-source boundary

현재 packet이 명시하는 다음 파일은 발견되지 않은 상태를 보존한다.

```text
BYUL_CLOSURE_TOOLKIT_CORE_COMBINATION_NEXT_CHANNEL_PACKET_2026-08-24.md
```

PMO는 이 파일을 읽었다고 주장하지 않는다.
해당 파일이 실제로 발견될 경우에만 successor revision과 targeted diff를 수행한다.

---

# 3. Revision의 목표 상태

## 3.1 핵심 정의 동기화

Successor revision은 최소한 다음 정의를 전 문서에서 동일하게 유지해야 한다.

```text
RELATION
= current-resolution directional mapping

RELATION + RELATION → RELATION
= recursive composition law / hypothesis

VIEW:X
= 관점·필터·조건·라우팅·해상도·구성 작용

STATE:X
= VIEW:X 아래 성립한 folded holding state

CONTROL:X
= 의도적 변화·steering

FOLD / OMIT
= 명시적 protocol에서 meaning-preserving representation omission

EXPAND / RECONSTRUCT
= View-relative high-resolution reconstruction;
  EXACT / INFERRED / UNKNOWN 및 multiple candidates 허용
```

## 3.2 금지 혼동 동기화

```text
VIEW != STATE
VIEW != VIEW output
CONTROL != DELTA
FOLD != lossy filtering
same endpoints != same Relation
View-relative equivalence != identity merge
reverse lookup != inverse Relation
higher resolution != final truth
STATE alone != predecessor-free State
```

## 3.3 상태 분리

Successor packet은 다음 상태를 혼합하지 않는다.

```text
OWNER_CONFIRMED
OWNER_CONFIRMED_DIRECTION
OWNER_CONFIRMED_PROVISIONAL_TERM
PRO_MODE_IMPLICATION
OPEN
EXTERNAL_RESEARCH_FINDING
IMPLEMENTATION_CANDIDATE
```

## 3.4 유지해야 할 비최종성

```text
FINAL ONTOLOGY = NO
FINAL DATABASE = NO
FINAL GRAPH MODEL = NO
FINAL RULE LANGUAGE = NO
TECHNOLOGY FREEZE = NO
PRODUCTION AUTHORIZATION = NO
```

## 3.5 External research의 역할

Research Matrix는 “정답 기술 선택표”가 아니다.

각 기술은 다음 plane의 candidate component로만 유지한다.

```text
RUNTIME
REFERENCE / ORACLE
STRUCTURAL COUNTER-MODEL
BOUNDED CANDIDATE SEARCH
PROVENANCE / REPLAY SPINE
LATENT CONTROL ADAPTER
```

Candidate A→B→C→D 순서는 연구 권고이며 implementation authorization이 아니다.

---

# 4. 제안 산출물

PMO는 원본을 덮어쓰지 않고 successor packet을 만든다.
정확한 version label은 `v2.1 CANDIDATE`로 제안하되 Owner 승인 전 Final/Active로 표기하지 않는다.

## 4.1 Revision outputs

```text
R1 = ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.1_CANDIDATE_2026-08-26.md
R2 = ASA_CORE_OWNER_DECISION_CROSSWALK_v2.1_CANDIDATE_2026-08-26.md
R3 = ASA_CORE_WORLD_MODEL_v2.1_CANDIDATE_CHANGELOG_2026-08-26.md
R4 = ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_v2.1_SYNC_2026-08-26.md
R5 = ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_v2.1_SYNC_2026-08-26.md
R6 = ASA_CORE_REVISION_PACKET_INDEX_v2.1_CANDIDATE_2026-08-26.md
R7 = SHA256SUMS.txt
```

### R1 — Main revision

- v2.0의 의미를 보존한다.
- Owner 결정과 충돌하는 문구를 제거·보정한다.
- 정의와 terminology guard를 한 곳에 모은다.
- Owner-confirmed / Pro-mode / Open 상태를 시각적으로 분리한다.
- 구현/기술 선택으로 읽힐 문구를 candidate status로 낮춘다.

### R2 — Decision crosswalk

Owner decision register를 다시 작성하거나 의미를 바꾸지 않는다.
대신 OD-001..073, OPEN-01..10, PI-01..07이 R1/R3/R4/R5 어느 section에 반영됐는지 mapping한다.

### R3 — Changelog

- v1.0→v2.0 breaking changes 보존
- v2.0→v2.1 candidate 편집·정합성 변경을 별도 구분
- semantic change와 editorial synchronization을 분리

### R4 — Research Matrix synchronization

외부연구를 전면 재조사하지 않는다.
다음만 수정한다.

- R1 terminology와 충돌하는 설명
- technology status가 과도하게 확정된 표현
- Candidate A/B/C/D와 20 Probe 간 참조 불일치
- source locator 오류 또는 명백한 날짜/상태 불일치

새 외부조사는 material gap 발견 시 Owner confirmation 후 별도 scope로 전환한다.

### R5 — Open Questions synchronization

180개 질문을 해결하지 않는다.

- 이미 Owner-confirmed인 질문을 반복하는지 확인
- terminology 변경으로 무효·중복된 질문 표시
- P0/P1/P2/P3 priority와 다음 인터뷰 순서 동기화
- 질문 ID는 가능한 보존
- 삭제 대신 `SUPERSEDED / DUPLICATE / RETAINED_OPEN` 상태를 사용

### R6 — Packet Index

- exact 읽기 순서
- 각 문서 역할
- Owner-confirmed / proposed / open 상태
- 다음 작업과 금지범위
- missing-source note

## 4.2 Execution and diagnostic outputs

```text
T1 = PMO_REVISION_EXECUTION_TIMELINE.tsv
T2 = PMO_GIT_READ_SCOPE_LEDGER.tsv
T3 = VALIDATION_EVENT_AND_FINDING_LEDGER.tsv
T4 = VALIDATION_LATENCY_ATTRIBUTION_REPORT.md
T5 = PMO_COMPLETION_PACKAGE.md
```

---

# 5. Persona routing

## 5.1 BYUL

- Owner intent와 작업 목적 정의
- 현재 proposal/plan 작성
- PMO dispatch 추천
- semantic target을 임의로 self-validate하지 않음

## 5.2 BYULV

Stage 0에서 본 proposal/plan의 다음 항목만 검증한다.

- Owner 요청 충실성
- revision과 재연구의 경계
- World Model non-freeze
- authority boundary
- validation attribution 설계가 결론을 미리 정하지 않았는지
- 예상시간·progress·Owner-check 구조

BYULV는 전체 source packet을 재리비전하지 않는다.

## 5.3 PMO

- WBS/parallelism/dependency
- stage timing
- progress
- exact target freeze
- correction batch
- completion package
- validation attribution integration

## 5.4 MODEL

- R1/R3/R4/R5의 model-semantic authoring
- Owner 결정과 Pro-mode proposal 분리
- v2.0에서 유지·보정·open 상태 구분

## 5.5 CONTROL

- exact input/output inventory
- duplicate input detection
- Owner decision crosswalk evidence
- source/read scope ledger
- stage/validator timeline evidence
- hashes

## 5.6 Validators

```text
MODELV
= revised World Model semantics, definitions, non-finality

CONTROLV
= exact source/output mapping, Owner-state classification, telemetry integrity

PMOV
= PMO scope, stage trace, validator routing, latency attribution calculation
```

세 validator는 frozen candidate에 대해 병렬 role-scoped validation을 수행한다.

## 5.7 기본 비참여

```text
ENG / ENGV
= implementation/tooling mutation이 없으므로 기본 미호출

IVA
= release, deletion, production, organization cutover가 아니므로 미호출
```

새 validator가 필요하면 PMO가 이유·추가시간·scope를 먼저 Owner에게 보고한다.

---

# 6. VALIDATING 원인 규명 설계

## 6.1 핵심 원칙

이번 진단은 “validator를 빼고 빨리 끝낸다”는 실험이 아니다.

정상적인 revision을 수행하면서 validation window를 분리하고 계측한다.

```text
AUTHORING CANDIDATE D0 FREEZE
→ PARALLEL ROLE-SCOPED VALIDATION
→ FINDING FREEZE
→ ONE CORRECTION BATCH
→ AFFECTED-DIFF RECHECK
```

validation과 authoring을 계속 교차시키지 않는다.

## 6.2 측정 단위

각 event는 최소 다음을 기록한다.

```text
EVENT_ID
STAGE_ID
ACTOR / PERSONA
CATEGORY
START_KST
END_KST
ACTIVE_SECONDS
WAIT_SECONDS
INPUT_REFS
FILES_READ
BYTES_OR_LINES_READ
GIT_CALL_COUNT
FULL_SCAN = YES/NO
REPEATED_READ = YES/NO
VALIDATION_TARGET_SHA
FINDING_COUNT
BLOCKING_FINDING_COUNT
ADVISORY_FINDING_COUNT
CORRECTION_TRIGGERED = YES/NO
NOTES
```

내부 token 수처럼 신뢰성 있게 관측할 수 없는 값은 원인분석의 핵심 지표로 사용하지 않는다.

## 6.3 Wall-clock 중복 처리

병렬 validator의 시간을 단순 합산하여 wall-clock으로 과장하지 않는다.

```text
VALIDATION_WALL_CLOCK
= first validator start → last validator finish

VALIDATOR_COMPUTE_SUM
= 각 validator active duration의 합

TOTAL_ACTIVE_WALL_CLOCK
= program start → completion
  - OWNER_WAIT
  - 명시적 external outage wait
```

## 6.4 Validation attributable time

```text
VALIDATION_ATTRIBUTABLE_WALL_CLOCK =
VALIDATION_CONTEXT_LOAD_WALL_CLOCK
+ VALIDATION_DIRECT_WALL_CLOCK
+ VALIDATION_FINDING_INTEGRATION_WALL_CLOCK
+ CORRECTION_TIME caused by blocking findings
+ REVALIDATION_WALL_CLOCK
```

단, 병렬구간은 중복 합산하지 않는다.

## 6.5 Overrun attribution

각 stage에는 `EXPECTED_RANGE`와 `OWNER_CHECK_LIMIT`을 사전 선언한다.

```text
STAGE_OVERRUN_i = max(0, ACTUAL_i - EXPECTED_UPPER_i)
TOTAL_OVERRUN = max(0, ACTUAL_TOTAL - EXPECTED_TOTAL_UPPER)
```

Validation-related overrun은 다음으로 계산한다.

```text
VALIDATION_OVERRUN =
validation stage overrun
+ validation-triggered correction/recheck overrun
+ validation-triggered repeated read/full scan overhead
```

## 6.6 판정 규칙

```text
VALIDATING_PRIMARY_CAUSE
= VALIDATION_OVERRUN이 TOTAL_OVERRUN의 50% 이상이며
  다른 단일 category보다 큼

VALIDATION_ORCHESTRATION_PRIMARY_CAUSE
= 위 조건을 만족하면서 validation-related overrun의 과반이
  repeated context load / serial dispatch / full rescan /
  unnecessary revalidation에서 발생

VALIDATING_CONTRIBUTING_CAUSE
= validation-related overrun이 TOTAL_OVERRUN의 20~49%

VALIDATING_NOT_PRIMARY
= validation-related overrun이 20% 미만이고
  source recovery / authoring / tool wait 등 다른 category가 지배

MIXED_CAUSE
= 복수 category가 유사한 기여를 보이며 단일 주원인이 없음

INDETERMINATE_DUE_TO_EVIDENCE_GAP
= active time의 10% 이상이 미분류되거나
  stage boundary/timestamps가 신뢰 불가능
```

이 threshold는 과학적 보편법칙이 아니라 이번 operational root-cause classification rule이다.
보고서에는 원시 시간표와 계산식을 함께 남긴다.

## 6.7 Validation 자체와 오케스트레이션 분리

최종 결론은 반드시 다음 두 질문에 각각 답한다.

1. validator의 실제 판단 자체가 오래 걸렸는가?
2. validator가 같은 자료를 다시 읽고, 순차로 호출되고, correction마다 전체를 다시 검증한 운영방식이 오래 걸렸는가?

`VALIDATING`이라는 한 단어로 둘을 합치지 않는다.

---

# 7. 예상시간과 Owner-check

본 제안은 현재 알려진 6-document packet과 main v2.0을 기준으로 한다.

```text
EXPECTED ACTIVE WALL-CLOCK = 45~90분
OWNER_CHECK TOTAL = 120분 초과 전망 시 확인
OWNER WAIT = 제외
```

이는 deadline이 아니다.
예상보다 작업이 커지는지 감지하는 anomaly detector다.

상세 stage budget은 실행계획서에 고정한다.

다음은 별도 scope다.

- 새 외부연구: 별도 견적
- 180개 질문 해결: 별도 interview program
- formal specification: 별도 research program
- prototype implementation: 별도 ENG program

---

# 8. Progress model

```text
S0 Plan validation / telemetry setup       5%
S1 Exact input freeze / dedup             10%
S2 Decision-definition crosswalk          15%
S3 Main revision authoring                25%
S4 Companion synchronization              15%
S5 Candidate freeze / self-check          10%
S6 Independent validation                 10%
S7 Correction / affected-diff recheck      5%
S8 Packaging / attribution verdict         5%
                                         ----
                                         100%
```

보고 형식:

```text
PROGRESS = [████░░░░░░] 40%
CURRENT_STAGE =
COMPLETED =
NOW =
REMAINING =
ACTIVE_WORKERS =
ACTIVE_VALIDATORS =
STAGE_EXPECTED =
OWNER_CHECK_LIMIT =
BLOCKER =
SCOPE_EXPANSION =
VALIDATION_TELEMETRY_STATE =
OWNER_ACTION_REQUIRED =
```

---

# 9. Stop / Owner-check 조건

PMO는 다음 상황에서 자동으로 범위를 확대하지 않는다.

- main v2.0 exact input을 복구할 수 없음
- primary 6-document packet의 canonical file 수가 불명확
- duplicate가 내용상 동일하지 않음
- Owner decision과 v2.0 본문 사이 material conflict
- 21개 external reference 재조사가 필요해짐
- 180개 질문 중 substantive Owner 결정이 필요해짐
- repository-wide history/tree/object scan 필요
- validator가 새 architecture를 blocking requirement로 요구
- validation stage가 Owner-check limit을 넘길 전망
- correction loop가 1 batch를 넘어감
- total active wall-clock이 120분을 넘길 전망
- validation telemetry 누락이 active time의 10%를 넘음

보고:

```text
PROGRESS =
CURRENT_STAGE =
ORIGINAL_SCOPE =
NEW_FINDING =
WHY_MORE_WORK =
REVISED_SCOPE =
ADDITIONAL_EXPECTED_TIME =
OPTIONS =
OWNER_CONFIRMATION_REQUIRED = YES
```

---

# 10. Acceptance criteria

```text
AC-01 primary source packet exact inputs identified
AC-02 duplicate inputs identified and canonicalized without content loss
AC-03 all 73 Owner-confirmed/direction items mapped
AC-04 all 10 explicit Open items preserved as Open
AC-05 PI-01..07 remain Pro-mode implications, not Owner decisions
AC-06 180 question IDs preserved or dispositioned with reason
AC-07 Reality / Claim / Relation Bundle / Closure Object status consistent
AC-08 VIEW / CONTROL / STATE / FOLD / EXPAND definitions consistent
AC-09 v1.0 retained governance/safety contract not silently removed
AC-10 technology selection remains open
AC-11 implementation remains unauthorized
AC-12 main revision and companion documents cross-reference correctly
AC-13 external research claims are not expanded without source work
AC-14 missing-source note preserved
AC-15 candidate packet hashes generated
AC-16 validator inputs are role-scoped
AC-17 no repeated full repository scan without recorded reason
AC-18 nonmaterial correction uses affected-diff recheck
AC-19 stage timing ledger coverage >= 90% of active time
AC-20 final report issues explicit VALIDATING cause classification
AC-21 report separates direct validation from orchestration overhead
AC-22 PMO completion package produced
```

---

# 11. BYUL 제안 판정

```text
RECOMMENDATION = GO

EXECUTION COMMAND = PMO
PLAN VALIDATION = BYULV
AUTHORING = MODEL
SOURCE / TELEMETRY CONTROL = CONTROL
OUTPUT VALIDATION = MODELV + CONTROLV + PMOV in parallel
ENG / ENGV = NOT PLANNED
IVA = NOT PLANNED

EXPECTED ACTIVE WALL-CLOCK = 45~90분
TOTAL OWNER CHECK = 120분 초과 전망

PRIMARY DIAGNOSTIC QUESTION =
Was VALIDATING the primary cause of slowdown?

REQUIRED ANSWER =
Evidence-based classification with raw stage timeline,
not impression or retrospective guess.
```

Owner의 현재 메시지는 PMO 진행 권한으로 기록한다.
PMO는 실행계획서의 S0부터 시작하고, broad Git read 전에 opening estimate/progress baseline을 보고한다.
