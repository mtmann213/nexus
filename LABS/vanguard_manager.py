import time
import json
from config import client

# Phase 9: Vanguard Dispatcher
# This script implements 'Silicon Economics' by routing tasks to the correct model tier.

TIER_1_DISPATCHER = "qwen3.5-0.8b"      # Fast routing (VRAM)
TIER_2_DEVELOPER  = "qwen/qwen3.5-35b-a3b" # Implementation (VRAM)
TIER_3_ARCHITECT  = "llama-3.3-70b"     # Strategic Design (RAM)

def classify_intent(user_prompt):
    """Uses the 0.8B model to decide if a task is TACTICAL or STRATEGIC."""
    print(f"🚦 Dispatcher ({TIER_1_DISPATCHER}) is classifying intent...")
    
    system_prompt = (
        "You are an AI Router. Classify the user prompt into ONE category: 'TACTICAL' or 'STRATEGIC'.\n"
        "- TACTICAL: Coding, debugging, shell commands, syntax fixes.\n"
        "- STRATEGIC: System design, math proofs, architectural planning.\n"
        "Output ONLY the word 'TACTICAL' or 'STRATEGIC'."
    )
    
    try:
        response = client.chat.completions.create(
            model=TIER_1_DISPATCHER,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.0,
            max_tokens=10
        )
        intent = response.choices[0].message.content.strip().upper()
        # Handle cases where model adds extra text
        if "STRATEGIC" in intent: return "STRATEGIC"
        return "TACTICAL"
    except Exception as e:
        print(f"❌ Dispatcher failed: {e}")
        return "TACTICAL" # Default to Developer tier

def execute_task(intent, user_prompt):
    """Routes the prompt to the appropriate model based on intent."""
    if intent == "STRATEGIC":
        target_model = TIER_3_ARCHITECT
        tier_name = "Senior Architect (Tier 3)"
    else:
        target_model = TIER_2_DEVELOPER
        tier_name = "Lead Developer (Tier 2)"
        
    print(f"📡 Routing to {tier_name}...")
    
    start_time = time.time()
    try:
        response = client.chat.completions.create(
            model=target_model,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        content = response.choices[0].message.content
        latency = time.time() - start_time
        return content, latency
    except Exception as e:
        return f"❌ Routing Error: {e}", 0

def run_vanguard_session():
    print("🏁 Project Nexus: Vanguard Management System 🏁")
    print("-" * 50)
    
    # Test Prompts
    prompts = [
        "Fix the syntax error in my Python list comprehension.",
        "Design a high-level plan for a multi-tenant MCP server architecture."
    ]
    
    for p in prompts:
        print(f"\n👤 User: {p}")
        intent = classify_intent(p)
        print(f"🎯 Intent: {intent}")
        
        result, latency = execute_task(intent, p)
        
        print(f"\n🤖 Response (latency: {latency:.2f}s):")
        print(f"{result[:200]}...")
        print("-" * 50)

if __name__ == "__main__":
    run_vanguard_session()
