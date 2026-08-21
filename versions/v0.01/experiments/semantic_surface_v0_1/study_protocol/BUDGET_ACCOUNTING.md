# Budget Accounting v0.1

```text
BUDGET_ID = BYUL-SEMANTIC-SURFACE-v0.1-HARD-CEILING
STATUS = PRE_REGISTERED_LIMITS / NOT_CONSUMED
BUDGETS_FUNGIBLE_ACROSS_UNITS = FALSE
HARD_TOTAL_WALL_WINDOW = 168 elapsed hours
HARD_TOTAL_WORKER_TIME = 72 worker-hours
HARD_TOTAL_MODEL_INPUT = 5,000,000 tokens
HARD_TOTAL_MODEL_OUTPUT = 1,300,000 tokens
HARD_TOTAL_MODEL_CALLS = 180 calls
HARD_TOTAL_TOOL_CALLS = 2,000 calls
HARD_TOTAL_HUMAN_TIME = 40 person-hours
EXHAUSTION_ROUTE = BUDGET_EXHAUSTED / INSUFFICIENT_EVIDENCE
```

## 1. Unit definitions

The units are recorded separately and may not offset one another.

| Unit | Definition | Clock start/stop |
| --- | --- | --- |
| Wall elapsed | Real time for the authorized experiment window, including waits for external roles | First post-freeze action to final V3/F9 evidence freeze; maximum 168 hours |
| Worker time | Sum of active controller, research, engineering, runner, and grading-worker time across parallel workers | Actor begins task-specific work to its output freeze; waiting without active work excluded |
| Model input | Provider-reported input, cached-input, and context tokens; cached tokens are reported separately but count toward the cap | Every model call in the experiment |
| Model output | Provider-reported reasoning/output tokens when exposed; otherwise provider total output unit | Every model call in the experiment |
| Model calls | One provider request, including failed/retried calls | Request submitted; retries each count |
| Tool calls | One shell, Git, schema, filesystem, browser/network, or external-store invocation; batched suboperations count as one invocation plus disclosed suboperation count | Invocation submitted; failed calls count |
| Human time | Sum of active reader, selector, custodian, reviewer, grader, auditor, and Owner-decision time | Human starts task-specific activity to handoff; passive scheduling wait excluded |

Unknown is not zero. If trustworthy usage cannot be obtained for a hard-capped
unit, the affected step is `BUDGET_ACCOUNTING_UNVERIFIED` and cannot enter a
comparative claim.

## 2. Step ceilings

The following are maxima, not targets. `Model in/out` is expressed in thousands
of tokens. The allocated sums remain below the hard total to leave a small
failure-recording reserve; unused allocation cannot be transferred without a
new pre-result authorization applied symmetrically.

| Step | Wall | Worker | Model in/out | Model calls | Tool calls | Human |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| V0 | 2 h | 2 h | 80k / 20k | 4 | 30 | 1 h |
| V1 | 3 h | 4 h | 160k / 40k | 8 | 80 | 1 h |
| V2 | 24 h | 4 h | 960k / 240k | 16 | 120 | 6 h |
| V3 | 8 h | 5 h | 400k / 100k | 16 | 80 | 8 h |
| F0 | 1 h | 1 h | 40k / 10k | 2 | 20 | 0.5 h |
| F1 | 2 h | 3 h | 160k / 40k | 6 | 60 | 1 h |
| F2 | 3 h | 4 h | 240k / 60k | 8 | 100 | 1 h |
| F3 | 4 h | 5 h | 320k / 80k | 10 | 120 | 1 h |
| F4 | 24 h | 3 h | 120k / 30k | 4 | 50 | 4 h |
| F5 | 2 h | 3 h | 120k / 30k | 4 | 60 | 1 h |
| F6 | 4 h | 6 h | 320k / 80k | 10 | 180 | 1 h |
| F7 | 8 h | 10 h | 1,160k / 280k | 56 | 560 | 2 h |
| F8 | 4 h | 6 h | 200k / 50k | 6 | 200 | 1 h |
| F9 | 8 h | 5 h | 320k / 80k | 10 | 100 | 6 h |
| F10 | 2 h | 2 h | 80k / 20k | 3 | 30 | 1 h |
| Allocated total | Parallel; governed by 168 h window | 63 h | 4,680k / 1,160k | 163 | 1,790 | 35.5 h |
| Unallocated recording reserve | N/A | 9 h | 320k / 140k | 17 | 210 | 4.5 h |

The sum of per-step wall ceilings is not the experiment wall ceiling because
independent tracks and actors may run in parallel. Every step still has its own
elapsed cap, and the whole experiment must finish within 168 elapsed hours.

## 3. Symmetric candidate budget

Within F7, the canonical candidate-build sub-budget is
`../candidate_protocol/BUILD_BUDGET.yaml`. C1 and C2 each receive exactly:

- 3 elapsed hours from clean packet delivery to ref freeze;
- 3 active worker-hours including candidate-native code, tests, and mechanical
  adapter;
- 500,000 model-input tokens and 120,000 model-output tokens;
- 24 model calls;
- 240 tool calls;
- one clean non-inherited context, isolated repository/container, and identical
  CPU/memory/disk/network policy; and
- two result-blind repair rounds on dummy-only feedback, each already included
  in the caps above.

The remaining F7 allocation—4 worker-hours, 160,000 input tokens, 40,000 output
tokens, eight model calls, and 80 tool calls—is controller/auditor overhead. It
may not be transferred to a candidate build.

C0 receives no prospective build budget and is labeled
`ARCHIVAL_CALIBRATION_ONLY`. If a maintained C0M is later authorized, it is a new
prospective candidate and must receive exactly the C1/C2 budget; it cannot reuse
the archival label or hidden prior work.

Candidate completeness is judged against the frozen charter before any real
public/holdout run. Failure to finish within budget is
`INCOMPLETE_UNDER_BUDGET`, not a semantic failure. No candidate receives extra
effort after another candidate result or holdout input is visible.

## 4. Visibility reader and grader accounting

Each model-reader session receives at most:

- 20 elapsed minutes;
- one fresh context;
- 50,000 input tokens and 12,500 output tokens;
- two model calls, including any retry; and
- 20 read-only tool calls.

Each human-reader session receives 20 elapsed minutes plus five minutes for
metadata. Graders and tie adjudicators record active minutes separately. Human
scheduling delay consumes wall elapsed but not person-hours.

## 5. Tool and inherited-service accounting

Every invocation log records actor, step, timestamp, tool class, command or
operation digest, success/failure, and declared suboperation count. Git, shell,
filesystem, schema validators, external ACL storage, and provider services are
not treated as free capabilities. For candidate cost comparison, disclose
inherited Git/object-store/runtime services separately from candidate-specific
code and adapter logic.

Batching may reduce invocation count but does not erase suboperation disclosure.
Manual edits or calculations count as worker/human time even when no tool call is
made.

## 6. Exhaustion, retries, and partial evidence

- Crossing any per-step or hard-total ceiling stops the affected work
  immediately.
- A failed model/tool request counts; its retry also counts.
- Budget remaining in another unit or candidate cannot pay the overrun.
- Partial files, logs, refs, native outputs, and stop reasons freeze before any
  further work.
- The result is `BUDGET_EXHAUSTED / INSUFFICIENT_EVIDENCE`, not candidate
  inferiority and not permission to relax the cap.
- A successor budget requires a new version, disclosed delta, fresh candidate
  contexts, and fresh holdout if any real holdout input was exposed.

The three-hour worker, token/call, tool, and human reserves may only record
failures, verify digests, close access, and publish stop receipts. They may not
complete or repair an over-budget candidate.

## 7. External coordination required

- `EXTERNAL_COORDINATION_REQUIRED / PROVIDER_METERING`: provider-level model
  lineage, input/output token, cache, and call records;
- `EXTERNAL_COORDINATION_REQUIRED / HUMAN_TIMESHEETS`: reader, selector,
  custodian, reviewer, grader, and auditor active-time logs;
- `EXTERNAL_COORDINATION_REQUIRED / WALL_CLOCK_CONTROLLER`: one authoritative
  experiment window and synchronized timestamps; and
- `EXTERNAL_COORDINATION_REQUIRED / RESOURCE_ENFORCEMENT`: per-container CPU,
  memory, disk, timeout, and network controls for future candidate execution.

Local shell timing alone cannot establish model-provider usage, independent
human time, or external-store cost.
