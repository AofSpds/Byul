#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from transformation_contracts import (  # noqa: E402
    QueryContract,
    TransformDefinition,
    TransformationReceipt,
    TransformRegistry,
    ViewPlanner,
    preservation_satisfies,
)


class TransformationContractTests(unittest.TestCase):
    def setUp(self):
        self.first = TransformDefinition(
            transform_id="raw-to-claims",
            version="1",
            input_view="RAW",
            output_view="CLAIMS",
            preservation={"source": "ANCHORED", "conflict": "EXACT"},
        )
        self.lossy = TransformDefinition(
            transform_id="claims-to-summary",
            version="1",
            input_view="CLAIMS",
            output_view="SUMMARY",
            preservation={"source": "ANCHORED", "conflict": "NON_RECOVERABLE"},
            dependencies=("claims",),
            declared_losses=("UNSELECTED_DETAIL",),
            introduced_interpretation=("SUMMARY_SELECTION",),
            cost_class="LINEAR_INPUT",
        )
        self.registry = TransformRegistry((self.first, self.lossy))

    def test_exact_contract_finds_admissible_path(self):
        found = self.registry.find_path("RAW", "CLAIMS", {"conflict": "EXACT"})
        self.assertIsNotNone(found)
        path, preservation = found
        self.assertEqual([item.transform_id for item in path], ["raw-to-claims"])
        self.assertEqual(preservation["conflict"], "EXACT")

    def test_loss_is_monotone_and_cannot_be_recovered_by_path_search(self):
        found = self.registry.find_path("RAW", "SUMMARY", {"conflict": "EXACT"})
        self.assertIsNone(found)
        plan = ViewPlanner(self.registry, source_view="RAW").plan(
            QueryContract("show conflict", "SUMMARY", {"conflict": "EXACT"})
        )
        self.assertEqual(plan.decision_state, "REVIEW_REQUIRED")
        self.assertIn("NO_ADMISSIBLE_TRANSFORMATION_PATH", plan.notes)

    def test_anchored_and_semantic_are_not_interchangeable(self):
        self.assertFalse(preservation_satisfies("ANCHORED", "SEMANTIC"))
        self.assertFalse(preservation_satisfies("SEMANTIC", "ANCHORED"))
        self.assertTrue(preservation_satisfies("EXACT", "ANCHORED"))

    def test_unknown_fails_closed(self):
        self.assertFalse(preservation_satisfies("UNKNOWN", "UNKNOWN"))
        with self.assertRaises(ValueError):
            TransformDefinition("bad", "1", "A", "B", {"meaning": "MAGIC"})

    def test_receipt_binds_definition_inputs_outputs_parameters_and_loss(self):
        receipt = TransformationReceipt.create(
            definition=self.lossy,
            input_digest="a" * 64,
            output_digest="b" * 64,
            parameters={"limit": 5},
            validation_results={"deterministic": "PASS"},
        )
        repeated = TransformationReceipt.create(
            definition=self.lossy,
            input_digest="a" * 64,
            output_digest="b" * 64,
            parameters={"limit": 5},
            validation_results={"deterministic": "PASS"},
        )
        self.assertEqual(receipt.receipt_id, repeated.receipt_id)
        self.assertEqual(receipt.loss_manifest["conflict"], "NON_RECOVERABLE")
        self.assertEqual(receipt.dependencies, ("claims",))
        self.assertEqual(receipt.declared_losses, ("UNSELECTED_DETAIL",))
        self.assertEqual(receipt.introduced_interpretation, ("SUMMARY_SELECTION",))
        self.assertEqual(receipt.cost_class, "LINEAR_INPUT")
        self.assertEqual(len(receipt.definition_digest), 64)


if __name__ == "__main__":
    unittest.main(verbosity=2)
