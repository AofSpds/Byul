#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "src" / "byul_v01.py"
REPO_ROOT = Path(__file__).resolve().parents[3]


class ByulCliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> dict:
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), *args],
            cwd=REPO_ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        return json.loads(result.stdout)

    def test_summary_and_materialize_documented_commands(self):
        summary = self.run_cli("summary")
        self.assertEqual(summary["source_mode"], "EXACT_GIT_TREE")
        self.assertTrue(summary["exact_baseline_verified"])
        materialized = self.run_cli(
            "materialize-view", "--name", "OPEN_QUESTION_VIEW"
        )
        self.assertEqual(materialized["receipt"]["validation_result"], "CONTRACT_CHECKED")

    def test_export_and_verify_import_round_trip(self):
        with tempfile.TemporaryDirectory() as temporary:
            snapshot = Path(temporary) / "snapshot.json"
            exported = self.run_cli("export", "--out", str(snapshot))
            imported = self.run_cli("verify-import", "--input", str(snapshot))
            self.assertTrue(exported["byte_exact"])
            self.assertTrue(imported["verified"])
            self.assertEqual(exported["content_digest"], imported["content_digest"])

    def test_documented_ledger_commands_persist_and_recover(self):
        with tempfile.TemporaryDirectory() as temporary:
            ledger_root = Path(temporary) / "ledger"
            initialized = self.run_cli(
                "ledger-init", "--repo", str(ledger_root), "--branch", "main"
            )
            claimed = self.run_cli(
                "ledger-claim",
                "--repo",
                str(ledger_root),
                "--branch",
                "main",
                "--claim-id",
                "q1",
                "--text",
                "Primitive remains open",
                "--class",
                "OPEN",
                "--actor",
                "owner",
            )
            split = self.run_cli(
                "ledger-split",
                "--repo",
                str(ledger_root),
                "--source",
                "main",
                "--target",
                "alternative",
            )
            recovered = self.run_cli(
                "ledger-recover", "--repo", str(ledger_root), "--branch", "alternative"
            )
            self.assertGreater(initialized["event_count"], 0)
            self.assertEqual(claimed["claim_id"], "q1")
            self.assertEqual(split["operation"], "SPLIT")
            self.assertEqual(recovered["state"], "RECOVERED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
