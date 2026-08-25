# ASA CORE WORLD MODEL / CLOSURE PROTOCOL v2.1 — SYNCHRONIZATION CANDIDATE

```text
STATUS = V2.1_CANDIDATE / OWNER_REVIEW_PENDING / NON_FROZEN
PROJECT = AAA / BYUL
PRODUCT = ASSET AGENT ASA
PURPOSE = ASA INIT / PERSONA ORCHESTRATION RESEARCH
REVISION_MODE = BOUNDED SYNCHRONIZATION OF THE V2.0 RESEARCH PACKET
DATE_KST = 2026-08-26
IMPLEMENTATION_AUTHORIZATION = NONE
FINAL_ONTOLOGY_CLAIM = NONE
TECHNOLOGY_FREEZE = NONE
OPEN_ITEMS_RESOLVED_BY_THIS_REVISION = NONE
```

---

## 0. 문서 판정

이 문서는 v2.0의 연구 내용을 다시 연구하거나 새 이론으로 교체하지 않는다.
v2.0에서 발생한 상태·권한·용어·후보 ID·Probe·참조 drift를 보정한
`v2.1 CANDIDATE`다. v1.0→v2.0의 breaking 의미는 그대로 보존하며,
Owner의 별도 수락 전에는 Final/Active/Frozen 상태가 아니다.

### 0.0 상태 범례

| 태그 | 의미 |
|---|---|
| `OWNER_CONFIRMED` | Owner가 직접 확정한 내용 |
| `CONFIRMED_DIRECTION / FORMALIZATION_OPEN` | 방향은 확정됐지만 정확한 법칙·interface는 미결 |
| `RETAINED_SAFETY_CONTRACT` | v1.0에서 유지된 governance·safety 경계 |
| `PRO_MODE_PROPOSAL` | 연구 권고 또는 시험 후보; Owner 결정 아님 |
| `OPEN` | 아직 해결되지 않은 질문 |

기존 v1.0의 다음 강점은 유지한다.

- Core는 정답 저장소가 아니라 교체 가능한 연구·실행 도구다.
- 여러 View·모델·실행전략을 같은 조건에서 비교할 수 있어야 한다.
- lineage, replay, audit, versioning, migration, governance를 보존해야 한다.
- Principal, Authority, Policy, Action, Signing, Deletion 등 운영상 중요한 구분은 의미론적 최소화 때문에 제거하면 안 된다.
- Evolution 가능성과 무제한 자율변경 권한은 다르다.

반면 v1.0의 `Reality / Source / Claim / AssertionFrame / ViewSpec-Run-Result` 중심 World Model kernel은 이번 채널의 Owner 결정과 일치하지 않는다. 해당 개념들은 필요하면 **Evidence·Governance·Execution layer의 도메인 계약**으로 남을 수 있으나, World Model의 최소 primitive로 고정하지 않는다.

### 0.1 자료 복구 주의

요청된 정확한 파일명
`BYUL_CLOSURE_TOOLKIT_CORE_COMBINATION_NEXT_CHANNEL_PACKET_2026-08-24.md`는
현재 6개 primary source set에 없다. v2.0의 복구 기록은 당시 연결된
인덱스와 저장소에서 발견하지 못했다고 보고했다. 이번 v2.1 동기화는
그 전체 검색을 반복하지 않았으므로, 이 상태를 `NOT_RECOVERED /
HISTORICAL_NOTE_NOT_BROADLY_REVERIFIED`로 보존한다.

현재 source precedence는 다음과 같다.

```text
1. 이번 채널에서 Owner가 직접 승인한 결정
2. BYUL 프로젝트 목적·기존 Owner confirmation 기록
3. ASA Core Worldview v1.0 및 Revision Report의 운영·안전 계약
4. 최신 외부 연구
5. 본 문서의 Pro-mode 추론과 제안
```

Owner confirmation과 Pro-mode 제안은 문서 안에서 구분한다.

---

# I. EXECUTIVE VERDICT

## 1. 핵심 전환

기존 질문은 대략 다음과 같았다.

```text
어떤 Relation Bundle / Closure Object를 저장할 것인가?
```

이번 채널에서 더 작은 질문으로 수렴했다.

```text
현재 해상도에서 보이는 방향 사상을 최소 Relation으로 두고,
복잡성은 Relation Composition으로 표현하며,
필요하지 않은 중간 Composition은 접고,
필요할 때 View-relative하게 다시 펼칠 수 있는가?
```

이 전환에 따라 ASA Core의 중심은 특정 graph, database, ontology가 아니라 다음 능력이다.

```text
COMPOSE
FOLD
EXPAND / RECONSTRUCT
APPLY VIEW
APPLY CONTROL
ADDRESS STATE
TRACE / REPLAY
PROPAGATE MINIMAL CHANGE
BRANCH / COMPARE / PROMOTE
MEASURE
```

## 2. 한 문장 정의

> **ASA Core World Model v2.1 Candidate는 현재 View 해상도에서 보이는 방향성 Relation을 최소 단위로 두고, 허용 가능한 관계구성을 재귀적 Composition으로 만들고 다시 Relation처럼 접어 사용하며, VIEW·CONTROL·STATE라는 역할별 표면 추상화 아래 필요한 부분만 관측·제어·복원·재계산할 수 있게 하는 교체 가능한 연구 프로토콜 후보다.**

## 3. 이 개정이 주장하지 않는 것

```text
MINIMAL RELATION KERNEL
!=
세상에 실제로 오직 한 종류의 존재만 있다는 형이상학적 주장

EVERYTHING CAN BE REPRESENTED RELATIONALLY
!=
모든 운영 구분을 하나의 무타입 edge로 저장해도 안전하다는 주장

HIGHER RESOLUTION
!=
하나의 유일한 절대 세계 구조

FOLDABLE
!=
항상 정확히 역복원 가능

VIEW-RELATIVE EQUIVALENCE
!=
법적·권한·보안 identity도 View마다 임의로 바뀐다는 뜻

AI CAN EXPLORE
!=
AI CAN PROMOTE OR DEPLOY WITHOUT A GATE
```

---

# II. MINIMAL RELATION PROTOCOL

## 4. Relation의 최소 정의

현재 강한 Owner-confirmed hypothesis:

```text
RELATION r : SOURCE → TARGET
```

여기서 Source와 Target은 존재 종류가 아니라 **현재 Relation 안에서의 방향적 역할**이다.

- Source/Target의 내부 형태와 수는 자유롭다.
- 한 항목, 복수 interface, STATE, VIEW, CONTROL, 다른 Relation 또는 접힌 Composition이 참여할 수 있다.
- `A → B`는 함수일 수도 있지만, Relation 전체를 deterministic function으로 제한하지 않는다.
- 같은 endpoints를 가진 Relation도 성립 경로·Composition·역할이 다르면 서로 다른 identity를 가질 수 있다.

### 4.1 현재 해상도에서의 최소성

`A → D`가 보인다고 해서 내부적으로 원자적이라는 뜻은 아니다.

```text
LOWER RESOLUTION
A ─────────────→ D

HIGHER RESOLUTION CANDIDATE
A → B → C → D
```

Relation의 최소성은 “더 이상 분해할 수 없음”이 아니라:

> **현재 View와 현재 목적에서 하나의 방향 사상으로 취급한다.**

라는 operational minimality다.

## 5. Composition closure

```text
IF ADMISSIBLE(r2, r1):
  COMPOSE(r2, r1) → RELATION
```

`[CONFIRMED_DIRECTION / FORMALIZATION_OPEN]` 선언된 interface와 아직
미결인 admissibility contract가 합성을 허용할 때, 합성 결과도 다시
Relation처럼 다른 Composition에 참여할 수 있다. 이 문서는
`OPEN-05 / Q-016`의 witness·typing rule을 해결하지 않는다.

```text
r1 : A → B
r2 : B → C

r2 ∘ r1 : A → C
```

더 복잡한 경우도 표면에서는 접을 수 있다.

```text
A → B → C → D

FOLD
A ─r*→ D
```

### 5.1 Composition continuity

명시적 고해상도 Composition에서는 연결 interface가 이어져야 한다.

```text
A → B
B → C
```

표면적으로 `A → B`와 `C → D`가 직접 이어진 것처럼 보인다면 즉시 오류 또는 임의 연결로 간주하지 않는다. 그 사이에 생략된 관계가 있을 수 있다.

```text
A → B → [omitted composition] → C → D
```

고해상도 복원 시 가능한 범위에서 continuity를 회복한다. 복원할 근거가 없는데 arbitrary mapping을 만들어내는 것은 허용하지 않는다.

## 6. Identity Relation

의미적으로 아무 변화도 만들지 않는 중립 Relation을 허용한다.

```text
ID_A : A → A

r ∘ ID = r
ID ∘ r = r
```

단, `Source = Target`이라고 해서 자동으로 Identity는 아니다. 내부 작동 후 현재 View에서 같은 State로 보일 수도 있다.
어느 View·scope에서 중립이어야 하는지와 formal identity law의 정확한
범위는 `Q-010`에 남아 있다.

## 7. Composition laws

### 7.1 순서

기본값은 non-commutative다.

```text
A then B
!=
B then A
```

순서를 바꿔도 의미가 같다는 것이 검증된 operator에만 commutative law를 선언한다.

### 7.2 접기의 결합성

**단순 FOLD 위치**는 의미를 바꾸지 않아야 한다.

```text
A → B → C

[AB] → C
A → [BC]
[ABC]
```

위 차이가 표기 축약뿐이라면 같은 Composition이다. 중간 결합의 방식 자체가 State를 다르게 만든다면 그것은 FOLD가 아니라 서로 다른 실제 Composition이다.

### 7.3 Relation identity

다음 둘은 endpoints가 같아도 다를 수 있다.

```text
r1 : A → B → D
r2 : A → C → D
```

따라서 endpoint equivalence는 Relation identity의 충분조건이 아니다.

## 8. View-relative equivalence

```text
VIEW:LOW
r1 ≈ r2

VIEW:HIGH
r1 ≠ r2
```

어떤 View에서 구별되지 않는다는 이유로 underlying identity를 영구 병합하지 않는다. 저해상도 계산에서는 같은 class처럼 취급할 수 있지만, 필요한 경우 다시 분리할 수 있어야 한다.

---

# III. SURFACE PROTOCOL: VIEW / CONTROL / STATE / SUBJECT

Relation은 너무 넓은 상위 개념이므로 일상 프로토콜에서 매번 `RELATION:`이라고 표기하지 않는다. 어떤 역할로 접혀 있는지 보여주는 discriminator를 사용한다.

## 9. VIEW:X

```text
VIEW:X
= 어떻게 볼 것인가
= 관점 / 조건 / 필터 / 선택 / 라우팅 / 해상도 / 구성
= 보는 역할의 Relation Composition을 접은 표면 추상화
```

View는 본질적으로 composable하다.

```text
VIEW:A + VIEW:B → VIEW:AB
VIEW:AB + VIEW:C → VIEW:ABC
```

`Composite View`라는 별도 존재 종류를 만들지 않는다. 결과도 그냥 `VIEW`다. 내부 chain, parallel, route, condition, recursion은 필요할 때만 펼친다.

## 10. CONTROL:X

```text
CONTROL:X
= 무엇을 어떻게 바꿀 것인가
= 의도적 변환 / 조절 / steering 역할의 Relation Composition
```

View와 Control은 모두 relational composition이지만 역할은 구분한다.

```text
VIEW
= observational / configurational

CONTROL
= transformational / steering
```

Control도 재귀적으로 조합 가능하다.

```text
CONTROL:A + CONTROL:B → CONTROL:AB
```

가중 조합은 의미가 정의되는 Control에만 허용한다. 삭제·금지·권한 부여처럼 discrete semantics를 가진 Control에 임의 가중합을 적용하지 않는다.

## 11. STATE:X

```text
STATE:X
= 현재 어떻게 성립해 있는가
= 선행 Relation Composition을 암묵적으로 생략한 상태 handle
```

State는 독립적인 최종 Object ontology가 아니다. 그러나 내부를 전부 펼치지 않고도 독립적으로 address할 수 있다.

> **STATE is independently addressable, not independently ontological.**

복원이나 원인 추적이 필요 없다면 `STATE:X`만 단독 참조할 수 있다.

```text
STATE:A
   ↓ VIEW:B
STATE:B
```

## 12. VIEW:X ↔ STATE:X naming pair

```text
VIEW:Persona
STATE:Persona
```

같은 suffix는 View와 그 View 아래 성립한 State의 대응 관계를 읽기 쉽게 한다. 그러나 두 identity는 discriminator로 분리한다.

같은 View를 여러 Subject·시점·Branch에 적용할 수 있으므로 실제 identity는 별도다.

```text
VIEW:Persona@v3
STATE:Persona@run17
STATE:Persona@run18
```

`VIEW:X ↔ STATE:X`가 항상 one-to-one이라는 뜻은 아니다. 이는 open formalization issue다.

## 13. SUBJECT

`Subject`는 현재 View가 향하는 것의 역할명이다. 고정 타입이 아니다.

```text
SUBJECT = STATE:A
VIEW:B
→ STATE:B
```

Source, Target, Input, Output 역시 relation-local role이며 고정 ontology class로 두지 않는다.

## 14. DELTA

Delta를 별도 최상위 primitive로 만들지 않는다.

```text
STATE:A@1 ─┐
            ├─ VIEW:DELTA → STATE:DELTA
STATE:A@2 ─┘
```

- `VIEW:DELTA` = 차이를 보는 방식
- `STATE:DELTA` = 그렇게 보았을 때 성립한 차이 상태

CONTROL은 바꾸는 작용이고, DELTA는 그 차이를 보는 View/State이므로 서로 동일하지 않다.

## 15. ATTRIBUTE

Attribute는 별도 원시 의미론으로 고정하지 않는다.

```text
X.weight = 0.7
```

은 필요에 따라 다음과 같은 Relation Composition을 접은 surface notation일 수 있다.

```text
X → ... → weight → 0.7
```

중요해지면 다시 펼친다. 단, `ABSENT`, `OMITTED`, `UNKNOWN`은 서로 섞으면 안 된다.

---

# IV. FOLD, VIEW, CONTROL의 명시적 구분

## 16. FOLD / OMIT

```text
FOLD / OMIT
= 의미 보존적인 표현 축약
= 중간 Relation을 현재 표면에서 쓰지 않음
```

```text
A → B → C → D
≡
A → D
```

이라고 쓸 수 있는 것은 중간을 표기하지 않았을 뿐일 때다.

## 17. VIEW

View는 단순 생략이 아니다. 어떤 관계를 선택·구성·구별·추상화할지 바꾸므로 다른 State가 성립할 수 있다.

```text
SUBJECT
  ↓ VIEW:A
STATE:A

SUBJECT
  ↓ VIEW:B
STATE:B
```

## 18. CONTROL

Control은 의도적으로 State, View 또는 다른 Control의 성립 방식을 바꾼다.

```text
STATE:A
  ↓ CONTROL:X
STATE:A'
```

명시적 protocol에서는 세 가지를 혼동하지 않는다.

```text
FOLD  = 표현 축약
VIEW  = 관측·구성 차이
CONTROL = 의도적 변화
```

---

# V. RESOLUTION AND RECONSTRUCTION

## 19. Resolution은 VIEW의 역할

해상도를 Relation 자체의 본질 속성으로 고정하지 않는다.

```text
VIEW:LOW
A → D

VIEW:HIGH
A → B → C → D
```

두 표현은 경쟁하는 ontologies가 아니라, 같은 또는 관련 관계구성을 서로 다른 View로 본 결과일 수 있다.

## 20. 최대 해상도 세계를 가정하지 않는다

`High Resolution`은 다음을 뜻한다.

> **현재 View, evidence, computation budget 아래에서 가능한 한 생략을 줄여 복원한 관계구성.**

다른 View에서는 다른 고해상도 구성이 나타날 수 있다.

```text
VIEW:X high-resolution
A → B → C → D

VIEW:Y high-resolution
A → P → Q → D
```

어느 하나를 자동으로 Final Ontology로 승격하지 않는다.

## 21. Reconstruction result

저해상도 Relation을 펼칠 때 단일 경로를 임의 생성하지 않는다.

```text
A → D

EXPAND
├─ A → B → D
├─ A → C → D
└─ A → E → F → D
```

복원은 여러 후보를 반환할 수 있다.

정확성 표시는 적어도 다음 차이를 보존해야 한다.

```text
EXACT
= 예: 기록된 입력·operator·version·path로 동일 결과를 재생하는 경우

INFERRED
= 일부 중간 관계를 주변 정보로부터 추정

UNKNOWN
= 현재 정보로 신뢰 가능한 상세화를 제공할 수 없음
```

이 구분을 Relation annotation, reconstructed State, reconstruction run envelope 중 어디에 둘지는 아직 formalization open issue다.
`EXACT`의 byte/path/semantic 수준 역시 `OPEN-02 / Q-091 / Q-092`에서
미결이며, 위 문구는 working example이지 최종 정의가 아니다.

## 22. Promotable intermediate

모든 중간 State를 항상 materialize하지 않는다.

```text
평소
A ─────────────→ D

필요 시
A → B? → C? → D
       ↑
중간을 재구성하고 addressable State로 승격
```

Owner-confirmed default:

> **Checkpoint 중심으로 계산하되, 필요해진 intermediate를 replay/reconstruction으로 생성해 그 시점부터 관측·측정·Control 가능한 State로 승격한다.**

## 23. Inferred State의 재사용

추정 복원된 intermediate도 다음 Composition에 참여할 수 있다. 단, 불확실성 lineage를 잃지 않는다.

```text
STATE:B? + VIEW:C → STATE:C?
```

불확실성이 누적되면 자동 deepening을 요청할 수 있다.

## 24. Adaptive abstraction depth

Core는 평소 큰 추상화로 계산하고, 중요한 곳만 더 깊게 펼칠 수 있어야 한다.

Deepening trigger 후보:

- 작은 변화가 예상보다 큰 영향을 보임
- reconstruction confidence가 낮음
- 후보들 사이의 결과가 크게 갈림
- 새로운 View/State가 발생함
- risk 또는 authority 경계에 접근함
- latent Control의 off-target effect가 커짐

모든 자동 deepening에는 depth, compute, scope, time budget을 적용할 수 있어야 한다.

---

# VI. MINIMUM NECESSARY RECOMPUTE

## 25. 성능 옵션이 아니라 설계 목표

Owner-confirmed goal:

> **가용한 dependency evidence 아래 계산 범위를 최소화하는 것을 설계 목표로 삼는다.**

```text
- relation r2
+ relation r5

→ 실제 dependency impact 추적
→ 영향받았다고 판정된 최소 후보 구성만 갱신
→ 전체 State/View는 크게 달라질 수 있음
```

의미 변화의 크기와 계산량의 크기는 같을 필요가 없다.

## 26. Bundle/State boundary는 recompute boundary가 아니다

`STATE:X` 또는 접힌 관계구성이 하나의 handle로 보인다고 해서 전체를 무조건 다시 계산하지 않는다.

```text
FOLDED STATE BOUNDARY
!=
RECOMPUTE BOUNDARY
```

계산 경계는 가용한 dependency와 operator의 change semantics에 따라
동적으로 정한다. 이는 전역적으로 정확한 최소성 보장이 아니며,
`Q-111 / Q-114`의 dependency precision은 OPEN이다.

## 27. Incremental contract

각 operator/View/Control은 가능한 경우 다음을 제공한다.

```text
FULL(S) → T
INCREMENTAL_CHANGE(ΔS, cached/context) → ΔT
AFFECTS(ΔS) → impacted subgraph/circuit
FALLBACK → safe full recompute
```

부분 계산이 안전한지 증명·검증할 수 없으면 해당 영역만 full recompute한다. 전체 시스템의 full recompute는 마지막 fallback이다.

DBSP는 풍부한 query와 recursion을 delta stream으로 incrementalize하는 강한 runtime 부품이며, Demanded Abstract Interpretation은 cyclic dependency graph에서도 demand-driven + incremental evaluation을 결합할 수 있음을 보여준다. 그러나 모든 변화가 incremental하게 싼 것은 아니므로, 변화 영향이 큰 경우 recomputation과 incremental maintenance의 비용을 비교하는 adaptive policy가 필요하다. [R1-R05][R1-R06][R1-R15]

## 28. Lineage의 양방향 사용

같은 dependency structure를 두 방향으로 활용한다.

```text
BACKTRACE
어디서 왔는가?
→ reconstruction / replay / provenance

FORWARD IMPACT
어디에 영향을 주는가?
→ invalidation / minimal recompute / deletion propagation
```

단순 reverse lookup은 새 semantic Relation이 아닐 수 있다. 반대 방향에 고유한 변환 의미가 있을 때만 별도 Relation이다.

---

# VII. CONTROLLED EXPERIMENTATION

## 29. Branch by default

Control은 원본을 덮어쓰기보다 기본적으로 새로운 experimental lineage를 만든다.

```text
STATE:A ─────────→ STATE:B
   │
   └─ CONTROL:X → STATE:A' → STATE:B'
```

원본과 대안 State를 비교·재생할 수 있어야 한다.

## 30. Alternate Composition

같은 입력에서 여러 View/Composition 후보를 동시에 유지할 수 있다.

```text
SUBJECT
├─ VIEW:A → STATE:A
├─ VIEW:B → STATE:B
└─ VIEW:C → STATE:C
```

후보는 즉시 모두 materialize할 필요가 없다. Lazy candidate graph로 보존하고 정보이득·위험·budget에 따라 필요한 후보만 계산한다.

## 31. AI autonomous experiment branch

AI는 다음을 자동 수행할 수 있다.

```text
View / Control / Composition candidate 제안
→ sandbox branch 생성
→ 실행
→ 측정
→ 비교
→ promotion candidate 제출
```

AI는 원본을 직접 변경하지 않는다.

## 32. Promotion control

승격 권한은 고정 actor가 아니라 policy로 제어할 수 있어야 한다.

```text
human-only
specified AI allowed
predeclared condition-based
promotion prohibited
```

ASA INIT 기본값은 **승격 Gate required**다. AI의 실험 성공은 production/default path 승격과 동일하지 않다.

## 33. Scoped Control

같은 Control도 적용 범위가 다를 수 있다.

```text
Scope = one experiment
Scope = one View lineage
Scope = several Views
Scope = branch
Scope = operational source state
```

실험적 counterfactual과 실제 operational change를 구별한다.

## 34. Replay envelope

재현 가능한 실험은 최소 다음을 보존한다.

```text
subject/input snapshot refs
VIEW versions and expanded/folded composition refs
CONTROL versions and scope
model / adapter / latent target versions
randomness / decoding / tool outputs
runtime and dependency versions
branch / promotion policy snapshot
measurements
resulting STATE refs
```

외부 비결정성 때문에 byte-identical output을 항상 보장하지는 않지만, semantic/behavioral replay 수준을 명시해야 한다.

---

# VIII. CYCLES, DYNAMIC PATTERNS, AND NON-FINAL CLOSURE

## 35. Cycle 허용

```text
A → B → C → A
```

순환 자체를 오류로 보지 않는다. 다음 종료·관측 계약을 적용한다.

```text
STABLE
OSCILLATING
DIVERGING
BUDGET_STOP
UNKNOWN
```

## 36. Dynamic Pattern State

정적 fixpoint가 없더라도 반복 패턴을 `VIEW:Pattern`으로 관측하여
`STATE:Pattern-P`로 형성할 수 있다. FOLD는 그처럼 이미 역할과 관측
계약이 확립된 표현을 의미 보존적으로 생략할 뿐이며, STATE를 생성하지
않는다.

```text
A ↔ B ↔ A ↔ B ...
       ↓ VIEW:Pattern
STATE:Pattern-P
```

이 State도 다른 View/Control의 Subject가 될 수 있다.

```text
STATE:Pattern-P
   ↓ VIEW:X
STATE:X
```

`Closure != Finality`를 이 방식으로 유지한다.

## 37. Closure의 재지정

Closure는 별도 ontology primitive가 아니다.

> **특정 View와 scope에서 어떤 Relation Composition을 하나의 안정된 interface/handle로 접어 다음 Composition에 참여시키는 capability.**

따라서:

```text
Closure = local operational closing / folding
Closure != final truth
Closure != permanent object boundary
composition closure != Datalog/fixed-point closure
Closure capability = working product label; naming remains OPEN-10
```

---

# IX. PROPOSED CLOSURE TOOLKIT CONTRACT v0.2

`[PRO_MODE_PROPOSAL]` 기술에 독립적인 Tool contract 후보·superset이다.
`Q-178`의 Owner-approved minimum toolkit을 이 문서가 선결하지 않는다.

| Tool | 계약 |
|---|---|
| `compose` | 여러 directional Relation을 declared interfaces와 order로 합성한다. |
| `fold` | 이미 선언된 role과 의미를 보존하며 Composition 표현의 중간을 생략한다. FOLD 자체가 VIEW/CONTROL/STATE role을 생성하지 않는다. |
| `expand` | 접힌 handle의 내부 Composition 후보를 View·budget·evidence 조건 아래 펼친다. |
| `apply_view` | Subject에 VIEW를 적용해 대응 STATE를 성립시킨다. |
| `apply_control` | target과 scope에 CONTROL을 적용해 기본적으로 branch STATE/VIEW/CONTROL을 만든다. |
| `address` | materialized 또는 reconstructed intermediate를 stable handle로 참조한다. |
| `trace` | backward lineage와 derivation evidence를 반환한다. |
| `impact` | relation-level delta의 downstream 영향을 계산한다. |
| `delta_update` | 지원 가능한 operator에서 최소 변화분만 갱신한다. |
| `replay` | recorded envelope로 execution/semantic state를 재생한다. |
| `compare` | View-relative equivalence, Delta, metrics를 계산한다. |
| `propose` | AI/algorithm이 View·Control·Composition·reconstruction 후보를 생성한다. |
| `branch` | 원본을 보존한 대안 lineage를 만든다. |
| `promote` | policy gate를 통과한 후보만 default/release path로 이동한다. |
| `measure` | controllability, observability, reconstruction, cost, side effects를 계측한다. |

### 37.1 Contract가 보존해야 할 메타정보

모든 것을 필드로 강제하지는 않지만 다음은 필요할 때 복원 가능해야 한다.

```text
identity / interface
composition order and topology
View / Control role
scope and branch
version
lineage / evidence
fold witness or equivalence condition
reconstruction status
runtime dependency
measurements
```

---

# X. EXTERNAL RESEARCH RE-INTERPRETATION

## 38. 기술은 Core 정답이 아니라 부품

| 연구군 | v2.0에서의 위치 |
|---|---|
| Category theory / operads / wiring diagrams | `Source→Target`, interface compatibility, identity, recursive nesting, composition law를 시험하는 reference algebra |
| Nested relational calculus | 접힌 nested State와 nested transformation의 reference representation |
| Datalog / Soufflé | recursive closure와 fixed-point rule evaluation의 runtime/reference engine |
| DBSP / IVM / differential dataflow | relation-level delta propagation과 minimum recompute runtime |
| Higher-order graph / hypergraph | Relation-on-Relation, composite interface, polyadic high-resolution structure의 reference/storage candidate |
| Rewriting Logic / Maude | CONTROL, event/protocol, cycle, branching state-space의 executable oracle |
| Graph rewriting | intermediate structural CONTROL과 local replacement semantics |
| E-graph / egglog | alternate composition 후보와 scoped equivalence 탐색 sidecar |
| Relational lenses | 명시적 bidirectional write-back 계약. 일반 View의 자동 inverse가 아님 |
| Provenance / semirings | compact derivation circuit, replay, deletion impact, reconstruction evidence |
| Abstract interpretation / demanded analysis | View-relative resolution, demand-driven deepening, cyclic dependency incremental evaluation |
| Concept bottleneck / DAS / SAE | human-readable 여부와 무관한 latent CONTROL adapter와 side-effect measurement |

## 39. 외부 연구가 지지하는 부분

- Catlab wiring diagrams는 input/output port를 가진 box가 다시 recursively nested diagram이 될 수 있고 operadic substitution으로 합성될 수 있음을 구현한다. 이는 `Composition → 다시 하나의 composable interface`와 가깝다. [R1-R01]
- Higher-Order Graph Databases는 hypergraph, node tuple, subgraph를 higher-order element로 직접 다루는 prototype을 제시한다. 이는 high-resolution topology backend 후보지만 Final Ontology는 아니다. [R1-R02]
- Soufflé는 recursive Datalog를 fixed-point relational machine과 최적화된 parallel C++로 컴파일하고 lazy provenance를 지원한다. [R1-R03][R1-R04]
- DBSP는 relational queries, aggregation, nested relations, monotonic/non-monotonic recursion의 incrementalization을 일반화한다. 특히 composition chain rule은 `작은 변경을 각 합성 단계에 전달`한다는 목표와 잘 맞는다. [R1-R05]
- Demanded Abstract Interpretation은 cyclic dependency graph에서도 demand-driven + incremental evaluation을 결합하면서 soundness와 termination을 보존할 수 있음을 보인다. [R1-R15]
- egglog은 Datalog fixed point와 equality saturation을 결합해 많은 대안 표현을 조기에 제거하지 않는 search plane에 적합하다. [R1-R11]
- Incremental Relational Lenses는 작은 View change를 잠재적으로 작은 Source change로 전파할 수 있지만, 이것은 명시적으로 lens law가 선언된 경우에만 적용해야 한다. [R1-R12]
- provenance traces와 Datalog semiring circuits는 derivation을 naïve tree가 아니라 trace/circuit로 표현할 근거를 준다. [R1-R13][R1-R14]
- Maude 및 rewriting logic은 state/event property, fairness, cyclic protocol을 executable하게 검증하는 reference oracle로 유용하다. [R1-R09][R1-R10]
- 2026 latent steering 연구는 distributed interchange intervention과 SAE feature steering이 가능하지만, context/model/dictionary에 따라 collateral effects가 달라진다는 것을 보여준다. 따라서 latent CONTROL은 target effect와 off-target effect를 모두 측정해야 한다. [R1-R16][R1-R17]

## 40. 외부 연구가 경고하는 부분

- Unrestricted causal abstraction mapping은 임의의 neural network를 임의의 algorithm에 맞출 정도로 vacuous해질 수 있다. 따라서 “잘 맞는 추상화가 존재한다”만으로 faithful View라고 판단하지 않는다. 복잡도, 제한, intervention generalization, out-of-distribution behavior를 함께 검증해야 한다. [R1-R18]
- E-graph의 equality는 ASA의 universal identity가 아니다. ASA의 동등성은 View, scope, resolution, purpose에 따라 달라질 수 있다.
- Abstract Interpretation의 abstraction은 일반적으로 정보 손실을 동반한다. FOLD와 semantic abstraction/View를 구별하고, reconstruction을 자동 inverse로 간주하지 않는다.
- DBSP는 무엇이 의미 있는 View인지 정하지 않는다. 이미 정의된 computation의 delta runtime 부품이다.
- Hypergraph/HO graph는 표현력이 높지만 subgraph identity와 matching 비용이 커질 수 있다.
- Datalog rule vocabulary를 World ontology로 고정하면 개방성을 잃을 수 있다.

---

# XI. HYBRID CORE CANDIDATES

기술 Freeze가 아니라 같은 protocol probe를 통과시키기 위한 후보군이다.

## 41. Candidate A — Minimal Relation Interpreter

```text
Relation IR
+ explicit interfaces/order
+ fold/expand references
+ in-memory dependency DAG/cycle markers
+ event/replay log
```

목적:

- 가장 작은 semantic oracle
- 다른 runtime의 correctness baseline
- operator law와 terminology test

장점: 단순, 교체 가능, ontology commitment가 낮다.

약점: scale과 incremental performance가 낮다.

## 42. Candidate B — Relational Delta Runtime

```text
Minimal Relation IR
+ Datalog-ish recursive View evaluator
+ DBSP / differential incremental engine
+ compact provenance circuit
+ branch/replay store
```

목적:

- minimum necessary recompute baseline
- recursive View와 live change propagation
- production-like scale probe

장점: runtime, update, replay가 강하다.

약점: arbitrary structural rewrite와 high-order interfaces가 평탄화될 위험이 있다.

## 43. Candidate C — Higher-Order Wiring / Rewrite Reference

```text
Wiring diagram / operad interfaces
+ higher-order graph representation
+ graph rewriting / Maude transition oracle
+ provenance
```

목적:

- relation-on-relation, nested topology, cycles, intermediate CONTROL의 의미 보존 검증
- Candidate B가 잃은 구조를 검출하는 counter-model

장점: recursive composition과 structural observability가 강하다.

약점: hot-path runtime, matching, state-space explosion 위험이 크다.

## 44. Candidate D — Split Runtime / Reference / Search Envelope

```text
                    Protocol Contract
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   Runtime Plane     Reference Plane     Search Plane
   DBSP/Datalog      Wiring/HO Graph     egglog/AI
          └────────────────┼────────────────┘
                           ▼
                 Provenance / Replay
                           ▼
                  Latent Control Adapter
```

현재 가장 높은 정보이득을 주는 연구 envelope다.

- 하나의 기술을 Final Core로 승격하지 않는다.
- 동일 Relation/View/Control/State interchange contract로 후보를 교체한다.
- runtime 결과와 structural reference 결과가 어긋나는 지점을 연구한다.
- equality saturation과 AI proposal은 bounded sandbox에서만 사용한다.

이 Candidate가 “항상 3개 engine을 production에 유지한다”는 의미는 아니다. **교체 가능한 연구 비교틀**이다.

---

# XII. COMMON PROBE PLAN

## 45. 공통 Probe

`[PRO_MODE_PROPOSAL]` 아래 Probe registry는 비교 연구를 위한 제안이며,
Owner가 승인한 Gate 또는 구현 순서가 아니다.

아래 표는 executive subset이다. Canonical registry와 판정 metric은
`ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_v2.1_SYNC_2026-08-26.md`의
`P01..P20`이 소유한다.

| Probe | 최소 fixture | 판정 포인트 |
|---|---|---|
| Basic Relation | `A→B` | 방향, interface, identity, reproducibility |
| Recursive Composition | `A→B→C`, 다시 합성 | composition closure, order, fold witness |
| Fold / Expand | `A→D`를 펼침 | exact/inferred/unknown, candidate plurality |
| Intermediate Promotion | 생략된 B를 address | reconstruction, branch Control, re-use |
| Alternate Composition | 같은 endpoints의 다른 paths | identity preservation, View-relative equivalence |
| View / Control Separation | 같은 Subject에 filter vs change | semantic boundary, unintended write-back 방지 |
| Protocol + Event | event sequence / invalid transition | trace, fairness, State/Event property |
| Deep Composition | depth 10/100/1000 | latency, memory, fold depth, replay |
| View Resolution | low↔high View | distinction preservation, reconstruction coverage |
| Cycle / Dynamic Pattern | stable/oscillating/diverging | stop rule, pattern State, budget |
| Scoped Control | one branch / source-wide | containment, propagation, original preservation |
| AI Candidate Discovery | View/Control 후보 생성 | valid candidate yield, branch safety, promotion gate |
| Latent Control | subspace/feature intervention | target effect, collateral spread, drift |
| Lineage / Replay | old State 재현 | completeness, semantic replay, version closure |
| Incremental Update | `-r2 +r5` | touched work, correctness, fallback behavior |
| Candidate Explosion | branching factor 증가 | lazy preservation, pruning audit, diversity loss |
| Scale | relations, depth, update rate, branches | p50/p95, memory, storage, recovery time |

## 46. 공통 Metrics

```text
CONTROLLABILITY
= 의도한 target 변화 / 비의도 변화

MEASURABILITY
= 전후 효과를 안정적으로 계측할 수 있는 정도

INTERMEDIATE OBSERVABILITY
= intermediate를 address/reconstruct/measure할 수 있는 범위와 비용

REPEATABILITY
= recorded envelope로 semantic behavior를 재생하는 능력

RECONSTRUCTION PRECISION
= 제시한 high-resolution path 중 evidence와 일치하는 비율

RECONSTRUCTION COVERAGE
= 필요한 내부 Composition 중 복원 가능한 범위

UPDATE AMPLIFICATION
= 작은 input delta 대비 실제 갱신 작업량

PROVENANCE COVERAGE
= State 결과 중 derivation을 추적 가능한 비율

VIEW-EQUIVALENCE ERROR
= 낮은 해상도에서 합친 후보가 높은 해상도에서 잘못 합쳐진 비율

BRANCH COST
= 후보 하나 추가 시 compute/storage 증가량

CANDIDATE YIELD
= AI가 제안한 후보 중 valid하고 측정 가능한 비율

LATENT COLLATERAL SPREAD
= target 밖 feature/behavior 변화량
```

## 47. Proposed falsification criteria

`[PRO_MODE_PROPOSAL]` 현재 최소 protocol을 강화하거나 폐기할지
검토하게 만드는 시험 후보다. `Q-175`의 Owner Gate를 선결하지 않는다.

- 의미 보존 FOLD witness를 현실적 비용으로 만들 수 없다.
- 고해상도 reconstruction candidate가 폭발해 유용한 측정이 불가능하다.
- minimal recompute를 위해 결국 View/Control 내부를 항상 전부 펼쳐야 한다.
- VIEW와 CONTROL의 역할 구분이 observation back-action 때문에 일관되게 유지되지 않는다.
- relation-local role만으로 authority, safety, identity invariant를 보존할 수 없다.
- 같은 interchange contract로 서로 다른 backend 결과를 비교할 수 없다.
- latent Control이 off-target effect를 계측·제한할 수 없다.
- View-relative equivalence가 operational identity를 오염시킨다.

이 경우 protocol을 신념으로 방어하지 않고 수정한다.

---

# XIII. OPERATIONAL CONSTITUTION — v1.0에서 보존할 경계

## 48. Minimal kernel은 무타입 운영을 뜻하지 않는다

World Model에서는 Relation이 상위 개념이더라도 제품 운영에서는 다음 구분을 강하게 유지한다.

```text
Principal
AuthorityGrant
PolicyDecision
PolicyEnforcement
ActionProposal
Authorization
Signature
Execution
Outcome
Deletion / Restriction / Invalidation
Audit / Incident / Rollback
```

이들은 Relation Composition으로 표현할 수 있다는 이유만으로 동일한 저장 타입이나 자유로운 View-relative identity로 합치지 않는다.

## 49. Five-plane compatibility

v1.0의 다음 plane 분리는 유지할 가치가 있다.

```text
Evidence / Data
Semantic / Interpretation
Governance / Authority
Execution / Action
Evaluation / Audit
```

v2.0 protocol은 Semantic kernel과 Evaluation/Replay contract를 재정의하지만 Governance boundary를 제거하지 않는다.

## 50. Promotion and release

```text
CAN BE REPRESENTED
!=
AUTHORIZED TO EXECUTE

AI FOUND A CANDIDATE
!=
CANDIDATE MAY BE PROMOTED

VIEW-RELATIVE EQUIVALENCE
!=
AUTHORITY EQUIVALENCE
```

wallet, signing, privacy, deletion, model release 같은 고위험 경계는 deterministic policy enforcement를 유지한다.

---

# XIV. ASA INIT PHASE TRANSITION GATE

ASA INIT은 완성된 World Model이 아니다. 다음 현상을 **발생시키고, 관측하고, 제어하고, 비교하고, 다시 시험**할 수 있을 때 Phase Transition Gate를 통과한다.

## 51. Proposed INIT capability candidate set

`[PRO_MODE_PROPOSAL]` 아래는 probe 설계를 위한 candidate set이며,
Owner-approved Phase Transition Gate나 구현 명령이 아니다. 특히 latent
Control metric(`PI-07`), backend replacement(`Q-174`), minimum
toolkit(`Q-178`)은 별도 결정·검증이 필요하다.

```text
1. Directional Relation과 recursive Composition을 표현할 수 있다.
2. VIEW / CONTROL / STATE를 명확히 구분해 실행할 수 있다.
3. Composition을 의미 보존적으로 접고 필요 시 펼칠 수 있다.
4. Intermediate를 on-demand 재구성하고 addressable하게 승격할 수 있다.
5. 원본 보존 Branch와 alternate candidate를 유지할 수 있다.
6. relation-level change를 따라 최소 필요한 부분만 재계산할 수 있다.
7. high-resolution reconstruction의 exact/inferred/unknown 및 복수 후보를 관리할 수 있다.
8. cycles와 dynamic pattern을 관측·제어할 수 있다.
9. AI가 View/Control/Composition 후보를 sandbox에서 제안·실행·측정할 수 있다.
10. Promotion authority를 policy로 제어할 수 있다.
11. lineage, replay, version, dependency를 보존한다.
12. latent Control의 target/off-target effect를 측정할 수 있다.
13. backend를 바꾸어도 같은 Probe를 재실행할 수 있다.
```

## 52. INIT에서 아직 고정하지 않는 것

```text
final ontology
one canonical graph/database
one universal View
fixed Persona count
split/merge/mutation primitive
one reconstruction algorithm
one equality definition
one latent representation
one automatic promotion policy
```

---

# XV. COMPACT DEFINITIONS

## 53. Protocol compact form

```text
RELATION
= 현재 해상도에서의 방향 사상

COMPOSITION
= declared interface/admissibility가 허용한 Relation들을 연결해
  결과를 다시 Relation처럼 사용할 수 있게 하는 성질

FOLD
= 의미를 보존하며 중간 Composition을 생략하는 표현

VIEW:X
= 보는 역할의 접힌 Relation Composition

CONTROL:X
= 바꾸는 역할의 접힌 Relation Composition

STATE:X
= 선행 Relation Composition을 암묵적으로 생략한 addressable state

SUBJECT
= 현재 View가 향하는 relation-local role

RESOLUTION
= VIEW가 결정하는 펼침의 정도

RECONSTRUCTION
= 접힌 Relation의 내부 Composition 후보를 evidence와 budget 아래 복원하는 과정
```

## 54. Core 한 문장

> **ASA INIT Core는 Relation을 많이 저장하는 시스템이 아니라, 관계합성을 필요한 만큼 접고 펼치며, 작은 변화가 큰 State 변화를 만들더라도 실제 영향분만 계산하고, 서로 다른 View·Control·복원 후보를 원본 훼손 없이 반복 시험할 수 있는 Closure Toolkit이어야 한다.**

## 55. 최종 Pro-mode 판정

현재 protocol은 근거 없는 단독 철학이라기보다 다음 연구군의 공통 부분을 ASA 목적에 맞게 느슨하게 재조합한 후보로 볼 수 있다.

```text
morphism / relation composition
operads and wiring diagrams
nested and higher-order data
recursive logic / rewriting
incremental computation
provenance
abstract interpretation
bidirectional transformations
latent causal intervention
```

그러나 아직 formal calculus가 완성된 것은 아니다. 특히 interface compatibility, relation identity, fold witness, reconstruction semantics, View/Control boundary, probabilistic/nondeterministic composition, authority typing은 추가 질문과 probe가 필요하다.

따라서 v2.1 candidate 권고 상태:

```text
RESEARCH_BASELINE = V2.1 CANDIDATE
OWNER_ACCEPTANCE = PENDING
IMPLEMENTATION_AUTHORIZATION = NONE
TECHNOLOGY = KEEP SWAPPABLE
OWNER INTERVIEW = CONTINUE ON FORMAL CAPABILITY BOUNDARIES
PROTOTYPE_SEQUENCE = RECOMMENDED ONLY IF SEPARATELY AUTHORIZED
OPEN_ITEMS_RESOLVED_BY_THIS_REVISION = NONE
```

---

# XVI. EXTERNAL RESEARCH REFERENCES

접근일: 2026-08-25. 최신 preprint는 검증된 표준이 아니라 emerging evidence로만 취급한다.

- **[R1-R01] Catlab.jl, Wiring Diagrams documentation.** Recursive nested boxes, input/output ports, operadic composition. https://algebraicjulia.github.io/Catlab.jl/latest/apis/wiring_diagrams/
- **[R1-R02] Besta et al., “Higher-Order Graph Databases,” 2025.** https://arxiv.org/abs/2506.19661
- **[R1-R03] Soufflé, Synthesis documentation.** Semi-naïve/fixed-point relational machine compiled to optimized parallel C++. https://souffle-lang.github.io/translate
- **[R1-R04] Soufflé, Provenance documentation.** https://souffle-lang.github.io/provenance
- **[R1-R05] Budiu, McSherry, Ryzhyk, Tannen, “DBSP: Automatic Incremental View Maintenance for Rich Query Languages.”** https://arxiv.org/abs/2203.16684
- **[R1-R06] Feldera publications / DBSP extended 2025 publication list.** https://docs.feldera.com/literature/papers/
- **[R1-R07] Koch, Lupei, Tannen, “Incremental View Maintenance For Collection Programming.”** https://arxiv.org/abs/1412.4320
- **[R1-R08] Brown et al., “Computational category-theoretic rewriting.”** https://arxiv.org/abs/2111.03784
- **[R1-R09] Maude Linear Temporal Logic of Rewriting Model Checker.** https://maude.cs.illinois.edu/tools/tlr/
- **[R1-R10] Maude LTL Logical Model Checker / folding abstraction.** https://maude.cs.illinois.edu/tools/lmc/
- **[R1-R11] Zhang et al., “Better Together: Unifying Datalog and Equality Saturation,” PLDI 2023.** https://arxiv.org/abs/2304.04332
- **[R1-R12] Horn, Perera, Cheney, “Incremental Relational Lenses,” ICFP 2018.** https://arxiv.org/abs/1807.01948
- **[R1-R13] Fan, Koutris, Roy, “Circuits and Formulas for Datalog over Semirings,” PODS 2025.** https://arxiv.org/abs/2504.08914
- **[R1-R14] Cheney, Acar, Ahmed, “Provenance Traces.”** https://arxiv.org/abs/0812.0564
- **[R1-R15] Stein, Chang, Sridharan, “Demanded Abstract Interpretation,” PLDI 2021.** https://arxiv.org/abs/2104.01270
- **[R1-R16] Bao et al., “Faithful Bi-Directional Model Steering via Distribution Matching and Distributed Interchange Interventions,” 2026 preprint.** https://arxiv.org/abs/2602.05234
- **[R1-R17] Duan, “Pre-Intervention Prediction of Sparse Autoencoder Steering Side Effects,” 2026 preprint.** https://arxiv.org/abs/2606.08365
- **[R1-R18] Sutter et al., “The Non-Linear Representation Dilemma,” 2025.** https://arxiv.org/abs/2507.08802
- **[R1-R19] Tiurin, Ghica, Hu, “E-Graphs With Bindings,” 2025.** https://arxiv.org/abs/2505.00807
- **[R1-R20] Olteanu, “Recent Increments in Incremental View Maintenance,” PODS 2024.** https://arxiv.org/abs/2404.17679
- **[R1-R21] Chmielewski et al., “The Role of Semirings in Incremental View Maintenance,” 2026 preprint.** https://arxiv.org/abs/2606.07795

---

## Appendix A — Protocol notation examples

```text
# 최소 Relation
r : A → B

# 합성
r3 := r2 ∘ r1

# 의미 보존 접기
A → B → C → D
≡ FOLD → A → D

# View / State
SUBJECT --VIEW:X→ STATE:X

# Control branch
STATE:X --CONTROL:Y→ STATE:X'  [branch]

# Delta
(STATE:X, STATE:X') --VIEW:DELTA→ STATE:DELTA

# 복원
A → D
--VIEW:HIGH / EXPAND→
{ A→B→D, A→C→D, UNKNOWN }

# 순환 pattern
A→B→A→...
--VIEW:PATTERN→ STATE:PATTERN
```

## Appendix B — Terminology guards

```text
STATE alone
!=
state without predecessors

ATTRIBUTE notation
!=
intrinsic property ontology

REVERSE INDEX
!=
reverse semantic Relation

SAME UNDER VIEW
!=
same identity

FOLD
!=
filter

VIEW
!=
VIEW output

CONTROL
!=
DELTA

HIGH RESOLUTION
!=
final truth
```
