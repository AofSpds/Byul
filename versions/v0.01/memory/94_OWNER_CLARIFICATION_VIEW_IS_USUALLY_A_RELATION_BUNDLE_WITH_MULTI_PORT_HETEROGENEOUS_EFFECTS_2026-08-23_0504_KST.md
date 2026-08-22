# 94. Owner clarification — VIEW is usually a relation-bundle with multi-port / heterogeneous effects

```text
STATUS = OWNER_MAJOR_CURRENT_HYPOTHESIS / INTERVIEW_MEMORY
PROJECT = BYUL
PARENT_PROJECT = AAA
PRODUCT = ASSET AGENT ASA
CHANNEL_WORKSTREAM = ASA-MI / BYUL MODEL-DISCOVERY INTERVIEW
FORMAL_PERSONA = AAA-ASA (ASA)
TIME_KST = 2026-08-23 05:04 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "VIEW는 관계의 최소단위가 아니라 대부분 관계다발로 봐야죠. 
> 보려고 VIEW라는 관계 다발을 만들었다면 볼수 있겠지요. 
>
> 여러가직 속성을 가진 관계 다발이 형성되고 한쪽으로는 작은 영향을 미치고, 한쪽으로는 큰 소스를 리턴하고 그럴수도 있겠지요."

## High-fidelity interpretation

The Owner clarifies that although VIEW remains inside the relation-first worldview, a practical VIEW should usually be understood as a **composed relation-bundle**, not as one minimal atomic relation.

Current intuition:

- a VIEW may be deliberately composed because some actor/persona wants to observe or interpret the world in a certain way;
- the resulting VIEW bundle can contain multiple relations and relation-properties/capabilities;
- a VIEW bundle may have multiple interaction surfaces rather than one simple binary source→target edge;
- different interaction surfaces may have very different effect magnitudes, directions, payload sizes, or returned source/target structures;
- one part of the bundle may only weakly affect another relation state, while another branch may produce or return a much larger relation/source bundle;
- therefore VIEW execution/routing should not be prematurely reduced to one scalar mapping, one symmetric edge, or one fixed input/output arity.

Conceptually:

```text
            small effect
Input A  -----------------> State X
   \
    \
     +--> VIEW relation-bundle V
    /
   /
Input B  -----------------> Large derived/returned relation bundle Y
            large output
```

The exact graph, arity, directionality, weighting, and execution semantics remain open.

## Important distinction

Do not infer:

`VIEW = ONE RELATION`.

Do not infer:

`VIEW BUNDLE = FIXED OBJECT`.

Do not infer:

`SOURCE/TARGET = ONE INPUT / ONE OUTPUT`.

Do not infer:

`EFFECT SIZE = ONE NUMERIC WEIGHT`.

The Owner is preserving a more expressive relation-bundle interpretation in which routing, branching, fan-in/fan-out, recursive composition, and heterogeneous effects are all conceptually possible.

## Research consequence

A strong next research axis is whether the relation substrate should support **variable-arity / multi-port composition** rather than assuming fixed binary relations.

Candidate questions:

- can one View relation-bundle consume multiple source relations/bundles simultaneously?
- can it return multiple target/source bundles?
- can different branches have different semantics, magnitudes, temporal scopes, or authority/effect classes?
- can a returned target immediately participate as a source in another routing branch?
- how should fan-in, fan-out, partial influence, and large derived outputs be represented without collapsing the worldview into object-first containers?

These are research candidates only. No canonical hypergraph, port-graph, dataflow, category, rule-engine, or execution formalism is selected by this note.
