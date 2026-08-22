# 79. Owner clarification — ASA INIT Bundle as externally delivered base capabilities

```text
STATUS = OWNER_PRIMARY_PURPOSE / CLARIFICATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 04:13 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "INIT BUNDLE 정도? 현재는 내부 조직이라기 보다 
> 바깥에서 API로 받게 하는 기본 기능일거예요."

## High-fidelity interpretation

The Owner corrects the prior interpretation that current AAA Personas such as ASA/PMO/MOD/RES/ENG should be treated as the internal organization of ASSET AGENT ASA.

Current practical framing is closer to **INIT BUNDLE**:

- ASA INIT begins with ASSET AGENT ASA as the initial user/domain-facing realization;
- the first practical seed is not necessarily an internal Persona org chart;
- instead, it is likely a bundle of baseline capabilities/functions available to ASSET AGENT ASA;
- those capabilities may be supplied through external APIs/services/providers;
- orchestration may therefore initially compose externally available capabilities rather than instantiate a mature internal Persona organization;
- later Persona differentiation, internalization, reorganization, or other structures remain open research outcomes.

Conceptually:

```text
USER
  ↕
ASSET AGENT ASA
  ↕
ASA INIT BUNDLE
  ├─ external API capability A
  ├─ external API capability B
  ├─ external API capability C
  └─ seed Views / relation interpretation support
```

This is only a current implementation intuition, not a fixed architecture.

## Important distinctions

Do not infer:

`CURRENT AAA PERSONA ORGANIZATION == ASSET AGENT ASA INTERNAL RUNTIME ORGANIZATION`.

Do not infer:

`API-DELIVERED CAPABILITY == PERMANENTLY EXTERNAL PERSONA`.

Do not infer:

`INIT BUNDLE == FINAL CAPABILITY SET`.

Do not infer:

`EXTERNAL API FUNCTION == VIEW`.

The exact mapping among capability, Persona, View, service, provider, API, and later internalized relation bundle remains OPEN.

## Research implication

A useful current question becomes:

> What is the minimum INIT Bundle of externally available capabilities and seed Views that lets ASSET AGENT ASA begin useful relations with the world without prematurely fixing its future Persona organization?

This reframes ASA INIT from a prebuilt internal organization to a practical bootstrap bundle that can later support empirically discovered Persona structures.
