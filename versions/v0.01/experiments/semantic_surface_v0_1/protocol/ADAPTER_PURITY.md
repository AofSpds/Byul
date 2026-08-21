# Adapter purity contract

## Role

An adapter is a transport boundary, not a second candidate. It may invoke a
declared native capability, preserve native output bytes, and mechanically map
native fields into the common observation vocabulary. It may not answer the
semantic question.

## Allowed operations

- invoke a predeclared candidate-native entrypoint;
- pass frozen stimulus bytes without semantic modification;
- capture stdout, stderr, exit status, files, and declared artifacts;
- decode a declared transport encoding;
- parse a declared media type without discarding the raw bytes;
- rename fields through a frozen lookup table;
- select a value with an exact JSON Pointer or byte range;
- perform a lossless primitive type conversion whose rule is frozen;
- map a native enum through a total, frozen table; and
- populate run/stimulus/native-capture metadata supplied by the harness.

Every terminal observation value outside `/mapping_receipt_refs` must have one
entry in the receipt's JSON-Pointer-keyed `mappings` object, using one of the
five origins defined by the schema. The keyed object makes duplicate target
fields unrepresentable; the runner still recomputes exact leaf coverage.

## Forbidden operations

An adapter must not:

- read an oracle, rubric, expected tuple, control label, grader record, or prior
  candidate result;
- branch on stimulus ID, oracle ID, case name, literal fixture value, file name,
  or hidden/public status, except for a frozen opaque dispatch token used only
  to select a declared native entrypoint;
- infer chronology, authority, conflict, equivalence, preservation, loss,
  recoverability, plan safety, or action posture from stimulus facts;
- invent evidence, required claims, conflicts, unknowns, losses, plans,
  artifacts, reconstruction results, or refusal reasons absent from native
  output;
- replace contradictory, unknown, unsupported, or lossy native output with a
  more favorable value;
- summarize or normalize native bytes before byte-exact capture;
- delete a native conflict, unknown, or loss record from the mapped envelope;
- use a model, network service, repository search, or external database to add
  semantics; or
- hide candidate-specific logic as harness, fixture, mapping table, manual
  adjudication, or post-processing.

Semantic logic required to satisfy a case belongs in the candidate and counts
against the candidate budget.

## Mapping origins

| Origin | Meaning | Native pointer required | May populate candidate semantic fields |
| --- | --- | --- | --- |
| `NATIVE` | value is present verbatim in native output | yes | yes |
| `MECHANICALLY_MAPPED` | value follows from a frozen lossless transport mapping | yes | yes |
| `HARNESS_SUPPLIED` | run/input/ref metadata known independently by the harness | no; immutable harness evidence required | metadata only |
| `UNSUPPORTED` | candidate exposes no native capability/value | capability evidence required | only an explicit unsupported marker; never a favorable substitute |
| `UNMAPPABLE` | native information exists but no permitted mechanical mapping exists | yes | only an explicit unmappable marker |

`HARNESS_SUPPLIED` is schema-limited to these metadata roots:
`schema_version`, `protocol_id`, observation/run/attempt/candidate identifiers,
immutable run/native/stimulus refs, run status and scoreability, native payload
digests, and the fixed authority boundary. It cannot populate `outcome`,
semantic claims, conflicts, unknowns, losses, actions, plans, produced
artifacts, or reconstruction evidence. Grader annotations are separate
adjudication records; `EVALUATOR_CODED` is intentionally not a mapping origin.

`UNSUPPORTED` and `UNMAPPABLE` are not `UNKNOWN` semantic answers unless the
candidate natively emitted that semantic answer. They are mapping states and
normally make a required field non-scoreable or incomplete.

## Required audit

Before any real case is executed, a result-blind auditor freezes:

- adapter source and dependency refs;
- declared native entrypoints and opaque dispatch table;
- every enum/rename/type-conversion mapping table;
- permitted input and output media types;
- adapter SLOC and files;
- network and external-tool denial policy; and
- a field inventory proving that every mapped observation field receives a
  receipt.

The dummy suite must demonstrate at least these properties:

1. a valid native answer maps without change;
2. always-unknown, always-conflict, and always-refuse outputs are not improved;
3. malformed native output does not become a valid answer;
4. a semantically incomplete native output remains incomplete;
5. a native digest mismatch is rejected;
6. erased native conflict or loss records are detected;
7. wrong spec/candidate/adapter/input refs are rejected; and
8. contaminated or stopped runs remain non-scoreable.

A truncated artifact may be recorded with mandatory truncation evidence, but
its attempt remains non-scoreable. Exact captured-prefix bytes are not evidence
that the complete native output was captured.

Passing the dummy suite demonstrates only transport behavior on frozen dummy
vectors. It does not validate the harness or adapter for real cases.
