# Phase 10: The Link (Local Network Access)
## Subject: LAN Bridging and Mobile Device Integration

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Bridge** the gap between the high-power Desktop "Base Station" and mobile "User Equipment" (Phone/Tablet) over the local network.
2. **Configure** local firewalls (ufw/Windows Firewall) to allow traffic on specific AI ports (1234, 8080).
3. **Optimize** LM Studio settings for "Serve on Local Network" visibility.
4. **Deploy** a mobile-responsive web frontend (e.g., Open WebUI or a custom Streamlit app) accessible via local IP.
5. **Implement** (Bonus) a secure remote tunnel using **Tailscale** for access outside the home network.

---

### 📖 Technical Deep Dive

#### 1. The Base Station vs. User Equipment (LAN Topology)
In RF, the Base Station handles the heavy signal processing, while the User Equipment (UE) provides the interface. 
* **The Desktop:** Your 3080 Ti is the signal processor. It hosts the LLMs and the Blackboard (`AGENTS.md`).
* **The UE:** Your phone or tablet acts as the "Remote Display." 
* **The Link:** We use the local Wi-Fi network as our primary data link. This requires knowing your desktop's local IP (e.g., `192.168.1.50`).

#### 2. Port Visibility & Firewalls
By default, most operating systems block incoming connections to protect you. To make the Link work, you must open "Ports":
* **Port 1234:** The standard entry point for LM Studio.
* **The Fix:** We learn to set up "Allow Rules" that specifically permit your phone's IP to talk to your desktop's AI ports.

#### 3. 🌟 Bonus: The Long-Range Link (Tailscale)
Once the local link is solid, we can extend the range.
* **The Tech:** **Tailscale** creates an encrypted "Virtual Ethernet Cable." It allows your phone to talk to your desktop as if it were on the local Wi-Fi, even when you are on a cellular data link (5G).

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Local IP** | The address of your device within your home network. | A **Station ID** in a local net. |
| **Port** | A specific logical "gate" used for data (e.g., 1234). | A **Channel Number** or Frequency Bin. |
| **LAN** | Local Area Network; your home/office Wi-Fi and Ethernet. | A **Local Cell** or Pico-cell. |
| **Firewall** | A security system that controls incoming/outgoing traffic. | An **RF Band-pass Filter**. |
| **Tunneling** | Encapsulating data to move it across a network securely. | **Sub-carrier Modulation**. |

---

### ❓ Comprehension Questions
1. Why does "localhost" only work on the desktop itself and not from your phone?
2. What is the command to find your local IP address on a Linux system?
3. How does a firewall act like a "Band-pass Filter" for network traffic?
4. What is the security risk of opening port 1234 to the *entire* internet instead of just your local network?
5. (Bonus) How does Tailscale solve the problem of "NAT Traversal"?

---

### 🧪 Lab Reference: `LABS/local_link_test.sh`

#### What to expect:
You will find your local IP, configure your desktop server to "Serve on Local Network," and then use your phone's browser to hit the desktop's IP address. Success is when you see the "LM Studio API" status page on your mobile device.

#### Generation Prompt (for the student):
> "Write a bash script that detects the local IP address of the host, checks if port 1234 is currently listening for external connections, and provides a QR code or URL that a user can scan with their phone to test the connection to the AI Base Station."

---

### ✅ Success Criteria
* **Proof of Work:** The student sends a prompt from a mobile browser (on the same Wi-Fi) and sees the 3080 Ti generate a response in real-time.
