# F5-D exact-ref dummy transport gate review

```text
MANIFEST_COMMIT = 865f0892fe668e76c7c21822ff9474809b99520d
SOURCE_COMMIT = 78a1a992a2cfecea337a8610112b6dbaa0a7e127
REVIEW_SCOPE = F3-D / F5-D / PRE-CODE DUMMY TRANSPORT ONLY
VERDICT = DUMMY_TRANSPORT_CANCEL
REVIEW_CLASS = SAME_MODEL_LINEAGE / CORRELATED_INTERNAL_EVIDENCE
VALIDATION_CLAIM = NONE
```

## Freeze verification

The manifest/source parent relation, source parent, subtree tree, file count,
and all 67 path/mode/Git-blob/raw-SHA-256/byte-length tuples matched exactly.
No harness implementation, candidate implementation, or holdout plaintext was
present.

## Blocking findings

1. The grader oracle contains native emission, adapter projection, forced run
   state, expected disposition, and reason codes. The runner is told it may
   materialize artifacts from those keys, so it cannot execute without reading
   answer-bearing oracle bytes or inventing an unfrozen driver.
2. No separately frozen actual-side dummy envelope exists: no runner-readable
   driver/control inputs, run-manifest bindings, native-capture source, mapping
   source, state-event evidence, or observation materialization input.
3. `STOPPED` and `CONTAMINATED` are oracle-forced labels rather than independent
   controller events with evidence. A future implementation would have to
   synthesize the event from the expected answer.
4. The wrong-ref vector lacks one frozen correct binding baseline and omits the
   runner/dependency-lock tokens later made mandatory.
5. `XF_TRUNC_001` is mandatory but no truncated-output profile exists. The
   candidate adapter audit requires `INVALID`, while the cross-file contract
   also names `INCOMPLETE`, `BUDGET_EXHAUSTED`, or `STOPPED`; the route is not
   uniquely frozen.
6. Trial execution authority resolves/null-checks a ref but is not mechanically
   bound to exact `HARNESS_DUMMY`, exact F5-D scope, exact reviewed source, and
   the F5-D verdict. Schedule prose alone does not prevent scope reuse.

## Required correction route

- freeze actual-side driver/controller data separately from grader oracles;
- make execution possible without oracle bytes or case/profile hard-coding;
- add evidence-bearing stopped, contaminated, truncated, and wrong-ref vectors;
- include complete correct bindings, including runner and dependency lock;
- choose one non-scoreable truncation route; and
- bind F5-D authority to exact dummy scope and reviewed refs.

This verdict does not require F3-C, a holdout, candidates, humans, or semantic
graders. It creates no validation, selection, merge, release, or production
authority.
