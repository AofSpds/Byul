# Result-Blind Candidate Charter Audit

```text
AUDIT_VERSION = 0.1.0
AUDIT_TIME = AFTER CANDIDATE/ADAPTER FREEZE / BEFORE ANY REAL STIMULUS
PUBLIC_RESULT_ACCESS = FORBIDDEN
HOLDOUT_ACCESS = FORBIDDEN
SIBLING_ACCESS = FORBIDDEN
WAIVER = NONE
```

## 1. Purpose

The audit classifies the frozen implementation by operational capability rather
than its directory name or author description. It does not judge scenario
success. An auditor must have authored neither the candidate nor its adapter and
must see only the charter, frozen source/ref manifests, dependency/storage maps,
dummy-only transcripts, and access/budget receipts.

These dummy boundary probes test only transport, completeness, and charter
classification. They are not expectation-reversing/metamorphic semantic cases
and do not satisfy correction 10 or the F3 exit gate.

C0 is an archival calibration specimen, C1 and C2 are prospective candidates,
and C3 is not a member of this trial. No role is preferred and no role is a
promotion state.

## 2. Mandatory evidence packet

The controller supplies an opaque candidate label plus:

1. exact candidate and adapter commit/tree/blob manifests;
2. immutable base and isolated repository/container/branch/write-scope receipt;
3. complete source, dependency, executable, service, and persisted-location
   inventories;
4. native interface and capability declaration;
5. static call/dataflow map for state writes, historical reads, and rebuild;
6. dummy-only boundary-probe transcripts;
7. build-budget and completeness receipts; and
8. adapter audit receipt.

The packet must not contain a public or holdout case, answer, score, candidate
comparison, C0 real-case result, or sibling source. If prohibited material is
present, the audit returns `CONTAMINATED` without inspecting performance.

## 3. Audit procedure

1. Verify all refs, manifests, and isolation receipts.
2. Inventory every candidate-owned persisted path and every inherited service.
3. Trace each native state-writing and reconstruction path from input bytes to
   source evidence, Git operations, candidate records, and projections.
4. Search for generic record identity, ordering/parent links, append, reducer,
   replay, cursor, event-fold, and projection-rebuild mechanisms.
5. Run only the charter's synthetic boundary probes inside a disposable clone.
6. Verify that the adapter did not supply any observed capability.
7. Apply the role-specific decision table below.
8. Freeze the audit receipt before the global candidate-ref barrier opens.

## 4. Role decision tables

### 4.1 C0 — archival calibration

The only passing classification is `ARCHIVAL_CALIBRATION_ONLY`. Verify every pin
and all 19 source blobs in `C0_ARCHIVAL_CALIBRATION.yaml`. Any patch, alternate
memory root, missing blob, or semantic adapter repair returns
`BLOCKED_C0_ARCHIVAL_PIN_MISMATCH`. C0 is never comparison-eligible.

### 4.2 C1 — Git-native control

| Observation | C1 classification |
| --- | --- |
| Git object database and commit graph are the only historical substrate | Required |
| Trial changes are ordinary file changes/commits in the assigned Git graph | Permitted |
| Current control manifest or derived index rebuilt from a selected Git tree | Permitted |
| Reconstruction selects Git commit/tree/blob rather than folding custom records | Required |
| Candidate-owned generic ordered append change records | Boundary violation |
| Candidate reducer/replay derives arbitrary current state from those records | Boundary violation |
| Git notes/messages/blobs used as a disguised generic replay journal | Boundary violation |
| Undisclosed database, object store, service, or second semantic authority | Boundary violation |

C1 passes only if all three probes in `C1_GIT_NATIVE_CONTROL.yaml` pass and no
two prohibited mechanisms collectively recreate a candidate-owned generic
change layer.

### 4.3 C2 — candidate-owned change layer

| Observation | C2 classification |
| --- | --- |
| Candidate-owned append record format with immutable record identity | Required |
| Explicit source/predecessor linkage | Required |
| Deterministic reducer/replay owned by candidate code | Required |
| Current projection rebuild from the candidate record set | Required |
| Prior records remain addressable after append | Required |
| Git stores records but candidate code owns record semantics/replay | Still C2 |
| Only ordinary Git history; no candidate record/replay layer | Incomplete C2 |
| Bitemporal/CRDT/TMS/fixed-plane or undisclosed service machinery | Scope violation |
| Candidate projection silently outranks or deletes source evidence | Scope violation |

C2 passes only if all three probes in
`C2_CANDIDATE_OWNED_CHANGE_LAYER.yaml` pass, its inherited Git affordances are
fully disclosed, and no prohibited richer structure is present.

### 4.4 C3 — successor only

Any C3 source, adapter, build allocation, or real execution in this trial is a
non-waivable charter violation. `C3_SUCCESSOR_TRIGGER.yaml` may only be evaluated
after this trial closes; it cannot retroactively admit C3.

## 5. Audit outcomes

| Outcome | Meaning | Route |
| --- | --- | --- |
| `PASS` | Frozen implementation matches the declared C1 or C2 operational boundary | Continue to remaining pre-run gates |
| `ARCHIVAL_CALIBRATION_ONLY` | Exact C0 specimen pinned | Calibration only; exclude from comparisons |
| `INCOMPLETE_UNDER_BUDGET` | Required role capability is absent after allowed result-blind repairs | Freeze partial evidence; no semantic failure claim |
| `BOUNDARY_VIOLATION` | Implementation has another role's operational capability or forbidden richness | Stop; recharter only in a successor spec |
| `INDETERMINATE` | Evidence cannot establish the boundary | Stop and default to `INCOMPARABLE` |
| `BLOCKED` | Required pin, isolation, budget, adapter, or completeness evidence is unavailable | Keep real-stimulus gate closed |
| `CONTAMINATED` | Auditor or build accessed prohibited source/result/oracle material | Exclude run; no silent rerun |

When an audit outcome must be serialized as a run, audit outcome
`INCOMPLETE_UNDER_BUDGET` uses run state `INCOMPLETE` and reason code
`INCOMPLETE_UNDER_BUDGET`.

Passing dummy behavior does not establish semantic conformance. Failing a
boundary or completeness audit is not evidence that the architecture's research
hypothesis is false.

## 6. Receipt

The frozen receipt records the opaque label, declared role, auditor/controller
IDs, evidence packet digest, exact candidate/adapter refs, every probe result,
all ambiguous findings, final outcome, timestamp, and receipt digest. Candidate
identity may be re-linked only after all charter audits and real-run judgments
are frozen.

No implementation may be relabelled after any public or holdout result is known.
A boundary change requires a successor specification, a clean build context,
fresh refs, all result-blind audits, and—if holdout evidence is sought—a fresh
unexposed holdout.
