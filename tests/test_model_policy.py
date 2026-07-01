from pathlib import Path

from ams_agent_factory.core.model_router import ModelRouter


def test_router_default_and_escalation():
    root = Path(__file__).resolve().parents[1]
    router = ModelRouter(root / "configs/providers.yaml", root / "configs/model_policy.yaml")
    assert router.choose("sizing_agent").alias == "medium_reasoning"
    assert router.choose("sizing_agent", ["device_region_violation"]).alias == "strong_reasoning"


def test_tool_only_verifier():
    root = Path(__file__).resolve().parents[1]
    router = ModelRouter(root / "configs/providers.yaml", root / "configs/model_policy.yaml")
    assert router.choose("verifier_agent").alias == "tool_only"
