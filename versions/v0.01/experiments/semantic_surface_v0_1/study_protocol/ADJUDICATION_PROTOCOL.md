# Adjudication Protocol v0.1

```text
PROTOCOL_ID = BYUL-ADJUDICATION-v0.1
STATUS = PROTOCOL_DESIGN_ONLY / NOT_EXECUTED
ORDER = MECHANICAL_GATE -> SANITIZE -> DUAL_BLIND_SEMANTIC -> DISAGREEMENT_FREEZE -> RELINK
MINIMUM_SEMANTIC_GRADERS = 2
DISAGREEMENT_ERASURE_ALLOWED = FALSE
IDENTITY_RELINK_BEFORE_GRADE_FREEZE = FALSE
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
```

## 1. Scope

This protocol grades a frozen public or holdout case observation without letting
candidate identity, implementation richness, cost, or narrative preference
change the semantic judgment. It does not adjudicate whether the experimental
surface is true or canonical.

Every record must validate against `schemas/adjudication.schema.json`. Schema
validity is necessary but not sufficient; cross-file ref, digest, uniqueness,
access, budget, and role-separation checks are mechanical obligations.
The record pins both `../protocol/MECHANICAL_CHECK_REGISTRY.json` and
`MECHANICAL_CHECK_BINDINGS.json` by path and SHA-256 at its exact `spec_ref`.
The binding file maps the twelve ordered adjudication checks to every mandatory
core cross-file check; an absent, changed, or uncovered check closes the gate.

## 2. Stage A — mechanical gate

The mechanical checker may see exact identities and refs. It performs no
semantic grading. For each run/case it verifies, in the frozen order:

1. experiment/spec, input, oracle, runner, harness, candidate, adapter,
   environment, dependency-lock, and resource-policy refs/digests;
2. run state and non-scoreability (`BLOCKED`, `STOPPED`, `CONTAMINATED`,
   `INVALID`, `INCOMPLETE`, or `BUDGET_EXHAUSTED` never become semantic passes);
3. candidate/adapter simultaneous-freeze and completeness-audit receipts;
4. candidate-visible input digest and absence of grader-only fields;
5. exact native-output byte locator, media type, size, and SHA-256;
6. adapter identity, mapping receipt, native-field/byte lineage, and explicit
   `UNSUPPORTED`/`UNMAPPABLE` states;
7. schema validation, cross-file unique IDs, and required observation coverage;
8. evidence locator resolution, digest equality, and capture-before-adaptation;
9. outcome/reason/artifact/reconstruction cross-field invariants;
10. resource/budget compliance and no undeclared network/service access;
11. holdout access-log and public-commitment verification when applicable; and
12. no silent retry, ref change, candidate-specific exclusion, or result leak.

The schema uses `prefixItems` to require these 12 IDs exactly once and in this
order; a duplicate, omission, reorder, or thirteenth entry is invalid. Checks
1–10 and 12 are `PASS` or `FAIL`. Check 11 may be `NOT_APPLICABLE` only for a
named public rehearsal; a claim-bearing holdout requires all 12 `PASS`.
Eligibility is mechanically derived, never operator-selected: it is true if and
only if `run_state=OBSERVED` and no mandatory check is `FAIL`. Every other run
has at least one failure/reason code, freezes non-scoreable, and receives no
sanitized packet, semantic judgment, or re-link. The checker does not repair
output or send an ineligible run to semantic graders.

## 3. Sanitized packet construction

For a mechanically eligible run, a custodian creates a byte-pinned sanitized
packet. It contains only:

- opaque case, candidate, run, and observation labels;
- the candidate-visible input exactly as run;
- the grader-only oracle and its evidence/derivation standards;
- captured native claims and evidence needed to judge them;
- the common observation and mechanical mapping-origin labels; and
- neutral runtime facts necessary to interpret the result.

It excludes or tokenizes:

- candidate and adapter IDs, names, refs, directories, filenames, and schemas
  that reveal architecture;
- builder, model, or organization identity;
- source line count, dependencies, speed, storage, human effort, and all cost
  data;
- public/holdout/control/family labels and pair polarity;
- grader discussion, previous judgments, aggregate results, and candidate order;
  and
- any result from another candidate.

Opaque labels are independently randomized per grader. The custodian freezes
the unsanitized-to-sanitized mapping and both packet digests before release. A
sanitization reviewer checks that material evidence was not removed and identity
cues were not intentionally retained. Perfect blinding may be impossible when
native output shape reveals a design; any inferred identity is recorded as a
blinding limitation, not silently ignored.

## 4. Stage B — independent blind semantic grading

`GRADER_A` and `GRADER_B` work independently. Neither may be a selector,
custodian, oracle author/reviewer, runner, builder, adapter author, mechanical
checker, or re-link controller for the same holdout.

For each case, each grader records:

- allowed-outcome-tuple match: `PASS`, `FAIL`, or `AMBIGUOUS`;
- required-condition coverage: `PASS`, `FAIL`, or `AMBIGUOUS`;
- forbidden behavior: `ABSENT`, `PRESENT`, or `AMBIGUOUS`;
- evidence sufficiency: `SUFFICIENT`, `INSUFFICIENT`, or `AMBIGUOUS`;
- conflict/unknown/loss retention as applicable;
- candidate-native versus adapted-claim faithfulness as observable in the
  sanitized packet;
- a final semantic judgment: `CONFORMING`, `NONCONFORMING`, `UNSUPPORTED`,
  `UNMAPPABLE`, `AMBIGUOUS`, or `UNSCORABLE`; and
- rationale and cited opaque evidence tokens.

A case can be `CONFORMING` only if the outcome tuple and all required conditions
pass, forbidden behavior is absent, and evidence is sufficient. `AMBIGUOUS` is
not converted to a pass. `UNSUPPORTED` and `UNMAPPABLE` are preserved as
distinct native/mapping states and are not silently converted to
`NONCONFORMING`.

Both signed judgment digests freeze before either grader sees the other's work.

## 5. Disagreement preservation and tie adjudication

Agreement means every component and final judgment is identical. All other
cases are disagreements. The schema fixes grader order as `GRADER_A` then
`GRADER_B`, enumerates equality across the five component fields and final
judgment, and requires a passing canonical-vector digest comparison. `AGREE`
cannot carry differing values; `DISAGREE` must contain at least one differing
value and cannot carry an agreed final result.

The record permanently preserves both original vectors, rationales, timestamps,
and digests. No averaging, majority shortcut, overwritten field, or informal
consensus is allowed.

A separate blind `TIE_ADJUDICATOR` receives the same sanitized packet, oracle,
and both frozen judgments in randomized A/B order. The adjudicator records an
independent diagnostic interpretation and whether the disagreement exposes an
oracle defect; it may not alter the oracle or request candidate identity/cost.
For candidate comparison and C3 triggering, any original dual-grader
disagreement remains exactly `DISAGREEMENT` and is non-orderable. The diagnostic
interpretation freezes beside, never in place of, the originals.

If disagreement reveals an oracle defect affecting every candidate, apply the
common exclusion/reserve rule from `HOLDOUT_PROTOCOL.md`. If it concerns only a
candidate's output, retain it as that candidate's adjudicated result. No case is
excluded merely because graders disagree.

## 6. Freeze and identity re-link

Before re-link, the custodian freezes:

- all mechanical records;
- every sanitized packet digest;
- both graders' original judgments;
- every tie-adjudication record;
- the final opaque case-results table;
- exclusions/replacements and minimum-balance recheck; and
- a commitment to the opaque-to-candidate mapping.

Only after that barrier may the `RELINK_CONTROLLER` join opaque labels to exact
candidate and adapter refs. The controller records mapping digest, re-link time,
actor, grade-freeze time, and pre-relink grade-freeze digest. The digest must
equal the semantic record's freeze digest, its freeze time must match, the
re-link timestamp must be strictly later, and the independent ordering check
must be `PASS`. Re-link is append-only: it cannot modify any judgment.

Cost, complexity, implementation completeness, and candidate identity are
joined only after semantic freeze. Comparison reports publish per-case vectors,
mechanical failures, disagreements, cost vectors, and uncertainty. They do not
substitute one aggregate score or a post-hoc narrative weighting.

## 7. Mandatory failure routes

| Condition | Route |
| --- | --- |
| Mandatory mechanical check fails | `MECHANICAL_INVALID / NON_SCOREABLE` |
| Holdout access or oracle separation fails | `HOLDOUT_CONTAMINATED / INSUFFICIENT_EVIDENCE` |
| Only one semantic grader exists | `ADJUDICATION_INSUFFICIENT_EVIDENCE` |
| Grader identity blindness is broken before freeze | `SEMANTIC_GRADE_CONTAMINATED` |
| Original graders disagree | Preserve `DISAGREEMENT`; non-orderable and no C3 trigger |
| Re-link occurs before grade freeze | `ADJUDICATION_ORDER_INVALID` |
| Candidate-specific case exclusion | `COMPARISON_INVALID` |
| Minimum common case balance fails after exclusions | `INSUFFICIENT_EVIDENCE` |

Failed runs and partial records remain evidence. They are not silently rerun,
repaired, dropped, or scored as zero/pass. A new ref after exposure belongs to a
successor experiment with a fresh holdout.

The schema also binds final state: non-observed run states retain their state;
an observed mechanical failure is `MECHANICAL_INVALID`; an agreed or disagreed
semantic result maps to its exact final state; and a common exclusion requires a
non-`NONE` common reason, all-candidate application, and a pre-frozen reserve.
The false exclusion tuple is exactly `NONE / false / null`. Cross-document
digest arithmetic, reason-set equality, and strict timestamp ordering follow
`CROSS_FILE_INTEGRITY.md`; they are required mechanical evidence because JSON
Schema alone cannot prove them.

## 8. External coordination required

- `EXTERNAL_COORDINATION_REQUIRED / ROLE_SEPARATION`: mechanical checker,
  custodian/sanitizer, sanitization reviewer, two graders, tie adjudicator, and
  re-link controller;
- `EXTERNAL_COORDINATION_REQUIRED / BLIND_PACKET_DELIVERY`: graders must receive
  packets without filesystem or metadata paths that reveal candidate identity;
- `EXTERNAL_COORDINATION_REQUIRED / IMMUTABLE_GRADE_STORE`: independent freeze
  of both original judgments before discussion; and
- `EXTERNAL_COORDINATION_REQUIRED / HOLDOUT_KEY_RELEASE`: grader-only oracle
  release only after native observations freeze.

A single shared local context cannot demonstrate these independence and custody
conditions. It may only test schema syntax and mechanical examples on dummy
artifacts in a later, separately authorized engineering phase.
