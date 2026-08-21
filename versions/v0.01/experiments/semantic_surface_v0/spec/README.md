# Byul Semantic Surface v0 — Experiment Specification

```text
STATUS = PROVISIONAL / NON_NORMATIVE / NOT_VALIDATED
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
IMPLEMENTATION_AUTHORITY = NONE
RESEARCH_BASELINE = AofSpds/Byul@8133e3d79c88b582bea6b8a45bc8a1970b261734
```

## Purpose

This tree defines a candidate-neutral experimental surface for asking whether a
Byul candidate makes currently surviving research obligations observable. It
does not define Byul, select an architecture, validate a model, or authorize an
implementation.

The surface converts actual repository incidents and open research constraints
into:

- public, falsifiable scenarios;
- a common observation envelope;
- non-normative candidate charters;
- a pre-registered comparison method;
- a cold-read comprehension instrument; and
- holdout selection rules without hidden answers.

## Explicit non-canonization boundary

Nothing here requires:

- a fixed five-plane architecture;
- a ledger as an ontological necessity;
- a fixed semantic-kernel object count;
- `R(S,M,L)` or any other planner signature;
- a shared internal API;
- deterministic identity after split or merge; or
- a single universal World Model.

Candidates may use different internal representations. Comparison occurs only
through observable inputs, outcomes, disclosed loss, retained conflict/unknown,
evidence, reconstruction behavior, and measured complexity.

## Outcome axes

Outcomes are deliberately separated. A single catch-all status must not collapse
these independent questions.

| Axis | Question | Values used by this specification |
| --- | --- | --- |
| `resolution` | Is the semantic question resolved? | `RESOLVED`, `CONFLICT`, `UNKNOWN`, `NOT_APPLICABLE` |
| `decision` | What action posture follows? | `EXECUTE`, `REVIEW`, `REFUSE`, `NOT_APPLICABLE` |
| `recoverability` | What reconstruction claim is supported? | `EXACT`, `PARTIAL`, `NON_RECOVERABLE`, `UNKNOWN`, `NOT_APPLICABLE` |
| `plan_status` | Is an admissible plan available? | `SAFE_PLAN`, `NO_SAFE_PLAN`, `NOT_REQUESTED`, `UNKNOWN` |

## Serialization rule

All `*.yaml` files in this tree use JSON syntax. JSON is a strict subset of
YAML, so a stdlib-only harness may parse them with `json` while YAML-aware tools
may still treat them as YAML. The schemas remain ordinary JSON Schema files.

## Read order

1. `PRE_REGISTRATION.md`
2. `schemas/scenario.schema.json`
3. `schemas/observation.schema.json`
4. `scenarios/*.yaml`
5. `candidate_charters/*.yaml`
6. `cold_read/QUESTIONNAIRE.md`
7. `cold_read/RUBRIC.md`
8. `holdout/README.md`

## Public scenarios

1. stale status locator versus later checkpoint;
2. proposal recommendation without implementation authority;
3. CRLF working-tree bytes versus canonical committed Git-blob identity;
4. normalized content falsely claimed as byte-exact reconstruction;
5. scoped authority conflict plus a resolvable positive control;
6. preservation-invalid cheap plan refusal plus a safe-plan positive control;
7. unresolved identity after split/merge; and
8. source mutation, derived invalidation, and evidence-backed rebuild.

The positive controls are mandatory. They prevent a candidate that always
returns `CONFLICT` or always refuses from passing by conservatism alone.

## Evidence pins

Every scenario cites exact paths at the baseline commit and records the Git blob
ID used when the specification was authored. The principal evidence pins are:

| Path | Git blob |
| --- | --- |
| `versions/v0.01/CURRENT_STATUS.md` | `20a8dd04702f3537c686a10d4b3c73770c8954d8` |
| `versions/v0.01/memory/13_ROUND1_ACCIDENTAL_IMPLEMENTATION_INCIDENT.md` | `4505dcc932053d2d398a99950b35de7b83277fa6` |
| `versions/v0.01/memory/14_ROUND1_RERUN_SAFETY_CORRECTION.md` | `78017ed909b8ce9421f0cfa2f25a3e64d5535aaa` |
| `versions/v0.01/memory/15_ROUND1_CLEAN_RERUN_EOL_HASH_GATE_CORRECTION.md` | `9c994bc00adea853af8d0543837de55ac871ae34` |
| `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md` | `068ea833a2eb8d0e0e9c93ce8b573aae3c35e7eb` |
| `versions/v0.01/memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md` | `8e45c0f403f6c2112eb64c136511f79ed263f3f0` |
| `versions/v0.1/MODEL_CONTRACT.md` | `8b7fb404c41a13e09de55d3adac8d309bf0352e3` |
| `versions/v0.1/src/byul_v01.py` | `467396287fa5a1c699b89485348080efac9f7b0e` |
| `versions/v0.1/tests/test_byul_v01.py` | `a39f5d3bdd91e865fdd3c98f17b688d7533df7a1` |

## Interpretation boundary

A schema-valid observation is not a conformance pass. A public-scenario match is
not semantic-preservation proof. A comparison result is not Owner Acceptance,
model validation, release authority, or production authorization.
