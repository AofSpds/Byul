# BYUL Prior-Art Atlas — Relation, Composition, Resolution, Recovery

**Version:** v1.0  
**Date:** 2026-08-26  
**Persona:** BYUL  
**State:** RESEARCH REFERENCE / NON-NORMATIVE / NOT VALIDATED / NOT FROZEN  
**Purpose:** prevent reinvention and preserve a durable map of established theories relevant to BYUL.

## 0. How to use this atlas

This is not a list of theories that BYUL must adopt. It is a routing map for prior-art-first research.

When a BYUL question appears, first ask which legacy family already studies the same structural problem. Reuse established concepts, theorems, counterexamples, terminology and implementation lessons where they fit; do not import hidden assumptions that conflict with BYUL.

Priority codes:

- `P0 CORE`: must be consulted before freezing BYUL foundations in the related area.
- `P1 STRONG`: likely to shape CATALOG, FOLD/VIEW, execution or validation design.
- `P2 DOMAIN`: important for specific later capabilities or stress tests.

BYUL current working premise remains `RELATION : SOURCE -> TARGET` as a conceptual-minimum hypothesis, with network/bundle Composition, multi-resolution abstraction, strong lineage/recovery goals and OPEN causality/primitive taxonomy.

---

# 1. Foundation cluster — Relation and Composition

## 1.1 Causal Set Theory / Causets — `P0 CORE`

**Core idea:** reality/spacetime is represented by a locally finite partial order of events; causal order is structurally primary.

**BYUL relevance:**
- event + partial-order minimum pressure test;
- local order versus global geometry/emergence;
- links, chains, antichains, transitive closure;
- warning that an arrow/order may carry strong causal/physical assumptions.

**Do not import blindly:** BYUL `SOURCE -> TARGET` is not currently frozen as physical causality or spacetime atomism.

**Primary/reference sources:**
- Sumati Surya, *The causal set approach to quantum gravity*: https://arxiv.org/abs/1903.11544
- Rideout & Sorkin causal-set dynamics lineage: https://arxiv.org/pdf/gr-qc/0212064

## 1.2 Category Theory / Symmetric Monoidal Categories / String Diagrams — `P0 CORE`

**Core idea:** study structures through morphisms and composition; string diagrams make compositional structure graphical and algebraic.

**BYUL relevance:**
- Relation as morphism pressure test;
- sequential/parallel composition laws;
- identity, associativity, equivalence and rewriting;
- graphical reasoning that is not object-first in the conventional OO sense.

**Do not import blindly:** mathematical morphisms may assume typing/composability laws stronger than BYUL currently wants.

**Sources:**
- *An Introduction to String Diagrams for Computer Scientists*: https://www.cambridge.org/core/elements/an-introduction-to-string-diagrams-for-computer-scientists/3CDAF8F57D2299F0EACA3354E9757CFD
- Bonchi et al., string-diagram rewriting: https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/string-diagram-rewrite-theory-ii-rewriting-with-symmetric-monoidal-structure/26B31C77D5ABFE8370B2A4C4589547B4

## 1.3 Applied Category Theory — Open Systems / Structured & Decorated Cospans — `P0 CORE`

**Core idea:** treat systems with explicit boundaries/interfaces as composable open systems.

**BYUL relevance:**
- FOLDed Composition with Ports/Boundary;
- Composition-of-Compositions;
- substitutability without EXPAND;
- formal foundation for open system interfaces.

**Do not import blindly:** cospan variable-sharing semantics is one composition paradigm, not necessarily universal for BYUL.

**Sources:**
- Baez, Courser, Vasilakopoulou, *Structured versus Decorated Cospans*: https://arxiv.org/abs/2101.09363
- Courser, *Open Systems: A Double Categorical Perspective*: https://arxiv.org/abs/2008.02394

## 1.4 Operads / Wiring Diagrams — `P0 CORE`

**Core idea:** specify how many components with typed interfaces can be wired into a larger component; composition itself has reusable algebraic structure.

**BYUL relevance:**
- higher-order Composition grammar;
- Ports and multi-input/multi-output systems;
- top-down versus bottom-up system assembly;
- possible mathematical backbone for FOLD interfaces.

**Sources:**
- Vagner, Spivak, Lerman, *Algebras of Open Dynamical Systems on the Operad of Wiring Diagrams*: https://arxiv.org/abs/1408.1598
- Yau, *Operads of Wiring Diagrams*: https://arxiv.org/abs/1512.01602
- Foley et al., operads for complex-system design: https://arxiv.org/pdf/2101.11115

## 1.5 Relational Model of Data — `P1 STRONG`

**Core idea:** represent data via mathematical n-ary relations rather than navigational object structures.

**BYUL relevance:**
- the word `relation` already has a deep data-model legacy;
- normalization, query algebra and declarative representation;
- warning against conflating binary graph edges with general mathematical relations.

**Source:**
- E. F. Codd, *A Relational Model of Data for Large Shared Data Banks*: https://dl.acm.org/doi/10.1145/362384.362685

## 1.6 RDF / Semantic Web / Knowledge Graphs — `P1 STRONG`

**Core idea:** subject-predicate-object triples form mergeable graphs for heterogeneous knowledge/data interchange.

**BYUL relevance:**
- practical relation-first data interchange;
- named graphs and heterogeneous-source merging;
- schema evolution and human-readable predicates;
- baseline comparison for “is BYUL merely another property/knowledge graph?”

**Do not import blindly:** RDF triples are primarily descriptive assertions; BYUL also wants Composition, operation/transform semantics, resolution and recovery.

**Sources:**
- W3C RDF 1.2 Concepts: https://www.w3.org/TR/rdf12-concepts/
- W3C RDF overview: https://www.w3.org/RDF/

---

# 2. Concurrency, events and process cluster

## 2.1 Petri Nets — `P0 CORE`

**Core idea:** places, transitions and tokens model concurrency, choice, synchronization and resource/state flow.

**BYUL relevance:**
- split/join/synchronization pressure tests;
- explicit operational state;
- concurrency without forcing total order;
- compact modeling of behaviors that may explode as naive binary Relations.

**Source:**
- Petri-net reference overview: https://link.springer.com/rwe/10.1007/978-0-387-09766-4_134

## 2.2 Event Structures — `P0 CORE`

**Core idea:** model events with causal dependency, conflict and concurrency, focusing on histories/configurations rather than only global state.

**BYUL relevance:**
- realized versus possible Composition;
- causality/order without total sequencing;
- conflict versus concurrency;
- event-history semantics for local Composition.

**Research route:** Winskel/event-structure literature should be consulted whenever BYUL freezes event/conflict/concurrency semantics.

## 2.3 Mazurkiewicz Trace Theory / Partial-Order Concurrency — `P1 STRONG`

**Core idea:** independent actions may commute; different sequential schedules can represent the same concurrent behavior.

**BYUL relevance:**
- avoid treating incidental execution order as semantic order;
- canonicalize equivalent network executions;
- reduce state/schedule explosion in validation/simulation.

**Source:**
- Trace Theory reference: https://link.springer.com/rwe/10.1007/978-0-387-09766-4_491

## 2.4 Process Calculi — CCS / CSP / π-calculus — `P0 CORE`

**Core idea:** algebraic models of interacting processes; π-calculus adds mobility where communication can change connectivity.

**BYUL relevance:**
- communication and interaction as first-class semantics;
- behavioral equivalence;
- dynamic topology / names / rebinding;
- Composition of concurrent behaviors.

**Do not import blindly:** process calculi are execution/behavior formalisms, not general world ontologies.

**Source:**
- Robin Milner, *Communicating and Mobile Systems: the π-Calculus*: https://www.cambridge.org/us/universitypress/subjects/computer-science/communications-information-theory-and-security/communicating-and-mobile-systems-pi-calculus

## 2.5 Coalgebra / Bisimulation / Coinduction — `P1 STRONG`

**Core idea:** a broad mathematical framework for state-based and potentially infinite behaviors; bisimulation captures behavioral equivalence.

**BYUL relevance:**
- compare Compositions by behavior rather than internal identity;
- loops, streams and ongoing systems;
- FOLD substitutability based on observable behavior;
- strong alternative to object-identity thinking.

**Sources:**
- Rutten, *A calculus of transition systems (towards universal coalgebra)*: https://ir.cwi.nl/pub/5060
- CWI coalgebraic methods overview: https://event.cwi.nl/cmcs10/proceedings/main.pdf

---

# 3. Coordination and network-execution cluster

## 3.1 Reo — Channel-based Coordination — `P0 CORE`

**Core idea:** build complex connectors compositionally from channels; coordination is separated from component internals.

**BYUL relevance:**
- Routing and interaction semantics;
- connector composition;
- dynamic reconfiguration;
- reason not to overload Relation itself with every communication discipline.

**Sources:**
- Arbab, *Reo: A Channel-based Coordination Model for Component Composition*: https://homepages.cwi.nl/~farhad/MSCS03Reo.pdf
- Reo reconfiguration: https://ir.cwi.nl/pub/10950/10950D.pdf

## 3.2 BIP / Algebra of Connectors — `P0 CORE`

**Core idea:** structured interactions among typed ports; rendezvous and broadcast are compositional connector semantics.

**BYUL relevance:**
- Port/Interaction Primitive pressure;
- multi-party synchronization;
- separate computation from coordination.

**Source:**
- Bliudze & Sifakis, *The Algebra of Connectors – Structuring Interaction in BIP*: https://www-verimag.imag.fr/~sifakis/connalg.pdf

## 3.3 Kahn Process Networks / Dataflow Process Networks — `P1 STRONG`

**Core idea:** deterministic processes communicate through channels; communication discipline shapes behavior.

**BYUL relevance:**
- same topology can have different execution semantics;
- async streaming and queue behavior;
- deterministic network semantics.

## 3.4 Synchronous Dataflow (SDF) — `P1 STRONG`

**Core idea:** fixed token production/consumption rates allow compile-time scheduling.

**BYUL relevance:**
- direct evidence for static-island performance;
- performance tradeoff from fixing degrees of freedom;
- execution profile reference for simulation/compiled paths.

**Source:**
- Lee & Messerschmitt, *Static Scheduling of Synchronous Data Flow Programs*: https://ieeexplore.ieee.org/document/5009446/

---

# 4. Dynamic structure and rewriting cluster

## 4.1 Algebraic Graph Transformation / DPO & SPO Rewriting — `P0 CORE`

**Core idea:** graph structure is changed by explicit rewrite rules with well-defined matching and gluing conditions.

**BYUL relevance:**
- topology rewrite rather than hidden mutation;
- dynamic Relation/Composition creation and deletion;
- conflict/critical-pair analysis;
- transformation grammar for self-modifying networks.

**Sources:**
- Ehrig tradition / AGG overview: https://link.springer.com/content/pdf/10.1007/978-3-540-25959-6_35.pdf
- typed attributed graph transformation references: https://link.springer.com/content/pdf/10.1007/978-3-540-30203-2_13.pdf

## 4.2 Statecharts — `P1 STRONG`

**Core idea:** hierarchical state machines add hierarchy, concurrency and communication to ordinary state diagrams.

**BYUL relevance:**
- hierarchy/FOLD applied to behavior;
- reactive human-friendly views;
- compare derived State versus explicit operational state.

**Source:**
- Harel, *Statecharts: a visual formalism for complex systems*: https://www.sciencedirect.com/science/article/pii/0167642387900359

## 4.3 Timed / Hybrid Automata — `P1 STRONG`

**Core idea:** discrete transitions are combined with clocks, timing constraints and/or continuous dynamics.

**BYUL relevance:**
- physical time versus logical events;
- continuous/discrete multi-model Composition;
- temporal contracts and cross-resolution simulation.

**Reference route:**
- Henzinger/Alur hybrid and timed automata tradition: https://link.springer.com/chapter/10.1007/978-3-642-00515-2_5

---

# 5. Abstraction, resolution and recovery cluster

## 5.1 Abstract Interpretation / Galois Connections — `P0 CORE`

**Core idea:** map concrete states into abstract domains for sound analysis; abstraction and concretization define what is preserved and what cannot be exactly recovered.

**BYUL relevance:**
- formal language for resolution-changing abstraction;
- EXACT versus approximate recovery;
- explicit precision loss;
- FOLD contract semantics.

**Source route:**
- classic Cousot tradition; accessible reactive-system formulation: https://dl.acm.org/doi/pdf/10.1145/244795.244800

## 5.2 CEGAR — Counterexample-Guided Abstraction Refinement — `P1 STRONG`

**Core idea:** begin with a coarse abstraction and selectively refine only where the abstraction is insufficient.

**BYUL relevance:**
- selective EXPAND;
- local resolution increase instead of whole-world expansion;
- AI/human investigation workflows.

**Reference:**
- hybrid-system CEGAR example: https://link.springer.com/chapter/10.1007/978-3-642-35873-9_6

## 5.3 Bidirectional Transformations / Lenses — `P0 CORE`

**Core idea:** maintain relationships between source data and simplified views with transformations in both directions.

**BYUL relevance:**
- multiple human/AI/domain Views over one substrate;
- source-view consistency;
- update propagation;
- strong prior art for reversible or partially reversible View semantics.

**Sources:**
- Foster et al., *Combinators for bidirectional tree transformations*: https://dl.acm.org/doi/10.1145/1232420.1232424
- incremental bidirectional transformations: https://dl.acm.org/doi/10.1145/2034773.2034825

## 5.4 Provenance / Lineage — `P0 CORE`

**Core idea:** record why/how a result was derived and which inputs/derivations contributed to it.

**BYUL relevance:**
- FOLD traceback;
- human “why?” drill-down;
- evidence routing;
- optimized/abstract model back-links to source Relations.

**Source:**
- Green, Karvounarakis, Tannen, *Provenance Semirings*: https://repository.upenn.edu/handle/20.500.14332/8764

## 5.5 Multilevel Graphs / Graph Coarsening & Uncoarsening — `P1 STRONG`

**Core idea:** collapse a large graph into coarser levels and then refine/uncoarsen as needed.

**BYUL relevance:**
- graph-native multi-resolution models;
- structural FOLD/EXPAND;
- performance-oriented coarse-to-fine algorithms.

**Caution:** coarsening usually optimizes graph algorithms and does not automatically preserve BYUL semantics/lineage.

## 5.6 Sheaf Theory / Cellular Sheaves — `P1 STRONG`

**Core idea:** attach local data to parts of a space/network and formalize when local pieces are mutually consistent and can be glued into global information.

**BYUL relevance:**
- local-to-global consistency;
- multiple local Views over shared structure;
- distributed information and conflict detection;
- possible mathematical tool for resolution/view compatibility.

**Sources:**
- Robinson, *Understanding networks and their behaviors using sheaf theory*: https://arxiv.org/pdf/1308.4621
- applied sheaf overview: https://arxiv.org/abs/2502.15476

---

# 6. Incrementality, history and recoverability cluster

## 6.1 Incremental View Maintenance (IVM) — `P0 CORE`

**Core idea:** update derived views using only changes rather than recomputing from scratch.

**BYUL relevance:**
- Relation-first network advantage should include affected-subgraph updates;
- multi-view maintenance;
- performance model for local change propagation.

**Sources:**
- *Maintaining views incrementally*: https://dl.acm.org/doi/10.1145/170036.170066
- modern DBSP formulation: https://dl.acm.org/doi/10.14778/3587136.3587137

## 6.2 Self-Adjusting Computation — `P1 STRONG`

**Core idea:** record dependencies so computation can efficiently update after input changes.

**BYUL relevance:**
- incremental Relation/Composition recomputation;
- locality and dependency tracking;
- performance evidence for preserving network structure.

**Reference route:**
- Acar self-adjusting computation lineage summarized in: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/097CE52C750E69BD16B78C318754C7A4/S0956796820000088a.pdf/build-systems-a-la-carte-theory-and-practice.pdf

## 6.3 Differential Dataflow / Timely Dataflow — `P1 STRONG`

**Core idea:** efficiently maintain iterative/incremental dataflow computations as data changes.

**BYUL relevance:**
- cyclic network + incremental change;
- large-scale distributed Relation updates;
- evidence that local/delta computation can outperform full recomputation.

**Source:**
- McSherry et al., Naiad/differential-dataflow lineage: https://www.microsoft.com/en-us/research/wp-content/uploads/2012/10/naiad.pdf

## 6.4 Event Sourcing — `P2 DOMAIN`

**Core idea:** store state changes as an event history from which past/current states can be reconstructed.

**BYUL relevance:**
- realized Composition history;
- temporal lineage and replay;
- distinction between current abstract state and derivational history.

**Reference:**
- Martin Fowler, Event Sourcing: https://martinfowler.com/eaaDev/EventSourcing.html

---

# 7. Logic, uncertainty and inference cluster

## 7.1 Datalog / Logic Programming — `P1 STRONG`

**Core idea:** declarative rules derive new relations recursively from existing relations.

**BYUL relevance:**
- inference as relation generation;
- recursive Composition;
- query/derivation semantics;
- optimization prior art for relation-centric computations.

**Source:**
- Maier, *Datalog: concepts, history, and outlook*: https://dl.acm.org/doi/abs/10.1145/3191315.3191317

## 7.2 Bayesian Networks / Probabilistic Graphical Models — `P1 STRONG`

**Core idea:** represent probabilistic dependencies in graph form and perform inference over them.

**BYUL relevance:**
- uncertainty should not be conflated with random execution or unknown data;
- probabilistic View/Composition candidates;
- comparison between Relation semantics and probabilistic dependency.

**Caution:** directed edges may encode conditional dependence and sometimes causal interpretation; BYUL Relation is currently broader.

## 7.3 Factor Graphs / Message Passing — `P1 STRONG`

**Core idea:** factorize a global function into local factors connected to variables; compute global/marginal results by local message passing.

**BYUL relevance:**
- local computation over a relational network;
- function/operation as graph structure;
- strong performance precedent for global results emerging from local relations.

**Reference:**
- IEEE topic route to Kschischang–Frey–Loeliger foundational paper: https://technav.ieee.org/topic/sum-product-algorithm/

---

# 8. Agent/social/economic composition cluster

## 8.1 Compositional Game Theory / Open Games — `P2 DOMAIN`

**Core idea:** build large games from smaller games that interact with an environment through open interfaces.

**BYUL relevance:**
- future agent/persona/economic models;
- bidirectional context, choices and feedback;
- system/environment boundary and human-facing modeling.

**Sources:**
- Ghani et al., *Compositional Game Theory*: https://arxiv.org/abs/1603.04641
- later compositional refinement: https://arxiv.org/abs/2101.12045

---

# 9. BYUL reference routing by research question

| BYUL question | Consult first |
|---|---|
| Is Relation a sensible minimum? | Causal Sets, Category Theory, Relational Model, RDF |
| How should Relations compose? | Monoidal Categories/String Diagrams, Operads, Cospans |
| How do branch/join/conflict/concurrency work? | Petri Nets, Event Structures, Trace Theory |
| How do interacting parts communicate? | Process Calculi, Reo, BIP, KPN |
| How should dynamic topology change? | π-calculus, Graph Transformation, Reo reconfiguration |
| How do we model loops/ongoing behavior? | Coalgebra, Petri Nets, Statecharts, Dataflow |
| How do FOLD/EXPAND and resolution work? | Abstract Interpretation, CEGAR, Multilevel Graphs |
| How do multiple Views stay connected? | Lenses/Bidirectional Transformations, Sheaves |
| How do we preserve “why/how derived”? | Provenance/Lineage, Event Sourcing |
| How do local changes avoid global recompute? | IVM, Self-Adjusting Computation, Differential Dataflow |
| How do explicit interfaces compose? | Structured/Decorated Cospans, Operads, Reo/BIP |
| How do time and continuous/discrete behavior mix? | Timed/Hybrid Automata, Statecharts |
| How do probabilistic relations/inference work? | Bayesian Networks, Factor Graphs |
| How do relation rules derive new facts? | Datalog / Logic Programming |
| How do agents/economic systems compose? | Open Games / Compositional Game Theory |

---

# 10. Highest-priority deep dives for BYUL

The following are the most likely to materially alter the BYUL foundation and therefore should be studied before related design freeze:

1. **Applied Category Theory: structured/decorated cospans + operads/wiring diagrams** — Composition, Ports, FOLD and open systems.
2. **Abstract Interpretation + CEGAR + Lenses** — resolution, abstraction, selective EXPAND and recovery guarantees.
3. **Provenance + Incremental View Maintenance + Self-Adjusting/Differential Dataflow** — lineage, local recomputation and network advantage.
4. **Petri Nets + Event Structures + Trace Theory** — synchronization, conflict, concurrency, realized histories.
5. **Process Calculi + Reo/BIP + Graph Rewriting** — communication, multi-party interaction and dynamic topology.
6. **Coalgebra/Bisimulation** — behavioral equivalence and FOLD substitutability for ongoing systems.
7. **RDF/Relational Model/Datalog** — practical data-model baseline and a test against reinventing existing relation-centric data systems.
8. **Sheaf Theory** — optional but potentially powerful local-to-global consistency framework for multi-view/multi-resolution data.

---

# 11. Prior-art discipline for future BYUL work

Before proposing a new Primitive, Composition operator, FOLD contract or execution semantics:

1. identify the structural problem precisely;
2. route to the relevant legacy families above;
3. record at least one established representation and one known limitation/counterexample;
4. attempt a BYUL decomposition using existing primitives/compositions;
5. state what BYUL requires that prior art does not provide;
6. only then consider a new BYUL construct;
7. preserve source references and whether the result is `BORROWED / ADAPTED / REJECTED / OPEN`.

The objective is not novelty. The objective is a coherent Relation-first world/data model that reuses the strongest existing mathematics and computer-science legacy while preserving BYUL's distinctive goals: flexible forms, multi-resolution Composition, human/AI Views, strong recovery/lineage, and optional efficient execution.

**Validation claim:** NONE  
**Ontology freeze:** FALSE  
**Production authority:** FALSE
