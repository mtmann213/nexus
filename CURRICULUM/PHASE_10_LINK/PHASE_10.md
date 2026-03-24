# Phase 10: The Link (Local Web Portal)
## Subject: Visual Interface Deployment and Mobile Interaction

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Deploy** a professional Web User Interface (WUI) such as **Open WebUI** or the **OpenCode Web Interface**.
2. **Bridge** the Desktop "Base Station" to a mobile "User Equipment" (Phone/Tablet) with a fully interactive visual dashboard.
3. **Configure** cross-origin resource sharing (CORS) and port visibility to allow the browser to control the 3080 Ti.
4. **Manage** agentic "Thoughts" and "File Trees" via a touch-optimized mobile interface.
5. **Implement** (Bonus) secure remote access via **Tailscale** to use the Web Portal outside the home network.

---

### 📖 Technical Deep Dive

#### 1. The UX Link (Chatbot vs. Command Center)
A terminal is great for development, but a **Web Portal** is necessary for a "Command Center" feel. 
* **The Interface:** We move beyond raw text to a **Single Page Application (SPA)** that runs in your mobile browser.
* **Open WebUI:** Provides a desktop-class experience on a tablet, including model switching, document uploads (RAG), and real-time inference monitoring.
* **OpenCode Web:** Allows you to see the "Agentic Loops" (Plan -> Act -> Validate) in a structured visual layout.

#### 2. Networking Topology (The Control Plane)
In RF, the Control Plane manages the signaling. In Phase 10, we establish the Web Control Plane:
* **The Backend:** LM Studio / Ollama running on port 1234/11434.
* **The Frontend:** Open WebUI running on port 3000 (usually via Docker).
* **The Link:** Your tablet connects to `http://<DESKTOP_IP>:3000`.

#### 3. Mobile-Responsive Interaction
We specifically focus on interfaces that adapt to touch-screens, allowing you to trigger "The Forge" (Phase 9) or "The Council" (Phase 6) while away from your desk.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **WUI** | Web User Interface; the visual dashboard for the AI. | A **Graphic Spectrum Display**. |
| **CORS** | Cross-Origin Resource Sharing; security settings for browser-to-API talk. | **Signal Handshaking**. |
| **Docker** | A container system used to easily deploy web portals like Open WebUI. | A **Modular Sub-system**. |
| **Mobile-Responsive** | Design that automatically scales for phones and tablets. | **Adaptive Bandwidth**. |

---

### ❓ Comprehension Questions
1. How does a Web Portal like Open WebUI differ from a simple `curl` command to the API?
2. Why is Docker the preferred method for deploying these complex AI interfaces?
3. What is the benefit of seeing the AI's "Thought Process" visually rather than just the final answer?
4. How do you ensure your tablet has permission to talk to the LM Studio server on your desktop?
5. (Bonus) How does Tailscale protect your Web Portal from the open internet?

---

### 🧪 Lab Reference: `LABS/deploy_portal.sh` (Planned)

#### What to expect:
You will run a script that launches **Open WebUI** using Docker. You will then configure it to point to your LM Studio API. Finally, you will open your tablet's browser and log into your own private "Nexus Portal."

#### Generation Prompt (for the student):
> "Write a bash script to deploy Open WebUI via Docker. The script should pull the latest image, map port 3000 to the host, and set the `OPENAI_API_BASE_URL` to point to the local LM Studio instance. Include a check to ensure the 3080 Ti drivers are visible to the container for GPU acceleration."

---

### ✅ Success Criteria
* **Proof of Work:** The student interacts with their Project Nexus agent via a tablet browser, successfully browsing files and triggering a local inference run.
