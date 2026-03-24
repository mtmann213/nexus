# Phase 1: The Foundation
## Subject: Inference, Tokens, and the Physical Layer of AI

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Define** a "Token" and explain how it relates to RF sampling.
2. **Understand** the "Context Window" as a sliding observation buffer.
3. **Measure** model throughput using Tokens Per Second (t/s).
4. **Configure** a local inference server (LM Studio) to bridge with a WSL/Linux environment.
5. **Analyze** the **Latency-Weight Tradeoff** between Local models (35B) and Frontier models (Cloud).

---

### 📖 Technical Deep Dive

#### 1. Tokens (The Samples of Language)
In AI, text is not processed as words, but as **Tokens**. 
* **The Analogy:** In RF, you sample a continuous wave to get discrete data points. In NLP (Natural Language Processing), the tokenizer "samples" the text. 
* **Key Insight:** A 1,000-token prompt is essentially a 1,000-sample buffer.

#### 2. The Context Window (The Observation FFT)
The Context Window is the maximum number of tokens a model can "see" at once.
* **The Analogy:** Think of it like an **FFT Window Size**. If your window is too small, you lose the "frequency resolution" (coherence) of the entire conversation.
* **The KV Cache:** Storing these tokens in memory consumes VRAM. This is why large context windows (like 128k) require significant hardware.

#### 3. Throughput (The AI Baud Rate)
We established a performance baseline of **~19 t/s** for a 35B model on an RTX 3080 Ti.
* **Insight:** Speed depends on the model's "Parameter Count" and the "Quantization" (compression) used. 19 t/s is fast enough for real-time agentic loops.

#### 4. The Latency-Weight Tradeoff (Local vs. Cloud)
Engineering is the science of trade-offs. 
* **Local (3080 Ti / 35B):** Low cost, high privacy, but limited "weight" (intelligence) and high TTFT (Time-to-First-Token) for complex prompts.
* **Cloud (Frontier Models):** Massive reasoning capability, instant TTFT, but high recurring cost and zero privacy.
* **Decision Matrix:** Use Local for iterative coding and hardware monitoring; use Cloud for high-level architectural research and "Brainstorming."

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Token** | The atomic unit of data processed by an LLM. | A **Sample** in an IQ stream. |
| **Context Window** | The sliding buffer of tokens the model can reference. | An **Observation Window** or Buffer. |
| **Inference** | The act of the model generating an output from an input. | **Demodulation/Decoding**. |
| **Quantization** | Reducing the precision of model weights (e.g., 16-bit to 4-bit). | **Bit-Depth Reduction** or Compression. |
| **Frontier Model** | The most powerful, state-of-the-art models (usually cloud-based). | **Lab-Grade Test Equipment**. |
| **TTFT** | Time-to-First-Token; the latency before the AI starts responding. | **Propagation Delay**. |

---

### ❓ Comprehension Questions
1. Why does a 35B model run faster on a GPU than on a CPU?
2. What happens to the AI's "memory" when the conversation exceeds the Context Window?
3. How does "Quantization" allow a 70GB model to fit into 12GB of VRAM?
4. When should you choose a Cloud model over your local 35B model?
5. How does TTFT impact the user experience of a real-time agent?

---

### 🧪 Lab Reference: `LABS/benchmark_inference.py`

#### What to expect:
When you run this script, it will connect to your local LM Studio instance. It sends a technical RF prompt and monitors the stream of incoming tokens. The final output will display the **Total Time**, **Total Tokens**, and the critical **Tokens Per Second (t/s)** metric.
* **Target Performance:** You should see ~15-20 t/s for a 35B model on your 3080 Ti.

#### Generation Prompt (for the student):
> "Write a Python script to benchmark a local LM Studio inference server at `http://<HOST_IP>:1234/v1`. Use the `openai` library to send a prompt like 'Explain PLL synchronization,' measure the time taken for the complete response, and calculate the Tokens Per Second (t/s) by dividing `completion_tokens` by duration."

---

### ✅ Success Criteria
* **Proof of Work:** `benchmark_inference.py` successfully connects to LM Studio and reports a throughput of > 10 t/s.
