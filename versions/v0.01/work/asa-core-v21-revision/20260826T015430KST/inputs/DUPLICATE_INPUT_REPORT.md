# Duplicate Input Report

```text
RUN_ID = 20260826T015430KST
PRIMARY_INPUT_COUNT = 6
EXACT_TITLE_DUPLICATE_GROUPS = 5
BYTE_IDENTICAL_DUPLICATE_GROUPS = 5
CONTENT_CONFLICTS = 0
```

P2 through P6 each had two exact-title Library items: one in
`/AAA WORLD MODEL BYUL/` and one at Library root. Both copies in every group
were materialized and compared byte-for-byte. Each pair is identical and has
the same SHA-256 recorded in `INPUT_MANIFEST.tsv`.

The folder copy is canonical because it is the Owner-organized project copy.
The root copy remains preserved as a duplicate; no deletion or mutation was
performed. P1 had one exact-title item and therefore required no duplicate
disposition.

Filename-suffixed supplemental candidates such as `(1)` were not promoted
into the exact-title primary set.

