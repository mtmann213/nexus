from config import client, MODEL_NAME
import os
import re
import time

def get_agent_response(messages, max_tokens=4000, temperature=0.3):
    """Sends a properly formatted message list and handles Reasoning Models."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Check for standard content
        content = response.choices[0].message.content
        
        # Check for 'Thinking' content (for models like DeepSeek R1 or Qwen 3.5 Reasoning)
        reasoning = getattr(response.choices[0].message, 'reasoning_content', None)
        
        if reasoning:
            print(f"\n🧠 [Internal Monologue]:\n{reasoning[:300]}...")

        if not content or content.strip() == "":
            if reasoning:
                return f"⚠️ Model spent all tokens thinking. Summary of thoughts: {reasoning[:200]}"
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
    print(f"🌟 Mission: {mission}")

    # --- PHASE 1: THE ARCHITECT ---
    # Simplified: No complex context, just the mission.
    print("\n🏗️  Architect is designing...")
    design = get_agent_response([
        {"role": "system", "content": "You are a Senior RF Engineer. Provide a concise Python/Numpy script. CODE ONLY."},
        {"role": "user", "content": mission}
    ], temperature=0.7)
    
    if not design:
        print("❌ CRITICAL: Architect failed to respond. Check LM Studio logs.")
        return
    
    print("\n--- ARCHITECT'S PROPOSAL ---")
    print(design[:300] + "...")

    # --- PHASE 2: THE REVIEWER ---
    print("\n🧐 Reviewer is analyzing...")
    critique = get_agent_response([
        {"role": "system", "content": "You are a strict Code Reviewer. Find 2 technical math errors in this code. Be brief."},
        {"role": "user", "content": f"Code:\n{design}"}
    ], temperature=0.1)
    
    if not critique:
        print("❌ CRITICAL: Reviewer failed to respond.")
        return

    print("\n--- CRITICAL FEEDBACK ---")
    print(critique)

    # --- PHASE 3: THE REVISION ---
    print("\n🛠️  Architect is revising...")
    final_output = get_agent_response([
        {"role": "system", "content": "You are a Master Engineer. Rewrite the code to address the feedback."},
        {"role": "user", "content": f"Feedback: {critique}\n\nProvide the final code."}
    ], temperature=0.2, max_tokens=2000)
    
    return final_output

if __name__ == "__main__":
    mission = "Write a Python function to simulate a Rayleigh Fading channel for a 5G signal."
    result = run_orchestration(mission)
    print("\n🎯 FINAL SOLUTION:")
    print("=" * 60)
    print(result)
    print("=" * 60)
