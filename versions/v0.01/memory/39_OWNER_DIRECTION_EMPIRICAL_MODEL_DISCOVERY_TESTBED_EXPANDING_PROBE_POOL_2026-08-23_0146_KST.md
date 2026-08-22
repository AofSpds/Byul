# 39. Owner Direction — Empirical Model-Discovery Testbed and Expanding Probe Pool

```text
STATUS = OWNER_DIRECTION / RESEARCH_METHOD_CORRECTION
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 01:46 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "우리는 지금 테스트항목과 근거가 없어요.필요한건 좋은 모델을 나올수 있게하는 거푸집같은 것이지요.
>
> 그래서 어느정도 모델 테스트 풀을 만들어 놓고 여러가지 요구사항에 대해 우리의 데이터를 갖고 싶어요. 일단 파일럿 세개 프로브 리뷰해보고 다음엔 더 필요한 거푸집?은 용어가 적당치 않은데 하여튼 그런게 더 필요하다는 리서치기 나오면 다시 확보하는 그런 걸 생각해보고 싶어요.
>
> 추정과 실증은 다르니까요"

## Correction to prior framing

The immediate goal is **not** to claim that BYUL already has a justified benchmark specification, fixed test items, or grounded scoring rules.

The near-term research objective is to construct an **empirical model-discovery testbed / expanding probe pool** that can:

- expose candidate models to heterogeneous real workload pressures;
- generate empirical observations about what information, semantics, lineage, context, constraints, and reconstruction capabilities actually matter;
- reveal missing requirements rather than presuppose them;
- provide data for revising, simplifying, rejecting, or generating successor model hypotheses;
- expand when research reveals an untested failure surface or preservation demand.

The initial three probes (TriliumNext / Joplin / Grist) are therefore not a final benchmark suite and are not justified as complete test coverage. They are an initial low-cost **probe set** intended to produce evidence and identify what further testbeds/probes are needed.

## Preferred terminology

Working terms:

- `MODEL_DISCOVERY_TESTBED`
- `EMPIRICAL_PROBE_POOL`
- `EXPANDING_WORKLOAD TESTBED`

Avoid treating `BENCHMARK` as the primary near-term label if that implies a frozen, already-justified scoring contract.

The Owner's intuitive word `거푸집` captures the desired role: not a final exam, but an experimental structure that helps stronger candidate models emerge and exposes where they fail.

## Research loop

```text
BRAINSTORM / PRIOR ART
        ↓
LIGHT PROBE DESIGN
        ↓
EMPIRICAL RUN
        ↓
RAW OBSERVATION / FAILURE / COST / LOSS DATA
        ↓
REQUIREMENT & HYPOTHESIS REVISION
        ↓
GAP RESEARCH
        ↓
ADD / MODIFY / RETIRE PROBES
        ↓
SUCCESSOR MODEL CANDIDATES
        ↺
```

Only after sufficient empirical evidence accumulates should the project consider freezing a narrower benchmark/evaluation suite with grounded test items and scoring rules.

## Epistemic guard

`HYPOTHESIS != EMPIRICAL EVIDENCE`

- A philosophically attractive or theoretically coherent requirement is not automatically a validated test requirement.
- A single successful probe does not validate a general model requirement.
- A repeated failure pattern across heterogeneous probes is stronger evidence for a requirement than a requirement invented from BYUL's current architecture.
- Probe expansion should be driven by observed gaps, unresolved questions, prior-art comparison, and explicit preservation demands.

## Current implication

The three currently discussed open-source probes should be reviewed as an **initial empirical discovery set**, not as a final tournament and not as evidence that the relevant test dimensions are already known.

No full implementation, benchmark freeze, scoring authority, architecture freeze, or scientific validation is created by this note.
