from config import client, MODEL_NAME
import os
import re
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

def get_research():
    """
    Parse AGENTS.md to extract system state and validate files.
    Returns structured context summary with validation warnings.
    """
    agents_md = "/home/dev/nexus/AGENTS.md"
    research_context = {
        "status": None,
        "last_run_id": None,
        "sync_time": None,
        "architect_design": None,
        "developer_files": [],
        "validation_warnings": []
    }

    if not os.path.exists(agents_md):
        research_context["validation_warnings"].append(f"AGENTS.md not found at {agents_md}")
        return research_context

    try:
        with open(agents_md, 'r') as f:
            content = f.read()

        # Extract System State using broader regex patterns
        status_match = re.search(r"- Status: (.+)", content)
        if status_match:
            research_context["status"] = status_match.group(1).strip()

        last_run_match = re.search(r"- Last Run ID: (\S+)", content)
        if last_run_match:
            research_context["last_run_id"] = last_run_match.group(1).strip()

        sync_time_match = re.search(r"- Sync Time: (.+)", content)
        if sync_time_match:
            research_context["sync_time"] = sync_time_match.group(1).strip()

        # Extract Architect's Design Context
        design_match = re.search(r"- Design: (.+)", content)
        if design_match:
            research_context["architect_design"] = design_match.group(1).strip()

        # Extract Files Created list
        files_match = re.search(r"- Files Created: (.+)", content)
        if files_match:
                raw_files = files_match.group(1).strip()
                # Parse comma-separated filenames, handling "etc." suffix
                file_list = [f.strip().rstrip('.') for f in raw_files.split(',') if f.strip()]
                research_context["developer_files"] = file_list

                # Validate each file exists on filesystem
                labs_dir = "/home/dev/nexus/LABS"
                for filename in file_list:
                    filepath = os.path.join(labs_dir, filename)
                    if not os.path.exists(filepath):
                        research_context["validation_warnings"].append(
                            f"⚠️ File missing: {filename} (expected at {filepath})"
                        )

    except Exception as e:
        research_context["validation_warnings"].append(f"❌ Error parsing AGENTS.md: {str(e)}")

    return research_context

def update_agents_md(run_id, sync_time):
    """Update the System State section in AGENTS.md with new run ID and sync time."""
    agents_md = "/home/dev/nexus/AGENTS.md"
    if not os.path.exists(agents_md):
        print(f"⚠️ Cannot update: {agents_md} does not exist")
        return False

    try:
        with open(agents_md, 'r') as f:
            content = f.read()

        # Update Last Run ID
        content = re.sub(
            r"(- \*\*Last Run ID\*\*: )(\S+)",
            rf"\1{run_id}",
            content
        )

        # Update Sync Time
        content = re.sub(
            r"(- \*\*Sync Time\*\*: .+)",
            f"- **Sync Time**: {sync_time}",
            content,
            count=1
        )

        with open(agents_md, 'w') as f:
            f.write(content)

        return True

    except Exception as e:
        print(f"❌ Error updating AGENTS.md: {str(e)}")
        return False

def run_orchestration(mission):
    run_id = f"REF-{int(time.time())}"
    print(f"🌟 Mission: {mission} (Run ID: {run_id})")

    # --- RESEARCHER PHASE: Parse system state and validate context ---
    research_output = get_research()
    
    if not research_output["validation_warnings"]:
        print("\n✅ Researcher: System state validated successfully.")
        print(f"   Status: {research_output['status']}")
        print(f"   Last Run ID: {research_output['last_run_id']}")
        print(f"   Architect Design Context: {research_output['architect_design'] or 'None'}")
    else:
        print("\n⚠️ Researcher: Validation warnings detected:")
        for warning in research_output["validation_warnings"]:
            print(f"   {warning}")

    # --- PHASE 1: THE ARCHITECT ---
    # Merge System and User into a single message for maximum local reliability
    architect_instruction = (
        "SYSTEM: You are a Senior RF Engineer. Provide a concise Python/Numpy implementation.\n"
        f"CONTEXT: Previous system state - Status: {research_output.get('status', 'Unknown')}, "
        f"Last Design Context: {research_output.get('architect_design', 'None')}\n"
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
