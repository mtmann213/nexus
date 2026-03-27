import os
import time
import subprocess
try:
    from faster_whisper import WhisperModel
except ImportError:
    print("❌ faster-whisper not installed. Please run: pip install faster-whisper")
    exit(1)

AUDIO_FILE = "nexus_voice_buffer.wav"

def record_audio(duration=5, filename=AUDIO_FILE):
    print(f"🎙️  Listening to internal Pulse loopback for {duration} seconds... Speak now!")
    
    # Using ffmpeg to record from the pulse audio source inside WSL
    cmd = [
        "ffmpeg",
        "-y",               # Overwrite existing file unconditionally
        "-f", "pulse",      # Force PulseAudio format
        "-i", "default",    # Use default input device
        "-t", str(duration),# Specify exact recording duration
        filename
    ]
    
    try:
        # Mute ffmpeg's massive stdout blocks to keep the terminal clean
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("✅ Recording complete.")
        return True
    except subprocess.CalledProcessError:
        print("❌ ffpmeg failed to record from PulseAudio. Ensure PulseAudio is bridged between your Windows Host and WSL.")
        return False
    except FileNotFoundError:
        print("❌ ffmpeg not found in your system path. Please install via: sudo apt install ffmpeg")
        return False

def transcribe_audio(filename=AUDIO_FILE):
    print("🧠 Loading Whisper 'tiny' model strictly on CPU to protect VRAM...")
    
    # Force the transcription engine onto the CPU using fast int8 quantization
    # This ensures your 3080 Ti doesn't crash if the main LLM is sitting active in VRAM!
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    
    print("⏩ Transcribing...")
    start_time = time.time()
    
    # Process the audio file
    segments, info = model.transcribe(filename, beam_size=5)
    
    # generator to string
    text = "".join([segment.text for segment in segments])
    
    end_time = time.time()
    latency = end_time - start_time
    
    print("\n" + "="*60)
    print(f"🗣️  VOICE PROMPT DETECTED (Latency: {latency:.2f}s)")
    print("="*60)
    print(text.strip())
    print("="*60 + "\n")
    print("💡 TIP: Copy this text directly into your OpenCode or Gemini terminal!")

if __name__ == "__main__":
    if record_audio():
        transcribe_audio()
        
    # Scrub the buffer block
    if os.path.exists(AUDIO_FILE):
        os.remove(AUDIO_FILE)
