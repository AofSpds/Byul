# 20. Item 2 Confirmed + Namespace Collision Requirement — 2026-08-22 20:28 KST

STATUS = OWNER_DECISION / BYUL_MIGRATION_REVIEW / NON_NORMATIVE
PROJECT = BYUL
RELATED_PROJECT = AAA / ASSET AGENT ASA

## Owner Decision — Item 2

Item 2 is confirmed.

BYUL separation is a migration of BYUL work into a separate ChatGPT Project / management / execution / memory / validation surface. AAA itself must not be modified by this migration.

AAA organization/persona/execution design is used only as a reference model for BYUL orchestration. AAA-ASA-MI and AAA-ASA-ME are temporary migration personas; after migration they remain in AAA only as backup/historical continuity and their active BYUL responsibilities succeed to new BYUL-native personas.

## Additional Owner Clarification — Namespace Collision

A separate BYUL persona namespace is also required to prevent naming collisions during new persona orchestration.

Therefore:

- current AAA persona identifiers/selectors must not be reused as BYUL current persona identifiers;
- ASA-MI / ASA-ME must not become BYUL current runtime selectors after migration;
- BYUL shall define its own canonical persona IDs and short selectors;
- historical AAA identifiers may remain in provenance/succession records only;
- runtime persona resolution must be unambiguous even when artifacts, prompts, journals, or orchestration outputs from AAA and BYUL are viewed together;
- exact BYUL role names and final organization topology remain under Item 3+ Owner review.

## AAA Firewall

This checkpoint does not authorize or perform any AAA modification.

AAA code, organization, authority, persona registry, memory, worklog, Shared Contract, release, or production state remain outside the BYUL migration mutation scope.

## Next Review

Item 3 will review the scope of the BYUL canonical namespace and collision-prevention policy before specific final persona role names are frozen.
