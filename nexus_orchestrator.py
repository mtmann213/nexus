from openai import OpenAI
import os

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
client = OpenAI(base_url=BASE_URL, api_key="lm-studio")
MODEL = "qwen/qwen3.5-35b-a3b"

def get_agent_response(messages, max_tokens=1000, temperature=0.3):
    """Sends a properly formatted message list to the AI."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def run_orchestration(mission):
    print(f"🌟 Mission: {mission}")
    
    # --- PHASE 1: THE ARCHITECT ---
    # We build the conversation for the Architect
    architect_msgs = [
        {"role": "system", "content": "You are a Senior RF Software Architect. Focus on concise, correct Python/Numpy code."},
        {"role": "user", "content": mission}
    ]
    
    print("\n🏗️  Architect is designing...")
    design = get_agent_response(architect_msgs, temperature=0.5, max_tokens=800)
    print("-" * 30)
    print(f"Architect's Initial Design:\n{design[:400]}...")
    print("-" * 30)

    # --- PHASE 2: THE REVIEWER ---
    # We build a DIFFERENT conversation for the Reviewer
    reviewer_msgs = [
        {"role": "system", "content": "You are a strict, concise Code Reviewer. Analyze for flaws in RF physics and math."},
        {"role": "user", "content": f"Please review this design for a Rayleigh Fading channel:\n\n{design}"}
    ]
    
    print("\n🧐 Reviewer is analyzing...")
    critique = get_agent_response(reviewer_msgs, temperature=0.1, max_tokens=400)
    print("-" * 30)
    print(f"Reviewer's Critique:\n{critique[:400]}...")
    print("-" * 30)

    # --- PHASE 3: THE REVISION ---
    # We go BACK to the Architect's conversation and add the critique
    architect_msgs.append({"role": "assistant", "content": design})
    architect_msgs.append({"role": "user", "content": f"The reviewer had this critique: {critique}\n\nPlease provide the final, optimized Python code."})
    
    print("\n🛠️  Architect is revising based on feedback...")
    final_output = get_agent_response(architect_msgs, temperature=0.2, max_tokens=1500)
    
    return final_output

if __name__ == "__main__":
    mission = "Write a Python function to simulate a Rayleigh Fading channel for a 5G signal."
    result = run_orchestration(mission)
    
    print("\n🎯 FINAL ORCHESTRATED SOLUTION:")
    print("=" * 50)
    print(result)
    print("=" * 50)
