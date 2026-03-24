import subprocess
import time
import os
from faster_whisper import WhisperModel

# Phase 8: High-Speed Voice-to-Text Command
# Goal: Capture your mic and transcribe it in < 1s for instant communication.

def capture_mic(duration=5, output_file="mic_capture.wav"):
    """Uses ffmpeg to pull audio from the WSL pulse source."""
    print(f"🎙️  LISTENING ({duration}s)... Speak now.")
    try:
        # We pull from the default PulseAudio source (which bridges to Windows Mic)
        cmd = [
            "ffmpeg", "-y", "-f", "pulse", "-i", "default",
            "-t", str(duration), "-ac", "1", "-ar", "16000", output_file
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"❌ Mic capture failed: {e}")
        return False

def transcribe_clip(file_path):
    """Transcribes the captured clip using local Whisper."""
    print("👂 Transcribing...")
    start_time = time.time()
    
    # We use CPU mode for 100% stability in WSL
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    
    segments, info = model.transcribe(file_path, beam_size=5)
    
    text = ""
    for segment in segments:
        text += segment.text + " "
    
    print(f"✅ Transcription complete in {time.time() - start_time:.2f}s")
    return text.strip()

def run_voice_command():
    print("🏁 Project Nexus Voice Interface")
    print("-" * 30)
    
    if capture_mic():
        text = transcribe_clip("mic_capture.wav")
        print("\n📝 YOUR PROMPT:")
        print("=" * 30)
        print(text)
        print("=" * 30)
        print("\n💡 TIP: Copy this text into your OpenCode or Gemini prompt!")
    
    # Clean up
    if os.path.exists("mic_capture.wav"):
        os.remove("mic_capture.wav")

if __name__ == "__main__":
    run_voice_command()
