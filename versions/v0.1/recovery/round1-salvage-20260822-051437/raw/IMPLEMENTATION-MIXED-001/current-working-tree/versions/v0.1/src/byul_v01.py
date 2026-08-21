#!/usr/bin/env python3
"""Byul v0.1 — exact memo authority, contracted views, and lifecycle ledger.

Default ingestion reads the exact Git tree named by SOURCE_BASELINE_COMMIT and
verifies every byte against an immutable manifest.  Working-tree ingestion is
available only through an explicit --memory-root override and is labeled
unpinned.  All structures remain experimental, non-normative, and unvalidated.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from epistemic_ledger import ClaimPacket, EpistemicLedger, LifecycleRepository, SourceAnchor
from transformation_contracts import (
    PRESERVATION_LEVELS,
    QueryContract,
    TransformDefinition,
    TransformationReceipt,
    TransformRegistry,
    ViewPlanner,
    sha256_json,
)


SOURCE_BASELINE_COMMIT = "2a4529b69bc237125a1f012835d7a9b78ce3fec9"
VERSIONS_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = VERSIONS_DIR.parent
DEFAULT_MEMORY_ROOT = VERSIONS_DIR / "v0.01" / "memory"
DEFAULT_MANIFEST_PATH = VERSIONS_DIR / "v0.1" / "data" / "source_manifest_v001.json"
MEMORY_TREE_PATH = "versions/v0.01/memory"


VIEW_DEPENDENCIES: Mapping[str, Tuple[str, ...]] = {
    "RAW_CORPUS": ("*",),
    "HISTORY_ORDER_INDEX": ("08_CHANNEL_CHRONOLOGY.md",),
    "CURRENT_STATE_VIEW": (
        "01_OWNER_WORLDVIEW_CURRENT.md",
        "02_CAUSAL_SET_LEARNING.md",
        "03_MODEL_FAMILY_AND_COMPLEMENTARITY.md",
        "04_ROUTING_AND_LIFECYCLE.md",
        "10_ACTIVE_CHANNEL_LOG.md",
        "11_CORE_PRINCIPLES.md",
    ),
    "OPEN_QUESTION_VIEW": ("07_OPEN_QUESTIONS_AND_NEXT_JOBS.md", "10_ACTIVE_CHANNEL_LOG.md"),
    "MODEL_FAMILY_VIEW": (
        "02_CAUSAL_SET_LEARNING.md",
        "03_MODEL_FAMILY_AND_COMPLEMENTARITY.md",
        "04_ROUTING_AND_LIFECYCLE.md",
        "05_SIMULATION_AND_COMMITTEE.md",
        "10_ACTIVE_CHANNEL_LOG.md",
    ),
    "LIFECYCLE_VIEW": (
        "04_ROUTING_AND_LIFECYCLE.md",
        "05_SIMULATION_AND_COMMITTEE.md",
        "06_MI1_INITIALIZATION_TARGET.md",
        "09_VERSION_POLICY.md",
        "10_ACTIVE_CHANNEL_LOG.md",
        "11_CORE_PRINCIPLES.md",
    ),
    "CORE_PRINCIPLES_VIEW": ("11_CORE_PRINCIPLES.md",),
}

INTENT_TO_VIEWS: Mapping[str, Tuple[str, ...]] = {
    "history": ("HISTORY_ORDER_INDEX",),
    "current_state": ("CURRENT_STATE_VIEW",),
    "open_questions": ("OPEN_QUESTION_VIEW",),
    "model_family": ("MODEL_FAMILY_VIEW",),
    "lifecycle": ("LIFECYCLE_VIEW",),
    "principles": ("CORE_PRINCIPLES_VIEW",),
    "raw": ("RAW_CORPUS",),
}


class BaselineVerificationError(ValueError):
    """Raised when a pinned Git source differs from its immutable manifest."""


def _norm(text: str) -> str:
    return " ".join(text.strip().split())


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _git(repo_root: Path, *args: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = ""
        if isinstance(exc, subprocess.CalledProcessError):
            detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise BaselineVerificationError(f"Git source read failed: {detail or exc}") from exc
    return result.stdout


def _corpus_digest(raw_documents: Mapping[str, bytes]) -> str:
    digest = hashlib.sha256()
    for source in sorted(raw_documents):
        name = source.encode("utf-8")
        digest.update(len(name).to_bytes(8, "big"))
        digest.update(name)
        digest.update(hashlib.sha256(raw_documents[source]).digest())
    return digest.hexdigest()


def _explicit_tags(text: str) -> Tuple[str, ...]:
    tags: List[str] = []
    upper = text.upper()
    if "OPEN" in upper or "미결" in text:
        tags.append("OPEN")
    if "WORKING_HYPOTHESIS" in upper or "WORKING HYPOTHESIS" in upper:
        tags.append("WORKING_HYPOTHESIS")
    if "OWNER_" in upper or "OWNER HYPOTHESIS" in upper or "OWNER 가설" in text:
        tags.append("OWNER_MARKER")
    if "NON_NORMATIVE" in upper or "NON-NORMATIVE" in upper:
        tags.append("NON_NORMATIVE")
    if "NOT_VALIDATED" in upper or "NOT VALIDATED" in upper:
        tags.append("NOT_VALIDATED")
    if "NON_CONCLUSION" in upper or "NON-CONCLUSION" in upper:
        tags.append("NON_CONCLUSION")
    if "CORE PRINCIPLE" in upper or "PRINCIPLE —" in upper:
        tags.append("CORE_PRINCIPLE")
    if "UNKNOWN" in upper:
        tags.append("UNKNOWN")
    return tuple(sorted(set(tags)))


@dataclass(frozen=True)
class MemoryAtom:
    atom_id: str
    source: str
    source_sha256: str
    line_no: int
    byte_start: int
    byte_end: int
    section: str
    kind: str
    text: str
    tags: Tuple[str, ...] = ()


@dataclass
class MemoryDocument:
    source: str
    raw_sha256: str
    raw_bytes: bytes = field(repr=False)
    git_blob_oid: Optional[str] = None
    atoms: List[MemoryAtom] = field(default_factory=list)


@dataclass
class SituationFingerprint:
    intent: str
    preservation: Dict[str, str] = field(default_factory=dict)
    require_exact_metric: bool = False
    unknowns: List[str] = field(default_factory=list)

    def validate(self) -> None:
        bad = {value.upper() for value in self.preservation.values()} - PRESERVATION_LEVELS
        if bad:
            raise ValueError(f"unknown preservation levels: {sorted(bad)}")


@dataclass(frozen=True)
class CurrentModelState:
    source_baseline_commit: str
    source_mode: str
    manifest_digest: Optional[str]
    exact_baseline_verified: bool
    content_digest: str
    normalized_digest: str
    document_count: int
    atom_count: int
    available_views: Tuple[str, ...]

    @property
    def normalized_content_digest(self) -> str:
        return self.normalized_digest


@dataclass(frozen=True)
class LifecycleContext:
    phase: str
    mutation_scope: str = "UNKNOWN"
    rollback_required: bool = False


@dataclass
class RoutePlan:
    decision_state: str
    target_views: List[str]
    transform_contracts: List[str]
    transformation_paths: Dict[str, List[str]]
    loss_manifest: Dict[str, Dict[str, str]]
    unmet_demands: List[str]
    required_validations: List[str]
    principle_gate_state: str
    notes: List[str]


@dataclass(frozen=True)
class DerivationReceipt:
    receipt_id: str
    view: str
    source_digest: str
    target_digest: str
    view_definition_digest: str
    parameter_digest: str
    preservation: Mapping[str, str]
    losses: Tuple[str, ...]
    validation_result: str
    reversible: str
    dependencies: Tuple[str, ...]
    introduced_interpretation: Tuple[str, ...]
    cost_class: str


def _parse_markdown(source: str, raw_bytes: bytes) -> List[MemoryAtom]:
    try:
        raw = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BaselineVerificationError(f"source is not UTF-8: {source}") from exc
    source_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    atoms: List[MemoryAtom] = []
    section = "ROOT"
    in_code = False
    seen: Dict[str, int] = {}
    byte_offset = 0
    for line_no, physical_line in enumerate(raw.splitlines(keepends=True), start=1):
        line = physical_line.rstrip("\r\n")
        line_bytes = line.encode("utf-8")
        byte_start = byte_offset
        byte_end = byte_start + len(line_bytes)
        byte_offset += len(physical_line.encode("utf-8"))
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            kind = "code_fence"
        elif in_code:
            kind = "code"
        elif stripped.startswith("#"):
            kind = "heading"
            section = stripped.lstrip("#").strip() or "ROOT"
        elif re.match(r"^\d+\.\s+", stripped):
            kind = "numbered"
        elif stripped.startswith("- "):
            kind = "bullet"
        elif stripped.startswith(">"):
            kind = "quote"
        else:
            kind = "text"
        normalized = _norm(stripped)
        occurrence = seen.get(normalized, 0)
        seen[normalized] = occurrence + 1
        atom_id = _sha256(
            f"{source_sha256}|{source}|{byte_start}|{byte_end}|{normalized}|{occurrence}"
        )[:20]
        atoms.append(
            MemoryAtom(
                atom_id=atom_id,
                source=source,
                source_sha256=source_sha256,
                line_no=line_no,
                byte_start=byte_start,
                byte_end=byte_end,
                section=section,
                kind=kind,
                text=stripped,
                tags=_explicit_tags(stripped),
            )
        )
    return atoms


class MemoryCorpus:
    def __init__(
        self,
        root: Optional[Path],
        documents: Dict[str, MemoryDocument],
        source_baseline_commit: str,
        source_mode: str,
        manifest_digest: Optional[str],
        manifest_verified: bool,
    ):
        self.root = root
        self.documents = documents
        self.source_baseline_commit = source_baseline_commit
        self.source_mode = source_mode
        self.manifest_digest = manifest_digest
        self.manifest_verified = manifest_verified

    @classmethod
    def load(
        cls,
        root: Optional[Path] = None,
        *,
        source_mode: Optional[str] = None,
        source_commit: str = SOURCE_BASELINE_COMMIT,
        repo_root: Path = REPO_ROOT,
        manifest_path: Path = DEFAULT_MANIFEST_PATH,
    ) -> "MemoryCorpus":
        if root is not None:
            if source_mode not in {None, "worktree", "WORKING_TREE_UNPINNED"}:
                raise ValueError("an explicit root supports only unverified worktree mode")
            root = Path(root)
            raw_documents = {
                path.name: path.read_bytes() for path in sorted(root.glob("*.md"))
            }
            if not raw_documents:
                raise FileNotFoundError(f"no markdown memory files found under {root}")
            return cls._from_raw(
                root=root,
                raw_documents=raw_documents,
                blob_oids={},
                source_baseline_commit="WORKING_TREE_UNPINNED",
                source_mode="WORKTREE_UNVERIFIED",
                manifest_digest=None,
                manifest_verified=False,
            )

        manifest_path = Path(manifest_path)
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes.decode("utf-8"))
        if not isinstance(manifest, dict):
            raise BaselineVerificationError("source manifest must be a JSON object")
        if manifest.get("source_baseline_commit") != source_commit:
            raise BaselineVerificationError("source commit does not match immutable manifest")
        source_root = str(manifest.get("source_root", ""))
        if source_root != MEMORY_TREE_PATH:
            raise BaselineVerificationError("source root does not match v0.1 contract")
        file_specs = manifest.get("files")
        if not isinstance(file_specs, list) or not file_specs:
            raise BaselineVerificationError("source manifest has no files")
        expected_paths = [str(item["path"]) for item in file_specs]
        actual_paths = _git(
            Path(repo_root), "ls-tree", "-r", "--name-only", source_commit, "--", source_root
        ).decode("utf-8").splitlines()
        if actual_paths != expected_paths:
            raise BaselineVerificationError(
                f"Git tree file set differs from manifest: expected {expected_paths}, got {actual_paths}"
            )

        raw_documents: Dict[str, bytes] = {}
        blob_oids: Dict[str, str] = {}
        for item in file_specs:
            path = str(item["path"])
            source = Path(path).name
            blob_oid = _git(Path(repo_root), "rev-parse", f"{source_commit}:{path}").decode().strip()
            if blob_oid != item.get("git_blob_oid"):
                raise BaselineVerificationError(f"Git blob differs from manifest: {path}")
            raw = _git(Path(repo_root), "cat-file", "blob", blob_oid)
            actual_sha256 = hashlib.sha256(raw).hexdigest()
            if actual_sha256 != item.get("sha256") or len(raw) != item.get("bytes"):
                raise BaselineVerificationError(f"source bytes differ from manifest: {path}")
            raw_documents[source] = raw
            blob_oids[source] = blob_oid
        return cls._from_raw(
            root=None,
            raw_documents=raw_documents,
            blob_oids=blob_oids,
            source_baseline_commit=source_commit,
            source_mode="EXACT_GIT_TREE",
            manifest_digest=hashlib.sha256(manifest_bytes).hexdigest(),
            manifest_verified=True,
        )

    @classmethod
    def _from_raw(
        cls,
        root: Optional[Path],
        raw_documents: Mapping[str, bytes],
        blob_oids: Mapping[str, str],
        source_baseline_commit: str,
        source_mode: str,
        manifest_digest: Optional[str],
        manifest_verified: bool,
    ) -> "MemoryCorpus":
        documents: Dict[str, MemoryDocument] = {}
        for source in sorted(raw_documents):
            raw = raw_documents[source]
            documents[source] = MemoryDocument(
                source=source,
                raw_sha256=hashlib.sha256(raw).hexdigest(),
                raw_bytes=raw,
                git_blob_oid=blob_oids.get(source),
                atoms=_parse_markdown(source, raw),
            )
        return cls(
            root=root,
            documents=documents,
            source_baseline_commit=source_baseline_commit,
            source_mode=source_mode,
            manifest_digest=manifest_digest,
            manifest_verified=manifest_verified,
        )

    def raw_documents(self) -> Dict[str, bytes]:
        return {source: document.raw_bytes for source, document in self.documents.items()}

    def restore_source_bytes(self, target_root: Path) -> Dict[str, str]:
        """Restore authoritative source bytes without overwriting existing files."""

        target_root = Path(target_root)
        target_root.mkdir(parents=True, exist_ok=True)
        restored: Dict[str, str] = {}
        for source, document in sorted(self.documents.items()):
            target = target_root / source
            with target.open("xb") as stream:
                stream.write(document.raw_bytes)
            restored[source] = document.raw_sha256
        return restored

    def atoms(self) -> List[MemoryAtom]:
        return [atom for name in sorted(self.documents) for atom in self.documents[name].atoms]

    def content_digest(self) -> str:
        return _corpus_digest(self.raw_documents())

    def normalized_content_digest(self) -> str:
        payload = "\n".join(
            f"{atom.source}|{_norm(atom.text)}" for atom in self.atoms() if _norm(atom.text)
        )
        return _sha256(payload)

    def model_state(self) -> CurrentModelState:
        return CurrentModelState(
            source_baseline_commit=self.source_baseline_commit,
            source_mode=self.source_mode,
            manifest_digest=self.manifest_digest,
            exact_baseline_verified=self.manifest_verified,
            content_digest=self.content_digest(),
            normalized_digest=self.normalized_content_digest(),
            document_count=len(self.documents),
            atom_count=len(self.atoms()),
            available_views=tuple(VIEW_DEPENDENCIES.keys()),
        )

    def history_items(self) -> List[MemoryAtom]:
        document = self.documents.get("08_CHANNEL_CHRONOLOGY.md")
        if not document:
            return []
        return [atom for atom in document.atoms if atom.kind == "numbered"]

    def history_edges(self) -> List[Tuple[str, str]]:
        items = self.history_items()
        return [(items[index].atom_id, items[index + 1].atom_id) for index in range(len(items) - 1)]

    def history_is_acyclic(self) -> bool:
        graph: Dict[str, List[str]] = {}
        for left, right in self.history_edges():
            graph.setdefault(left, []).append(right)
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node: str) -> bool:
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            if any(not visit(nxt) for nxt in graph.get(node, [])):
                return False
            visiting.remove(node)
            visited.add(node)
            return True

        return all(visit(node) for node in list(graph))

    def view(self, name: str) -> List[MemoryAtom]:
        if name not in VIEW_DEPENDENCIES:
            raise KeyError(name)
        dependencies = VIEW_DEPENDENCIES[name]
        atoms = (
            self.atoms()
            if dependencies == ("*",)
            else [
                atom
                for source in dependencies
                if source in self.documents
                for atom in self.documents[source].atoms
            ]
        )
        if name == "HISTORY_ORDER_INDEX":
            return self.history_items()
        if name == "OPEN_QUESTION_VIEW":
            return [
                atom
                for atom in atoms
                if "OPEN" in atom.tags or "미결" in atom.text or "Open Question" in atom.text
            ]
        if name == "CURRENT_STATE_VIEW":
            needles = ("current", "현재", "strongest", "현행", "direction", "방향")
            return [
                atom for atom in atoms if any(needle.lower() in atom.text.lower() for needle in needles)
            ]
        return atoms

    def snapshot(self) -> Dict[str, object]:
        return {
            "snapshot_schema": 2,
            "source_baseline_commit": self.source_baseline_commit,
            "source_mode": self.source_mode,
            "manifest_digest": self.manifest_digest,
            "manifest_verified": self.manifest_verified,
            "content_digest": self.content_digest(),
            "normalized_digest": self.normalized_content_digest(),
            "documents": {
                name: {
                    "raw_sha256": document.raw_sha256,
                    "raw_base64": base64.b64encode(document.raw_bytes).decode("ascii"),
                    "git_blob_oid": document.git_blob_oid,
                    "atoms": [asdict(atom) for atom in document.atoms],
                }
                for name, document in sorted(self.documents.items())
            },
        }

    @staticmethod
    def snapshot_content_digest(snapshot: Mapping[str, object]) -> str:
        documents = snapshot.get("documents")
        if not isinstance(documents, Mapping):
            raise ValueError("snapshot documents are missing")
        raw_documents: Dict[str, bytes] = {}
        for source in sorted(documents):
            document = documents[source]
            if not isinstance(document, Mapping) or "raw_base64" not in document:
                raise ValueError("snapshot lacks exact raw bytes")
            raw = base64.b64decode(str(document["raw_base64"]), validate=True)
            if hashlib.sha256(raw).hexdigest() != document.get("raw_sha256"):
                raise ValueError(f"snapshot raw digest mismatch: {source}")
            raw_documents[str(source)] = raw
        return _corpus_digest(raw_documents)

    @classmethod
    def from_snapshot(cls, snapshot: Mapping[str, object]) -> "MemoryCorpus":
        documents = snapshot.get("documents")
        if not isinstance(documents, Mapping):
            raise ValueError("snapshot documents are missing")
        raw_documents: Dict[str, bytes] = {}
        blob_oids: Dict[str, str] = {}
        for source, value in documents.items():
            if not isinstance(value, Mapping):
                raise ValueError(f"invalid snapshot document: {source}")
            raw = base64.b64decode(str(value["raw_base64"]), validate=True)
            if hashlib.sha256(raw).hexdigest() != value.get("raw_sha256"):
                raise ValueError(f"snapshot raw digest mismatch: {source}")
            raw_documents[str(source)] = raw
            if value.get("git_blob_oid"):
                blob_oids[str(source)] = str(value["git_blob_oid"])
        corpus = cls._from_raw(
            root=None,
            raw_documents=raw_documents,
            blob_oids=blob_oids,
            source_baseline_commit=str(snapshot.get("source_baseline_commit", "UNKNOWN")),
            source_mode=str(snapshot.get("source_mode", "SNAPSHOT")),
            manifest_digest=(
                None if snapshot.get("manifest_digest") is None else str(snapshot["manifest_digest"])
            ),
            manifest_verified=bool(snapshot.get("manifest_verified", False)),
        )
        for source, value in documents.items():
            assert isinstance(value, Mapping)
            stored_atoms = value.get("atoms")
            rebuilt_atoms = [asdict(atom) for atom in corpus.documents[str(source)].atoms]
            if json.dumps(stored_atoms, sort_keys=True) != json.dumps(rebuilt_atoms, sort_keys=True):
                raise ValueError(f"snapshot derived atoms differ from exact source bytes: {source}")
        if corpus.content_digest() != snapshot.get("content_digest"):
            raise ValueError("snapshot corpus digest mismatch")
        if corpus.manifest_verified:
            expected = cls.load(source_commit=corpus.source_baseline_commit)
            expected_digests = {
                source: document.raw_sha256 for source, document in expected.documents.items()
            }
            restored_digests = {
                source: document.raw_sha256 for source, document in corpus.documents.items()
            }
            if (
                corpus.manifest_digest != expected.manifest_digest
                or restored_digests != expected_digests
            ):
                raise ValueError("snapshot exact-baseline claim differs from immutable manifest")
        return corpus

    def simulate_virtual_mutation(
        self, source: str, text: str = "VIRTUAL_MUTATION"
    ) -> Dict[str, object]:
        if source not in self.documents:
            raise KeyError(source)
        mutated = self.raw_documents()
        before_raw_sha256 = self.documents[source].raw_sha256
        separator = b"" if mutated[source].endswith((b"\n", b"\r")) else b"\n"
        mutated[source] = mutated[source] + separator + text.encode("utf-8") + b"\n"
        after_raw_sha256 = hashlib.sha256(mutated[source]).hexdigest()
        affected = [
            view
            for view, dependencies in VIEW_DEPENDENCIES.items()
            if dependencies == ("*",) or source in dependencies
        ]
        derived = [view for view in VIEW_DEPENDENCIES if view != "RAW_CORPUS"]
        affected_derived = [view for view in affected if view != "RAW_CORPUS"]
        return {
            "source": source,
            "before_digest": self.content_digest(),
            "after_digest": _corpus_digest(mutated),
            "before_raw_sha256": before_raw_sha256,
            "after_raw_sha256": after_raw_sha256,
            "affected_views": affected,
            "dependency_closure": affected,
            "invalidation_radius": len(affected_derived) / len(derived) if derived else 0.0,
            "recovery": "DISCARD_VIRTUAL_MUTATION_RESTORES_PINNED_SOURCE",
        }

    def materialize_view(
        self, name: str, registry: Optional[TransformRegistry] = None
    ) -> Tuple[List[MemoryAtom], DerivationReceipt]:
        if name == "RAW_CORPUS":
            raise ValueError("RAW_CORPUS is authoritative and needs no derived-view receipt")
        registry = registry or default_transform_registry()
        definition = registry.direct("RAW_CORPUS", name)
        atoms = self.view(name)
        output_digest = sha256_json([asdict(atom) for atom in atoms])
        contract_receipt = TransformationReceipt.create(
            definition=definition,
            input_digest=self.content_digest(),
            output_digest=output_digest,
            parameters={"view": name},
            validation_results={
                "SOURCE_MANIFEST": "PASS" if self.manifest_verified else "UNPINNED",
                "DETERMINISTIC_OUTPUT": "PASS",
            },
        )
        losses = list(contract_receipt.declared_losses)
        losses.extend(
            f"{dimension}:{grade}"
            for dimension, grade in sorted(contract_receipt.loss_manifest.items())
        )
        receipt_body = {
            "view": name,
            "source_digest": contract_receipt.input_digest,
            "target_digest": contract_receipt.output_digest,
            "view_definition_digest": contract_receipt.definition_digest,
            "parameter_digest": contract_receipt.parameter_digest,
            "preservation": dict(contract_receipt.preservation),
            "losses": tuple(losses),
            "validation_result": "CONTRACT_CHECKED",
            "reversible": contract_receipt.reversible,
            "dependencies": contract_receipt.dependencies,
            "introduced_interpretation": contract_receipt.introduced_interpretation,
            "cost_class": contract_receipt.cost_class,
        }
        receipt = DerivationReceipt(receipt_id=sha256_json(receipt_body), **receipt_body)
        return atoms, receipt


def default_transform_registry() -> TransformRegistry:
    contract_ids = {
        "HISTORY_ORDER_INDEX": "chronology-index-v1",
        "CURRENT_STATE_VIEW": "current-state-view-v1",
        "OPEN_QUESTION_VIEW": "open-question-view-v1",
        "MODEL_FAMILY_VIEW": "model-family-view-v1",
        "LIFECYCLE_VIEW": "lifecycle-view-v1",
        "CORE_PRINCIPLES_VIEW": "core-principles-view-v1",
    }
    definitions: List[TransformDefinition] = []
    for view, dependencies in VIEW_DEPENDENCIES.items():
        if view == "RAW_CORPUS":
            continue
        preservation: Dict[str, str] = {
            "source_bytes": "ANCHORED",
            "source_anchor": "EXACT",
            "provenance": "ANCHORED",
            "epistemic_class": "VIEW_DEPENDENT",
            "transformation_semantics": "NON_RECOVERABLE",
        }
        if view == "HISTORY_ORDER_INDEX":
            preservation["history"] = "EXACT"
        elif view == "OPEN_QUESTION_VIEW":
            preservation["unknown_open"] = "ANCHORED"
        elif view == "CORE_PRINCIPLES_VIEW":
            preservation["principles"] = "ANCHORED"
        definitions.append(
            TransformDefinition(
                transform_id=contract_ids[view],
                version="1",
                input_view="RAW_CORPUS",
                output_view=view,
                preservation=preservation,
                deterministic=True,
                reversible="SOURCE_ANCHORED_ONLY",
                preconditions=("PINNED_OR_EXPLICIT_SOURCE",),
                dependencies=dependencies,
                declared_losses=("UNSELECTED_SOURCE_LINES",),
                introduced_interpretation=(f"{view}_SELECTION_POLICY",),
                cost_class="LINEAR_IN_DEPENDENT_SOURCE_ATOMS",
            )
        )
    return TransformRegistry(definitions)


class Router:
    def __init__(self, registry: Optional[TransformRegistry] = None):
        self.registry = registry or default_transform_registry()
        self.planner = ViewPlanner(self.registry)

    def route(
        self,
        situation: SituationFingerprint,
        model: CurrentModelState,
        lifecycle: LifecycleContext,
    ) -> RoutePlan:
        situation.validate()
        intent = situation.intent.strip().lower()
        known_intent = intent in INTENT_TO_VIEWS
        target_views = list(INTENT_TO_VIEWS.get(intent, ("RAW_CORPUS",)))
        validations = [
            "PROVENANCE_PRESERVATION",
            "SOURCE_DIGEST_CHECK",
            "EXACT_BASELINE_MANIFEST_CHECK",
            "CORE_PRINCIPLE_REVIEW",
        ]
        notes: List[str] = []
        unmet: List[str] = []
        decision_state = "ROUTE_CANDIDATE"
        paths: Dict[str, List[str]] = {}
        losses: Dict[str, Dict[str, str]] = {}
        transform_contracts: List[str] = []

        if not model.exact_baseline_verified:
            decision_state = "REVIEW_REQUIRED"
            notes.append("UNPINNED_SOURCE: exact baseline authority not verified")
            unmet.append("exact_baseline:EXACT:UNVERIFIED")
        if not known_intent:
            decision_state = "REVIEW_REQUIRED"
            notes.append("UNKNOWN_INTENT: no model commitment inferred")

        if situation.require_exact_metric:
            decision_state = "REVIEW_REQUIRED"
            validations.append("EXTERNAL_METRIC_SOURCE_REQUIRED")
            notes.append("v0.1 memo authority has no exact metric/clock anchor")
            unmet.append("metric:EXACT:NO_AUTHORITATIVE_ANCHOR")
        if situation.unknowns:
            decision_state = "REVIEW_REQUIRED"
            notes.append("UNKNOWN_FIELDS_PRESERVED: " + ", ".join(situation.unknowns))

        lifecycle_phase = lifecycle.phase.lower()
        if lifecycle_phase in {
            "mutate",
            "compose",
            "split",
            "merge",
            "migrate",
            "recover",
            "successor",
            "retire",
        }:
            if "LIFECYCLE_VIEW" not in target_views:
                target_views.append("LIFECYCLE_VIEW")
            validations.extend(
                [
                    "ROUND_TRIP_BYTE_CHECK",
                    "DEPENDENCY_INVALIDATION_CHECK",
                    "MUTATION_LINEAGE_CHECK",
                    "LOSS_RECEIPT_CHECK",
                ]
            )
        if lifecycle.rollback_required:
            validations.append("ROLLBACK_OR_COMPENSATION_PLAN")

        for target in (target_views if known_intent else ()):
            plan = self.planner.plan(
                QueryContract(
                    question=intent,
                    target_view=target,
                    required_preservation={
                        key: value.upper() for key, value in situation.preservation.items()
                    },
                    lifecycle=lifecycle.phase,
                )
            )
            paths[target] = list(plan.transformation_path)
            losses[target] = dict(plan.loss_manifest)
            transform_contracts.extend(
                item.rsplit("@", 1)[0] for item in plan.transformation_path
            )
            validations.extend(plan.validation_requirements)
            notes.extend(plan.notes)
            if plan.decision_state != "ROUTE_CANDIDATE":
                decision_state = "REVIEW_REQUIRED"
                unmet.extend(
                    f"{dimension}:{grade.upper()}:NO_ADMISSIBLE_PATH"
                    for dimension, grade in situation.preservation.items()
                )

        notes.append("v0.1 does not auto-PASS natural-language Core Principles")
        return RoutePlan(
            decision_state=decision_state,
            target_views=sorted(set(target_views)),
            transform_contracts=sorted(set(transform_contracts)),
            transformation_paths=paths,
            loss_manifest=losses,
            unmet_demands=sorted(set(unmet)),
            required_validations=sorted(set(validations)),
            principle_gate_state="REVIEW_REQUIRED",
            notes=sorted(set(notes)),
        )


def _parse_preserve(items: Iterable[str]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise ValueError("--preserve expects key=LEVEL")
        key, value = item.split("=", 1)
        result[key.strip()] = value.strip().upper()
    return result


def _load_corpus(args: argparse.Namespace) -> MemoryCorpus:
    if args.source_mode == "worktree":
        return MemoryCorpus.load(
            args.memory_root or DEFAULT_MEMORY_ROOT,
            source_mode="worktree",
        )
    if args.memory_root is not None:
        raise ValueError("--memory-root requires --source-mode worktree")
    return MemoryCorpus.load(source_commit=args.source_commit, manifest_path=args.manifest)


def _initialize_ledger(corpus: MemoryCorpus, root: Path, branch: str, actor: str) -> Dict[str, object]:
    root = Path(root)
    ledger_path = root / "ledger.jsonl"
    refs_path = root / "refs.json"
    if ledger_path.exists() or refs_path.exists():
        raise FileExistsError(f"lifecycle repository already exists: {root}")
    ledger = EpistemicLedger(path=ledger_path)
    for source, document in sorted(corpus.documents.items()):
        ledger.append(
            "TRANSFORM",
            actor,
            {
                "operation": "INGEST_ARTIFACT",
                "source_digest": document.raw_sha256,
                "target_digest": document.raw_sha256,
                "contract_digest": sha256_json(
                    {
                        "operation": "INGEST_ARTIFACT",
                        "preservation": {"source_bytes": "EXACT", "provenance": "EXACT"},
                    }
                ),
                "losses": [],
                "source": source,
                "source_sha256": document.raw_sha256,
                "raw_base64": base64.b64encode(document.raw_bytes).decode("ascii"),
                "git_blob_oid": document.git_blob_oid,
                "source_baseline_commit": corpus.source_baseline_commit,
                "preservation": {"source_bytes": "EXACT", "provenance": "EXACT"},
            },
        )
    repository = LifecycleRepository(root)
    commit = repository.initialize(branch=branch)
    return {
        "root": str(root),
        "branch": branch,
        "commit_id": commit.commit_id,
        "event_count": len(repository.ledger.events),
        "state_root": repository.ledger.state_root(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Byul v0.1 memo authority and lifecycle model")
    parser.add_argument(
        "--memory-root",
        type=Path,
        default=None,
        help="explicit unpinned working-tree source; default reads the pinned Git tree",
    )
    parser.add_argument(
        "--source-mode",
        choices=("exact_git_tree", "worktree"),
        default="exact_git_tree",
    )
    parser.add_argument("--source-commit", default=SOURCE_BASELINE_COMMIT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary")
    sub.add_parser("verify-baseline")

    route_parser = sub.add_parser("route")
    route_parser.add_argument("--intent", required=True)
    route_parser.add_argument("--lifecycle", default="operate")
    route_parser.add_argument("--preserve", action="append", default=[])
    route_parser.add_argument("--exact-metric", action="store_true")
    route_parser.add_argument("--unknown", action="append", default=[])

    mutation_parser = sub.add_parser("simulate-mutation")
    mutation_parser.add_argument("--source", required=True)
    mutation_parser.add_argument("--text", default="VIRTUAL_MUTATION")

    export_parser = sub.add_parser("export")
    export_parser.add_argument("--out", type=Path, required=True)

    import_parser = sub.add_parser("verify-import")
    import_parser.add_argument("--input", type=Path, required=True)
    import_parser.add_argument("--restore-dir", type=Path)

    receipt_parser = sub.add_parser("materialize-view", aliases=["materialize"])
    receipt_parser.add_argument(
        "--name", "--view", dest="view", required=True, choices=sorted(VIEW_DEPENDENCIES)
    )

    init_parser = sub.add_parser("ledger-init")
    init_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    init_parser.add_argument("--branch", default="main")
    init_parser.add_argument("--actor", default="BYUL_V0.1")

    claim_parser = sub.add_parser("ledger-claim")
    claim_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    claim_parser.add_argument("--branch", default="main")
    claim_parser.add_argument("--claim-id")
    claim_parser.add_argument("--text", required=True)
    claim_parser.add_argument(
        "--epistemic-class", "--class", dest="epistemic_class", required=True
    )
    claim_parser.add_argument("--actor", required=True)
    claim_parser.add_argument("--context", default="GLOBAL_UNSPECIFIED")

    state_parser = sub.add_parser("ledger-state")
    state_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    state_parser.add_argument("--branch", default="main")

    split_parser = sub.add_parser("ledger-split", aliases=["lifecycle-split"])
    split_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    split_parser.add_argument("--source", required=True)
    split_parser.add_argument("--target", required=True)

    merge_parser = sub.add_parser("ledger-merge", aliases=["lifecycle-merge"])
    merge_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    merge_parser.add_argument("--left", required=True)
    merge_parser.add_argument("--right", required=True)
    merge_parser.add_argument("--target", required=True)

    migrate_parser = sub.add_parser("ledger-migrate", aliases=["lifecycle-migrate"])
    migrate_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    migrate_parser.add_argument("--source", required=True)
    migrate_parser.add_argument("--target", required=True)
    migrate_parser.add_argument("--schema-version", type=int, required=True)
    migrate_parser.add_argument("--transformer-version", required=True)

    recover_parser = sub.add_parser("ledger-recover", aliases=["lifecycle-recover"])
    recover_parser.add_argument("--root", "--repo", dest="root", type=Path, required=True)
    recover_parser.add_argument("--branch", default="main")

    args = parser.parse_args()

    if args.command in {
        "summary",
        "verify-baseline",
        "route",
        "simulate-mutation",
        "export",
        "materialize-view",
        "materialize",
        "ledger-init",
    }:
        corpus = _load_corpus(args)

    if args.command == "summary":
        state = corpus.model_state()
        output = {
            **asdict(state),
            "history_items": len(corpus.history_items()),
            "history_edges": len(corpus.history_edges()),
            "history_acyclic": corpus.history_is_acyclic(),
            "open_atoms": len(corpus.view("OPEN_QUESTION_VIEW")),
            "core_principle_atoms": len(corpus.view("CORE_PRINCIPLES_VIEW")),
        }
    elif args.command == "verify-baseline":
        output = {
            "state": "VERIFIED" if corpus.manifest_verified else "UNPINNED",
            "source_baseline_commit": corpus.source_baseline_commit,
            "manifest_digest": corpus.manifest_digest,
            "content_digest": corpus.content_digest(),
            "document_count": len(corpus.documents),
            "files": {
                name: document.raw_sha256 for name, document in sorted(corpus.documents.items())
            },
        }
    elif args.command == "route":
        situation = SituationFingerprint(
            intent=args.intent,
            preservation=_parse_preserve(args.preserve),
            require_exact_metric=args.exact_metric,
            unknowns=args.unknown,
        )
        lifecycle = LifecycleContext(phase=args.lifecycle)
        plan = Router().route(situation, corpus.model_state(), lifecycle)
        output = {
            "situation": asdict(situation),
            "model": asdict(corpus.model_state()),
            "lifecycle": asdict(lifecycle),
            "route_plan": asdict(plan),
        }
    elif args.command == "simulate-mutation":
        output = corpus.simulate_virtual_mutation(args.source, args.text)
    elif args.command == "export":
        snapshot = corpus.snapshot()
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
        restored = MemoryCorpus.from_snapshot(snapshot)
        output = {
            "written": str(args.out),
            "content_digest": corpus.content_digest(),
            "roundtrip_digest": restored.content_digest(),
            "byte_exact": corpus.content_digest() == restored.content_digest(),
        }
    elif args.command == "verify-import":
        snapshot = json.loads(args.input.read_text(encoding="utf-8"))
        restored = MemoryCorpus.from_snapshot(snapshot)
        output = {
            "verified": True,
            "source_baseline_commit": restored.source_baseline_commit,
            "content_digest": restored.content_digest(),
            "document_count": len(restored.documents),
        }
        if args.restore_dir is not None:
            output["restored_sha256"] = restored.restore_source_bytes(args.restore_dir)
    elif args.command in {"materialize-view", "materialize"}:
        atoms, receipt = corpus.materialize_view(args.view)
        output = {"view": args.view, "atom_count": len(atoms), "receipt": asdict(receipt)}
    elif args.command == "ledger-init":
        output = _initialize_ledger(corpus, args.root, args.branch, args.actor)
    elif args.command == "ledger-claim":
        repository = LifecycleRepository(args.root)
        claim_id = args.claim_id or _sha256(
            f"{args.text}|{args.epistemic_class}|{args.actor}|{args.context}"
        )[:24]
        event = repository.ledger.append_claim(
            ClaimPacket(
                claim_id=claim_id,
                exact_text=args.text,
                epistemic_class=args.epistemic_class,
                actor=args.actor,
                context_id=args.context,
            )
        )
        commit = repository.commit_events(args.branch, (event.event_id,), operation="MUTATE")
        output = {"event_id": event.event_id, "claim_id": claim_id, "commit_id": commit.commit_id}
    elif args.command == "ledger-state":
        repository = LifecycleRepository(args.root)
        head = repository.head(args.branch)
        output = {
            "branch": args.branch,
            "head": head.commit_id,
            "state": repository.ledger.fold(head.event_ids),
        }
    elif args.command in {"ledger-split", "lifecycle-split"}:
        repository = LifecycleRepository(args.root)
        commit = repository.split(args.source, args.target)
        output = asdict(commit)
    elif args.command in {"ledger-merge", "lifecycle-merge"}:
        repository = LifecycleRepository(args.root)
        commit = repository.merge(args.left, args.right, args.target)
        output = asdict(commit)
    elif args.command in {"ledger-migrate", "lifecycle-migrate"}:
        repository = LifecycleRepository(args.root)
        commit = repository.migrate(
            args.source,
            args.target,
            args.schema_version,
            args.transformer_version,
        )
        output = asdict(commit)
    elif args.command in {"ledger-recover", "lifecycle-recover"}:
        output = LifecycleRepository(args.root).recover(args.branch)
    else:
        raise AssertionError(args.command)

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
