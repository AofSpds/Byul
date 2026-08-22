# 122. Owner idea — Persona/View may be rebuilt on demand; LoRA can be optional materialized execution state

```text
STATUS = OWNER_IDEA / RESEARCH_CANDIDATE / NON-FROZEN
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 07:37 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "View를 그때그때 다시 빚어줄수도 있지 않을까요"

## Scope

`IMPLEMENTATION / PERSONA VIEW / DYNAMIC RECONSTRUCTION`

## High-fidelity interpretation

The Owner proposes that a Persona/View need not exist mainly as one pre-materialized, persistent object or adapter. A View may be re-composed/reconstructed at use time from currently admissible Source, legacy, context, purpose, policy, and prior View lineage.

Conceptually:

```text
current admissible Source
+ retained legacy / lineage
+ current context
+ current purpose
+ access / policy constraints
+ Seed / inherited meta-stance
        ↓
VIEW reconstruction / composition
        ↓
current Persona projection
        ↓
optional execution adaptation
(Base model + selected/cached/generated adapter state)
```

This is highly compatible with the current foundational worldview because View is already treated as dynamic, View-conditioned, and lifecycle-bearing rather than as a fixed immutable object.

## LoRA placement refinement

The prior LoRA candidate should therefore be weakened from `Persona/View implementation` to an optional optimization/materialization mechanism.

Three implementation patterns remain open:

1. `FULL DYNAMIC VIEW`
   - rebuild the relevant Persona View from Source/context/purpose each time;
   - use prompt/context/routing/runtime logic without persistent learned adapter.

2. `HYBRID VIEW + ADAPTER`
   - dynamically build the semantic View;
   - select one or more existing LoRA/adapters to accelerate stable execution tendencies.

3. `VIEW MATERIALIZATION / COMPILATION`
   - when a View pattern becomes sufficiently stable and frequently reused, compile/materialize part of it into a LoRA or other adapter;
   - later invalidate/retrain/replace that adapter if the semantic View changes materially.

No pattern is selected yet.

## Important distinction

`REBUILD VIEW ON DEMAND`

is not the same as:

`RETRAIN LORA ON EVERY REQUEST`.

The former can be implemented with explicit Source selection, retrieval, routing, rules, context construction, graph/query evaluation, or other runtime composition methods.

Training a new LoRA for every interaction would usually introduce latency, compute, provenance, deletion/unlearning, and stability problems and is not required by the concept.

## Architectural consequence

The semantic authority should remain above the adapter layer:

```text
SEMANTIC PERSONA/VIEW STATE
= Source + lineage + visibility + purpose + composition + loss profile + current context

EXECUTION MATERIALIZATION
= prompt/context/cache/adapter/LoRA/other runtime optimization
```

A LoRA may be treated analogously to a cached/materialized View result: useful when stable, disposable/rebuildable when stale, but not authoritative for the underlying Persona meaning.

## Data-governance consequence

Dynamic reconstruction is particularly attractive for mutable/deletable user data because Source deletion can trigger dependency invalidation and subsequent View recomputation without requiring every personal memory to have been irreversibly baked into weights.

Adapters trained on mutable personal Source still require explicit provenance/version/deletion semantics.

## Research consequence

A strong next research axis is not `Should Persona use LoRA?` but:

> Which parts of a Persona/View should remain dynamically reconstructable, and which stable recurring transformations are worth materializing/caching/compiling into learned adapters?

Candidate decision factors:
- change frequency;
- latency budget;
- Source/data size;
- deletion/reset requirements;
- provenance/reconstructability;
- behavioral stability;
- compute/storage cost;
- degree of user-specificity.
