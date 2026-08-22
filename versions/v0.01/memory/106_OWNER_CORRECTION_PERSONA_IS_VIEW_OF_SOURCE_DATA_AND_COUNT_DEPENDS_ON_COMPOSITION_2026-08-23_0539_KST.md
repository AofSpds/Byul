# 106. Owner correction — Persona is a View of source data; one/many depends on composition

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / PERSONA-CONCEPT CORRECTION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:39 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "원래 제가 생각하는 페르소나는 하나입니다. 둘이기도 하고 수없이 많을수도 있는 관계 다발입니다. 
>
> 어떻게 조합되느냐입니다.  
> 페르소나의 소스가 되는 데이터를 특정 VIEW로 본것이다 라는 게 제 개념 설계입니다."

## High-fidelity interpretation

The Owner corrects an overly object-like / count-first reading of Persona.

Persona should not be modeled first as a set of independently existing Persona objects that then split or merge.

Current concept:

- Persona is a View-conditioned relation-bundle produced from Persona source data;
- whether there appears to be one Persona, two Personas, or many Personas depends on how the relevant relations/data are composed and viewed;
- Persona count is therefore not foundational;
- composition / selection / abstraction under a View is primary;
- the same underlying source domain may support different Persona projections under different Views;
- what operationally appears as a Persona is the result of viewing/composing source data through a particular Persona-forming View.

Conceptually:

```text
PERSONA SOURCE DATA / RELATIONS
          |
          v
   [ PERSONA-FORMING VIEW ]
          |
          +--> one Persona-like bundle
          +--> two Persona-like bundles
          +--> many Persona-like bundles
          +--> recomposed / overlapping bundles
```

The branches above are illustrative only. They do not imply that one fixed View must output multiple Personas simultaneously.

## Important correction to prior interview framing

The prior question:

```text
P0 -> P1 / P2
```

risked assuming Persona objects as primary entities and then asking about split/succession.

The Owner's current design is instead closer to:

```text
source data / relations
    -> View-conditioned composition
    -> Persona projection(s)
```

Succession / lineage can still be useful at the Persona operational layer, but it is not the foundational Persona construction model.

## Guards

Do not infer:

`PERSONA = ONE FIXED OBJECT`.

Do not infer:

`PERSONA COUNT = STORED GLOBAL FACT`.

Do not infer:

`ONE SOURCE DOMAIN -> ONE PERSONA ONLY`.

Do not infer:

`PERSONA VIEW -> SOURCE DATA IS MUTATED`.

Do not infer:

`PERSONA SOURCE DATA = ONLY MEMORY RECORDS`.

The exact source-domain scope remains open and should be asked explicitly.

## Research consequence

The next Persona questions should focus on the Persona-forming View over source data rather than premature split/merge object mechanics.

A useful unresolved axis is:

> What belongs to the Persona source domain: only stored memory/experience/profile data, or a broader set of relations including current context, goals, external interactions, roles, environment, and other world relations?

This should be asked under explicit scope `PERSONA / SOURCE DOMAIN`.
