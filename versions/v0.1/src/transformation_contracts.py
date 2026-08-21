#!/usr/bin/env python3
"""Field-level preservation contracts and safe view planning for Byul v0.1."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


PRESERVATION_LEVELS = {
    "EXACT",
    "SEMANTIC",
    "ANCHORED",
    "APPROXIMATE",
    "STATISTICAL",
    "VIEW_DEPENDENT",
    "NON_RECOVERABLE",
    "UNKNOWN",
}

_GRADE_RANK = {
    "UNKNOWN": 0,
    "NON_RECOVERABLE": 1,
    "VIEW_DEPENDENT": 2,
    "APPROXIMATE": 3,
    "STATISTICAL": 3,
    "ANCHORED": 4,
    "SEMANTIC": 5,
    "EXACT": 6,
}


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value: object) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def preservation_satisfies(actual: str, required: str) -> bool:
    """Return whether an actual grade satisfies a required grade.

    ANCHORED and SEMANTIC are intentionally not interchangeable. UNKNOWN always
    fails closed, including when a caller asks for UNKNOWN.
    """

    actual = actual.upper()
    required = required.upper()
    if actual not in PRESERVATION_LEVELS or required not in PRESERVATION_LEVELS:
        raise ValueError(f"unknown preservation grade: {actual} / {required}")
    if actual == "UNKNOWN":
        return False
    if required == "EXACT":
        return actual == "EXACT"
    if required == "SEMANTIC":
        return actual in {"EXACT", "SEMANTIC"}
    if required == "ANCHORED":
        return actual in {"EXACT", "ANCHORED"}
    if required in {"APPROXIMATE", "STATISTICAL"}:
        return actual in {
            "EXACT",
            "SEMANTIC",
            "ANCHORED",
            "APPROXIMATE",
            "STATISTICAL",
        }
    if required == "VIEW_DEPENDENT":
        return actual not in {"UNKNOWN", "NON_RECOVERABLE"}
    if required == "NON_RECOVERABLE":
        return True
    return False


def weaker_grade(left: str, right: str) -> str:
    left = left.upper()
    right = right.upper()
    if left not in PRESERVATION_LEVELS or right not in PRESERVATION_LEVELS:
        raise ValueError(f"unknown preservation grade: {left} / {right}")
    if _GRADE_RANK[left] < _GRADE_RANK[right]:
        return left
    if _GRADE_RANK[right] < _GRADE_RANK[left]:
        return right
    if left == right:
        return left
    # Equal-rank distinct grades cannot safely substitute for one another.
    return "VIEW_DEPENDENT"


@dataclass(frozen=True)
class TransformDefinition:
    transform_id: str
    version: str
    input_view: str
    output_view: str
    preservation: Mapping[str, str]
    deterministic: bool = True
    reversible: str = "NONE"
    preconditions: Tuple[str, ...] = ()
    dependencies: Tuple[str, ...] = ()
    declared_losses: Tuple[str, ...] = ()
    introduced_interpretation: Tuple[str, ...] = ()
    cost_class: str = "UNMEASURED"

    def __post_init__(self) -> None:
        if not all((self.transform_id, self.version, self.input_view, self.output_view)):
            raise ValueError("transform identity and views are required")
        bad = {grade.upper() for grade in self.preservation.values()} - PRESERVATION_LEVELS
        if bad:
            raise ValueError(f"unknown preservation levels: {sorted(bad)}")

    def to_dict(self) -> Dict[str, object]:
        return {
            "transform_id": self.transform_id,
            "version": self.version,
            "input_view": self.input_view,
            "output_view": self.output_view,
            "preservation": {key: value.upper() for key, value in sorted(self.preservation.items())},
            "deterministic": self.deterministic,
            "reversible": self.reversible,
            "preconditions": list(self.preconditions),
            "dependencies": list(self.dependencies),
            "declared_losses": list(self.declared_losses),
            "introduced_interpretation": list(self.introduced_interpretation),
            "cost_class": self.cost_class,
        }

    @property
    def definition_digest(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True)
class TransformationReceipt:
    receipt_id: str
    transform_id: str
    transform_version: str
    definition_digest: str
    input_digest: str
    output_digest: str
    parameter_digest: str
    preservation: Mapping[str, str]
    loss_manifest: Mapping[str, str]
    validation_results: Mapping[str, str]
    reversible: str
    dependencies: Tuple[str, ...]
    declared_losses: Tuple[str, ...]
    introduced_interpretation: Tuple[str, ...]
    cost_class: str

    @classmethod
    def create(
        cls,
        definition: TransformDefinition,
        input_digest: str,
        output_digest: str,
        parameters: Mapping[str, object],
        validation_results: Mapping[str, str],
    ) -> "TransformationReceipt":
        preservation = {
            key: value.upper() for key, value in sorted(definition.preservation.items())
        }
        loss_manifest = {
            key: value for key, value in preservation.items() if value != "EXACT"
        }
        body = {
            "transform_id": definition.transform_id,
            "transform_version": definition.version,
            "definition_digest": definition.definition_digest,
            "input_digest": input_digest,
            "output_digest": output_digest,
            "parameter_digest": sha256_json(dict(parameters)),
            "preservation": preservation,
            "loss_manifest": loss_manifest,
            "validation_results": dict(sorted(validation_results.items())),
            "reversible": definition.reversible,
            "dependencies": definition.dependencies,
            "declared_losses": definition.declared_losses,
            "introduced_interpretation": definition.introduced_interpretation,
            "cost_class": definition.cost_class,
        }
        return cls(receipt_id=sha256_json(body), **body)


class TransformRegistry:
    def __init__(self, definitions: Iterable[TransformDefinition] = ()):
        self._definitions: Dict[Tuple[str, str], TransformDefinition] = {}
        for definition in definitions:
            self.register(definition)

    def register(self, definition: TransformDefinition) -> None:
        key = (definition.transform_id, definition.version)
        if key in self._definitions:
            raise ValueError(f"duplicate transform definition: {key}")
        self._definitions[key] = definition

    @property
    def definitions(self) -> Tuple[TransformDefinition, ...]:
        return tuple(self._definitions[key] for key in sorted(self._definitions))

    def direct(self, input_view: str, output_view: str) -> TransformDefinition:
        matches = [
            definition
            for definition in self.definitions
            if definition.input_view == input_view and definition.output_view == output_view
        ]
        if len(matches) != 1:
            raise KeyError(f"expected one transform {input_view} -> {output_view}, found {len(matches)}")
        return matches[0]

    @staticmethod
    def compose_preservation(path: Sequence[TransformDefinition]) -> Dict[str, str]:
        dimensions = sorted({key for definition in path for key in definition.preservation})
        result: Dict[str, str] = {}
        for dimension in dimensions:
            grade = "EXACT"
            for definition in path:
                grade = weaker_grade(grade, definition.preservation.get(dimension, "UNKNOWN"))
            result[dimension] = grade
        return result

    def find_path(
        self,
        input_view: str,
        output_view: str,
        required: Mapping[str, str],
        max_depth: int = 8,
    ) -> Optional[Tuple[Tuple[TransformDefinition, ...], Mapping[str, str]]]:
        if input_view == output_view:
            return (), {key: "EXACT" for key in required}
        frontier: List[Tuple[str, Tuple[TransformDefinition, ...]]] = [(input_view, ())]
        while frontier:
            view, path = frontier.pop(0)
            if len(path) >= max_depth:
                continue
            used_views = {input_view, *(definition.output_view for definition in path)}
            for definition in self.definitions:
                if definition.input_view != view or definition.output_view in used_views:
                    continue
                new_path = (*path, definition)
                composed = self.compose_preservation(new_path)
                if definition.output_view == output_view and all(
                    preservation_satisfies(composed.get(key, "UNKNOWN"), grade)
                    for key, grade in required.items()
                ):
                    return tuple(new_path), composed
                frontier.append((definition.output_view, tuple(new_path)))
        return None


@dataclass(frozen=True)
class QueryContract:
    question: str
    target_view: str
    required_preservation: Mapping[str, str] = field(default_factory=dict)
    lifecycle: str = "OPERATE"
    max_transform_depth: int = 8


@dataclass(frozen=True)
class ViewPlan:
    decision_state: str
    source_view: str
    target_view: str
    transformation_path: Tuple[str, ...]
    preservation: Mapping[str, str]
    loss_manifest: Mapping[str, str]
    validation_requirements: Tuple[str, ...]
    notes: Tuple[str, ...]


class ViewPlanner:
    def __init__(self, registry: TransformRegistry, source_view: str = "RAW_CORPUS"):
        self.registry = registry
        self.source_view = source_view

    def plan(self, contract: QueryContract) -> ViewPlan:
        bad = {
            grade.upper() for grade in contract.required_preservation.values()
        } - PRESERVATION_LEVELS
        if bad:
            raise ValueError(f"unknown preservation levels: {sorted(bad)}")
        found = self.registry.find_path(
            self.source_view,
            contract.target_view,
            {key: value.upper() for key, value in contract.required_preservation.items()},
            max_depth=contract.max_transform_depth,
        )
        if found is None:
            return ViewPlan(
                decision_state="REVIEW_REQUIRED",
                source_view=self.source_view,
                target_view=contract.target_view,
                transformation_path=(),
                preservation={},
                loss_manifest={
                    key: "UNSATISFIED:" + value.upper()
                    for key, value in contract.required_preservation.items()
                },
                validation_requirements=("CONTRACT_REVIEW", "DIRECT_SOURCE_ACCESS"),
                notes=("NO_ADMISSIBLE_TRANSFORMATION_PATH",),
            )
        path, preservation = found
        validations = ["FIELD_PRESERVATION_CHECK", "TRANSFORMATION_RECEIPT_CHECK"]
        if any(not definition.deterministic for definition in path):
            validations.append("NONDETERMINISTIC_OUTPUT_CAPTURE")
        return ViewPlan(
            decision_state="ROUTE_CANDIDATE",
            source_view=self.source_view,
            target_view=contract.target_view,
            transformation_path=tuple(
                f"{definition.transform_id}@{definition.version}" for definition in path
            ),
            preservation=preservation,
            loss_manifest={key: grade for key, grade in preservation.items() if grade != "EXACT"},
            validation_requirements=tuple(sorted(validations)),
            notes=(),
        )
