# MODEL S2–S4 Semantic Synchronization Report

```text
ROLE = MODEL
SCOPE = six canonical v2.0 packet documents + current work proposal only
EXTERNAL_RESEARCH = NOT PERFORMED
SOURCE_OVERWRITE = NONE
OPEN_ITEM_RESOLUTION = NONE
TECHNOLOGY_SELECTION = NONE
REPORT_STATUS = DRAFT FOR PMO / D0 AUTHORING INPUT
```

## 1. Verdict

The six-document packet is semantically coherent enough to serve as the v2.1 source baseline. No fatal contradiction requires reopening the research. The needed v2.1 work is mainly synchronization, authority/status correction, and terminology/cross-reference normalization.

Four issues should be treated as D0-blocking:

1. Some formalization-open or Pro-mode proposals are written as settled contracts or mandatory INIT capabilities.
2. `FOLD`, role assignment, and State formation are occasionally collapsed into one operation despite the confirmed guard `FOLD != VIEW != CONTROL`.
3. Candidate IDs, Probe registries, metric lists, and citation keys are not consistent across the main revision and research matrix.
4. Several questions ask again what an Owner decision already settled, while other genuinely open issues are partially pre-answered in the main document.

Recommended revision class:

```text
v2.0 -> v2.1 = SYNCHRONIZATION CANDIDATE
NEW OWNER DECISION = NONE
NEW RESEARCH CLAIM = NONE
FORMAL CALCULUS COMPLETION = NONE
```

## 2. Kernel, terminology, and status inconsistencies

| ID | Source tension | Semantic risk | Required v2.1 treatment |
|---|---|---|---|
| K-01 | Main §5 and compact summaries state `RELATION + RELATION -> RELATION`; OD-059 is only `CONFIRMED_DIRECTION`, OPEN-05 and Q-016 leave admissibility witness open. | Arbitrary pairs may appear universally composable. | Use: “**If** declared interfaces are admissible under the still-open witness contract, the composition result may again be addressed as a Relation.” Preserve closure-under-admissible-composition; do not define the witness. |
| K-02 | Main §6 gives unconditional identity equations; Q-010 leaves the View/scope under which a Relation is neutral open. | A local or View-relative no-op can be mistaken for a universal identity. | Retain Identity Relation as confirmed, but mark neutrality scope/formal law open and cross-link Q-010. |
| K-03 | Main §21 defines `EXACT` as replay of recorded input/operator/version/path; OD-021 confirms only the three-way distinction and leaves representation open; Q-092 leaves exactness level open. | Main text silently resolves byte/path/semantic exactness. | Demote the sentence to a **working example**, state that exactness levels remain open under Q-092, and avoid using it as an acceptance criterion. |
| K-04 | VIEW is described as “observational/configurational,” while Q-037/Q-038 leave pure observation and operational back-action open. | “Observational” may be read as a guarantee of no side effect. | Define VIEW as a semantic role, not a side-effect guarantee. Preserve back-action recording/separation as OPEN. Clarify that “configuration” means configuring observation/composition unless an intentional mutation is explicitly CONTROL. |
| K-05 | Main §12 pairs `VIEW:X <-> STATE:X`; OPEN-04/Q-079 leave cardinality open. | Diagrams can imply one-to-one identity. | Use occurrence-aware examples such as `apply(VIEW:X, SUBJECT, run/context) -> STATE:X@occurrence`; retain the suffix pair only as naming aid. |
| K-06 | Main §37 and changelog CHG-005 allow `FOLD(composition) -> Relation/VIEW/CONTROL/STATE handle`; confirmed rules say FOLD is only meaning-preserving omission and VIEW/CONTROL are semantic roles. | FOLD can appear to create or change a role. | State that FOLD preserves an already-declared role; it does not turn a Relation into VIEW/CONTROL/STATE. Role exposure/application and State formation are distinct from representation omission. |
| K-07 | “minimum necessary recompute” is sometimes phrased as the actual minimum impact update; Q-111/Q-114 leave dependency precision open. | An optimization goal becomes an exact minimality guarantee. | Use “design objective / minimize work using available dependency evidence, with safe fallback.” Do not claim global minimality or exact dependency capture. |
| K-08 | Main cycle outcomes add `UNKNOWN`; OD-033 confirms four outcomes: STABLE, OSCILLATING, DIVERGING, BUDGET_STOP. | An unconfirmed fifth outcome is presented in the same status block. | Either tag UNKNOWN as a Pro-mode proposed extension or leave it outside the Owner-confirmed outcome set. Do not remove the four confirmed outcomes. |
| K-09 | “Closure” means at least: composition-closure property, Datalog/fixed-point closure, and ASA local folding capability; OPEN-10 leaves the product term itself open. | Cross-document statements can appear equivalent when they are not. | Explicitly distinguish `composition closure`, `fixed-point closure`, and the working label `Closure capability (name open)`. |
| K-10 | “directional mapping” can imply deterministic function, while OD-066 explicitly allows nondeterministic/multi-valued Relation. | Kernel definition can contradict its own generality. | Add the guard: “mapping is morphism-like/directional terminology here; it is not restricted to a deterministic function.” |
| K-11 | “AI may explore” is sometimes adjacent to execution language. OD-004 permits sandbox branching; OD-005/006 require a controllable promotion gate. | Capability may be misread as standing operational authority. | Repeat `capability != authorization`; candidate execution is policy-scoped, sandboxed, and non-promoting by default unless a gate policy says otherwise. |
| K-12 | Main §51 labels 13 items “mandatory capability,” but latent-control metrics, backend replacement, toolkit operations, and some exact contracts are Pro-mode proposals or open Gate questions. | PI/research recommendations are elevated to Owner-confirmed INIT requirements. | Retitle as “Proposed INIT capability candidate set.” Tag each line by authority source, especially latent control (PI-07), backend swap (Q-174), and minimum toolkit (Q-178). |
| K-13 | Main §47 falsification criteria and §37 toolkit “contract” are written normatively; Q-175 and Q-178 still ask whether these become Owner Gates/minimum tools. | Open Gate decisions appear pre-approved. | Keep both as Pro-mode test proposals/supersets, not Owner-approved gates or minimum contracts. |
| K-14 | Main/Index say “proceed/build Candidate A after Owner review” while all front matter says no implementation authorization. | Research sequence can be read as dispatched implementation. | Use “recommended sequence if separately authorized”; explicitly state that v2.1 authoring does not authorize a prototype. |
| K-15 | `SOURCE` is a relation-local role, but “source state/source record” remains in operational prose. | Evidence origin may be confused with the kernel role. | Reserve uppercase `SOURCE/TARGET` for relation-local roles; write `Evidence/Data record`, `operational current state`, or `origin record` elsewhere. |
| K-16 | Capital `DELTA` is rejected as a primitive, while “relation-level delta” names change propagation. | A change-set can be mistaken for `VIEW:DELTA/STATE:DELTA`. | Call the runtime input a `relation change-set` or `relation-level change`; reserve `VIEW:DELTA/STATE:DELTA` for observation of difference. |
| K-17 | `EXPAND` and `RECONSTRUCT` are used as near synonyms although results range from recorded internals to inferred candidates. | Exact unfold can be conflated with inferred path generation. | Keep the current umbrella without inventing a final operator, but require every result to carry EXACT/INFERRED/UNKNOWN and note that operation/level distinctions remain open under Q-091/Q-092. |

## 3. Cross-document registry inconsistencies

### 3.1 Candidate identifiers

The main revision uses Candidate `0/1/2/3`; the research matrix and current proposal use Candidate `A/B/C/D`. Names also drift (`Delta Relation Runtime` vs `Relational Delta Runtime`). v2.1 should adopt the proposal-locked registry:

```text
A = Minimal Relation Interpreter
B = Relational Delta Runtime
C = Higher-Order Wiring / Rewrite Reference
D = Split Runtime / Reference / Search Envelope
```

This is an editorial registry synchronization, not technology selection.

### 3.2 Probe and metric registries

The main revision contains an unnumbered 17-row “common Probe” table and a shorter metric list. The matrix defines canonical `P01..P20` and a larger metric registry. The packet index claims 20 common Probes.

Recommendation: R4 owns the canonical `P01..P20` and metric registry; R1 summarizes and links to R4 rather than maintaining a second divergent list. Any retained shorter list must be labeled “executive subset,” not “the common Probe plan.”

### 3.3 Citation identifiers

`[Rxx]` is not stable across R1 and R4. For example, DBSP is `[R05]` in the main revision and `[R04]` in the matrix; the two documents also assign different works to `[R21]`. This is a real reference-integrity defect even though the underlying research claims are not being rechecked.

Recommendation: either:

- make R4 the single bibliography and have R1 cite R4 section/source anchors; or
- introduce stable semantic source keys/prefixed namespaces.

Do not renumber silently. R3 must record the reference-key migration. No new external research is needed.

### 3.4 Missing-source statement

The v2.0 documents report that a named packet was not found in earlier indexes/repositories. The current task did not re-run that search. R1/R6 should preserve this as a historical boundary:

```text
NOT PRESENT IN THE CURRENT PRIMARY SOURCE SET;
PREVIOUS v2.0 RECOVERY NOTE REPORTED IT NOT FOUND;
NOT REVERIFIED BY THIS v2.1 SYNCHRONIZATION PASS.
```

## 4. v2.1 revision delta backlog

| Priority | Delta | Class | Target |
|---|---|---|---|
| P0 | Add authority tags: OWNER-CONFIRMED, CONFIRMED-DIRECTION/OPEN-FORMALIZATION, RETAINED-SAFETY, PRO-MODE-PROPOSAL, OPEN. | status/authority | R1 |
| P0 | Qualify recursive composition by admissibility; do not resolve witness. | semantic guard alignment | R1, R3 |
| P0 | Demote exactness definition to working example; cross-link Q-091/Q-092 and OPEN-02. | status correction | R1, R3, R5 |
| P0 | Separate FOLD from role assignment and State formation. | semantic clarification to confirmed guard | R1, R3 |
| P0 | Change mandatory INIT/toolkit language to proposed candidate set/superset. | authority correction | R1, R3 |
| P0 | Preserve all 10 OPEN IDs and PI-01..07 without promotion. | status preservation | R1, R5 |
| P1 | Normalize Candidate IDs/names to A-D. | terminology/reference | R1, R3, R4 |
| P1 | Make R4 canonical for P01-P20 and metrics. | cross-reference | R1, R3, R4 |
| P1 | Repair citation-key namespace without re-research. | reference correction | R1, R3, R4 |
| P1 | Disambiguate three uses of Closure. | terminology guard | R1, R3, R4 |
| P1 | Disambiguate SOURCE role, evidence origin, runtime change-set/DELTA. | terminology guard | R1, R3, R4 |
| P1 | Mark qualitative H/VH rankings and Candidate D recommendation as inherited Pro-mode assessments, not benchmarks or selection. | status correction | R4 |
| P1 | Add question dispositions and links to OD/OPEN/PI without changing question IDs. | ledger sync | R5 |
| P2 | Qualify missing-source note as inherited/not reverified. | evidence status | R1, R3 |
| P2 | Consolidate repeated definitions and retain one compact terminology guard. | editorial | R1 |

## 5. Precise output recommendations

### R1 — Main Revision

1. Put a status legend immediately after front matter and tag each normative section.
2. Use this kernel wording:

   ```text
   [OWNER-CONFIRMED]
   RELATION r : SOURCE -> TARGET
   SOURCE/TARGET are relation-local roles; r need not be deterministic.

   [CONFIRMED DIRECTION; ADMISSIBILITY FORMALIZATION OPEN]
   When an interface/admissibility contract permits COMPOSE(r2, r1),
   its result may again be addressed as a Relation.
   The witness/typing rule remains OPEN-05 / Q-016.
   ```

3. State that FOLD preserves meaning and an already-declared role; it does not manufacture VIEW/CONTROL/STATE.
4. Present State examples with run/occurrence context and explicitly preserve OPEN-03/04.
5. Present EXACT/INFERRED/UNKNOWN as confirmed vocabulary only; keep exactness levels and attachment location open.
6. Label incremental operator signatures, toolkit operations, trigger lists, falsification criteria, and INIT capabilities as Pro-mode proposals unless mapped to an exact OD status.
7. Use Candidate A-D and refer to R4 for P01-P20, metrics, and external research details.
8. Keep the title/product name explicitly working because OPEN-10/Q-179/Q-180 remain open.
9. End with an authority summary, not an execution directive:

   ```text
   RESEARCH_BASELINE = V2.1 CANDIDATE
   OWNER_APPROVAL = PENDING
   IMPLEMENTATION_AUTHORIZATION = NONE
   TECHNOLOGY_SELECTION = NONE
   OPEN_ITEMS_RESOLVED_BY_THIS_REVISION = NONE
   ```

### R3 — Changelog

Keep two clearly separate histories:

```text
PART A = v1.0 -> proposed v2.0 foundational/breaking delta (preserved)
PART B = v2.0 -> v2.1 candidate synchronization delta
```

Part B should explicitly log at least:

- candidate `0..3 -> A..D` registry normalization;
- canonical `P01..P20` ownership moved to R4;
- citation-key namespace correction;
- authority labels added and proposal/open material de-escalated;
- admissible-composition qualifier restored;
- FOLD/role/State-formation guard clarified;
- exactness wording returned to open status;
- Closure/SOURCE/DELTA terminology disambiguated;
- missing-source statement marked inherited/not reverified;
- question disposition ledger added without resolving OPEN items.

Default classification should be `STATUS/AUTHORITY`, `REFERENCE`, `TERMINOLOGY`, or `EDITORIAL`. If any true semantic delta remains after alignment, isolate it and require Owner review; do not hide it as editorial consolidation.

### R4 — Research Matrix Sync

1. Do not re-evaluate papers or ratings in this pass.
2. Mark every H/VH/M/L rating as inherited qualitative assessment, not measured benchmark.
3. Keep A-D as candidates; replace “primary”/“most likely” where necessary with “current Pro-mode probe recommendation.”
4. Keep Candidate D as a comparative research envelope and Candidate A as proposed first probe **if separately authorized**.
5. Make P01-P20 and the metric registry canonical; repair all candidate/probe/metric cross-references.
6. Adopt a stable citation namespace and make R1 consume it.
7. Add semantic guards where research analogies can overclaim:
   - lifting/lowering is only an analogy for fold/expand;
   - category identity does not settle Q-010;
   - e-class equality is not ASA identity;
   - Datalog fixed-point closure is not ASA Closure capability;
   - DBSP supplies update machinery, not View meaning or a selected runtime.

### R5 — Open Question Sync

Default to `RETAINED_OPEN`. A question may be superseded only by a direct decision-register item, not by a Pro-mode implication or a sentence in R1.

Required columns:

```text
QUESTION_ID
PRIORITY
DISPOSITION
RELATED_OD
RELATED_OPEN_ID
RELATED_PI
V2.1_WORDING_OR_CROSSREF
NOTE
```

High-confidence disposition actions:

| Question | Recommendation | Reason |
|---|---|---|
| Q-021 | `TERMINOLOGY_UPDATE_ONLY` or retained but narrowed to runtime enforcement/witness | OD-060 already settles that lossy abstraction is VIEW, not FOLD. |
| Q-062 | `SUPERSEDED_BY_OWNER_DECISION` (OD-061), with residual law/equivalence details linked to Q-018..020 | Default order preservation is already confirmed. |
| Q-099 | `RETAINED_OPEN`, narrowed | OD-025/027 settle automatic deepening capability and some triggers; thresholds/policy remain open. |
| Q-126 | Candidate `DUPLICATE_OF_Q023` | Both ask which semantics a folded cycle declares. Preserve the H-section cross-reference. |
| Q-133 | `TERMINOLOGY_UPDATE_ONLY`, with witness linked to Q-020 | OD-060 settles FOLD vs semantic VIEW; exact witness remains open. |
| Q-138 | `RETAINED_OPEN`, narrowed | OD-005/006 settle gated and controllable promotion; the default low-risk policy remains open. |
| Q-143 | Candidate `DUPLICATE_OF_Q069` | Both ask latent Control identity across model/version. |
| Q-145 | `RETAINED_OPEN`, narrowed | OD-071 settles that human readability is not mandatory; sufficiency and safety thresholds remain open. |

Questions that must remain open because R1 currently risks pre-answering them:

```text
Q-010 identity-neutrality scope
Q-016 composition admissibility witness
Q-037/Q-038 View purity and back-action
Q-079 VIEW/STATE cardinality
Q-091/Q-092 reconstruction mode and exactness levels
Q-111/Q-114 dependency capture across folded boundaries
Q-151/Q-156 operational typing and authority identity as Owner-formalized rules
Q-175 falsification rule as Owner Gate
Q-178 minimum toolkit
Q-179/Q-180 Closure/product naming
```

Map the 10 explicit OPEN items to the 180-question ledger, but do not collapse them into one count or imply that all 180 are independent blockers. Recalculate disposition totals only after the full ledger pass; do not predeclare counts.

## 6. MODEL recommendation to PMO

```text
S2/S3 AUTHORING = GO WITH ABOVE GUARDS
NEW RESEARCH = NOT NEEDED
OWNER QUESTION = NOT NEEDED FOR SYNCHRONIZATION PASS
D0 FREEZE CONDITION = P0 BACKLOG APPLIED
MODEL SELF-CLAIM OF VALIDATION = NONE
```

The best v2.1 outcome is not a more ambitious theory. It is a cleaner authority-preserving packet in which confirmed direction, inherited safety, Pro-mode recommendation, and unresolved formalization cannot be mistaken for one another.
