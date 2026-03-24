import json
from config import client, MODEL_NAME
import os

def create_file(filename, content):
    """The actual 'Hand' that touches the disk."""
    with open(filename, "w") as f:
        f.write(content)
    return f"✅ Successfully created {filename}"

def run_agent(user_prompt):
    print(f"🤖 Agent is thinking about: '{user_prompt}'")
    
    system_instruction = """
    You are a helpful assistant with access to a tool.
    Tool: create_file(filename, content)
    
    If the user asks you to create a file, respond ONLY with a JSON object in this format:
    {"action": "create_file", "filename": "name.py", "content": "file_content_here"}
    """
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0 
    )
    
    # Parse the AI's "Signal"
    raw_output = response.choices[0].message.content.strip()
    
    # Defensive JSON Parsing
    try:
        start_idx = raw_output.find("{")
        end_idx = raw_output.rfind("}")
        if start_idx != -1 and end_idx != -1:
            clean_json = raw_output[start_idx:end_idx + 1]
            signal = json.loads(clean_json)
            if signal["action"] == "create_file":
                result = create_file(signal["filename"], signal["content"])
                print(result)
    except Exception as e:
        print(f"❌ Failed to parse agent signal: {e}")
        print(f"Raw Output: {raw_output}")

if __name__ == "__main__":
    prompt = "Create a python script named 'wavelength.py' that calculates wavelength given frequency."
    run_agent(prompt)
