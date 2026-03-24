# Phase 3: The Hand (Agency)
## Subject: Function Calling, Tool Use, and System Directives

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** "Function Calling" and explain how JSON acts as the AI's "nervous system."
2. **Implement** a manual Tool-Use loop using structured JSON signaling.
3. **Apply** **System Directives** to "Anchor" the AI and prevent prompt drift during complex tasks.
4. **Construct** a Multi-Tool Agent capable of performing sequential tasks (e.g., write a file, then run it).
5. **Analyze** the impact of **Context Poisoning** and how to protect the agent's core mission.

---

### 📖 Technical Deep Dive

#### 1. Function Calling (The Motor Cortex)
Until this phase, the AI was a "Brain in a Jar"—it could think but not touch. **Function Calling** is the mechanism where the model generates a structured instruction (usually JSON) that your code then executes.
* **The Analogy:** In biology, your brain sends an electrical impulse to your hand to pick up a tool. In AI, the model sends a JSON packet like `{"action": "create_file", "filename": "test.py"}` to your Python script.

#### 2. System Directives & Anchoring
As a conversation grows, the AI can suffer from "Context Poisoning," where the immediate chat history distracts it from its original goal.
* **The Strategy:** We use **System Directives** (the "System Prompt") to anchor the AI. This is a fixed set of instructions that remains at the top of the context window, regardless of how long the chat becomes.
* **Key Insight:** Without a strong directive, an AI agent might start "chatting" instead of "executing" tools.

#### 3. Defensive JSON Parsing
We discovered that models often wrap their JSON in backticks (```json ... ```) or add conversational filler. 
* **The Solution:** We implemented "Defensive Parsing" by hunting for the first `{` and the last `}` in the model's output. This makes the agent's "Hands" more resilient to "Mental Noise" from the brain.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Function Calling** | The process where an AI outputs structured data to trigger a specific code function. | **Command Logic** sent to a USRP. |
| **System Directive** | A high-priority instruction that defines the AI's core behavior and constraints. | **Firmware Hard-Coding**. |
| **Anchoring** | Keeping the AI focused on a specific task despite growing context noise. | **Frequency Locking** or Sync. |
| **Context Poisoning** | When irrelevant data in the context window degrades the AI's reasoning. | **Interference/Noise** in the channel. |
| **Agency** | The capacity of an AI to interact with its environment. | **Actuation**. |

---

### ❓ Comprehension Questions
1. Why is JSON used for function calling instead of plain English sentences?
2. What is the difference between a "User Message" and a "System Directive" in terms of priority?
3. How does "Anchoring" help an agent complete a 10-step task without getting distracted?
4. What is "Context Poisoning," and what is one way to mitigate it?
5. Why is robust JSON parsing considered a "Defensive Engineering" practice?

---

### 🧪 Lab Reference: `LABS/agent_simple.py` & `LABS/agent_multitool.py`

#### What to expect:
1. **`agent_simple.py`**: This script takes a request to create an RF tool (like a wavelength calculator) and outputs a JSON command. The script then captures that JSON and creates a real `.py` file on your disk.
2. **`agent_multitool.py`**: This is a multi-step loop. The agent will create a calculator script, execute it using the terminal, and read the result to confirm it works. You will see the agent "Think" and "Act" across multiple turns.

#### Generation Prompt (for the student):
> "Build an autonomous agent loop in Python. The agent should have access to two tools: `create_file(filename, content)` and `run_terminal_command(command)`. Use a system prompt to instruct the AI to respond ONLY with JSON objects representing these actions. Write the Python logic to parse the JSON (using defensive indexing for `{` and `}`), execute the tool, and feed the result back into the message history so the agent can see its own progress."

---

### ✅ Success Criteria
* **Proof of Work:** `agent_multitool.py` successfully executes a multi-step loop without losing track of its original mission, even after receiving multiple tool results.
