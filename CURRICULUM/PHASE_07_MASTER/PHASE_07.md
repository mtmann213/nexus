# Phase 7: The Master (Expert Skill Engineering)
## Subject: Upgrading AI Reasoning with Procedural Playbooks

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** "Skill Engineering" and explain how it differs from simple RAG or prompting.
2. **Utilize** a **Skill Library** to assign specialized "Playbooks" to the OpenCode agent.
3. **Construct** complex Skill Documents (Markdown) that enforce architectural logic and state-tracking.
4. **Implement** "Skill Injection" to give agents expert-level knowledge of new or internal libraries.
5. **Analyze** the impact of skills on "Task Success Rate" for complex, multi-file refactors.

---

### 📖 Technical Deep Dive

#### 1. Skill Engineering (The SOP for AI)
Most LLMs have a "Knowledge Cutoff." They don't know about libraries or versions released yesterday. **Skill Engineering** solves this by providing the model with a structured "Procedural Manual" at runtime.
* **Key Insight:** Skills aren't just data (RAG); they are **Instructions** on *how* to act, what syntax to use, and what pitfalls to avoid.

#### 2. The Skill Library (Specialist Playbooks)
In this phase, we move beyond basic chat. We give our OpenCode agent specialized powers:
* **Documentation Oracle:** A skill that indexes and live-queries the latest technical docs.
* **Architecture Visualizer:** Automatically converts plans into Mermaid.js diagrams.
* **Self-Critique Loops:** A skill that forces an agent to run its code and refactor it until it meets a success metric.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Skill** | A structured Markdown file containing procedural expert knowledge. | A **Technical Standard** or SOP. |
| **Skill Library** | A collection of modular playbooks assigned to specific agents. | A **Technical Reference** library. |
| **Skill Injection** | Providing an agent with specific skills during its initialization phase. | **Firmware Loading**. |
| **Procedural Knowledge** | Knowledge of *how* to do something, rather than just facts. | **Operator Proficiency**. |

---

### ❓ Comprehension Questions
1. Why is a "Skill" more effective than a "Tool" for supporting a library that was released after the model's training cutoff?
2. What is the benefit of keeping Skills in Markdown format rather than embedding them in Python code?
3. How does a "Documentation Oracle" skill prevent an agent from using deprecated API syntax?
4. What is the difference between "Declarative Knowledge" (facts) and "Procedural Knowledge" (skills)?

---

### 🧪 Lab Reference: `SKILLS/nexus-hardware.md`

#### What to expect:
You will refine your existing `nexus-hardware.md` skill to include more complex "State-Aware" rules (e.g., "If VRAM is full, suggest deleting the KV cache"). You will watch OpenCode ingest this skill and change its behavior in real-time.

#### Generation Prompt (for the student):
> "Write an advanced Markdown 'Skill' document. It should provide a step-by-step strategy for debugging a 5G Sionna simulation that is hitting VRAM limits. Include instructions on how to analyze the error logs and suggest specific memory-saving refactors."

---

### ✅ Success Criteria
* **Proof of Work:** The OpenCode agent successfully follows a multi-step debugging strategy defined in a custom Skill MD without human intervention.
