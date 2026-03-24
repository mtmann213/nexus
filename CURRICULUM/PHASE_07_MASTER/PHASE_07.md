# Phase 7: The Master (Skills & OpenCode)
## Subject: Skill Engineering and Autonomous Coding Agents

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** "Skill Engineering" and explain how it upgrades an AI's procedural strategy.
2. **Utilize** a **Skill Library** to assign specialized "Playbooks" to different agents.
3. **Configure** an autonomous terminal-native agent (OpenCode) for project-wide reasoning.
4. **Construct** a custom Skill Document (Markdown) to enforce local architectural constraints and guardrails.
5. **Implement** "Skill Injection" using an `AGENTS.md` file to upgrade an agent's project context.

---

### 📖 Technical Deep Dive

#### 1. Skill Engineering (The SOP for AI)
Most LLMs have a "Knowledge Cutoff." They don't know about libraries or versions released yesterday. **Skill Engineering** solves this by providing the model with a structured "Procedural Manual" at runtime.
* **The Analogy:** If the model is a general-purpose CPU, a **Skill** is the **Bitstream** you load onto an FPGA. It transforms the general reasoning into a specialized, expert-level DSP for a specific task.

#### 2. The Skill Library (Specialist Playbooks)
In 2026, agents use **Skill Modules** (Markdown playbooks) to gain specialized powers:
* **Documentation Oracle:** A skill that indexes and live-queries the latest technical docs.
* **Architecture Visualizer:** Automatically converts plans into Mermaid.js diagrams.
* **Self-Critique Loops:** A skill that forces an agent to run its code and refactor it until it meets a success metric.

#### 3. OpenCode (The Autonomous Peer)
Standard AI tools are reactive. **OpenCode** is a terminal-native, autonomous agent that uses a **Plan -> Act -> Validate** cycle.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Skill** | A structured Markdown file containing procedural expert knowledge. | A **Technical Standard** or SOP. |
| **Skill Library** | A collection of modular playbooks assigned to specific agents. | A **Technical Reference** library. |
| **OpenCode** | An open-source, terminal-native autonomous coding agent. | An **Automated Test Suite**. |
| **Skill Injection** | Providing an agent with specific skills during its initialization phase. | **Firmware Loading**. |
| **Plan-Act-Validate** | The cognitive loop used by autonomous agents. | **Scan-Process-Transmit** loop. |

---

### ❓ Comprehension Questions
1. Why is a "Skill" more effective than a "Tool" for supporting a library that was released after the model's training cutoff?
2. How does an autonomous agent like OpenCode differ from a reactive assistant?
3. What is the benefit of keeping Skills in Markdown format rather than embedding them in Python code?
4. If an agent is ignoring your VRAM limits, which skill file should you update to fix its behavior?
5. How does a "Documentation Oracle" skill prevent an agent from using deprecated API syntax?

---

### 🧪 Lab Reference: `SKILLS/nexus-hardware.md` & `AGENTS.md`

#### What to expect:
In this lab, you create a **Skill Document** (`SKILLS/nexus-hardware.md`) that explicitly lists your hardware constraints. You then initialize OpenCode, which creates an **`AGENTS.md`** file. By linking the skill in `AGENTS.md`, you will see the agent acknowledge your hardware limits (e.g., "VRAM usage is high, I will not load a larger model").

#### Generation Prompt (for the student):
> "Write a Markdown 'Skill' document for an AI agent. It should define the hardware context of a local workstation with an RTX 3080 Ti (12GB VRAM). Include procedural rules, such as a 'VRAM Guardrail' that forbids loading models if utilization is above 93%. Provide expert workflows for checking hardware status using the standardized MCP pattern."

---

### ✅ Success Criteria
* **Proof of Work:** `SKILLS/nexus-hardware.md` is successfully created and referenced in the project's agentic configuration, enforcing VRAM guardrails during local inference.
