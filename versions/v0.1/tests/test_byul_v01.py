#!/usr/bin/env python3
import json
import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from byul_v01 import (  # noqa: E402
    LifecycleContext,
    MemoryCorpus,
    Router,
    SituationFingerprint,
)


class ByulV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = MemoryCorpus.load()

    def test_loads_v001_memory_corpus(self):
        state = self.corpus.model_state()
        self.assertGreaterEqual(state.document_count, 12)
        self.assertGreater(state.atom_count, 100)
        self.assertEqual(len(state.content_digest), 64)

    def test_core_principles_view_exists(self):
        atoms = self.corpus.view("CORE_PRINCIPLES_VIEW")
        self.assertGreater(len(atoms), 0)
        self.assertTrue(any("CHANGE / MUTABILITY" in a.text for a in atoms))
        self.assertTrue(any("CONDITIONAL RELATIONALITY" in a.text for a in atoms))

    def test_raw_snapshot_roundtrip_content_digest(self):
        snapshot = self.corpus.snapshot()
        encoded = json.dumps(snapshot, ensure_ascii=False)
        decoded = json.loads(encoded)
        self.assertEqual(
            self.corpus.content_digest(),
            MemoryCorpus.snapshot_content_digest(decoded),
        )

    def test_chronology_index_is_acyclic(self):
        self.assertGreater(len(self.corpus.history_items()), 10)
        self.assertTrue(self.corpus.history_is_acyclic())

    def test_known_history_route(self):
        plan = Router().route(
            SituationFingerprint(intent="history", preservation={"history": "EXACT"}),
            self.corpus.model_state(),
            LifecycleContext(phase="initialize"),
        )
        self.assertEqual(plan.decision_state, "ROUTE_CANDIDATE")
        self.assertIn("HISTORY_ORDER_INDEX", plan.target_views)
        self.assertEqual(plan.principle_gate_state, "REVIEW_REQUIRED")
        self.assertIn("CORE_PRINCIPLE_REVIEW", plan.required_validations)

    def test_principles_route(self):
        plan = Router().route(
            SituationFingerprint(intent="principles"),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertIn("CORE_PRINCIPLES_VIEW", plan.target_views)
        self.assertEqual(plan.principle_gate_state, "REVIEW_REQUIRED")

    def test_unknown_intent_fails_to_review_required(self):
        plan = Router().route(
            SituationFingerprint(intent="invent_a_world_model"),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertIn("RAW_CORPUS", plan.target_views)

    def test_exact_metric_requires_external_source(self):
        plan = Router().route(
            SituationFingerprint(intent="history", require_exact_metric=True),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertIn("EXTERNAL_METRIC_SOURCE_REQUIRED", plan.required_validations)

    def test_lifecycle_mutation_route_adds_preservation_checks(self):
        plan = Router().route(
            SituationFingerprint(intent="current_state"),
            self.corpus.model_state(),
            LifecycleContext(phase="mutate"),
        )
        self.assertIn("LIFECYCLE_VIEW", plan.target_views)
        self.assertIn("ROUND_TRIP_CONTENT_CHECK", plan.required_validations)
        self.assertIn("INVALIDATION_RADIUS_CHECK", plan.required_validations)

    def test_virtual_mutation_changes_digest_and_tracks_invalidation(self):
        result = self.corpus.simulate_virtual_mutation("10_ACTIVE_CHANNEL_LOG.md")
        self.assertNotEqual(result["before_digest"], result["after_digest"])
        self.assertGreater(result["invalidation_radius"], 0)
        self.assertLessEqual(result["invalidation_radius"], 1)
        self.assertIn("CURRENT_STATE_VIEW", result["affected_views"])

    def test_invalid_preservation_level_rejected(self):
        with self.assertRaises(ValueError):
            Router().route(
                SituationFingerprint(intent="history", preservation={"history": "PERFECT_MAGIC"}),
                self.corpus.model_state(),
                LifecycleContext(phase="operate"),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
