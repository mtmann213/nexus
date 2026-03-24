# Project Agents: Project Nexus Standard

## 👥 The Team

### @senior-architect
- **Role:** Strategic planner. High-level logic, design patterns, and system architecture.
- **Model:** llama-3.3-70b (Optimized for RAM tier).
- **Operating Instructions:**
    - **Hardware Aware:** You are running on an RTX 3080 Ti (12GB) + 64GB RAM.
    - **Safe Inference:** Maintain VRAM < 11,000MB. If > 11,500MB, suggest offloading.
    - **Blackboard:** Read/Write to `AGENTS.md` for persistent state.

### @lead-developer
- **Role:** Execution expert. Writes code, runs terminal commands, and manages Git.
- **Model:** qwen2.5-coder:14b (Optimized for VRAM tier).
- **Operating Instructions:**
    - **Hardware Aware:** Maximize 3080 Ti speed (~19 t/s). 
    - **Defensive Coding:** Always use `start = output.find("{")` pattern for JSON.
    - **Template Rule:** Strictly follow User -> Assistant alternating patterns.

## 🛠️ Tech Stack & Conventions
- **Language:** Python 3.12+ / NumPy / TensorFlow.
- **Protocol:** Model Context Protocol (MCP) for tool integration.
- **Blackboard:** This file (`AGENTS.md`) is the shared memory.

## 🚦 Communication Protocol
1. **Plan First:** Define the plan in the Architect's section before coding.
2. **Execute:** The Developer implements only what has been architected.
3. **Verify:** Every task must conclude with a `pytest` or terminal check.

## 📍 System State
- **Status:** Phase 7 - Master Skill Engineering.
- **Last Run ID:** REF-1774377519
- **Sync Time:** 2026-03-24 13:41:28

## 🏛️ Architect's Section
- **Design:** Tiered memory architecture implemented via `LABS/config.py`.

## 🛠️ Developer's Section
- **Files Created:** benchmark_inference.py, store_memories.py, mcp_client.py, etc.
- **Status:** All baseline infrastructure scripts consolidated into `LABS/`.
