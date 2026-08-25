# ASA CORE WORLD MODEL v2.1 SYNC — OPEN QUESTIONS / OWNER INTERVIEW LEDGER

```text
STATUS = V2.1_SYNC / OPEN QUESTION REGISTER / NON_FROZEN
PROJECT = AAA / BYUL
PRODUCT = ASSET AGENT ASA
DATE_KST = 2026-08-26
INTERVIEW_RULE = ONE SUBSTANTIVE QUESTION AT A TIME
TECHNOLOGY_SELECTION_BY_OWNER = PROHIBITED
BUSINESS_LOGIC_FREEZE = PROHIBITED AT THIS STAGE
QUESTIONS_PRESERVED = 180
QUESTIONS_ANSWERED_BY_THIS_SYNC = 0
PRIMARY_DISPOSITION_COUNTS = RETAINED_OPEN 174 / SUPERSEDED 1 / DUPLICATE 2 / TERMINOLOGY_UPDATE_ONLY 3 / DEFERRED 0
```

---

## Disposition legend

```text
RETAINED_OPEN = 질문의 substantive answer가 여전히 미결
SUPERSEDED_BY_OWNER_DECISION = exact OD가 질문의 핵심 default를 이미 확정
DUPLICATE_OF_Qxxx = 다른 질문과 같은 미결 문제를 중복 질문
TERMINOLOGY_UPDATE_ONLY = 답은 미결이나 v2.1 용어·범위만 정정
DEFERRED = 현재 단계 밖이며 미결 상태로 보존
```

Disposition은 질문을 자동 해결하지 않는다. Pro-mode implication이나
R1의 제안 문구만으로 `SUPERSEDED`를 부여하지 않는다.

## 0. 인터뷰 원칙

이 문서의 질문은 `Datalog을 쓸까요, Hypergraph를 쓸까요?`처럼 기술을 Owner에게 선택하게 하지 않는다.

질문 형식은 다음을 따른다.

> **설계 A는 이런 controllability/observability를 제공하고, 설계 B는 이런 비용과 제약을 갖는다. ASA INIT이 반드시 보존해야 하는 능력은 어디까지인가?**

Owner 인터뷰에서는 아래 질문을 한 번에 하나씩 사용한다. 이미 승인된 내용을 반복 확인하지 않는다.

### Priority

```text
P0 = formal protocol이 깨지지 않기 위해 먼저 필요
P1 = ASA INIT probe/gate 전에 필요
P2 = prototype 결과를 보고 결정 가능
P3 = 이후 domain/governance 단계
```

---

# A. MINIMAL RELATION AND IDENTITY

## Q-001 · P0 — Relation identity의 최소 기준

> DISPOSITION: RETAINED_OPEN

같은 Source/Target과 같은 현재 output을 가진 두 Relation이 서로 다른 내부 Composition을 가진다면, Core는 언제까지 둘을 별도 identity로 유지해야 합니까? **계보가 다르면 항상 분리**해야 합니까, 아니면 선언된 View에서 완전히 대체 가능하면 같은 operational identity로 취급할 수 있습니까?

## Q-002 · P0 — Identity의 안정 범위

> DISPOSITION: RETAINED_OPEN

Relation identity는 View가 달라도 유지되는 backend-level identity여야 합니까, 아니면 View마다 별도 handle을 갖고 cross-View relation으로 연결하면 충분합니까?

## Q-003 · P0 — Current-resolution minimum의 종료 기준

> DISPOSITION: RETAINED_OPEN

현재 해상도에서 무엇을 하나의 최소 Relation으로 접을지는 누가 결정해야 합니까? View 정의, runtime cost model, 연구자 지정, AI proposal 중 어떤 권한을 반드시 제어할 수 있어야 합니까?

## Q-004 · P0 — Source/Target interface의 명시 수준

> DISPOSITION: RETAINED_OPEN

고해상도 Composition의 continuity를 검증하려면 Source/Target interface를 어느 수준까지 선언해야 합니까? 단순 handle 일치만으로 충분합니까, 아니면 role/shape/constraint를 검증할 수 있어야 합니까?

## Q-005 · P0 — Source/Target의 복수 구조

> DISPOSITION: RETAINED_OPEN

`(A,B,C) → (D,E)`를 한 Relation로 접을 때, A/B/C가 모두 필요한지, 일부가 optional인지, 후보인지까지 interface에서 표현해야 합니까, 아니면 필요할 때 내부 Composition으로만 펼치면 됩니까?

## Q-006 · P0 — Relation kind 최소화의 안전 경계

> DISPOSITION: RETAINED_OPEN

Relation의 본질 특성을 방향 사상 하나로 유지하면서도 `authority`, `causal`, `dependency`, `evidence`, `execution`을 잘못 서로 대체하지 않게 하려면, Core 외부에 강한 role/type guard를 반드시 둘까요?

## Q-007 · P1 — Opaque endpoint 허용 범위

> DISPOSITION: RETAINED_OPEN

내용을 열 수 없는 encrypted/remote/latent State도 Relation의 Source/Target이 될 수 있게 해야 합니까? 그렇다면 interface와 lineage만으로 합성 가능성을 판단해도 됩니까?

## Q-008 · P1 — Relation identity의 content addressability

> DISPOSITION: RETAINED_OPEN

같은 Composition을 replay했을 때 같은 relation handle을 재사용하려면 deterministic hash가 필요합니까, 아니면 run마다 다른 identity를 만들고 equivalence로 연결하는 편이 안전합니까?

## Q-009 · P1 — Same-content different-lineage

> DISPOSITION: RETAINED_OPEN

동일한 State/Relation 내용을 서로 다른 View와 Control 경로로 얻었다면, 하나의 content state와 여러 lineage를 연결할까요, 아니면 lineage별 State를 분리할까요?

## Q-010 · P1 — Identity Relation의 범위

> DISPOSITION: RETAINED_OPEN

`ID_A`가 의미적으로 아무 변화가 없다는 판정은 어느 View에서의 동일성을 기준으로 합니까? 모든 relevant View에서 같아야 합니까, 아니면 선언된 View/scope에서만 중립이면 됩니까?

## Q-011 · P1 — Unknown endpoint

> DISPOSITION: RETAINED_OPEN

Source 또는 Target 일부가 `UNKNOWN`이어도 Relation handle을 허용합니까? 허용한다면 어떤 Control/Promotion은 금지되어야 합니까?

## Q-012 · P1 — Partial endpoint

> DISPOSITION: RETAINED_OPEN

고해상도 복원 중 Source/Target interface가 일부만 복원된 Relation도 다음 Composition 후보로 참여할 수 있게 합니까?

## Q-013 · P2 — Relation deletion의 의미

> DISPOSITION: RETAINED_OPEN

Relation이 “삭제됐다”는 것은 operational current State에서 더 이상 성립하지 않는 것입니까, 기록 자체를 지운 것입니까, 특정 View에서 보이지 않는 것입니까? 세 경우를 어떤 표면 구분으로 보존해야 합니까?

## Q-014 · P2 — Relation immutability

> DISPOSITION: RETAINED_OPEN

하나의 Relation record를 수정할까요, 아니면 수정 전후를 별 Relation/State로 남겨 변화 관계로 연결할까요? replay와 최소계산을 위해 후자를 기본으로 할 필요가 있습니까?

## Q-015 · P2 — Ephemeral Relation

> DISPOSITION: RETAINED_OPEN

한 실행 중 잠깐 생기고 저장되지 않는 Relation도 formal identity를 가져야 합니까, 아니면 trace에만 남으면 충분합니까?

---

# B. COMPOSITION VALIDITY AND LAWS

## Q-016 · P0 — Composition admissibility witness

> DISPOSITION: RETAINED_OPEN

두 Relation이 직접 이어지지 않아 보이지만 intermediate가 생략됐다고 가정할 때, 합성을 허용하려면 어떤 근거가 필요합니까? 기록된 path, inferred candidate, declared interface adapter 중 최소 무엇을 요구해야 합니까?

## Q-017 · P0 — 추정 bridge의 사용 권한

> DISPOSITION: RETAINED_OPEN

`B → ? → C`를 추정해 Composition을 이어갈 때, 추정 bridge를 read-only research candidate로만 둘까요, 아니면 branch Control의 target이 될 수 있게 할까요?

## Q-018 · P0 — Operator law declaration

> DISPOSITION: RETAINED_OPEN

각 View/Control/Relation operator가 associativity, commutativity, idempotence, monotonicity 같은 법칙을 명시적으로 선언하고 test해야 합니까?

## Q-019 · P0 — Law가 View-relative한가

> DISPOSITION: RETAINED_OPEN

같은 operator가 VIEW:X에서는 commutative하고 VIEW:Y에서는 그렇지 않을 수 있습니까? 그렇다면 law는 operator 본체가 아니라 View/scope contract에 귀속해야 합니까?

## Q-020 · P0 — FOLD equivalence의 증거

> DISPOSITION: RETAINED_OPEN

`A→B→C`를 `A→C`로 접었을 때 의미 보존임을 어떤 수준으로 보장해야 합니까? exact proof, test equivalence, declared assumption, empirical tolerance를 구분해야 합니까?

## Q-021 · P0 — FOLD와 lossy abstraction

> DISPOSITION: TERMINOLOGY_UPDATE_ONLY · SUBSTANTIVE_STATUS: OPEN · RELATED_OD: OD-060 · RELATED_OPEN: OPEN-05

어떤 View가 정보를 버리지만 목적상 충분한 경우, 이를 `FOLD`가 아니라 별도 semantic View라고 표기하는 규칙을 runtime에서도 강제해야 합니까?

## Q-022 · P0 — Composition path ambiguity

> DISPOSITION: RETAINED_OPEN

동일 endpoints에 여러 path가 있고 모두 현재 View에서 같은 결과를 낼 때, fold handle 하나 아래 path들을 보존할까요, 아니면 path별 handle을 유지하고 View에서 grouping할까요?

## Q-023 · P0 — Cyclic composition law

> DISPOSITION: RETAINED_OPEN

cycle이 있는 Composition을 하나의 Relation으로 접을 때, 한 번의 mapping, fixed point, transition system, dynamic pattern 중 어떤 contract를 반드시 명시해야 합니까?

## Q-024 · P1 — Parallel composition

> DISPOSITION: RETAINED_OPEN

두 Relation이 서로 dependency 없이 함께 적용될 때 parallel Composition을 표면에 구분해야 합니까, 아니면 order-insensitive law가 검증된 chain으로만 표현해도 됩니까?

## Q-025 · P1 — Candidate composition과 simultaneous composition

> DISPOSITION: RETAINED_OPEN

복수 target이 `함께 성립`하는 경우와 `서로 대안`인 경우를 고해상도 topology로만 구분하면 충분합니까, 아니면 저해상도 handle에서도 candidate/simultaneous discriminator가 필요합니까?

## Q-026 · P1 — Composition conflict

> DISPOSITION: RETAINED_OPEN

동일 scope에서 함께 성립할 수 없는 Control/View compositions가 만나면, conflict를 하나의 State로 관측하고 lazy branch 후보로 보존하는 능력을 INIT 필수로 둘까요?

## Q-027 · P1 — Conflict resolution policy

> DISPOSITION: RETAINED_OPEN

충돌을 반드시 해결해야 할 때, hidden last-write-wins를 금지하고 모든 resolution rule을 명시적 View/Control로 남겨야 합니까?

## Q-028 · P1 — Composition cancellation

> DISPOSITION: RETAINED_OPEN

`r` 뒤에 `s`를 적용했더니 현재 View에서 원상태가 됐을 때, `s∘r = ID`로 접을 수 있습니까, 아니면 내부 변화와 비용 때문에 별 Relation으로 유지해야 합니까?

## Q-029 · P1 — Partial inverse

> DISPOSITION: RETAINED_OPEN

어떤 View/Control이 일부 범위에서만 역방향 복원이 가능하면 partial inverse contract를 허용합니까? 실패 범위와 정보손실을 어떻게 드러내야 합니까?

## Q-030 · P1 — Many-to-one fold

> DISPOSITION: RETAINED_OPEN

여러 Composition candidate가 하나의 낮은 해상도 Relation으로 접힐 때, high-resolution expansion이 원래 후보들을 모두 회수할 수 있어야 합니까, 아니면 대표 일부와 coverage만 제공해도 됩니까?

## Q-031 · P2 — Composition normalization

> DISPOSITION: RETAINED_OPEN

동일 의미의 Composition을 하나의 canonical form으로 정규화할까요, 아니면 서로 다른 표현을 유지하고 View-relative equivalence로 연결할까요?

## Q-032 · P2 — Rewrite와 Composition의 경계

> DISPOSITION: RETAINED_OPEN

기존 Composition 내부 구조를 바꾸는 것은 Control입니까, 새 Composition candidate 생성입니까, 둘 다 가능한 별 role입니까?

## Q-033 · P2 — Lazy Composition identity

> DISPOSITION: RETAINED_OPEN

아직 실행하지 않은 lazy View/Composition도 stable identity를 가져야 합니까? 실행 전후 identity를 같게 유지할까요?

## Q-034 · P2 — Failed composition

> DISPOSITION: RETAINED_OPEN

interface mismatch, budget stop, unknown intermediary 때문에 완성되지 않은 Composition을 `STATE:FAILED`로 남길까요, 아니면 실행 log에만 둘까요?

## Q-035 · P2 — Composition cost as relational input

> DISPOSITION: RETAINED_OPEN

예상 비용·latency·memory를 View candidate selection에 사용하는 경우, cost estimate 자체를 State로 승격해 다른 View의 Subject로 다룰 필요가 있습니까?

---

# C. VIEW SEMANTICS

## Q-036 · P0 — VIEW의 최소 contract

> DISPOSITION: RETAINED_OPEN

VIEW라고 부르기 위해 반드시 필요한 능력은 무엇입니까? Subject를 받아 State를 성립시키는 것만으로 충분합니까, 아니면 scope, resolution, composition identity, repeatability를 선언해야 합니까?

## Q-037 · P0 — VIEW와 pure observation

> DISPOSITION: RETAINED_OPEN

View는 Subject를 변화시키지 않는 것으로 정의할까요? 측정 자체가 상태를 바꾸는 경우에는 View+Control composition으로 명시해야 합니까?

## Q-038 · P0 — View back-action

> DISPOSITION: RETAINED_OPEN

외부 API 조회, model inference, sensor read처럼 관측이 cache·rate-limit·학습 상태를 바꾸는 경우, semantic View와 operational side-effect Control을 분리 기록해야 합니까?

## Q-039 · P0 — View identity

> DISPOSITION: RETAINED_OPEN

조건 하나가 추가·제거되면 항상 새로운 VIEW identity입니까, 아니면 동일 View family의 version입니까? 어떤 capability 차이를 보존해야 합니까?

## Q-040 · P0 — View family

> DISPOSITION: RETAINED_OPEN

`VIEW:A@v1`, `VIEW:A@v2`를 같은 계열로 묶는 기준은 이름, lineage, declared succession, behavior equivalence 중 무엇입니까?

## Q-041 · P0 — View-relative sameness의 한계

> DISPOSITION: RETAINED_OPEN

View-relative equivalence가 허용되더라도 legal identity, authority, ownership 같은 invariant를 바꾸지 못하게 별도 boundary를 둘까요?

## Q-042 · P0 — Resolution axis의 다차원성

> DISPOSITION: RETAINED_OPEN

Resolution을 단순 depth 하나로 볼까요, 아니면 temporal, semantic, structural, latent, provenance resolution을 별 축으로 제어할 수 있어야 합니까?

## Q-043 · P1 — View composition visibility

> DISPOSITION: RETAINED_OPEN

평소 View 내부를 접되, researcher가 어느 operator에서 distinction이 사라졌는지 확인할 수 있도록 “loss/selection boundary”를 표시해야 합니까?

## Q-044 · P1 — Seed View minimum

> DISPOSITION: RETAINED_OPEN

ASA INIT이 relation을 전혀 볼 수 없는 상태를 피하기 위해 seed View를 몇 종류의 capability로 준비해야 합니까? 개수보다 `관측·비교·lineage·control target 발견` 능력으로 Gate를 정할까요?

## Q-045 · P1 — View discovery scope

> DISPOSITION: RETAINED_OPEN

AI가 새 View를 제안할 때 existing View의 작은 mutation만 허용할까요, 완전히 다른 composition topology도 sandbox에서 허용할까요?

## Q-046 · P1 — View narrowing vs new View

> DISPOSITION: RETAINED_OPEN

기존 View의 조건을 더한 결과를 version으로 볼지 새 View로 볼지, identity보다 lineage를 보존하면 충분합니까?

## Q-047 · P1 — Cross-View comparison

> DISPOSITION: RETAINED_OPEN

두 View의 State를 비교하는 것 자체가 또 다른 View라는 원칙을 protocol에 명시할까요?

## Q-048 · P1 — View result multiplicity

> DISPOSITION: RETAINED_OPEN

같은 View와 Subject에서 여러 State candidate가 나올 수 있습니까? 가능하다면 View가 nondeterministic한 것인지, reconstruction 후보인지 구분해야 합니까?

## Q-049 · P1 — View determinism declaration

> DISPOSITION: RETAINED_OPEN

반복 가능한 실험을 위해 View가 deterministic, stochastic, external-dependent 중 어떤 mode인지 선언하게 할까요?

## Q-050 · P1 — View portability

> DISPOSITION: RETAINED_OPEN

같은 VIEW:X를 다른 backend/AI model에서 적용했을 때 어느 정도 결과가 같아야 같은 View로 부를 수 있습니까?

## Q-051 · P2 — View materialization

> DISPOSITION: RETAINED_OPEN

자주 쓰이는 View를 cache/materialize할 때, 그 materialization을 View identity와 분리된 execution artifact로 둘까요?

## Q-052 · P2 — View deprecation

> DISPOSITION: RETAINED_OPEN

새 View가 더 낫다고 평가되어도 기존 View를 삭제하지 않고 deprecated lineage로 남겨 replay를 보존할까요?

## Q-053 · P2 — View purpose

> DISPOSITION: RETAINED_OPEN

Purpose를 View 내부 속성으로 고정하지 않고, `Purpose State → selects/configures → View` 관계로 외부화할까요?

## Q-054 · P2 — View composition depth cap

> DISPOSITION: RETAINED_OPEN

View가 재귀적으로 다른 View를 접을 수 있을 때 identity lookup과 replay를 위해 최대 unfold depth 또는 cycle guard가 필요합니까?

## Q-055 · P2 — View observability overhead

> DISPOSITION: RETAINED_OPEN

모든 View operator를 관측 가능하게 만들면 runtime 비용이 커집니다. 항상 trace할 최소 spine과 on-demand 상세 trace를 구분할까요?

---

# D. CONTROL SEMANTICS

## Q-056 · P0 — CONTROL의 최소 contract

> DISPOSITION: RETAINED_OPEN

CONTROL이라고 부르기 위해 target, scope, intended change, reversibility, measurement expectation 중 무엇을 필수로 선언해야 합니까?

## Q-057 · P0 — Control target classes

> DISPOSITION: RETAINED_OPEN

Control은 STATE, VIEW, 다른 CONTROL, latent representation, runtime policy 모두에 적용할 수 있어야 합니까? INIT에서 반드시 필요한 target 범위는 어디까지입니까?

## Q-058 · P0 — View/Control boundary under parameter change

> DISPOSITION: RETAINED_OPEN

threshold 변경처럼 “보는 조건”과 “상태를 바꾸는 조절” 양쪽으로 읽힐 수 있는 경우, 결과의 대상이 Subject인지 View definition인지로 구분하면 충분합니까?

## Q-059 · P0 — Control reversibility

> DISPOSITION: RETAINED_OPEN

모든 experimental Control은 inverse가 없어도 branch rollback으로 철회할 수 있으면 충분합니까, 아니면 Control 자체의 semantic inverse를 구분해야 합니까?

## Q-060 · P0 — Control conflict preservation

> DISPOSITION: RETAINED_OPEN

상충 Control을 하나로 자동 resolve하지 않고 conflict State와 alternative branches로 보존하는 능력을 INIT 필수로 확정할까요?

## Q-061 · P0 — Control compatibility declaration

> DISPOSITION: RETAINED_OPEN

Control 조합이 가능한지 operator가 compatibility law를 선언해야 합니까, 아니면 sandbox execution으로 발견해도 됩니까?

## Q-062 · P0 — Control order

> DISPOSITION: SUPERSEDED_BY_OWNER_DECISION · RELATED_OD: OD-061 · RESIDUAL: Q-018..Q-020

Control A→B와 B→A가 다를 수 있으므로 order를 기본 보존합니다. 결과가 같은지 검증된 경우에만 접을까요?

## Q-063 · P1 — Control scope inheritance

> DISPOSITION: RETAINED_OPEN

접힌 CONTROL:AB 내부 A와 B의 scope가 다를 때 composite Control의 scope를 어떻게 계산해야 합니까? 가장 좁은 범위, union, explicit route 중 무엇을 허용해야 합니까?

## Q-064 · P1 — Control budget inheritance

> DISPOSITION: RETAINED_OPEN

Control이 재귀적으로 합성될 때 compute/risk/authority budget을 단순 합산할까요, 별 policy View가 계산하게 할까요?

## Q-065 · P1 — Control measurement contract

> DISPOSITION: RETAINED_OPEN

Control은 적용 전에 target metric과 off-target metric을 선언하도록 해야 합니까, 아니면 exploratory Control은 사후 발견을 허용합니까?

## Q-066 · P1 — Control promotion criteria

> DISPOSITION: RETAINED_OPEN

좋은 결과라는 단일 score가 아니라 repeatability, collateral effect, reconstruction, governance pass를 함께 요구할까요?

## Q-067 · P1 — Control over inferred State

> DISPOSITION: RETAINED_OPEN

INFERRED State에 Control을 적용할 때 실제 operational State로 승격하는 경로를 금지하고 experimental branch에만 한정할까요?

## Q-068 · P1 — Source-wide Control

> DISPOSITION: RETAINED_OPEN

operational current state 전체에 적용되는 Control은 experimental Control과 다른 authorization class를 가져야 합니까?

## Q-069 · P1 — Latent Control portability

> DISPOSITION: RETAINED_OPEN

같은 이름의 latent Control이 model version이 달라지면 새 Control identity여야 합니까?

## Q-070 · P2 — Continuous/discrete control mix

> DISPOSITION: RETAINED_OPEN

가중 가능한 Control과 discrete Control을 합성할 때 하나의 algebra를 만들지 않고 typed composition으로 제한할까요?

## Q-071 · P2 — Control no-op

> DISPOSITION: RETAINED_OPEN

Control을 적용했지만 현재 View에서 Delta가 0이면 no-op으로 접을까요, 아니면 내부 effect 가능성 때문에 별 execution을 남길까요?

## Q-072 · P2 — Control learning

> DISPOSITION: RETAINED_OPEN

반복 실험으로 Control parameter가 업데이트될 때 같은 Control의 evolution입니까, 새 Control candidate입니까?

## Q-073 · P2 — Control admission

> DISPOSITION: RETAINED_OPEN

AI가 만든 Control을 실행하기 전에 static validation, simulation, sandbox, human approval 중 어떤 Gate가 scope별로 필요합니까?

## Q-074 · P2 — Control composition pruning

> DISPOSITION: RETAINED_OPEN

Control 후보가 조합 폭발할 때 diversity를 잃지 않으면서 어떤 View로 우선순위를 정할지 Owner가 제어할 수 있어야 합니까?

## Q-075 · P3 — Control accountability

> DISPOSITION: RETAINED_OPEN

Control 결과가 외부 행동으로 이어질 때 제안자, 승인자, 실행자, 서명자를 반드시 분리 기록할까요?

---

# E. STATE SEMANTICS, IDENTITY, TIME

## Q-076 · P0 — STATE의 최소 contract

> DISPOSITION: RETAINED_OPEN

STATE:X는 addressable handle만 있으면 됩니까, 아니면 View ref, Subject ref, lineage root, version boundary를 최소 보존해야 합니까?

## Q-077 · P0 — State content vs State occurrence

> DISPOSITION: RETAINED_OPEN

동일 content가 여러 실행에서 나타나면 하나의 content State와 여러 occurrence를 분리할까요?

## Q-078 · P0 — Same State under different Views

> DISPOSITION: RETAINED_OPEN

VIEW:A와 VIEW:B가 동일한 관계구성을 만들었다면 `STATE:A`와 `STATE:B`는 같은 State입니까, 서로 다른 State이며 equivalence만 가집니까?

## Q-079 · P0 — State naming pair cardinality

> DISPOSITION: RETAINED_OPEN

하나의 VIEW:X에서 여러 STATE:X@run이 나오고, 하나의 STATE가 여러 View 경로로 생성될 수 있음을 공식 허용할까요?

## Q-080 · P0 — State temporal identity

> DISPOSITION: RETAINED_OPEN

시간이 지나 내부가 일부 달라지면 새 State identity를 만들고 temporal relation으로 연결할까요, 하나의 mutable State handle의 version으로 볼까요?

## Q-081 · P0 — State branch identity

> DISPOSITION: RETAINED_OPEN

원본과 experimental branch가 결과상 같아져도 lineage가 다르면 별 State occurrence로 유지할까요?

## Q-082 · P1 — Ephemeral State

> DISPOSITION: RETAINED_OPEN

중간 State를 저장하지 않고 계산 중에만 존재하게 할 때, 나중에 재현 가능한 minimal trace만 남기면 충분합니까?

## Q-083 · P1 — State canonicalization boundary

> DISPOSITION: RETAINED_OPEN

State 내부 전체를 펼치지 않고도 같은 content인지 판정하려면 어떤 digest/equivalence witness가 필요합니까?

## Q-084 · P1 — State completeness

> DISPOSITION: RETAINED_OPEN

Partial/Unknown/Approximate State를 일반 State와 같은 namespace에 둘까요, discriminator를 의무화할까요?

## Q-085 · P1 — State materialization level

> DISPOSITION: RETAINED_OPEN

State handle이 full materialization, partial cache, reconstructable recipe, inference-only candidate 중 어떤 상태인지 표면에서 구분해야 합니까?

## Q-086 · P1 — State lifecycle

> DISPOSITION: RETAINED_OPEN

created, materialized, stale, invalidated, archived, deleted 같은 lifecycle은 State ontology가 아니라 operational relation으로 처리하면 충분합니까?

## Q-087 · P1 — State deletion and lineage

> DISPOSITION: RETAINED_OPEN

privacy deletion으로 State content를 제거해도 audit용 lineage tombstone은 남겨야 합니까? 어느 정도까지 남길 수 있습니까?

## Q-088 · P2 — State merge label

> DISPOSITION: RETAINED_OPEN

서로 다른 lineage가 동일 State content에 도달하는 경우 `merge`를 primitive로 만들지 않고 incoming relations로만 표현하는 방향을 유지할까요?

## Q-089 · P2 — State split label

> DISPOSITION: RETAINED_OPEN

한 State에서 여러 successor가 생겨도 `split`은 derived View label로만 둘까요?

## Q-090 · P2 — State immutability

> DISPOSITION: RETAINED_OPEN

연구 repeatability를 위해 materialized State occurrence는 immutable하게 하고 수정은 새 State로 만드는 것이 필요합니까?

---

# F. RECONSTRUCTION, RESOLUTION, UNCERTAINTY

## Q-091 · P0 — Reconstruction target

> DISPOSITION: RETAINED_OPEN

고해상도 복원은 “실제로 과거에 실행된 path”를 찾는 것과 “현재 evidence로 가능한 path”를 찾는 것을 별 mode로 구분해야 합니까?

## Q-092 · P0 — Exact의 정의

> DISPOSITION: RETAINED_OPEN

EXACT는 byte-identical replay, 동일 operator path, 동일 semantic output 중 어느 수준입니까? 여러 exactness level을 둘까요?

## Q-093 · P0 — Inferred의 최소 evidence

> DISPOSITION: RETAINED_OPEN

INFERRED candidate를 생성하려면 최소한 어떤 evidence가 있어야 합니까? 자유로운 AI 생성과 evidence-grounded reconstruction을 분리해야 합니까?

## Q-094 · P0 — Unknown의 작동 규칙

> DISPOSITION: RETAINED_OPEN

UNKNOWN intermediate가 포함된 Composition은 어디까지 실행할 수 있습니까? 관측·sandbox·promotion 각각 다른 금지선을 둘까요?

## Q-095 · P0 — Candidate plurality limit

> DISPOSITION: RETAINED_OPEN

복원 후보를 모두 보존하면 폭발할 수 있습니다. 상위 N개만 보존할까요, compressed equivalence class와 discarded summary를 남길까요?

## Q-096 · P0 — Candidate pruning audit

> DISPOSITION: RETAINED_OPEN

제거한 reconstruction 후보가 나중에 중요해질 수 있으므로, 왜 제거했는지와 다시 생성할 recipe를 남겨야 합니까?

## Q-097 · P0 — Reconstruction confidence semantics

> DISPOSITION: RETAINED_OPEN

confidence를 단일 확률처럼 쓰지 않고 evidence coverage, path plausibility, model uncertainty, View stability를 분리해야 합니까?

## Q-098 · P0 — Uncertainty propagation

> DISPOSITION: RETAINED_OPEN

여러 inferred relations을 합성할 때 uncertainty를 어떤 법칙으로 전달할지 operator별 contract를 요구할까요?

## Q-099 · P1 — Adaptive deepening trigger

> DISPOSITION: RETAINED_OPEN · NOTE: narrowed by OD-025 and OD-027

자동 deepening은 uncertainty threshold뿐 아니라 impact, risk, candidate disagreement, novelty를 함께 고려하도록 해야 합니까?

## Q-100 · P1 — Deepening stop

> DISPOSITION: RETAINED_OPEN

더 펼쳐도 정보이득이 작을 때, budget이 남아 있어도 멈출 수 있는 criterion이 필요합니까?

## Q-101 · P1 — Resolution comparison

> DISPOSITION: RETAINED_OPEN

LOW/HIGH View의 결과를 비교할 때 distinction preservation, information loss, compute cost 중 어떤 metric을 INIT Gate에 포함할까요?

## Q-102 · P1 — Multiple high-resolution Views

> DISPOSITION: RETAINED_OPEN

서로 다른 View의 고해상도 복원이 충돌할 때 더 높은 meta-View로 비교할까요, 충돌 자체를 State로 보존하면 충분합니까?

## Q-103 · P1 — Reconstruction Control

> DISPOSITION: RETAINED_OPEN

연구자가 “이 path는 가능하지 않다고 가정”하는 Control을 reconstruction candidate graph에 적용할 수 있어야 합니까?

## Q-104 · P1 — Reconstruction replay

> DISPOSITION: RETAINED_OPEN

INFERRED candidate를 나중에 새로운 evidence로 다시 계산했을 때 identity를 유지하며 confidence만 갱신할까요, 새 candidate State를 만들까요?

## Q-105 · P1 — Attribute expansion

> DISPOSITION: RETAINED_OPEN

surface attribute notation을 펼쳤을 때 exact relation path를 반드시 제공해야 합니까, 아니면 opaque external assignment도 허용합니까?

## Q-106 · P2 — Cross-model reconstruction

> DISPOSITION: RETAINED_OPEN

서로 다른 AI model이 제안한 high-resolution path를 같은 candidate space에서 비교할 수 있도록 model-independent interface를 요구할까요?

## Q-107 · P2 — Human reconstruction input

> DISPOSITION: RETAINED_OPEN

사람의 해석도 reconstruction candidate로 넣되, AI candidate와 동일한 evidence/lineage contract를 적용할까요?

## Q-108 · P2 — Reconstruction cache invalidation

> DISPOSITION: RETAINED_OPEN

새 evidence가 추가·삭제되면 어떤 candidate를 최소 비용으로 invalidation/recompute할지 provenance dependency를 필수로 둘까요?

## Q-109 · P2 — Resolution as one View or View family

> DISPOSITION: RETAINED_OPEN

`VIEW:HIGH`를 하나의 generic View로 둘까요, structural/temporal/semantic/latent resolution별 View를 따로 둘까요?

## Q-110 · P2 — Maximum useful resolution

> DISPOSITION: RETAINED_OPEN

유일한 maximum은 없지만 목적별 “충분히 높은 해상도”를 선언할 수 있어야 합니까? 그 criterion은 측정 가능한 requirement로만 정의할까요?

---

# G. MINIMUM RECOMPUTE AND DEPENDENCY

## Q-111 · P0 — Dependency capture minimum

> DISPOSITION: RETAINED_OPEN

relation-level delta propagation을 위해 모든 operator가 exact dependency를 남겨야 합니까, 아니면 일부 opaque operator는 coarse dependency만 제공해도 됩니까?

## Q-112 · P0 — Correctness over minimality

> DISPOSITION: RETAINED_OPEN

최소 계산 경로와 full recompute 결과가 다를 때 항상 full recompute를 기준 oracle로 둘까요?

## Q-113 · P0 — Incremental fallback threshold

> DISPOSITION: RETAINED_OPEN

부분 갱신이 full recompute보다 비싸지는 경우 runtime이 자동 전환할 수 있어야 합니까? 이 전환은 replay envelope에 기록할까요?

## Q-114 · P0 — Dependency across folded boundaries

> DISPOSITION: RETAINED_OPEN

View/State가 접혀 있어도 내부 dependency를 전부 보존할까요, coarse boundary dependency와 on-demand expansion으로 충분합니까?

## Q-115 · P0 — Deletion propagation

> DISPOSITION: RETAINED_OPEN

관계 하나가 삭제되었을 때 derived State를 invalidation만 할지 즉시 recompute할지 policy로 제어할 수 있어야 합니까?

## Q-116 · P0 — Non-monotonic change

> DISPOSITION: RETAINED_OPEN

삭제, negation, rule change처럼 기존 결과를 철회해야 하는 경우를 INIT 핵심 Probe로 둘까요?

## Q-117 · P1 — Update amplification Gate

> DISPOSITION: RETAINED_OPEN

작은 delta가 너무 많은 downstream work를 요구하면 View/Composition 설계 자체를 나쁜 후보로 평가할까요?

## Q-118 · P1 — Cached State trust

> DISPOSITION: RETAINED_OPEN

부분 계산 후 cached State가 stale인지 검증하는 invariant/checksum을 요구할까요?

## Q-119 · P1 — Cross-branch sharing

> DISPOSITION: RETAINED_OPEN

Branch들이 공통 계산을 공유하되, identity와 isolation을 해치지 않는 structural sharing을 runtime 최적화로 허용할까요?

## Q-120 · P1 — Shared relation update

> DISPOSITION: RETAINED_OPEN

같은 relation이 여러 View에 참여할 때 update를 한 번 계산해 공유할지, View별 delta semantics가 달라 별 계산할지 operator가 결정하게 할까요?

## Q-121 · P1 — Dynamic dependency discovery

> DISPOSITION: RETAINED_OPEN

AI 또는 runtime이 execution 중 새로운 dependency를 발견하면 dependency graph 자체를 versioned State로 갱신할까요?

## Q-122 · P1 — Demand-driven observation

> DISPOSITION: RETAINED_OPEN

관측 요청이 없으면 downstream State를 계산하지 않고 delta recipe만 유지하는 lazy mode를 기본으로 둘까요?

## Q-123 · P2 — Approximate incremental update

> DISPOSITION: RETAINED_OPEN

정확한 minimal update가 비싼 경우 approximate State를 먼저 제공하고 뒤에서 deepening하는 것을 허용할까요? 정확성 표시는 어디에 붙입니까?

## Q-124 · P2 — Resource-aware View

> DISPOSITION: RETAINED_OPEN

계산 budget 때문에 해상도를 낮추는 것은 runtime choice입니까, 결과가 달라지므로 별 VIEW identity입니까?

## Q-125 · P2 — Hardware/runtime portability

> DISPOSITION: RETAINED_OPEN

다른 runtime에서 계산 순서가 달라져도 semantic State가 같으면 replay 성공으로 볼까요?

---

# H. CYCLES, EVENTS, DYNAMIC PATTERNS

## Q-126 · P0 — Cycle semantics declaration

> DISPOSITION: DUPLICATE_OF_Q023 · SUBSTANTIVE_STATUS: OPEN

cycle을 접은 Relation/View는 fixed-point, transition stream, periodic pattern 중 어떤 semantics인지 명시해야 합니까?

## Q-127 · P0 — Oscillation identity

> DISPOSITION: RETAINED_OPEN

주기와 진폭이 같은 두 dynamic pattern을 같은 State로 볼지, 내부 path가 다르면 분리할지 View-relative rule이 필요합니까?

## Q-128 · P0 — Divergence handling

> DISPOSITION: RETAINED_OPEN

DIVERGING pattern도 다음 Composition의 Subject로 허용합니까, 아니면 sandbox observation에만 제한합니까?

## Q-129 · P0 — Budget stop semantics

> DISPOSITION: RETAINED_OPEN

BUDGET_STOP은 계산 실패입니까, partial State입니까, dynamic pattern candidate입니까?

## Q-130 · P1 — Event vs State

> DISPOSITION: RETAINED_OPEN

Event를 별 primitive로 둘 필요 없이 State transition Relation으로 표현하면 충분합니까, 아니면 replay·ordering·fairness를 위해 event occurrence를 별 operational record로 유지해야 합니까?

## Q-131 · P1 — Out-of-order events

> DISPOSITION: RETAINED_OPEN

늦게 도착한 event가 과거 State와 현재 State를 모두 바꿀 때 versioned lineage와 minimum recompute를 어떻게 보존해야 합니까?

## Q-132 · P1 — Cycle Control

> DISPOSITION: RETAINED_OPEN

cycle을 약화·증폭·중단하는 Control을 적용할 때 target을 relation path, pattern State, View 중 어디로 지정할 수 있어야 합니까?

## Q-133 · P1 — Dynamic pattern folding

> DISPOSITION: TERMINOLOGY_UPDATE_ONLY · SUBSTANTIVE_STATUS: OPEN · RELATED_OD: OD-060 · WITNESS: Q-020

긴 transition history를 Pattern State로 접을 때 의미 보존 FOLD입니까, semantic View abstraction입니까? 둘을 구분할 witness가 필요합니까?

## Q-134 · P2 — Fairness

> DISPOSITION: RETAINED_OPEN

프로토콜/agent interaction을 시험할 때 일부 participant가 영구히 굶지 않는 fairness property를 INIT Probe에 포함할까요?

## Q-135 · P2 — Continuous time

> DISPOSITION: RETAINED_OPEN

INIT에서는 discrete event/time만 다루고, dense/continuous dynamics는 reference model에만 둘까요?

---

# I. AI CANDIDATE DISCOVERY AND LATENT CONTROL

## Q-136 · P0 — AI proposal contract

> DISPOSITION: RETAINED_OPEN

AI가 Relation/View/Control candidate를 제안할 때 최소한 interfaces, evidence refs, expected metrics, uncertainty, budget을 제출해야 합니까?

## Q-137 · P0 — AI candidate validity

> DISPOSITION: RETAINED_OPEN

형식적으로 compose 가능하다는 것과 의미적으로 유용하다는 것을 별 Gate로 분리할까요?

## Q-138 · P0 — Promotion prohibition default

> DISPOSITION: RETAINED_OPEN · NOTE: narrowed by OD-005 and OD-006

ASA INIT 기본 policy는 AI가 직접 promotion하지 못하도록 할까요, 아니면 특정 low-risk scope에서는 자동 승격을 시험할까요?

## Q-139 · P0 — AI branch budget

> DISPOSITION: RETAINED_OPEN

AI가 branch를 무한 생성하지 못하도록 View family·Control family별 compute/storage budget을 Owner가 제어할 수 있어야 합니까?

## Q-140 · P0 — Candidate diversity

> DISPOSITION: RETAINED_OPEN

AI가 score가 비슷한 후보를 pruning할 때 서로 다른 high-resolution paths의 diversity를 보존하는 metric이 필요합니까?

## Q-141 · P1 — AI self-proposed measurement

> DISPOSITION: RETAINED_OPEN

AI가 후보와 함께 평가 metric도 제안할 수 있게 하되, metric 자체를 또 다른 View candidate로 취급할까요?

## Q-142 · P1 — Latent State naming

> DISPOSITION: RETAINED_OPEN

사람이 해석할 수 없는 latent subspace도 `STATE:X`로 address할 수 있으면 충분합니까, 아니면 model/layer/dictionary discriminator를 표면 이름에 강제할까요?

## Q-143 · P1 — Latent Control identity

> DISPOSITION: DUPLICATE_OF_Q069 · SUBSTANTIVE_STATUS: OPEN

같은 steering vector라도 context/model version이 다르면 별 CONTROL identity로 볼까요?

## Q-144 · P1 — Latent off-target Gate

> DISPOSITION: RETAINED_OPEN

Target 효과가 크더라도 collateral spread가 일정 기준을 넘으면 promotion을 금지하는 것을 Core Gate로 둘까요?

## Q-145 · P1 — Latent reconstruction

> DISPOSITION: RETAINED_OPEN · NOTE: narrowed by OD-071

latent Control의 중간 mechanism을 정확히 설명하지 못해도 intervention effect가 반복·측정 가능하면 INIT 통과 후보로 인정할까요?

## Q-146 · P1 — Causal abstraction guard

> DISPOSITION: RETAINED_OPEN

높은 interchange-intervention accuracy만으로 faithful View라고 판단하지 않고, alignment map complexity와 out-of-distribution tests를 반드시 요구할까요?

## Q-147 · P1 — Model drift

> DISPOSITION: RETAINED_OPEN

모델 update 뒤 기존 latent View/Control을 자동 invalidation하고 재검증해야 합니까?

## Q-148 · P2 — Human-readable bridge

> DISPOSITION: RETAINED_OPEN

Human-readable concept와 latent State 사이 mapping은 optional View로 둘까요, 일부 safety-critical Control에서는 필수로 요구할까요?

## Q-149 · P2 — AI candidate authorship

> DISPOSITION: RETAINED_OPEN

AI가 제안한 Composition을 다른 AI가 수정했을 때 lineage authorship을 relation path로 보존할까요?

## Q-150 · P2 — Discovery reward

> DISPOSITION: RETAINED_OPEN

AI candidate search를 단일 utility score가 아니라 controllability·novelty·cost·uncertainty의 multi-objective View로 평가할까요?

---

# J. EVIDENCE, GOVERNANCE, PRIVACY, REPLAY

## Q-151 · P0 — Minimal kernel과 operational types

> DISPOSITION: RETAINED_OPEN

모든 것이 relational하게 표현 가능해도 Principal, Authority, Policy, Signature, Execution은 강한 typed contract로 별도 보존하는 것을 v2.0 공식 원칙으로 승인할까요?

## Q-152 · P0 — Evidence ingress

> DISPOSITION: RETAINED_OPEN

Reality/Source View를 제거한 뒤, Evidence/Data plane의 record가 최초 Subject로 들어오는 순간을 별 ingest relation과 validation contract로 표현할까요?

## Q-153 · P0 — Evidence vs inference

> DISPOSITION: RETAINED_OPEN

직접 기록된 Relation과 AI가 inferred한 Relation을 동일 kernel로 다루되 provenance/evidence strength를 반드시 구분할까요?

## Q-154 · P0 — Privacy deletion vs replay

> DISPOSITION: RETAINED_OPEN

사용자가 evidence 삭제를 요청했을 때 derived State를 재계산해야 하지만 과거 실행 audit도 필요합니다. 삭제된 내용을 복원할 수 없는 tombstone lineage만 남기는 방향이 충분합니까?

## Q-155 · P0 — Right to reset vs data deletion

> DISPOSITION: RETAINED_OPEN

Persona/State reset과 underlying evidence deletion을 별 Control/operation으로 유지할까요?

## Q-156 · P0 — Authorization non-relative identity

> DISPOSITION: RETAINED_OPEN

AuthorityGrant identity와 signature validity는 View-relative equivalence로 합칠 수 없다는 hard invariant를 둘까요?

## Q-157 · P0 — Replay under removed data

> DISPOSITION: RETAINED_OPEN

법적 삭제 후 과거 State를 exact replay할 수 없으면 `UNAVAILABLE_BY_POLICY`를 UNKNOWN과 구분해야 합니까?

## Q-158 · P1 — External side-effect replay

> DISPOSITION: RETAINED_OPEN

결제·메시지·서명 같은 외부 행동은 replay 시 실제로 다시 실행하지 않고 simulation/recorded outcome으로 대체하는 Gate가 필요합니까?

## Q-159 · P1 — Model/tool dependency closure

> DISPOSITION: RETAINED_OPEN

재현을 위해 외부 model/API/tool version을 어느 수준까지 snapshot 또는 hash-reference해야 합니까?

## Q-160 · P1 — Evidence contradiction

> DISPOSITION: RETAINED_OPEN

서로 모순되는 evidence를 하나로 resolve하지 않고 서로 다른 State/View candidates로 보존하는 능력을 INIT에 포함할까요?

## Q-161 · P1 — Trust boundary View

> DISPOSITION: RETAINED_OPEN

Evidence source의 신뢰도를 평가하는 것 역시 View라는 원칙을 적용하되, security allowlist 같은 deterministic policy와 분리할까요?

## Q-162 · P1 — Audit resolution

> DISPOSITION: RETAINED_OPEN

평소 audit은 접은 trace만 유지하고 incident 시 high-resolution trace를 재구성하는 방식이 허용됩니까? 어떤 최소 spine은 항상 보존해야 합니까?

## Q-163 · P2 — Cross-user sharing

> DISPOSITION: RETAINED_OPEN

여러 사용자의 State/View가 공통 relation을 공유할 때 privacy boundary를 relation-local scope만으로 충분히 표현할 수 있습니까?

## Q-164 · P2 — Derived deletion impact

> DISPOSITION: RETAINED_OPEN

evidence 삭제가 View/State/latent adapter에 미친 영향을 어디까지 추적하고 재계산할지 Gate를 capability로 정의할까요?

## Q-165 · P3 — Legal hold

> DISPOSITION: RETAINED_OPEN

삭제 Control과 법적 보존 의무가 충돌할 때 operational governance가 World Model branch보다 우선한다는 hard rule을 둘까요?

---

# K. PERSONA ORCHESTRATION AND ASA INIT GATE

## Q-166 · P1 — Persona naming

> DISPOSITION: RETAINED_OPEN

Persona는 `VIEW:Persona`와 `STATE:Persona` pair로 표현하되, Persona라는 final object type으로 승격하지 않는 방향이 충분합니까?

## Q-167 · P1 — Persona count

> DISPOSITION: RETAINED_OPEN

“Persona가 몇 개인가”는 어떤 View로 구별하느냐에 따라 달라진다는 원칙을 INIT Probe로 실제 검증할까요?

## Q-168 · P1 — Persona succession

> DISPOSITION: RETAINED_OPEN

Persona succession을 source/target State 사이의 directional Relation과 View-relative sameness evidence로 표현하면 충분합니까?

## Q-169 · P1 — Persona evolution Control

> DISPOSITION: RETAINED_OPEN

Persona View/State가 변화할 수 있음과 스스로 변경할 권한이 있음은 분리합니다. INIT에서 어떤 변화까지 자동 sandbox로 허용할까요?

## Q-170 · P1 — Seed View governance

> DISPOSITION: RETAINED_OPEN

사람이 설계한 seed View는 bootstrap 도구이며 final View set이 아닙니다. seed를 교체·폐기할 수 있는 조건과 legacy replay를 Gate에 포함할까요?

## Q-171 · P1 — INIT minimum viable phenomena

> DISPOSITION: RETAINED_OPEN

Persona Orchestration, View Genesis, Evolution 중 최소 몇 가지를 실제로 발생·관측·Control해야 Phase Transition Gate를 통과합니까?

## Q-172 · P1 — INIT performance floor

> DISPOSITION: RETAINED_OPEN

scale threshold를 절대 숫자로 먼저 정하기보다, full recompute 대비 update amplification과 branch cost 개선 비율로 Gate를 정할까요?

## Q-173 · P1 — INIT interpretability floor

> DISPOSITION: RETAINED_OPEN

Human-readable interpretability는 필수가 아니지만, safety-critical promotion에서는 최소한 reproducible measurement와 bounded off-target effect를 요구할까요?

## Q-174 · P1 — Backend replaceability Gate

> DISPOSITION: RETAINED_OPEN

두 backend가 같은 Relation/View/Control fixture를 replay했을 때 어느 정도 semantic equivalence를 보여야 Core replaceability가 성립합니까?

## Q-175 · P1 — Formalism survival test

> DISPOSITION: RETAINED_OPEN

Minimal Relation protocol이 common probes에서 반복적으로 special-case primitive를 요구하면 v2.0을 수정한다는 falsification rule을 Owner Gate로 명시할까요?

## Q-176 · P2 — Candidate A baseline necessity

> DISPOSITION: TERMINOLOGY_UPDATE_ONLY · SUBSTANTIVE_STATUS: OPEN

성능은 낮더라도 이해 가능한 minimal interpreter를 correctness oracle로 반드시 유지할까요?

## Q-177 · P2 — Research plane separation

> DISPOSITION: RETAINED_OPEN

Runtime, formal reference, candidate search plane을 초기 연구에서는 분리하되, production에는 필요한 plane만 남길 수 있게 할까요?

## Q-178 · P2 — Core toolkit boundary

> DISPOSITION: RETAINED_OPEN

`compose/fold/expand/view/control/state/trace/replay/delta_update/branch/promote/measure` 중 ASA INIT이 반드시 제공해야 하는 최소 Tool set은 어디까지입니까?

## Q-179 · P2 — Closure terminology retention

> DISPOSITION: RETAINED_OPEN

Closure라는 말을 capability 이름으로 유지할까요, 아니면 finality 오해를 피하기 위해 `Folded Composition` 또는 다른 용어로 바꿀까요?

## Q-180 · P2 — v2.0 naming

> DISPOSITION: RETAINED_OPEN

이번 개정의 공식 이름을 `ASA Core World Model`, `ASA Relation Composition Protocol`, `ASA Closure Toolkit Core` 중 무엇으로 병기할지 결정할 필요가 있습니까?

---

# L. RECOMMENDED INTERVIEW ORDER

아래 순서는 기술 선택이 아니라, v2.0 protocol을 깨뜨릴 가능성이 큰 capability boundary 순서다.

```text
1. Q-006  Minimal relation kernel과 safety/admissibility typing 경계
2. Q-020  FOLD meaning-preservation witness의 요구 수준
3. Q-036  VIEW의 최소 contract
4. Q-056  CONTROL의 최소 contract
5. Q-076  STATE의 최소 contract
6. Q-091  Historical replay와 possible reconstruction 분리
7. Q-097  Uncertainty를 단일 숫자로 둘지 다축으로 둘지
8. Q-111  Dependency capture의 최소 수준
9. Q-060  Control conflict를 보존할지
10. Q-151 Operational constitution을 공식 분리할지
11. Q-171 ASA INIT minimum viable phenomena
12. Q-178 Closure Toolkit 최소 Tool set
```

### 다음 Owner substantive question 권고

> **Minimal Relation은 방향 사상 하나로 최대한 작게 유지하되, authority·signature·privacy·causal dependency처럼 서로 잘못 대체되면 위험한 관계에는 World Model 밖의 강한 type/admissibility guard를 반드시 두는 것이 맞습니까?**

이 질문은 기술 이름을 고르게 하지 않고, v2.0이 반드시 보존해야 할 안전 제어능력의 경계를 확인한다.

---

# M. QUESTION COVERAGE SUMMARY

```text
RELATION / IDENTITY            = Q-001..015
COMPOSITION / LAWS             = Q-016..035
VIEW                            = Q-036..055
CONTROL                         = Q-056..075
STATE                           = Q-076..090
RECONSTRUCTION / RESOLUTION     = Q-091..110
MINIMUM RECOMPUTE               = Q-111..125
CYCLES / EVENTS / PATTERNS      = Q-126..135
AI / LATENT                     = Q-136..150
EVIDENCE / GOVERNANCE / PRIVACY = Q-151..165
PERSONA / ASA INIT              = Q-166..180

TOTAL QUESTIONS = 180
```
