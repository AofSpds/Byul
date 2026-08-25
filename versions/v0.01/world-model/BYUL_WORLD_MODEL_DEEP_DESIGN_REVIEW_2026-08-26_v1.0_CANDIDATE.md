# BYUL World Model — Deep Design Review & Architecture Recommendation

**Date:** 2026-08-26  
**Persona:** BYUL  
**State:** DEEP REVIEW CANDIDATE / NON-NORMATIVE / NOT VALIDATED / NOT FROZEN  
**Review basis:** Current Design Status v1.1, Roadmap v1.0, current Owner Q&A and primary/official prior-art comparison  
**VALIDATION_CLAIM:** NONE  
**PRODUCTION_AUTHORIZED:** FALSE

## 0. Executive verdict

> **The current BYUL direction is suitable as a research and modeling architecture and has credible potential to become a flexible, high-performance programming foundation. It is not yet suitable for direct implementation as one universal dynamic graph runtime. Doing so would likely lose both performance and flexibility.**

Assessment codes:

- philosophical/conceptual direction: `SUITABLE`;
- Composition-first direction: `SUITABLE`;
- CATALOG-first method: `SUITABLE WITH SCHEMA REVISION`;
- current execution-semantics completeness: `INSUFFICIENT`;
- high-performance potential: `CONDITIONALLY VIABLE`;
- target flexibility potential: `HIGH POTENTIAL`;
- universal graph interpreter as final architecture: `NOT RECOMMENDED`;
- recommended structure: `MULTI-LEVEL SEMANTIC MODEL + EXPLICIT EXECUTION PROFILES + STATIC/DYNAMIC PARTITION + LOWERING`.

There is no evidence that BYUL is a dead-end design. The strongest safeguards already exist: `CONCEPTUAL MINIMUM != IMPLEMENTATION MINIMUM`, `COMPOSITION-FIRST / PRIMITIVE-OPEN`, and `SEMANTICS != RUNTIME`.

The realistic target is not maximum freedom and maximum performance at every point. It is:

> **Keep narrow regions dynamic where flexibility is required; freeze, specialize and compile broad regions where performance matters; achieve high flexibility and high performance at whole-system level.**

Static synchronous dataflow demonstrates that fixed production/consumption rates can eliminate runtime scheduling by compile-time scheduling. Hybrid streaming systems show that dynamic boundaries can coexist with large statically optimized subgraphs. These support `STATIC ISLANDS + EXPLICIT DYNAMIC BOUNDARIES`.

### Most important revisions

1. Separate World Model semantics from executable semantics.
2. Do not freeze V/C/T as peer Primitives; stratify them into semantic facets.
3. Keep binary Relation as conceptual minimum while allowing multi-port/multi-party interactions in executable IR.
4. Separate network topology from execution/interaction semantics.
5. Require an Interface Summary Contract on every executable FOLD.
6. Make dynamic topology an explicit bounded capability, not a global default.
7. Run small executable probes and benchmarks before CATALOG saturation.

### Hard limitation of this review

No parser, canonical IR, scheduler, compiler, runtime or benchmark exists yet. Therefore no claim such as “within X percent of native” is justified. This is an architecture viability judgment based on current design evidence and primary/official prior art. Quantitative performance claims require the revised roadmap’s probes and benchmark gates.

## 1. Scope and method

### Internal design basis

Current Git design states:

- `RELATION : SOURCE -> TARGET` is a conceptual-minimum hypothesis, not physical/storage/implementation minimum;
- Composition is network/bundle-first rather than chain-only;
- V/C/T remain open composition-role candidates;
- FOLD/EXPAND are separate abstraction mechanisms;
- routing, switching, distribution, possible/realized networks, Primitive admission and performance profiles are research targets;
- CATALOG is managed by Coverage + Saturation rather than a fixed count.

Roadmap v1.0 proposes preservation, observed-pattern collection, normalized CATALOG, decomposition, flexibility stress, performance viability, Primitive admission, Grammar, Syntax/Tooling, FIRST BYUL, scale and v0.3 consolidation.

### External comparison set

The review compared BYUL against:

- multi-level compiler IR and lowering: MLIR, TVM;
- heterogeneous Models of Computation: Ptolemy II, ForSyDe;
- coordination and connector composition: Reo, BIP;
- static/dynamic dataflow tradeoffs: SDF, hybrid StreamIt, Kahn/dataflow process networks;
- dynamic specialization: Truffle partial evaluation;
- cyclic distributed progress: Timely Dataflow;
- dynamic-topology formalism: Dynamic I/O Automata;
- open-system/FOLD interfaces: structured cospans;
- algorithm/schedule separation: Halide;
- routing/join diversity: Workflow Patterns.

These sources do not validate BYUL ontology. They are used only to compare how related engineering problems are separated and contracted.

## 2. Design changes produced by the current dialogue

### 2.1 Directionality, Resultant and Orientation are separated

The stronger early interpretation `local directionality -> composite orientation` was weakened.

- `Directionality`: ordered endpoints of an individual Relation.
- `Resultant`: post-hoc net result of a realized Composition under a declared View.
- `Orientation`: higher-order interpretation of non-trivial directional asymmetry, convergence, persistence or constraint, not mere terminal identification.

This is a sound correction. Keeping Orientation as an analysis/interpretation property rather than a routing engine or fourth Primitive reduces unnecessary execution complexity.

### 2.2 Chain examples are replaced by network/routing intent

Normal Composition now includes:

- branch, merge, parallel, loop and many-to-many;
- switching, split, distribution and multicast;
- condition-sensitive routing;
- multi-port interfaces of folded Compositions;
- Composition-of-Compositions.

`Multiple target != conflict` is correct. Real conflict requires incompatible requirements under the same relevant View, Condition and resource boundary.

### 2.3 Grammar, Operator and Derived Pattern are separated

- Grammar/topology describes allowed structural forms.
- Operator/operation changes structure or active routes.
- Derived pattern is a recurring composition of smaller elements.

For example, FAILOVER may decompose into `BRANCH + HEALTH CONDITION + PRIORITY SELECT/SWITCH`. This preserves a broad observed CATALOG while allowing a small core.

### 2.4 Composition-first becomes Primitive-open

Use Composition when existing elements express meaning naturally and efficiently. Admit a Primitive when evidence shows non-expressibility, semantic distortion, unnatural non-minimality, or material implementation/performance disadvantage. The goal is not the smallest Primitive count; it is a small sufficient core.

### 2.5 VOID is not one Primitive

Separate:

- ABSENT;
- EMPTY;
- UNDEFINED;
- UNREALIZED;
- NO-OUTPUT.

These belong to different type, query, execution, realization and interface semantics. Collapsing them into one value would increase errors and reduce optimization opportunities.

### 2.6 CATALOG becomes a two-level collection with a performance track

- Observed Pattern Pool remains broad.
- Normalized Composition CATALOG controls aliases and layer confusion.
- decomposition witnesses and Primitive pressure are recorded.
- each candidate records static/dynamic fraction, locality, state/synchronization/routing cost, FOLD transparency, lowering options and performance cliffs.

This is appropriate, but each candidate must also state its Execution Profile/Model of Computation.

## 3. Suitability assessment

The following scores are expert judgments on current evidence, not measurements.

- **Conceptual neutrality:** current 4.0/5; after revision 4.5/5.
- **Composition scalability:** current 4.0/5; after revision 4.5/5.
- **Semantic-layer clarity:** current 2.0/5; after revision 4.0/5.
- **Heterogeneous execution semantics:** current 1.5/5; after revision 4.5/5.
- **Analyzability/verifiability:** current 2.0/5; after revision 4.0/5.
- **High-performance lowering potential:** current 3.0/5; after revision 4.0/5.
- **Dynamic flexibility:** current 4.0/5; after revision 4.5/5.
- **Implementation readiness:** current 1.5/5; after revision 3.5/5.
- **Long-term dead-end risk:** medium now; low-to-medium after revision.

## 4. Suitable parts that should be preserved

### 4.1 Separate conceptual minimum from implementation minimum

This is the most important survival property. `Relation` as a semantic minimum does not imply a runtime that follows heap Relation objects one by one. Multi-level IR systems allow different abstraction levels to coexist and lower into target-specific forms.

Preserve:

```text
BYUL WORLD SEMANTICS
!= NORMALIZED EXECUTION IR
!= RUNTIME DATA STRUCTURE
!= MACHINE INSTRUCTION
```

### 4.2 Network-first and higher-order Composition

Hierarchical networks with ports/interfaces are a proven way to build open compositional systems. BYUL’s network/bundle-first and FOLD/higher-order direction is therefore engineering-compatible with mature prior work.

### 4.3 CATALOG-first and evidence-based Primitive admission

Broad observation followed by normalization and decomposition is rational. The requirement is that topology, interaction, state, time, effect and Execution Profile are separated on every candidate card.

### 4.4 Static/dynamic choice

The Owner’s willingness to freeze selected freedoms for performance is decisive. Compile-time scheduling in SDF and static subgraph optimization around dynamic streaming boundaries show that flexibility need not be paid everywhere.

## 5. Core weaknesses in the current design

### 5.1 World Model and Programming Model still overlap

World Model asks what is related and composed. Programming Model must define when elements activate, what they read/write, how they synchronize, schedule and fail. If the two are not separated, ontology absorbs CPU/GPU/queue details or runtime pays philosophical freedom on every operation.

**Recommendation:** `Semantic Model -> Open Composition IR -> Execution Profile -> Lowering -> Runtime`.

### 5.2 V/C/T are not the same kind of Primitive

- VIEW mixes observation, projection, abstraction and query.
- CONDITION mixes guard, invariant, contract, policy, eligibility and trigger.
- TRANSFORM mixes pure computation, external effect, state update and topology rewrite.

Freezing them as peer atoms would cause semantic inflation and hide information needed by optimizers.

**Recommendation:** retain the vocabulary but stratify it.

```text
VIEW       -> Observation / Projection facet
CONDITION  -> Guard / Contract / Policy / Trigger facets
TRANSFORM  -> Pure Transform / Effect / State Transition / Topology Rewrite facets
```

### 5.3 Binary Relation should not be forced through the executable layer

`SOURCE -> TARGET` is clean as a conceptual minimum. JOIN, rendezvous, broadcast, quorum and atomic commit involve multiple ports. Encoding all of them as binary chains can create hidden state and arbitrary ordering.

Test two normalized execution representations:

1. a multi-port Interaction node connected to ports by binary Relations;
2. typed hyperedge or m:n operation.

The first preserves the conceptual Relation minimum while isolating atomic multi-party semantics.

### 5.4 Topology does not determine behavior

The same `A -> B` may be blocking rendezvous, asynchronous buffered queue, nonblocking push, pull/request, clocked sample, timestamped discrete event, continuous signal or database relation/query.

**Recommendation:** every executable region declares an explicit Execution Profile/Model of Computation. Initial candidates:

- Static Dataflow / Fixed-Rate;
- Event / FSM;
- Async FIFO / Process Network;
- Rendezvous / Connector;
- Timed / Discrete Event;
- Bounded Dynamic Topology.

### 5.5 FOLD must preserve a typed interface contract

FOLD cannot be mere visual hiding. Every executable FOLD should summarize:

- typed input/output ports;
- cardinality, rate and capacity bounds;
- Execution Profile;
- guards/contracts;
- pure/effectful behavior;
- state/history;
- time/clock/deadline;
- synchronization/ordering;
- determinism/nondeterminism;
- resource/ownership/locality;
- topology mutability;
- failure/cancellation;
- refinement/lowering witness.

Without this summary, a compiler must EXPAND every Composition before reorder, fusion, parallelization, caching or distribution.

### 5.6 Possible Network must be intensional

The possible/realized distinction is useful, but materializing every possible route causes combinatorial explosion in branch, loop and dynamic topology.

Represent possible networks through guarded templates, parameterized routes, symbolic conditions, bounded rewrite rules and profile-specific schedulability constraints. Record realized execution as traces or realized subgraphs.

### 5.7 Effect, State, Time and Resource are not late metadata

Optimization requires knowledge of reads/writes, ordering and resource conflicts. Cyclic distributed systems need explicit progress/time tracking. Therefore semantic kernel work must reserve typed contract domains for:

- effect;
- state/history;
- time/clock;
- resource/ownership;
- failure/cancellation.

They need not all become Primitives, but they cannot remain implicit.

### 5.8 Dynamic topology should be a bounded capability

Dynamic topology is compositional in principle, but global arbitrary mutation prevents topology and target-set specialization.

Recommended capability classes:

- `STATIC REGION`;
- `BOUNDED-DYNAMIC REGION`;
- `OPEN-DYNAMIC CONTROL REGION`.

Most hot paths should be static or bounded-dynamic. Open-dynamic behavior belongs primarily in orchestration/control planes.

### 5.9 Orientation and Causality should not block executable work

Orientation may remain a derived analysis property. Causality remains a foundational research question. Neither should be a prerequisite for Grammar, scheduler or type/effect work.

## 6. Expected performance in real application

Performance depends less on the catalog name of a Composition than on where freedom remains at runtime:

- is topology fixed at compile time;
- are types, effects and resources known;
- are route cardinalities and rates bounded;
- is synchronization local or global;
- can state/time progress be tracked locally;
- is FOLD analyzable without EXPAND;
- can dynamic dispatch and allocation be removed from hot paths.

### Recommended performance envelopes

#### P0 — Static Kernel

- freedom: topology/type/effect/rate fixed;
- expected behavior: scheduler and graph traversal can be compiled away; a near-native target is structurally plausible;
- suitable for numeric kernels, DSP, GPU and repeated pipelines.

#### P1 — Fixed Graph / Dynamic Guard

- freedom: graph and target set fixed; conditions and route selection dynamic;
- expected behavior: lowering to branches, FSMs or table dispatch; low-to-moderate overhead is plausible;
- suitable for control, routing and business rules.

#### P2 — Bounded Dynamic Coordination

- freedom: queues, K-of-N, timeout and bounded spawn;
- expected behavior: scheduler/state/queue cost exists but can be practical at coarse grain;
- suitable for workflows, actors and streaming.

#### P3 — Bounded Dynamic Topology

- freedom: create/retire/rewire inside marked regions;
- expected behavior: analysis, allocation and invalidation cost rises; unsuitable for hot numeric loops;
- suitable for adaptive systems and orchestration.

#### P4 — Open Reflective Network

- freedom: arbitrary self-modification and global discovery;
- expected behavior: high overhead and low predictability; suitable for research and control planes rather than performance kernels.

Target high performance in P0/P1 and localize P2/P3. Do not promise near-native performance for arbitrary P4 networks.

### Dynamic specialization is possible but not free

A future JIT can specialize stable assumptions and deoptimize when they break, but this requires assumption tracking, specialization boundaries, invalidation/deoptimization, code-size budgets and profiling granularity. It is a later option, not a FIRST BYUL prerequisite.

### Distributed, cyclic and timed cost

The following combination is high risk:

```text
fine-grained timestamps
+ cyclic graph
+ distributed workers
+ dynamic topology
+ global completion query
```

Coordination and progress-tracking cost can dominate Transform cost. Mitigations are coarse granularity, local frontiers, batching, bounded regions and profile-specific runtimes.

### Objective performance conclusion

- structural possibility of high performance: **yes**;
- near-native performance for arbitrary dynamic graph: **not guaranteed and should not be expected**;
- near-native target for static/partially static regions: **reasonable**;
- practical dynamic orchestration: **possible depending on granularity and boundary design**;
- quantitative performance: **unknown until prototypes and benchmarks**.

## 7. Flexibility assessment

### High-confidence flexibility

- arbitrary network topology;
- branch/merge/many-to-many;
- condition-dependent routing;
- switching/distribution/multicast;
- hierarchy/FOLD/Composition-of-Compositions;
- heterogeneous target lowering;
- multiple Views;
- bounded dynamic topology;
- host-language/external-kernel integration.

### Incomplete without additional design

- Composition across different time semantics;
- sync/async/rendezvous mixing;
- stateful join/K-of-N/cancellation;
- safe movement of effectful Transforms;
- cross-profile determinism;
- resource contention/ownership;
- self-rewriting Composition;
- absence/undefined semantics.

### Key conclusion

> BYUL should gain flexibility not by pretending everything has one universal meaning, but by explicitly declaring different execution meanings and composing them through contracts.

## 8. Recommended architecture

```text
A0. WORLD / RESEARCH SEMANTICS
    Relation, Composition, View, Orientation annotation,
    possible/realized distinction, causality research

                 ↓ normalize

A1. OPEN COMPOSITION IR
    typed ports, boundaries, multi-port interaction,
    topology, hierarchy, FOLD interface

                 +

A2. SEMANTIC FACETS / CONTRACTS
    Guard, Contract, Policy, Pure Transform, Effect,
    State, Time, Resource, Failure, Topology Rewrite

                 +

A3. EXECUTION PROFILE / MoC
    Static Dataflow | Event/FSM | Async FIFO |
    Rendezvous/Connector | Timed/DE | Bounded Dynamic

                 ↓ analyze / specialize / partition

A4. OPTIMIZATION & LOWERING IRs
    static schedule, fusion, inlining, state machine,
    queue runtime, SIMD/GPU, distributed placement, DB/query

                 ↓

A5. MINIMAL TARGET RUNTIMES
    runtime cost is paid only by dynamic regions
```

### FOLD Interface Summary Contract

```text
FOLD(C) -> AbstractComposition {
  ports
  types
  interaction_profile
  rates/cardinality/bounds
  guards/contracts
  effects/state/time/resources
  determinism
  failure/cancellation
  topology_mutability
  refinement/lowering_witness
}
```

### Static Islands + Dynamic Boundaries

```text
[STATIC REGION A]
       ↓
[DYNAMIC ROUTER]
   ↙          ↘
[STATIC B]  [STATIC C]
       \      /
       [BOUNDED JOIN]
```

### Separate reference interpreter from production execution

- Reference Interpreter: semantic testing, traces, EXPAND/FOLD and CATALOG work. It may be slow.
- Production Lowering/Runtime: profile-specific specialized code. Do not leave a graph interpreter on hot paths.

## 9. Primitive-candidate revision

### Preserve

- `RELATION` — conceptual-minimum hypothesis;
- `COMPOSITION` — network/hierarchy.

### Defer freezing

- `VIEW / CONDITION / TRANSFORM` — useful vocabulary but not yet peer Primitives;
- `ORIENTATION` — derived analysis;
- `CAUSALITY` — open research.

### Focused pressure candidates

- `PORT / BOUNDARY`;
- `INTERACTION` — atomic multi-party coordination;
- `EFFECT`;
- `STATE / DELAY`;
- `TIME / CLOCK`;
- `RESOURCE / OWNERSHIP`;
- `TOPOLOGY REWRITE`.

Admit them only after comparison with natural Composition decompositions and lowering benefits.

## 10. Alternative architectures

### A — Universal Dynamic Graph Runtime

- apparent flexibility: very high;
- performance potential: low to uncertain;
- implementation difficulty: medium;
- verdict: useful only as a prototype/reference interpreter, risky as the final architecture.

### B — Multi-level architecture + Execution Profiles

- flexibility: very high;
- performance potential: conditionally high;
- implementation difficulty: high;
- verdict: **recommended final architecture**.

### C — Coordination DSL + external high-performance kernels

- flexibility: high;
- performance potential: high;
- implementation difficulty: medium;
- verdict: **safest first implementation**.

### D — Actor/KPN-first runtime

- flexibility: high for distributed and dynamic regions;
- performance potential: medium;
- implementation difficulty: medium;
- verdict: good for orchestration, limited for static kernels.

### E — Formal Open-System Algebra

- flexibility: high for modeling and proofs;
- direct execution performance: low;
- implementation difficulty: high;
- verdict: use as a formal backbone/reference, not as the whole runtime.

### F — Local Graph-Rewrite Runtime

- flexibility: high for dynamic topology;
- performance potential: workload-dependent;
- implementation difficulty: high;
- verdict: suitable as a later research profile.

### Recommended combination

Adopt **B** as the whole architecture, use **C** for the first implementation, and use **E** as a mathematical reference for FOLD/Composition contracts. Initial BYUL should express coordination, contracts, routing and hierarchy while connecting C/Rust/Python/CUDA/SQL kernels as Transform implementations. Expand native BYUL kernels later.

## 11. Risk register

- **V/C/T semantic inflation — high:** everything is forced into Condition/Transform. Mitigation: facet separation and admission tests.
- **Graph/meta-rule explosion — high:** simple JOIN/retry needs a huge graph. Mitigation: Interaction/State Primitive pressure review.
- **Opaque FOLD — very high:** every optimization requires EXPAND. Mitigation: mandatory typed summary contract.
- **Global runtime dynamism — very high:** every operation performs lookup/dispatch/allocation. Mitigation: marked dynamic capabilities.
- **Execution-semantics ambiguity — very high:** the same graph changes result with scheduler order. Mitigation: explicit profiles/MoCs.
- **Distributed progress overhead — high:** coordination/frontier work dominates Transform. Mitigation: coarse grain, local frontier and batching.
- **CATALOG overcollection — medium:** names grow without decomposition evidence. Mitigation: schema, normalization and probes in parallel.
- **Premature syntax lock-in — medium:** notation freezes ontology. Mitigation: stabilize IR/semantics first.
- **JIT complexity trap — high:** full JIT is attempted before AOT/profile lowering. Mitigation: AOT and static lowering first.

## 12. Architecture Viability Check v2

### Required pass conditions before Grammar freeze

1. Static straight-line and branch regions lower without runtime graph traversal.
2. FOLDed Composition supports type/effect/dependency analysis without EXPAND.
3. Local JOIN does not require a global scan or global barrier.
4. Dynamic topology does not invalidate optimization of static regions outside its boundary.
5. One semantic model lowers consistently to at least two Execution Profiles.
6. Common patterns avoid order-of-magnitude graph expansion.
7. Reference interpreter and optimized execution agree on declared observable semantics.

### Immediate redesign signals

- heap object and virtual dispatch are mandatory for every small Transform;
- all possible routes must be materialized;
- every pass must EXPAND because FOLD summaries are absent;
- synchronization/time/state can only be hidden inside one overloaded Condition;
- a profile adapter is effectively a separate whole program;
- a simple static pipeline cannot structurally approach a handwritten baseline.

## 13. Minimum validation vertical slices

### Slice A — Static/Timed Control

- sensor -> condition -> heat/cool -> feedback;
- state/delay/time;
- static lowering witness.

### Slice B — Async Routing and Coordination

- branch, multicast, K-of-N join, timeout, retry, cancellation and failover;
- fixed topology with dynamic conditions;
- compare reference interpreter and state-machine/queue runtime.

### Slice C — Bounded Dynamic Topology

- actor/process spawn and retire;
- route rebind;
- preserve FOLD boundary;
- preserve static optimization outside the dynamic region.

Optional Slice D adds a SIMD/GPU data pipeline to test high-performance lowering more strongly.

## 14. Final recommendation

### Continue the project?

**Yes.** There is no reason to abandon the direction. Finding the required revisions before implementation is advantageous.

### Implement the current design unchanged?

**No.** A universal graph runtime built directly from the current conceptual diagram is likely to lose both performance and flexibility through execution-semantics ambiguity, opaque FOLD and fine-grained dynamic overhead.

### Can the target be achieved?

**Conditionally yes**, with:

- world/execution semantics separation;
- explicit Execution Profiles;
- multi-port/Interaction support;
- typed FOLD contracts;
- static/dynamic partitioning;
- explicit effect/state/time/resource contracts;
- early probes and benchmarks;
- separate reference interpreter and optimized runtimes.

### Most realistic strategy

1. Continue broad CATALOG collection.
2. Define semantic stratification and Candidate Card v2 first.
3. Do not wait for saturation before three vertical probes.
4. Begin with a coordination DSL plus external kernels.
5. Build AOT lowering for static regions before a general dynamic runtime.
6. Add Primitives and profiles based on measurements.

## 15. Source route

### Git-governed BYUL sources

- Current Design Status v1.1;
- Roadmap v1.0;
- World Model research-artifact index.

### Primary/official prior art

- MLIR Language Reference;
- MLIR Side Effects & Speculation;
- Ptolemy II;
- Reo: A Channel-based Coordination Model for Component Composition;
- The Algebra of Connectors — Structuring Interaction in BIP;
- Static Scheduling of Synchronous Data Flow Programs;
- Dynamic Expressivity with Static Optimization for Streaming Languages;
- Practical Partial Evaluation for High-Performance Dynamic Language Runtimes;
- Verified Progress Tracking for Timely Dataflow;
- Dynamic Input/Output Automata;
- Structured Cospans;
- Formal Semantics for the Halide Language;
- Workflow Control-Flow Patterns;
- Dataflow Process Networks;
- TVM: An Automated End-to-End Optimizing Compiler;
- ForSyDe: Formal System Design.

This candidate does not create a Validation PASS, ontology freeze, production authority or AAA mutation.
