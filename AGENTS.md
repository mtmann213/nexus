# Project Agents: Project Nexus Tiered Team

## 👥 The Team Structure (Compute-Aware)

### 1. @dispatcher (Tier 1: VRAM)
- **Role**: Intent Classification & Routing.
- **Model**: Gemma 3 1B (Pinned to VRAM).
- **Responsibility**: Instant triage. Decides if a task is TACTICAL or STRATEGIC.

### 2. @lead-developer (Tier 2: VRAM)
- **Role**: Implementation & Execution.
- **Model**: Qwen 3.5 Coder 14B (VRAM).
- **Responsibility**: Writing code, running terminal commands, and managing file structures.

### 3. @researcher (Tier 3: System RAM)
- **Role**: Technical Intelligence & Documentation.
- **Model**: Llama 3.1 8B (System RAM).
- **Responsibility**: Scanning local docs, web search, and API summarization.

### 4. @senior-architect (Tier 4: System RAM)
- **Role**: Strategy & Senior Review.
- **Model**: Llama 3.3 70B (System RAM - 0 GPU Layers).
- **Responsibility**: High-level system design, complex math, and architectural audits.

## 🛠️ Tech Stack & Conventions
- **Blackboard**: This file (`AGENTS.md`) is the single source of truth for cross-agent synchronization.
- **Optimizations**: KV Cache Quantization (INT4) and Flash Attention enabled.
- **Protocol**: Model Context Protocol (MCP) for tool integration.

## 🚦 Communication Protocol
1. **Dispatcher Triage**: Every request starts with the @dispatcher.
2. **Strategic Planning**: If the task is complex, @senior-architect writes the plan to this file.
3. **Execution**: @lead-developer implements only after the plan is synchronized.
4. **Verification**: @researcher validates API usage and @lead-developer runs tests.

## 📍 System State
- **Status**: Phase 9 - The Forge (4-Agent Integration).
- **Target Hardware**: Desktop (3080 Ti / 64GB) & Laptop (8GB / 32GB).
- **Last Sync**: 2026-03-24 15:45:00
