# Study cross-file integrity rules

These rules are mandatory mechanical checks over exact bytes. JSON Schema can
constrain one record but cannot prove digest arithmetic, timestamp ordering,
cross-document equality, actor independence, or custody. A missing verifier or
receipt is a failed gate, not an invitation to infer the fact.

## 1. Role identity and separation

Construct the ordered role vector from the private manifest:

`selector, custodian, oracle_author, oracle_reviewer, runner,
mechanical_checker, sanitizer, sanitization_reviewer, graders[0], graders[1],
tie_adjudicator, relink_controller, access_auditor`.

All 13 `role_id` values and all 13 `actor_identity_commitment_sha256` values
must be pairwise distinct. Distinct pseudonyms or contexts controlled by the
same actor do not satisfy this rule. The access-log actor role/ID, adjudication
checker, packet creator/reviewer, graders, tie adjudicator, re-link controller,
and audit actor must equal the corresponding frozen manifest role instance.
Candidate and adapter builders must be absent from this vector and must have a
different actor-identity commitment from every holdout role. Any equality,
missing conflict disclosure, or unverifiable identity yields
`ROLE_SEPARATION_FAILED` and closes the candidate-trial gate.

## 2. Balance derivation

Counts are derived from `cases`; they are not trusted declarations.

1. `primary_count` is the number of cases with `disposition=PRIMARY`;
   `reserve_count` is the number with `disposition=RESERVE`.
2. `family_primary_counts[f]` counts only primary cases in family `f`.
3. Action, resolution, representation, and novelty counts use only primary
   cases. `novel_primary_count` counts `NOVEL_NATURALISTIC` plus
   `NOVEL_COMPOSITIONAL`.
4. A valid expectation pair is exactly two primary cases with one pair ID,
   identical family, one `A` and one `B`, and the pre-reviewed one-feature
   reversal receipt. `expectation_pair_counts[f]` counts valid pair IDs, not
   case rows. A pair ID may occur in only one family.
5. Reserve priority is unique within every replacement target. A reserve may
   replace only targets listed before candidate construction and must preserve
   family, representation, action stratum, resolution stratum, and pair role.

The non-secret balance projection is exactly the RFC 8785 JCS value
`{primary_case_count,reserve_case_count,family_counts,balance_counts,
novel_primary_count,expectation_pair_count}` with the public-schema field names.
Its SHA-256 must equal both manifests' declared
`balance_projection_canonical_sha256`; every projected number must equal the
private derivation above. Any mismatch is `HOLDOUT_BALANCE_BINDING_FAILED`.

## 3. Private oracle to core CASE_KEY bridge

Every private `cases[i].oracle.case_key` validates directly against the frozen
core `protocol/schemas/oracle.schema.json`, uses `oracle_kind=CASE_KEY`, has a
null dummy fixture, and uses exactly these derivation classes:
`SOURCE_SUPPORTED`, `OWNER_DIRECTION`, `EXPERIMENTAL_CONVENTION`,
`WORKING_HYPOTHESIS`, `UNRESOLVED`.

One private bridge record per case validates against
`schemas/holdout_oracle_bridge.schema.json`. Resolve the exact private manifest,
verify `cases[i].opaque_case_id`, extract `/cases/i/oracle/case_key`, validate it,
encode that value as RFC 8785 JCS UTF-8 with no BOM or trailing bytes, and seal
those exact bytes as the grader oracle. Source canonical digest, target byte
digest, target ref digest/length, oracle ID, and stimulus-to-candidate-input ref
must match. No field may be added, dropped, renamed, normalized, or interpreted.
Failure is `HOLDOUT_ORACLE_BRIDGE_FAILED`; an adapter may not repair it.

## 4. Bundle and public commitment binding

The custodian freezes a separate private bundle-index value before candidate
construction. It contains: the private manifest with the three derived binding
fields (`private_bundle_digest_sha256`, `public_commitment_digest_sha256`, and
`salt_b64`) omitted; every primary/reserve input exact-object record; every core
CASE_KEY exact-object record; every bridge record; case order; and replacement
map. Object arrays are sorted by private object ID. No result or candidate ref is
present.

Let `B = RFC8785_JCS_UTF8(bundle_index)` and `S` be the decoded `salt_b64` bytes.
Then all of the following are mandatory:

- private `private_bundle_digest_sha256 = SHA256(B)`;
- public `commitment_digest_sha256 =
  SHA256(UTF8("BYUL-HOLDOUT-v0.1") || 0x00 || S || B)`;
- private `public_commitment_digest_sha256` equals that public digest;
- experiment IDs, schema digest, balance projection digest/counts, witness
  receipt, and commitment context match; and
- public access-log genesis and pre-candidate head digests equal the private
  manifest access-log fields at commitment time.

The salt and bundle stay external. After authorized reveal, an independent
auditor recomputes every equality. A commitment without this binding is only an
opaque hash and yields `HOLDOUT_COMMITMENT_BINDING_FAILED`.

## 5. Access-log digest, chain, head, and audit

For each event, project exactly the 13 fields listed in
`digest_preimage_contract.event_projection_fields`, JCS-encode the projection,
and recompute:

`event_digest_sha256 = SHA256(UTF8("BYUL-ACCESS-EVENT-v0.1") || 0x00 ||
RFC8785_JCS_UTF8(projected_event))`.

Sequences must be exactly `0..n-1`; event zero has null previous digest; every
later previous digest equals the preceding recomputed digest; genesis equals
event zero; head equals event `n-1`; and timestamps are nondecreasing. The audit
event count equals `n`. The audited event-set digest is SHA-256 over the JCS
event array. The audit receipt preimage is the JCS object
`{log_id,experiment_id,event_count,audited_events_canonical_sha256,
audited_genesis_event_digest_sha256,audited_head_event_digest_sha256,
checked_rule_ids,findings,status}` prefixed by
`UTF8("BYUL-ACCESS-AUDIT-v0.1") || 0x00`; its SHA-256 equals the receipt field.
The manifest audit receipt and log receipt must match. Candidate execution
requires `chain_audit.status=PASS` and all ten exact rule IDs. Missing,
discontinuous, forbidden, or unaudited access yields
`HOLDOUT_ACCESS_AUDIT_FAILED`.

## 6. Run-state mapping

The adjudication run-state digest resolves to exactly one core terminal
run-state record for the same run/attempt. State mapping is identity except
core `INCOMPLETE` maps to adjudication `INCOMPLETE_UNDER_BUDGET`. Core and
adjudication reason-code sets are exactly equal. `OBSERVED` has no reason codes;
every other state has at least one reason and evidence ref. Only `OBSERVED` can
continue. `BLOCKED`, `STOPPED`, `CONTAMINATED`, `INVALID`, `INCOMPLETE`, and
`BUDGET_EXHAUSTED` map to their corresponding final state and never receive a
semantic packet or re-link.

## 7. Two-stage adjudication and final state

Resolve the exact core mechanical registry and study binding file named by the
adjudication record at its `spec_ref`. Their byte SHA-256 values must match the
record. The twelve ordered schema check IDs must exactly equal
`MECHANICAL_CHECK_BINDINGS.json.ordered_bindings[*].check_id`, and the union of
all `core_check_ids` must exactly cover every mandatory core registry check ID.
An unknown, missing, or uncovered ID is `MECHANICAL_CHECK_BINDING_FAILED`.

The mechanical array contains the 12 mandatory IDs exactly once and in schema
order. Checks 1–10 and 12 are `PASS` or `FAIL`; check 11 may be
`NOT_APPLICABLE` only for a named public rehearsal. A claim-bearing holdout run
requires all 12 `PASS`. Semantic eligibility is true if and only if run state is
`OBSERVED` and no mandatory check failed. Failure codes equal the set of failed
check IDs plus registered route codes.

For `AGREE`, both signed grader vectors must match on all five components and
final judgment; for `DISAGREE`, at least one differs, originals remain frozen,
and final judgment is `DISAGREEMENT`. The schema enforces the finite value
comparison; the mechanical checker recomputes the two canonical vector digests.

Re-link is permitted only after semantic, disagreement, exclusion, and opaque
final-table freeze. Its pre-relink digest equals the semantic grade-freeze
digest, `grade_freeze_frozen_at` equals the semantic freeze timestamp, and
`relinked_at` is strictly later. The ordering receipt must pass. Early re-link
is `ADJUDICATION_ORDER_INVALID`.

An exclusion is either the exact false tuple
`(NONE,false,null)` or the true tuple `(common reason,true,pre-frozen reserve)`.
True exclusion applies to every candidate and forces `COMMON_EXCLUDED`; false
exclusion forces the final state corresponding to the dual semantic result.
Non-observed states and observed mechanical failure follow the schema's exact
final-state mapping. Candidate-specific exclusion is `COMPARISON_INVALID`.

## 8. Gate boundary

Repository-local schema validation and dummy transport checks cannot prove any
cross-file equality above without exact artifacts, nor can they establish
independent actors, external custody, or timestamps. The candidate-trial gate
therefore remains closed until frozen external evidence and an independent
mechanical audit satisfy every applicable rule. Dummy-harness review is a
separate gate and creates no candidate-trial authority.
