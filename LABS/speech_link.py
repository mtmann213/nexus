import subprocess
import time
import os

# Phase 8: Local Neural TTS (The "Voice")
# Uses Piper (local neural model) for 100% offline synthesis.

def run_tts_test(text, output_file="output.wav"):
    print(f"🔊 [Neural TTS] Initializing Piper engine...")
    
    # Paths to our local assets
    piper_path = "/home/dev/nexus/piper_bin/piper"
    model_path = "/home/dev/nexus/en_US-lessac-medium.onnx"
    
    if not os.path.exists(piper_path) or not os.path.exists(model_path):
        print("❌ Error: Piper binary or model not found.")
        return

    print(f"📡 [Neural TTS] Synthesizing: '{text}'")
    start_time = time.time()
    
    try:
        # We use a shell pipe to send text to the neural engine
        # Command: echo "text" | ./piper --model voice.onnx --output_file out.wav
        cmd = f'echo "{text}" | {piper_path} --model {model_path} --output_file {output_file}'
        
        if os.path.exists(output_file):
            os.remove(output_file)
            
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
        
        print(f"✅ Neural Speech synthesis complete in {time.time() - start_time:.2f}s")
        print(f"💾 High-Fidelity file saved to: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"❌ Error during neural synthesis: {e}")

if __name__ == "__main__":
    test_phrase = "Project Nexus Neural Voice Link established. All systems nominal."
    run_tts_test(test_phrase)
