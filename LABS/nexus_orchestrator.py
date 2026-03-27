from config import client, MODEL_NAME, TIMEOUT
import os
import re

# Project Root STATE file
STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "STATE.md")
AGENTS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "AGENTS.md")

def get_agent_model(tier_name):
    """Parses AGENTS.md to find the exact model assigned to a given Tier."""
    if not os.path.exists(AGENTS_FILE):
        return MODEL_NAME
        
    with open(AGENTS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Split content on the specific Tier header
    tier_block = content.split(f"## [{tier_name}]")
    if len(tier_block) > 1:
        block = tier_block[1].split("## [")[0]  # Get content strictly for this tier
        
        # 1. Search for explicit - **Model:** line first
        model_match = re.search(r"- \*\*Model:\*\* (.+)", block)
        if model_match:
            return model_match.group(1).strip()
            
        # 2. Fallback to parsing the parenthesis in the header line
        title_line = block.split("\n")[0]
        paren_match = re.search(r"\(([^)]+)\)", title_line)
        if paren_match:
            return paren_match.group(1).strip()
            
    return MODEL_NAME # Fallback to config if tier not found

def get_agent_response(role_tier, system_instruction, user_content, max_tokens=4000, temperature=0.3):
    """Sends a properly formatted message list with dynamically parsed model targets."""
    
    target_model = get_agent_model(role_tier)
    print(f"🔌 [Orchestrator] Directing request to server model: {target_model}")
    
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

def run_senior_architect(mission):
    print("🏗️  [Tier 4: Senior Architect (Qwen 35B Sim)] drafting architecture...")
    system_prompt = (
        "You are the Tier 4 Senior Architect. You specialize in strategic long-term planning "
        "and broad system design for RF algorithms. Focus on generating a high-level Python draft "
        "for the requested architecture."
    )
    
    draft = get_agent_response("Tier 4", system_prompt, mission, temperature=0.6)
    
    if not draft:
        print("❌ CRITICAL: Senior Architect failed to respond.")
        return False
        
    # Blackboard Protocol: Overwrite state with new session
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Multi-Agent State Board\n\n## 1. Senior Architect Draft\n{draft}\n\n")
    print(f"✅ Architect draft saved to Blackboard: {STATE_FILE}.")
    return True

def run_auditor():
    print("🧐 [Tier 3: Auditor (Phi-4 Sim)] reading blackboard and reviewing...")
    
    # Blackboard Protocol: Read state
    if not os.path.exists(STATE_FILE):
        print(f"❌ CRITICAL: Blackboard file {STATE_FILE} not found.")
        return False
        
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        current_state = f.read()
        
    system_prompt = (
        "You are the Tier 3 Auditor. Your skill is complex mathematical verification and "
        "logical debugging. Read the current architecture draft and provide a harsh, critical "
        "review of its flaws. Use <thinking> tags to show your logic."
    )
    
    user_prompt = f"Review this draft from the blackboard:\n\n{current_state}"
    critique = get_agent_response("Tier 3", system_prompt, user_prompt, temperature=0.1)
    
    if not critique:
        print("❌ CRITICAL: Auditor failed to respond.")
        return False
        
    # Blackboard Protocol: Append critique
    with open(STATE_FILE, "a", encoding="utf-8") as f:
        f.write(f"## 2. Auditor Critique\n{critique}\n\n")
    print(f"✅ Auditor critique appended to Blackboard: {STATE_FILE}.")
    return True

def run_eval():
    print("🔍 Running Verification Layer (Evals)...")
    if not os.path.exists(STATE_FILE):
        print("❌ EVAL FAILED: Blackboard file missing.")
        return
        
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "## 1. Senior Architect Draft" in content and "## 2. Auditor Critique" in content:
        print("🎯 EVAL PASSED: Multi-Agent Council successfully utilized the Blackboard Protocol.")
    else:
        print("❌ EVAL FAILED: Blackboard state does not reflect expected multi-agent interaction.")

if __name__ == "__main__":
    business_logic_task = (
        "Design the system architecture for an AI-driven RF anomaly detection module. "
        "It needs to continuously monitor incoming IQ streams, detect interference, and log events."
    )
    
    print(f"🌟 Mission: {business_logic_task}\n")
    if run_senior_architect(business_logic_task):
        if run_auditor():
            run_eval()
