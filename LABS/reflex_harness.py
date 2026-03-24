import json
from openai import OpenAI
import os

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
# We add a 300s timeout to allow the 3080 Ti time to process large prompts
client = OpenAI(base_url=BASE_URL, api_key="lm-studio", timeout=300.0)
MODEL = "qwen/qwen3.5-35b-a3b"

def get_response(messages, temp=0.3):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temp,
        max_tokens=1000
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

    # STEP 2: THE SELF-REFLECTION (The 'Reflex' Loop)
    print("\n🧐 [Harness] Enforcing Step 2: Critical Self-Reflection...")
    # Notice we change the system prompt to force a 'Critic' mindset
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
    # A tricky RF task that usually needs a second look
    mission = "Write a Python script to calculate the Link Budget for a 5G mmWave link at 28GHz, including rain attenuation."
    
    final_result = run_cognitive_harness(mission)
    
    print("\n🎯 HARNESS OUTPUT (Final Peer-Reviewed Version):")
    print("=" * 60)
    print(final_result)
    print("=" * 60)

"""
Terminology Spotlight:
1. Cognitive Harness: This script. It 'wraps' the AI's thoughts in a structured process.
2. Reflection Loop: The process of an AI reviewing its own output to reduce hallucinations.
3. Zero-Shot vs. Reflected: 
   - Zero-Shot: Asking once (The draft).
   - Reflected: Asking, critiquing, then rewriting (The final version).
"""
