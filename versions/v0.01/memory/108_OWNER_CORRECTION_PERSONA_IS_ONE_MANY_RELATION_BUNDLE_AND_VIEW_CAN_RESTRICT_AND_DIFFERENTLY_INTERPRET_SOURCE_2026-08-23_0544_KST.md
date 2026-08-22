# 108. Owner correction — Persona is one/many relation-bundle; Persona View may restrict and differently interpret source

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / PERSONA-CONCEPT CORRECTION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:44 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "PERSONA는 기본적으로 하나예요 여럿이기도 하고 공유하고 말고 할게 없어요. 
> 이 페르소나 VIEW는 이걸 못보게 제한을 걸고 다른 친구들이랑 다르게 볼 수도 있고 그런겁니다."

## High-fidelity interpretation

The Owner corrects the prior `shared memory between Personas` framing as still too object-first.

Current concept:

- Persona is fundamentally one relation-bundle that may also be viewed/composed as many; Persona count is View-conditioned rather than foundational;
- therefore `Persona A owns memory X` versus `Persona B shares memory X` is not the right foundational framing;
- the relevant question is how a **Persona-forming View** selects, restricts, combines, and interprets source relations;
- a Persona View may be prevented from seeing some source relations even if those relations exist in the broader source domain;
- two Persona Views may access overlapping source relations but interpret/compose the same relations differently;
- what appears operationally as different Personas can therefore arise from different visibility, selection, composition, resolution, weighting, or interpretation over an underlying relation/source domain.

Conceptually:

```text
broad source relation domain
        |
        +--> Persona View V1
        |      - can see A,B,C
        |      - cannot see D,E
        |      - composes A+B strongly
        |      -> Persona projection P1
        |
        +--> Persona View V2
               - can see B,C,D
               - interprets B,C differently
               -> Persona projection P2
```

`P1` and `P2` above are operational projections, not foundational independent objects that own separate memory stores.

## Important distinction

`SOURCE EXISTS`

is separate from:

`THIS PERSONA VIEW MAY SEE / USE / INTERPRET SOURCE`.

This introduces at least two Persona-View dimensions:

1. **visibility / admissibility** — which source relations may enter the View;
2. **interpretation / composition** — how admitted relations are combined, weighted, abstracted, or understood.

The exact implementation of restriction is not yet fixed.

## Guards

Do not infer:

`PERSONA VIEW RESTRICTION -> SOURCE DATA IS DELETED`.

Do not infer:

`DIFFERENT PERSONA -> DIFFERENT PHYSICAL MEMORY STORE`.

Do not infer:

`ONE PERSONA FUNDAMENTALLY -> ONLY ONE OPERATIONAL PERSONA VIEW AT A TIME`.

Do not infer:

`VISIBILITY RESTRICTION -> SECURITY/AUTHORIZATION POLICY ONLY`.

A restriction may be part of abstraction, context, purpose, safety, role, access authority, implementation, or another View-conditioned mechanism. The exact governance/mechanism remains open.

## Research consequence

Future Persona questions should focus on Persona-View configuration rather than memory ownership:

- what source relations are visible/admissible?
- what source relations are suppressed or inaccessible?
- how can the same source be interpreted differently?
- how do changing visibility/composition rules alter the Persona projection?
- which restrictions are intrinsic to the Persona View versus imposed by external policy/governance?

The last distinction is a useful next question under explicit scope `PERSONA / VIEW POLICY BOUNDARY`.
