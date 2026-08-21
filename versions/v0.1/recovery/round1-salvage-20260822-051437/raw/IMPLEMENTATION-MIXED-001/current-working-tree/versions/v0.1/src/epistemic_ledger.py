#!/usr/bin/env python3
"""Append-only epistemic records and persisted lifecycle lineage for Byul v0.1.

These structures are authoritative for what was recorded and how repository state
succeded. They do not assert that a proposition is scientifically true.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


EPISTEMIC_CLASSES = {
    "SOURCE_SUPPORTED",
    "OWNER_DIRECTION",
    "WORKING_HYPOTHESIS",
    "OPEN",
    "NON_CONCLUSION",
    "YOUR_INFERENCE",
    "UNKNOWN",
    "RETRACTED_OR_CORRECTED",
}

EVENT_TYPES = {
    "CLAIM",
    "CLASSIFY",
    "CONTEXT",
    "JUSTIFY",
    "CORRECT",
    "SUPERSEDE",
    "RETRACT",
    "REVIEW",
    "TRANSFORM",
    "LIFECYCLE",
}

LIFECYCLE_OPERATIONS = {
    "CREATE",
    "MUTATE",
    "COMPOSE",
    "SPLIT",
    "MERGE",
    "MIGRATE",
    "DEGRADED",
    "RECOVER",
    "SUCCESSOR",
    "RETIRE",
}

JUSTIFICATION_RELATIONS = {
    "SUPPORTS",
    "ATTACKS",
    "REFINES",
    "SPECIALIZES",
    "ALTERNATE",
    "COMPOSES",
}

EVENT_REQUIRED_FIELDS: Mapping[str, Tuple[str, ...]] = {
    "CLAIM": ("claim_id", "exact_text", "epistemic_class", "valid_time", "context_id"),
    "CLASSIFY": ("claim_id", "epistemic_class"),
    "CONTEXT": ("context_id", "description", "valid_time"),
    "JUSTIFY": ("justification_id", "conclusion_claim_id", "relation", "method"),
    "CORRECT": ("claim_id", "predecessor_event_id", "successor_event_id", "reason"),
    "SUPERSEDE": ("claim_id", "predecessor_event_id", "successor_event_id", "reason"),
    "RETRACT": ("claim_id", "predecessor_event_id", "reason"),
    "REVIEW": ("target_event_id", "decision"),
    "TRANSFORM": ("source_digest", "target_digest", "contract_digest", "losses"),
    "LIFECYCLE": ("operation",),
}


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_json(value: object) -> str:
    return _sha256_bytes(_canonical_json(value).encode("utf-8"))


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _atomic_write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def _validate_event_payload(event_type: str, payload: Mapping[str, Any]) -> None:
    missing = [field_name for field_name in EVENT_REQUIRED_FIELDS[event_type] if field_name not in payload]
    if missing:
        raise ValueError(f"{event_type} payload missing required fields: {missing}")
    epistemic_class = payload.get("epistemic_class")
    if epistemic_class is not None and epistemic_class not in EPISTEMIC_CLASSES:
        raise ValueError(f"unsupported epistemic class: {epistemic_class}")
    relation = payload.get("relation")
    if event_type == "JUSTIFY" and relation not in JUSTIFICATION_RELATIONS:
        raise ValueError(f"unsupported justification relation: {relation}")
    operation = payload.get("operation")
    if event_type == "LIFECYCLE" and operation not in LIFECYCLE_OPERATIONS:
        raise ValueError(f"unsupported lifecycle operation: {operation}")


@dataclass(frozen=True)
class SourceAnchor:
    source_path: str
    source_sha256: str
    byte_start: int
    byte_end: int

    def validate(self) -> None:
        if not self.source_path:
            raise ValueError("source_path is required")
        if not re.fullmatch(r"[0-9a-f]{64}", self.source_sha256):
            raise ValueError("source_sha256 must be a lowercase SHA-256 digest")
        if self.byte_start < 0 or self.byte_end < self.byte_start:
            raise ValueError("invalid source byte range")


@dataclass(frozen=True)
class ClaimPacket:
    claim_id: str
    exact_text: str
    epistemic_class: str
    actor: str
    source_anchors: Tuple[SourceAnchor, ...] = ()
    structured_form: Optional[Mapping[str, Any]] = None
    polarity: str = "UNSPECIFIED"
    context_id: str = "GLOBAL_UNSPECIFIED"
    assumptions: Tuple[str, ...] = ()
    valid_time: str = "UNKNOWN"
    schema_version: int = 1

    def validate(self) -> None:
        if not self.claim_id or not self.actor or not self.exact_text:
            raise ValueError("claim_id, actor, and exact_text are required")
        if self.epistemic_class not in EPISTEMIC_CLASSES:
            raise ValueError(f"unsupported epistemic class: {self.epistemic_class}")
        for anchor in self.source_anchors:
            anchor.validate()

    def payload(self) -> Dict[str, Any]:
        self.validate()
        value = asdict(self)
        value["source_anchors"] = [asdict(anchor) for anchor in self.source_anchors]
        value["assumptions"] = list(self.assumptions)
        return value


@dataclass(frozen=True)
class ContextRecord:
    context_id: str
    description: str
    actor: str
    assumptions: Tuple[str, ...] = ()
    valid_time: str = "UNKNOWN"
    schema_version: int = 1

    def payload(self) -> Dict[str, Any]:
        if not self.context_id or not self.description or not self.actor:
            raise ValueError("context_id, description, and actor are required")
        value = asdict(self)
        value["assumptions"] = list(self.assumptions)
        return value


@dataclass(frozen=True)
class JustificationRecord:
    justification_id: str
    premise_claim_ids: Tuple[str, ...]
    conclusion_claim_id: str
    relation: str
    method: str
    actor: str
    assumption_ids: Tuple[str, ...] = ()
    schema_version: int = 1

    def payload(self) -> Dict[str, Any]:
        if not self.justification_id or not self.conclusion_claim_id or not self.method:
            raise ValueError("justification_id, conclusion_claim_id, and method are required")
        if self.relation not in JUSTIFICATION_RELATIONS:
            raise ValueError(f"unsupported justification relation: {self.relation}")
        value = asdict(self)
        value["premise_claim_ids"] = list(self.premise_claim_ids)
        value["assumption_ids"] = list(self.assumption_ids)
        return value


@dataclass(frozen=True)
class LedgerEvent:
    event_id: str
    event_type: str
    transaction_time: str
    actor: str
    payload: Mapping[str, Any]
    previous_event_id: Optional[str]
    schema_version: int = 1

    @staticmethod
    def create(
        event_type: str,
        actor: str,
        payload: Mapping[str, Any],
        previous_event_id: Optional[str],
        transaction_time: Optional[str] = None,
    ) -> "LedgerEvent":
        if event_type not in EVENT_TYPES:
            raise ValueError(f"unsupported event type: {event_type}")
        if not actor:
            raise ValueError("actor is required")
        _validate_event_payload(event_type, payload)
        body = {
            "event_type": event_type,
            "transaction_time": transaction_time or _utc_now(),
            "actor": actor,
            "payload": dict(payload),
            "previous_event_id": previous_event_id,
            "schema_version": 1,
        }
        return LedgerEvent(event_id=_sha256_json(body), **body)

    def verify(self) -> None:
        if self.event_type not in EVENT_TYPES:
            raise ValueError(f"unsupported event type: {self.event_type}")
        _validate_event_payload(self.event_type, self.payload)
        body = asdict(self)
        event_id = body.pop("event_id")
        if _sha256_json(body) != event_id:
            raise ValueError(f"event digest mismatch: {self.event_id}")


class EpistemicLedger:
    """Append-only hash-chained JSONL ledger with deterministic fold semantics."""

    def __init__(self, events: Optional[Sequence[LedgerEvent]] = None, path: Optional[Path] = None):
        self.events: List[LedgerEvent] = list(events or [])
        self.path = Path(path) if path is not None else None
        self.verify_chain()

    @classmethod
    def load(cls, path: Path) -> "EpistemicLedger":
        path = Path(path)
        events: List[LedgerEvent] = []
        if path.exists():
            for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                if not line.strip():
                    continue
                try:
                    events.append(LedgerEvent(**json.loads(line)))
                except (TypeError, json.JSONDecodeError) as exc:
                    raise ValueError(f"invalid ledger event at line {line_no}") from exc
        return cls(events=events, path=path)

    def verify_chain(self) -> None:
        previous: Optional[str] = None
        seen = set()
        for event in self.events:
            event.verify()
            if event.event_id in seen:
                raise ValueError(f"duplicate event id: {event.event_id}")
            if event.previous_event_id != previous:
                raise ValueError(f"broken event chain at {event.event_id}")
            seen.add(event.event_id)
            previous = event.event_id

    def append(
        self,
        event_type: str,
        actor: str,
        payload: Mapping[str, Any],
        transaction_time: Optional[str] = None,
    ) -> LedgerEvent:
        previous = self.events[-1].event_id if self.events else None
        event = LedgerEvent.create(
            event_type=event_type,
            actor=actor,
            payload=payload,
            previous_event_id=previous,
            transaction_time=transaction_time,
        )
        if self.path is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            encoded = (_canonical_json(asdict(event)) + "\n").encode("utf-8")
            with self.path.open("ab") as stream:
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
        self.events.append(event)
        return event

    def append_claim(self, packet: ClaimPacket, transaction_time: Optional[str] = None) -> LedgerEvent:
        return self.append("CLAIM", packet.actor, packet.payload(), transaction_time)

    def append_context(self, context: ContextRecord, transaction_time: Optional[str] = None) -> LedgerEvent:
        return self.append("CONTEXT", context.actor, context.payload(), transaction_time)

    def append_justification(
        self, record: JustificationRecord, transaction_time: Optional[str] = None
    ) -> LedgerEvent:
        return self.append("JUSTIFY", record.actor, record.payload(), transaction_time)

    def event_map(self) -> Dict[str, LedgerEvent]:
        return {event.event_id: event for event in self.events}

    def fold(self, event_ids: Optional[Iterable[str]] = None) -> Dict[str, Any]:
        selected = set(event_ids) if event_ids is not None else None
        claims: Dict[str, List[Dict[str, Any]]] = {}
        contexts: Dict[str, List[Dict[str, Any]]] = {}
        justifications: List[Dict[str, Any]] = []
        relations: List[Dict[str, Any]] = []
        reviews: List[Dict[str, Any]] = []
        transformations: List[Dict[str, Any]] = []
        lifecycle: List[Dict[str, Any]] = []
        included: List[str] = []

        for event in self.events:
            if selected is not None and event.event_id not in selected:
                continue
            included.append(event.event_id)
            envelope = {
                "event_id": event.event_id,
                "transaction_time": event.transaction_time,
                "actor": event.actor,
                **dict(event.payload),
            }
            if event.event_type == "CLAIM":
                claims.setdefault(str(event.payload["claim_id"]), []).append(envelope)
            elif event.event_type == "CONTEXT":
                contexts.setdefault(str(event.payload["context_id"]), []).append(envelope)
            elif event.event_type == "JUSTIFY":
                justifications.append(envelope)
            elif event.event_type in {"CLASSIFY", "CORRECT", "SUPERSEDE", "RETRACT"}:
                relations.append({"event_type": event.event_type, **envelope})
            elif event.event_type == "REVIEW":
                reviews.append(envelope)
            elif event.event_type == "TRANSFORM":
                transformations.append(envelope)
            elif event.event_type == "LIFECYCLE":
                lifecycle.append(envelope)

        conflicts = self._detect_conflicts(claims, relations)
        return {
            "included_event_ids": included,
            "claims": claims,
            "contexts": contexts,
            "justifications": justifications,
            "relations": relations,
            "reviews": reviews,
            "transformations": transformations,
            "lifecycle": lifecycle,
            "conflicts": conflicts,
        }

    @staticmethod
    def _detect_conflicts(
        claims: Mapping[str, Sequence[Mapping[str, Any]]],
        relations: Sequence[Mapping[str, Any]],
    ) -> List[Dict[str, Any]]:
        superseded = {
            str(relation.get("predecessor_event_id"))
            for relation in relations
            if relation.get("event_type") in {"SUPERSEDE", "CORRECT", "RETRACT"}
            and relation.get("predecessor_event_id")
        }
        conflicts: List[Dict[str, Any]] = []
        semantic_fields = ("exact_text", "epistemic_class", "polarity", "context_id")
        for claim_id, versions in sorted(claims.items()):
            active = [version for version in versions if version.get("event_id") not in superseded]
            signatures = {
                tuple(_canonical_json(version.get(field)) for field in semantic_fields)
                for version in active
            }
            if len(signatures) > 1:
                conflicts.append({
                    "claim_id": claim_id,
                    "event_ids": sorted(str(version["event_id"]) for version in active),
                    "reason": "COMPETING_ACTIVE_CLAIM_VARIANTS",
                })
        return conflicts

    def state_root(self, event_ids: Optional[Iterable[str]] = None) -> str:
        return _sha256_json(self.fold(event_ids))


@dataclass(frozen=True)
class LifecycleCommit:
    commit_id: str
    operation: str
    branch: str
    parent_ids: Tuple[str, ...]
    event_ids: Tuple[str, ...]
    transaction_time: str
    schema_version: int = 1
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @staticmethod
    def create(
        operation: str,
        branch: str,
        parent_ids: Iterable[str],
        event_ids: Iterable[str],
        metadata: Optional[Mapping[str, Any]] = None,
        transaction_time: Optional[str] = None,
    ) -> "LifecycleCommit":
        if operation not in LIFECYCLE_OPERATIONS:
            raise ValueError(f"unsupported lifecycle operation: {operation}")
        body = {
            "operation": operation,
            "branch": branch,
            "parent_ids": tuple(parent_ids),
            "event_ids": tuple(sorted(set(event_ids))),
            "transaction_time": transaction_time or _utc_now(),
            "schema_version": 1,
            "metadata": dict(metadata or {}),
        }
        return LifecycleCommit(commit_id=_sha256_json(body), **body)

    def verify(self) -> None:
        body = asdict(self)
        commit_id = body.pop("commit_id")
        if _sha256_json(body) != commit_id:
            raise ValueError(f"lifecycle commit digest mismatch: {self.commit_id}")


class LifecycleRepository:
    """Immutable lifecycle commits plus mutable branch refs over an event ledger."""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.commits_dir = self.root / "commits"
        self.refs_path = self.root / "refs.json"
        self.ledger = EpistemicLedger.load(self.root / "ledger.jsonl")

    @staticmethod
    def _validate_branch(branch: str) -> None:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,127}", branch):
            raise ValueError(f"invalid branch name: {branch!r}")
        if ".." in branch or branch.endswith("/"):
            raise ValueError(f"invalid branch name: {branch!r}")

    def refs(self) -> Dict[str, str]:
        if not self.refs_path.exists():
            return {}
        value = json.loads(self.refs_path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("refs.json must contain an object")
        return {str(key): str(item) for key, item in value.items()}

    def _write_refs(self, refs: Mapping[str, str]) -> None:
        _atomic_write_json(self.refs_path, dict(sorted(refs.items())))

    def _commit_path(self, commit_id: str) -> Path:
        if not re.fullmatch(r"[0-9a-f]{64}", commit_id):
            raise ValueError(f"invalid lifecycle commit id: {commit_id!r}")
        return self.commits_dir / f"{commit_id}.json"

    def _store_commit(self, commit: LifecycleCommit) -> LifecycleCommit:
        commit.verify()
        event_map = self.ledger.event_map()
        missing_events = sorted(set(commit.event_ids) - set(event_map))
        if missing_events:
            raise ValueError(f"commit references missing ledger events: {missing_events}")
        for parent in commit.parent_ids:
            if not self._commit_path(parent).exists():
                raise ValueError(f"commit references missing parent: {parent}")
        path = self._commit_path(commit.commit_id)
        if path.exists():
            existing = LifecycleCommit(**json.loads(path.read_text(encoding="utf-8")))
            existing.verify()
            if existing != commit:
                raise ValueError(f"commit id collision: {commit.commit_id}")
        else:
            _atomic_write_json(path, asdict(commit))
        refs = self.refs()
        refs[commit.branch] = commit.commit_id
        self._write_refs(refs)
        return commit

    def read_commit(self, commit_id: str) -> LifecycleCommit:
        path = self._commit_path(commit_id)
        if not path.exists():
            raise KeyError(commit_id)
        value = json.loads(path.read_text(encoding="utf-8"))
        value["parent_ids"] = tuple(value["parent_ids"])
        value["event_ids"] = tuple(value["event_ids"])
        commit = LifecycleCommit(**value)
        commit.verify()
        return commit

    def head(self, branch: str) -> LifecycleCommit:
        self._validate_branch(branch)
        commit_id = self.refs().get(branch)
        if commit_id is None:
            raise KeyError(branch)
        return self.read_commit(commit_id)

    def initialize(self, branch: str = "main", transaction_time: Optional[str] = None) -> LifecycleCommit:
        self._validate_branch(branch)
        if branch in self.refs():
            raise ValueError(f"branch already exists: {branch}")
        commit = LifecycleCommit.create(
            operation="CREATE",
            branch=branch,
            parent_ids=(),
            event_ids=(event.event_id for event in self.ledger.events),
            transaction_time=transaction_time,
        )
        return self._store_commit(commit)

    def commit_events(
        self,
        branch: str,
        event_ids: Iterable[str],
        operation: str = "MUTATE",
        metadata: Optional[Mapping[str, Any]] = None,
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        parent = self.head(branch)
        combined = set(parent.event_ids) | set(event_ids)
        commit = LifecycleCommit.create(
            operation=operation,
            branch=branch,
            parent_ids=(parent.commit_id,),
            event_ids=combined,
            metadata=metadata,
            transaction_time=transaction_time,
        )
        return self._store_commit(commit)

    def split(
        self,
        source_branch: str,
        new_branch: str,
        exclude_event_ids: Iterable[str] = (),
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        self._validate_branch(new_branch)
        if new_branch in self.refs():
            raise ValueError(f"branch already exists: {new_branch}")
        parent = self.head(source_branch)
        excluded = set(exclude_event_ids)
        unknown = excluded - set(parent.event_ids)
        if unknown:
            raise ValueError(f"cannot exclude events absent from source branch: {sorted(unknown)}")
        commit = LifecycleCommit.create(
            operation="SPLIT",
            branch=new_branch,
            parent_ids=(parent.commit_id,),
            event_ids=set(parent.event_ids) - excluded,
            metadata={"source_branch": source_branch, "exclusion_manifest": sorted(excluded)},
            transaction_time=transaction_time,
        )
        return self._store_commit(commit)

    def compose(
        self,
        source_branches: Sequence[str],
        target_branch: str,
        interface_map: Mapping[str, Any],
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        if len(source_branches) < 2:
            raise ValueError("compose requires at least two source branches")
        return self._multi_parent_commit(
            "COMPOSE", source_branches, target_branch, {"interface_map": dict(interface_map)}, transaction_time
        )

    def merge(
        self,
        left_branch: str,
        right_branch: str,
        target_branch: str,
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        return self._multi_parent_commit(
            "MERGE", (left_branch, right_branch), target_branch, {}, transaction_time
        )

    def _multi_parent_commit(
        self,
        operation: str,
        source_branches: Sequence[str],
        target_branch: str,
        metadata: Mapping[str, Any],
        transaction_time: Optional[str],
    ) -> LifecycleCommit:
        self._validate_branch(target_branch)
        parents = [self.head(branch) for branch in source_branches]
        event_ids = sorted({event_id for parent in parents for event_id in parent.event_ids})
        conflicts = self.ledger.fold(event_ids)["conflicts"]
        full_metadata = {
            **dict(metadata),
            "source_branches": list(source_branches),
            "semantic_conflicts": conflicts,
            "auto_resolution": "NONE",
        }
        commit = LifecycleCommit.create(
            operation=operation,
            branch=target_branch,
            parent_ids=(parent.commit_id for parent in parents),
            event_ids=event_ids,
            metadata=full_metadata,
            transaction_time=transaction_time,
        )
        return self._store_commit(commit)

    def migrate(
        self,
        source_branch: str,
        target_branch: str,
        target_schema_version: int,
        transformer_version: str,
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        source = self.head(source_branch)
        commit = LifecycleCommit.create(
            operation="MIGRATE",
            branch=target_branch,
            parent_ids=(source.commit_id,),
            event_ids=source.event_ids,
            metadata={
                "source_branch": source_branch,
                "target_schema_version": target_schema_version,
                "transformer_version": transformer_version,
                "unknown_field_policy": "PRESERVE_RAW",
            },
            transaction_time=transaction_time,
        )
        return self._store_commit(commit)

    def recover(self, branch: str) -> Dict[str, Any]:
        head = self.head(branch)
        event_map = self.ledger.event_map()
        missing = sorted(set(head.event_ids) - set(event_map))
        if missing:
            return {
                "state": "DEGRADED",
                "branch": branch,
                "head": head.commit_id,
                "missing_event_ids": missing,
            }
        self.ledger.verify_chain()
        folded = self.ledger.fold(head.event_ids)
        return {
            "state": "RECOVERED",
            "branch": branch,
            "head": head.commit_id,
            "event_count": len(head.event_ids),
            "state_root": _sha256_json(folded),
            "semantic_conflicts": folded["conflicts"],
        }

    def retire(
        self,
        branch: str,
        successor_branch: str,
        unresolved_losses: Sequence[str] = (),
        transaction_time: Optional[str] = None,
    ) -> LifecycleCommit:
        successor = self.head(successor_branch)
        return self.commit_events(
            branch=branch,
            event_ids=(),
            operation="RETIRE",
            metadata={
                "successor_branch": successor_branch,
                "successor_commit_id": successor.commit_id,
                "unresolved_losses": list(unresolved_losses),
                "predecessor_remains_readable": True,
            },
            transaction_time=transaction_time,
        )
