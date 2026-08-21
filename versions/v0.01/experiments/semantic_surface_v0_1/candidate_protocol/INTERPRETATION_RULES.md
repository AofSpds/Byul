# Candidate Trial Interpretation Rules

```text
RULES_VERSION = 0.1.0
PUBLIC_CASES = DIAGNOSTIC_ONLY
DEFAULT_RELATION = INCOMPARABLE
SCALAR_SCORE = FORBIDDEN
WINNER_CLAIM = FORBIDDEN
SELECTION_AUTHORITY = NONE
VALIDATION_CLAIM = NONE
```

## 1. Authority boundary

This trial may produce bounded evidence about conformance to a frozen semantic
surface under a declared adapter. It cannot establish that the surface is true
or canonical, that any internal ontology is required, that one candidate is
Byul, or that any candidate should be merged, promoted, released, or used in
production.

Do not assign any precedence label or use “winner,” “validated architecture,”
“selected,” or equivalent language. Historical labels do not control build
resources or interpretation.

## 2. Eligibility gates

A C1 or C2 result enters any comparative relation only when all of the following
are frozen as `PASS` before real stimulus:

- successor spec and exact digest manifest;
- symmetric build and execution budgets;
- result-blind completeness audit;
- operational charter audit;
- adapter purity audit;
- final isolation/controller receipt;
- candidate and adapter refs at the global simultaneous freeze barrier;
- runner/harness/environment/input refs;
- externally sealed holdout protocol, if a holdout claim is attempted; and
- two-stage mechanical and blind semantic adjudication protocol.

Failure of a mandatory control is a gate, not a score. An Owner may authorize a
separately named public rehearsal, but cannot waive an integrity blocker into a
comparison-eligible experiment.

## 3. Public evidence

Public cases are development and diagnostic probes because builders can know
their structure and expectations. They may show:

- whether a frozen candidate can be invoked;
- native coverage, unsupported, and unmappable areas;
- adapter and evidence-capture behavior;
- reproducible failure traces; and
- hypotheses for a future experiment.

Public evidence may not support `outperforms`, superiority, candidate narrowing,
C3 activation, architecture validation, or selection. A public-only run ends
`INSUFFICIENT_EVIDENCE` even when every public case conforms.

No correction-10 public semantic fixture suite currently exists in this tree.
The transport dummy pack is not a public semantic case set. Expectation-
reversing/metamorphic cases and an executable deterministic invalidation/rebuild
fixture must be created and frozen in a future candidate-trial successor F3
before F5-D, F5-C, or candidate work can open.

## 4. Holdout gate

A comparative holdout claim requires all of these conditions:

1. plaintext inputs, oracles, and salts never entered the public Git history;
2. an independent selector and custodian sealed the bundle before candidate
   construction;
3. an independent oracle reviewer froze agreements and disagreements before
   execution;
4. a salted commitment, non-secret balance manifest, and append-only access log
   were frozen externally;
5. there are at least eight primary cases and four ordered reserve cases, at
   least two primary cases in each of the four frozen families, and at least two
   execution-required, two refusal-required, two resolvable, and two unresolved
   primary cases;
6. at least half the cases are naturalistic or compositionally different from
   public templates rather than lexical/minimal rewrites;
7. candidate and adapter authors never received the bundle or oracle;
8. the isolated runner used only frozen refs and the exact equal execution
   budget;
9. outputs and randomized identities remained sealed through mechanical checks
   and at least two blind semantic grades; and
10. no code, adapter, oracle, or rubric repair occurred after exposure.

If any condition is missing or cannot be proven, the result is
`INSUFFICIENT_EVIDENCE` or `CONTAMINATED`; public success cannot fill the gap.

## 5. Run and candidate states

| State | Unit | Meaning | Scoreability |
| --- | --- | --- | --- |
| `UNSUPPORTED` | Case observation | A complete candidate explicitly lacks the native capability | Preserve as capability gap; do not call implementation incomplete or silently mark incorrect |
| `UNMAPPABLE` | Mapping/grade status | A well-formed native capture cannot be mechanically represented without semantic invention/loss | A required field makes the case non-scoreable/non-orderable; malformed native JSON is instead `INVALID / NATIVE_PARSE_FAILURE` |
| `NONCONFORMING` | Case observation | Complete native behavior contradicts a frozen oracle obligation with sufficient evidence | Report per case; no scalar penalty |
| `INCOMPLETE_UNDER_BUDGET` | Candidate build | Result-blind completeness was not reached within equal cap | Candidate-level non-scoreable; not a semantic failure |
| `BUDGET_EXHAUSTED` | Build or run | A numeric cap was reached | Freeze partial evidence; non-scoreable; no extra effort |
| `BLOCKED` | Build, audit, or run | A prerequisite or required pin was unavailable before execution | Non-scoreable |
| `STOPPED` | Run | A pre-registered stop condition fired | Non-scoreable; preserve cause and native bytes |
| `INVALID` | Run or case | Ref, digest, schema, capture, or mechanical contract failed | Non-scoreable |
| `CONTAMINATED` | Build, audit, or run | Prohibited access, cross-inspection, outcome-aware change, or leakage occurred or cannot be excluded | Exclude comparative claims; no silent rerun |
| `AMBIGUOUS` | Grade | Both blind graders agree that the semantic evidence or oracle application remains ambiguous | Preserve; case not orderable |
| `DISAGREEMENT` | Grade | Blind graders did not reach the frozen agreement rule | Preserve disagreement; case not orderable |

`UNSUPPORTED` is possible only after the candidate is
`COMPLETE_UNDER_BUDGET`: completeness requires explicit native handling of the
operation vocabulary, not successful implementation of every capability.
When serialized through the shared run-state schema,
`INCOMPLETE_UNDER_BUDGET` uses run state `INCOMPLETE` and preserves
`INCOMPLETE_UNDER_BUDGET` as its reason code; it is never rewritten as a
semantic observation.

## 6. C0 interpretation

C0 is an archival calibration specimen created before the questions and is
frozen with a known code/data-baseline mismatch. Report its public/holdout-like
stimulus coverage only as historical distance or known limitation evidence. C0
cannot enter semantic or cost Pareto relations, dominate or be dominated, count
toward candidate narrowing, or trigger C3.

## 7. Per-case semantic vector

For each frozen holdout case, report one of:

- `CONFORMING`: the native/mapped evidence satisfies one allowed outcome tuple
  and every invariant/required observation;
- `UNSUPPORTED`;
- `UNMAPPABLE`;
- `NONCONFORMING`;
- `INVALID`;
- `AMBIGUOUS`;
- `DISAGREEMENT`; or
- `UNSCORABLE` or another non-scoreable run state.

Different allowed tuples—such as a justified refusal and a justified execution—
are equally conforming when the oracle permits both. Conflict, unknown, refusal,
and non-recoverability are not intrinsically worse states. Their meaning is
case- and referent-specific.

The only frozen partial order is:

- `CONFORMING` is above `UNSUPPORTED` and `NONCONFORMING` for that exact case;
- `UNSUPPORTED` and `NONCONFORMING` are not ordered against each other;
- `UNMAPPABLE`, `AMBIGUOUS`, `DISAGREEMENT`, `INVALID`, `UNSCORABLE`, and other
  non-scoreable states are not orderable; and
- no order crosses cases or failure families.

No count or percentage may replace the full per-case vector.

## 8. Pareto interpretation

First apply every integrity and control gate. Then publish the complete per-case
semantic vector and the cost vectors defined in `COST_MEASUREMENT_MANUAL.md`.

Candidate A semantically dominates B only if all holdout cases are orderable,
A is no lower than B on every case under the frozen partial order, and A is
strictly higher on at least one case. Candidate A cost-dominates B only under
the manual's all-known, same-scope, no-greater-on-every-axis rule. Crossed
semantic cases, crossed cost axes, unknowns, inherited-affordance mismatches, or
unmappable/disputed cases yield `INCOMPARABLE`.

Even when one candidate semantically and cost-dominates another, the permitted
statement is limited to:

> Under the frozen v0.1 holdout, adapter, environment, and budgets, A exhibited
> a Pareto relation to B on the reported vectors.

That statement is evidence, not selection or validation. No aggregate score,
weight, tie-breaker, or qualitative winner is available.

## 9. C3 route

C3 is not part of this trial. Only the exact numeric rule in
`C3_SUCCESSOR_TRIGGER.yaml` can make a separately authorized successor proposal
eligible. The trigger itself is not evidence that richer structure is superior.
An exposed holdout is never reused after repair, and the successor requires a
fresh holdout plus rerun simpler comparators.

## 10. Default conclusion

Unless every gate and every ordering condition is satisfied, the comparative
conclusion is exactly `INCOMPARABLE`. Missing evidence is preserved as missing;
it is not converted into equivalence, simplicity, failure, or preference.
