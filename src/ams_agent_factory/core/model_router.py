from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import yaml


@dataclass(frozen=True)
class ModelChoice:
    alias: str
    provider: str
    model: str
    cost_class: str


class ModelRouter:
    def __init__(self, providers_path: str | Path, policy_path: str | Path):
        self.providers = yaml.safe_load(Path(providers_path).read_text())
        self.policy = yaml.safe_load(Path(policy_path).read_text())

    def choose(self, agent_name: str, escalation_signals: Iterable[str] | None = None) -> ModelChoice:
        agent_policy = self.policy.get("agents", {}).get(agent_name, {})
        alias = agent_policy.get("default", self.policy.get("default_model", "cheap_fast"))
        signals = set(escalation_signals or [])
        configured = set(agent_policy.get("escalation_signals", []))
        if signals & configured and agent_policy.get("escalate_to"):
            alias = agent_policy["escalate_to"]
        m = self.providers["models"][alias]
        return ModelChoice(alias=alias, provider=m.get("provider", "none"), model=m.get("model", "none"), cost_class=m.get("cost_class", "unknown"))
