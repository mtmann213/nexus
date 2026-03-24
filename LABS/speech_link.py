from gtts import gTTS
import time
import os

# Phase 8: Local TTS (The "Voice")
# Uses gTTS for 100% reliability in WSL/Headless environments.

def run_tts_test(text, output_file="output.mp3"):
    print(f"🔊 [TTS] Initializing gTTS engine...")
    
    print(f"📡 [TTS] Synthesizing: '{text}'")
    start_time = time.time()
    
    try:
        # Create synthesis object
        tts = gTTS(text=text, lang='en')
        
        # Save to file
        if os.path.exists(output_file):
            os.remove(output_file)
            
        tts.save(output_file)
        
        print(f"✅ Speech synthesis complete in {time.time() - start_time:.2f}s")
        print(f"💾 File saved to: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"❌ Error during synthesis: {e}")

if __name__ == "__main__":
    test_phrase = "Project Nexus Voice Link established. All systems nominal."
    run_tts_test(test_phrase)
