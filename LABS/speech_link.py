import pyttsx3
import time
import os

# Phase 8: Local TTS (The "Voice")
# We save to a file to ensure compatibility in headless/WSL environments.

def run_tts_test(text, output_file="output.mp3"):
    print(f"🔊 [TTS] Initializing engine...")
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    print(f"📡 [TTS] Synthesizing: '{text}'")
    start_time = time.time()
    
    # Save to file instead of 'say()'
    if os.path.exists(output_file):
        os.remove(output_file)
        
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    print(f"✅ Speech synthesis complete in {time.time() - start_time:.2f}s")
    if os.path.exists(output_file):
        print(f"💾 File saved to: {os.path.abspath(output_file)}")
    else:
        print("❌ Error: File was not generated.")

if __name__ == "__main__":
    test_phrase = "Project Nexus Voice Link established. All systems nominal."
    run_tts_test(test_phrase)
