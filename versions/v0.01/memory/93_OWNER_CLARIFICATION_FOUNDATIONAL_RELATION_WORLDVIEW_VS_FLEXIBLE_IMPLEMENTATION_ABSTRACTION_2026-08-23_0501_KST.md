# 93. Owner clarification — Foundational relation worldview is distinct from flexible implementation abstraction

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / IMPLEMENTATION-SEPARATION CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:01 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "아 기본 세계관은 그렇고 실구현은 뭐 .. 이 세계관 위에서 어떻게 추상화하느냐는 여러 방법이 있겠지요. 
>
> 네 당연히 관계가 생깁니다."

## High-fidelity interpretation

The Owner draws an explicit boundary between the **foundational/current worldview hypothesis** and the **implementation abstraction strategy**.

Current framing:

- foundational/current worldview hypothesis: the world is interpreted relation-first, with transient source/target roles, mutable relation networks, and View-conditioned abstractions;
- implementation is not required to mirror that worldview literally at every layer;
- practical implementations may use objects, records, graph nodes, relational tables, reification, event logs, functions, rule systems, or other abstractions if they are useful;
- those implementation structures are Views / abstractions built over the relation-first worldview, not claims that the underlying worldview has changed;
- therefore multiple implementation strategies can coexist or be selected for different domains, resolutions, performance constraints, or purposes.

Concise distinction:

```text
FOUNDATIONAL / CURRENT WORLDVIEW HYPOTHESIS
    relation-first / dynamic / View-conditioned

IMPLEMENTATION ABSTRACTION
    many possible encodings / data models / algorithms / representations
```

The Owner also confirms the interactional point raised in the preceding question:

- when a person relation-bundle encounters / acts in the world, relations necessarily arise;
- therefore View formation/use need not be modeled as a purely internal event disconnected from the world;
- however no single canonical formula such as `Person + World + Purpose -> View` is fixed yet.

## Important guards

Do not infer:

`RELATION-FIRST WORLDVIEW -> IMPLEMENTATION MUST BE PURE RELATION GRAPH`.

Do not infer:

`OBJECT/DB/REIFIED IMPLEMENTATION -> OBJECT-FIRST ONTOLOGY`.

Do not infer:

`PERSON-WORLD RELATION EXISTS -> VIEW MUST ALWAYS BE GENERATED ONLY FROM PERSON-WORLD INTERACTION`.

The relation-first worldview constrains interpretation, not one mandatory implementation encoding.

## Research consequence

BYUL should explicitly evaluate abstraction/implementation strategies **on top of** the current relation-worldview rather than conflating worldview selection with data-model selection.

This suggests a two-layer research discipline:

1. **Worldview / model assumptions** — what is being hypothesized about relation, change, identity, View, source/target, abstraction, and purpose.
2. **Representation / implementation experiments** — which existing techniques most effectively realize useful Views under practical constraints.

PRIOR-ART-FIRST remains active; implementation freedom is a feature of the research program, not evidence that the foundational hypothesis is meaningless.
