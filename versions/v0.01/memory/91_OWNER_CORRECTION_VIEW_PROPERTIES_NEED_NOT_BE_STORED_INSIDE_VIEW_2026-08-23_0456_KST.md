# 91. Owner correction — VIEW properties need not be stored inside a VIEW object

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / CORRECTION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:56 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "VIEW에 속성이 담겨야 하는지는 모르겠습니다."

## Correction

Do not assume a container/object model in which VIEW contains fields such as `scope`, `resolution`, `purpose`, `routing`, or `temporal_scope`.

The current relation-first hypothesis only requires that some relation / relation-bundle can be distinguished or used as a VIEW because of how it participates in a larger relation network.

Possible descriptions such as:

```text
V.scope
V.resolution
V.routing
```

are explanatory shorthand only and must not be treated as an implementation or ontology commitment.

An equally compatible relation-centric representation is:

```text
V <-> SCOPE relation
V <-> RESOLUTION relation
V <-> ROUTING relation
V <-> TEMPORAL relation
V <-> PURPOSE relation
```

or another prior-art-grounded representation entirely.

## Current open question

The meaningful research question is not yet `what fields belong inside VIEW?` but rather:

> what relational pattern / capability / behavior makes a relation or relation-bundle function as a VIEW?

This may ultimately be characterized structurally, behaviorally, operationally, relationally, or by a combination of those approaches.

## Guard

- `VIEW HAS PROPERTIES` does not imply `VIEW STORES PROPERTIES AS FIELDS`.
- `VIEW IS A RELATION` does not imply a specific graph/node/edge encoding.
- `VIEW-NESS` may be role-like or relational rather than a fixed class/type; this remains OPEN.
- no canonical VIEW schema, field set, metadata model, execution contract, or persistence representation is fixed by this note.
