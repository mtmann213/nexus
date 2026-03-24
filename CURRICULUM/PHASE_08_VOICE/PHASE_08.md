# Phase 8: The Voice (Speech-to-Text Mastery)
## Subject: High-Speed Audio Capture and Local Transcription

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Implement** a local audio capture link between Windows and WSL using `ffmpeg`.
2. **Utilize** the **Whisper** model family for sub-second text transcription.
3. **Analyze** the latency of the "Voice-to-Prompt" pipeline.
4. **Optimize** audio sampling rates and bit-depth for efficient AI ingestion.
5. **Differentiate** between Cloud-based STT and local neural transcription.

---

### 📖 Technical Deep Dive

#### 1. The Acoustic Interface (The "Ear")
To communicate at the speed of thought, we need to bypass the keyboard. 
* **The Stack:** We use **PulseAudio** to bridge your Windows microphone into the Linux environment. 
* **The Demodulator:** **faster-whisper** acts as our digital decoder, turning raw PCM audio data into semantic text tokens.

#### 2. Sub-Second Latency
For a voice interface to be useful for coding, the transcription must happen in near real-time. 
* **Strategy:** We use the **Whisper-Tiny** model. While it has fewer parameters than the "Large" model, its speed allows for instant "Voice-to-Terminal" workflows on a 3080 Ti.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **STT** | Speech-to-Text; converting audio waves into text data. | **Demodulation**. |
| **PCM** | Pulse Code Modulation; raw digital audio format. | **Baseband Signal**. |
| **Whisper** | A state-of-the-art neural network for speech recognition. | A high-fidelity **Signal Processor**. |
| **Sampling Rate** | The number of samples of audio carried per second (e.g., 16kHz). | **Sampling Frequency (Fs)**. |

---

### 🧪 Lab Reference: `LABS/voice_to_text.py`

#### What to expect:
You will run the script, speak for 5 seconds, and watch the AI instantly print your prompt in the terminal. This allows you to "Talk to your Codebase" by pasting the transcribed text directly into OpenCode.

#### Generation Prompt (for the student):
> "Write a Python script that uses `ffmpeg` to capture 5 seconds of audio from the system's pulse source. Then, use the `faster-whisper` library to transcribe that audio on the CPU using the 'tiny' model. The script should output the final text clearly for use in an AI prompt."

---

### ✅ Success Criteria
* **Proof of Work:** Student successfully transcribes a 5-second voice command into the terminal in under 1.0 second of processing time.
