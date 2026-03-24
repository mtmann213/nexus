# Phase 1: The Foundation
## Subject: Inference, Tokens, and the Physical Layer of AI

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** a "Token" and explain how it relates to RF sampling.
2. **Understand** the "Context Window" as a sliding observation buffer.
3. **Measure** model throughput using Tokens Per Second (t/s).
4. **Configure** a local inference server (LM Studio) to bridge with a WSL/Linux environment.
5. **Initialize** the **OpenCode Interface** to establish a real-time terminal connection with the local 35B model.

---

### 📖 Technical Deep Dive

#### 1. Tokens (The Samples of Language)
In AI, text is not processed as words, but as **Tokens**. 
* **Key Insight:** A 1,000-token prompt is essentially a 1,000-sample buffer.

#### 2. The Context Window (The Observation FFT)
The Context Window is the maximum number of tokens a model can "see" at once.

#### 3. Throughput (The AI Baud Rate)
We establish a performance baseline for the local 3080 Ti.

#### 4. The Interface (OpenCode)
Before we can build agents, we need a "Pilot's Seat." **OpenCode** is a terminal-based interface that allows you to chat with your local model and gives that model permission to read/write files in your project.
* **Why it matters:** In the following phases, you will use OpenCode to *write* your scripts instead of coding them manually.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Token** | The atomic unit of data processed by an LLM. | A **Sample** in an IQ stream. |
| **Context Window** | The sliding buffer of tokens the model can reference. | An **Observation Window**. |
| **OpenCode** | A terminal-native AI interface for coding. | The **Control Console** or Cockpit. |
| **Quantization** | Reducing the precision of model weights to save VRAM. | **Bit-Depth Reduction**. |

---

### 🧪 Lab Reference: `LABS/benchmark_inference.py` & OpenCode Init

#### What to expect:
1. **Inference Test:** Run the python script to establish your 3080 Ti baseline.
2. **Interface Init:** Run `opencode /init` in your terminal. You will configure it to point to your LM Studio URL (`http://<HOST_IP>:1234/v1`). 

#### Generation Prompt (for the student):
> "Write a Python script to benchmark a local LM Studio inference server. Then, configure an OpenCode session to connect to that same server so we can begin collaborative development."

---

### ✅ Success Criteria
* **Proof of Work:** Student can type a message in the OpenCode terminal and receive a response from their local 35B model.
