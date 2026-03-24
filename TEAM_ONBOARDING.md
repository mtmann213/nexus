# 🚀 Project Nexus: Team Onboarding Guide
## AI Mastery via Construction (Hardware: Native Ubuntu 24.04 / 8GB VRAM P2000)

Welcome to the team! This guide will help you set up your local "AI Command Center." We learn by **building**, not just reading. 

---

### 1. The "Engine Room" (Inference Options)

Project Nexus is designed to be hardware-agnostic. You can switch between your local GPU and the Cloud by editing **just one file**: `LABS/config.py`.

#### Option A: Local (Recommended for 8GB+ VRAM)
If you have an NVIDIA GPU (P2000 or better):
1.  **Install LM Studio (Linux):** Download the AppImage from [lmstudio.ai](https://lmstudio.ai/).
2.  **Server Setup:** Ensure "Serve on Local Network" is checked.
3.  **Config:** Open `LABS/config.py`. Ensure `GROQ_KEY` is empty. The project will automatically use your local GPU.

#### Option B: The Cloud Bridge (For Low-Power Laptops)
If you do NOT have a dedicated GPU, use **Groq** for near-instant inference:
1.  **Sign up:** Go to [console.groq.com](https://console.groq.com/) and get an API Key.
2.  **Enable:** Run this in your terminal: `export GROQ_API_KEY="your_key_here"`.
3.  **Config:** Project Nexus will detect the key and automatically switch all labs to use the Groq Cloud.

---

### 2. The "Interface" (The Mentor)
We use a Cloud-based CLI (like **Gemini CLI**, **Claude Code**, or **Aider**) to act as the "Lead Research Mentor."

1.  **Install the Tool:** 
    - Ensure you have Node.js: `sudo apt install nodejs npm`.
    - Install the CLI: (e.g., `npm install -g @google/gemini-cli`).
2.  **The Handshake:** 
    - In your CLI settings, point your "Local Model" to your IP address (usually `localhost` or your WSL bridge IP).

---

### 3. Your First Mission: The Inference Baseline
Copy the `PROJECT_NEXUS_MANIFEST.md` from this repo and tell your AI Mentor:

> "I am ready to begin Project Nexus. I have my inference engine running. 
> Assign my first task: Build a script to measure my inference speed (Tokens/Sec)."

---

### 💡 Why this works:
- **Universal Switch:** The `LABS/config.py` handles all the API plumbing. You don't have to change your code when switching from local to cloud.
- **Learn by Doing:** You won't just 'use' AI; you will build the scripts that connect the AI to your local hardware and files.

### ⚠️ Pro-Tips: Avoiding the "Engineering Traps"
1.  **JSON Hygiene:** Use "Defensive Parsing" (see `TROUBLESHOOTING_AI.md`) to handle model noise.
2.  **The Template Rule:** Local servers require strict alternating **User -> Assistant -> User** conversations. 
3.  **VRAM Awareness:** If utilizing local hardware, ensure your model fits 100% in VRAM. Partial offloading will slow the system to a crawl.

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
