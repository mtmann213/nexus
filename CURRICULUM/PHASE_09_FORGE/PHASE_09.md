# Phase 9: The Forge (Local Team Engineering)
## Subject: Silicon Economics and Tiered Model Deployment

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Allocate** compute resources across VRAM and RAM tiers based on task complexity.
2. **Deploy** a multi-model "Brain" using the Dispatcher Pattern.
3. **Master** the "Small-Med-Large" strategy for local engineering teams.
4. **Implement** persistence using the Blackboard Protocol (`AGENTS.md`).
5. **Optimize** high-parameter models (70B+) for use in low-VRAM environments.

---

### 📖 Technical Deep Dive: Silicon Economics

#### 1. The Tri-Tier Strategy
We don't use one model for everything. We use a **Tiered Hierarchy**:

*   **Tier 1: The Dispatcher (1B - 3B)**
    *   *Purpose:* Routing, Voice transcription, and Hardware monitoring.
    *   *Constraint:* Must be sub-second latency. Always pinned to VRAM.
*   **Tier 2: The Developer (7B - 14B)**
    *   *Purpose:* Coding, Unit testing, and Shell execution.
    *   *Constraint:* Must have high "Coding IQ." Should fit 100% in VRAM for real-time interaction.
*   **Tier 3: The Architect (30B - 70B+)**
    *   *Purpose:* Complex architectural design, mathematical proofs, and logic review.
    *   *Constraint:* Intelligence is prioritized over speed. Can be offloaded to System RAM (CPU).

#### 2. Hardware Deployment Blueprints

**Desktop Profile (12GB VRAM / 64GB RAM):**
- **Dispatcher:** Qwen 2.5 1.5B (VRAM)
- **Developer:** Qwen 2.5 Coder 14B (VRAM)
- **Architect:** Llama 3.3 70B (System RAM)

**Laptop Profile (8GB VRAM / 32GB RAM):**
- **Dispatcher:** Qwen 2.5 0.5B (VRAM)
- **Developer:** Qwen 2.5 Coder 7B (VRAM)
- **Architect:** Qwen 2.5 32B (System RAM)

---

### 🚦 The Workflow (The Loop of Three)
1.  **User** sends a prompt to the Dispatcher.
2.  **Dispatcher** classifies: is this `TACTICAL` or `STRATEGIC`?
3.  **Handoff:**
    *   If `STRATEGIC`: Architect writes a design to `AGENTS.md`.
    *   If `TACTICAL`: Developer reads the design and implements code.
4.  **Sync:** All changes are logged in the System State of `AGENTS.md`.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Compute Budgeting** | Allocating specific hardware resources to specific tasks. | **Link Budgeting**. |
| **VRAM Pinning** | Ensuring a model never leaves the GPU memory. | **Frequency Locking**. |
| **CPU Offloading** | Moving model layers to System RAM to handle large models. | **Off-chip processing**. |
| **Intent Classification** | Detecting what the user wants before choosing a model. | **Signal Identification**. |

---

### 🧪 Lab Reference: `LABS/vanguard_manager.py`

#### What to expect:
You will build a manager that automatically routes your prompt to the correct model. You will see the **Dispatcher** make a split-second decision to either call the **Developer** for code or the **Architect** for a deep design session.

#### Generation Prompt (for the student):
> "Build a Python manager script that uses LM Studio's multi-model support. Use a 1.5B model as a 'Router' to classify prompts. If the prompt requires coding, call the 14B model. If it requires strategy, call the 70B model. Record the 'Resource Usage' for each turn."

---

### ✅ Success Criteria
* **Proof of Work:** Student demonstrates a single prompt triggering different models based on complexity, with all results synced to `AGENTS.md`.
