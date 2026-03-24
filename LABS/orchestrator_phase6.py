from config import client, MODEL_NAME
import os
import time
from datetime import datetime

BLACKBOARD_PATH = "AGENTS.md"

def read_blackboard():
    """Read current blackboard state."""
    try:
        with open(BLACKBOARD_PATH, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "# Project Agents: Project Nexus Standard\n\n## 📍 System State\n- **Current Phase:** Not Started"

def write_blackboard(content):
    """Update blackboard with new content."""
    with open(BLACKBOARD_PATH, 'w') as f:
        f.write(content)

def append_to_section(section_name, text):
    """Append text to a specific section in the blackboard."""
    current = read_blackboard()
    
    if f"## {section_name}" not in current:
        print(f"⚠️ Section '{section_name}' not found. Creating it.")
        # Append at end before any existing closing markers
        current = current.rstrip() + "\n\n### " + section_name + "\n" + text
    
    else:
        # Find the section and append after its content
        lines = current.split('\n')
        new_lines = []
        in_section = False
        
        for line in lines:
            new_lines.append(line)
            if f"## {section_name}" in line:
                in_section = True
            elif in_section and line.startswith("## "):
                # New section starting - insert before it
                new_lines.insert(-1, text.rstrip())
                in_section = False
        
        current = '\n'.join(new_lines)
    
    with open(BLACKBOARD_PATH, 'w') as f:
        f.write(current)
    
    return read_blackboard()

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
            return None
        return content
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return None

def architect_persona(mission, blackboard_state):
    """Architect reads blackboard and writes design plan."""
    system_prompt = (
        "You are a Strategic Planner specializing in high-level logic, design patterns, and system architecture.\n"
        "\n"
        "TASK: Review the current mission and create an architectural design.\n"
        "\n"
        "INSTRUCTIONS:\n"
        "1. Read the existing blackboard state for context\n"
        "2. Create a clear, actionable design plan\n"
        "3. Write your response to be appended to 'Architect's Section' in AGENTS.md\n"
        "\n"
        "BLACKBOARD CONTEXT:\n" + blackboard_state + "\n"
        "\n"
        "MISSION: " + mission + "\n\n"
        "Provide your architectural design now. Be concise but thorough."
    )
    
    print("\n🏗️  Architect reading blackboard and designing...")
    response = get_agent_response([{"role": "user", "content": system_prompt}], temperature=0.7, max_tokens=2000)
    
    if not response:
        print("⚠️ Architect failed to generate design.")
        return None
    
    # Extract the design (remove markdown code blocks if present)
    design = response.strip()
    if design.startswith("```") and design.endswith("```"):
        lines = design.split('\n')
        design = '\n'.join(lines[1:-1])
    
    print("\n--- ARCHITECT'S DESIGN ---")
    print(design[:600] + ("..." if len(design) > 600 else ""))
    print("--------------------------\n")
    
    return design

def reviewer_persona(mission, blackboard_state):
    """Reviewer reads blackboard and writes critique."""
    system_prompt = (
        "You are a Critical Reviewer specializing in code quality, security, and best practices.\n"
        "\n"
        "TASK: Review the Architect's design and provide constructive feedback.\n"
        "\n"
        "INSTRUCTIONS:\n"
        "1. Read the existing blackboard state including Architect's design\n"
        "2. Identify 3-5 specific improvements or concerns\n"
        "3. Write your response to be appended to 'Reviewer's Section' in AGENTS.md\n"
        "\n"
        "BLACKBOARD CONTEXT:\n" + blackboard_state + "\n"
        "\n"
        "MISSION: " + mission + "\n\n"
        "Provide your critical review now. Be specific and actionable."
    )
    
    print("\n🧐 Reviewer reading blackboard and reviewing...")
    response = get_agent_response([{"role": "user", "content": system_prompt}], temperature=0.3, max_tokens=1500)
    
    if not response:
        print("⚠️ Reviewer failed to generate critique.")
        return None
    
    # Extract the critique (remove markdown code blocks if present)
    critique = response.strip()
    if critique.startswith("```") and critique.endswith("```"):
        lines = critique.split('\n')
        critique = '\n'.join(lines[1:-1])
    
    print("\n--- REVIEWER'S CRITIQUE ---")
    print(critique)
    print("---------------------------\n")
    
    return critique

def run_orchestration(mission):
    """Main orchestration loop with blackboard persistence."""
    run_id = f"REF-{int(time.time())}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 70)
    print(f"🌟 Phase 6 Orchestration: {mission}")
    print(f"   Run ID: {run_id} | Time: {timestamp}")
    print("=" * 70)
    
    # Update System State in blackboard before starting
    initial_blackboard = read_blackboard()
    update_system_state(initial_blackboard, "Phase 6 - Starting Orchestration", run_id, timestamp)
    
    # --- PHASE 1: THE ARCHITECT ---
    print("\n" + "=" * 70)
    print("PHASE 1: ARCHITECT")
    print("=" * 70)
    
    design = architect_persona(mission, initial_blackboard)
    
    if not design:
        print("❌ Architecture phase failed. Aborting.")
        return None
    
    # Write Architect's output to blackboard
    updated_blackboard = append_to_section(
        "Architect's Section",
        f"\n**Run {run_id} ({timestamp})**\n{design}"
    )
    update_system_state(updated_blackboard, "Phase 6 - Architecture Complete", run_id)
    
    # --- PHASE 2: THE REVIEWER ---
    print("\n" + "=" * 70)
    print("PHASE 2: REVIEWER")
    print("=" * 70)
    
    critique = reviewer_persona(mission, updated_blackboard)
    
    if not critique:
        print("❌ Review phase failed. Aborting.")
        return None
    
    # Write Reviewer's output to blackboard
    final_blackboard = append_to_section(
        "Reviewer's Section",
        f"\n**Run {run_id} ({timestamp})**\n{critique}"
    )
    
    # Update System State with completion
    update_system_state(final_blackboard, "Phase 6 - Orchestration Complete", run_id)
    
    print("\n" + "=" * 70)
    print("🎯 FINAL BLACKBOARD STATE:")
    print("=" * 70)
    print(final_blackboard)
    print("=" * 70)
    
    return {
        "run_id": run_id,
        "mission": mission,
        "timestamp": timestamp,
        "design": design,
        "critique": critique,
        "final_blackboard": final_blackboard
    }

def update_system_state(blackboard, status, run_id, timestamp=None):
    """Update the System State section in blackboard."""
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Try to update existing System State or create it
    lines = blackboard.split('\n')
    new_lines = []
    in_system_state = False
    state_updated = False
    
    for line in lines:
        if "## 📍 System State" in line:
            in_system_state = True
            new_lines.append(line)
        elif in_system_state and not state_updated and line.startswith("- **"):
            # Replace or add to system state
            continue  # Skip old entries, we'll add new ones after the section marker
        elif in_system_state and line.strip() == "":
            if not state_updated:
                # Add our updates before blank line
                new_lines.append(f"- **Status:** {status}")
                new_lines.append(f"- **Last Run ID:** {run_id}")
                new_lines.append(f"- **Sync Time:** {timestamp}")
                state_updated = True
            new_lines.append(line)
        else:
            if not in_system_state or (in_system_state and state_updated):
                new_lines.append(line)
    
    # If we never added updates, append after System State section
    if not state_updated:
        for i, line in enumerate(new_lines):
            if "## 📍 System State" in line:
                new_lines.insert(i + 1, f"- **Status:** {status}")
                new_lines.insert(i + 2, f"- **Last Run ID:** {run_id}")
                new_lines.insert(i + 3, f"- **Sync Time:** {timestamp}")
                state_updated = True
                break
    
    if not state_updated:
        # Append at end
        new_lines.extend([
            "",
            "## 📍 System State",
            f"- **Status:** {status}",
            f"- **Last Run ID:** {run_id}",
            f"- **Sync Time:** {timestamp}"
        ])
    
    updated = '\n'.join(new_lines)
    write_blackboard(updated)
    return updated

if __name__ == "__main__":
    mission = "Design a multi-agent system for automated code review and refactoring."
    result = run_orchestration(mission)
    
    if result:
        print("\n✅ Orchestration complete. Check AGENTS.md for full state.")
