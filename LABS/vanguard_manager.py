import os
import time
from config import client, MODEL_NAME

# Tri-Tier Role Mapping (Simulated if models are not loaded)
# TACTICAL: Lead Developer (VRAM / qwen-14b)
# STRATEGIC: Senior Architect (RAM / llama-70b)
# DISPATCHER: 1B Router (VRAM / gemma-1b)

def get_routing_decision(prompt):
    """The Dispatcher (Tier 1) decides the 'Link Budget' for this thought."""
    dispatch_prompt = (
        "Classify the following user prompt as either 'TACTICAL' (coding, shell, bugs) "
        "or 'STRATEGIC' (architecture, math, design, theory). "
        "Respond with ONLY the word TACTICAL or STRATEGIC.\n\n"
        f"Prompt: {prompt}"
    )
    
    print("📡 [Tier 1] Dispatcher is analyzing intent...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME, # In a real tri-tier, this would be a 1B model
            messages=[{"role": "user", "content": dispatch_prompt}],
            max_tokens=5,
            temperature=0.0
        )
        decision = response.choices[0].message.content.strip().upper()
        return "STRATEGIC" if "STRATEGIC" in decision else "TACTICAL"
    except Exception as e:
        print(f"⚠️ Dispatcher failed: {e}. Defaulting to TACTICAL.")
        return "TACTICAL"

def talk_to_team(user_prompt):
    decision = get_routing_decision(user_prompt)
    print(f"⚡ [Tier 2/3] Routing to: {decision} Agent...")
    
    # Read the Blackboard (AGENTS.md)
    context = ""
    if os.path.exists("../AGENTS.md"):
        with open("../AGENTS.md", "r") as f:
            context = f.read()

    system_msg = f"You are part of Project Nexus. Intent: {decision}. Current State:\n{context}"
    
    try:
        start_time = time.time()
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        duration = time.time() - start_time
        print(f"✅ Response received in {duration:.2f}s")
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error communicating with team: {e}"

if __name__ == "__main__":
    print("🚀 Vanguard Multi-Agent Manager Online.")
    print("This script simulates the VRAM/RAM tiering using your current configuration.")
    while True:
        prompt = input("\n[User] ❯ ")
        if prompt.lower() in ['exit', 'quit']: break
        print("-" * 30)
        print(talk_to_team(prompt))
        print("-" * 30)
