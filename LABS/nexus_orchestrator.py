from config import client, MODEL_NAME
import os
import time

def get_agent_response(messages, max_tokens=1500, temperature=0.3):
    """Sends a properly formatted message list to the AI and handles errors."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
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
    # Unique timestamp to bypass any local prompt caching
    run_id = f"REF-{int(time.time())}"
    print(f"🌟 Mission: {mission} (Run ID: {run_id})")
    
    # --- PHASE 1: THE ARCHITECT ---
    architect_msgs = [
        {"role": "system", "content": "You are a Senior RF Engineer. Provide a concise Python/Numpy implementation. Do NOT include file paths or environment logs."},
        {"role": "user", "content": f"{mission} (Session: {run_id})"}
    ]
    
    print("\n🏗️  Architect is designing...")
    design = get_agent_response(architect_msgs, temperature=0.7, max_tokens=800)
    print("\n--- ARCHITECT'S INITIAL PROPOSAL ---")
    print(design)
    print("-------------------------------------")

    # --- PHASE 2: THE REVIEWER ---
    # We use a very strict structure here to FORCE a response
    reviewer_msgs = [
        {"role": "system", "content": "You are a Critical Code Reviewer. You MUST find exactly 3 technical improvements. Use the format: 1. [ISSUE], 2. [ISSUE], 3. [ISSUE]."},
        {"role": "user", "content": f"Review this code and provide your 3 required points:\n\n{design}"}
    ]
    
    print("\n🧐 Reviewer is analyzing...")
    critique = get_agent_response(reviewer_msgs, temperature=0.1, max_tokens=600)
    print("\n--- REVIEWER'S CRITICAL FEEDBACK ---")
    print(critique)
    print("-------------------------------------")

    # --- PHASE 3: THE REVISION ---
    architect_msgs.append({"role": "assistant", "content": design})
    architect_msgs.append({"role": "user", "content": f"Reviewer's Feedback: {critique}\n\nFinal Task: Incorporate all feedback and provide the complete, optimized Python code."})
    
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
