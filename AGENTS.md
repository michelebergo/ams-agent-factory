# AMS Agent Factory Rules

## Source hierarchy

1. Jama baselined requirements are authoritative for requirements.
2. Spectre/ngspice measurement JSON is authoritative for verification results.
3. Cadence netlists/schematics are authoritative for implemented connectivity.
4. Human design-review decisions are authoritative for architecture.
5. Wiki pages are synthesized memory, not source of truth.

## Raw source policy

- Never edit files under `raw/`.
- Imported sources must preserve origin metadata when possible.
- Conflicts go into `wiki/contradictions/open_conflicts.md`.

## Verification policy

An agent may write `PASS` only if all are present:

- requirement ID
- testbench name
- simulation run ID
- measurement value
- required bound
- corner/condition
- comparison result

## Model routing policy

- Cheap/fast models: extraction, formatting, classification, report drafting.
- Medium reasoning models: requirement normalization and routine debug.
- Strong reasoning models: topology choice, ambiguous failures, high-risk optimization.
- Tool-only agents: simulation execution and hard pass/fail verification.

## Forbidden claims

Agents must not claim `verified`, `stable`, or `meets all specs` without measured evidence.
