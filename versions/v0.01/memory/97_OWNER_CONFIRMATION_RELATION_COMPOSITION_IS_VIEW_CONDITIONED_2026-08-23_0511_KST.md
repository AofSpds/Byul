# 97. Owner confirmation — Relation composition is View-conditioned

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:11 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "합성함수 얘긴가요? VIEW가 그렇게 보는거겠죠?"

## High-fidelity interpretation

The Owner confirms that the immediately preceding question about whether `A -> B -> C` yields a meaningful `A -> C` relation is a **composition-function / composed-mapping** question, and that under the current hypothesis the composed relation is not assumed to be globally or automatically present independent of perspective.

Instead:

- basic relations remain directional transformations/mappings;
- multiple relations may be composed;
- whether a sequence is treated as one meaningful composed relation is View-conditioned;
- a View may select a path, choose a scope/resolution, collapse intermediate states, and interpret the composition as a higher-level relation;
- another View may preserve the intermediate relations or refuse the composition as semantically inappropriate;
- therefore composition is not merely graph reachability or automatic transitive closure.

Conceptually:

```text
A --r1--> B --r2--> C

View V1:
  compose(r1, r2) -> r* : A -> C

View V2:
  preserve A -> B -> C without collapsing to A -> C

View V3:
  composition not meaningful / not admitted
```

## Important nuance

The Owner's phrase `VIEW가 그렇게 보는거겠죠` supports View-conditioned composition, not necessarily a claim that composition exists only as a visual label.

A composed result may itself become a relation/relation-bundle and later serve as source/input to other Views, consistent with prior recursive routing hypotheses.

## Guards

Do not infer:

`A -> B and B -> C => A -> C automatically in every View`.

Do not infer:

`VIEW-CONDITIONED COMPOSITION -> composition is arbitrary`.

A View may need compatibility, scope, temporal, semantic, or other conditions; the exact admission conditions remain open.

Do not infer a canonical mathematical composition law, category-theoretic formalism, graph transitive closure rule, or implementation operator from this note.

## Research consequence

The research question shifts from `does composition exist?` to:

> Under what View-conditioned rules, compatibility constraints, temporal scopes, and abstraction resolutions should directional relations be composable into higher-level relations/bundles?

This is a central bridge between the basic directional-relation worldview and practical higher-level abstractions such as objects, Personas, organizations, contracts, and world Views.
