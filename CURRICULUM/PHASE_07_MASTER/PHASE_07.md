# Phase 7: The Master (Skills & OpenCode)
## Subject: Skill Engineering and Autonomous Coding Agents

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** "Skill Engineering" and explain how it upgrades an AI's procedural strategy.
2. **Differentiate** between a Tool (capability) and a Skill (procedural guide).
3. **Configure** an autonomous terminal-native agent (OpenCode) for project-wide reasoning.
4. **Construct** a custom Skill Document (Markdown) to enforce local architectural constraints and guardrails.
5. **Implement** "Skill Injection" using an `AGENTS.md` file to upgrade an agent's project context.

---

### 📖 Technical Deep Dive

#### 1. Skill Engineering (The SOP for AI)
Most LLMs have a "Knowledge Cutoff." They don't know about libraries or versions released yesterday. **Skill Engineering** solves this by providing the model with a structured "Procedural Manual" at runtime.
* **The Analogy:** If the model is a general-purpose CPU, a **Skill** is the **Bitstream** you load onto an FPGA. It transforms the general reasoning into a specialized, expert-level DSP for a specific task.
* **Key Insight:** Skills aren't just data (RAG); they are **Instructions** on *how* to act, what syntax to use, and what pitfalls to avoid.

#### 2. OpenCode (The Autonomous Peer)
Standard AI tools are reactive—they wait for you to prompt them. **OpenCode** is a terminal-native, autonomous agent.
* **The Cycle:** It uses a **Plan -> Act -> Validate** cycle. It can analyze your entire repository, create a multi-file plan, and execute it without turn-by-turn instruction.
* **Transparency:** Unlike "Black Box" tools, OpenCode works directly in your terminal, allowing you to see every file search and command it executes.

#### 3. The AGENTS.md Protocol
To keep an agent focused on your project's unique constraints (like your 12GB VRAM limit), we use an **`AGENTS.md`** file.
* **The Strategy:** This file acts as the "Standard Operating Procedure" for any agent entering the repo. By listing our custom **Nexus Skills** in this file, we ensure every agent follows our hardware-aware safety protocols.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Skill** | A structured Markdown file containing procedural expert knowledge for an AI. | A **Technical Standard** or SOP. |
| **Skill Creator** | An agentic workflow designed to analyze a codebase and generate a Skill document. | An **Auto-Documenter** or Spec-Gen tool. |
| **OpenCode** | An open-source, terminal-native autonomous coding agent. | An **Automated Test Suite** for development. |
| **Skill Injection** | Providing an agent with specific skills during its initialization phase. | **Firmware Loading** or Bitstream Config. |
| **Plan-Act-Validate** | The cognitive loop used by autonomous agents to solve high-level prompts. | **Scan-Process-Transmit** loop. |

---

### ❓ Comprehension Questions
1. Why is a "Skill" more effective than a "Tool" for supporting a library that was released after the model's training cutoff?
2. How does an autonomous agent like OpenCode differ from a reactive assistant like basic ChatGPT?
3. What is the benefit of keeping Skills in Markdown format rather than embedding them in Python code?
4. If OpenCode is ignoring your VRAM limits, which file in the repository should you update to fix its behavior?
5. How can "Skill Engineering" reduce the number of tokens required for a complex refactor?

---

### 🧪 Lab Reference: `SKILLS/nexus-hardware.md` & `AGENTS.md`

#### What to expect:
In this lab, you don't run a Python script. Instead, you create a **Skill Document** (`SKILLS/nexus-hardware.md`) that explicitly lists your RTX 3080 Ti constraints. You then initialize OpenCode, which creates an **`AGENTS.md`** file. By linking the skill in `AGENTS.md`, you will see the agent acknowledge your hardware limits (e.g., "VRAM usage is high, I will not load a larger model").

#### Generation Prompt (for the student):
> "Write a Markdown 'Skill' document for an AI agent. It should define the hardware context of a local workstation with an RTX 3080 Ti (12GB VRAM). Include procedural rules, such as a 'VRAM Guardrail' that forbids loading models if utilization is above 93%. Provide expert workflows for checking hardware status using the standardized MCP pattern."

---

### ✅ Success Criteria
* **Proof of Work:** `SKILLS/nexus-hardware.md` is successfully created and referenced in the project's agentic configuration, enforcing VRAM guardrails during local inference.
