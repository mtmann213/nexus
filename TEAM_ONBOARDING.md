# 🚀 Project Nexus: Team Onboarding Guide
## AI Mastery via Construction (Hardware: Native Ubuntu 24.04 / 8GB VRAM P2000)

Welcome to the team! This guide will help you set up your local "AI Command Center" on your native Ubuntu 24.04 workstation. We learn by **building**, not just reading. 

---

### 1. The "Engine Room" (Inference Options)

#### Option A: Local (Recommended for 8GB+ VRAM)
If you have an NVIDIA GPU (P2000 or better):
1.  **Install LM Studio (Linux):** Download the AppImage from [lmstudio.ai](https://lmstudio.ai/).
2.  **Model:** Llama-3.1-8B-Instruct (Q4_K_M).
3.  **Endpoint:** `http://localhost:1234/v1`.

#### Option B: The Cloud Bridge (For Low-Power Laptops)
If you do NOT have a dedicated GPU, you can use a high-speed cloud provider. This is free/low-cost and uses the same code:
1.  **Sign up for Groq:** Go to [console.groq.com](https://console.groq.com/) and get an API Key.
2.  **Update your Labs:** In your `.py` files, change:
    - `BASE_URL = "https://api.groq.com/openai/v1"`
    - `api_key = "YOUR_GROQ_API_KEY"`
    - `MODEL = "llama-3.1-8b-instant"`

---

### 2. The "Interface" (The Mentor)
We use a Cloud-based CLI (like **Gemini CLI**, **Claude Code**, or **Aider**) to act as the "Lead Research Mentor."

1.  **Install the Tool:** 
    - Ensure you have Node.js: `sudo apt install nodejs npm`.
    - Install the CLI: (e.g., `npm install -g @google/gemini-cli`).
2.  **The Handshake:** Unlike WSL, "localhost" actually means "localhost" here.
    - Your local API endpoint is simply: `http://localhost:1234/v1`.

---

### 3. Your First Mission: The Inference Baseline
Copy the `PROJECT_NEXUS_MANIFEST.md` from this repo and tell your AI Mentor:

> "I am ready to begin Project Nexus. I have LM Studio running with Llama-3 8B. 
> Assign my first task: Build a script to measure my inference speed (Tokens/Sec)."

---

### 💡 Why this works:
- **Native Linux:** You avoid the "WSL Bridge" latency. Your code talks directly to the GPU.
- **8GB VRAM:** Using an 8B model at Q4/Q5 quantization uses ~5-6GB of VRAM, leaving room for your context window.

### ⚠️ Pro-Tips: Avoiding the "Engineering Traps"
1.  **JSON Hygiene:** If you build an agent, always use `start = output.find("{")` and `end = output.rfind("}")` to extract JSON. Models often add conversational "noise" around their data.
2.  **The Template Rule:** Your AI server expects a strict alternating conversation. If you send two "User" messages in a row, it will throw a `400 BadRequestError`. Always alternate User/Assistant/User.
3.  **The "VRAM is King" Rule:** Do NOT use "Partial Offload" to System RAM. It will slow your mentor down to 1 token/second. Use **Mistral Nemo 12B** or **Llama 3.1 8B**; they fit entirely in 8GB.
4.  **Virtual Environments:** Always run your code in a `venv`. Ubuntu 24.04 blocks global `pip` installs to protect the OS.

---

### 🏛️ The Curriculum (Full Roadmap)
1. **Phase 1: The Foundation** (Inference, Tokens, & Tradeoffs)
2. **Phase 2: The Librarian** (Embeddings & RAG)
3. **Phase 3: The Hand** (Agency & System Directives)
4. **Phase 4: The Bridge** (MCP & Security)
5. **Phase 5: The Rig** (Harness Engineering)
6. **Phase 6: The Council** (Orchestration & Evals)
7. **Phase 7: The Master** (Skills & OpenCode)
8. **Phase 8: The Voice** (Multimodality - Elective)

Welcome to the future of RF Engineering!
