# Pre-code dummy oracle pack

This public pack tests only the future harness and adapter boundary. It contains
12 candidate-visible stimuli under `stimuli/` and 12 grader-only keys under
`oracles/`. File names and runtime IDs are opaque; pairing occurs only through
the oracle's `stimulus_id` and exact `stimulus_ref`.

The frozen profiles are:

- one valid positive;
- always-unknown, always-conflict, and always-refuse semantic mismatches;
- malformed native output;
- schema-shaped but semantically incomplete output;
- native/capture digest mismatch;
- adapter-erased conflict;
- adapter-erased loss;
- wrong immutable refs;
- contaminated run; and
- controller-stopped run.

The expected native bytes, compact adapter projection, terminal state,
mechanical disposition, semantic disposition, scoreability, and reason codes
are stored only in the oracle files. A future dummy runner may materialize full
native-capture, receipt, state, and observation documents from these keys, but
that implementation is outside this protocol task.

These vectors must not be used as candidate requirements, candidate training
examples, holdout cases, Byul validation, architecture evidence, or selection
evidence.
