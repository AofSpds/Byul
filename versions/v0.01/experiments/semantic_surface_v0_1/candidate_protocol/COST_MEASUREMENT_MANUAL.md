# Cost Measurement Manual

```text
MANUAL_VERSION = 0.1.0
SCOPE = C1 / C2 PROSPECTIVE COMPARISON; C0 ARCHIVAL CALIBRATION DISCLOSURE
UNKNOWN_IS_ZERO = FALSE
SCALAR_SCORE = FORBIDDEN
PERMITTED_COMPARISON = VECTOR / PARETO ONLY
```

## 1. General rules

Every value must include a unit, measurement scope, collection method, and raw
evidence locator. `UNKNOWN` is a value state, not the number zero. An unknown
value must include `unknown_reason` and may not be imputed, omitted, ranked as
small, or converted to an empty collection.

Measure C1 and C2 from separate clean environments under
`EXECUTION_BUDGET.yaml`. Report actual consumption even when it is below the
cap. Candidate-specific adapter work, schemas, configuration, tests, repair,
and operator work are part of total burden. Inherited Git, Python, operating
system, runner, and harness capabilities are disclosed separately rather than
treated as free candidate code.

Generated or vendored code is not permitted by `BUILD_BUDGET.yaml`. If either
is later authorized in a successor specification, report its full bytes, files,
generation time, generator/dependency cost, and generated SLOC separately; do
not hide it from total burden.

## 2. Build-level scope

Record the following for each candidate and its adapter:

| Metric | Included scope | Required evidence |
| --- | --- | --- |
| Runtime SLOC | Candidate executable source | File manifest and line-count receipt |
| Schema/config SLOC | Candidate-specific JSON/YAML/TOML/configuration | File manifest and line-count receipt |
| Adapter SLOC | Invocation, serialization, and mapping source | Adapter manifest and line-count receipt |
| Test SLOC | Candidate and adapter tests | Test manifest and line-count receipt |
| Files | Every candidate-owned regular file and symlink | Path/type/byte-digest inventory |
| Dependencies | Direct standard-library modules, external executables, packages, services | Import trace and dependency lock |
| Build wall time | Controller start through frozen complete or exhausted ref | Monotonic timestamps |
| Active worker time | Time spent issuing or reviewing build actions | Worker activity log |
| Model usage | Calls, input/output tokens, model/snapshot/config | Provider usage receipt |
| Tool usage | Every tool invocation and result status | Controller tool log |
| Repair effort | Each result-blind repair trigger, actions, time, tokens, tool calls | Repair-round receipts |
| Setup burden | Environment preparation and candidate-specific setup commands | Setup transcript |

### 2.1 SLOC counting

Use UTF-8 text after the frozen ref is created. A physical line counts when it
contains a non-whitespace character and is not solely a language-recognized
comment. Python docstring lines count because they are runtime syntax. For JSON,
every nonblank line counts, including lines containing only braces or brackets.
For YAML, comment-only lines do not count; every other nonblank line counts.
Markdown is not SLOC and is reported as nonblank documentation lines. A symlink
counts as one file and its target remains independently counted when owned by
the candidate. Hard links count once in logical bytes and once per directory
entry in file count; allocated bytes are reported separately.

Count distinct top-level imported standard-library modules as direct standard-
library dependencies. Capture modules actually imported in a clean dummy run as
the runtime dependency trace. Python and Git are inherited executables and are
not called zero dependencies: record their versions, executable digests,
installed allocated bytes when measurable, and invoked subcommands.

## 3. Fixture-level scope

All candidates receive one byte-identical, read-only fixture export. Measure:

1. source logical bytes and file count before ingest;
2. source allocated bytes before ingest;
3. candidate-owned derived logical and allocated bytes after ingest;
4. Git object-store logical and allocated bytes before and after ingest;
5. temporary peak bytes;
6. incremental candidate, Git, and temporary deltas for each mutation; and
7. bytes remaining after deterministic cleanup.

Never combine source bytes, candidate record bytes, current projection bytes,
Git-object overhead, adapter artifacts, runner evidence, and temporary bytes.
Report all seven scopes independently. Use the same clean fixture digest and the
same filesystem/container image. Compression must be reported as both logical
uncompressed input bytes and actual allocated persisted bytes; neither replaces
the other.

## 4. Operation-level scope

Measure the exact warm-up and repetition counts in `EXECUTION_BUDGET.yaml`.
Public and holdout semantic cases are not performance warm-ups. Performance
samples use only the frozen non-secret benchmark fixture.

For each operation record:

- cold ingest wall time, process CPU time, peak memory, read/write bytes, and
  persisted delta;
- query wall/CPU time and native bytes returned;
- mutation wall/CPU time, records/files/objects added, and persisted delta;
- reconstruction wall/CPU time, records/objects read, operator actions, and
  output digest;
- failure/recovery wall/CPU time, data unavailable, recovery actions, and final
  evidence state; and
- timeout, signal, exit status, and resource-exhaustion state.

Use monotonic nanoseconds for duration and cgroup/process counters for resource
use. Preserve every raw sample and report minimum, median, p95, and maximum.
Do not compare a warm operation for one candidate with a cold operation for
another. A cache that cannot be equivalently reset must be disclosed and makes
that operation cost `INCOMPARABLE`.

## 5. Human-level scope

One operator action is one manual command submission, edit approval, file move,
credential/session intervention, judgment, or recovery decision. Automated
subcommands inside one frozen script are not additional human actions but remain
tool/process events.

Record separately:

- build-time operator actions and active minutes;
- fixture preparation actions and active minutes;
- ordinary operation actions and active minutes;
- result-blind adapter/charter/completeness adjudications;
- blind semantic adjudications;
- disagreement-resolution actions, without erasing the original disagreement;
- failure-recovery actions and active/elapsed minutes; and
- required expertise as a factual task description, not a numeric prestige
  score.

Idle wait and compute time are excluded from active human time but included in
elapsed wall time. If reliable active-time capture is unavailable, report
`UNKNOWN` with the reason.

## 6. Adapter scope

Adapter cost is never folded into candidate cost without also being visible as
its own vector. Record adapter files, SLOC, standard-library imports, build time,
model/tool usage, runtime latency, native-byte reads, envelope bytes produced,
mapping-table rows, audit actions, and repair actions.

A semantic value supplied by the harness or evaluator is not adapter output and
must be labelled accordingly. If adapter mapping is `UNSUPPORTED` or
`UNMAPPABLE`, record that state; do not estimate the missing candidate behavior
as zero work.

## 7. Inherited-service scope

At minimum disclose:

- Git version, executable digest, installed allocated bytes when measurable,
  input object-store bytes, object-store delta, commands, and relevant config;
- Python version, executable digest, standard-library location/bytes when
  measurable, and imported modules;
- container image digest and image size;
- operating-system/kernel and filesystem type;
- harness/runner source refs, SLOC, dependencies, and runtime resources; and
- any human-maintained fixture/control manifest supplied to all candidates.

Inherited capability is not charged as candidate-owned SLOC, but it is not
reported as zero cost. If an inherited capability materially performs history,
content addressing, transactionality, parsing, or reconstruction, name the
capability and the candidate call path that invokes it.

## 8. Recovery scope

For every injected or incidental failure, report detection latency, evidence
lost or inaccessible, automatic steps, manual steps, active human time, elapsed
time, bytes read/written, number of retries, final recoverability state, and
whether the original failure evidence remains preserved. Silent retry is a
protocol violation. A successful recovery does not erase the original cost or
failure record.

## 9. Missing values

The only missing-value token is `UNKNOWN`. Each occurrence requires:

```text
value_state = UNKNOWN
unknown_reason = <specific reason>
collection_attempt = <method and evidence ref>
comparison_effect = AXIS_NOT_ORDERABLE
```

`null`, absent fields, empty lists, empty strings, and `0` do not mean unknown.
Zero is valid only when a measurement was performed and immutable evidence shows
that the counted event or byte delta was actually zero.

## 10. Permitted comparison

Publish the complete semantic vector and these cost sub-vectors:

1. build and implementation effort;
2. candidate-owned static size;
3. adapter burden;
4. fixture/persistence burden;
5. operation resource distributions;
6. human/operational burden;
7. inherited-service affordances; and
8. failure/recovery burden.

No scalar complexity score, weighted sum, rank aggregation, post-hoc threshold,
or cost-per-pass number is permitted. A cost vector `A` dominates `B` only when
every compared cost axis is known and no greater for `A`, at least one is
strictly lower, and scopes and measurement methods match. An unknown,
scope mismatch, crossed trade-off, or material inherited-affordance difference
prevents domination and yields `INCOMPARABLE` on cost. Semantic eligibility and
ordering are governed separately by `INTERPRETATION_RULES.md`.
