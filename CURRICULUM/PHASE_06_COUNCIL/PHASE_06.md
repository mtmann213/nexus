# Phase 6: The Council (Orchestration)
## Subject: Multi-Agent Systems, Evals, and the Blackboard Protocol

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Explain** the concept of Multi-Agent Orchestration and why specialization improves output quality.
2. **Implement** a "Design-Review-Refine" loop using multiple AI personas.
3. **Apply** the **Blackboard Protocol** (`AGENTS.md`) to synchronize state between agents across different AI frameworks (Gemini, OpenCode, Aider).
4. **Configure** agent guardrails including `max_tokens` and specific `temperatures`.
5. **Implement** an **Evaluation Layer (Evals)** to empirically measure agent performance.

---

### 📖 Technical Deep Dive

#### 1. Specialization over Generalization
In Phase 6, we delegate specific roles to specialized agents. The Architect designs, and the Reviewer critiques.

#### 2. The Blackboard Protocol (`AGENTS.md`)
To prevent token waste and "Context Drift" in a multi-agent swarm, we use a central Markdown file as a persistent **Source of Truth**.
* **Framework Agnosticism:** By using `AGENTS.md`, our project memory becomes **Portable**. OpenCode reads it natively, and you can instruct the Gemini CLI to use it as a reference.
* **Service-Specific Options:** If using Claude Code, you can simply `cp AGENTS.md CLAUDE.md` to leverage its built-in blackboard feature.
* **The Workflow:** Agents "Sign-in" to the file, read the current state, perform their task, and "Sign-out" by updating the file.

#### 3. The Evaluation Layer (Evals)
How do we know if our Reviewer agent is actually making the code better? We implement **Evals** to compare the "Before" and "After" code against a "Ground Truth" baseline.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Orchestration** | Managing the interaction and data-flow between multiple AI agents. | An **ATE Controller**. |
| **Blackboard Protocol** | A shared file (`AGENTS.md`) used for inter-agent synchronization. | A **Shared Lab Notebook**. |
| **Portability** | The ability of a system to run across different platforms (Gemini vs. Claude). | **Universal Connectivity**. |
| **Eval (Evaluation)** | A systematic way to measure the performance or accuracy of an AI agent. | **V&V Testing**. |
| **Regression** | When a new change causes the AI to perform worse than before. | **Link Budget Degradation**. |

---

### ❓ Comprehension Questions
1. Why is `AGENTS.md` a better choice than `CLAUDE.md` for a team using multiple AI services?
2. What is the role of the "Blackboard Protocol" in preventing context drift?
3. How do you "Port" your project state if you switch from the Gemini CLI to OpenCode?
4. In a multi-agent loop, why should the "Reviewer" have a lower temperature than the "Architect"?
5. How would you design an "Eval" to test if your PICC can correctly calculate a 5G link budget?

---

### 🧪 Lab Reference: `LABS/nexus_orchestrator.py`

#### What to expect:
This script simulates a "Meeting of the Minds." It manages separate conversations for the Architect and Reviewer. You will see the draft-refine loop in action, resulting in a finalized RF script.

#### Generation Prompt (for the student):
> "Create an orchestration script in Python that manages two AI personas: an Architect and a Reviewer. Ensure that the Architect's initial design is documented in a local 'AGENTS.md' file, and the Reviewer reads this file to provide its critique. The final output should be an updated 'AGENTS.md' reflecting the refined architecture."

---

### ✅ Success Criteria
* **Proof of Work:** `nexus_orchestrator.py` successfully completes a loop, and the finalized design is captured in `AGENTS.md`.
