# 110. Owner implementation idea — Common View then Persona View as optional multi-stage pipeline

```text
STATUS = OWNER_IMPLEMENTATION_IDEA / NON-FROZEN / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:48 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "모든 소스를 그대로 볼수는 없고, 공통 VIEW라 한번 보고 페르소나VIEW를 한번 더 만들어 둔다던가 하는 생각은 하고 잇어요. 파편화된 아이디어가 있는데, 사실 구현 상황이 어떻게 될지 모르겠어요."

## High-fidelity interpretation

At scope `IMPLEMENTATION / VIEW PIPELINE`, the Owner has an active but intentionally non-frozen implementation idea:

- the full potential source domain is too large to inspect or load directly for every Persona projection;
- therefore one candidate is a multi-stage abstraction pipeline;
- a broader/common View may first select, normalize, index, compress, or otherwise produce a more tractable intermediate relation-domain;
- a Persona-specific View may then operate over that intermediate domain to further restrict/select/compose/interpret relations for the active Persona projection;
- this is a practical implementation candidate, not a foundational ontology claim;
- the Owner explicitly says implementation conditions are not yet known and ideas remain fragmented.

Conceptually:

```text
very large / open source relation domain
        ↓
[ common / broader VIEW ]
        ↓
intermediate selected/normalized/abstracted relation domain
        ↓
[ Persona VIEW ]
        ↓
current Persona projection
```

Other pipelines remain possible, including direct Persona View access to some source relations, multiple common Views, hierarchical Views, cached/materialized layers, or purpose-specific bypasses.

## Important architectural caution

A `common View` should not automatically be treated as the one true canonical world representation.

Under the current worldview hypothesis:

- there is no privileged universal true View;
- a common View can still be useful as an implementation convenience / shared abstraction layer;
- its own loss profile, scope, lifecycle, and limitations should remain explicit;
- Persona Views may need access to source relations that the common View discarded, depending on purpose and required resolution.

Therefore a practical design should avoid silently turning a shared intermediate representation into an irreversible semantic bottleneck.

## Guards

Do not infer:

`COMMON VIEW -> MANDATORY SINGLE GLOBAL VIEW`.

Do not infer:

`PERSONA VIEW -> MUST ONLY READ COMMON VIEW OUTPUT`.

Do not infer:

`MULTI-STAGE PIPELINE -> IMPLEMENTATION DECISION FROZEN`.

Do not infer:

`COMMON VIEW -> SOURCE DATA MAY BE DELETED AFTER ABSTRACTION`.

## Research consequence

The important implementation research question is not whether multi-stage Views are allowed—they are—but how to choose the staging architecture under performance, memory/data-size, latency, freshness, fidelity, and selective high-resolution access constraints.

Candidate forms to later test:

- one shared coarse View + Persona-specific View;
- multiple domain/common Views + Persona composition;
- hierarchical View chain;
- dynamic direct-source bypass for high-resolution needs;
- cached/materialized intermediate Views;
- adaptive routing based on purpose and cost.

No canonical pipeline is selected by this note.
