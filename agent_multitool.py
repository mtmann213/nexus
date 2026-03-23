import json
import subprocess
from openai import OpenAI
import os

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
client = OpenAI(base_url=BASE_URL, api_key="lm-studio")
MODEL = "qwen/qwen3.5-35b-a3b"

def create_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return f"✅ File {filename} created."

def run_terminal_command(command):
    print(f"🖥️ Executing: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return f"Output: {result.stdout}\nError: {result.stderr}"
    except Exception as e:
        return f"❌ Execution failed: {str(e)}"

def run_agent_loop(user_prompt):
    print(f"🤖 Starting Multi-Tool Agent...")
    
    # The 'Conversation' history is key to Multi-Step tasks
    messages = [
        {"role": "system", "content": """
        You are an autonomous agent with two tools:
        1. create_file(filename, content)
        2. run_terminal_command(command)
        
        To use a tool, output a JSON object:
        {"action": "create_file", "filename": "test.py", "content": "print(1)"}
        OR
        {"action": "run_terminal_command", "command": "python3 test.py"}
        
        Only perform one action at a time. After each action, I will give you the result. 
        When the task is complete, respond with: 'FINISH: [summary]'
        """},
        {"role": "user", "content": user_prompt}
    ]

    for i in range(5): # Limit to 5 turns to prevent infinite loops
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )
        
        raw_output = response.choices[0].message.content.strip()
        print(f"\n🧠 AI Thought: {raw_output}")

        if "FINISH" in raw_output:
            print(f"\n🎯 MISSION COMPLETE: {raw_output}")
            break

        # Robust JSON Extraction: Find the first '{' and last '}'
        try:
            start_idx = raw_output.find("{")
            end_idx = raw_output.rfind("}")
            
            if start_idx == -1 or end_idx == -1:
                raise ValueError("No JSON object found in output.")
            
            clean_json = raw_output[start_idx:end_idx + 1]
            signal = json.loads(clean_json)
            
            # Execute logic
            tool_result = ""
            if signal["action"] == "create_file":
                tool_result = create_file(signal["filename"], signal["content"])
            elif signal["action"] == "run_terminal_command":
                tool_result = run_terminal_command(signal["command"])
            
            print(f"🔧 Tool Result: {tool_result}")
            
            # Feed the result BACK into the conversation
            messages.append({"role": "assistant", "content": clean_json})
            messages.append({"role": "user", "content": f"Tool Result: {tool_result}"})

        except Exception as e:
            print(f"❌ Error parsing JSON: {e}")
            print(f"Full Raw Output for Debugging:\n{raw_output}")
            break

if __name__ == "__main__":
    prompt = "Create a script 'test_calc.py' that calculates 2+2, then run it and tell me the result."
    run_agent_loop(prompt)
