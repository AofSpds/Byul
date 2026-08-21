# Semantic Surface v0.1 — Successor Experiment Protocol

```text
STATUS = WORKING / PRE_FREEZE / PRE_IMPLEMENTATION
PREDECESSOR = semantic_surface_v0 / PRESERVED_EVIDENCE
CURRENT_ENGINEERING_GATE = CLOSED
DUMMY_HARNESS_GATE = CLOSED / PRE_FREEZE / F5-D_NOT_RUN
CANDIDATE_TRIAL_GATE = CLOSED / F5-C_NOT_ELIGIBLE
HOLDOUT_STATUS = NOT_PRESENT
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
MAIN_MERGE_AUTHORITY = FALSE
PRODUCTION_AUTHORITY = FALSE
```

## Purpose

This directory is the result-blind successor-protocol response to the closed
Semantic Surface v0 S4 gate. It does not repair v0 in place, define Byul,
select an architecture, or authorize a candidate implementation. It specifies
what would have to be frozen and evidenced before a dummy transport harness,
public rehearsal, or claim-bearing candidate trial could begin.

The protocol deliberately separates three questions:

1. Can native candidate bytes be transported and mechanically mapped without
   an adapter inventing semantics?
2. Can C1 and C2 be built and measured under an operationally symmetric,
   auditable comparison boundary?
3. Can visibility, holdout custody, execution, and adjudication make a study
   result interpretable without leaking answers or identities?

No positive answer is inferred merely because the corresponding document or
schema exists.

## Read order

1. `DELTA_FROM_V0.md` — disposition of every binding S4 correction.
2. `protocol/README.md` — native capture, mapping, tuple, and run-state boundary.
3. `candidate_protocol/README.md` — C0/C1/C2/C3 roles, budgets, and isolation.
4. `study_protocol/README.md` — visibility, holdout, schedule, and adjudication.
5. `SUCCESSOR_FREEZE_MANIFEST.json` — added only after the protocol source is
   committed; it pins the exact source commit and Git blobs reviewed next.

## Gate separation

| Gate | Permitted scope if opened | Cannot establish | Current state |
| --- | --- | --- | --- |
| Protocol freeze | Commit exact protocol and blob manifest | Correctness or feasibility | Pending |
| Dummy harness | Implement and run only public synthetic transport vectors | Candidate semantics, H1/H3, superiority | Closed; F3-D exists, but exact freeze and F5-D review have not run |
| Public rehearsal | Exercise frozen candidates only on disclosed diagnostics | Generalization, narrowing, C3 trigger | Closed; separately named authorization and all engineering controls required |
| Holdout candidate trial | Execute frozen C1/C2 refs under sealed custody and blind grading | Canonical Byul or production fitness | Closed; external prerequisites absent |
| C3 successor | Propose a new experiment after numeric trigger | Automatic C3 implementation or selection | Not authorized |

An opened dummy-harness gate does not open a candidate or holdout gate. An
Owner instruction cannot convert a missing integrity control into evidence; a
separately authorized reduced-control rehearsal must preserve
`INSUFFICIENT_EVIDENCE`.

## Current blockers

The repository currently contains the pre-code F3-D malicious/dummy transport
pack for schema, adapter, capture, and run-state checks. That pack becomes
eligible for F5-D review only after an exact source/blob freeze; it does not
open the harness gate by itself.

The pack does not contain the expectation-reversing/metamorphic public
development suite or executable, evidence-complete deterministic
invalidation/rebuild fixture required by correction 10 and F3-C. F3-C therefore
remains incomplete, F5-C is ineligible, and no candidate gate is open. F3-C is
not a dependency of the transport-only F5-D/F6 route.

A future candidate-trial successor must complete F3-C, freeze the actual
fixtures and grader-only keys, and obtain F5-C in addition to the separate
F5-D/F6 transport evidence. The repository also cannot locally fabricate:

- an externally ACL-controlled plaintext holdout, salt, commitment witness,
  and chained access log;
- independent selector, custodian, oracle reviewer, dual graders, tie
  adjudicator, evidence verifier, and re-link controller;
- two model lineages and independent human readers for the visibility study;
- provider-verifiable model snapshot, token, and resource receipts;
- isolated candidate repositories/containers and a simultaneous result
  visibility barrier; or
- an independent validation claim.

Until those prerequisites are evidenced, the candidate-trial route remains
`CLOSED` and any public-only execution can conclude no more than
`INSUFFICIENT_EVIDENCE`.

## Authority boundary

This is research protocol material only. Schema validity, dummy conformance,
public-case success, reviewer agreement, or a future holdout result would not
by itself prove semantic preservation in general, select a World Model,
authorize merge/release/production, or create AAA validation authority.
