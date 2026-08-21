# Owner Trial Authorization — Semantic Surface v0

## Record

- RECORDED_AT: `2026-08-22 07:42 KST`
- OWNER_MESSAGE: `네 모두 실행하는데 시간 오래 걸릴까요? 뭐하면 코드 X 돌려도 됩니다. 충전했어요.`
- INTERPRETATION: `EXPLICIT_RESEARCH_AND_IMPLEMENTATION_TRIAL_AUTHORIZATION`
- STATUS: `ACTIVE_FOR_THIS_EXPERIMENT / NON_PRODUCTION`

## Authorized scope

- execute S0–S9 in `EXECUTION_SCHEDULE.md`, subject to its entry, exit, failure,
  contamination, and stop gates;
- use Codex workers for isolated research, schedule review, harness work, and
  C0/C1/C2 implementation trials;
- create commits on `asa-me/research-surface-conformance-v0.1` and publish a
  draft pull request for review;
- run C3 only if its pre-registered C2 failure gate is actually crossed.

## Not authorized

- direct writes or merge to `main`;
- production deployment or production-use claims;
- Owner Acceptance, independent validation, scientific proof, or canonical
  architecture/model selection;
- rewriting or moving the existing research memory corpus;
- relaxing a frozen scenario, metric, or stop rule after observing a candidate
  result.

This record narrows the meaning of the Owner message to the experiment already
described immediately before it. It does not convert a broad conversational
`execute` into open-ended repository authority.
