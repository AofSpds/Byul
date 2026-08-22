# 105. Owner interview protocol — Scope each question to avoid repeated generic answers

```text
STATUS = OWNER_INTERVIEW_PROTOCOL / PROCESS_CORRECTION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:37 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "질문의 스코프를 정해주시면 계속 같은 대답이 안나와요. ㅋㅋㅋ"

## Process correction

Future interview questions should explicitly state their scope before asking, so the Owner does not have to repeatedly answer at the wrong abstraction layer.

Recommended scope labels:

- `WORLDVIEW` — foundational/current worldview hypothesis; relation, change, source/target, sameness, composition.
- `VIEW MODEL` — what qualifies as a VIEW, abstraction/loss/preservation, routing, lifecycle, performance.
- `PERSONA` — Persona orchestration, succession/lineage, split/merge, memory/history, organization.
- `IMPLEMENTATION` — concrete data model, storage, API, runtime, algorithm, representation choice.
- `EVALUATION` — how candidate Views/Persona models are tested or scored.

A question may include a narrower sub-scope when needed, e.g. `PERSONA / SUCCESSION` or `VIEW MODEL / LOSS PROFILE`.

## Guard

Do not ask a broad question whose answer is already fixed at the worldview layer when the actual unresolved issue is Persona or implementation-specific.

Do not treat an answer given in one scope as automatically resolving all other scopes.

## Immediate clarification already obtained

- At the worldview layer, asking whether successive states are "the same" is often not useful under the current hypothesis.
- At the Persona layer, the Owner does consider `succession / lineage` useful.

This distinction should guide follow-up questions.
