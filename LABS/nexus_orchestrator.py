from config import client, MODEL_NAME
import os
import re
import time

def get_agent_response(messages, max_tokens=1500, temperature=0.3):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        content = response.choices[0].message.content
        if not content or content.strip() == "":
            return None
        return content
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return None

def get_research():
    agents_md = "AGENTS.md"
    # Use relative path if local, else absolute for standard environment
    path = agents_md if os.path.exists(agents_md) else "/home/dev/nexus/AGENTS.md"
    
    research_context = {"status": "Unknown", "last_run_id": "None", "design": "None"}

    if not os.path.exists(path):
        return research_context

    with open(path, 'r') as f:
        content = f.read()

    # Robust regex to catch: - **Key**: Value OR - Key: Value
    def extract(key):
        match = re.search(rf"- (?:\*\*)?{key}(?:\*\*)?:\s*(.+)", content, re.IGNORECASE)
        return match.group(1).strip() if match else "Unknown"

    research_context["status"] = extract("Status")
    research_context["last_run_id"] = extract("Last Run ID")
    research_context["design"] = extract("Design")
    
    return research_context

def run_orchestration(mission):
    run_id = f"REF-{int(time.time())}"
    print(f"🌟 Mission: {mission} (Run ID: {run_id})")

    # --- RESEARCH PHASE ---
    ctx = get_research()
    print(f"\n✅ Researcher: Context Loaded.")
    print(f"   Project Status: {ctx['status']}")
    print(f"   Architecture: {ctx['design']}")

    # --- PHASE 1: ARCHITECT ---
    architect_instruction = (
        "SYSTEM: You are a Senior RF Engineer. Provide a concise Python/Numpy implementation.\n"
        f"CONTEXT: Current Status is {ctx['status']}. Previous Design: {ctx['design']}\n"
        f"USER: {mission} (Session: {run_id})"
    )
    
    print("\n🏗️  Architect is designing...")
    design = get_agent_response([{"role": "user", "content": architect_instruction}], temperature=0.7)
    
    if not design:
        print("⚠️ Architect was silent. Using skeleton.")
        design = "def simulate_channel(): pass"
    
    print("\n--- ARCHITECT'S PROPOSAL ---")
    print(design[:300] + "...")

    # --- PHASE 2: THE REVIEWER ---
    reviewer_instruction = (
        "SYSTEM: You are a strict Code Reviewer. You MUST find 3 technical flaws. Be vocal and critical.\n"
        f"USER: Review this code and provide 3 points of feedback:\n{design}"
    )
    
    print("\n🧐 Reviewer is analyzing...")
    # Increase temperature to 0.4 to encourage 'Creative' criticism
    critique = get_agent_response([{"role": "user", "content": reviewer_instruction}], temperature=0.4)
    
    if not critique:
        print("⚠️ Reviewer was silent. Using forced feedback.")
        critique = "1. Optimize math. 2. Add docs. 3. Check normalization."

    print("\n--- CRITICAL FEEDBACK ---")
    print(critique)

    # --- PHASE 3: THE REVISION ---
    final_msgs = [
        {"role": "system", "content": "You are a Master Engineer. Incorporate feedback into final code."},
        {"role": "user", "content": f"Feedback to address: {critique}\n\nProvide the final optimized Python code."},
    ]
    
    print("\n🛠️  Architect is revising...")
    final_output = get_agent_response(final_msgs, temperature=0.2, max_tokens=2000)
    
    return final_output

if __name__ == "__main__":
    mission = "Write a Python function to simulate a Rayleigh Fading channel for a 5G signal."
    result = run_orchestration(mission)
    print("\n🎯 FINAL SOLUTION:")
    print("=" * 60)
    print(result)
    print("=" * 60)
