# Holdout Selection and Handling Rules

```text
STATUS = PROVISIONAL / RULES_ONLY
HOLDOUT_CONTENT_PRESENT = FALSE
HIDDEN_ANSWERS_PRESENT = FALSE
VALIDATION_CLAIM = NONE
SELECTION_AUTHORITY = NONE
```

This directory intentionally contains no holdout inputs, expected outcomes, or
answer keys.

## Selection rules

1. An independent selector who did not author candidate implementations selects
   cases after public scenarios and candidate charters are frozen but before
   candidate refs/adapters are revealed to graders.
2. Each case must derive from an exact Git-pinned Byul incident, a disclosed
   minimal transformation of one, or a lifecycle combination of such incidents.
3. Record repository, commit, path, Git blob, extraction range, transformation,
   and any introduced loss in a private holdout manifest.
4. Do not copy or rewrite an authoritative corpus as a second semantic source.
   Fixtures reference exact sources and disclose extraction/derivation.
5. Balance at least four failure families: authority/conflict, preservation/loss,
   lifecycle/identity, and reconstruction/invalidation.
6. Include both refusal-required and execution-required cases, plus both
   unresolved and resolvable cases.
7. Avoid cases whose expected behavior requires a fixed ledger, five-plane
   structure, API method set, planner signature, or deterministic identity rule.
8. Freeze inputs and adjudication notes by content digest before candidate access.
9. Give every candidate identical inputs, resource limits, and observation
   requirements.
10. Do not tune adapters or candidates after holdout exposure. Any defect is
    reported against the frozen ref.

## Access and contamination rules

- Candidate authors and adapter authors may not access holdout material before
  their exact commits are frozen.
- Graders receive candidate-neutral observations in randomized order and remain
  blind to candidate identity until judgments are frozen.
- Any leak, answer-key exposure, case-specific patch, or ref change contaminates
  the affected run. Record and exclude it; do not silently regenerate a more
  favorable holdout.
- Holdout results must disclose case counts and category balance. Inputs may be
  released after the experiment if doing so does not compromise a successor
  holdout.

## Interpretation boundary

Holdout success is comparative research evidence only. It grants no validation,
selection, implementation, merge, release, freeze, or production authority.
