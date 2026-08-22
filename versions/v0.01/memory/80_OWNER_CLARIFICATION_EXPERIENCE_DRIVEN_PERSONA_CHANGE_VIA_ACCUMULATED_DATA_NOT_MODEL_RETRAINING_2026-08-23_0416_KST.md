# 80. Owner clarification — Persona evolution is primarily experience/data-driven adaptation, not LLM-style retraining

```text
STATUS = OWNER_PRIMARY_PURPOSE / CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:16 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 최소인데 기능이라는게 사실 저희가 개발한다기보다 학습개념을 생각하지요. 
> AI 잖아요. 물론 LLM이 학습하듯 한다기보다는 데이터를 쌓는다 우리가 지금 AAA에서 처음 만드는 부가기능 API에 접속 가능한다던가 하는 외부 서비스는 더 지원이 가능하겠지만 
>
> 기본적으로 경험을 하면서 바뀐다는 컨셉은 여기에 있습니다."

## High-fidelity interpretation

The Owner clarifies that the core ASA INIT concept is not primarily to ship a large hand-developed feature set.

The primary mechanism is **experience-driven change through accumulated data/state/relations**.

Current framing:

- ASA INIT should start minimal;
- the system accumulates experience/data over time;
- Persona/View/orchestration state may change as that experience accumulates;
- this should not be conflated with retraining an LLM's model weights in the conventional foundation-model sense;
- external APIs/services may expand what ASA can do, including project-specific capabilities developed in AAA;
- however those external capabilities are auxiliary service surfaces, not the core meaning of "learning" in the current concept.

Conceptually:

```text
ASA INIT minimal seed
    -> interaction / events / outcomes / relationships
    -> accumulated experiential data/state/history
    -> changed interpretation / View / Persona relation bundles
    -> changed orchestration / behavior

plus optional external services/APIs
    -> additional capabilities
```

## Important distinction

```text
EXPERIENCE-DRIVEN ADAPTATION
    !=
FOUNDATION-MODEL WEIGHT RETRAINING
```

and:

```text
EXTERNAL API CAPABILITY EXPANSION
    !=
THE CORE LEARNING MECHANISM
```

The current hypothesis is closer to **stateful, history-bearing adaptation** than to model-training-as-persona-evolution.

## Research implication

BYUL/ASA-MI should therefore study what experiential state must be accumulated so that Persona and View evolution can be observed and tested without prematurely assuming weight updates.

Candidate research objects may include:

- relation history;
- event history;
- memory/state accumulation;
- outcomes and feedback;
- purpose changes;
- View usage and replacement history;
- capability/API usage history;
- Persona split/merge/succession signals.

These are candidate research objects only. No canonical memory schema, learning rule, update algorithm, or automatic mutation threshold is fixed by this note.

## Current concise statement

`ASA INIT LEARNING CONCEPT = EXPERIENCE / DATA / STATE ACCUMULATION -> ADAPTATION`

with the guards:

`NOT NECESSARILY LLM WEIGHT TRAINING`

`NOT PRIMARILY A PREBUILT FEATURE CATALOG`
