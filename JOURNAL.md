# Project Nexus: The Living Journal

## Session 3: 2026-03-22
### Learning Focus: Agency (The "Motor Cortex")
- **Concepts:** Function Calling (JSON Signaling); Tool Execution; The Action-Observation Loop.
- **Tooling:** `agent_multitool.py` with multi-step reasoning.
- **Success:** Created an autonomous "Think-Act-Verify" loop.

## Session 4: 2026-03-22
### Learning Focus: The Model Context Protocol (The "Bridge")
- **Concepts:** MCP Standard; Client-Server Architecture; JSON-RPC; Standardized Tool Discovery.
- **Tooling:** `nexus_hardware_server.py` and `mcp_client.py`.
- **Success:** Built a hardware-aware MCP server that exposes RTX 3080 Ti metrics (VRAM/Load) to any MCP-compatible AI.

### Daily Log
- Built a custom MCP server in Python.
- Successfully connected a Python MCP client to the hardware server.
- **Lesson Learned:** MCP eliminates "Tool Brittleness" by allowing the server to describe its own capabilities to the client.
- **Hardware Note:** 3080 Ti VRAM is at 95% capacity (11.7GB/12GB) while running the 35B model. This is the "Inference Ceiling."
- **Ready for Phase 5:** Orchestrating multiple agents using these tools.
