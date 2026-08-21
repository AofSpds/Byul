# Metadata

- BASELINE_COMMIT: `8133e3d79c88b582bea6b8a45bc8a1970b261734`
- WORKTREE: `byul-baseline` / detached snapshot
- READ_CONSTRAINT: context-blind; repository snapshot only; `byul-execution` not inspected during the cold read
- MODEL_LINEAGE_LIMITATION: same-model-lineage analysis; not statistically independent expert replication
- VALIDATION_BOUNDARY: evidence report only; not independent validation

---

# Cold-read evidence report

Scope: inspected only `/workspace/scratch/9831a5d04d00/byul-baseline`. I did not inspect `byul-execution`, edit files, run tests, or run Git writes.

## Read-path finding

The apparent default path is:

`README.md` → `versions/v0.01/CURRENT_STATUS.md` → `versions/v0.01/memory/11_CORE_PRINCIPLES.md` → `versions/v0.01/README.md` → memory `00~11`.

That path is stale. `README.md` and `CURRENT_STATUS.md` do not point to memory `13~17`, while the latest in-tree checkpoint, `versions/v0.01/memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`, explicitly warns that `CURRENT_STATUS.md` may lag and supplies a corrected read order. A literal first reader can therefore miss the latest authority, execution-safety, convergence, and non-selection corrections.

## 1. What is authoritative?

The repository defines several scoped kinds of authority:

- For v0.1 provenance, the primary evidence is the raw `versions/v0.01/memory/*.md` corpus. The declared order is raw memory → derived view/index → routing recommendation → reconstruction/summary. This is provenance authority, not a claim that memory contents are externally true. Evidence: `versions/v0.1/data/SOURCE_MANIFEST.md`, sections “Primary Corpus” and “Data Authority Rule”; `versions/v0.1/MODEL_CONTRACT.md`, sections “DATA” and “RAW_CORPUS”.
- Authority is scoped to what a record captured, not automatically external reality. Evidence: `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`, “STRONG CONVERGENCE OBSERVED”.
- For persisted artifact identity, the corrected canonical comparison is committed Git-blob content, not checkout bytes. Evidence: `versions/v0.01/memory/15_ROUND1_CLEAN_RERUN_EOL_HASH_GATE_CORRECTION.md`, “Correct Canonical Identity Rule”.
- `BYUL CORE-A` is Owner-adopted guidance within Byul research, but is neither an AAA canonical requirement nor scientific truth. Evidence: `versions/v0.01/memory/11_CORE_PRINCIPLES.md`, “Status” and “Non-Claim”; `README.md`, “Governance Note”.
- `MODEL_CONTRACT.md` is authoritative only as the implementation contract for the current experimental slice. It explicitly does not replace AAA canonical Requirement/Design.
- The latest apparent continuation record is `versions/v0.01/memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`, but it remains `NON_NORMATIVE / NOT_VALIDATED`.

Implementation caveat: `versions/v0.1/src/byul_v01.py` declares baseline commit `2a4529...` but reads the current filesystem glob without verifying that Git commit. At this snapshot it can ingest later memory while still stamping the old commit. The latest checkpoint explicitly identifies “filesystem rather than enforced Git-object source pinning” as a material weakness.

Confidence: high on declared authority ordering; medium-high on which file should be treated as the current continuation locator because the official locator is stale.

## 2. What is derived?

Declared derived representations are:

- `HISTORY_ORDER_INDEX`
- `CURRENT_STATE_VIEW`
- `OPEN_QUESTION_VIEW`
- `MODEL_FAMILY_VIEW`
- `LIFECYCLE_VIEW`
- `CORE_PRINCIPLES_VIEW`
- routing recommendations / `RoutePlan`
- reconstructions and summaries

Evidence: `versions/v0.1/MODEL_CONTRACT.md`, “Derived Representations”; `versions/v0.1/data/SOURCE_MANIFEST.md`, “Data Authority Rule”.

The later convergence checkpoint generalizes this: current/history/open/search/causal/Petri/Event/LTS/simulation representations should default to rebuildable, provenance-bearing projections unless later evidence grants them scoped authority. Evidence: `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`.

Actual code is narrower and heuristic:

- Views use hard-coded file dependencies in `versions/v0.1/src/byul_v01.py`, `VIEW_DEPENDENCIES`.
- “Current” and “open” filtering is keyword-based.
- Later memory `12~17` is ingested into raw atoms but omitted from `CURRENT_STATE_VIEW`, `OPEN_QUESTION_VIEW`, and `LIFECYCLE_VIEW` dependencies.
- The in-memory “raw” representation is not byte-exact: blank lines are omitted, lines are stripped, and content digests normalize whitespace.

Confidence: high.

## 3. What happens on loss?

Intended research discipline:

- Loss must be classified as `EXACT`, `ANCHORED`, `SEMANTIC`, `STATISTICAL`, `VIEW_DEPENDENT`, `NON_RECOVERABLE`, or `UNKNOWN`. Evidence: `versions/v0.1/MODEL_CONTRACT.md`, “Reconstruction / Preservation Classes”.
- Discarded transformation semantics are not recoverable. Lossy reverse synthesis must not be relabeled as recovered ground truth. Evidence: `versions/v0.01/memory/02_CAUSAL_SET_LEARNING.md`, “Reconstruction”; `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`.
- Transformations should produce explicit preservation/loss contracts and receipts, and semantic admissibility should precede cost/ranking. This is a surviving design invariant, not yet an implemented mechanism. Evidence: memory `16` and `17`.
- Material source changes should not overwrite the old baseline; they create an exact successor target and results from different targets must not be mixed. Evidence: `versions/v0.1/data/SOURCE_MANIFEST.md`, “Future Data Mutation”.
- Current virtual mutation recovery simply discards the virtual mutation and restores the source snapshot. Evidence: `versions/v0.1/src/byul_v01.py`, `simulate_virtual_mutation()`.
- For lost conversational context, the documented fallback is `versions/v0.00/context/AAA-ASA-ME_CONTEXT_BACKUP_2026-08-22.md`. Evidence: `README.md`, “Succession Rule”; memory `17`, “Immediate Recovery Locators”.

Implementation gap: v0.1 has no transformation receipts, semantic-equivalence checker, or general “requested preservation cannot be met, therefore refuse” mechanism. It mostly preserves vocabulary and normalized digests.

Confidence: medium-high on intended behavior; high that it is not currently enforced.

## 4. What happens on unresolved conflict?

The intended semantic behavior is preservation, not silent resolution:

- Explicit conflicts and lineage should survive correction, branch/split, merge, migration, recovery, and succession.
- Incomparable causal relations must not be silently total-ordered.
- `UNKNOWN`, `OPEN`, and non-conclusions remain valid states.
- Evaluation can return `TRADEOFF`, `COMPLEMENTARY`, or `INSUFFICIENT_EVIDENCE`; minority proposals are preserved rather than erased by consensus.

Evidence:

- `versions/v0.01/memory/17_CHANNEL_SUCCESSION_CHECKPOINT_2026-08-22_0700_KST.md`, “Current Byul Research State”, “Anti-Confirmation-Bias Correction”, and “Research Method Discipline”.
- `versions/v0.01/experiments/round1/ROUND1_EVALUATION_PACKET.md`, “Pairwise Review” and “Diversity Preservation”.

For Git execution, an actual content conflict must not be resolved arbitrarily; the run reports `PUSH_BLOCKED / REVIEW_REQUIRED`. Evidence: `versions/v0.1/runs/LOCAL_CODEX_PUSH_POLICY.md`, “Push Retry”.

Implementation gap: the v0.1 executable has no conflict object, merge semantics, or conflict-retaining lifecycle state. A `conflict` routing intent is unrecognized and merely falls back to `REVIEW_REQUIRED`.

Confidence: medium-high on policy; high that the implementation lacks it.

## 5. What is invariant versus candidate?

Narrow surviving methodological invariants are explicitly listed in memory `17`:

- source/derived authority separation;
- visible loss and provenance;
- conflict preservation;
- `UNKNOWN` as a normal state;
- semantic admissibility before cost;
- explicit lifecycle/succession.

Additional experiment invariants include pinned baselines, immutable Phase-1 freeze artifacts, lineage-preserving successor targets, and non-reused run IDs.

`BYUL CORE-A` supplies current Owner-adopted constraints—mutability, non-substantiality/derived entity, composition/emergence, conditional relationality—but even its count is open and semantic changes may be explicitly recorded. It is not an immutable ontology or scientific axiom. Evidence: `versions/v0.01/memory/11_CORE_PRINCIPLES.md`.

Still candidates or open:

- the worldview phrase “무수한 국소 사상들의 합성망”;
- primitive/minimal algebra;
- Causal Set, Petri/Open/Reconfigurable Petri, Occurrence Net, Event Structure, causal-order and LTS roles;
- one-model versus multi-model routing;
- `R(S,M,L)` and the exact Situation Fingerprint;
- Preservation Demand as the dominant routing axis;
- minimal ledger versus richer ledger versus hardened Git+Markdown;
- fixed planes/kernels, `P=(F,E,R,D)`, `PLAN(Q,K,P,L,B)`, deterministic split/merge identity, and single-plane semantic ownership.

Evidence: memory `17`, especially “Formalism Position” and “Anti-Confirmation-Bias Correction”; memory `16`, “MOST IMPORTANT DIVERGENCE”.

Confidence: high.

## 6. When is execution refused?

There are three distinct behaviors:

1. Research-controller hard stop: a worker must fail closed if it cannot verify isolated worktree ownership, exact baseline reads, Phase-1 remote freeze, or report push. Evidence: `versions/v0.01/memory/14_ROUND1_RERUN_SAFETY_CORRECTION.md`, “Failure Closed”.

2. Implementation authorization boundary: `KEEP/MODIFY/REPLACE/HYBRID/REFRAME` is advisory only. Generic `execute` authorizes the research packet, not implementation. A separate explicit implementation-trial authorization is required. Evidence: memory `13`, “Interpretation”; memory `14`, “Core correction”; memory `17`, “Next-Channel Operating Direction”.

3. Current router behavior:
   - unknown intent → `REVIEW_REQUIRED`;
   - exact metric without an authoritative metric/clock source → `REVIEW_REQUIRED`;
   - supplied unknown fields → `REVIEW_REQUIRED`;
   - Core-A always remains `REVIEW_REQUIRED`;
   - invalid preservation enum → `ValueError`.

Evidence: `versions/v0.1/src/byul_v01.py`, `SituationFingerprint.validate()` and `Router.route()`; `versions/v0.1/tests/test_byul_v01.py`.

Important distinction: `REVIEW_REQUIRED` is not a true execution refusal in current CLI code; it returns a route plan normally. A general semantic-loss/refusal gate is only a proposed next experiment, not implemented authoritative behavior.

Confidence: high on controller and authorization rules; medium on the broader semantic refusal question because the repository has not selected or implemented such a gate.

## 7. What remains unselected or unvalidated?

Unselected:

- any universal/canonical World Model;
- final architecture;
- primitive/minimal algebra;
- exact planner signature;
- ledger versus Git+Markdown control;
- rich ledger extensions;
- Petri/Event/Causal/LTS authority roles beyond candidate views;
- `R(S,M,L)` as a canonical planner;
- deterministic identity semantics after split/merge;
- any v0.2 successor;
- any Round-1 implementation recommendation.

Unvalidated/unapproved:

- v0.1 as a World Model;
- Core-A scientifically;
- Owner acceptance;
- independent validation;
- production authorization;
- preservation proof or semantic equivalence;
- same-model convergence as independent replication.

Evidence: `README.md`; `versions/v0.1/README.md`; `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`; memory `17`.

At the 06:00 checkpoint, R07’s final Phase-2 completion was still pending after the EOL gate defect. The local snapshot contains no individual clean-run result directories, so the claimed convergence cannot be independently audited from this working tree alone. The detailed program document mentioned by memory `17` is explicitly excluded from the checkpoint.

Confidence: high on non-selection/non-validation; medium on the underlying Round-1 evidence because only its summaries are present.

## 8. What could falsify the leading candidates?

| Candidate | Discriminating evidence | Falsifying result |
|---|---|---|
| C2 minimal Artifact + append-only Ledger | Blind reconstruction, lifecycle torture, semantic-loss/refusal, invalidation accuracy, merge/conflict retention, recovery, total complexity/cost | Hardened Git+Markdown C1 matches fidelity and lifecycle behavior at materially lower complexity, or C2 still loses provenance/conflicts |
| C1 hardened Git+Markdown | Same suite against C2/C3 | Cannot represent explicit lineage, heads, conflict retention, or deterministic recovery without recreating ledger complexity |
| Current v0.1/C0 | Enforced Git-object pinning, byte-exact round trip, current-view freshness, real lifecycle transitions, sound invalidation | Failure on exactness, later-correction visibility, conflict/lifecycle behavior, or semantic-loss refusal shows it is inadequate beyond scaffold value |
| `R(S,M,L)` / Preservation Demand | Feature ablation across T1–T10, unknown-heavy cases, planner accuracy/cost comparisons | Axes are redundant or insufficient, a simpler `Plan(Q,P,A)` performs as well, or fingerprint construction costs exceed routing benefit |
| Multi-model Petri/Event/Causal/LTS family | Transformation probes, preservation drift, size blow-up, query gain, maintenance cost versus simpler controls | A single/reduced representation matches required queries and lifecycle behavior without conversion loss/cost |
| Round-1 convergence | Different model families, independent human experts, less leading prompts, adversarial reframing | Convergence disappears or tracks prompt wording/model lineage rather than task evidence |
| Rich ledger/TMS/CRDT extensions | Add only after C2 fails targeted reconstruction/conflict/lifecycle cases | Minimal core passes those cases; richer machinery adds cost without measurable benefit |

Primary evidence: `versions/v0.01/memory/16_ROUND1_CLEAN_RERUN_CONVERGENCE_CHECKPOINT.md`, “CURRENT ASA INTERPRETATION” and “LIMITATIONS”; `versions/v0.01/memory/05_SIMULATION_AND_COMMITTEE.md`; `versions/v0.01/memory/10_ACTIVE_CHANNEL_LOG.md`, “Immediate Validation Questions”; memory `17`, “Research Method Discipline”.

The repository names test categories but does not yet define quantitative acceptance thresholds, so falsification is designed but not operationally complete.

Confidence: medium-high.

## Cold-read discoverability scores

Scale: 0 = effectively absent, 1 = discoverable only by synthesis/corrections, 2 = explicit on the apparent path.

| Question | Score | Reason |
|---|---:|---|
| 1. Authority | 2 | Explicit in root README, manifest, and contract; scoped-authority nuance is later |
| 2. Derived | 2 | Named directly in the contract and code |
| 3. Loss | 1 | Taxonomy is clear, actual response/enforcement is scattered and incomplete |
| 4. Conflict | 1 | Latest checkpoint and push/evaluation policies are clear, but not on the root path or implemented |
| 5. Invariant vs candidate | 1 | Memory `17` answers this directly, but the default locator does not lead there |
| 6. Refusal | 1 | Requires combining safety correction, push policy, authorization incident, and router code |
| 7. Unselected/unvalidated | 2 | Repeated prominently across README/status/checkpoints |
| 8. Falsification | 1 | Test categories are explicit in memory `16`, but thresholds/protocol remain open |

Total: **11/16**.

## Likely cold-reader misreadings

- Treating `CURRENT_STATUS.md` as current and never reading memory `13~17`.
- Treating the v0.1 baseline commit constant as enforced, although the code reads a live filesystem glob.
- Treating `RAW_CORPUS` or the round-trip digest as byte-exact; whitespace and blank lines are normalized/lost.
- Assuming later corrections appear in `CURRENT_STATE_VIEW`; its dependencies stop at selected files through memory `11`.
- Reading “lowest authority layer” in memory `16` as “least authoritative,” despite the manifest’s raw-over-derived ordering; it means foundational substrate.
- Treating `ROUTE_CANDIDATE` as model approval or an executable transformation.
- Treating `REVIEW_REQUIRED` as a hard runtime refusal.
- Treating strong cross-run convergence as Owner selection, scientific validation, or independent expert replication.
- Treating a test pass as preservation proof, production approval, or implementation authorization.
- Treating the minimal ledger as already implemented in the baseline.
- Treating stale `P-series` language in memory `00`, `04`, `06`, `07`, or `08` as canonical; memory `10`, Core-A, and the contract explicitly correct/remove it.
- Treating Petri, Causal Set, `R(S,M,L)`, or the worldview phrase as selected ontology.
- Treating unresolved conflict as something the current executable can merge; it cannot.
- Treating run numbers as ranks, generations, or successor versions.
- Treating a recommendation or generic `execute` as authority to mutate shared implementation.
- Assuming all ten clean runs completed and are present locally; the checkpoint says R07 was pending, and the working tree contains no run artifacts.

Overall confidence: **high** for the repository’s declared posture and current implementation gaps; **medium** for claims about Round-1 proposal contents because only checkpoint summaries, not the exact run branches/artifacts, are present in this snapshot.
