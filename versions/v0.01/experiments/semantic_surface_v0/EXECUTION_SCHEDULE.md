# Byul Semantic Surface / Candidate Competition Execution Schedule v0

## Authority and boundary

- TRACK: `BYUL / AAA-ASA-ME`
- OPERATING_ROLE: `ASA-ME`
- BASELINE: `AofSpds/Byul@8133e3d79c88b582bea6b8a45bc8a1970b261734`
- STATUS: `WORKING / NON_NORMATIVE / NOT_VALIDATED`
- SELECTION_AUTHORITY: `NONE`
- PRODUCTION_AUTHORIZED: `FALSE`
- DEFAULT_ATTACKABLE: `TRUE`

This schedule executes a research experiment. It does not define Byul, select an
architecture, validate a model, or authorize a merge to `main`.

## Global controls

- Preserve the baseline commit in a detached read-only worktree for all
  pre-change measurements.
- Make all changes on `asa-me/research-surface-conformance-v0.1`.
- Do not move, rewrite, or duplicate the existing memory corpus.
- Use canonical committed Git-blob bytes for persisted-artifact equality.
- Freeze scenario selection, expected C0 behavior, metrics, and stop rules before
  reading C1/C2 trial results.
- Keep public development scenarios separate from an undisclosed holdout set.
- Count same-model-lineage reviewers as correlated evidence, not independent
  expert replication.
- A test pass is implementation evidence only.

## Detailed schedule

| Step | Purpose | Exact input | Actor / model | Dependency | Isolation | Output | Entry gate | Exit gate | Failure route | Contamination risk | Compute budget | Stop rule | Next route |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S0 | Measure the original repository's first-read legibility | Detached `8133e3d...`; eight cold-read questions | Context-blind model reviewer; later human/different-lineage reviewers | None | Read-only detached worktree; no project-memory prompt | Baseline answers, evidence paths, confidence, 0–2 rubric scores | Baseline commit and tree verified | Raw response frozen before repository edits are disclosed | Mark `BASELINE_INVALID` and rerun with a fresh reviewer | Prior project context; opening non-default files; learning proposed answers | 20–40 min per reviewer | Stop a reviewer on any evidence of prior context | S1 and S2 may proceed after at least one frozen baseline; independent replications remain open |
| S1 | Remove locator drift without changing model semantics | Root `README.md`; `CURRENT_STATUS.md`; memory 16–17; v0.1 README | Documentation worker | S0 baseline frozen | Feature branch only; additive locators | Current entry path; v0.1 labeled C0 experimental baseline | Exact baseline confirmed | No active locator says Round-1 is unstarted; latest checkpoint reachable within two links | Revert only S1 files and record unresolved drift | Rewriting history; moving paths; turning summary into new authority | 20–40 min | Stop if a locator conflict cannot be resolved from exact Git evidence | S2/S3 |
| S2 | Expose claim status without canonizing a solution | Memory 11, 15, 16, 17 and exact source refs | Research-state worker | S0 | Feature branch; one machine-readable index | `BYUL_RESEARCH_STATE.yaml` | Taxonomy and authority boundary declared | Every entry has classification, evidence, counterevidence/falsifier, promotion and demotion routes | Leave item `OPEN` or omit it; never infer a stronger status | Manifest becoming canonical truth; manual drift | 30–60 min | Stop on unsupported `INVARIANT`, `REJECTED`, or selected architecture claim | S3 |
| S3 | Pre-register candidate-neutral attacks and controls | Real incidents in memory 13–17; current code/test behavior | Scenario/spec worker | S0; may run parallel with S1/S2 | Spec-only paths; no candidate result access | Scenario schema; observation schema; eight public scenarios; positive controls; holdout rules; C0–C3 charters | Candidate-neutral vocabulary and exact evidence available | JSON/schema validation; no ledger/plane/API required; always-refuse and always-conflict candidates cannot trivially pass | Reject or rewrite the affected scenario before any candidate run | Designing tests around desired winner; post-hoc scenario choice | 45–90 min | Freeze before observing C1/C2 results | S4 |
| S4 | Attack, delete, or reorder the execution plan | This schedule; frozen S0–S3 artifacts | Fresh adversarial schedule reviewer using high reasoning | S0–S3 drafts | Reviewer receives no candidate result | `SCHEDULE_REVIEW.md` with ACCEPT / MODIFY / CANCEL and mandatory corrections | Inputs frozen and candidate code not begun | All blocking corrections resolved or Owner explicitly accepts residual risk | Cancel candidate implementation and preserve preparation artifacts | Reviewer anchoring to proposed architecture; embellishment-only review | 30–60 min | Any unresolved leakage, non-neutral metric, missing negative control, or unbounded scope blocks S5 | S5 only on ACCEPT or corrected ACCEPT_WITH_CHANGES |
| S5 | Build a candidate-neutral observation harness | Frozen scenario/observation schemas and charters | Engineering worker | S4 gate pass | Harness code separate from candidate-native code | Loader, schema checks, adapter boundary, evidence-rich result writer | Scenario freeze digest recorded | Harness can wrap C0 and dummy positive/negative controls without internal ontology assumptions | Modify harness/spec before real candidates; invalidate prior dry-run results | Hidden solution assumptions in pass/fail mapping | 45–90 min | Stop if common schema discards candidate-native evidence or UNKNOWN | S6 |
| S6 | Implement isolated comparison candidates | C0 exact baseline; frozen C1/C2 charters | Separate candidate workers where possible | S5 | Candidate-specific directories/worktrees; no cross-reading before freeze | C0 adapter; C1 hardened Git+Markdown trial; C2 minimal content-addressed ledger trial | Exact charters and permitted dependencies frozen | Candidate-native tests pass; commit and source digest recorded; no `main` mutation | Mark candidate `BLOCKED` or `INCOMPLETE`; do not relax scenario after observing failure | Cross-candidate copying; overfitting to public cases; richer candidate receiving more effort | 2–4 h total, parallelizable | Time/LOC/dependency cap exceeded; unplanned semantic expansion; implementation needs a new ontology | S7 or return to S3 with a new experiment version |
| S7 | Compare behavior, ablations, and cost | Frozen candidates; public scenarios; hidden holdout when available | Evaluation runner plus blind reviewer | S6 | Results-only directory; candidate order randomized for qualitative review | Per-scenario observations, failures, loss/conflict/UNKNOWN retention, refusal accuracy, LOC/runtime/dependency measures | All compared commits pinned | Public and holdout results separated; raw observations retained; no aggregate score hides gate failures | Declare `INSUFFICIENT_EVIDENCE`; do not select a winner | Outcome-aware rubric changes; tuning on holdout; same-lineage convergence | 1–2 h plus holdout reviewer time | Stop selection if holdout leakage, schema mismatch, or unequal material effort is found | S8 |
| S8 | Measure whether the new repository surface actually reads better | Original detached baseline and changed commit; same questionnaire | Fresh blind reviewers, preferably different model families and humans | S1–S3 frozen; changed commit pinned | Randomized A/B labels; no project explanation | Pre/post comprehension matrix with exact-repository citations | Reviewer has not seen proposal or rubric answer key | Reports what remains unselected, authority boundaries, refusal/loss/conflict behavior, and falsifiers without treating candidates as canon | Preserve failure; return to S1–S3 rather than adding explanatory prose blindly | Prompt leakage; using only the builders as reviewers | 30–90 min per cohort | Stop claims of improvement without at least one uncontaminated comparison | S9 |
| S9 | Preserve evidence without selecting or releasing | All exact commits, frozen specs, raw results, review | ASA-ME synthesis; Owner decides next route | S7 and S8 | Draft PR; no auto-merge | Evidence index, limitations, open questions, draft PR | Clean status, tests recorded, diff reviewed | PR explicitly says non-normative/not validated/production unauthorized and separates preparation from results | Keep PR draft or close without merge; retain exact evidence refs | Treating PR/test success as architecture approval | 30–60 min | No merge, v0.2 promotion, or production claim without separate Owner decision | Owner chooses further research, candidate revision, external validation, or no change |

## Estimated duration

- Preparation and safety gates (S0–S4): about **2–4 wall-clock hours** with
  parallel workers.
- Automated harness and initial candidate trials (S5–S7): about **3–6
  wall-clock hours**, depending on corrections from S4.
- Credible multi-family/human cold-read and holdout evaluation (S8): typically
  **half a day to one day** because reviewer isolation, not computation, is the
  limiting factor.
- The complete cycle is therefore expected to take **5–10 compute hours** and
  **roughly half a day to one day of elapsed time**. A same-lineage internal
  rehearsal can finish sooner but is not independent validation.

## Current execution gate

`S0–S3 AUTHORIZED / S4 REQUIRED BEFORE CANDIDATE IMPLEMENTATION / S5–S9 CONDITIONALLY AUTHORIZED BY THIS OWNER REQUEST / MAIN MERGE NOT AUTHORIZED`
