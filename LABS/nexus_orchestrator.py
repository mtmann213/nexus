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
            return None # Return None to trigger retry/error handling
        return content
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return None

def run_orchestration(mission):
    run_id = f"REF-{int(time.time())}"
    print(f"🌟 Mission: {mission} (Run ID: {run_id})")
    
    # --- PHASE 1: THE ARCHITECT ---
    # Merge System and User into a single message for maximum local reliability
    architect_instruction = (
        "SYSTEM: You are a Senior RF Engineer. Provide a concise Python/Numpy implementation.\n"
        f"USER: {mission} (Session: {run_id})"
    )
    
    print("\n🏗️  Architect is designing...")
    design = get_agent_response([{"role": "user", "content": architect_instruction}], temperature=0.7)
    
    if not design:
        print("⚠️ Architect was silent. Using default skeleton.")
        design = "def simulate_channel(): pass # Initial draft failed"
    
    print("\n--- ARCHITECT'S INITIAL PROPOSAL ---")
    print(design[:500] + "...")
    print("-------------------------------------")

    # --- PHASE 2: THE REVIEWER ---
    reviewer_instruction = (
        "SYSTEM: You are a Critical Code Reviewer. List 3 required technical improvements.\n"
        f"USER: Review this code:\n{design}"
    )
    
    print("\n🧐 Reviewer is analyzing...")
    critique = get_agent_response([{"role": "user", "content": reviewer_instruction}], temperature=0.1)
    
    if not critique:
        print("⚠️ Reviewer was silent. Forcing critical feedback.")
        critique = "1. Performance optimization needed. 2. Add docstrings. 3. Verify math."

    print("\n--- REVIEWER'S CRITICAL FEEDBACK ---")
    print(critique)
    print("-------------------------------------")

    # --- PHASE 3: THE REVISION ---
    # The final turn usually works best with the full U->A->U sequence
    final_msgs = [
        {"role": "system", "content": "You are a Master Engineer. Address the critique and provide final code."},
        {"role": "user", "content": f"Initial Design: {design}"},
        {"role": "assistant", "content": "I have received the design."},
        {"role": "user", "content": f"Reviewer Feedback: {critique}\n\nFinal Task: Provide optimized Python code."}
    ]
    
    print("\n🛠️  Architect is revising based on feedback...")
    final_output = get_agent_response(final_msgs, temperature=0.2, max_tokens=2000)
    
    return final_output

if __name__ == "__main__":
    mission = "Write a Python function to simulate a Rayleigh Fading channel for a 5G signal."
    result = run_orchestration(mission)
    
    print("\n🎯 FINAL ORCHESTRATED SOLUTION:")
    print("=" * 60)
    print(result)
    print("=" * 60)
