# Phase 6: The Council (Orchestration)
## Subject: Multi-Agent Systems, Evals, and the Blackboard Protocol

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Explain** the concept of Multi-Agent Orchestration and why specialization improves output quality.
2. **Implement** a "Design-Review-Refine" loop using multiple AI personas.
3. **Apply** the **Blackboard Protocol** (`CLAUDE.md`) to synchronize state between agents.
4. **Configure** agent guardrails including `max_tokens` and specific `temperatures`.
5. **Implement** an **Evaluation Layer (Evals)** to empirically measure agent performance.

---

### 📖 Technical Deep Dive

#### 1. Specialization over Generalization
In Phase 6, we moved away from the idea of a single "Generalist" AI. In complex RF projects, error rates drop when you delegate specific roles to specialized agents.
* **Key Insight:** Two 35B models working together (one creating, one critiquing) are significantly more reliable than a single model asked to "get it right the first time."

#### 2. The Blackboard Protocol (`CLAUDE.md`)
As teams grow, passing the entire chat history to every agent becomes token-expensive and introduces "Context Drift."
* **The Strategy:** We use a central Markdown file (The Blackboard) as a persistent "Source of Truth." Agents "Sign-in" to the file, read the current state, perform their task, and "Sign-out" by updating the file.
* **Impact:** This allows a Developer agent to know exactly what the Architect planned without needing to read the entire planning conversation.

#### 3. The Evaluation Layer (Evals)
How do we know if our Reviewer agent is actually making the code better? We implement **Evals**.
* **The Strategy:** We create a "Ground Truth" (a perfectly working script) and use a third agent (The Judge) to compare the "Before" and "After" code against that ground truth.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Orchestration** | Managing the interaction and data-flow between multiple AI agents. | An **ATE Controller**. |
| **Blackboard Protocol** | A shared file used for inter-agent state synchronization. | A **Shared Lab Notebook**. |
| **Eval (Evaluation)** | A systematic way to measure the performance or accuracy of an AI agent. | **V&V Testing**. |
| **Ground Truth** | The "correct" answer used as a baseline for evaluation. | A **Calibrated Reference**. |
| **Regression** | When a new change causes the AI to perform worse than before. | **Link Budget Degradation**. |

---

### ❓ Comprehension Questions
1. Why does giving an agent a "Persona" (like Senior RF Engineer) improve its technical performance?
2. What is the role of the "Evaluation Layer" in a professional AI workflow?
3. How does the Blackboard Protocol prevent "Context Drift" in a multi-agent swarm?
4. In a multi-agent loop, why should the "Reviewer" have a lower temperature than the "Architect"?
5. How would you design an "Eval" to test if your PICC can correctly calculate a 5G link budget?

---

### 🧪 Lab Reference: `LABS/nexus_orchestrator.py`

#### What to expect:
This script simulates a "Meeting of the Minds." It manages two separate conversations: one for the **Architect** (Creator) and one for the **Reviewer** (Critic). You will see the Architect propose a 5G Rayleigh Fading simulation, the Reviewer find mathematical flaws, and the Architect produce a final, peer-reviewed script.

#### Generation Prompt (for the student):
> "Create an orchestration script in Python that manages two AI personas: an Architect and a Reviewer. The Architect should design an RF Python script based on a user mission. The Reviewer should then receive that script and find 3 technical improvements. Finally, the Architect should receive the reviewer's feedback and output the final code. Ensure that each agent interaction is treated as a fresh message list to maintain strict alternating 'user' and 'assistant' roles."

---

### ✅ Success Criteria
* **Proof of Work:** `nexus_orchestrator.py` successfully completes a loop, and a human (or "Judge" agent) confirms the final code is superior to the initial draft.
