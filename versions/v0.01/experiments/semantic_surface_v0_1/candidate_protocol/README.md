# Semantic Surface v0.1 — Candidate Fairness Protocol

```text
PROTOCOL_STATUS = DRAFT_SUCCESSOR_SPEC_COMPONENT
SCOPE = CANDIDATE_FAIRNESS_ONLY
V0_MUTATION = FORBIDDEN
CANDIDATE_IMPLEMENTATION = NOT_AUTHORIZED_BY_THIS_DIRECTORY
HARNESS_IMPLEMENTATION = OUT_OF_SCOPE
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
MAIN_MERGE_AUTHORITY = NONE
PRODUCTION_AUTHORITY = NONE
```

This directory repairs only the candidate-role, budget, isolation, adapter,
cost, and interpretation defects identified at the Semantic Surface v0 S4 gate.
It does not implement C1, C2, C3, an adapter, or a harness, and it does not
retroactively repair or replace the preserved v0 evidence.

## Evidence basis

The protocol was designed result-blind with respect to C1/C2/C3 because none of
those candidates exists. It is based on the following preserved evidence at
repository ref `2b79313d5d74160899caa1391cc46221355c18f4`:

- `semantic_surface_v0/reviews/raw/CANDIDATE_FAIRNESS_ADVERSARY_01.md`
  (`blob 3008e171e6ce408ccd111186fde57847f15e9c4a`);
- `semantic_surface_v0/reviews/raw/SCHEDULE_GATE_ADVERSARY_01.md`
  (`blob f1329919579cd329e7c7e8ac83ee1f8b0debedd9`);
- `semantic_surface_v0/reviews/S4_CONSOLIDATED_GATE_DECISION.md`
  (`blob bf73209d4fdf42d74782bf2f62667f13f814ab5a`);
- all four v0 candidate charters; and
- the C0 implementation, contract, tests, and memory corpus pinned in
  `C0_ARCHIVAL_CALIBRATION.yaml`.

The adversarial reviews target `d3b328c09e009fb24ede309ffae4fed66d5c680f`.
The later evidence ref above is used only to pin the preserved review blobs; it
does not change their review target or disposition.

## Files and dependency order

1. `C0_ARCHIVAL_CALIBRATION.yaml` makes C0 comparison-ineligible and separately
   pins its implementation, contract, tests, detached execution ref, and all 19
   source-data blobs.
2. `C1_GIT_NATIVE_CONTROL.yaml` defines the Git-native control boundary by
   operational capability.
3. `C2_CANDIDATE_OWNED_CHANGE_LAYER.yaml` defines the prospective candidate-owned
   append-record/replay boundary and inherited-Git disclosure.
4. `C3_SUCCESSOR_TRIGGER.yaml` keeps C3 outside this trial and defines only a
   numeric successor-experiment trigger.
5. `BUILD_BUDGET.yaml` freezes equal prospective build caps for C1 and C2.
6. `EXECUTION_BUDGET.yaml` freezes equal runtime resources and repetitions.
7. `COMPLETENESS_CHECKLIST.yaml` separates result-blind build completeness from
   semantic behavior.
8. `COST_MEASUREMENT_MANUAL.md` defines build, fixture, operation, human,
   adapter, recovery, and inherited-service accounting.
9. `ISOLATION_CONTROLLER.schema.json` defines the mandatory final isolation and
   ref-freeze receipt.
10. `ADAPTER_AUDIT_CHECKLIST.yaml` limits adapters to auditable mechanical
    mapping.
11. `CHARTER_AUDIT.md` defines the pre-execution, result-blind boundary audit.
12. `INTERPRETATION_RULES.md` defines the only permitted comparison language.

All `.yaml` files in this directory deliberately use the JSON subset of YAML so
that both strict JSON parsers and YAML 1.2 parsers can read them without implicit
typing differences.

## Non-negotiable ordering

The candidate protocol is not an execution token. Before any candidate build:

1. correction 10 must be completed in F3 with actual expectation-reversing and
   metamorphic public development fixtures plus an executable, evidence-complete
   deterministic invalidation/rebuild fixture; the current transport dummy pack
   does not satisfy this condition;
2. the complete successor specification must be committed at an exact 40-hex
   ref;
3. F5-D must record `DUMMY_TRANSPORT_ACCEPT` on the exact freeze and the F6
   dummy-only harness audit must pass;
4. F4 holdout commitment, V1 pre-candidate treatment freeze, and F5-C
   `CANDIDATE_TRIAL_ACCEPT` must all exist;
5. the common build packet, model snapshot, container image, and isolation
   controller must be pinned;
6. C1 and C2 must be built under the same numeric budget in isolated contexts;
7. candidate and adapter refs must pass completeness, adapter, charter, and
   isolation audits before any real public or holdout stimulus is run; and
8. no candidate result may be disclosed until all runs and blind judgments are
   frozen.

## Unresolved external prerequisites

These are deliberately not fabricated by this protocol and remain blocking:

- exact successor-spec commit and blob manifest;
- exact provider/model/snapshot/reasoning/tool-policy identifiers shared by C1
  and C2;
- exact common build-packet digest and tokenizer/accounting receipt;
- exact container-image digest and isolated repository/container allocations;
- independently appointed holdout selector, custodian, oracle reviewer, and
  blind graders;
- external ACL-controlled holdout commitment, balance manifest, and access-log
  refs;
- exact candidate, adapter, runner, harness, and environment refs; and
- independent result-blind gate sign-off.

In addition, correction 10 is a local design blocker rather than an external
custody blocker: no expectation-reversing/metamorphic public semantic suite or
executable deterministic invalidation fixture exists yet. It must be created and
frozen in a future candidate-trial successor F3-C before F5-C can open candidate
work. F5-D may independently review only the frozen transport surface and cannot
authorize a candidate build.

If any prerequisite is absent, the corresponding run is `BLOCKED` or
`INSUFFICIENT_EVIDENCE`; an intention to fill it later is not a substitute.
