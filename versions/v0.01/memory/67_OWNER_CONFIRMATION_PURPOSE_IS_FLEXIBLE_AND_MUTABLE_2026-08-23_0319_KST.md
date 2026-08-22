# 67. Owner confirmation — Purpose is flexible and may change when the current purpose does not work

```text
STATUS = OWNER_WORLDVIEW_ORAL_STATEMENT / CONFIRMATION / INTERVIEW_MEMORY
PROJECT = BYUL
CHANNEL_WORKSTREAM = ASA-MI
TIME_KST = 2026-08-23 03:19 KST
IMPLEMENTATION_AUTHORIZED = FALSE
VALIDATION_CLAIM = NONE
```

## Owner statement

> "목적도 어느 정도 유연하지요. 뭐 잘 안되면 바꿔야죠 뭐 ㅋㅋ"

## Referent being answered

The immediately preceding unresolved boundary asked whether `Purpose P` should remain an externally fixed condition for one modeling episode while Model/View/Requirement/Evaluation Relation mutate, or whether Purpose itself may also change in response to empirical failure/surprise.

## High-fidelity interpretation

The Owner confirms that Purpose is **not absolutely fixed**.

Current research framing therefore becomes:

- Model `M` is mutable;
- View / abstraction `V` is mutable;
- Requirement-performance bundle `Q` is mutable;
- Evaluation/relation configuration `R` is mutable;
- Purpose `P` is also eligible for revision when the current purpose is not working or is no longer useful.

Conceptually:

```text
F0 = {Purpose P0, View V0, Requirement Bundle Q0, Relation/Evaluation R0, Evidence E}
Model M0
        |
        v
empirical observation / failure / surprise
        |
        +--> revise M
        +--> revise V
        +--> revise Q
        +--> revise R
        +--> revise P when justified
```

The phrase `어느 정도 유연` is important. It should **not** be expanded into the stronger claim that Purpose is freely or constantly mutable, or that every failed probe should cause a purpose change.

A more accurate current status is:

`PURPOSE_MUTABLE = YES / BOUNDED_FLEXIBILITY`

not:

`PURPOSE_ALWAYS_MUTATES = TRUE`

and not:

`PURPOSE_IS_ARBITRARY = TRUE`.

## Experiment-history guard

If Purpose changes after a probe, preserve the prior purpose and result rather than retroactively rewriting the historical evaluation frame.

For example:

```text
Episode/Frame F0 under P0 -> FAIL
P0 revised to P1 for stated reason
Successor Episode/Frame F1 under P1 -> new evaluation
```

The original `FAIL under F0/P0` remains part of the research history.

## Research implication

The Model-Discovery Testbed is therefore allowed to discover not only:

- which model fits a purpose;
- which view/resolution fits a purpose;
- which requirements/evaluation relation fit a purpose;

but, when evidence warrants it, also that **the currently declared purpose itself should be revised or succeeded**.

This strengthens the co-adaptive discovery framing without implying unrestricted relativism.

## Immediate next unresolved axis

Now that `P/M/V/Q/R` are all mutable research objects, a useful next question is **what constrains a legitimate change**.

In particular, when a failed result appears, how should the research distinguish:

- justified learning/reframing;
- convenient goalpost moving that merely escapes a failure?

This should be asked without presuming one privileged universal criterion, because the Owner has already established that evaluation and comparison are View/relation-conditioned.

No canonical mutation rule, episode boundary, stopping rule, or testbed implementation is fixed by this note.
