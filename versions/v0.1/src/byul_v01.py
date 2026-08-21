#!/usr/bin/env python3
"""Byul v0.1 — memo-driven experimental model.

Primary data: versions/v0.01/memory/*.md
Stdlib only. Non-normative, not validated.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

SOURCE_BASELINE_COMMIT = "2a4529b69bc237125a1f012835d7a9b78ce3fec9"
VERSIONS_DIR = Path(__file__).resolve().parents[2]
DEFAULT_MEMORY_ROOT = VERSIONS_DIR / "v0.01" / "memory"

PRESERVATION_LEVELS = {
    "EXACT",
    "ANCHORED",
    "SEMANTIC",
    "STATISTICAL",
    "VIEW_DEPENDENT",
    "NON_RECOVERABLE",
    "UNKNOWN",
}

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


def _norm(text: str) -> str:
    return " ".join(text.strip().split())


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
    line_no: int
    section: str
    kind: str
    text: str
    tags: Tuple[str, ...] = ()


@dataclass
class MemoryDocument:
    source: str
    raw_sha256: str
    atoms: List[MemoryAtom] = field(default_factory=list)


@dataclass
class SituationFingerprint:
    intent: str
    preservation: Dict[str, str] = field(default_factory=dict)
    require_exact_metric: bool = False
    unknowns: List[str] = field(default_factory=list)

    def validate(self) -> None:
        bad = {v for v in self.preservation.values() if v not in PRESERVATION_LEVELS}
        if bad:
            raise ValueError(f"unknown preservation levels: {sorted(bad)}")


@dataclass(frozen=True)
class CurrentModelState:
    source_baseline_commit: str
    content_digest: str
    document_count: int
    atom_count: int
    available_views: Tuple[str, ...]


@dataclass(frozen=True)
class LifecycleContext:
    phase: str
    mutation_scope: str = "UNKNOWN"


@dataclass
class RoutePlan:
    decision_state: str
    target_views: List[str]
    required_validations: List[str]
    principle_gate_state: str
    notes: List[str]


class MemoryCorpus:
    def __init__(self, root: Path, documents: Dict[str, MemoryDocument]):
        self.root = root
        self.documents = documents

    @classmethod
    def load(cls, root: Path = DEFAULT_MEMORY_ROOT) -> "MemoryCorpus":
        root = Path(root)
        documents: Dict[str, MemoryDocument] = {}
        for path in sorted(root.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            documents[path.name] = MemoryDocument(
                source=path.name,
                raw_sha256=hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                atoms=_parse_markdown(path.name, raw),
            )
        if not documents:
            raise FileNotFoundError(f"no markdown memory files found under {root}")
        return cls(root, documents)

    def atoms(self) -> List[MemoryAtom]:
        return [atom for name in sorted(self.documents) for atom in self.documents[name].atoms]

    def content_digest(self) -> str:
        payload = "\n".join(
            f"{a.source}|{_norm(a.text)}" for a in self.atoms() if _norm(a.text)
        )
        return _sha256(payload)

    def model_state(self) -> CurrentModelState:
        return CurrentModelState(
            source_baseline_commit=SOURCE_BASELINE_COMMIT,
            content_digest=self.content_digest(),
            document_count=len(self.documents),
            atom_count=len(self.atoms()),
            available_views=tuple(VIEW_DEPENDENCIES.keys()),
        )

    def history_items(self) -> List[MemoryAtom]:
        doc = self.documents.get("08_CHANNEL_CHRONOLOGY.md")
        if not doc:
            return []
        return [a for a in doc.atoms if a.kind == "numbered"]

    def history_edges(self) -> List[Tuple[str, str]]:
        items = self.history_items()
        return [(items[i].atom_id, items[i + 1].atom_id) for i in range(len(items) - 1)]

    def history_is_acyclic(self) -> bool:
        edges = self.history_edges()
        graph: Dict[str, List[str]] = {}
        for a, b in edges:
            graph.setdefault(a, []).append(b)
        visiting, visited = set(), set()

        def dfs(node: str) -> bool:
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nxt in graph.get(node, []):
                if not dfs(nxt):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        return all(dfs(n) for n in list(graph))

    def view(self, name: str) -> List[MemoryAtom]:
        if name not in VIEW_DEPENDENCIES:
            raise KeyError(name)
        deps = VIEW_DEPENDENCIES[name]
        atoms = self.atoms() if deps == ("*",) else [
            a for source in deps if source in self.documents for a in self.documents[source].atoms
        ]
        if name == "HISTORY_ORDER_INDEX":
            return self.history_items()
        if name == "OPEN_QUESTION_VIEW":
            return [a for a in atoms if "OPEN" in a.tags or "미결" in a.text or "Open Question" in a.text]
        if name == "CURRENT_STATE_VIEW":
            needles = ("current", "현재", "strongest", "현행", "direction", "방향")
            return [a for a in atoms if any(n.lower() in a.text.lower() for n in needles)]
        return atoms

    def snapshot(self) -> Dict[str, object]:
        return {
            "source_baseline_commit": SOURCE_BASELINE_COMMIT,
            "content_digest": self.content_digest(),
            "documents": {
                name: {
                    "raw_sha256": doc.raw_sha256,
                    "atoms": [asdict(a) for a in doc.atoms],
                }
                for name, doc in sorted(self.documents.items())
            },
        }

    @staticmethod
    def snapshot_content_digest(snapshot: Mapping[str, object]) -> str:
        docs = snapshot["documents"]
        rows: List[str] = []
        assert isinstance(docs, Mapping)
        for source in sorted(docs):
            doc = docs[source]
            assert isinstance(doc, Mapping)
            atoms = doc["atoms"]
            assert isinstance(atoms, Sequence)
            for atom in atoms:
                assert isinstance(atom, Mapping)
                rows.append(f"{source}|{_norm(str(atom['text']))}")
        return _sha256("\n".join(rows))

    def simulate_virtual_mutation(self, source: str, text: str = "VIRTUAL_MUTATION") -> Dict[str, object]:
        if source not in self.documents:
            raise KeyError(source)
        mutated = copy.deepcopy(self.snapshot())
        docs = mutated["documents"]
        assert isinstance(docs, dict)
        atoms = docs[source]["atoms"]
        next_line = max((int(a["line_no"]) for a in atoms), default=0) + 1
        atoms.append({
            "atom_id": _sha256(f"{source}|virtual|{text}"),
            "source": source,
            "line_no": next_line,
            "section": "VIRTUAL_MUTATION",
            "kind": "text",
            "text": text,
            "tags": (),
        })
        affected = [
            view for view, deps in VIEW_DEPENDENCIES.items()
            if deps == ("*",) or source in deps
        ]
        derived = [v for v in VIEW_DEPENDENCIES if v != "RAW_CORPUS"]
        affected_derived = [v for v in affected if v != "RAW_CORPUS"]
        return {
            "source": source,
            "before_digest": self.content_digest(),
            "after_digest": self.snapshot_content_digest(mutated),
            "affected_views": affected,
            "invalidation_radius": (len(affected_derived) / len(derived)) if derived else 0.0,
            "recovery": "DISCARD_VIRTUAL_MUTATION_RESTORES_SOURCE_SNAPSHOT",
        }


def _parse_markdown(source: str, raw: str) -> List[MemoryAtom]:
    atoms: List[MemoryAtom] = []
    section = "ROOT"
    in_code = False
    seen: Dict[str, int] = {}
    for line_no, line in enumerate(raw.splitlines(), start=1):
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
        atom_id = _sha256(f"{source}|{normalized}|{occurrence}")[:20]
        atoms.append(MemoryAtom(
            atom_id=atom_id,
            source=source,
            line_no=line_no,
            section=section,
            kind=kind,
            text=stripped,
            tags=_explicit_tags(stripped),
        ))
    return atoms


class Router:
    def route(
        self,
        situation: SituationFingerprint,
        model: CurrentModelState,
        lifecycle: LifecycleContext,
    ) -> RoutePlan:
        situation.validate()
        intent = situation.intent.strip().lower()
        target = list(INTENT_TO_VIEWS.get(intent, ("RAW_CORPUS", "CURRENT_STATE_VIEW")))
        validations = ["PROVENANCE_PRESERVATION", "SOURCE_DIGEST_CHECK", "CORE_PRINCIPLE_REVIEW"]
        notes: List[str] = []
        decision_state = "ROUTE_CANDIDATE"

        if intent not in INTENT_TO_VIEWS:
            decision_state = "REVIEW_REQUIRED"
            notes.append("UNKNOWN_INTENT: no model commitment inferred")

        exact_history = situation.preservation.get("history") == "EXACT"
        if exact_history and "HISTORY_ORDER_INDEX" not in target:
            target.append("HISTORY_ORDER_INDEX")
            validations.append("HISTORY_ORDER_PRESERVATION")

        if situation.require_exact_metric:
            decision_state = "REVIEW_REQUIRED"
            validations.append("EXTERNAL_METRIC_SOURCE_REQUIRED")
            notes.append("v0.1 memo model has no authoritative metric/clock source")

        if situation.unknowns:
            decision_state = "REVIEW_REQUIRED"
            notes.append("UNKNOWN_FIELDS_PRESERVED: " + ", ".join(situation.unknowns))

        if lifecycle.phase.lower() in {"mutate", "compose", "split", "merge", "migrate", "recover", "successor"}:
            if "LIFECYCLE_VIEW" not in target:
                target.append("LIFECYCLE_VIEW")
            validations.extend([
                "ROUND_TRIP_CONTENT_CHECK",
                "INVALIDATION_RADIUS_CHECK",
                "MUTATION_LINEAGE_CHECK",
            ])

        principle_state = "REVIEW_REQUIRED"
        notes.append("v0.1 does not auto-PASS natural-language Core Principles")

        return RoutePlan(
            decision_state=decision_state,
            target_views=sorted(set(target)),
            required_validations=sorted(set(validations)),
            principle_gate_state=principle_state,
            notes=notes,
        )


def _parse_preserve(items: Iterable[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise ValueError("--preserve expects key=LEVEL")
        key, value = item.split("=", 1)
        out[key.strip()] = value.strip().upper()
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Byul v0.1 memo-driven experimental model")
    parser.add_argument("--memory-root", type=Path, default=DEFAULT_MEMORY_ROOT)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary")

    route_p = sub.add_parser("route")
    route_p.add_argument("--intent", required=True)
    route_p.add_argument("--lifecycle", default="operate")
    route_p.add_argument("--preserve", action="append", default=[])
    route_p.add_argument("--exact-metric", action="store_true")
    route_p.add_argument("--unknown", action="append", default=[])

    mut_p = sub.add_parser("simulate-mutation")
    mut_p.add_argument("--source", required=True)
    mut_p.add_argument("--text", default="VIRTUAL_MUTATION")

    export_p = sub.add_parser("export")
    export_p.add_argument("--out", type=Path, required=True)

    args = parser.parse_args()
    corpus = MemoryCorpus.load(args.memory_root)

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
    elif args.command == "route":
        situation = SituationFingerprint(
            intent=args.intent,
            preservation=_parse_preserve(args.preserve),
            require_exact_metric=args.exact_metric,
            unknowns=args.unknown,
        )
        plan = Router().route(
            situation,
            corpus.model_state(),
            LifecycleContext(phase=args.lifecycle),
        )
        output = {
            "situation": asdict(situation),
            "model": asdict(corpus.model_state()),
            "lifecycle": asdict(LifecycleContext(phase=args.lifecycle)),
            "route_plan": asdict(plan),
        }
    elif args.command == "simulate-mutation":
        output = corpus.simulate_virtual_mutation(args.source, args.text)
    elif args.command == "export":
        snapshot = corpus.snapshot()
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
        output = {
            "written": str(args.out),
            "content_digest": corpus.content_digest(),
            "roundtrip_digest": MemoryCorpus.snapshot_content_digest(snapshot),
        }
    else:
        raise AssertionError(args.command)

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
