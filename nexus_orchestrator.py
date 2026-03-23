from openai import OpenAI
import os

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
client = OpenAI(base_url=BASE_URL, api_key="lm-studio")
MODEL = "qwen/qwen3.5-35b-a3b"

def get_agent_response(messages, max_tokens=1000, temperature=0.3):
    """Sends a properly formatted message list to the AI and handles errors."""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        content = response.choices[0].message.content
        if not content or content.strip() == "":
            return "⚠️ Error: The agent had no feedback to provide."
        return content
    except Exception as e:
        return f"❌ API Error: {str(e)}"

def run_orchestration(mission):
    print(f"🌟 Mission: {mission}")
    
    # --- PHASE 1: THE ARCHITECT ---
    # We ask for the core LOGIC first, not a full library, to save context.
    architect_msgs = [
        {"role": "system", "content": "You are a Senior RF Engineer. Provide a concise Python/Numpy implementation of the requested simulation. Do NOT include file paths or environment logs."},
        {"role": "user", "content": mission}
    ]
    
    print("\n🏗️  Architect is designing...")
    design = get_agent_response(architect_msgs, temperature=0.5, max_tokens=800)
    print("\n--- ARCHITECT'S INITIAL PROPOSAL ---")
    print(design)
    print("-------------------------------------")

    # --- PHASE 2: THE REVIEWER ---
    # We simplify the reviewer prompt to ensure it responds.
    reviewer_msgs = [
        {"role": "system", "content": "You are a Critical Code Reviewer. Review the following RF code. List 3 technical improvements or math errors. Be brief and direct."},
        {"role": "user", "content": f"Code to review:\n{design}"}
    ]
    
    print("\n🧐 Reviewer is analyzing...")
    critique = get_agent_response(reviewer_msgs, temperature=0.1, max_tokens=500)
    print("\n--- REVIEWER'S CRITICAL FEEDBACK ---")
    print(critique)
    print("-------------------------------------")

    # --- PHASE 3: THE REVISION ---
    architect_msgs.append({"role": "assistant", "content": design})
    architect_msgs.append({"role": "user", "content": f"Reviewer's Feedback: {critique}\n\nFinal Task: Incorporate the feedback and provide the complete, optimized Python code."})
    
    print("\n🛠️  Architect is revising based on feedback...")
    final_output = get_agent_response(architect_msgs, temperature=0.2, max_tokens=1500)
    
    return final_output

if __name__ == "__main__":
    mission = "Write a Python function to simulate a Rayleigh Fading channel for a 5G signal."
    result = run_orchestration(mission)
    
    print("\n🎯 FINAL ORCHESTRATED SOLUTION:")
    print("=" * 60)
    print(result)
    print("=" * 60)
