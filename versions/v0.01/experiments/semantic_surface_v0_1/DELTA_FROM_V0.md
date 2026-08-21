# Semantic Surface v0.1 — Binding-correction disposition

```text
SOURCE_GATE = semantic_surface_v0/reviews/S4_CONSOLIDATED_GATE_DECISION.md
DISPOSITION_BASIS = SUCCESSOR_PROTOCOL_SOURCE / PRE_FREEZE
IMPLEMENTATION_EVIDENCE = NONE
EXTERNAL_CONTROL_EVIDENCE = NONE
NEW_ADVERSARIAL_REVIEW = PENDING_EXACT_FREEZE_REF
```

`SPECIFIED` means the successor contains an operational contract. It does not
mean the control has been implemented, executed, or independently validated.
`EXTERNAL_BLOCKED` means this repository cannot honestly generate the required
independence or custody evidence by itself.

| S4 correction | Successor location | Protocol disposition | Execution disposition |
| --- | --- | --- | --- |
| 1. Split stimulus, oracle, and mapping contracts | `protocol/schemas/` | `SPECIFIED` | `NOT_IMPLEMENTED` |
| 2. Opaque IDs and enforced answer separation | `protocol/CROSS_FILE_INTEGRITY.md`; `study_protocol/VISIBILITY_PROTOCOL.md` | `SPECIFIED` | `NOT_IMPLEMENTED` |
| 3. Complete allowed tuples and explicit axis referents | `protocol/OUTCOME_SEMANTICS.md`; oracle schema | `SPECIFIED` | `NOT_EXECUTED` |
| 4. Exact refs for all inputs, code, environment, native bytes, mappings, and state | run/capture/receipt/observation schemas; candidate isolation receipt | `SPECIFIED` | `MISSING_ACTUAL_REFS` |
| 5. Non-scoreable terminal states | run-state and observation schemas; interpretation rules | `SPECIFIED` | `NOT_EXECUTED` |
| 6. Pre-code malicious/dummy harness fixtures | `protocol/dummy_oracles/` | `SPECIFIED_PRE_HARNESS / TRANSPORT_ONLY` | `HARNESS_NOT_IMPLEMENTED`; does not satisfy correction 10 |
| 7. Mechanical adapter with native lineage | `protocol/ADAPTER_PURITY.md`; mapping-receipt schema; adapter audit | `SPECIFIED` | `ADAPTERS_NOT_IMPLEMENTED` |
| 8. C0 archival-only and operational C1/C2 boundary | `candidate_protocol/C0_ARCHIVAL_CALIBRATION.yaml`; C1/C2 charters | `SPECIFIED` | `C1_C2_NOT_IMPLEMENTED` |
| 9. Symmetric numeric budgets and complete cost accounting | build/execution budgets; cost manual | `SPECIFIED` | `EXTERNAL_TELEMETRY_AND_ISOLATION_UNPROVISIONED` |
| 10. Expectation reversal, metamorphism, and deterministic invalidation/rebuild | `study_protocol/EXECUTION_SCHEDULE.md` F3-C; future candidate-trial successor fixture pack | `NOT_YET_SATISFIED` | No expectation-reversing/metamorphic public suite and no executable evidence-complete deterministic invalidation/rebuild fixture exist; F3-C and F5-C remain closed, while transport-only F5-D is independently pending |
| 11. Cold-read artifacts separated from rubric, answers, candidates, and results | `study_protocol/VISIBILITY_PROTOCOL.md`; accessible-path policy | `SPECIFIED` | `EXTERNAL_BLOCKED` for independent readers/lineages |
| 12. Externally sealed holdout or explicit downgrade | `study_protocol/HOLDOUT_PROTOCOL.md`; holdout schemas | `SPECIFIED` | `EXTERNAL_BLOCKED`; no-holdout route is `INSUFFICIENT_EVIDENCE` |
| 13. C3 only in a fresh successor experiment | C3 candidate trigger and successor holdout rule | `SPECIFIED` | `C3_NOT_AUTHORIZED` |
| 14. Mandatory unique isolation and simultaneous freeze | isolation-controller schema; execution schedule | `SPECIFIED` | `EXTERNAL_BLOCKED` until allocations/receipts exist |
| 15. Two-stage mechanical and blind semantic adjudication | `study_protocol/ADJUDICATION_PROTOCOL.md`; adjudication schema | `SPECIFIED` | `EXTERNAL_BLOCKED` for independent graders/controllers |
| 16. New exact-ref adversarial review | root freeze-manifest procedure | `ROUTED` | `PENDING` |

## Non-waivable conclusion

The successor protocol removes several ambiguities from the written design but
has not yet demonstrated that the controls work. The next legitimate local
action is to freeze the exact F3-D/spec refs and obtain the narrow F5-D
adversarial verdict. Correction 10 still requires a future F3-C before F5-C can
be reviewed. Candidate implementation does not begin from this pre-freeze tree.
