# Owner Direction — Inherit AAA Organization & Operating Principles, Adapt for BYUL

STATUS = OWNER_DIRECTION / CURRENT
PROJECT = BYUL
CURRENT_MIGRATION_PERSONA = ASA-MI
TIME_KST = 2026-08-23 06:56 KST

## Owner decision

- AAA의 조직도와 운영원칙은 BYUL로 계승한다.
- 단, BYUL이 AAA 조직을 동일한 Persona 수, 역할명, domain split, topology로 그대로 복제할 필요는 없다.
- 따라서 이관은 `COPY`가 아니라 `INHERIT_PRINCIPLES_AND_ADAPT_TO_BYUL`로 해석한다.
- 이전 Owner correction에 따라 CORE A / CORE B 상위 구분은 BYUL에서 사용하지 않는다.

## Migration interpretation

기본적으로 보존할 AAA organizational/operating patterns:
- Owner-facing planning/design surface와 execution command surface의 분리
- 주요 authoring/execution 역할과 paired validator의 분리
- paired validator와 organization-external independent validator/auditor의 분리
- Owner reserved authority와 routine execution의 분리
- Persona를 지속 조직 정체성으로 보고 실제 task execution surface와 구분하는 원칙
- cross-functional workstream / bounded work packet 운용
- execution completion / paired validation / Owner review / closure state 분리
- self-validation 및 same-act material edit+PASS 방지 원칙

BYUL에서 재설계할 항목:
- 정확한 Persona inventory와 최소 Persona 수
- Persona 명칭과 selector
- CTL/MOD/RES/ENG 기능을 독립 Persona로 유지할지, 결합/분할/신설할지
- Planning/PMO 및 각 specialist 역할의 정확한 scope와 authority
- validator granularity와 conditional independent-audit trigger
- 실제 Channel/Thread/Worktree/runtime topology
- memory/succession routing 세부

## Consequence for Owner interview

더 이상 `AAA 조직/운영원칙을 계승할 것인가?`를 질문하지 않는다.
앞으로는 `AAA 원칙을 BYUL 특성에 맞게 어떤 형태로 변형할 것인가?`만 질문한다.

TESTBED discussion remains out of current priority. Persona organization migration planning is current priority.

AAA_MUTATION_AUTHORIZED = FALSE
IMPLEMENTATION_AUTHORIZED = FALSE
