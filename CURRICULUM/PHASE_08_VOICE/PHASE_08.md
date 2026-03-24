# Phase 8: The Voice (Multimodality)
## Subject: Speech-to-Text, Text-to-Speech, and Low-Latency Interaction

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Differentiate** between Speech-to-Text (STT) and Text-to-Speech (TTS) technologies.
2. **Understand** the concept of "Multimodal Latency" and calculate the Round-Trip Time (RTT) of a voice conversation.
3. **Configure** a local STT engine (e.g., OpenAI Whisper) to "demodulate" human voice into machine text.
4. **Implement** a TTS engine (e.g., Piper or ElevenLabs) to provide auditory feedback from the PICC.
5. **Analyze** the trade-offs between model size and responsiveness in a voice-first interface.

---

### 📖 Technical Deep Dive

#### 1. The Voice Stack (Modulation/Demodulation)
In RF, you modulate a baseband signal onto a carrier to transmit it. In AI Multimodality, we perform a similar conversion:
* **STT (The Demodulator):** This is the **Analog-to-Digital Converter (ADC)** for your voice. A model like **Whisper** takes raw audio waves and "demodulates" them into text tokens.
* **TTS (The Modulator):** This is the **Digital-to-Analog Converter (DAC)**. It takes the AI's text tokens and "modulates" them into synthesized audio waves that sound like human speech.

#### 2. The Latency Wall (RTT)
The biggest challenge in voice AI is **Total Round-Trip Latency**.
* **The Loop:** `[Audio Capture] -> [STT Processing] -> [LLM Reasoning] -> [TTS Generation] -> [Playback]`.
* **The Physics:** If this total loop takes more than **1.5 - 2.0 seconds**, the conversation becomes awkward, similar to a satellite link with high propagation delay.
* **Optimization:** To break the "Latency Wall," we often use smaller, faster models (e.g., 1.5B or 7B) for voice interactions, sacrificing a bit of "IQ" for "Speed."

#### 3. The WSL Impedance Mismatch
Running AI in WSL (Linux) while your Microphone and Speakers are on Windows creates a "Driver Bridge" problem.
* **The Solution:** We learn to use tools like `ffmpeg` or specialized Python libraries to stream audio over the WSL-Host bridge, ensuring the AI can "hear" the local environment.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **STT** | Speech-to-Text; converting audio waves into text data. | **Demodulation** (Audio to Data). |
| **TTS** | Text-to-Speech; converting text data into synthetic audio. | **Modulation** (Data to Audio). |
| **Multimodal** | An AI's ability to process multiple types of data (Text, Image, Sound). | A **Multi-Band** Receiver. |
| **Whisper** | An industry-standard open-source STT model by OpenAI. | A high-performance **DSP Decoder**. |
| **Latency** | The time delay between a user speaking and the AI responding. | **Propagation Delay** or Link Latency. |

---

### ❓ Comprehension Questions
1. Why is "Time-to-First-Token" (TTFT) more important for voice interfaces than for code generation?
2. How does using a quantized model (e.g., 4-bit) help improve the "Natural" feel of a voice conversation?
3. In the "Voice Stack" loop, which component is usually the biggest bottleneck for latency?
4. If your AI is hallucinating in voice mode, should you increase the model size or improve the STT accuracy? Why?
5. What is the difference between "Streaming STT" and "Batch STT," and which one is better for a real-time Command Center?

---

### 🧪 Lab Reference: `LABS/voice_bridge.py` (Draft)

#### What to expect:
(This lab is a future implementation goal). The student will run a script that captures a 5-second audio clip from the microphone, uses a local **Whisper** model to transcribe it, and then uses a **Piper** engine to speak the AI's text response back to the user. You will measure the **Round-Trip Latency** to see if it meets the "Natural Conversation" threshold of < 2.0 seconds.

#### Generation Prompt (for the student):
> "Design a Python workflow for a voice-activated AI assistant. It should use the `faster-whisper` library for local Speech-to-Text and the `piper-tts` library for high-speed local Text-to-Speech. The assistant should capture microphone input, transcribe it, send the text to a local Qwen model for a response, and then speak that response out loud. Include timing logs for each step to calculate the total latency."

---

### ✅ Success Criteria
* **Proof of Work:** (Planned) The user can speak an RF command (e.g., "Check GPU status"), and the AI responds via synthesized voice with the correct VRAM metrics.
