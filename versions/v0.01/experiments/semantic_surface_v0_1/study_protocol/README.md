# Semantic Surface v0.1 — Study Protocol

```text
EXPERIMENT_FAMILY = BYUL-SEMANTIC-SURFACE
SUCCESSOR_VERSION = v0.1
OPERATING_ROLE = ASA-ME
STATUS = PROTOCOL_DESIGN_ONLY / NOT_EXECUTED / NON_NORMATIVE / NOT_VALIDATED
BASELINE_REPOSITORY = AofSpds/Byul
BASELINE_COMMIT = 8133e3d79c88b582bea6b8a45bc8a1970b261734
V0_REVIEW_TARGET = d3b328c09e009fb24ede309ffae4fed66d5c680f
V0_DISPOSITION = PRESERVE_AS_EVIDENCE / DO_NOT_EDIT / CANDIDATE_TRIAL_GATE_CLOSED
SELECTION_AUTHORITY = NONE
MAIN_MERGE_AUTHORIZED = FALSE
PRODUCTION_AUTHORIZED = FALSE
```

## Purpose

This directory defines only the successor study controls required after the
three correlated adversarial reviews closed the v0 candidate-trial gate. It does
not implement a harness, adapter, candidate, holdout case, or grading result.

The successor separates two independent evidence tracks:

- `V0–V3`: repository visibility and cold-read comprehension; and
- `F0–F10`: successor conformance preparation, sealed evaluation, blind
  adjudication, and the successor-only C3 route.

A failure or missing result in one track remains a failure or missing result. It
does not authorize rewriting or reinterpreting a completed run in the other
track.

## Binding interpretation

- The existing `11/16` cold-read report is a
  `BASELINE_ISOLATION_UNVERIFIED` pilot. It is useful for instrument repair but
  is excluded from causal visibility arithmetic.
- Public scenarios are development probes, not comparative ranking evidence.
- C0 is archival calibration only. It is not an equal prospective entrant.
- A holdout that is absent, leaked, unsealed, under-sized, or not independently
  adjudicated forces `INSUFFICIENT_EVIDENCE`.
- C3 is outside the current candidate trial. A qualifying trigger can authorize
  only a separately approved successor experiment with a fresh holdout.
- Agreement with an experimental semantic surface is not proof that the
  surface is true, canonical, or a superior Byul architecture.

## Files

| File | Function |
| --- | --- |
| `EXECUTION_SCHEDULE.md` | Independent visibility and conformance schedules with failure-closed gates |
| `VISIBILITY_PROTOCOL.md` | Reader isolation, factorial treatment, grading, reliability, and exact threshold arithmetic |
| `ACCESSIBLE_PATH_POLICY.yaml` | Machine-readable path and tool access rules for each cold-read arm |
| `HOLDOUT_PROTOCOL.md` | External custody, balancing, novelty, commitment, access, reserve, and contamination rules |
| `ADJUDICATION_PROTOCOL.md` | Mechanical validation followed by sanitized dual-blind semantic grading |
| `MECHANICAL_CHECK_BINDINGS.json` | Exact mapping from twelve adjudication gates to the core cross-file registry |
| `C3_SUCCESSOR_HOLDOUT_RULE.md` | Numeric successor-only eligibility rule and mandatory fresh-holdout route |
| `BUDGET_ACCOUNTING.md` | Non-fungible wall, worker, model, tool, and human ceilings |
| `schemas/holdout_private_manifest.schema.json` | Private externally stored holdout manifest contract |
| `schemas/holdout_public_commitment.schema.json` | Non-secret salted commitment and balance disclosure contract |
| `schemas/access_log.schema.json` | Chained holdout-access event log contract |
| `schemas/adjudication.schema.json` | Mechanical, semantic, disagreement, freeze, and re-link record contract |

## Required ordering

1. Preserve v0 and this successor design as separate evidence.
2. Freeze visibility instruments and inaccessible grading material outside the
   reader bundles.
3. Pin pre-candidate treatment bundles and their accessible-path manifests.
4. Freeze all corrected schemas, charters, budgets, dummy harness controls, and
   interpretation rules at an exact successor specification ref.
5. Obtain separate result-blind adversarial verdicts for (a) a dummy-only
   transport harness and (b) a claim-bearing candidate trial.
6. A narrow dummy-harness verdict may open only synthetic transport work; it
   does not depend on or substitute for a holdout.
7. Select, oracle-review, seal, and commit the external holdout before any
   prospective candidate is built.
8. Only a separate candidate-trial verdict, plus the sealed holdout and all
   engineering controls, may route to prospective candidate construction.

## External coordination required

The following conditions cannot be satisfied by repository edits or a single
local Codex environment:

- `EXTERNAL_COORDINATION_REQUIRED / VISIBILITY_READERS`: at least two distinct
  model lineages and two human readers in every executed arm;
- `EXTERNAL_COORDINATION_REQUIRED / BLIND_GRADERS`: two independent graders and
  a separate tie adjudicator, with rubric/key isolation;
- `EXTERNAL_COORDINATION_REQUIRED / HOLDOUT_ROLES`: mutually separated selector,
  custodian, oracle author/reviewer, runner, and graders;
- `EXTERNAL_COORDINATION_REQUIRED / ACL_STORE`: encrypted non-Git storage for
  plaintext holdout material, salt, private manifest, and private access log;
- `EXTERNAL_COORDINATION_REQUIRED / COMMITMENT_WITNESS`: an external timestamp or
  equivalent witness for the public salted commitment; and
- `EXTERNAL_COORDINATION_REQUIRED / MODEL_ACCOUNTING`: trustworthy per-session
  lineage, context, token, and tool-usage records.

Until those controls exist, local work may validate document syntax and prepare
rehearsal artifacts only. It cannot produce the visibility, holdout, comparative,
H3, C3-trigger, validation, or selection claims governed here.

## Source controls read for this design

This protocol was derived from the three raw v0 adversarial reviews, the
consolidated S4 gate, the current questionnaire/rubric/pilot report, the v0
holdout rules and pre-registration, memories 13–17, and
`OWNER_TRIAL_AUTHORIZATION.md`. Owner trial authorization permits bounded
non-production research work; the consolidated integrity blockers remain
non-waivable for any claim-bearing successor run.
