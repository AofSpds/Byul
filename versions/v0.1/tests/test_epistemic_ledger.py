#!/usr/bin/env python3
import json
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from epistemic_ledger import (  # noqa: E402
    ClaimPacket,
    ContextRecord,
    EpistemicLedger,
    JustificationRecord,
    LifecycleRepository,
    SourceAnchor,
)


FIXED_TIMES = [f"2026-08-22T00:00:{second:02d}Z" for second in range(40)]


class EpistemicLedgerTests(unittest.TestCase):
    def test_generic_events_still_enforce_typed_payload_contracts(self):
        ledger = EpistemicLedger()
        with self.assertRaisesRegex(ValueError, "missing required fields"):
            ledger.append("CORRECT", "owner", {"claim_id": "claim-a"}, FIXED_TIMES[0])
        with self.assertRaisesRegex(ValueError, "unsupported epistemic class"):
            ledger.append(
                "CLASSIFY",
                "owner",
                {"claim_id": "claim-a", "epistemic_class": "CERTAIN_MAGIC"},
                FIXED_TIMES[1],
            )

    def test_typed_records_roundtrip_and_preserve_bitemporal_fields(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "ledger.jsonl"
            ledger = EpistemicLedger.load(path)
            anchor = SourceAnchor(
                source_path="memory.md",
                source_sha256="a" * 64,
                byte_start=10,
                byte_end=25,
            )
            context = ContextRecord(
                context_id="context-a",
                description="Assumption environment A",
                actor="owner",
                assumptions=("no-global-now",),
                valid_time="2026-08-21",
            )
            context_event = ledger.append_context(context, transaction_time=FIXED_TIMES[0])
            claim = ClaimPacket(
                claim_id="claim-a",
                exact_text="The primitive remains open.",
                epistemic_class="OPEN",
                actor="owner",
                source_anchors=(anchor,),
                context_id="context-a",
                assumptions=("no-global-now",),
                valid_time="2026-08-21",
            )
            claim_event = ledger.append_claim(claim, transaction_time=FIXED_TIMES[1])
            justification = JustificationRecord(
                justification_id="just-a",
                premise_claim_ids=("claim-a",),
                conclusion_claim_id="claim-b",
                relation="SUPPORTS",
                method="OWNER_STATEMENT",
                actor="curator",
                assumption_ids=("no-global-now",),
            )
            ledger.append_justification(justification, transaction_time=FIXED_TIMES[2])

            reloaded = EpistemicLedger.load(path)
            self.assertEqual(len(reloaded.events), 3)
            self.assertEqual(reloaded.events[0].event_id, context_event.event_id)
            self.assertEqual(reloaded.events[1].event_id, claim_event.event_id)
            state = reloaded.fold()
            self.assertEqual(state["claims"]["claim-a"][0]["valid_time"], "2026-08-21")
            self.assertEqual(state["claims"]["claim-a"][0]["transaction_time"], FIXED_TIMES[1])
            self.assertEqual(state["contexts"]["context-a"][0]["assumptions"], ["no-global-now"])
            self.assertEqual(state["justifications"][0]["relation"], "SUPPORTS")

    def test_hash_chain_detects_event_tampering(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "ledger.jsonl"
            ledger = EpistemicLedger.load(path)
            ledger.append_claim(
                ClaimPacket("claim-a", "OPEN", "OPEN", "owner"),
                transaction_time=FIXED_TIMES[0],
            )
            value = json.loads(path.read_text(encoding="utf-8"))
            value["payload"]["exact_text"] = "silently changed"
            path.write_text(json.dumps(value) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                EpistemicLedger.load(path)

    def test_correction_preserves_predecessor_and_removes_active_conflict(self):
        ledger = EpistemicLedger()
        first = ledger.append_claim(
            ClaimPacket("claim-a", "Old text", "WORKING_HYPOTHESIS", "owner"),
            transaction_time=FIXED_TIMES[0],
        )
        second = ledger.append_claim(
            ClaimPacket("claim-a", "Corrected text", "SOURCE_SUPPORTED", "owner"),
            transaction_time=FIXED_TIMES[1],
        )
        self.assertEqual(len(ledger.fold()["conflicts"]), 1)
        ledger.append(
            "CORRECT",
            "owner",
            {
                "claim_id": "claim-a",
                "predecessor_event_id": first.event_id,
                "successor_event_id": second.event_id,
                "reason": "explicit correction",
            },
            transaction_time=FIXED_TIMES[2],
        )
        state = ledger.fold()
        self.assertEqual(len(state["claims"]["claim-a"]), 2)
        self.assertEqual(state["conflicts"], [])
        self.assertEqual(state["relations"][0]["event_type"], "CORRECT")

    def test_initialize_split_merge_retains_competing_claims(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository = LifecycleRepository(Path(temporary))
            root = repository.initialize("main", transaction_time=FIXED_TIMES[0])
            first = repository.ledger.append_claim(
                ClaimPacket("claim-a", "Option A", "WORKING_HYPOTHESIS", "owner"),
                transaction_time=FIXED_TIMES[1],
            )
            main_commit = repository.commit_events(
                "main", (first.event_id,), transaction_time=FIXED_TIMES[2]
            )
            branch_commit = repository.split(
                "main", "alternative", transaction_time=FIXED_TIMES[3]
            )
            second = repository.ledger.append_claim(
                ClaimPacket("claim-a", "Option B", "WORKING_HYPOTHESIS", "reviewer"),
                transaction_time=FIXED_TIMES[4],
            )
            repository.commit_events(
                "alternative", (second.event_id,), transaction_time=FIXED_TIMES[5]
            )
            merged = repository.merge(
                "main", "alternative", "merged", transaction_time=FIXED_TIMES[6]
            )

            self.assertIn(root.commit_id, main_commit.parent_ids)
            self.assertIn(main_commit.commit_id, branch_commit.parent_ids)
            self.assertEqual(merged.operation, "MERGE")
            self.assertEqual(merged.metadata["auto_resolution"], "NONE")
            self.assertEqual(len(merged.metadata["semantic_conflicts"]), 1)
            recovered = repository.recover("merged")
            self.assertEqual(recovered["state"], "RECOVERED")
            self.assertEqual(len(recovered["semantic_conflicts"]), 1)

    def test_split_exclusion_manifest_is_persisted(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository = LifecycleRepository(Path(temporary))
            repository.initialize("main", transaction_time=FIXED_TIMES[0])
            event = repository.ledger.append_claim(
                ClaimPacket("claim-a", "Exclude me", "OPEN", "owner"),
                transaction_time=FIXED_TIMES[1],
            )
            repository.commit_events("main", (event.event_id,), transaction_time=FIXED_TIMES[2])
            split = repository.split(
                "main",
                "without-a",
                exclude_event_ids=(event.event_id,),
                transaction_time=FIXED_TIMES[3],
            )
            self.assertNotIn(event.event_id, split.event_ids)
            self.assertEqual(split.metadata["exclusion_manifest"], [event.event_id])

    def test_compose_preserves_interfaces_parents_and_conflicts(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository = LifecycleRepository(Path(temporary))
            repository.initialize("left", transaction_time=FIXED_TIMES[0])
            repository.initialize("right", transaction_time=FIXED_TIMES[1])
            left = repository.ledger.append_claim(
                ClaimPacket("shared", "Left meaning", "OWNER_DIRECTION", "owner"),
                transaction_time=FIXED_TIMES[2],
            )
            repository.commit_events("left", (left.event_id,), transaction_time=FIXED_TIMES[3])
            right = repository.ledger.append_claim(
                ClaimPacket("shared", "Right meaning", "OPEN", "reviewer"),
                transaction_time=FIXED_TIMES[4],
            )
            repository.commit_events("right", (right.event_id,), transaction_time=FIXED_TIMES[5])
            composed = repository.compose(
                ("left", "right"),
                "composed",
                interface_map={"left.shared": "right.shared"},
                transaction_time=FIXED_TIMES[6],
            )
            self.assertEqual(composed.operation, "COMPOSE")
            self.assertEqual(len(composed.parent_ids), 2)
            self.assertEqual(composed.metadata["interface_map"]["left.shared"], "right.shared")
            self.assertEqual(len(composed.metadata["semantic_conflicts"]), 1)

    def test_migrate_recover_retire_keeps_predecessor_readable(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repository = LifecycleRepository(root)
            repository.initialize("main", transaction_time=FIXED_TIMES[0])
            event = repository.ledger.append_claim(
                ClaimPacket("claim-a", "Preserve unknown", "UNKNOWN", "owner"),
                transaction_time=FIXED_TIMES[1],
            )
            repository.commit_events("main", (event.event_id,), transaction_time=FIXED_TIMES[2])
            migrated = repository.migrate(
                "main", "schema-v2", 2, "migration-1", transaction_time=FIXED_TIMES[3]
            )
            self.assertEqual(migrated.metadata["unknown_field_policy"], "PRESERVE_RAW")
            recovered = repository.recover("schema-v2")
            self.assertEqual(recovered["state"], "RECOVERED")
            retired = repository.retire(
                "main", "schema-v2", ("metric semantics unresolved",), transaction_time=FIXED_TIMES[4]
            )
            self.assertTrue(retired.metadata["predecessor_remains_readable"])

            reloaded = LifecycleRepository(root)
            self.assertEqual(reloaded.head("main").commit_id, retired.commit_id)
            self.assertEqual(reloaded.head("schema-v2").commit_id, migrated.commit_id)
            self.assertEqual(reloaded.recover("schema-v2")["state_root"], recovered["state_root"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
