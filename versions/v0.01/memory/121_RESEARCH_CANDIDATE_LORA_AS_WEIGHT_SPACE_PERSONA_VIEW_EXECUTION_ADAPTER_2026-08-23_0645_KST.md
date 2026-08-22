# 121. Research candidate — LoRA as a weight-space execution adapter for Persona/View

```text
STATUS = RESEARCH_CANDIDATE / NON-FROZEN / ASSISTANT_SYNTHESIS
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 06:45 KST
IMPLEMENTATION_AUTHORIZED = FALSE
OWNER_CONFIRMATION = NOT_YET
```

## Question

The Owner asked whether LoRA fits the current ASA/BYUL concept and what architectural place it could occupy.

## Candidate conclusion

LoRA appears conceptually compatible **if treated as an implementation mechanism rather than as Persona, View, memory, or data governance itself**.

A useful current placement is:

```text
Source / Legacy / Experience Relations
        ↓
Common / Domain / Persona Views
  - visibility
  - selection
  - composition
  - discard / resolution
  - purpose-conditioned interpretation
        ↓
Runtime context / representation
        ↓
Base Model + selected LoRA adapter(s)
        ↓
behavior / expression / judgment output
        ↓
new event / experience relations
```

In this reading, LoRA can implement or approximate part of the learned transformation between a View-conditioned input representation and model behavior/output.

## Strong candidate role

LoRA is best treated as a **learned weight-space adapter** or a **partially materialized/compiled implementation of a recurring Persona/View transformation pattern**.

It may be useful for relatively stable or frequently reused patterns such as:

- Seed Persona meta-stance;
- stable domain/task behavior;
- response/interaction tendencies;
- recurring transformation habits that are expensive or inefficient to reconstruct purely from prompt/context every time.

It should not automatically be equated with:

- Persona identity;
- Persona count;
- Source memory;
- explicit View definition;
- data visibility/access policy;
- provenance/lineage;
- deletion/reset semantics.

## Fit with current A/B framing

In the current non-frozen A/B convenience split:

```text
A = how selected Source is interpreted / represented
B = how interpretation becomes behavior / expression / action
```

LoRA plausibly sits most naturally on or near the `A -> B` model-execution transformation, while also potentially influencing internal interpretation. It should not be relied upon as the authoritative mechanism for Source visibility or governance.

## Important data-governance caution

ASA/BYUL currently treats user data control, deletion, provenance, and recomputation as core requirements.

Therefore training persistent LoRA weights directly on mutable/deletable user memories introduces a difficult dependency problem: deleting a Source relation does not automatically remove its learned influence from the adapter.

Research implication:

```text
DYNAMIC / DELETABLE PERSONAL DATA
-> prefer explicit Source/View/context layer

STABLE / CONSENTED / SLOW-CHANGING BEHAVIOR PATTERNS
-> LoRA may be an optimization/adaptation candidate
```

If per-user LoRA is later considered, adapter lineage, training-source provenance, retraining/unlearning cost, versioning, deletion semantics, and recomputation policy must be treated explicitly.

## Composition caution

Multiple LoRA adapters can be selected, weighted, merged, or swapped in existing PEFT implementations, but **weight-space composition must not be assumed equivalent to semantic relation/View composition**.

Interference, merge quality, ordering, and adapter compatibility require empirical evaluation.

Thus:

```text
VIEW COMPOSITION
!= automatically
LoRA WEIGHT ADDITION / MERGE
```

## Candidate architecture principle

A strong initial separation is:

```text
EXPLICIT SEMANTIC PLANE
Source + lineage + governance + View selection/composition

LEARNED EXECUTION PLANE
Base model + optional LoRA/adapter configuration
```

The first remains authoritative for data meaning/control; the second is an execution accelerator/adaptation mechanism selected by the first.

## Status

This note is a research candidate only. The Owner has not yet approved LoRA's architectural role.
