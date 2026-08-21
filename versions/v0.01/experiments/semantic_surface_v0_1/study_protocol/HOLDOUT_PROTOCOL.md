# Holdout Protocol v0.1

```text
PROTOCOL_ID = BYUL-HOLDOUT-v0.1
STATUS = PROTOCOL_DESIGN_ONLY / HOLDOUT_NOT_PRESENT
PLAINTEXT_HOLDOUT_ALLOWED_IN_GIT = FALSE
SALT_ALLOWED_IN_GIT = FALSE
MINIMUM_PRIMARY_CASES = 8
MINIMUM_RESERVE_CASES = 4
MINIMUM_CASES_PER_FAMILY = 2
NO_HOLDOUT_ROUTE = INSUFFICIENT_EVIDENCE
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
```

## 1. Purpose and boundary

The holdout tests generalization beyond public development probes after all
prospective candidate and adapter refs are frozen. It is comparative research
evidence only. It cannot select or canonize Byul, validate a World Model,
authorize implementation or merge, or support production use.

No plaintext input, oracle, salt, private manifest, private access log, or
decryption key may ever enter this Git repository, including temporary branches,
pull requests, issues, CI artifacts, or deleted history.

## 2. Required independent roles

Each role has a distinct actor/process identity and conflict disclosure. No
single person or model context may hold two of the following roles for the same
holdout.

| Role | May access | Must not access or do |
| --- | --- | --- |
| `SELECTOR` | Eligible incident population, source evidence, selection rules | Candidate/adapter code or results; runner output; grading |
| `CUSTODIAN` | Plaintext bundle, salt, keys, ACL, commitments, access log | Author cases/oracles; build candidates/adapters; grade semantics |
| `ORACLE_AUTHOR` | Selected inputs and exact source evidence | Candidate identities/code/results; runner observations |
| `ORACLE_REVIEWER` | Inputs, proposed oracle, evidence derivation | Candidate identities/code/results; case selection; running/grading |
| `RUNNER` | Candidate-visible inputs, frozen executable/adapter refs, resource envelope | Oracle, salt, grading notes, candidate repair |
| `GRADER_A` / `GRADER_B` | Sanitized observations and grader-only oracle after run freeze | Candidate identity, cost vector, builder discussion, re-link table |
| `TIE_ADJUDICATOR` | Frozen dual judgments and same sanitized packet/key | Candidate identity and cost before adjudication freeze |
| `RELINK_CONTROLLER` | Frozen grades and sealed opaque-to-candidate map | Change any judgment, oracle, exclusion, or candidate result |

The selector must not have authored v0/v0.1 public scenarios, candidate charters,
candidates, adapters, grading keys, or the favored architecture. The oracle
reviewer must be independent of the oracle author. At least one of selector,
oracle reviewer, and one semantic grader should be outside the same model
lineage as the protocol authors; otherwise the report must say
`CORRELATED_INTERNAL_EVIDENCE`.

## 3. External ACL store

Before selection, the custodian provisions a non-Git store with:

- encryption at rest and in transit;
- named least-privilege ACLs for every role;
- separate objects for candidate-visible inputs, grader-only oracles, salt,
  private manifest, re-link table, and access log;
- immutable versioning or write-once retention for the frozen bundle;
- per-object content digests and a chained access log;
- denied-access logging;
- key rotation and recovery procedures that do not reveal plaintext to builders;
  and
- an external timestamp/witness for the public commitment.

Store vendor, account, object URI, key identifier, salt, and private actor
identity remain private. The public record contains only the schema-valid
commitment, non-secret balance counts, sanitized audit digest, and witness
receipt.

## 4. Case population and balance

The selector freezes an eligible population and rejected-case log before
choosing primary cases. A case must derive from exact Git-pinned Byul evidence,
a disclosed structural transformation, or a composition of exact incidents.
The private manifest records repository, 40-hex commit, path, Git blob ID,
extraction range, transformation steps, introduced loss, and the oracle's
normativity classification.

The primary set contains at least eight cases, at least two in each family:

1. `AUTHORITY_CONFLICT`;
2. `PRESERVATION_LOSS`;
3. `LIFECYCLE_IDENTITY`; and
4. `RECONSTRUCTION_INVALIDATION`.

Across the primary set there must be at least:

- two `EXECUTION_REQUIRED` and two `REFUSAL_REQUIRED` cases;
- two `RESOLVABLE` and two `UNRESOLVED` cases;
- one raw-evidence representation and one structured representation in every
  family; and
- one expectation-reversing pair in every family.

An expectation-reversing pair differs in exactly one declared causal feature
that changes the allowed outcome tuple or required action. Irrelevant names,
ordering, serialization, and decoy fields must vary without changing the oracle.
Every pair has an opaque pair ID and opposite `A/B` polarity recorded only in
the private manifest.

## 5. Novelty and anti-template rules

At least four of the eight primary cases must be naturalistic or compositionally
different from all public scenarios. A case is not novel merely because symbols,
filenames, values, or prose were renamed.

Before freeze, the selector and oracle reviewer document structural features of
each public case and each holdout case. A primary case is ineligible when it has
the same operation, same decisive predicates, same fixture-field topology, and
same outcome cue pattern as a public case. Holdout candidate-visible inputs must
use opaque randomized IDs and must not expose:

- public case/scenario IDs or titles;
- `control_type` or pair polarity;
- allowed outcomes or expected posture;
- required/forbidden observation prose;
- family label, novelty class, or difficulty label; or
- answer-revealing operation/field names.

The oracle reviewer records `NOVEL`, `COMPOSITIONAL`, or `INELIGIBLE_CLONE` with
a reason before candidate construction. Any `INELIGIBLE_CLONE` is excluded from
the eligible population, not repaired after candidate results.

## 6. Oracle derivation and freeze

Candidate input and grader oracle are separate objects with separate digests.
The oracle uses allowed outcome tuples rather than independent per-axis lists.
For every required or forbidden condition it classifies the derivation as one
of:

- `SOURCE_SUPPORTED`;
- `OWNER_DIRECTION`;
- `EXPERIMENTAL_CONVENTION`;
- `WORKING_HYPOTHESIS`; or
- `UNRESOLVED`.

The oracle author signs the draft. The oracle reviewer independently checks
input sufficiency, source support, tuple consistency, expectation reversal,
evidence standards, and whether multiple legitimate answers remain. A case with
unresolved oracle disagreement before exposure is either repaired and re-frozen
before candidate construction or excluded from the eligible population. The
author and reviewer freeze separate approval digests; agreement is not inferred
from silence.

## 7. Salted public commitment

After the private manifest, all primary/reserve inputs, all oracles, the case
order, and the replacement map freeze, the custodian:

1. canonicalizes one private bundle index using RFC 8785 JSON Canonicalization
   Scheme (`JCS`), UTF-8, no byte-order mark;
2. generates at least 32 cryptographically random salt bytes;
3. computes
   `SHA-256("BYUL-HOLDOUT-v0.1\\0" || salt_bytes || canonical_bundle_bytes)`;
4. stores salt and plaintext only in the external ACL store;
5. publishes a schema-valid `holdout_public_commitment` containing the digest,
   balance counts, algorithms, timestamps, and external witness receipt, but no
   salt, plaintext, object locator, key, or answer; and
6. begins the chained access log before any candidate builder receives a build
   packet.

The commitment cannot prove good selection by itself; it proves only that the
later-revealed private bundle matches the pre-candidate commitment.

## 8. Access and run sequence

1. Candidate and adapter builders receive no holdout object or metadata beyond
   the public count/balance commitment.
2. All prospective candidate and adapter refs, dependency locks, environments,
   budgets, and completeness audits freeze simultaneously.
3. The custodian grants the isolated runner read access to candidate-visible
   inputs only. The runner cannot list or read oracle/salt/re-link objects.
4. Each frozen candidate receives byte-identical candidate-visible inputs under
   identical resource limits and exactly three sealed repetitions per case, as
   frozen in `../candidate_protocol/EXECUTION_BUDGET.yaml`. Input order is seeded
   and candidate-specific, but the seed mapping freezes before execution.
5. Native bytes, adapter mapping receipts, environment/resource logs, and run
   states freeze before the custodian grants graders access to oracles.
6. The custodian produces sanitized packets with opaque candidate/run labels.
7. Dual semantic grades and any tie adjudication freeze.
8. Only then does the re-link controller disclose candidate identity and join
   semantic judgments to cost/complexity vectors.

No candidate or adapter may be repaired after any real holdout input exposure.
A changed ref belongs to a successor experiment and requires a fresh holdout.

## 9. Access log

Every allow, deny, list, read, write, key-use, decrypt, export, grade-release,
re-link, and disclosure event is appended to an external chained log validating
against `schemas/access_log.schema.json`. Each event includes a monotonic
sequence, pseudonymous role instance, object class, action, decision, timestamp,
authorization ref, previous-event digest, and event digest.

JSON Schema cannot verify chain continuity. Before grading, an independent audit
must verify sequence uniqueness, digest linkage, timestamp order, role/ACL
conformance, and absence of builder access. Publish only a sanitized log digest
and audit disposition. A missing, discontinuous, or unexplained event chain
causes `HOLDOUT_ACCESS_AUDIT_FAILED`.

## 10. Reserve cases and common exclusion

At least four reserve cases freeze with the primary bundle: at least one per
family and with a declared replacement target/pair polarity. Reserve priority is
fixed before candidate construction.

If a primary case is invalidated for a candidate-neutral reason discovered
after freeze—corrupt input, oracle ambiguity, common runner failure, or common
contamination—the same case is removed for every candidate. It may be replaced
only by its highest-priority, pre-frozen, unexposed reserve that preserves the
family, representation, action/resolution stratum, and expectation-pair role.

Rules:

- no candidate-specific exclusion or replacement;
- no newly authored reserve after any candidate result;
- no replacement selected using candidate outcomes;
- original case, reason, access history, and replacement remain published in
  the audit record;
- if a reserve was exposed, contaminated, or cannot preserve the stratum, it is
  skipped only according to pre-frozen priority; and
- if the final common set falls below eight total, two per family, or any
  execution/refusal/resolvable/unresolved minimum, all holdout comparison claims
  become `INSUFFICIENT_EVIDENCE`.

An implementation-specific timeout, unsupported operation, or semantic failure
is a candidate result, not a common exclusion reason.

## 11. Contamination and no-holdout routes

Any pre-freeze builder access, oracle access by runner/candidate/adapter, answer
leak, case-specific patch, ref change, unlogged access, post-result oracle edit,
or candidate-specific exclusion contaminates the holdout. Preserve the event and
return `HOLDOUT_CONTAMINATED`; do not silently regenerate or reuse the set.

If the external store, minimum roles, public commitment, access log, oracle
review, minimum cases, reserves, or common-exclusion mechanics are unavailable,
public cases may be run only as a named rehearsal. The required result is:

`NO_HOLDOUT => INSUFFICIENT_EVIDENCE`.

Such a rehearsal cannot support outperform/equality claims, H3, candidate
narrowing, C3 activation, validation, selection, merge, or production.

## 12. External coordination required

- `EXTERNAL_COORDINATION_REQUIRED / ROLE_ASSIGNMENT`: selector, custodian,
  oracle author, independent oracle reviewer, runner, two graders, tie
  adjudicator, and re-link controller;
- `EXTERNAL_COORDINATION_REQUIRED / ACL_STORE`: encrypted, versioned, access-
  logged storage outside Git;
- `EXTERNAL_COORDINATION_REQUIRED / CASE_SELECTION`: an eligible incident
  population, private selection/rejection log, and at least 12 frozen cases
  including reserves;
- `EXTERNAL_COORDINATION_REQUIRED / COMMITMENT_WITNESS`: externally timestamped
  public commitment before candidate work; and
- `EXTERNAL_COORDINATION_REQUIRED / ACCESS_AUDIT`: independent chain and ACL
  verification before semantic grading.

This local environment can validate the schemas and protocol text. It cannot
create a genuinely hidden holdout, provision independent actors, or prove that
an external ACL boundary and commitment witness exist.
