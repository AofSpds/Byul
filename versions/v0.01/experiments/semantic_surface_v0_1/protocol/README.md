# Semantic Surface v0.1 — Successor Transport Protocol

```text
PROTOCOL_STATUS = WORKING / NON_NORMATIVE / PRE_IMPLEMENTATION
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
SHARED_BASELINE_MUTATION_AUTHORITY = FALSE
MAIN_MERGE_AUTHORITY = FALSE
PRODUCTION_AUTHORITY = FALSE
HARNESS_IMPLEMENTED = FALSE
CANDIDATE_IMPLEMENTED_BY_THIS_PROTOCOL = FALSE
```

## Purpose

This directory defines only the transport and evidence boundary for a successor
semantic-surface experiment. It separates:

1. bytes visible to a candidate;
2. grader-only expectations;
3. byte-exact candidate-native output;
4. adapter mappings from native output to a comparison envelope;
5. exact run inputs and authorities;
6. terminal run state; and
7. the resulting observation.

It does **not** define Byul, validate any semantic claim, select an architecture,
or authorize implementation, merge, release, or production. It does not require
a ledger, plane decomposition, object count, planner signature, lifecycle API,
or candidate-internal ontology.

## Visibility boundary

| Artifact | Candidate process | Adapter process | Runner/controller | Mechanical checker | Semantic grader |
| --- | --- | --- | --- | --- | --- |
| stimulus | read | read only for invocation/transport | read | read | read after identity sanitization |
| oracle | no access | no access | locator only; content withheld from execution processes | read after native capture closes | read |
| native capture | candidate writes native bytes; does not rewrite capture record | read | write capture record | read | read after sanitization when required |
| mapping receipt | no requirement | write | preserve | read | read when mapping fidelity is disputed |
| run manifest | receive only separately disclosed execution/resource subset | receive only separately disclosed adapter subset | read/write before run | read | sanitized subset only |
| run state | no write after termination | no write after termination | write once per attempt | read | read |
| observation | no write | adapter proposes mapped values; runner seals | seal | read | sanitized copy |

The candidate and adapter must never receive oracle bytes, oracle locator names,
control labels, allowed tuples, required-claim identifiers, forbidden-behavior
text, expected verdicts, grader state, or prior candidate results. A manifest
that names an oracle is controller-private and is not a candidate packet.

## Files

- `OUTCOME_SEMANTICS.md` defines the exact referent of every outcome axis and
  the global tuple rules.
- `ADAPTER_PURITY.md` restricts adapters to auditable transport and mechanical
  mapping.
- `CROSS_FILE_INTEGRITY.md` defines checks that JSON Schema cannot enforce
  across separate files.
- `MECHANICAL_CHECK_REGISTRY.json` inventories those mandatory checks and
  distinguishes ID declarations from repeated binding references; it is a
  registry, not an implemented checker or pass receipt.
- `schemas/stimulus.schema.json` validates candidate-visible opaque byte inputs.
- `schemas/oracle.schema.json` validates grader-only keys and pre-code dummy
  harness vectors.
- `schemas/native_capture.schema.json` pins unmodified native bytes.
- `schemas/mapping_receipt.schema.json` uses unique JSON-Pointer keys to record
  a source and origin for every terminal observation value except the
  self-referential receipt-ref subtree.
- `schemas/run_manifest.schema.json` pins the experiment inputs and separates
  trial execution authority from every promotion authority; it also pins the
  runner and dependency lock and makes sealed-holdout evidence explicit.
- `schemas/run_state.schema.json` preserves terminal, non-scoreable failure and
  contamination states.
- `schemas/observation.schema.json` defines a candidate-neutral comparison
  envelope with typed conflict, unknown, and loss records.
- `dummy_oracles/` is a synthetic, public, dummy-only conformance pack. It is
  not a real candidate suite or a holdout.

## Artifact sequence

1. Freeze stimulus bytes and a separate oracle under distinct access controls.
2. Freeze spec, harness, runner, candidate, adapter, environment,
   dependency-lock, resource, input, and oracle refs in a controller-private
   run manifest. An `AUTHORIZED` trial has an immutable authority ref.
3. Expose only stimulus bytes and the authorized execution/resource subset.
4. Capture candidate-native bytes before any adapter mapping.
5. Freeze the native capture record.
6. Produce field-level mapping receipts under `ADAPTER_PURITY.md`.
7. Seal a terminal run state. Non-`OBSERVED` states are non-scoreable.
8. Seal the observation and perform cross-file mechanical checks.
9. Only then expose the oracle to the mechanical checker and blind semantic
   grader under the separate adjudication protocol.

A `SEALED_HOLDOUT` manifest additionally requires immutable evidence refs for
the public and private-manifest commitments, access-log head and independent
audit, custodian release, external ACL boundary, and a `CASE_KEY` oracle. A
missing gate cannot be represented as an authorized sealed-holdout run; use a
new `PUBLIC_REHEARSAL` manifest instead.

No failed or contaminated attempt may be overwritten. A retry is a new
`run_id` and `attempt_id` that cites the prior terminal state.

## Scope of evidence

A schema-valid file is not proof that its claims are true. JSON Schema checks
shape. `CROSS_FILE_INTEGRITY.md` checks referential and digest consistency.
`ADAPTER_PURITY.md` checks that mapping did not add semantics. A separate blind
semantic adjudication compares an eligible observation with the oracle.

The strongest result this protocol can transport is:

```text
CONFORMANCE_TO_A_FROZEN_EXPERIMENTAL_SEMANTIC_SURFACE
UNDER_DECLARED_INPUTS_ADAPTER_RESOURCES_AND_EVIDENCE
```

It cannot by itself establish scientific truth, semantic preservation in
general, candidate superiority, canonical Byul architecture, or production
fitness.

## Successor-only rule

Any material change to an oracle, outcome rule, mapping-origin rule, dummy
expected verdict, or cross-file check after harness code or candidate results
exist creates a successor protocol ref. Existing files and failed attempts stay
preserved as evidence.
