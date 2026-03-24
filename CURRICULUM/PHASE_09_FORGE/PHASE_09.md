# Phase 9: The Forge (Local Team Engineering)
## Subject: Maximizing Tiered Hardware for Multi-Agent Workflows

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Design** a Tiered Hybrid Architecture that balances VRAM (Speed) and System RAM (Depth).
2. **Implement** the **Dispatcher Pattern** using a 1B model to route tasks between implementation and reasoning agents.
3. **Configure** a "Shared-Brain" environment using the **Blackboard Protocol** (`CLAUDE.md`).
4. **Optimize** local inference using KV Cache Quantization and Flash Attention.
5. **Construct** an automated **Git Hook Audit** that enforces quality gates on every commit.

---

### 📖 Technical Deep Dive

#### 1. Silicon Economics (The RAM/VRAM Split)
In Phase 9, we stop treating the GPU as the only compute resource. We learn to split roles based on the **Latency-Logic Tradeoff**:
* **The Lead Dev (VRAM Tier):** A 14B model (like Qwen 3.5 Coder) pinned to the 3080 Ti. It provides 50+ t/s for tactical coding and shell execution.
* **The Architect (RAM Tier):** A 70B+ model (like Llama 3.3 or DeepSeek-V3) running primarily on 64GB System RAM. It provides deep reasoning (1-3 t/s) for planning and audits.

#### 2. The Blackboard Protocol (`CLAUDE.md`)
To prevent token waste and "context drift" between agents, we implement a persistent Blackboard.
* **The Strategy:** Instead of agents passing massive message histories, they update a central Markdown file. The Architect writes the math and design; the Developer reads it to write the code.
* **Key Insight:** This creates a "Single Source of Truth" that persists even if the AI processes are restarted.

#### 3. The Dispatcher Pattern
We utilize a tiny **1B parameter model** (Gemma 3 1B) as a "Pre-Selector." 
* **The Mission:** It analyzes the user's prompt in milliseconds (<200ms) and decides if it is **TACTICAL** (Developer) or **STRATEGIC** (Architect). 
* **Impact:** This protects the slow reasoning agents from being bogged down by simple requests.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Blackboard Protocol** | A shared file used for inter-agent state synchronization. | A **Shared Lab Notebook**. |
| **Dispatcher** | A lightweight model that routes requests to specialized agents. | A **Pre-Selector Filter** in a receiver. |
| **KV Cache Quantization** | Compressing the AI's "working memory" to save VRAM. | **Buffer Compression**. |
| **Partial Offload** | Running some model layers on GPU and others on CPU/RAM. | **Hybrid Analog/Digital** processing. |
| **Git Hook Audit** | An automated script that triggers an AI review before a code commit. | A **Final Test Gate** before shipment. |

---

### ❓ Comprehension Questions
1. Why is it more efficient to run an Architect on System RAM instead of VRAM for high-level planning?
2. How does the Blackboard Protocol (`CLAUDE.md`) save money and tokens in a multi-agent team?
3. What is the benefit of using a 1B model as a Dispatcher instead of simple keyword matching?
4. If your 14B model is running at 1 token/sec, what is the likely hardware bottleneck, and how do you fix it?
5. How does a Git Hook Audit turn your local machine into a "Professional Dev Shop"?

---

### 🧪 Lab Reference: `LABS/vanguard_manager.py` (Draft)

#### What to expect:
(This lab represents the state-of-the-art 2026 setup). You will run a "Tri-Tier" manager script. You will speak to a single terminal. A 1B model will route your request. If you ask for a "MIMO simulation plan," the 70B model in your RAM will answer. If you ask for the "Python code for a 1024-point FFT," the 14B model in your VRAM will generate it instantly.

#### Generation Prompt (for the student):
> "Build a Tri-Tier AI Manager in Python. Use a 1B model to classify user intent as TACTICAL or STRATEGIC. Route TACTICAL requests to a 14B model pinned to the GPU and STRATEGIC requests to a 70B model offloaded to System RAM. Ensure both agents read and write to a 'CLAUDE.md' file to maintain project state."

---

### ✅ Success Criteria
* **Proof of Work:** (Planned) The user demonstrates a "Handoff" where the Architect designs a feature in the blackboard, and the Developer implements it without further user input.
