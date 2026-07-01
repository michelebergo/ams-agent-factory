# AMS Agent Factory

Agentic framework for analog/mixed-signal IC design with Jama-driven requirements, Karpathy-style LLM wiki memory, AutoSearch retrieval, multi-model routing, and simulation-grounded verification.

This repository is generated as a practical scaffold for building agents that can:

- ingest baselined requirements from Jama,
- normalize requirements into measurable verification contracts,
- maintain a persistent `raw/` + `wiki/` memory system,
- select the right LLM model per agent to optimize cost and token usage,
- propose bounded design/sizing changes,
- run EDA/simulation tool adapters,
- parse measurement JSON,
- verify against hard requirements,
- document experiments and lessons learned.

## Quick start

```bash
pip install -e .[dev]

amsaf models show-policy
amsaf verify examples/ldo_core/requirements.yaml examples/ldo_core/measurement_example.json
amsaf optimize examples/ldo_core/optimization_surface.yaml examples/ldo_core/measurement_example.json
pytest
```

## Core ideas

```text
raw/  = immutable source material from Jama, Cadence, Spectre, docs, reviews
wiki/ = LLM-maintained synthesized memory with links and evidence tags
```

The LLM agents are not used as signoff authority. Simulation measurements and requirement traceability are the source of truth.

## Repository map

```text
configs/                 runtime configuration
configs/model_policy.yaml per-agent model routing policy
docs/                    architecture and integration notes
examples/ldo_core/       first AMS block example
raw/                     immutable ingested source material
wiki/                    synthesized design memory
src/ams_agent_factory/   Python package
tests/                   pytest baseline
```

## Multi-model routing

Agents use symbolic model classes such as:

- `cheap_fast`
- `medium_reasoning`
- `strong_reasoning`
- `local_coder`
- `local_embedder`

These aliases are mapped in `configs/providers.yaml` and selected per task in `configs/model_policy.yaml`.

## Safety philosophy

```text
LLM proposes → deterministic EDA tools execute → simulator measures → verifier decides → human approves.
```
