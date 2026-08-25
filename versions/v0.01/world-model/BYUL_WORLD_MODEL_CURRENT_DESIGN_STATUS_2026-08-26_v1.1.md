# BYUL World Model — Current Design Status

**Snapshot:** 2026-08-26  
**Revision:** v1.1  
**Persona:** BYUL  
**State:** RESEARCH_WORKING / NON_NORMATIVE / NOT_VALIDATED / NOT_FROZEN  
**v0.3 target:** RELATION COMPOSITION CATALOG

## 1. Current synthesis

- **Conceptual minimum hypothesis:** `RELATION : SOURCE -> TARGET`.
- This is a conceptual minimum, not a physical/storage/implementation minimum.
- `SOURCE/TARGET` are ordered endpoint roles; `DIRECTION != CAUSATION`, `TARGET != GOAL`.
- Composition is **network/bundle first**, not chain-only: branch, merge, parallel paths, loops, many-to-many and higher-order composition are admissible.
- Current minimal composition-role candidates remain `VIEW / CONDITION / TRANSFORM`; finality is OPEN.
- `FOLD / EXPAND` remain abstraction mechanisms separate from the V/C/T role taxonomy.
- Large folded Compositions must be able to preserve externally useful multi-port, routing, switching and distribution semantics.
- `POSSIBLE COMPOSITION NETWORK` and `REALIZED COMPOSITION` remain distinct.
- Orientation is increasingly treated as a higher-order reading/structural property of a Composition under a declared View/Condition, not as an automatic fourth primitive role.
- Causality remains a foundational OPEN research question.

## 2. Composition-first, Primitive-open principle

Use Composition when existing Relation/roles/grammar can express the required meaning naturally and usefully. Primitive admission remains allowed when one or more of the following are evidenced:

1. composition cannot express the meaning accurately;
2. composition causes semantic distortion or excessive hidden rules;
3. the decomposition is unnaturally non-minimal;
4. implementation/runtime cost is materially inferior without a compensating benefit;
5. a stable, reusable primitive provides clear semantic and lowering/optimization benefit.

Primitive minimization is not the objective; the objective is a small **sufficient** core.

## 3. Current composition layers

```text
L0 RELATION
   SOURCE --R--> TARGET

      compose
        ↓
L1 RELATION COMPOSITION
   network / bundle / sequence / branch / merge / parallel / loop / many-to-many

      condition / routing
        ↓
L2 COMPOSITION BEHAVIOR
   select / switch / split / distribute / activation / synchronization / recurrence

      FOLD / abstraction
        ↓
L3 ABSTRACT / HIGHER-ORDER COMPOSITION
   ports / interfaces / composition-of-compositions

      VIEW / interpretation
        ↓
L4 DERIVED / HIGHER-LEVEL CONCEPTS
   State / Control / Memory / Orientation / Object / Persona / ...
```

## 4. Routing clarification

Multiple targets, switching, distribution, fan-out and conditional routing are ordinary Composition behavior, not intrinsic conflict. True conflict requires incompatible requirements under the same relevant View/Condition/resource constraints.

Routing should be decomposed rather than represented as a single monolithic concept:

- available routes / topology;
- admissible or active routes under Condition;
- cardinality (`1`, `K-of-N`, `ALL`, etc.);
- selection policy;
- distribution semantics;
- synchronization/join semantics;
- failure/cancellation/timeout semantics.

## 5. Candidate catalog families

1. Topology
2. Choice / Activation
3. Synchronization
4. Multiplicity
5. Routing / Distribution
6. Interaction / Transport
7. Recurrence
8. Temporal
9. Failure / Cancellation
10. Resource
11. Dynamic Topology
12. Hierarchy / Abstraction
13. Absence pressure set (`ABSENT / EMPTY / UNDEFINED / UNREALIZED / NO-OUTPUT`)

## 6. CATALOG structure

```text
Observed Pattern Pool
        ↓ normalize
Normalized Composition Catalog
        ↓ decomposition / admission
Core Grammar + Primitive Candidates
```

Observed real-world/domain patterns are retained even when they later decompose into a smaller BYUL core.

## 7. CATALOG collection policy

CATALOG is managed by **Coverage + Saturation**, not a fixed number such as 100. Seed 30–50 and broad 70–120 are only exploratory reference ranges. Continue collection while new cases introduce genuinely new structure, semantics or primitive pressure.

## 8. Performance & flexibility track

World-model semantics must not be equated with runtime representation. Rich BYUL meaning may be analyzed, specialized and lowered before execution.

Every catalog candidate should record:

- expressibility;
- naturalness / semantic fidelity;
- static fraction / dynamic fraction;
- locality;
- state/synchronization/routing cost;
- parallelism;
- FOLD optimization transparency;
- freeze/specialization options;
- lowering options;
- performance cliffs;
- primitive pressure.

The same BYUL semantics may support different execution constraints:

```text
FLEXIBLE
  dynamic topology / target / routing / condition
      ↓ constraints
BALANCED
  fixed topology/target set; dynamic condition/routing
      ↓ specialization
STATIC / HIGH PERFORMANCE
  fixed/bounded topology, type, routes, effects, resources where useful
```

## 9. Architecture Viability Check — before Grammar

The design should be reconsidered before Grammar if representative cases require any of the following as unavoidable defaults:

- whole-network scans for local work;
- runtime dynamic dispatch for almost every operation;
- global synchronization for local joins;
- opaque FOLD that destroys dependency/effect information;
- uncontainable dynamic topology/routing across the whole program;
- no plausible lowering to efficient branch/state-machine/dataflow/SIMD/GPU/process/database constructs;
- huge graphs/meta-rules to express simple recurring semantics.

## 10. Integrated roadmap

`R0 Preserve -> R1 Observed Pattern Pool -> R2 Normalized Catalog -> R3 Decomposition -> R4 Flexibility Stress -> R5 Performance & Viability -> R6 Primitive Admission -> R7 Grammar -> R8 Syntax/Tooling -> R9 FIRST BYUL -> R10 Scale/Heterogeneity -> R11 v0.3 Consolidation`

Detailed exit criteria are maintained in the companion Roadmap document.

## 11. First BYUL milestone

FIRST BYUL means a small world can be expressed end-to-end using BYUL Relation/Composition/V-C-T/Routing/FOLD semantics, viewed at micro and higher-order levels, and at least one representative execution path has an efficient lowering witness.

## 12. Open / not frozen

- V/C/T finality
- Orientation taxonomy
- Causality
- exact routing grammar/operator/derived boundaries
- time / synchronization / interaction semantics
- absence semantics
- primitive set
- final Grammar / Syntax

No validation, ontology freeze, production authority or application to AAA is created by this document.

## 13. Source route

Interpret in this order:

`Git governed current state > current Git contracts/runtime > BYUL MEMORY/WORKLOG > merged Relation/Orientation checkpoint > current Owner Q&A.`

Companion: `BYUL_WORLD_MODEL_ROADMAP_2026-08-26_v1.0.md`.
