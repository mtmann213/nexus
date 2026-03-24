import time
import os
from openai import OpenAI

# 1. LOCAL CONFIGURATION
LOCAL_URL = "http://172.18.176.1:1234/v1"
LOCAL_MODEL = "qwen/qwen3.5-35b-a3b"

# 2. GROQ CONFIGURATION
# To run the cloud test, set your GROQ_API_KEY environment variable
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
    
    # Setup Clients
    local_client = OpenAI(base_url=LOCAL_URL, api_key="lm-studio")
    groq_client = OpenAI(base_url=GROQ_URL, api_key=GROQ_KEY)

    print("🏁 STARTING THE PROJECT NEXUS DRAG RACE 🏁")
    print("-" * 40)

    # Run Local
    local_speed = run_test("LOCAL (3080 Ti)", local_client, LOCAL_MODEL, prompt)

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
        print(f"🏎️  Groq is {ratio:.1f}x faster than your 3080 Ti.")
        print("💡 TIP: Use Local for privacy/dev, use Groq for mass-evals!")
        print("=" * 40)
