# ASA CORE WORLD MODEL v2.1 CANDIDATE — CHANGELOG / REVISION REPORT

```text
STATUS = V2.1_CANDIDATE CHANGELOG / OWNER_REVIEW_PENDING / NON_FROZEN
BASELINE_OLD = ASA_CORE_WORLDVIEW_v1.0_2026-08-24.md
BASELINE_INTERMEDIATE = ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.0_2026-08-25.md
BASELINE_NEW = ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.1_CANDIDATE_2026-08-26.md
CHANGE_CLASS = V1.0_TO_V2.0 FOUNDATIONAL + V2.0_TO_V2.1 SYNCHRONIZATION
DATE_KST = 2026-08-26
IMPLEMENTATION_AUTHORIZATION = NONE
```

---

## 0. Revision verdict

Part A는 v1.0→v2.0의 기존 breaking change 기록을 보존한다. Part B는
v2.0→v2.1 candidate의 bounded synchronization만 기록한다. Part B는
새 Owner 결정, 기술 선택, formal calculus 완성 또는 구현 승인이 아니다.

v2.0은 v1.0의 governance·audit·replay·safety 구조를 폐기하지 않는다. 그러나 **World Model kernel의 존재론·어휘·합성 단위**를 크게 바꾸므로 minor revision이 아니다.

```text
v1.0 중심
Reality / SourceRecord / Claim / RelationAssertion / Closure / ViewSpec-Run-Result

v2.0 중심
Directional Relation / Recursive Composition / FOLD-EXPAND / VIEW / CONTROL / STATE
```

핵심 변화는 “더 많은 객체 타입을 정의하는 것”에서 “최소 Relation과 역할별 접힌 추상화를 정의하는 것”으로의 이동이다.

---

# I. BREAKING CONCEPTUAL CHANGES

## CHG-001 — `Reality` Core entity 제거

### v1.0

`REALITY > ANY MODEL / VIEW`, RealityReferent, Observation 등이 kernel vocabulary에 존재했다.

### v2.0

`Reality`를 Core 객체·계층에서 제거한다.

### 이유

Owner는 `Reality`가 ASA Core 개념표에 없다고 명시했다. 모델 비최종성은 object type이 아니라 guard로 표현할 수 있다.

### Migration

| 기존 | 조치 |
|---|---|
| `RealityReferent` | REMOVE FROM WORLD-MODEL KERNEL |
| `REALITY > MODEL` | MOVE TO NON-FINALIZATION / EPISTEMIC GUARD, 필요 시 문구 재검토 |
| 외부 evidence ingress | Evidence/Data layer contract로 재설계 |

---

## CHG-002 — `Source`를 존재 종류에서 relation-local role로 이동

### v1.0

SourceRecord/EvidenceItem/Observation 계층이 World Model의 앞단으로 제안됐다.

### v2.0

`Source`와 `Target`은 각 방향 Relation 안에서의 역할이다. 고정 class가 아니다.

### Migration

- 원본 파일·로그·센서·계약 문서는 Evidence plane의 typed records로 유지 가능하다.
- 그러나 World Model kernel의 모든 입력을 `SourceObject` ontology에 강제하지 않는다.
- `source_ref`라는 operational field는 유지 가능하지만 의미상 role이다.

---

## CHG-003 — `Claim` 폐기

### v1.0

Claim과 RelationAssertion을 분리해 “누가 무엇을 주장했는가”와 “구조적으로 무엇이 성립하는가”를 나누었다.

### v2.0

Claim은 최소 Relation 이름으로 부적절하므로 제거한다.

### 보존 범위

- 사람이 한 주장, 모델 출력, 법적 진술을 표현하는 **도메인-specific statement type**은 Evidence/Governance layer에 남을 수 있다.
- 다만 모든 Relation을 Claim으로 강제하지 않는다.

---

## CHG-004 — `RelationAssertion`에서 current-resolution directional Relation으로

### v1.0

다항 RelationAssertion record가 canonical semantic assertion 후보였다.

### v2.0

```text
RELATION : SOURCE → TARGET
```

현재 해상도에서의 방향 사상이 최소 hypothesis다. Source/Target interface 구조는 자유롭다.

### 주의

- 이것이 binary edge schema를 뜻하지 않는다.
- 방향성만 남기고 모든 semantic typing을 없애자는 뜻도 아니다.
- runtime record 형식은 아직 기술 선택 대상이다.

---

## CHG-005 — `Relation Bundle` / `Closure Object`를 primitive에서 제거

### v1.0

여러 관계가 국소 Closure/Bundle을 이루고 다시 다른 Composition에 참여하는 구조가 핵심이었다.

### v2.0

해당 능력은 다음으로 재표현한다.

```text
RELATION + RELATION → RELATION

FOLD(composition)
→ composable Relation / VIEW / CONTROL / STATE handle
```

### 이유

`Bundle`은 물리적 상자·계산 경계를 암시했고, `Closure`는 finality 또는 독립 object처럼 오해될 수 있었다.

### Migration

| 기존 용어 | 신규 의미 |
|---|---|
| Relation Bundle | folded Relation Composition / 관계구성 설명용 별칭 |
| Closure | 특정 View 아래 Composition을 interface/handle로 접는 capability |
| Bundle boundary | NOT recompute boundary |
| Higher Bundle | recursively composed/folded Relation |

---

## CHG-006 — `View` 결과물 의미 제거

### v1.0

ViewSpec, ViewRun, ViewResult를 분리했다.

### v2.0

```text
VIEW:X  = 관점/필터/조건/라우팅/해상도/구성 작용
STATE:X = 그 View 아래 성립한 상태
```

View는 target/result가 아니다.

### Migration

| v1.0 | v2.0 |
|---|---|
| `ViewSpec` | `VIEW:X` definition/version candidate |
| `ViewRun` | Execution/Replay envelope; World Model primitive 아님 |
| `ViewResult` | `STATE:X` candidate |
| `ViewSnapshot` | versioned `STATE:X` or operational snapshot |

실제 one-to-one mapping은 아직 formalization open이다.

---

## CHG-007 — `Composite View` 타입 제거

### v1.0 / 초기 채널

View Composition, Composite View, View Bundle을 별도 명칭으로 검토했다.

### v2.0

```text
VIEW + VIEW → VIEW
```

View는 애초에 recursive composition이 가능하다. 내부 Composition이 중요할 때만 펼친다.

---

## CHG-008 — `CONTROL`을 `VIEW`와 분리

### 이전 혼동

Control을 View 조건 또는 단순 State 변화에 흡수하려는 제안이 있었다.

### v2.0

```text
VIEW    = observational / configurational
CONTROL = transformational / steering
```

둘 다 relation-composition abstraction이지만 역할이 다르다.

### Migration

- weight, threshold가 결과의 관점·선택을 바꾸면 VIEW 내부일 수 있다.
- 실제 State/View/Control을 의도적으로 변화시키는 작용은 CONTROL이다.
- runtime resource tuning이 의미를 바꾸지 않으면 Execution config다.

---

## CHG-009 — `Intervention` primitive 보류

### v1.0 / 초기 연구

Intermediate Intervention이 주요 capability로 사용됐다.

### v2.0

`Intervention`은 causal `do()` semantics를 암시할 수 있어 kernel primitive로 두지 않는다.

### 대체

```text
CONTROL
+ scope
+ branch
+ replay
+ measurement
```

필요한 controllability는 그대로 유지한다.

---

## CHG-010 — `STATE` 신설·강화

### v1.0

State가 여러 operational record 중 하나였고 ViewResult가 중심이었다.

### v2.0

State는 선행 Relation Composition을 암묵적으로 생략한 addressable holding state다.

```text
STATE:X
```

만 독립적으로 참조할 수 있다. 단, 독립 ontology object라는 뜻은 아니다.

---

## CHG-011 — `Subject` role 도입

`Subject`는 View가 현재 향하는 역할명이다. 고정 type이 아니다. 이름은 provisional이다.

---

# II. COMPOSITION AND ABSTRACTION CHANGES

## CHG-012 — FOLD와 VIEW를 분리

### 이전

abstraction, collapse, omission, View가 혼용될 위험이 있었다.

### v2.0

```text
FOLD/OMIT = 의미 보존 표현 축약
VIEW      = 선택·구성·구별에 따라 다른 State를 성립시키는 작용
CONTROL   = 의도적 변화
```

이 구분은 명시적 protocol에서 강제한다.

---

## CHG-013 — Resolution을 VIEW로 이동

### 이전

Relation/Bundle 자체가 resolution 속성을 가진다는 표현이 있었다.

### v2.0

```text
VIEW:LOW  → A→D
VIEW:HIGH → A→B→C→D
```

Resolution은 어떻게 펼쳐 보는지의 문제다.

---

## CHG-014 — 단일 `Maximum Resolution` 가정 제거

### 이전

maximum-resolution reference가 하나의 궁극 구조로 읽힐 여지가 있었다.

### v2.0

`Higher Resolution Reconstruction`은 View·evidence·budget-relative다. 다른 View에서 다른 고해상도 Composition이 나올 수 있다.

---

## CHG-015 — Reconstruction은 단일 inverse가 아님

### 신규 규칙

```text
A→D
EXPAND
├─ A→B→D
├─ A→C→D
└─ UNKNOWN
```

복수 후보, exact/inferred/unknown을 허용한다.

### 영향

- View는 일반적으로 invertible하지 않다.
- provenance/replay와 inference를 구분해야 한다.
- candidate explosion control이 필요하다.

---

## CHG-016 — Composition order 기본 보존

```text
A then B != B then A
```

commutative law는 operator별로 검증·선언한다.

---

## CHG-017 — FOLD grouping의 표현적 associativity

단순 접기라면 grouping 위치가 의미를 바꾸지 않는다. grouping이 결과를 바꾸면 다른 actual Composition이다.

---

## CHG-018 — Identity Relation 추가

```text
ID_A : A → A
```

합성 중립 Relation을 허용한다. endpoints가 같다는 이유만으로 ID로 판정하지 않는다.

---

## CHG-019 — Endpoint identity rule 폐기

같은 Source/Target이어도 내부 path가 다르면 다른 Relation일 수 있다.

---

## CHG-020 — View-relative equivalence 도입

어떤 View에서 구별되지 않는 것과 실제 identity를 병합하는 것을 분리한다.

---

## CHG-021 — Multi-valued Relation 허용

Relation을 deterministic function으로 제한하지 않는다. 다만 AND/OR/fan-out/route를 primitive로 즉시 고정하기보다 high-resolution topology로 복원한다.

---

# III. COMPUTATION AND RUNTIME CHANGES

## CHG-022 — Partial recompute를 Core goal로 승격

v1.0의 incremental update 요구를 다음처럼 강화한다.

```text
MINIMUM NECESSARY RECOMPUTE
= architectural objective
```

관계단위 change propagation과 demand-driven deepening이 핵심이다.

---

## CHG-023 — Recompute boundary 동적화

Bundle/State/View handle boundary를 물리 계산 경계로 고정하지 않는다. operator dependency와 delta semantics가 실제 영향 범위를 정한다.

---

## CHG-024 — Partial/full adaptive fallback

부분 계산이 항상 더 빠르거나 안전하다고 가정하지 않는다.

```text
fine incremental
→ affected operator full recompute
→ region recompute
→ global recompute
```

중 가장 낮은 비용과 충분한 correctness를 제공하는 경로를 고른다.

---

## CHG-025 — Intermediate는 Lazy + Promotable

모든 B1/B2/B3를 상시 materialize하는 요구를 제거한다. 필요할 때 재구성·승격한다.

---

## CHG-026 — Adaptive abstraction depth

고정 depth가 아니라 중요도·불확실성·risk·budget에 따라 필요한 구간만 더 펼친다.

---

## CHG-027 — Dynamic pattern 지원

Cycle이 fixpoint를 만들지 않아도 oscillation/divergence pattern을 `STATE:Pattern`으로 관측하고 다시 Composition에 넣을 수 있다.

---

# IV. EXPERIMENT/GOVERNANCE CHANGES

## CHG-028 — Branch by default 명시

Control은 원본 overwrite 대신 branch를 기본으로 한다.

---

## CHG-029 — AI exploration capability 확대

AI는 proposal뿐 아니라 sandbox branch 생성·실행·측정까지 할 수 있다.

---

## CHG-030 — Promotion capability와 authority 분리

AI가 후보를 만들 수 있다는 사실은 자동 승격 권한을 뜻하지 않는다. Gate policy가 필요하다.

---

## CHG-031 — Scoped Control 공식화

Control의 target뿐 아니라 scope를 별도로 표현한다.

---

## CHG-032 — Replay envelope 확장

Data와 View version뿐 아니라 Control, model/adapter/latent target, runtime dependency, branch/promotion policy, measurements를 포함한다.

---

# V. RETAINED FROM v1.0

다음은 v2.0에서도 유지한다.

## KEEP-001 — Non-final model stance

어떤 View/State/Relation Composition도 Final Ontology로 자동 승격하지 않는다.

## KEEP-002 — Multi-strategy comparison

동일 input/snapshot에서 여러 View·runtime·policy 후보를 비교한다.

## KEEP-003 — Versioning / Replay / Audit

semantic version, run envelope, lineage, migration, rollback을 유지한다.

## KEEP-004 — Authority boundary

Principal, grant, policy, authorization, signing, execution을 합치지 않는다.

## KEEP-005 — Evidence / Semantic / Governance / Execution / Evaluation plane separation

World Model kernel이 작아져도 operational constitution은 유지한다.

## KEEP-006 — Evolution openness with governance

변화를 표현할 수 있음과 무제한 self-modification 권한은 다르다.

## KEEP-007 — Persona/Object/System non-finality

Persona·Agent·Object·System은 특정 View에서 나타난 State/Manifestation일 수 있고 Core primitive로 고정하지 않는다.

## KEEP-008 — split/merge/mutation derived labels

Core primitive로 선행 정의하지 않는다.

---

# VI. MOVED OUT OF THE WORLD-MODEL KERNEL

| 개념 | 신규 위치 | 이유 |
|---|---|---|
| `Principal` | Governance plane | authority invariant 필요 |
| `AuthorityGrant` | Governance plane | View-relative identity로 취급 금지 |
| `ActionProposal/Authorization/Execution` | Execution plane | operational separation 필요 |
| `EvidenceItem/SourceRecord` | Evidence plane | ingress typed contract 필요 |
| `ViewRun` | Execution/Replay envelope | View 자체와 run 분리 |
| `Measurement` | Evaluation plane | State 내부 본질 속성으로 고정 금지 |
| `Incident/Rollback` | Audit/Operations | runtime governance |
| `Model/Adapter Version` | Execution/Latent adapter envelope | reproducibility |

이동은 중요도 감소가 아니다. **World Model의 최소 ontology와 제품 운영 계약을 분리**하는 것이다.

---

# VII. REMOVED / DEFERRED TERMS

| 용어 | 상태 | 설명 |
|---|---|---|
| Reality | REMOVE FROM CORE | Owner correction |
| Source View | REMOVE | View는 필터 자체이며 source/result가 아님 |
| Derived View | REMOVE | 모든 View는 그냥 VIEW |
| View Result | REPLACE | STATE |
| Claim | REMOVE AS KERNEL UNIT | domain statement로만 가능 |
| Reading | DEFER/ABSORB | View composition으로 처리 가능 |
| Relation Bundle | REMOVE AS PRIMITIVE | recursive composition/fold로 대체 |
| Composite View | REMOVE AS TYPE | VIEW가 본래 composable |
| View Composition | OMIT AS ROUTINE NOUN | 내부 구조 설명에만 사용 |
| Intervention | DEFER | CONTROL로 capability 보존 |
| Closure Object | REMOVE | Closure capability로 재정의 |
| Attribute primitive | DEFER | folded relation notation |
| Delta primitive | REPLACE | VIEW:DELTA / STATE:DELTA |
| Maximum Resolution | REPLACE | View-relative higher resolution |

---

# VIII. MIGRATION GUIDE

## 1. 문서 문장 변환 예

### Old

```text
SourceRecord에서 RelationAssertion을 추출하고 ViewSpec을 실행해 ViewResult를 만든다.
```

### New

```text
Evidence/Data layer가 제공한 Subject에 VIEW:X를 적용해 STATE:X를 성립시킨다.
필요하면 VIEW:X와 STATE:X의 내부 Relation Composition 및 evidence lineage를 펼친다.
```

### Old

```text
R1 + R2 + R3 → Relation Bundle B1
```

### New

```text
r1 ; r2 ; r3 → r*

또는 역할에 따라
VIEW:X / CONTROL:X / STATE:X로 접어 표현
```

### Old

```text
View를 좁혀 Relation을 삭제한다.
```

### New

```text
VIEW:X가 어떤 관계 구별을 드러내지 않아 STATE:X에서 보이지 않게 된다.
원본 State를 의도적으로 바꾸는 경우는 CONTROL:Y로 별도 표현한다.
```

### Old

```text
Delta가 Relation을 바꾼다.
```

### New

```text
CONTROL 또는 operational change로 STATE가 달라진다.
두 State의 차이는 VIEW:DELTA를 통해 STATE:DELTA로 관측한다.
```

---

## 2. 구현 schema migration 원칙

아직 구현을 승인하지 않는다. 향후 prototype에서는 다음을 지킨다.

```text
DO NOT
- v2.0 용어를 곧바로 단일 database schema로 freeze
- every relation = one graph edge로 축소
- View/Control/State를 endpoint 이름만으로 canonicalize
- folded relation을 항상 fully materialize
- inference reconstruction을 exact lineage처럼 저장

DO
- backend-independent Relation IR contract
- explicit discriminator for VIEW / CONTROL / STATE
- composition identity and interface refs
- lazy fold/expand
- branch and replay envelope
- delta dependency hooks
- operational governance types outside minimal kernel
```

---

# IX. RISK CHANGES

## New risks introduced by v2.0

1. **Over-general relation kernel:** 모든 것이 Relation이라는 말이 operational type safety를 약화시킬 수 있다.
2. **Hidden composition ambiguity:** 접힌 Relation의 내부 path가 여러 개일 수 있다.
3. **Candidate explosion:** reconstruction·alternate View가 지수적으로 늘 수 있다.
4. **Equivalence leakage:** View-relative equivalence가 실제 identity merge로 오용될 수 있다.
5. **Fold/View confusion:** 의미 보존 축약과 semantic abstraction을 구현이 혼동할 수 있다.
6. **State identity ambiguity:** 같은 관계내용·다른 lineage의 State canonicalization이 어렵다.
7. **Incremental metadata cost:** 최소 계산을 위해 dependency/provenance 저장 비용이 커질 수 있다.
8. **Back-action boundary:** 일부 관측은 Subject를 바꾸므로 View/Control 경계가 흐릴 수 있다.
9. **Latent control instability:** model/version/context에 따라 같은 Control 효과가 변할 수 있다.

## Risks reduced from v1.0

1. Claim/Assertion ontology를 너무 일찍 고정할 위험 감소.
2. Relation Bundle을 물리적 object로 오해할 위험 감소.
3. View와 ViewResult 혼동 감소.
4. Resolution을 본질 property로 고정할 위험 감소.
5. 자동 inverse/reconstruction 과신 감소.
6. View와 Control을 분리해 write-back 사고 위험 감소.
7. minimum recompute 목표가 더 명확해짐.

---

# X. REVISION ACCEPTANCE CONDITIONS

v2.0은 다음 조건에서 연구 baseline으로 채택할 수 있다.

```text
- Owner-confirmed decisions와 충돌하지 않는다.
- 기존 governance/safety plane을 삭제하지 않는다.
- common probe에서 최소 Relation + Composition이 표현력을 보인다.
- FOLD / VIEW / CONTROL separation이 구현 가능하다.
- reconstruction candidate와 uncertainty를 추적할 수 있다.
- relation-level delta propagation이 전체 계산보다 유의미한 절약을 만든다.
- backend 교체 후에도 동일 fixture를 replay할 수 있다.
```

현재 판정:

```text
CHANGELOG_COMPLETE = YES
V2.0 OWNER APPROVAL = NOT YET
FORMAL SPEC = NOT YET
PROTOTYPE AUTHORIZED = NOT BY THIS DOCUMENT
```

---

# XI. PART B — v2.0 → v2.1 CANDIDATE SYNCHRONIZATION

| ID | Class | Change | Authority effect |
|---|---|---|---|
| SYNC-001 | STATUS/AUTHORITY | OWNER_CONFIRMED, CONFIRMED_DIRECTION/FORMALIZATION_OPEN, RETAINED_SAFETY_CONTRACT, PRO_MODE_PROPOSAL, OPEN 범례 추가 | 제안·Open의 Owner 결정 승격 방지 |
| SYNC-002 | SEMANTIC GUARD | `RELATION + RELATION → RELATION`을 admissibility가 허용한 composition closure로 한정 | OPEN-05/Q-016 미결 보존 |
| SYNC-003 | SEMANTIC GUARD | FOLD를 role assignment 및 State formation과 분리 | OD-060 및 `FOLD != VIEW != CONTROL` 정합화 |
| SYNC-004 | STATUS | EXACT 설명을 working example로 낮추고 Q-091/Q-092에 연결 | exactness level 미결 보존 |
| SYNC-005 | TERMINOLOGY | Candidate `0..3`을 `A..D`로 통일 | 기술 선택 없음 |
| SYNC-006 | REFERENCE | Canonical Probe/metric registry를 R4의 `P01..P20`으로 단일화 | R1의 17개 표는 executive subset |
| SYNC-007 | REFERENCE | R1/R4의 로컬 `[Rxx]` 충돌을 문서별 namespace로 명시 | 외부연구 재검증 없음 |
| SYNC-008 | TERMINOLOGY | composition closure, fixed-point closure, working product label을 구분 | OPEN-10 보존 |
| SYNC-009 | TERMINOLOGY | uppercase SOURCE/TARGET 역할과 evidence origin을 구분; runtime DELTA를 relation change로 표기 | kernel/runtime 혼동 제거 |
| SYNC-010 | STATUS/AUTHORITY | Toolkit contract, falsification criteria, INIT capability를 Pro-mode proposal로 명시 | Q-175/Q-178 선결 금지 |
| SYNC-011 | EVIDENCE | missing-source 문구를 inherited historical note / not broadly reverified로 정정 | 읽지 않은 자료 주장 방지 |
| SYNC-012 | LEDGER | Q-001..Q-180에 disposition을 추가하되 질문 ID와 Open 의미 보존 | Open 해결 0 |

## v2.1 candidate 판정

```text
V1.0_TO_V2.0_BREAKING_HISTORY = PRESERVED
V2.0_TO_V2.1_NEW_OWNER_DECISION = NONE
V2.0_TO_V2.1_NEW_RESEARCH_CLAIM = NONE
OPEN_ITEMS_RESOLVED = NONE
OWNER_ACCEPTANCE = PENDING
IMPLEMENTATION_AUTHORIZATION = NONE
TECHNOLOGY_FREEZE = NONE
```
