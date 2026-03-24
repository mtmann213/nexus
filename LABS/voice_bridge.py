import os
import time
from config import client, MODEL_NAME

# Terminology: This is our 'Voice Link Budget'
# We need to measure how long each step takes to ensure RTT < 2.0s.

def capture_audio():
    """Simulates Speech-to-Text (STT)."""
    print("\n🎙️ [Simulated Mic]: 'Check the VRAM status of my 3080 Ti.'")
    return "Check the VRAM status of my 3080 Ti."

def play_voice(text):
    """Simulates Text-to-Speech (TTS)."""
    print(f"\n🔊 [AI Voice Output]:\n{text}")

def run_voice_session():
    print("🏁 STARTING PROJECT NEXUS VOICE BASELINE 🏁")
    print("-" * 40)
    
    # 1. STT Phase (Capture)
    start_stt = time.time()
    user_text = capture_audio()
    stt_latency = time.time() - start_stt
    print(f"⏱️  STT Latency: {stt_latency:.2f}s")

    # 2. REASONING Phase (Inference)
    print("🧠 AI is thinking...")
    start_llm = time.time()
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": user_text}],
            max_tokens=150 # Keep it short for low-latency voice
        )
        ai_text = response.choices[0].message.content
        llm_latency = time.time() - start_llm
        print(f"⏱️  LLM Latency: {llm_latency:.2f}s")
    except Exception as e:
        print(f"❌ LLM Error: {e}")
        return

    # 3. TTS Phase (Synthesis)
    start_tts = time.time()
    play_voice(ai_text)
    tts_latency = time.time() - start_tts
    print(f"⏱️  TTS Latency: {tts_latency:.2f}s")

    # 4. TOTAL LINK BUDGET
    total_rtt = stt_latency + llm_latency + tts_latency
    print("-" * 40)
    print(f"📊 TOTAL ROUND-TRIP LATENCY (RTT): {total_rtt:.2f}s")
    
    if total_rtt < 2.0:
        print("🎯 STATUS: VOICE-READY (Natural conversation possible)")
    elif total_rtt < 5.0:
        print("⚠️  STATUS: SATELLITE-LINK (Delay will be noticeable)")
    else:
        print("❌ STATUS: UNUSABLE (Optimization required)")

if __name__ == "__main__":
    run_voice_session()
