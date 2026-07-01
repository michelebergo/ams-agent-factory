from __future__ import annotations

import json
from pathlib import Path
import typer
import yaml
from rich import print

from ams_agent_factory.core.model_router import ModelRouter
from ams_agent_factory.agents.verifier import Verifier
from ams_agent_factory.agents.optimizer import BoundedOptimizer
from ams_agent_factory.tools.autosearch import AutoSearch

app = typer.Typer()
models_app = typer.Typer()
app.add_typer(models_app, name="models")


@models_app.command("show-policy")
def show_policy() -> None:
    router = ModelRouter("configs/providers.yaml", "configs/model_policy.yaml")
    for agent in router.policy.get("agents", {}):
        choice = router.choose(agent)
        print(f"{agent}: {choice.alias} ({choice.cost_class})")


@app.command()
def verify(requirements_yaml: Path, measurement_json: Path) -> None:
    reqs = yaml.safe_load(requirements_yaml.read_text())
    meas = json.loads(measurement_json.read_text())
    for result in Verifier().verify(reqs, meas):
        print(result)


@app.command()
def optimize(surface_yaml: Path, measurement_json: Path) -> None:
    surface = yaml.safe_load(surface_yaml.read_text())
    meas = json.loads(measurement_json.read_text())
    print(BoundedOptimizer().propose(surface, meas))


@app.command()
def search(query: str, depth: int = 2) -> None:
    for hit in AutoSearch().search(query, depth=depth):
        print(hit)
