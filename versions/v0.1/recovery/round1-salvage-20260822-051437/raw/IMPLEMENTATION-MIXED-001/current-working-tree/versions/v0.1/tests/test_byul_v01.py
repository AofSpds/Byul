#!/usr/bin/env python3
import base64
import json
import subprocess
import sys
import tempfile
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


EXPECTED_BASELINE_FILES = {
    "00_CHANNEL_AND_METHOD.md",
    "01_OWNER_WORLDVIEW_CURRENT.md",
    "02_CAUSAL_SET_LEARNING.md",
    "03_MODEL_FAMILY_AND_COMPLEMENTARITY.md",
    "04_ROUTING_AND_LIFECYCLE.md",
    "05_SIMULATION_AND_COMMITTEE.md",
    "06_MI1_INITIALIZATION_TARGET.md",
    "07_OPEN_QUESTIONS_AND_NEXT_JOBS.md",
    "08_CHANNEL_CHRONOLOGY.md",
    "09_VERSION_POLICY.md",
    "10_ACTIVE_CHANNEL_LOG.md",
    "11_CORE_PRINCIPLES.md",
}


class ByulV01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = MemoryCorpus.load()

    def test_loads_only_exact_manifest_git_tree(self):
        state = self.corpus.model_state()
        self.assertEqual(state.document_count, 12)
        self.assertEqual(set(self.corpus.documents), EXPECTED_BASELINE_FILES)
        self.assertNotIn("12_PARALLEL_PROPOSAL_ROUND1.md", self.corpus.documents)
        self.assertEqual(state.source_mode, "EXACT_GIT_TREE")
        self.assertTrue(state.exact_baseline_verified)
        self.assertEqual(len(state.content_digest), 64)
        self.assertIsNotNone(state.manifest_digest)

    def test_manifest_sha_and_git_blob_are_verified(self):
        for document in self.corpus.documents.values():
            self.assertEqual(len(document.raw_sha256), 64)
            self.assertIsNotNone(document.git_blob_oid)
            self.assertEqual(len(document.git_blob_oid), 40)

    def test_core_principles_view_exists(self):
        atoms = self.corpus.view("CORE_PRINCIPLES_VIEW")
        self.assertGreater(len(atoms), 0)
        self.assertTrue(any("CHANGE / MUTABILITY" in atom.text for atom in atoms))
        self.assertTrue(any("CONDITIONAL RELATIONALITY" in atom.text for atom in atoms))

    def test_snapshot_roundtrip_is_byte_exact(self):
        snapshot = self.corpus.snapshot()
        encoded = json.dumps(snapshot, ensure_ascii=False)
        decoded = json.loads(encoded)
        restored = MemoryCorpus.from_snapshot(decoded)
        self.assertEqual(self.corpus.content_digest(), restored.content_digest())
        self.assertEqual(
            self.corpus.content_digest(),
            MemoryCorpus.snapshot_content_digest(decoded),
        )
        for name, document in self.corpus.documents.items():
            self.assertEqual(document.raw_bytes, restored.documents[name].raw_bytes)

    def test_snapshot_detects_raw_byte_tampering(self):
        snapshot = self.corpus.snapshot()
        source = sorted(snapshot["documents"])[0]
        raw = base64.b64decode(snapshot["documents"][source]["raw_base64"])
        snapshot["documents"][source]["raw_base64"] = base64.b64encode(raw + b" ").decode("ascii")
        with self.assertRaisesRegex(ValueError, "raw digest mismatch"):
            MemoryCorpus.from_snapshot(snapshot)

    def test_snapshot_rejects_derived_atoms_that_disagree_with_raw_bytes(self):
        snapshot = self.corpus.snapshot()
        source = sorted(snapshot["documents"])[0]
        snapshot["documents"][source]["atoms"][0]["text"] = "tampered derived text"
        with self.assertRaisesRegex(ValueError, "derived atoms differ"):
            MemoryCorpus.from_snapshot(snapshot)

    def test_restore_source_bytes_matches_every_digest(self):
        with tempfile.TemporaryDirectory() as temporary:
            written = self.corpus.restore_source_bytes(Path(temporary))
            self.assertEqual(set(written), EXPECTED_BASELINE_FILES)
            for name, digest in written.items():
                self.assertEqual(digest, self.corpus.documents[name].raw_sha256)

    def test_worktree_mode_is_explicitly_unverified(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "memo.md").write_bytes(b"# memo\nOPEN\n")
            corpus = MemoryCorpus.load(root=root, source_mode="worktree")
            self.assertFalse(corpus.model_state().exact_baseline_verified)
            plan = Router().route(
                SituationFingerprint(intent="raw"),
                corpus.model_state(),
                LifecycleContext(phase="operate"),
            )
            self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
            self.assertTrue(any("exact_baseline" in item for item in plan.unmet_demands))

    def test_byte_offsets_anchor_exact_atom_text(self):
        document = self.corpus.documents["11_CORE_PRINCIPLES.md"]
        atom = next(item for item in document.atoms if "CHANGE / MUTABILITY" in item.text)
        anchored = document.raw_bytes[atom.byte_start : atom.byte_end].decode("utf-8")
        self.assertEqual(anchored, atom.text)

    def test_chronology_index_is_acyclic(self):
        self.assertGreater(len(self.corpus.history_items()), 10)
        self.assertTrue(self.corpus.history_is_acyclic())

    def test_known_history_route_enforces_exact_contract(self):
        plan = Router().route(
            SituationFingerprint(intent="history", preservation={"history": "EXACT"}),
            self.corpus.model_state(),
            LifecycleContext(phase="initialize"),
        )
        self.assertEqual(plan.decision_state, "ROUTE_CANDIDATE")
        self.assertIn("HISTORY_ORDER_INDEX", plan.target_views)
        self.assertIn("chronology-index-v1", plan.transform_contracts)
        self.assertEqual(plan.principle_gate_state, "REVIEW_REQUIRED")
        self.assertIn("EXACT_BASELINE_MANIFEST_CHECK", plan.required_validations)

    def test_unmet_semantic_demand_fails_closed(self):
        plan = Router().route(
            SituationFingerprint(
                intent="history",
                preservation={"conflict": "EXACT", "resource": "EXACT"},
            ),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertTrue(any(item.startswith("conflict:EXACT") for item in plan.unmet_demands))
        self.assertTrue(any(item.startswith("resource:EXACT") for item in plan.unmet_demands))

    def test_unknown_intent_fails_to_review_required(self):
        plan = Router().route(
            SituationFingerprint(intent="invent_a_world_model"),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertIn("RAW_CORPUS", plan.target_views)
        self.assertEqual(plan.transform_contracts, [])

    def test_exact_metric_requires_external_source(self):
        plan = Router().route(
            SituationFingerprint(intent="history", require_exact_metric=True),
            self.corpus.model_state(),
            LifecycleContext(phase="operate"),
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertIn("EXTERNAL_METRIC_SOURCE_REQUIRED", plan.required_validations)
        self.assertTrue(any(item.startswith("metric:EXACT") for item in plan.unmet_demands))

    def test_lifecycle_route_adds_byte_lineage_and_loss_checks(self):
        plan = Router().route(
            SituationFingerprint(intent="current_state"),
            self.corpus.model_state(),
            LifecycleContext(phase="merge", rollback_required=True),
        )
        self.assertIn("LIFECYCLE_VIEW", plan.target_views)
        self.assertIn("ROUND_TRIP_BYTE_CHECK", plan.required_validations)
        self.assertIn("DEPENDENCY_INVALIDATION_CHECK", plan.required_validations)
        self.assertIn("LOSS_RECEIPT_CHECK", plan.required_validations)
        self.assertIn("ROLLBACK_OR_COMPENSATION_PLAN", plan.required_validations)

    def test_view_materialization_emits_derivation_receipt(self):
        atoms, receipt = self.corpus.materialize_view("OPEN_QUESTION_VIEW")
        self.assertGreater(len(atoms), 0)
        self.assertEqual(receipt.source_digest, self.corpus.content_digest())
        self.assertEqual(len(receipt.target_digest), 64)
        self.assertEqual(len(receipt.view_definition_digest), 64)
        self.assertEqual(receipt.validation_result, "CONTRACT_CHECKED")
        self.assertIn("UNSELECTED_SOURCE_LINES", receipt.losses)
        self.assertGreater(len(receipt.dependencies), 0)
        self.assertIn("OPEN_QUESTION_VIEW_SELECTION_POLICY", receipt.introduced_interpretation)
        self.assertEqual(receipt.cost_class, "LINEAR_IN_DEPENDENT_SOURCE_ATOMS")

    def test_virtual_mutation_changes_exact_digest_and_tracks_dependency_closure(self):
        result = self.corpus.simulate_virtual_mutation("10_ACTIVE_CHANNEL_LOG.md")
        self.assertNotEqual(result["before_digest"], result["after_digest"])
        self.assertNotEqual(result["before_raw_sha256"], result["after_raw_sha256"])
        self.assertGreater(result["invalidation_radius"], 0)
        self.assertLessEqual(result["invalidation_radius"], 1)
        self.assertIn("CURRENT_STATE_VIEW", result["dependency_closure"])

    def test_invalid_preservation_level_rejected(self):
        with self.assertRaises(ValueError):
            Router().route(
                SituationFingerprint(intent="history", preservation={"history": "PERFECT_MAGIC"}),
                self.corpus.model_state(),
                LifecycleContext(phase="operate"),
            )

    def test_cli_export_verify_import_and_ledger_initialization(self):
        script = SRC / "byul_v01.py"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            snapshot = root / "snapshot.json"
            exported = subprocess.run(
                [sys.executable, "-B", str(script), "export", "--out", str(snapshot)],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )
            self.assertTrue(json.loads(exported.stdout)["byte_exact"])
            verified = subprocess.run(
                [sys.executable, "-B", str(script), "verify-import", "--input", str(snapshot)],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )
            self.assertTrue(json.loads(verified.stdout)["verified"])

            ledger_root = root / "ledger"
            initialized = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(script),
                    "ledger-init",
                    "--root",
                    str(ledger_root),
                    "--branch",
                    "main",
                ],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )
            value = json.loads(initialized.stdout)
            self.assertEqual(value["event_count"], 12)
            self.assertEqual(len(value["commit_id"]), 64)


if __name__ == "__main__":
    unittest.main(verbosity=2)
