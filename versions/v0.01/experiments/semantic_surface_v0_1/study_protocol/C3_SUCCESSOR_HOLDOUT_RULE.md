# C3 Successor Holdout Rule

```text
RULE_ID = BYUL-C3-SUCCESSOR-v0.1
CURRENT_TRIAL_C3_IMPLEMENTATION = PROHIBITED
CURRENT_TRIAL_C3_EVALUATION = PROHIBITED
TRIGGER_EFFECT = SUCCESSOR_RESEARCH_ELIGIBILITY_ONLY
FRESH_HOLDOUT_REQUIRED = TRUE
SEPARATE_OWNER_AUTHORIZATION_REQUIRED = TRUE
SELECTION_AUTHORITY = NONE
```

## 1. Boundary

C3 cannot be appended to the v0.1 C1/C2 trial after observing public or holdout
results. The current holdout is consumed by exposure and cannot be reused to
show that a richer structure repairs the failures that inspired it.

Crossing this rule does not mean C3 is needed, correct, simpler, superior, or
selected. It permits only a proposal for a separately authorized successor
experiment.

## 2. Eligible trigger

Exactly one of the following predeclared routes must pass.

### Route A — replicated multi-family semantic insufficiency

All conditions are required:

1. C2 was charter-complete and mechanically valid under the frozen symmetric
   budget.
2. At least two distinct primary holdout cases in each of at least two of the
   four predeclared families receive final blind `NONCONFORMING` judgments.
3. Each failure reproduces in all three pre-frozen deterministic execution
   repetitions without candidate, adapter, input, resource, or environment ref
   change.
4. The two cases within a family are not an expectation pair's duplicate
   serialization and do not share the same single corrupt source fixture.
5. The two original blind graders independently agree on `NONCONFORMING` before
   candidate identities are re-linked. Any original grader disagreement is
   preserved and is ineligible to trigger C3 even if a tie adjudicator later
   supplies an interpretation.
6. The same failure obligation cannot be satisfied by C1 within its frozen
   capability boundary, or the result remains a general surface/fixture problem
   rather than evidence for C3 richness.

Minimum qualifying failures under Route A: four distinct cases, two per family,
with three repeated executions each.

### Route B — replicated catastrophic evidence-loss fault

All conditions are required:

1. The catastrophic class and fault injection were frozen before candidate
   implementation. Eligible classes are irreversible source/evidence loss,
   silent conflict deletion, false exact-reconstruction certification, or
   unrecoverable lineage corruption.
2. One holdout case produces the same catastrophic event in three of three
   isolated fault-injection repetitions.
3. Native bytes and independent storage evidence demonstrate the event; an
   adapter label or missing observation is insufficient.
4. The event is not caused by resource exhaustion, incomplete implementation,
   external service failure, invalid fixture, oracle ambiguity, or runner fault.
5. The two original blind graders agree on the catastrophic failure, and
   mechanical fault triage freezes, before identity re-link. Disagreement is a
   no-trigger result.

## 3. Mandatory blind triage

Every proposed trigger failure is tested, without candidate identity, against:

- adapter semantic mutation or mapping loss;
- harness/runner defect;
- resource or budget exhaustion;
- undeclared dependency/service failure;
- candidate incompleteness under budget;
- corrupted or insufficient input;
- oracle ambiguity or unsupported normativity;
- access contamination or ref drift; and
- a defect repairable without adding the hypothesized richer structure.

Any unresolved triage cause yields `C3_TRIGGER_INSUFFICIENT_EVIDENCE`. An
ordinary defect may be reproduced on public/dummy fixtures and repaired in a
new C2 ref, but the repaired ref may not be tested on the exposed holdout.

## 4. Successor authorization packet

If Route A or B passes, close the current experiment and prepare a successor
packet containing:

1. exact current spec, candidate, adapter, environment, observation, grade, and
   access-log refs;
2. the qualifying failure IDs and frozen triage evidence;
3. a feature-to-failure charter naming only the minimum richer capability under
   test;
4. a numeric complexity/resource cap for C3;
5. an ablation that removes the proposed richer feature while preserving other
   code and budget where technically possible;
6. exact rebuild rules for C1 and C2 comparators under symmetric clean contexts;
7. a new protocol/version and disclosed delta;
8. separate Owner authorization; and
9. a fresh externally selected, oracle-reviewed, committed holdout satisfying
   all v0.1 minimums and sharing no plaintext case with the consumed holdout.

The fresh holdout must be selected before C3 implementation. C3 builders may see
only public reproductions and the feature-to-failure charter, never consumed or
fresh holdout inputs/oracles.

## 5. Non-triggering conditions

None of the following opens C3:

- public-case failure or prose disagreement alone;
- one holdout failure in one family;
- aggregate score difference;
- implementation timeout, incompleteness, or budget exhaustion;
- test pass after tuning on an exposed case;
- same-model architectural convergence;
- C2 complexity being aesthetically undesirable;
- Owner interest without a separately scoped authorization; or
- inability to create a fresh holdout.

If no eligible trigger exists, record `C3_GATE_CLOSED`. If an eligible trigger
exists but external custody, fresh cases, symmetric comparators, or authorization
is missing, record `C3_SUCCESSOR_BLOCKED / INSUFFICIENT_EVIDENCE`.

## 6. External coordination required

- `EXTERNAL_COORDINATION_REQUIRED / FRESH_SELECTOR_AND_CUSTODIAN`;
- `EXTERNAL_COORDINATION_REQUIRED / FRESH_HOLDOUT_AND_COMMITMENT`;
- `EXTERNAL_COORDINATION_REQUIRED / BLIND_FAILURE_TRIAGE`;
- `EXTERNAL_COORDINATION_REQUIRED / SEPARATE_OWNER_AUTHORIZATION`; and
- `EXTERNAL_COORDINATION_REQUIRED / COMPARATOR_REBUILD_ISOLATION`.

This repository protocol cannot itself open, authorize, or execute the C3
successor.
