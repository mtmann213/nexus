import pyttsx3
import time

# Phase 8: Local TTS (The "Voice")
# Uses espeak-ng backend on Linux.

def run_tts_test(text):
    print(f"🔊 [TTS] Initializing engine...")
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    print(f"📡 [TTS] Speaking: '{text}'")
    start_time = time.time()
    
    engine.say(text)
    engine.runAndWait()

    print(f"✅ Speech complete in {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    test_phrase = "Project Nexus Voice Link established. All systems nominal."
    run_tts_test(test_phrase)
