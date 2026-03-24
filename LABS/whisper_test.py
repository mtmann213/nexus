from faster_whisper import WhisperModel
import time
import os

# Phase 8: Local STT (The "Ear")
# We use the 'tiny' model for maximum speed on your 3080 Ti.

def run_whisper_test(audio_path):
    print(f"👂 [Whisper] Initializing local model (tiny)...")
    
    # Run on GPU if possible
    model = WhisperModel("tiny", device="cuda", compute_type="float16")

    print(f"📡 [Whisper] Transcribing file: {audio_path}")
    start_time = time.time()
    
    segments, info = model.transcribe(audio_path, beam_size=5)

    print(f"✅ Transcription complete in {time.time() - start_time:.2f}s")
    print(f"🌍 Detected language: '{info.language}' with probability {info.language_probability:.2f}")

    print("\n--- RESULTS ---")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
    print("----------------")

if __name__ == "__main__":
    # Note: Using a standard SciPy test wave file for the first run
    test_audio = "./venv/lib/python3.12/site-packages/scipy/io/tests/data/test-44100Hz-le-1ch-4bytes.wav"
    
    if os.path.exists(test_audio):
        run_whisper_test(test_audio)
    else:
        print(f"❌ Test audio not found at {test_audio}")
        print("💡 TIP: You can record a message on your phone, save it as 'my_voice.wav' in this folder, and run the script again!")
