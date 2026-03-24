# Project Opal Vanguard: 4-Agent Final Roster (2026)

## [Tier 0] Global Orchestrator: Gemini CLI
- **Model:** Gemini 3 Flash / Ultra (Cloud)
- **Role:** Global Context & Project Lighthouse.
- **Responsibility:** Ingests massive documentation and full repo state. Routes strategic intent to local sub-agents.

---

## [Tier 1] Dispatcher: @.opencode/agent/dispatcher.md (Gemma 3 1B)
- **Placement:** VRAM (Desktop) / RAM (Laptop)
- **Settings:** Context: 8,192 | KV: Q4_0 | Temp: 0.0
- **Skill:** Sub-100ms intent routing. The first line of interaction.

## [Tier 2] Lead Developer: @.opencode/agent/lead-developer.md (Qwen 3.5 Coder 9B)
- **Placement:** VRAM (3080 Ti - All Layers Offloaded)
- **Settings:** Context: 16,384 | KV: IQ4_NL | Temp: 0.2 | Min-P: 0.05
- **Skill:** Verbatim coding and CLI execution. Optimized for TensorFlow/Sionna syntax.
- **Hardware Goal:** Maintain 3.5GB VRAM buffer for active simulations.

## [Tier 3] Auditor (Technical Logic): @.opencode/agent/auditor.md (Phi-4 Reasoning 14B)
- **Placement:** System RAM (64GB)
- **Settings:** Context: 32,768 | KV: IQ4_NL | Temp: 0.1 | Use <thinking> tags.
- **Skill:** Complex RF math verification, Chain-of-Thought debugging, and protocol analysis.
- **Focus:** The "Auditor" who ensures the 9B's code won't break the physics of the receiver.

## [Tier 4] Senior Architect: @.opencode/agent/senior-architect.md (Qwen 3.5 35B-A3B)
- **Placement:** System RAM (64GB)
- **Settings:** Context: 128k (MoE Efficiency) | KV: INT4 | Temp: 0.6
- **Skill:** Strategic long-term planning and "Mixture of Experts" reasoning.
- **Focus:** Broad system design, modulation classification architecture, and multi-file logic.

---

## Shared Communication Protocol
- **State File:** `CLAUDE.md` (Shared blackboard for agents).
- **Inference Mode:** Use "Thinking/Reasoning" mode for Phi-4 and 35B-A3B; "Flash/Direct" for 9B and 1B.
