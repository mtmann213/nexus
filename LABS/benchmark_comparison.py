import time
import os
from config import client as local_client, MODEL_NAME as LOCAL_MODEL
from openai import OpenAI

# 2. GROQ CONFIGURATION
GROQ_URL = "https://api.groq.com/openai/v1"
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_KEY = os.environ.get("GROQ_API_KEY", "MISSING")

def run_test(name, client, model, prompt):
    print(f"\n🏎️  Testing {name} ({model})...")
    start_time = time.time()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        duration = time.time() - start_time
        tokens = response.usage.completion_tokens
        tps = tokens / duration
        print(f"✅ Result: {tps:.2f} tokens/sec")
        return tps
    except Exception as e:
        print(f"❌ {name} failed: {str(e)}")
        return 0

if __name__ == "__main__":
    prompt = "Explain the difference between a matched filter and an equalizer in digital signal processing."
    
    # Setup Groq Client
    groq_client = OpenAI(base_url=GROQ_URL, api_key=GROQ_KEY)

    print("🏁 STARTING THE PROJECT NEXUS DRAG RACE 🏁")
    print("-" * 40)

    # Run Local (Using import from config)
    local_speed = run_test("LOCAL Hardware", local_client, LOCAL_MODEL, prompt)

    # Run Groq
    groq_speed = 0
    if GROQ_KEY == "MISSING":
        print("\n☁️  GROQ: Skipped (Set GROQ_API_KEY to run this test)")
    else:
        groq_speed = run_test("CLOUD (Groq LPU)", groq_client, GROQ_MODEL, prompt)

    # Comparison
    if local_speed > 0 and groq_speed > 0:
        print("\n" + "=" * 40)
        print("📊 THE FINAL VERDICT:")
        ratio = groq_speed / local_speed
        print(f"🏎️  Groq is {ratio:.1f}x faster than your Local setup.")
        print("💡 TIP: Use Local for privacy/dev, use Groq for mass-evals!")
        print("=" * 40)
