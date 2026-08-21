# 11. Byul Core Principles

## Status

- OWNER_ADOPTED_WITHIN_BYUL_RESEARCH: `TRUE`
- AAA_CANONICAL_REQUIREMENT: `NO`
- SCIENTIFIC_VALIDATION: `NOT_PERFORMED`
- COUNT: `OPEN / NOT FIXED`

이 문서는 Byul/AAA-ASA-ME에서 모델·표현·라우팅·mutation을 해석할 때 사용하는 상위 원칙을 기록한다.

원칙의 개수는 고정하지 않는다. 필요하면 후속 연구에서 합치거나 나누거나 추가할 수 있다. 다만 의미 변경은 명시적으로 기록한다.

## Principle — CHANGE / MUTABILITY

어떤 상태·모델·Object·Identity·Boundary도 현실의 영구 불변 실체라고 선험적으로 가정하지 않는다.

- 현재 상태는 successor state로 변화할 수 있다.
- continuity는 단순한 `same-as`보다 succession/history/lineage로 표현될 수 있다.
- Frozen snapshot, stable ID, immutable receipt는 운영상 필요한 고정점일 수 있으나 현실 자체의 불변성을 뜻하지 않는다.

## Principle — NON-SUBSTANTIALITY / DERIVED ENTITY

Object·Self·Persona·Boundary를 반드시 primitive substance로 두지 않는다.

- 높은 scale에서 지속적으로 관측되는 pattern/view/materialization일 가능성을 열어둔다.
- stable handle과 ontological substance를 구분한다.
- 특정 formalism이 Object-first를 사용하더라도 그것을 세계의 궁극적 존재론으로 자동 승격하지 않는다.

## Principle — COMPOSITION / EMERGENCE

국소 mapping/process/interaction이 합성되어 더 큰 process·pattern·Object·Persona·Protocol view를 형성할 수 있음을 기본 가능성으로 둔다.

- local → composed → higher-scale view의 lineage를 가능한 범위에서 보존한다.
- 고수준 구조를 primitive로만 취급해 하위 구성과의 관계를 잃지 않도록 한다.
- 반대로 모든 고수준 구조가 반드시 단순한 하위 합성으로 환원된다고 단정하지 않는다.

## Principle — CONDITIONAL RELATIONALITY

상태·의미·행동·Identity는 고립된 본질보다 조건·관계·맥락에 의존할 수 있음을 기본 가능성으로 둔다.

- relation/context가 바뀌면 같은 handle의 의미나 behaviour가 달라질 수 있다.
- 관측·상호작용·환경을 World Model 밖의 특권적 meta-operation으로 자동 분리하지 않는다.
- 서로 causal하게 비교 불가능하거나 아직 분류되지 않은 관계를 억지로 단일 전역질서에 넣지 않는다.

## Application Rule

이 원칙들은 특정 formalism을 강제하지 않는다.

Causal Set, Petri Net, Event Structure, LTS, Rewrite 등 어떤 구현도 사용할 수 있다. 대신 모델 선택·변환·복원·mutation 과정에서 위 원칙과 충돌하는 가정을 암묵적으로 도입하지 않았는지 검토한다.

`P0/P1` 같은 세계관 우선순위 표기는 Byul/AAA-ASA-ME에서는 더 이상 사용하지 않는다. AAA 전체 governance의 별도 위험등급 체계는 이 문서의 대상이 아니다.

## Non-Claim

이 원칙은 물리학·철학의 진리를 증명하는 axiom이 아니다. Owner가 채택한 현재 연구·설계 원칙이며, 구현과 simulation을 통해 유용성·충돌·부작용을 계속 검증한다.

작성시각: 2026-08-22 03:08 KST
