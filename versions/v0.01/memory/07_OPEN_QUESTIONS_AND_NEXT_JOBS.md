# 07. Open Questions & Next Jobs

COPIED_FROM: `versions/v0.00/memory/07_OPEN_QUESTIONS_AND_NEXT_JOBS.md`

## Open Questions
- Primitive / minimal algebra: Event / Local Mapping / Interaction / Composition / Rewrite 중 무엇을 최소 문법으로 볼지.
- Transformation Semantics: 무엇을 lossless로 보존해야 하는지.
- Model Family Compatibility: forward/reverse translation 조건·손실·비유일성.
- Situation Fingerprint: routing에 필요한 최소 feature set.
- `R(S,M,L)`: 충분한가, 추가 인자가 필요한가.
- P-series Gate: canonical semantics를 훼손하지 않고 routing/mutation 결과를 어떻게 검증할지.
- Lifecycle Drift: 누적 semantic drift 정의/계측.
- Reconstruction Reliability: EXACT/ANCHORED/STATISTICAL/VIEW-DEPENDENT/NON-RECOVERABLE acceptance.
- Canonical vs Multi-authoritative Representation.
- Scale: link/reachability/unfolding explosion 및 incremental materialization.
- Model Mutation: Reconfigurable Petri/graph rewrite 적합성.
- Committee Scenario Quality: coverage/bias/realism 검증.

## Next Jobs — Current Priority
1. v0.01 active research memory 운영 및 승계 안정화.
2. MI-1 initialization/reconstruction 시험 구조 확정.
3. 위원회 외주용 `Lifecycle + Routing Simulation Challenge Requirements` 작성.
4. blind/model-attack/coverage-gap scenario corpus 설계.
5. lifecycle benchmark acceptance metrics 정교화.
6. v0.1 구현 전 exact implementation target 결정.

## Version Boundary
- v0.00/v0.01~v0.0x: 연구·메모·검증설계.
- v0.1+: 실제 모델 구현.

## Do Not Prematurely Decide
- Petri canonical model
- Causal Set final architecture
- one universal model
- one canonical representation
- Event/local mapping primitive
- discarded semantics 자동 복원

작성시각: 2026-08-22 02:37 KST
