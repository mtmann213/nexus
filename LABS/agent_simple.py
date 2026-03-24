import json
from openai import OpenAI
import os

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
client = OpenAI(base_url=BASE_URL, api_key="lm-studio")
MODEL = "qwen/qwen3.5-35b-a3b"

def create_file(filename, content):
    """The actual 'Hand' that touches the disk."""
    with open(filename, "w") as f:
        f.write(content)
    return f"✅ Successfully created {filename}"

def run_agent(user_prompt):
    print(f"🤖 Agent is thinking about: '{user_prompt}'")
    
    # We provide the AI with a 'System Prompt' that defines its 'Hand'
    # Note: Modern models have 'tool_use' features, but we are building it 
    # manually first so you understand the 'JSON Plumbing'.
    system_instruction = """
    You are a helpful assistant with access to a tool.
    Tool: create_file(filename, content)
    
    If the user asks you to create a file, respond ONLY with a JSON object in this format:
    {"action": "create_file", "filename": "name.py", "content": "file_content_here"}
    """
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0 # We want precise JSON, not creativity
    )
    
    # Parse the AI's "Signal"
    raw_output = response.choices[0].message.content.strip()
    
    # Some models wrap JSON in markdown blocks ```json ... ```
    if "```json" in raw_output:
        raw_output = raw_output.split("```json")[1].split("```")[0].strip()
    elif "```" in raw_output:
        raw_output = raw_output.split("```")[1].strip()

    try:
        signal = json.loads(raw_output)
        if signal["action"] == "create_file":
            # Execute the action!
            result = create_file(signal["filename"], signal["content"])
            print(result)
    except Exception as e:
        print(f"❌ Failed to parse agent signal: {e}")
        print(f"Raw Output: {raw_output}")

if __name__ == "__main__":
    prompt = "Create a python script named 'wavelength.py' that calculates wavelength given frequency."
    run_agent(prompt)
