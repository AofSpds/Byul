# Visibility Protocol v0.1

```text
PROTOCOL_ID = BYUL-VISIBILITY-v0.1
STATUS = PROTOCOL_DESIGN_ONLY / NOT_EXECUTED
BASELINE_COMMIT = 8133e3d79c88b582bea6b8a45bc8a1970b261734
EXISTING_11_OF_16_REPORT = BASELINE_ISOLATION_UNVERIFIED / PILOT_ONLY
CAUSAL_BASELINE_ELIGIBLE = FALSE
MAX_SCORE_PER_READER = 16
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
```

## 1. Question and non-claim

The study asks whether a deliberately limited repository surface helps a cold
reader recover the current research posture without converting candidates into
canonical Byul. It does not measure architecture quality, semantic preservation,
candidate superiority, model validation, or Owner Acceptance.

The existing report at
`semantic_surface_v0/spec/cold_read/results/BASELINE_8133E3D_CONTEXT_BLIND_01.md`
is retained as instrument-design evidence only. Its raw response, rubric,
treatment surface, and self-grade first appear together; its isolation and
pre-treatment ordering therefore cannot be independently established. Its
reported `11/16` must not enter baseline medians, effect sizes, reliability, or
threshold calculations.

## 2. Intervention arms

The preferred design is a four-arm, reader-between-subjects factorial probe.
Every bundle is read-only, omits `.git`, and is audited against
`ACCESSIBLE_PATH_POLICY.yaml`.

| Arm | Surface | Purpose |
| --- | --- | --- |
| `B` | Exact exported baseline tree at `8133e3d...` | Fresh uncontaminated baseline |
| `L` | Baseline plus locator-only changes | Estimate the locator intervention |
| `M` | Baseline locators plus the state-map file only | Estimate the state-map intervention |
| `LM` | Locator changes plus the state-map file | Measure the combined surface and interaction |

The bundle generator must pin every included path and SHA-256 in an external
manifest before candidate construction. `L`, `M`, and `LM` may not contain the
questionnaire, rubric, answer key, previous answers, scores, study protocol,
candidate/adapter code, candidate results, holdout material, or grader notes.

If construction of `M` is operationally impossible, `B`, `L`, and `LM` may run,
but the report must state `STATE_MAP_EFFECT_NOT_IDENTIFIABLE`. If only `B` and
`LM` run, the result is `DESCRIPTIVE_ONLY_NO_COMPONENT_ATTRIBUTION`. Missing the
minimum sample in any arm used for a causal contrast yields
`VISIBILITY_INSUFFICIENT_EVIDENCE` for that contrast.

## 3. Reader eligibility and minimum sample

Each executed arm requires, after exclusions:

- two fresh model-reader instances from two distinct model lineages; and
- two distinct human readers.

Thus the four-arm study requires at least 16 valid response units: eight fresh
model sessions and eight humans. A human reads one arm only. A model instance
reads one arm only; no context, transcript, memory packet, scratch artifact, or
tool output crosses sessions. A lineage may supply a fresh instance to each arm,
but the lineage must be recorded and its sessions must remain isolated.

Readers are ineligible if they authored or read any surface, rubric, key, prior
response, candidate, adapter, or adversarial review for this experiment. Prior
Byul exposure must be recorded. Exposure discovered after starting is retained
as contamination evidence and excluded by the pre-registered rule; it is not
silently replaced after the response is viewed.

If the per-arm minimum cannot be met, the arm remains a pilot and returns
`VISIBILITY_INSUFFICIENT_EVIDENCE`. “When feasible” is not a sample-size waiver.

## 4. Instrument and reader access

The questionnaire is delivered externally at session start by exact SHA-256.
The unchanged grading rubric, answer key, critical-error examples, prior
responses/results, assignment seed, and arm mapping remain inaccessible to all
readers. The reader receives no chat history or oral briefing.

Each reader has at most 20 elapsed minutes after the first bundle read. The
controller records, in order:

1. opaque reader instance and arm labels;
2. reader type and lineage or human-reader class;
3. prior-exposure declaration;
4. session start, first-read, submission, and timeout timestamps;
5. every normalized path opened and access result;
6. exact prompt/questionnaire digest;
7. bundle-manifest and bundle digests; and
8. the unedited raw response digest and external immutable locator.

A timeout response is graded as submitted; it is not excluded for low quality.
Only a technical failure before the first repository read may use a pre-declared
reserve reader. Any response observed before replacement freezes the original
as a non-scoreable event and forbids selective retry.

## 5. Randomization

Randomization is performed before recruitment completion by an independent
coordinator who is not a reader or grader.

1. Generate a 256-bit cryptographic seed and a separate random 256-bit salt.
2. Publish only
   `SHA-256("BYUL-VISIBILITY-ASSIGN-v0.1\\0" || salt || seed)` before assignment.
   Keep seed and salt in the external ACL store.
3. Human readers are block-randomized by declared prior Byul exposure and
   technical/research experience. Within each block, sort opaque reader IDs,
   apply Fisher–Yates using a counter-mode SHA-256 stream derived from the seed,
   and allocate cyclically to the least-filled arm in the order produced by a
   separately shuffled arm list.
4. For model readers, each distinct lineage forms a block. Create one fresh
   session per arm and Fisher–Yates-randomize the arm-to-opaque-session mapping.
5. Keep arm labels opaque to readers and semantic graders. Freeze the assignment
   table digest before any session starts.
6. Release seed, salt, assignment table, and reproducibility receipt only after
   all raw responses and grades are frozen, unless privacy rules require the
   seed to remain private. If private, an independent verifier publishes a
   deterministic assignment-verification receipt.

No post-response balancing or discretionary reassignment is allowed.

## 6. Grading and citation verification

Each response is processed in this order:

1. The custodian replaces explicit arm labels, treatment filenames, absolute
   paths, model/person names, and repository refs with opaque tokens. Claims and
   wording are not rewritten.
2. Two independent graders, blind to arm and reader identity, grade all eight
   questions `0`, `1`, or `2` using the frozen rubric. They also mark each of the
   six critical-error codes independently.
3. The two original score vectors and flags are frozen before discussion.
4. A separate blind adjudicator resolves every difference. The final score is
   the adjudicator's rubric-supported integer, never an average. If the rubric
   cannot resolve the difference, the question is `UNSCORABLE`; the whole
   response is non-scoreable and remains in the audit trail.
5. After semantic grades freeze, an evidence verifier re-links opaque citations
   to the assigned bundle. For each question, no valid supporting citation caps
   the final question score at `0`; a citation that resolves but does not support
   the material claim caps it at `1`; otherwise the semantic score stands.
6. The evidence-capped score and critical-error flags freeze before arm labels
   are disclosed.

The six critical-error codes are exactly:

- `VIEW_AS_SOURCE_AUTHORITY`;
- `RECOMMENDATION_AS_IMPLEMENTATION_AUTHORITY`;
- `NORMALIZED_AS_BYTE_EXACT`;
- `CANDIDATE_AS_CANONICAL_BYUL`;
- `ALWAYS_REFUSE_ACCEPTED_AS_SAFE`; and
- `TEST_PASS_AS_VALIDATION`.

## 7. Reliability gate

Reliability uses the two original, pre-adjudication graders over all scoreable
reader-question units pooled across executed arms.

- `P_exact = exact score agreements / all dual-scored units`.
- `kappa_qw` is quadratic-weighted Cohen's kappa for categories `0,1,2`, with
  weight `w(i,j) = 1 - ((i-j)^2 / 4)` and expected agreement calculated from the
  two graders' observed marginal distributions.
- Critical-error agreement is calculated per code as identical present/absent
  flags divided by all response-code units.

The reliability gate passes only when:

- `P_exact >= 0.75`;
- `kappa_qw >= 0.70`; and
- critical-error exact agreement equals `1.00`.

If a denominator is zero or kappa is undefined because both graders use only one
category, reliability is `UNESTIMABLE`. A failed or unestimable gate permits
publication of raw dual grades and adjudication but forbids a visibility-effect
claim: `VISIBILITY_RELIABILITY_FAILED`.

## 8. Exact threshold arithmetic

For each arm `a`, let `S(a,r)` be a valid reader's final evidence-capped total
from `0` to `16`. Sort totals and define the arm median conventionally; with an
even sample it is the exact arithmetic mean of the two middle integer totals and
therefore may end in `.5`.

Let:

- `M_B = median_r S(B,r)`;
- `M_a = median_r S(a,r)`; and
- `G = 16 - M_B`.

If `G = 0`, the study has a baseline ceiling and returns
`VISIBILITY_CEILING_INSUFFICIENT_EVIDENCE`; it cannot claim improvement.

The provisional 25%-of-available-gap threshold for an arm is met exactly when:

`4 * (M_a - M_B) >= 16 - M_B`.

No rounding is applied. In addition, all of these gates must pass:

1. model-stratum and human-stratum medians in `a` are each at least their
   corresponding baseline-stratum median;
2. the arm's median question score does not decline from baseline on protected
   questions `Q1`, `Q3`, `Q4`, `Q5`, `Q6`, or `Q7`;
3. no valid treatment response contains any critical-error code;
4. minimum sample, bundle integrity, reader isolation, and reliability gates all
   pass; and
5. no reader had access to grader-only or prior-result material.

Primary registered contrasts are:

- locator effect: `L - B`;
- state-map effect: `M - B`;
- combined effect: `LM - B`; and
- descriptive interaction: `(M_LM - M_L) - (M_M - M_B)`.

Medians, all per-reader totals, per-question vectors, stratum results, critical
errors, disagreements, exclusions, and the exact inequality operands must be
published. The interaction is descriptive at this sample size; no p-value or
independence claim is made.

## 9. Stop, contamination, and insufficient routes

Stop the affected arm before scoring if its bundle is unpinned, contains a
denied path, contains candidate/result material, permits network/write access,
or differs from its frozen manifest. Stop the affected reader if assignment,
context isolation, or prior exposure cannot be verified.

The following routes are mandatory and cannot be renamed as success:

- missing reader minimum: `VISIBILITY_INSUFFICIENT_EVIDENCE`;
- grader material visible to a reader: `VISIBILITY_CONTAMINATED`;
- treatment not frozen before candidate work: `TREATMENT_ORDER_INVALID`;
- failed reliability: `VISIBILITY_RELIABILITY_FAILED`;
- baseline ceiling: `VISIBILITY_CEILING_INSUFFICIENT_EVIDENCE`;
- missing `M` arm: `STATE_MAP_EFFECT_NOT_IDENTIFIABLE`; and
- only `B` versus `LM`: `DESCRIPTIVE_ONLY_NO_COMPONENT_ATTRIBUTION`.

No contaminated response is silently rerun. A successor version may repeat the
study with fresh readers, a new randomization commitment, and a disclosed delta.

## 10. External coordination required

- `EXTERNAL_COORDINATION_REQUIRED / 8_HUMAN_ASSIGNMENTS`: two unique humans for
  each of four arms;
- `EXTERNAL_COORDINATION_REQUIRED / 2_MODEL_LINEAGES`: two genuinely distinct
  model lineages, each supplying isolated sessions to all arms;
- `EXTERNAL_COORDINATION_REQUIRED / RANDOMIZATION_CUSTODY`: independent seed,
  salt, and assignment-table custody;
- `EXTERNAL_COORDINATION_REQUIRED / DUAL_GRADING`: two blind graders, one tie
  adjudicator, and one evidence verifier with role separation; and
- `EXTERNAL_COORDINATION_REQUIRED / IMMUTABLE_RESPONSE_STORE`: external raw
  response, access-log, and grade-freeze storage.

A single local Codex context can prepare bundles and validate syntax but cannot
satisfy lineage independence, human minimums, hidden assignment custody, or
independent grading.
