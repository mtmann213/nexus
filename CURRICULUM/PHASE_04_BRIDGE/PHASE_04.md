# Phase 4: The Bridge (MCP)
## Subject: The Model Context Protocol and Tool Security

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Explain** the Model Context Protocol (MCP) and why it replaces "Hard-Wired" tool plumbing.
2. **Differentiate** between an MCP Client and an MCP Server.
3. **Analyze** **Tool Security** and the risks of giving an AI shell access.
4. **Implement** a **Sandbox** or "Human-in-the-Loop" (HITL) safety pattern for MCP tools.
5. **Build** a custom MCP Server in Python to expose local hardware metrics.

---

### 📖 Technical Deep Dive

#### 1. The "USB" of AI (The Standard Bridge)
In Phase 3, we built manual tools. **MCP** is like **USB**. It allows an AI (the Client) to connect to any tool (the Server) and "Discover" what it can do without the developer hard-coding the instructions.

#### 2. Tool Security & Sandboxing
Giving an AI "Hands" (Agency) creates a new **Exploit Surface**. If an AI is tricked by a malicious prompt (Prompt Injection), it could use its tools to delete files or leak sensitive hardware data.
* **The Strategy:** We implement **Sandboxing**—restricting the AI's tools to specific folders (like `/home/dev/nexus`) and requiring **Human-in-the-Loop** approval for dangerous commands (like `rm -rf` or firmware flashes).
* **Key Insight:** A secure bridge is more important than a powerful bridge.

#### 3. Hardware Awareness (The Nexus Server)
We built a custom MCP server (`nexus_hardware_server.py`) that proved that MCP can bridge the gap between "Digital AI" and "Physical Hardware." 

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **MCP** | Model Context Protocol; an open standard for AI-to-tool connectivity. | **VITA 49** or **USB** standard. |
| **Sandboxing** | Restricting an AI's tool access to a safe, isolated environment. | **Galvanic Isolation** or a Faraday Cage. |
| **Prompt Injection** | A technique to hijack an AI's behavior by embedding commands in user input. | **Signal Jamming** or Spoofing. |
| **Exploit Surface** | The total number of points where an attacker can try to enter data or extract it. | **Antenna Aperture** or Port exposure. |
| **HITL** | Human-in-the-Loop; requiring a human to approve an AI's action. | **Manual Override** switch. |

---

### ❓ Comprehension Questions
1. Why is MCP considered "Plug-and-Play" compared to the manual tools we built in Phase 3?
2. What is one risk of giving an AI agent direct access to your `nvidia-smi` tool?
3. How does "Sandboxing" protect your host operating system from a hallucinating AI?
4. What is a "Prompt Injection," and how could it cause an agent to misuse an MCP tool?
5. Why should a professional PICC require "Human-in-the-Loop" approval for terminal commands?

---

### 🧪 Lab Reference: `LABS/nexus_hardware_server.py` & `LABS/mcp_client.py`

#### What to expect:
1. **`nexus_hardware_server.py`**: This script acts as an MCP server. It "Exposes" your RTX 3080 Ti hardware status to any connecting AI. When it runs, it waits for a JSON-RPC handshake over `stdio`.
2. **`mcp_client.py`**: This is the universal bridge. It launches the hardware server, performs the formal MCP handshake, discovers the `get_gpu_status` tool, and executes it. You will see your real VRAM usage printed in the terminal.

#### Generation Prompt (for the student):
> "Write a custom MCP Server in Python using the `mcp` library. The server should provide a tool named `get_gpu_status` that executes the shell command `nvidia-smi` and returns VRAM usage. Then, write an MCP Client script that uses `StdioServerParameters` to launch that server, performs the `session.initialize()` handshake, and calls the tool to display the hardware report."

---

### ✅ Success Criteria
* **Proof of Work:** `mcp_client.py` successfully connects to the hardware server, but the server refuses to provide info for any hardware not explicitly listed in its "Safe Schema."
