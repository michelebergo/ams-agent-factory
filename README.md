# AMS Agent Factory

A GitHub-ready scaffold for building a multi-agent Analog/Mixed-Signal IC design assistant.

The intended flow is:

```text
Jama requirements → LLM wiki memory → AutoSearch context → design/testbench agents → Spectre/Cadence tools → measured JSON → verifier → optimizer → documentation/Jama traceability
```

The system separates source of truth from LLM memory:

```text
raw/  = immutable imported source material
wiki/ = LLM-maintained synthesized memory
```

## Features

- Jama-first requirements architecture
- Karpathy-style `raw/` + `wiki/` memory system
- AutoSearch context retrieval
- Multi-model routing to optimize token and model cost
- Simulation-grounded verifier
- Bounded optimizer scaffold
- Example LDO requirement and measurement files

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Commands

```bash
amsaf models show-policy
amsaf verify examples/ldo_core/requirements.yaml examples/ldo_core/measurement_example.json
amsaf optimize examples/ldo_core/optimization_surface.yaml examples/ldo_core/measurement_example.json
pytest -q
```

## Design principle

```text
LLM proposes → deterministic EDA tools execute → simulator measures → verifier decides → human approves.
```
