# Project Agents: Project Nexus Standard

## 👥 The Team
- **@senior-architect**: Strategic planner. High-level logic, design patterns, and system architecture. (Optimized for RAM tier/70B models).
- **@lead-developer**: Execution expert. Writes code, runs terminal commands, and manages Git. (Optimized for VRAM tier/14B models).
- **@researcher**: Knowledge specialist. Scans local docs and web for updated APIs.

## 🛠️ Tech Stack & Conventions
- **Language:** Python 3.12+ / NumPy / TensorFlow (Sionna).
- **Architecture:** Modular, service-oriented with robust Integration Harnesses.
- **Protocol:** Model Context Protocol (MCP) for tool integration.
- **Blackboard:** This file (`AGENTS.md`) is the single source of truth for cross-agent synchronization.

## 🚦 Communication Protocol
1. **Plan First:** Always define the mathematical or architectural plan in the Architect's section below before coding.
2. **Execute:** The Developer implements only what has been architected.
3. **Verify:** Every task must conclude with a terminal-based verification or unit test.
4. **Handoff:** Update the "System State" section after every major change.

## 📍 System State
- **Current Phase:** Initialized Project Nexus.
- **Active Sprint:** Infrastructure Setup.
- **Last Sync:** 2026-03-22

## 🏛️ Architect's Section
- **Design:** Tiered memory architecture implemented via `LABS/config.py`.

## 🛠️ Developer's Section
- **Files Created:** benchmark_inference.py, store_memories.py, mcp_client.py, etc.
- **Status:** All baseline infrastructure scripts consolidated into `LABS/`.
