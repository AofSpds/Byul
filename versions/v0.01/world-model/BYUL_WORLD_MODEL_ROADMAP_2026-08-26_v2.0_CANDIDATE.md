# BYUL World Model Roadmap v2.0 — Candidate

**Date:** 2026-08-26  
**Persona:** BYUL  
**State:** RESEARCH ROADMAP CANDIDATE / NON-NORMATIVE / NOT VALIDATED / NOT FROZEN  
**Supersession:** Roadmap v1.0 remains current until explicit Owner adoption.  
**Review basis:** `BYUL_WORLD_MODEL_DEEP_DESIGN_REVIEW_2026-08-26_v1.0_CANDIDATE.md`  
**Owner questions:** `BYUL_WORLD_MODEL_OWNER_QUESTIONS_2026-08-26_v1.0.md`

## 0. Revision rationale

Roadmap v1.0 correctly introduced CATALOG-first collection, coverage+saturation, Primitive-open admission and early performance concern. v2.0 changes the order and gates because:

- pattern collection before semantic stratification can mix topology, interaction, policy and Transform;
- performance probes placed after broad CATALOG work can discover structural failure too late;
- World Semantics, executable IR and runtime need explicit mission separation;
- FOLD contract and Execution Profile/MoC need independent evidence gates;
- FIRST BYUL must not overfit one thermostat example.

v2.0 therefore continues broad collection while moving the semantic kernel, FOLD contract and small executable probes much earlier.

## 1. Roadmap principles

1. **PRESERVE BEFORE REVISE** — preserve current design and Owner decisions.
2. **MISSION SPLIT** — separate World Semantics, Executable Composition IR, lowering and runtime.
3. **CATALOG BROAD / CORE SMALL** — observe broadly and compress only with evidence.
4. **COMPOSITION-FIRST / PRIMITIVE-OPEN** — evaluate meaning, performance and implementation cost, not reducibility alone.
5. **PROFILE-EXPLICIT** — topology does not imply execution semantics.
6. **OPEN FOLD CONTRACT** — folded executable Compositions expose typed ports and summaries.
7. **STATIC ISLANDS / DYNAMIC BOUNDARIES** — localize flexibility.
8. **PROBE EARLY** — attack runtime/compiler failure before CATALOG saturation.
9. **MEASURE COMBINATIONS** — benchmark individual patterns and their interaction matrix.
10. **NO PREMATURE FREEZE** — V/C/T, Orientation, Causality, Primitive and Grammar remain evidence-gated.

## 2. Parallel research tracks

### Track A — Semantics and CATALOG

- conceptual kernel;
- pattern collection;
- normalization;
- decomposition witnesses;
- Primitive pressure;
- formal/open-system Composition.

### Track B — Execution and Lowering

- Execution Profiles/Models of Computation;
- reference interpreter;
- static scheduling and state-machine lowering;
- bounded dynamic runtime;
- FOLD interfaces and adapters.

### Track C — Evidence and Validation

- benchmark harness;
- semantic conformance tests;
- performance interaction matrix;
- flexibility/complexity metrics;
- fail-fast architecture gates.

The tracks are iterative and feed back into one another rather than forming one serial queue.

## 3. Phase overview

- **R0 — Baseline & Source Lock:** preserve exact current refs and candidate provenance. Exit G0.
- **R1 — Mission & Success Contract:** define BYUL product identity, target workloads and success envelope. Exit G1.
- **R2 — Semantic Stratification:** separate layer model and role/facet map. Exit G2.
- **R3 — Open Composition & FOLD Contract:** define ports, boundaries and summary schema. Exit G3.
- **R4 — Prior-Art Atlas & CATALOG Schema:** normalize candidate analysis card. Exit G4.
- **R5 — Probe IR & Reference Interpreter 0:** implement minimal executable semantics. Exit G5.
- **R6 — Execution Profile Atlas:** define initial MoCs/profiles and adapters. Exit G6.
- **R7 — Broad Pattern Collection & Normalization:** expand observed pool and normalized CATALOG. Exit at saturation checkpoint.
- **R8 — Decomposition & Primitive Pressure:** collect witnesses and counterexamples. Exit G7.
- **R9 — Performance/Flexibility Probes:** benchmark profiles and pattern combinations. Exit G8.
- **R10 — Primitive Admission:** admit, defer or reject candidate Primitives with evidence. Exit G9.
- **R11 — Composition Algebra / Grammar:** produce Grammar v0.x. Exit G10.
- **R12 — Syntax / Tooling / Lowering Skeleton:** parser, canonical IR, diagnostics and backends. Exit G11.
- **R13 — FIRST BYUL Acceptance Suite:** three or four vertical slices. Exit G12.
- **R14 — Scale & Heterogeneity:** scale curves and placement findings. Exit G13.
- **R15 — v0.3 Consolidation:** Relation Composition CATALOG v0.3 and Owner freeze decision.

## 4. Detailed phases

### R0 — Baseline & Source Lock

**Goal:** preserve Current Design Status v1.1, Roadmap v1.0, this deep review, Owner Q&A and exact Git refs without mixing adopted and candidate decisions.

**Artifacts:** source index, decision log and explicit `OPEN / ADOPTED / REJECTED / CANDIDATE` status.

**G0:** a fresh channel can reconstruct both the current baseline and candidate review.

### R1 — Mission & Success Contract

**Goal:** define what the first BYUL product is and what success means.

Questions include World Model only, semantic IR/modeling language, coordination DSL, general-purpose language and runtime/platform.

**Recommended baseline:** `World Semantic Model + Executable Coordination IR/DSL first`; defer general-purpose runtime.

**Required decisions:** priority workloads, performance envelope, external kernel policy, determinism and time requirements.

**Artifacts:** `BYUL_TARGET_AND_SUCCESS_CONTRACT_v1.0` and benchmark baseline policy.

**G1:** FIRST BYUL scope and failure criteria are fixed in writing.

### R2 — Semantic Stratification

Separate:

```text
World Semantics
Open Composition IR
Semantic Facets / Contracts
Execution Profile
Lowering / Runtime
```

Research binary Relation applicability, multi-port Interaction pressure, V/C/T facet separation, topology versus behavior versus observation, possible versus realized intensional representation, and Orientation/Causality boundaries.

**Artifacts:** layer diagram, canonical terminology, anti-conflation rules and Primitive-pressure shortlist.

**G2:** one concept is not silently used with incompatible meanings across two layers.

### R3 — Open Composition & FOLD Contract

**Goal:** make Composition independently connectable and replaceable.

Mandatory summary fields:

- ports/types;
- cardinality/rates/bounds;
- Execution Profile;
- guards/contracts/policies;
- effects/state/time/resources;
- ordering/synchronization;
- determinism;
- failure/cancellation;
- topology mutability;
- refinement/lowering witness.

**Artifacts:** `FOLD_INTERFACE_CONTRACT_v0.x`, substitutability tests and EXPAND/FOLD round-trip rules.

**G3:** upper-level compiler/analysis can make the required decisions without internal EXPAND, and replacement preserves declared observable behavior.

### R4 — Prior-Art Atlas & CATALOG Schema

Create Candidate Card v2 before large-scale collection. Each important candidate records:

1. identity, aliases and domain;
2. topology, ports and cardinality;
3. interaction semantics;
4. Execution Profile;
5. state/time/effect/resource requirements;
6. possible versus realized behavior;
7. decomposition witness;
8. semantic fidelity and naturalness;
9. FOLD contract;
10. static/dynamic fraction;
11. locality, communication and synchronization;
12. lowering options;
13. performance cliffs;
14. Primitive pressure;
15. source route and evidence state.

**Artifacts:** prior-art atlas, observed-pattern template and normalized-catalog template.

**G4:** aliases are controlled and topology, interaction, policy and Transform are not mixed.

### R5 — Probe IR & Reference Interpreter 0

**Goal:** execute the smallest semantics before Grammar is frozen.

Initial scope:

- typed ports;
- Relation/Composition;
- basic branch/merge;
- guard;
- pure Transform;
- explicit state/delay;
- FOLD interface;
- trace output.

The reference interpreter is a semantic oracle, not the production architecture. Do not claim production performance from it.

**G5:** micro examples execute consistently and preserve EXPAND/FOLD traces.

### R6 — Execution Profile Atlas

Do not force one universal runtime. Initial profiles:

- Static Dataflow / Fixed-Rate;
- Event / FSM;
- Async FIFO / Process Network;
- Rendezvous / Connector;
- Timed / Discrete Event;
- Bounded Dynamic Topology.

Each profile declares activation/firing rule, communication discipline, scheduling freedom, determinism, state/time semantics, deadlock/progress condition, allowable topology mutation and lowering targets.

Cross-profile adapters declare buffer/sample/clock conversion, event-to-signal or signal-to-event conversion, sync/async bridging and ownership/effect boundaries.

**G6:** at least two profiles are structurally distinguished in the Open Composition IR, and adapters do not erase their semantics.

### R7 — Broad Pattern Collection & Normalization

Collect by Coverage + Saturation across:

- topology;
- choice/activation;
- synchronization;
- multiplicity;
- routing/distribution;
- interaction/transport;
- recurrence;
- temporal;
- failure/cancellation;
- resource;
- dynamic topology;
- hierarchy/abstraction;
- absence pressure set.

Counts such as 30–50 seed or 70–120 broad are references, not gates. Saturation is signaled when recent candidates map stably to existing families/signatures and new Primitive pressure becomes rare.

**Parallel rule:** continuously feed R5/R6/R9 probe findings back into the CATALOG.

### R8 — Decomposition & Primitive Pressure

Classify each candidate as:

- `DIRECT GRAMMAR/OPERATOR CANDIDATE`;
- `DERIVED PATTERN`;
- `PROFILE-SPECIFIC CONSTRUCT`;
- `PRIMITIVE PRESSURE`.

Evaluate expressibility, semantic fidelity, decomposition size, hidden-state/meta-rule count, analyzability, lowering quality and runtime cost.

**G7:** every high-cost/high-frequency candidate has a witness or counterexample.

### R9 — Performance/Flexibility Probes

Benchmark before Grammar. Families include:

- straight-line Transform;
- static branch/switch;
- fan-out/fan-in;
- AND/OR/K-of-N join;
- feedback/delay;
- queue/backpressure;
- timeout/retry/cancel;
- bounded dynamic routing;
- spawn/retire/rebind;
- nested FOLD calls;
- distributed cyclic progress.

Measure throughput, p50/p99 latency, allocation/op, dispatch/op, synchronization/op, scheduler overhead, memory footprint, graph/IR size, compile/specialization time, code size and cross-profile adapter cost.

Compare with handwritten C/Rust or equivalent, reference interpreter, profile-specific optimized lowering and established runtimes where appropriate.

High-risk interaction combinations include dynamic topology + global synchronization, quorum + timeout + cancellation, dynamic-N distribution + resource contention, recurrence + topology mutation, opaque FOLD + unknown effects and arbitrary routing + global optimization.

**G8 Architecture Viability Check:** HOLD/REDESIGN if local work structurally requires whole-network scans, nearly all operations require dynamic lookup/dispatch, local joins require global barriers, FOLD loses effect/dependency information, topology mutation contaminates static regions, common patterns explode into huge graphs/meta-rules, or no efficient lowering witness exists.

### R10 — Primitive Admission

Admit a Primitive only with evidence of one or more:

- non-expressibility;
- semantic distortion;
- unnatural non-minimal decomposition;
- material implementation/performance advantage;
- stable reusable meaning;
- useful compiler/runtime optimization handle.

Focus candidates include Port/Boundary, Interaction, Effect, State/Delay, Time/Clock, Resource/Ownership and Topology Rewrite.

**G9:** every adopted Primitive has a witness and counterfactual comparison.

### R11 — Composition Algebra / Grammar

Define compact grammar and semantics for sequential/parallel composition, branch/merge, feedback/recurrence, interaction/join, routing activation/distribution, FOLD/EXPAND, profile annotation, contracts/guards/effects and error/undefined handling.

Test associativity/identity domains, profile-specific closure, boundary substitutability and determinism/refinement properties.

**G10:** representative CATALOG cases fit without exception explosion.

### R12 — Syntax / Tooling / Lowering Skeleton

Artifacts:

- textual syntax;
- canonical machine IR;
- parser/formatter;
- type/contract checker;
- visualizer and EXPAND/FOLD explorer;
- reference backend;
- static FSM/dataflow backend;
- diagnostics with source route.

**G11:** syntax sugar and canonical IR are reversible enough for analysis, and errors appear during compile/analyze rather than as hidden runtime failures.

### R13 — FIRST BYUL Acceptance Suite

FIRST BYUL is not one overfitted demo. It includes at least:

- **A. Static/Timed Control:** feedback, state, delay, condition and static lowering;
- **B. Async Routing/Coordination:** multicast, K-of-N, timeout, retry, cancellation, failover and queue/state-machine lowering;
- **C. Bounded Dynamic Topology:** spawn/retire/rebind with isolation of static regions;
- **D. Optional High-Performance Kernel:** SIMD/GPU/data pipeline and external/native lowering comparison.

**G12:** micro-to-macro FOLD/EXPAND, reference/optimized observable consistency, at least one efficient static-path lowering, localized dynamic cost and explicit CATALOG coverage gaps.

### R14 — Scale & Heterogeneity

Test large graphs, distributed deployment, mixed CPU/GPU/DB/service targets, multi-profile hierarchy, incremental compilation and partial reload/reconfiguration.

**G13:** scale curves and performance cliffs are measured, and resource/locality placement strategy exists.

### R15 — v0.3 Consolidation

Artifacts:

- Relation Composition CATALOG v0.3;
- Primitive register;
- Grammar v0.x;
- Profile atlas;
- FOLD contract;
- benchmark/viability evidence;
- OPEN questions;
- rejected alternatives and reasons.

v0.3 is not an automatic freeze. The Owner decides the selected baseline, OPEN set and next implementation scope.

## 5. Ordering and parallelism

```text
R0 -> R1 -> R2 -> R3
               |-> R4 -> R7 -> R8 -> R10 -> R11
               |-> R5 -> R6 -> R9 -----------|
                                             v
                                      R12 -> R13 -> R14 -> R15
```

The key revision is that R5/R6/R9 are not deferred until CATALOG saturation.

## 6. Relative effort and Owner checkpoints

Calendar estimates follow the R1 target decision. Current relative effort only:

- R0–R1: S — mission and performance-envelope approval;
- R2–R3: L — semantic layer and FOLD contract direction;
- R4–R7: XL — CATALOG scope and profile coverage;
- R5–R6: L — probe architecture and initial profiles;
- R8–R10: XL — Primitive admission;
- R9: L–XL depending on benchmark scope;
- R11–R12: XL — Grammar/Syntax candidate;
- R13: L — FIRST BYUL acceptance;
- R14–R15: XL — scale evidence and v0.3 baseline.

`S/L/XL` describes relative research/implementation amount, not calendar duration.

## 7. Immediate next actions

1. Obtain the Priority-0 decisions in Owner Questions v1.0 that change R1 scope.
2. Write `Semantic Stratification Note v0.1`.
3. Define Candidate Card v2 schema.
4. Draft the minimum FOLD Interface Summary.
5. Continue CATALOG collection using the v2 schema.
6. Limit Probe IR 0 to a one-page specification.
7. Start with `static branch + state/delay + FOLD`.
8. Then test `K-of-N join + timeout` for semantic pressure.
9. Third, test bounded spawn/retire.

## 8. Freeze boundary

This roadmap does not freeze:

- final ontological status of Relation;
- V/C/T finality;
- Interaction/Port Primitive adoption;
- Orientation/Causality;
- exact Execution Profiles;
- Grammar/Syntax/runtime;
- performance PASS or production/AAA application.
