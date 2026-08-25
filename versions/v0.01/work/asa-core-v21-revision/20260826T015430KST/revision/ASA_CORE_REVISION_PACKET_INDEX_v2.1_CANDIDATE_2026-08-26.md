# ASA / BYUL — ASA Core v2.1 Candidate Revision Packet Index

```text
STATUS = V2.1_CANDIDATE / OWNER_REVIEW_PENDING / NON_FROZEN
RUN_ID = 20260826T015430KST
PACKET_DOCUMENTS = 6
HASH_MANIFEST = SHA256SUMS.txt
IMPLEMENTATION_AUTHORIZATION = NONE
TECHNOLOGY_SELECTION = NONE
PRODUCTION_AUTHORIZATION = NONE
```

## 1. 권장 읽기 순서

1. `ASA_CORE_WORLD_MODEL_PRO_MODE_REVISION_v2.1_CANDIDATE_2026-08-26.md`  
   전체 연구 protocol 후보. Owner-confirmed, confirmed-direction,
   retained-safety, Pro-mode proposal, Open 상태를 구분한다.

2. `ASA_CORE_OWNER_DECISION_CROSSWALK_v2.1_CANDIDATE_2026-08-26.md`  
   OD-001..073, OPEN-01..10, PI-01..07의 successor 위치를 보여준다.
   Exact Owner wording은 원본 decision register가 우선한다.

3. `ASA_CORE_WORLD_MODEL_v2.1_CANDIDATE_CHANGELOG_2026-08-26.md`  
   v1.0→v2.0 breaking history와 v2.0→v2.1 synchronization을 분리한다.

4. `ASA_CLOSURE_TOOLKIT_EXTERNAL_RESEARCH_MATRIX_v2.1_SYNC_2026-08-26.md`  
   Candidate A-D, canonical P01-P20, metric registry와 R4-local
   bibliography를 보존한다. 새 외부연구나 기술 선택은 없다.

5. `ASA_CORE_WORLD_MODEL_OPEN_QUESTIONS_v2.1_SYNC_2026-08-26.md`  
   Q-001..Q-180과 disposition을 보존한다. 이번 revision이 새로 답한
   질문은 0개다.

6. `SHA256SUMS.txt`  
   위 문서들의 exact byte identity를 고정한다.

## 2. 한눈에 보는 상태

| 구분 | 수량 | 상태 |
|---|---:|---|
| Owner decision/direction | 73 | mapped; exact source status preserved |
| Explicit Open register | 10 | retained Open |
| Pro-mode implications | 7 | proposal only; not promoted |
| Owner interview questions | 180 | 174 retained, 1 superseded, 2 duplicate, 3 terminology-only |
| External references | 21 per local bibliography | inherited; not re-researched |
| Hybrid candidates | 4 | A-D; none selected |
| Common probes | 20 | P01-P20 canonical in the matrix |

## 3. v2.1 synchronization highlights

- Recursive composition is limited to declared admissible interfaces; the
  witness/formal rule remains Open.
- FOLD is representation omission and does not create VIEW, CONTROL, or STATE
  roles.
- EXACT/INFERRED/UNKNOWN vocabulary is retained while exactness levels and
  attachment location remain Open.
- Candidate IDs are normalized from 0–3 to A–D.
- R4 owns the canonical P01–P20 and metric registry.
- R1 and R4 use separate `R1-Rxx` and `R4-Rxx` citation namespaces.
- Toolkit, falsification criteria, INIT capability and prototype order are
  Pro-mode proposals, not Owner-approved implementation gates.

## 4. Authority and non-finality

```text
OWNER_CONFIRMED != PRO_MODE_PROPOSAL
CONFIRMED_DIRECTION != COMPLETED_FORMALIZATION
OPEN != RESOLVED
RESEARCH_CANDIDATE != SELECTED_ARCHITECTURE
V2.1_CANDIDATE != ACTIVE / FINAL / FROZEN
CAPABILITY != AUTHORIZATION
```

## 5. Source recovery boundary

The exact six-source input manifest and duplicate comparison are stored under
`../inputs/`. The primary bytes were recovered from the Owner's project file
set. This run's Git read ledger does not contain an exact source-filename
locator result, so this packet makes no stronger claim about Git presence or
absence. The source hashes are frozen in `INPUT_MANIFEST.tsv`.

`BYUL_CLOSURE_TOOLKIT_CORE_COMBINATION_NEXT_CHANNEL_PACKET_2026-08-24.md`
remains `NOT_RECOVERED`. Its contents were not inferred. If it is later
recovered, compare only that exact source against this candidate.

## 6. Next actions

1. Owner reviews the v2.1 candidate and may accept, reject, or request revision.
2. Open formal questions continue one at a time; no mass resolution is implied.
3. Candidate A implementation is considered only under separate authorization.
4. Candidate/Probe results, if later produced, may inform a future active
   baseline or technology decision.
