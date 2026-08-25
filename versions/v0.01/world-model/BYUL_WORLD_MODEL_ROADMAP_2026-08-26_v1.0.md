# BYUL World Model Roadmap

**Version:** v1.0  
**Date:** 2026-08-26  
**Persona:** BYUL  
**State:** RESEARCH PLANNING / NON_NORMATIVE / NOT_VALIDATED / NOT_FROZEN  
**Current design baseline:** `BYUL_WORLD_MODEL_CURRENT_DESIGN_STATUS_2026-08-26_v1.1.md`  
**v0.3 target:** RELATION COMPOSITION CATALOG

## 0. Purpose

This is not a calendar schedule. It is a research-maturity roadmap designed to collect enough Composition candidates, normalize them, test decomposition, identify semantic and implementation pressure, detect performance cliffs early, and only then converge on Grammar and a First BYUL.

Core rules:

- **CATALOG-FIRST:** collect broadly before compressing aggressively.
- **COMPOSITION-FIRST, PRIMITIVE-OPEN:** use Composition where natural; admit primitives when evidence shows expression, minimality, implementation or performance advantages.
- **COVERAGE + SATURATION:** no fixed candidate-count gate.
- **SEMANTICS != RUNTIME:** conceptual minimum is not implementation minimum.
- **EARLY VIABILITY:** performance/implementation architecture is attacked before Grammar freeze.

## 1. Phases

| Phase | Name | Goal | Main artifact | Exit signal |
|---|---|---|---|---|
| R0 | Current Baseline & Preservation | prevent loss of design/Owner decisions | Current Design Status | traceable current baseline |
| R1 | Observed Pattern Pool | broad collection across domains | Observed Pattern Pool | major domain coverage, continue while new families appear |
| R2 | Normalized Composition Catalog | normalize aliases and layer confusion | canonical families/signatures | topology/semantics/operator/derived distinctions become usable |
| R3 | Decomposition & Witness | express candidates using Relation + V/C/T + existing composition elements | decomposition witnesses | natural decomposition or primitive-pressure evidence for major cases |
| R4 | Flexibility Stress Test | attack extreme network, routing, time, sync, self-modification | stress matrix | expression failures and semantic inflation points identified |
| R5 | Performance & Implementation Viability | find performance cliffs and useful constraints | performance profiles / interaction matrix | Architecture Viability Check passes or redesign action exists |
| R6 | Primitive Admission | promote only evidenced primitives | primitive candidate register | admission/rejection linked to evidence |
| R7 | Composition Algebra / Grammar | define compact composition rules and semantics | Grammar v0.x | representative Catalog cases fit without exception explosion |
| R8 | BYUL Syntax / Tooling Skeleton | provide authorable notation and analyzable representation | syntax + parser/IR skeleton | small programs can be written and expanded/analyzed |
| R9 | FIRST BYUL | express one small world end-to-end | reference composition | micro→macro composition + lowering witness |
| R10 | Scale & Heterogeneity | test large/distributed/heterogeneous systems | benchmarks/findings | tradeoffs informed by measurement |
| R11 | v0.3 Consolidation | integrate research evidence | RELATION COMPOSITION CATALOG v0.3 | clear OPEN/DERIVED/PRIMITIVE/REJECTED states and source traceability |

## 2. R1 — Collection policy

Candidate counts are hints, not gates. Seed 30–50 and broad 70–120 may occur naturally. Stop/slow broad collection only when **saturation** is visible: recent new cases mostly reuse existing families, decomposition witnesses repeat, and new primitive pressure becomes rare.

Primary families:

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
13. Absence pressure set

## 3. Catalog layers

```text
Observed Pattern Pool
        ↓ normalize
Normalized Composition Catalog
        ↓ decomposition / admission
Core Grammar + Primitive Candidates
```

A pattern such as FAILOVER can remain in the observed catalog while decomposing into `BRANCH + CONDITION + SELECT/SWITCH` at the normalized/core level.

## 4. Candidate analysis card

Every important candidate should carry:

- identity / aliases / domain source;
- topology / cardinality / ports;
- interaction semantics;
- possible vs realized network behavior;
- decomposition witness;
- semantic fidelity / naturalness;
- FOLD/EXPAND contract;
- static fraction / dynamic fraction;
- locality;
- state/synchronization/routing/communication cost;
- parallelism;
- freeze/specialization options;
- lowering targets;
- performance cliffs;
- primitive pressure.

## 5. Performance & flexibility track

The language/model may remain flexible while programs or regions choose stronger constraints for performance.

```text
FLEXIBLE
  topology / target / routing / condition dynamic
        ↓ constraints
BALANCED
  topology + target set fixed; condition/routing dynamic
        ↓ specialization
STATIC / HIGH PERFORMANCE
  topology/types/routes/effects/resources fixed or bounded where useful
```

The important research question is not “is dynamic behavior allowed?” but “can dynamic behavior be localized and can static regions be strongly specialized?”

## 6. Interaction Matrix

Performance must be evaluated for combinations, not only individual compositions. Early high-risk combinations include:

- dynamic topology + global synchronization;
- quorum + timeout + cancellation;
- dynamic-N distribution + resource contention;
- recurrence + topology mutation;
- opaque FOLD + unknown effects;
- arbitrary routing + global optimization requirement.

## 7. Architecture Viability Check

Before Grammar, verify representative cases do **not** structurally require:

1. whole-network scans for local work;
2. dynamic lookup/dispatch on nearly every operation;
3. global barriers for local coordination;
4. loss of effect/dependency information at FOLD boundaries;
5. program-wide dynamic topology when only small regions need it;
6. inability to lower common patterns to efficient existing execution constructs;
7. huge graph/meta-rule expansion for simple recurring semantics.

A persistent failure is a redesign/primitive-admission signal, not something to hide in implementation.

## 8. Primitive Admission Gate

Review a new primitive when there is evidence of one or more:

- non-expressibility;
- semantic distortion/inflation;
- unnatural non-minimal decomposition;
- material runtime/implementation disadvantage;
- stable and reusable meaning;
- meaningful compiler/runtime optimization handle.

Primitive minimization is not a goal by itself.

## 9. First BYUL entry conditions

- major catalog families covered and near saturation;
- decomposition/counterexample evidence exists;
- structural viability red flags addressed;
- a usable primitive candidate set exists;
- minimal branch/merge/routing/synchronization/loop/FOLD semantics exists;
- one small reference world can be expressed micro→macro;
- at least one representative path has an efficient lowering witness.

## 10. Immediate research order

1. SPLIT / CHOICE / JOIN / SYNCHRONIZATION
2. ROUTING / DISTRIBUTION
3. CONCURRENCY / INTERACTION DISCIPLINE
4. DYNAMIC TOPOLOGY
5. LOOP / FEEDBACK / RECURRENCE
6. TIME
7. FAILURE / CANCELLATION / RESOURCE
8. FOLD / PORT / EFFECT CONTRACT
9. ABSENCE semantics

## 11. Freeze boundary

This roadmap does not freeze the World Model, V/C/T, Orientation, Causality, Routing taxonomy, primitive set, Grammar, Syntax or runtime model. It defines research order and evidence expectations only.
