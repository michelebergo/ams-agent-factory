from __future__ import annotations

from typing import Any


class BoundedOptimizer:
    def propose(self, surface: dict[str, Any], measurements: dict[str, Any]) -> dict[str, Any]:
        pm = measurements.get("measurements", {}).get("phase_margin_deg")
        proposal = {"action": "hold", "reason": "No failing metric detected or no rule available", "parameter_changes": {}}
        if pm is not None and pm < 60:
            proposal = {
                "action": "adjust_compensation",
                "reason": "Phase margin below 60 deg",
                "parameter_changes": {"ccomp_f": "+15%", "rzero_ohm": "evaluate_zero_resistor"},
                "risk": "May worsen load transient response"
            }
        return proposal
