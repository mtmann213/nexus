# Project Nexus: The Living Journal

## Session 1: 2026-03-22
### Learning Focus: Foundations (Tokens & Context)
- **Terminology Spotlight:**
    - **Tokens:** Atomic units of text (The "Samples" of language).
    - **Context Window:** The model's observation buffer (The "FFT Window").
    - **Quantization:** Compressing 16-bit weights to 4-bit (Reducing "Precision" to save VRAM).

## Session 2: 2026-03-22
### Learning Focus: Embeddings & Vector DBs (The "Persistent Librarian")
- **Terminology Spotlight:**
    - **Vector Embedding:** High-dimensional coordinates of meaning (The "Semantic Spectrum").
    - **Cosine Similarity:** Measuring the angle between vectors (The "Correlation Coefficient").
    - **Vector Database:** A spatial index for semantic retrieval (The "Library Map").

## Session 3-4: 2026-03-22
### Learning Focus: Agency & MCP
- **Terminology Spotlight:**
    - **Function Calling:** AI triggering code via JSON (The "Nervous System").
    - **Test Harness:** The controlled environment for executing AI actions (The "Test Rig").
    - **MCP (Model Context Protocol):** A standardized "USB" for connecting AI to tools.

## Session 5: 2026-03-22
### Learning Focus: Orchestration & Defensive Engineering
- **Terminology Spotlight:**
    - **Orchestration:** Managing multiple AI specialists (The "Management Layer").
    - **JSON Hygiene:** Cleaning AI output to ensure valid data parsing.
    - **Jinja Template:** The strict "Conversation Script" local servers follow.

## Session 6: 2026-03-22
### Learning Focus: Cognitive Harnesses (Phase 8)
- **Terminology Spotlight:**
    - **Cognitive Harness:** A software wrapper that enforces a specific thought-process on an LLM (e.g., `reflex_harness.py`).
    - **Reflexive Reasoning:** The AI's ability to "look back" at its own work and identify flaws.
    - **Latency Timeout:** A failure mode where complex logic takes longer than the default API wait-time.
- **Success:** Built a "Reflex Rig" that allowed a 35B model to catch its own syntax errors and improve RF physics (ITU-R rain models) through a 3-step loop.

### Daily Log
- Built `reflex_harness.py` to demonstrate the "Harness vs. Model" distinction.
- Successfully implemented a 300s timeout to handle heavy RF math processing on the 3080 Ti.
- **Milestone:** Proved that "Harness Engineering" can upgrade a model's intelligence without changing its weights.
- **Final Status:** Project Nexus is fully documented and pushed to GitHub.
