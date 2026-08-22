# Pre-code dummy oracle pack

This public pack tests only the future harness and adapter boundary. It contains
13 candidate-visible stimuli under `stimuli/`, 13 frozen actual-side packets
under `actuals/`, and 13 grader-only semantic/expected keys under `oracles/`.
File names and runtime IDs are opaque. Stimulus/actual pairing uses only the
actual packet's `stimulus_id` and exact `stimulus_ref`; oracle pairing occurs
only after native capture closes through the oracle's independently checked
`stimulus_id` and `stimulus_ref`.

## Visibility and read order

1. The controller validates an actual packet against
   `../schemas/dummy_actual_fixture.schema.json` and verifies its exact stimulus
   ref, embedded bytes, event evidence, and binding baseline.
2. The dummy driver receives only the packet's `/driver_visible` subtree. It
   receives native-emission and compact adapter-projection inputs, but no oracle
   locator, expected verdict, expected reason code, or case profile.
3. The controller retains `/controller_only`. That subtree contains the complete
   correct binding-token baseline, including runner and dependency-lock tokens,
   plus non-oracle stop, canary, or byte-limit event inputs when applicable.
4. The runner captures native bytes and seals the actual-side records without
   reading an oracle. The mechanical checker may resolve the grader key only
   after capture closes.

The native emissions and projections duplicated in grader keys are comparison
values, never runtime driver inputs. A conforming implementation must source
runtime bytes and control events only from the matching actual packet. It must
not infer behavior from an oracle file, profile label, file name, stimulus ID,
or literal fixture value.

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
- controller-stopped run; and
- exact byte-limit truncation with frozen complete bytes, captured prefix,
  lengths, SHA-256 values, and controller-event evidence.

The truncation vector is mechanical-only. Its separated oracle records the
non-scoreable expectation because `XF_TRUNC_001` terminates it before semantic
grading; its actual packet contains no expected disposition or reason code.

Expected terminal state, mechanical disposition, semantic disposition,
scoreability, and reason codes are stored only in oracle files. Candidate-side
native emissions and compact adapter projections are frozen separately in the
actual packets, while STOPPED and CONTAMINATED outcomes are driven by
evidence-bearing controller events. A future dummy runner may materialize full
native-capture, receipt, state, and observation documents from actual packets
without reading oracle bytes. That implementation is outside this protocol
task.

These vectors must not be used as candidate requirements, candidate training
examples, holdout cases, Byul validation, architecture evidence, or selection
evidence.
