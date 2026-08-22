# 40. Owner Direction — Question Ledger and Discovery Coverage for Probe Scope

```text
STATUS = OWNER_DIRECTION / RESEARCH_METHOD_REFINEMENT
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 01:49 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "네 지금 질문들은 모아서 프루브를 어디까지 구성하면 좋을지 볼때 좋겠다 싶어요.
>
> 어때요? 더 좋은 대안이 있을까요"

## Interpretation

The questions generated during BYUL brainstorming should be preserved and later used as one input for deciding how far the empirical probe pool should be expanded.

However, the question set must not become the sole source of probe scope because it is shaped by the current BYUL worldview and current hypotheses. A discovery testbed should also capture phenomena and surprises that were not anticipated by the current question set.

## Preferred research structure

Use a linked discovery system rather than a flat benchmark list:

1. `RESEARCH_QUESTION_LEDGER`
   - preserve questions, origin/context, and status without treating them as validated requirements;
   - do not require an expected answer when the question is still exploratory.

2. `PHENOMENON / PRIOR-ART INVENTORY`
   - record real workload behaviours, native semantics, anomalies, and external systems that may expose relevant phenomena;
   - this is an exogenous source of probe ideas, not derived only from BYUL questions.

3. `EMPIRICAL_PROBE_POOL`
   - lightweight bounded probes chosen because they expose one or more useful real phenomena;
   - a probe may answer existing questions or produce entirely new ones.

4. `OBSERVATION / SURPRISE LEDGER`
   - preserve raw observed behaviour, failures, loss, ambiguity, cost, reconstruction, and unexpected outcomes;
   - surprises are first-class evidence because the current requirement set is incomplete.

5. `DISCOVERY_GAP MAP`
   - periodically connect questions ↔ observable phenomena ↔ existing probes ↔ evidence;
   - identify unexercised questions, weakly evidenced claims, and observed failure surfaces with no adequate probe;
   - use these gaps to guide research for new probes.

## Anti-confirmation-bias guard

Probe scope should be generated from at least three sources:

- endogenous BYUL questions/hypotheses;
- exogenous prior art and native workload phenomena;
- empirical surprises/gaps produced by previous probes.

Therefore:

`CURRENT_QUESTIONS != COMPLETE_TEST_REQUIREMENTS`

and

`QUESTION_COVERAGE != EMPIRICAL_COVERAGE`.

## Recommended loop

```text
BRAINSTORM / OWNER INTERVIEW / PRIOR ART
                ↓
      RESEARCH QUESTION LEDGER
                ↘
        PHENOMENON INVENTORY
                ↓
       LIGHT EMPIRICAL PROBES
                ↓
   RAW OBSERVATION + SURPRISES
                ↓
         DISCOVERY GAP MAP
          ↙             ↘
QUESTION REVISION     NEW PROBE RESEARCH
          ↘             ↙
         PROBE POOL UPDATE
                ↺
```

Only after repeated cross-probe evidence accumulates should some questions be promoted into candidate requirements or a frozen evaluation suite.

No benchmark freeze, test-completeness claim, architecture freeze, or scientific validation is created by this note.
