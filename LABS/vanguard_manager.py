from config import client, TIMEOUT, MODEL_NAME
import os
import re
import time

STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "STATE.md")
AGENTS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "AGENTS.md")

def get_agent_model(tier_name):
    """Dynamically parses the specific model assigned to a Tier from AGENTS.md"""
    if not os.path.exists(AGENTS_FILE):
        return MODEL_NAME
    with open(AGENTS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    tier_block = content.split(f"## [{tier_name}]")
    if len(tier_block) > 1:
        block = tier_block[1].split("## [")[0]
        model_match = re.search(r"- \*\*Model:\*\* (.+)", block)
        if model_match: return model_match.group(1).strip()
        title_line = block.split("\n")[0]
        paren_match = re.search(r"\(([^)]+)\)", title_line)
        if paren_match: return paren_match.group(1).strip()
    return MODEL_NAME

def get_response(target_model, system_instruction, user_content, max_tokens=2000, temperature=0.1):
    print(f"🔌 [Routing] Request directed to local server model: {target_model}")
    try:
        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_content}
        ]
        response = client.chat.completions.create(
            model=target_model, 
            messages=messages, 
            temperature=temperature, 
            max_tokens=max_tokens, 
            timeout=TIMEOUT
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ API Error connecting to {target_model}: {str(e)}")
        return None

def run_dispatcher(prompt):
    model = get_agent_model("Tier 1")
    print(f"\n⚡ [Tier 1: Dispatcher ({model})] Analyzing intent at low latency...")
    start_time = time.time()
    
    sys_prompt = (
        "You are the Tier 1 Dispatcher. Your *only* job is intent classification. "
        "If the user asks to write code, Python functions, or execute shell scripts, reply exactly with: TACTICAL\n"
        "If the user asks about system design, theory, architecture, physics, or complex logic flows, reply exactly with: STRATEGIC\n"
        "Reply with absolutely NOTHING ELSE."
    )
    
    classification = get_response(model, sys_prompt, prompt, max_tokens=10, temperature=0.0)
    latency = time.time() - start_time
    print(f"⏱️ Dispatcher Latency: {latency:.2f}s")
    
    if not classification:
        return "STRATEGIC" # Default to heavy reasoning on fail
        
    if "TACTICAL" in classification.upper():
        return "TACTICAL"
    elif "STRATEGIC" in classification.upper():
        return "STRATEGIC"
    else:
        print(f"⚠️ Dispatcher returned ambiguous classification: '{classification}'. Defaulting to STRATEGIC.")
        return "STRATEGIC"

def execute_task(classification, prompt):
    with open(STATE_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n# New Vanguard Multi-Model Task\n**Intent:** {classification}\n**Task:** {prompt}\n\n")

    if classification == "TACTICAL":
        print("🛠️  Routing to [Tier 2: Developer] for strict coding work to save VRAM...")
        model = get_agent_model("Tier 2")
        result = get_response(model, "You are the Tier 2 Developer. Write perfect code based on the prompt. No fluff.", prompt, temperature=0.2)
        writer = "Tier 2 Developer Output"
        
    else:
        print("🏗️  Routing to [Tier 4: Architect] for heavy mathematical/architectural reasoning...")
        model = get_agent_model("Tier 4")
        result = get_response(model, "You are the Tier 4 Architect. Design the robust architecture and logic flow for the prompt.", prompt, temperature=0.6)
        writer = "Tier 4 Architect Output"

    if result:
        print(f"✅ Execution complete. Syncing {writer} to STATE.md.")
        with open(STATE_FILE, "a", encoding="utf-8") as f:
            f.write(f"## {writer}\n{result}\n")
    return result

if __name__ == "__main__":
    task1 = "Write a fast python script to deploy an NGINX docker container mapping port 80 to 8080."
    task2 = "Design the theoretical signaling protocol architecture for a federated agent swarm connecting via MCP."
    
    print("\n" + "="*50)
    print("--- Testing Task 1 (Coding Task) ---")
    print(f"User: {task1}")
    print("="*50)
    class1 = run_dispatcher(task1)
    execute_task(class1, task1)
    
    print("\n" + "="*50)
    print("--- Testing Task 2 (Theory Task) ---")
    print(f"User: {task2}")
    print("="*50)
    class2 = run_dispatcher(task2)
    execute_task(class2, task2)
