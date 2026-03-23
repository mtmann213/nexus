# 🛠️ Project Nexus: AI Troubleshooting Guide
## Why is my AI failing? (Common Engineering Traps)

AI models are not deterministic. They are probabilistic engines that can fail in subtle ways. This guide documents the "Traps" discovered during the development of Project Nexus.

---

### 🏮 Trap 1: The "Empty Response" (Context & Refusal)
**Symptom:** The AI returns an empty string or just "..."
- **Cause A (Context Overflow):** You sent too much data (e.g., a massive code block) and exceeded the model's context window. The model "crashed" silently.
- **Cause B (Prompt Refusal):** The model didn't understand the prompt or found it too complex to start.
- **The Fix:**
    - Reduce `max_tokens` to force conciseness.
    - Simplify the prompt (e.g., "List 3 flaws" instead of "Analyze this entire project").
    - Lower the `temperature` (0.1) to make it more focused.

### 🏮 Trap 2: The "400 BadRequest" (Template Collision)
**Symptom:** `openai.BadRequestError: No user query found in messages.`
- **Cause:** Local servers (LM Studio/Ollama) use **Jinja Templates** that require a strict alternating pattern: **User -> Assistant -> User**. If you send two "User" messages in a row (e.g., in a complex orchestration loop), the template engine fails.
- **The Fix:** Always ensure your `messages` list follows the `U -> A -> U -> A` pattern. Use a "system" message at the very top.

### 🏮 Trap 3: The "Runaway Agent" (Over-generation)
**Symptom:** The AI generates 5,000+ tokens and starts repeating itself or writing irrelevant text.
- **Cause:** `temperature` is too high (0.7+) or no `max_tokens` limit was set.
- **The Fix:** 
    - Always set a `max_tokens` limit (e.g., 500 for reviews, 1500 for code).
    - Use `temperature=0.0` or `0.1` for logic-heavy tasks like reviews.

### 🏮 Trap 4: The "JSON Hygiene" Issue
**Symptom:** `json.loads()` fails because of extra text or backticks.
- **Cause:** Models love to add "Sure! Here is your JSON:" before the actual data.
- **The Fix:** Use "Defensive Parsing" in your Python code:
    ```python
    start = raw_output.find("{")
    end = raw_output.rfind("}")
    clean_json = raw_output[start:end+1]
    ```

---

### 🎓 The Golden Rule:
If an agent fails, don't just "try again." **Inspect the raw logs.** Look at exactly what was sent and exactly what was received. AI Engineering is 10% prompting and 90% building robust wrappers.
