import json
from config import client, MODEL_NAME, TIMEOUT
import os

def get_response(messages, temp=0.3):
    # Use the TIMEOUT from config
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temp,
        max_tokens=1000,
        timeout=TIMEOUT
    )
    return response.choices[0].message.content

def run_cognitive_harness(mission):
    print(f"🚀 Mission: {mission}")
    
    # STEP 1: THE INITIAL DRAFT
    print("\n📝 [Harness] Enforcing Step 1: Initial Draft...")
    draft_messages = [
        {"role": "system", "content": "You are a professional Python developer. Provide a functional solution."},
        {"role": "user", "content": mission}
    ]
    draft = get_response(draft_messages, temp=0.7)
    print(f"--- DRAFT COMPLETE ---\n{draft[:200]}...")

    # STEP 2: THE SELF-REFLECTION
    print("\n🧐 [Harness] Enforcing Step 2: Critical Self-Reflection...")
    reflect_messages = [
        {"role": "system", "content": "You are a strict code auditor. Find 3 potential bugs, performance bottlenecks, or RF physics errors in the provided code. Be brutal."},
        {"role": "user", "content": f"Review your own code:\n{draft}"}
    ]
    critique = get_response(reflect_messages, temp=0.1)
    print(f"--- SELF-CRITIQUE ---\n{critique}")

    # STEP 3: THE FINAL POLISH
    print("\n🛠️ [Harness] Enforcing Step 3: Final Integration...")
    final_messages = [
        {"role": "system", "content": "You are a Master Engineer. Rewrite the code to address the critique."},
        {"role": "user", "content": f"Original Mission: {mission}\n\nInitial Draft: {draft}\n\nYour Critique: {critique}\n\nPlease provide the final, bulletproof code."}
    ]
    final_version = get_response(final_messages, temp=0.2)
    return final_version

if __name__ == "__main__":
    mission = "Write a Python script to calculate the Link Budget for a 5G mmWave link at 28GHz, including rain attenuation."
    final_result = run_cognitive_harness(mission)
    print("\n🎯 HARNESS OUTPUT (Final Peer-Reviewed Version):")
    print("=" * 60)
    print(final_result)
    print("=" * 60)
