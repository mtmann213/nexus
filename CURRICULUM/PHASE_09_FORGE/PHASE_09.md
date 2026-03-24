# Phase 9: The Forge (Local Team Engineering)
## Subject: Maximizing Tiered Hardware for Multi-Agent Workflows

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Design** a Tiered Hybrid Architecture that balances VRAM (Speed) and System RAM (Depth).
2. **Implement** the **Dispatcher Pattern** using a 1B model to route tasks between implementation and reasoning agents.
3. **Configure** a "Shared-Brain" environment using the **Blackboard Protocol** (`AGENTS.md`).
4. **Optimize** local inference using KV Cache Quantization and Flash Attention.
5. **Construct** an automated **Git Hook Audit** that enforces quality gates on every commit.

---

### 📖 Technical Deep Dive

#### 1. Silicon Economics (The RAM/VRAM Split)
In Phase 9, we split roles based on the **Latency-Logic Tradeoff**:
* **The Lead Dev (VRAM Tier):** A 14B model pinned to the 3080 Ti for high-speed syntax and execution.
* **The Architect (RAM Tier):** A 70B+ model offloaded to System RAM for strategic reasoning.

#### 2. The Blackboard Protocol (`AGENTS.md`)
To prevent token waste and "context drift" between agents, we implement a persistent Blackboard.
* **The Strategy:** We use `AGENTS.md` as a persistent "Source of Truth." The Architect writes the math and design; the Developer reads it to write the code.
* **Neutrality:** Using `AGENTS.md` ensures that your project context is **Portable** across Gemini, OpenCode, and Aider.

#### 3. The Dispatcher Pattern
We utilize a tiny **1B parameter model** as a "Pre-Selector" to route user prompts to the correct tier based on intent (TACTICAL vs. STRATEGIC).

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Blackboard Protocol** | A shared file (`AGENTS.md`) used for inter-agent state synchronization. | A **Shared Lab Notebook**. |
| **Dispatcher** | A lightweight model that routes requests to specialized agents. | A **Pre-Selector Filter**. |
| **KV Cache Quantization** | Compressing the AI's "working memory" to save VRAM. | **Buffer Compression**. |
| **Partial Offload** | Running some model layers on GPU and others on CPU/RAM. | **Hybrid Processing**. |
| **Portability** | The ability to move project state between different AI services. | **Universal Interoperability**. |

---

### ❓ Comprehension Questions
1. Why is it more efficient to run an Architect on System RAM instead of VRAM for high-level planning?
2. How does the Blackboard Protocol save money and tokens in a multi-agent team?
3. What is the benefit of using `AGENTS.md` over a service-specific file like `CLAUDE.md`?
4. If your 14B model is running at 1 token/sec, what is the likely hardware bottleneck?
5. How does a Git Hook Audit turn your local machine into a "Professional Dev Shop"?

---

### 🧪 Lab Reference: `LABS/vanguard_manager.py` (Draft)

#### What to expect:
You will run a "Tri-Tier" manager script. You will speak to a single terminal. A 1B model will route your request. The result will be documented in `AGENTS.md` for persistent project tracking.

#### Generation Prompt (for the student):
> "Build a Tri-Tier AI Manager in Python. Use a 1B model to classify user intent as TACTICAL or STRATEGIC. Route requests to specialized agents. Ensure both agents read and write to an 'AGENTS.md' file to maintain project state."

---

### ✅ Success Criteria
* **Proof of Work:** (Planned) The user demonstrates a "Handoff" where the Architect designs a feature in the blackboard (`AGENTS.md`), and the Developer implements it.
