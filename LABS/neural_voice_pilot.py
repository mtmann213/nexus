import subprocess
import time
import os
from config import client

# Phase 8: The Neural Voice Pilot
# Integration of 0.8B LLM (Thinking) + Piper (Speaking)

VOICE_MODEL = "qwen3.5-0.8b"
PIPER_PATH = "/home/dev/nexus/piper_bin/piper"
VOICE_MODEL_PATH = "/home/dev/nexus/en_US-lessac-medium.onnx"

def get_ai_response(prompt):
    print(f"🧠 AI ({VOICE_MODEL}) is thinking...")
    try:
        response = client.chat.completions.create(
            model=VOICE_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to 0.8B model: {e}"

def speak_response(text, output_file="pilot_voice.wav"):
    print(f"🔊 [Piper] Synthesizing neural voice...")
    try:
        # Clean previous file
        if os.path.exists(output_file):
            os.remove(output_file)
            
        # Pipe the AI text into the Piper neural engine
        cmd = f'echo "{text}" | {PIPER_PATH} --model {VOICE_MODEL_PATH} --output_file {output_file}'
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
        print(f"✅ Voice generated: {output_file}")
    except Exception as e:
        print(f"❌ Synthesis error: {e}")

def run_pilot_turn(user_input):
    print(f"🏁 Starting Neural Pilot Turn...")
    print(f"👤 User: {user_input}")
    
    # 1. THINK
    ai_text = get_ai_response(user_input)
    print(f"🤖 AI: {ai_text}")
    
    # 2. SPEAK
    start_time = time.time()
    speak_response(ai_text)
    
    print(f"⏱️  Total Synthesis Latency: {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    # Test with a hardware-aware prompt
    user_query = "Hello Pilot. What is our current VRAM safety limit for the 3080 Ti?"
    run_pilot_turn(user_query)
