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
3.  **Config:** Open `LABS/config.py`. Ensure `GROQ_KEY` is empty.

#### Option B: The Cloud Bridge (For Low-Power Laptops)
If you do NOT have a dedicated GPU, use **Groq**:
1.  **Sign up:** Go to [console.groq.com](https://console.groq.com/).
2.  **Enable:** Run: `export GROQ_API_KEY="your_key_here"`.

---

### 2. The IDE & Interface (The Cockpit)
To effectively build your Command Center, you need a robust code editor. We highly recommend **VS Code** or **Antigravity**.

1. **Repository Import:** 
    - Navigate to the project folder (`/Ubuntu/home/dev/nexus`).
    - Run `code .` to open the repository in **VS Code**, or open it directly via **Antigravity**.
2. **The "Mentor" (Gemini CLI in VS Code):**
    - To get real-time guidance directly within your editor, install the Gemini extension.
    - In VS Code, go to the Extensions tab (`Ctrl+Shift+X`), search for "Gemini Code Assist" (or the relevant Gemini extension), and install it. This allows the Mentor to see your workspace context.
3.  **The "Executor" (OpenCode / Local AI):** An autonomous terminal agent.
    - **Install:** `curl -fsSL https://opencode.ai/install | bash`
    - **Initialize:** Run `opencode /init` in this folder. Point it to your LM Studio URL.

---

### 3. Audio Infrastructure (For Phase 8)
To use the Voice-to-Text interface in WSL, you must bridge your Windows microphone:
1.  **Install ffmpeg (Linux):** `sudo apt update && sudo apt install -y ffmpeg`
2.  **WSL Audio Bridge:** Most modern WSL versions (Windows 11) bridge PulseAudio automatically. If your mic fails, check the `TROUBLESHOOTING_AI.md`.

---

### 4. Your First Mission: The Interface Handshake
Open your **OpenCode** terminal and type:
> "Hello. You are my local developer. Confirm you can see the files in this directory."

Then, run the benchmark:
`./venv/bin/python LABS/benchmark_inference.py`

---

### 💡 Why this works:
- **Immediate Collaboration:** By setting up OpenCode in Phase 1, you can use the AI to help you write the complex scripts in later phases.
- **Universal Switch:** The `LABS/config.py` handles all the API plumbing. 

### ⚠️ Pro-Tips: Avoiding the "Engineering Traps"
1.  **JSON Hygiene:** Use "Defensive Parsing" to handle model noise.
2.  **The Template Rule:** Ensure strict alternating User/Assistant conversations.
3.  **VRAM Awareness:** Ensure your model fits 100% in VRAM for optimal speed.

---

### 🏛️ The Curriculum (Full Roadmap)
1. **Phase 1: The Foundation** (Inference & OpenCode Setup)
2. **Phase 2: The Librarian** (Embeddings & RAG)
3. **Phase 3: The Hand** (Agency & System Directives)
4. **Phase 4: The Bridge** (MCP & Security)
5. **Phase 5: The Rig** (Harness Engineering)
6. **Phase 6: The Council** (Orchestration & Evals)
7. **Phase 7: The Master** (Skills Mastery)
8. **Phase 8: The Voice** (Multimodality - Elective)
9. **Phase 9: The Forge** (Tiered Team Engineering)
10. **Phase 10: The Link** (Visual Web Portals)

Welcome to the future of RF Engineering!
