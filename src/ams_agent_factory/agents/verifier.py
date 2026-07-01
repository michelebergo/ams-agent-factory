from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class VerificationResult:
    requirement_id: str
    metric: str
    status: str
    measured: float | None
    required: dict[str, float]


class Verifier:
    def verify(self, requirements: dict[str, Any], measurements: dict[str, Any]) -> list[VerificationResult]:
        measured = measurements.get("measurements", {})
        results: list[VerificationResult] = []
        for req in requirements.get("requirements", []):
            metric = req["metric"]
            value = measured.get(metric)
            status = "PASS"
            if value is None:
                status = "NOT_RUN"
            if value is not None and "min" in req and value < req["min"]:
                status = "FAIL"
            if value is not None and "max" in req and value > req["max"]:
                status = "FAIL"
            results.append(VerificationResult(req["id"], metric, status, value, {k: req[k] for k in ("min", "max") if k in req}))
        return results
