# BYUL Owner Decision — Q0-1 Project Identity

**Date:** 2026-08-26  
**Persona:** BYUL  
**Status:** OWNER DIRECTION RECORDED / RESEARCH BASELINE INPUT / NOT ONTOLOGY FREEZE

## Owner direction

BYUL is **not** being designed primarily as a programming language.

The core intent is a **data/world model** for representing and working with the world through Relations, Compositions, multiple resolutions, multiple abstractions and multiple forms.

Programming-language support should remain open and plural. BYUL may support or interoperate with many programming languages rather than define one mandatory language.

The data model is not intended to be merely passive data. Because function/mapping/operation is treated as deeply connected to the origin/formation of values in the Owner's worldview, operational/transformational meaning may itself be abstracted inside the model. Exact formalization remains OPEN.

A BYUL-specific compiler was not an original design requirement. Compiler/IR/lowering technology may be adopted later if it materially improves analysis, execution, interoperability or performance, but it is an optional derived implementation/tooling layer rather than the identity of BYUL.

The primary design goals are:

1. **Flexibility** — many forms and abstractions should be possible without forcing one programming paradigm or one representation.
2. **Multi-resolution modeling** — the same underlying world/data may support multiple resolutions and abstraction models with strong traceability/recoverability where declared.
3. **Relation-first fidelity** — model the world's operation and interdependence naturally rather than force object-first or language-first structures.
4. **AI-era human View** — BYUL should serve as a human-facing View over complex AI-era world models: understandable and familiar to people while preserving high-resolution machine-usable structure underneath.
5. **Faithful world-operation modeling** — the model should aim to represent how the world works, not merely how conventional software is organized.

## Q0-1 resolution

`BYUL IDENTITY = RELATION-FIRST DATA / WORLD MODEL PROJECT`

Programming language, compiler/IR and runtime are **optional interoperable implementation/tooling surfaces**, not the defining identity.

## Architecture implication

Recommended ordering becomes:

```text
WORLD / DATA SEMANTICS
    Relation / Composition / View / Resolution / FOLD-EXPAND / lineage

        ↓ optional projections / adapters

DOMAIN / HUMAN / AI ABSTRACTION MODELS
    many forms and views over the same underlying model where possible

        ↓ optional executable mapping

PROGRAMMING-LANGUAGE / TOOL ADAPTERS
    C / Rust / Python / SQL / GPU / future languages / other systems

        ↓ optional optimization path

COMPILER / IR / RUNTIME
    only where useful for execution, analysis or performance
```

This decision does not freeze Relation, V/C/T, FOLD semantics, Primitive set, execution profiles, compiler architecture or runtime design.
