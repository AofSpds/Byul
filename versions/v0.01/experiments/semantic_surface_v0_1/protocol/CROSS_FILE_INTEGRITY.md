# Cross-file integrity rules

JSON Schema validates one document at a time. The runner's mechanical gate must
also enforce every rule below against canonical bytes. Failure of any mandatory
rule yields terminal `INVALID` unless a more specific pre-existing terminal
state (`CONTAMINATED`, `STOPPED`, `BLOCKED`, or `BUDGET_EXHAUSTED`) must be
preserved.

## Canonical bytes and digests

1. File refs use SHA-256 over the exact stored bytes, not parsed or normalized
   content.
2. Embedded `content_base64` is strict RFC 4648 base64. Its decoded byte length
   and SHA-256 must equal the declared values.
3. `canonical_json_sha256` values use RFC 8785 JSON Canonicalization Scheme over
   the designated JSON value encoded as UTF-8.
4. A Git ref, when used, must resolve repository, commit, path, and Git blob;
   the retrieved file bytes must also match the declared SHA-256 and length.
5. Locator success without digest equality is failure.

## Identity and uniqueness

An ID is **declared** only where its entity is created. Examples are
`stimulus_id` in a stimulus, `oracle_id` in an oracle, `capture_id` in a native
capture, `receipt_id` in a mapping receipt, `observation_id` in an observation,
and a record ID inside the array/object that owns that record. A field such as
`stimulus_id` in an oracle, `native_capture_id` in a receipt, or
`observation_id` in a receipt is a **reference**, not a second declaration.

Within one experiment freeze:

1. each declaration ID names exactly one entity in its declared namespace;
2. a second declaration using the same ID is invalid;
3. repeated references to a declared ID are allowed only where a binding rule
   requires them and must resolve to that one declaration;
4. a repeated embedded evidence or immutable-ref object with the same
   `evidence_id` or `ref_id` must be canonical-byte identical; and
5. semantic record IDs and mapping IDs are unique across their owning sealed
   observation/receipt set, even if two records otherwise have equal content.

Opaque IDs must not encode scenario family, expected result, candidate
identity, or control type. `MECHANICAL_CHECK_REGISTRY.json` distinguishes every
declaration role from its permitted foreign-key/reference roles.

## Required bindings

1. The oracle's `stimulus_ref` must match the exact stimulus file.
2. The run manifest's spec, harness, runner, candidate, adapter, environment,
   dependency-lock, resource, stimulus, and oracle refs must all resolve and
   match exact bytes.
3. Candidate and adapter execution processes must not be able to resolve or read
   the manifest's oracle ref. The access-denial test and its evidence are frozen.
4. The run state, native capture, every mapping receipt, and observation must
   name the same `run_id` and `attempt_id`.
5. The native capture's stimulus, candidate, environment, dependency-lock,
   harness, and runner refs must equal the run manifest refs.
6. The observation's native payload digest set must exactly equal the native
   capture artifact digest set; order is irrelevant, membership is exact.
7. Every mapping receipt must cite the same native capture and adapter refs as
   the run manifest and must target the sealed observation ID.
8. Every observation mapping-receipt ref must resolve, and every receipt for the
   observation must be listed. Extra or missing receipts are invalid.
9. Derive the receipt inventory from the sealed observation by recursively
   visiting each JSON object member and array element. A terminal value is a
   scalar, `null`, empty array, or empty object. Escape object keys as RFC 6901
   JSON Pointer tokens; use decimal array indexes; exclude exactly the
   `/mapping_receipt_refs` subtree because including receipt digests would make
   the receipt/observation relation circular. Sort pointers by UTF-8 byte order.
10. The resulting pointer set must equal all three of: the keys of the receipt's
    `mappings` object, `coverage.target_field_inventory`, and the independently
    recomputed inventory. No duplicate target is representable in the keyed
    object. `mapping_count` equals the set size; the three status counts sum to
    it; and `inventory_canonical_json_sha256` is the RFC 8785 digest of the
    sorted inventory array.
11. `HARNESS_SUPPLIED` may occur only under the metadata roots enumerated in the
    mapping-receipt schema. Every other target may only be `NATIVE`,
    `MECHANICALLY_MAPPED`, `UNSUPPORTED`, or `UNMAPPABLE`. Grader annotations
    are not mappings and never appear in a mapping receipt.
12. For a `MAPPED` entry, `value_canonical_json_sha256` must equal the RFC 8785
    digest of the exact target observation terminal value. `UNSUPPORTED` and
    `UNMAPPABLE` entries carry a null value digest and cannot populate a
    favorable semantic substitute.
13. Every `NATIVE` or `MECHANICALLY_MAPPED` source pointer/byte range must resolve
    inside captured native bytes and its evidence digest must match.
14. Every mapping ID is unique across the receipts for one observation, and all
    receipt target-key sets are disjoint. Multiple receipts cannot claim the
    same observation terminal value.
15. `UNSUPPORTED` and `UNMAPPABLE` required fields cannot be silently omitted or
    converted into a favorable semantic value.

## Oracle and tuple checks

1. The candidate/adapter never receives oracle bytes or derived answer content.
2. The observed tuple is compared with complete oracle tuples; per-axis set
   membership or Cartesian expansion is forbidden.
3. Oracle-required claim IDs are grader-private. They are matched to mapped
   semantic paths/predicates only after the observation is sealed.
4. Required evidence must resolve and predate the sealed observation.
5. Forbidden-behavior findings, required-claim coverage, and tuple matching are
   separate verdict components; one cannot compensate for another.
6. An oracle ambiguity or disagreement preserved before execution may allow
   multiple complete tuples. Post-result addition of a tuple creates a successor
   oracle and cannot repair the current attempt.
7. `action_record.posture` must equal `outcome.decision` whenever a decision is
   applicable; `plan_record.status` must equal `outcome.plan_status` whenever a
   plan was requested. A `SAFE_PLAN` has a non-null immutable plan artifact.
8. Oracle axis applicability and tuple not-applicable values must agree exactly.
   This is cross-file because the observation schema cannot see the oracle.
9. For `recoverability = EXACT`, the checker must establish that no disclosed
   loss affects the oracle-designated reconstruction target. Losses outside that
   target are not prohibited. For `NON_RECOVERABLE`, evidence must name the
   frozen reconstruction boundary; absence alone remains `UNKNOWN`.

## Run state and scoreability

1. Exactly one terminal run-state record exists per attempt.
2. Only `OBSERVED` may be marked `ELIGIBLE_PENDING_GATES`. All other states are
   `NON_SCOREABLE` and carry `outcome = null` in any observation wrapper.
3. `CONTAMINATED` and `STOPPED` are preserved as such; they must not be rewritten
   as `INVALID` merely because no semantic result exists.
4. `BUDGET_EXHAUSTED` and `INCOMPLETE` are not semantic failures.
5. A retry has a new run/attempt identity and cites the prior terminal state.
   Files from the prior attempt are immutable and remain reportable.
6. No aggregation, winner, dominance, narrowing, or selection statement may use
   a non-scoreable attempt.

## Native and adapter monotonicity

The mapped observation may not be semantically stronger than native output.
Specifically:

- native `UNKNOWN`, `CONFLICT`, or `REFUSE` cannot map to a more favorable value;
- a native conflict, unknown, or loss record cannot disappear;
- native unsupported/unmappable capability cannot become evidenced support;
- native byte or reconstruction uncertainty cannot become `EXACT`; and
- adapter/harness metadata cannot serve as candidate-native semantic evidence.

Violations are adapter-purity failures and yield `INVALID`, not candidate
semantic failure.

## Truncated native artifacts

A truncated stream is preserved as evidence rather than rejected by shape.
For every artifact with `truncated = true`:

1. `truncation_evidence` is present and immutable;
2. `captured_prefix_byte_length` equals the captured artifact `byte_length`;
3. when the original length is known, it is greater than the captured length;
4. when an original digest is declared, evidence resolves to the complete
   original bytes rather than a guessed digest;
5. `capture_completeness` is `PARTIAL`; and
6. the terminal run state is exactly `INCOMPLETE`, with
   `scoreability = NON_SCOREABLE` and reason code
   `NATIVE_CAPTURE_TRUNCATED`; and
7. the run state's evidence and partial-artifact refs resolve to the immutable
   native capture, captured prefix bytes, and truncation evidence.

`byte_exact = true` means the stored prefix bytes are exact; it does not claim
the complete native artifact was captured. Unknown original length/digest stays
explicitly null. Truncation is not `INVALID`, `STOPPED`, or
`BUDGET_EXHAUSTED`; those states remain available for their own accurately
recorded causes. A digest mismatch or byte alteration remains `INVALID` and is
not relabeled as truncation.

## Trial authority and sealed holdout gates

1. `trial_execution.status = AUTHORIZED` requires a non-null immutable
   `authority_ref`. `NOT_AUTHORIZED` and `UNKNOWN` require null; a generic
   authority string cannot substitute for the ref.
2. An authorized F5-D run is valid only when `trial_class = HARNESS_DUMMY`,
   `authority_kind = F5_DUMMY_TRANSPORT_ACCEPT`, and
   `scope = F5_DUMMY_TRANSPORT_ONLY`; its authorization object must pin exact
   immutable 40-hex successor freeze and source commit refs, the fixed
   `SUCCESSOR_FREEZE_MANIFEST_R2.json` path, and a resolvable immutable F5-D verdict
   ref. The manifest at the freeze ref must resolve at that exact path, name the
   exact source commit, and pass its own path/blob/digest/length freeze checks.
   The generic `authority_ref` must identify the same verdict bytes. Any other
   trial class carrying the F5-D kind, scope, verdict, or authorization object
   is invalid.
3. The resolved F5-D verdict must itself state
   `F5_DUMMY_TRANSPORT_ACCEPT` and `F5_DUMMY_TRANSPORT_ONLY`; a path, branch,
   mutable label, symbolic ref, or verdict for different source/freeze refs
   cannot authorize execution.
4. `SEALED_HOLDOUT` is invalid unless `sealed_holdout` supplies resolvable,
   immutable refs for the public commitment, private-manifest commitment,
   access-log head, independent access-log audit, custodian release, and
   external ACL evidence, with `oracle_kind = CASE_KEY`.
5. The public commitment, private-manifest commitment, access-log head/audit,
   custodian release, ACL evidence, and oracle ref must agree on the same frozen
   experiment/run/case identity through the external study protocol. A public
   digest alone is not a custodian release or ACL proof.
6. Any absent, unresolved, late, failed, or mutually inconsistent holdout gate
   makes the attempt non-scoreable. It may be rerouted as a named public
   rehearsal only under a new manifest and identity.
7. `refs.runner` and `refs.dependency_lock` are independent immutable refs; an
   environment image or harness ref does not silently stand in for either.

## Dummy-pack rule

Files under `dummy_oracles/` are public synthetic harness vectors. Their
stimuli and oracles are split so the future runner must exercise access
separation even though a human can inspect both in the repository. They must
never be used to rank a real candidate, estimate Byul conformance, construct a
holdout, or infer architecture quality.
