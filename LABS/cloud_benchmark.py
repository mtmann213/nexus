import os
import time
import requests
from openai import OpenAI

try:
    from config import TIMEOUT
except ImportError:
    TIMEOUT = 300

test_prompt = "Write a comprehensive mathematical essay explaining exactly why running highly-quantized dense parameter models locally bypasses standard cloud transmission latency chokepoints."

def get_openrouter_free_models():
    """Dynamically fetches exactly which models OpenRouter is offering for free today."""
    print("📡 Querying OpenRouter API for today's active free-tier models...")
    try:
        response = requests.get("https://openrouter.ai/api/v1/models", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        free_models = []
        for model in data.get("data", []):
            model_id = model.get("id", "")
            # Look for models explicitly tagged as free by OpenRouter currently
            if ":free" in model_id:
                free_models.append(model_id)
                if len(free_models) >= 4:  # Just grab the top 4 active algorithms to save time
                    break
        return free_models
    except Exception as e:
        print(f"❌ Failed to dynamically fetch OpenRouter models: {e}")
        return []

def run_inference(model_id, prompt, api_key, base_url, location="CLOUD API"):
    print(f"\n🚀 Booting [{model_id}] on {location}...")
    start_time = time.time()
    
    try:
        api_client = OpenAI(base_url=base_url, api_key=api_key)
        
        response = api_client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=200,
            timeout=TIMEOUT,
            extra_headers={
                "HTTP-Referer": "https://github.com/project-nexus",
                "X-Title": "Project Nexus Cloud Benchmarker"
            }
        )
        
        content = response.choices[0].message.content.strip()
        
        if response.usage and response.usage.completion_tokens:
            out_tokens = response.usage.completion_tokens
        else:
            out_tokens = len(content.split()) * 1.3
            
        latency = time.time() - start_time
        tps = out_tokens / latency

        print(f"✅ Pass | Latency: {latency:.2f}s | Speed: {tps:.2f} T/s | Tokens: {out_tokens}")
        print(f"   Sample: '{content[:65].replace(chr(10), ' ')}...'")
        return {"model": model_id, "latency": latency, "tps": tps}

    except Exception as e:
        print(f"❌ Failed: {str(e)}")
        return None

if __name__ == "__main__":
    print("="*75)
    print("☁️ PROJECT NEXUS: DEDICATED CLOUD BENCHMARKER")
    print("="*75)
    
    try:
        from tokenizers import Tokenizer
        print("🧮 Initializing HuggingFace `tokenizers` core...")
        tk = Tokenizer.from_pretrained("gpt2") 
        in_tokens = len(tk.encode(test_prompt).ids)
        print(f"📏 Calculated Outbound Payload: {in_tokens} physical tokens.")
    except Exception:
        print("⚠️ Core HF `tokenizers` not installed.")

    results = []
    
    print("\n" + "#"*70)
    print("1️⃣ INITIATING OPENROUTER FREE-TIER CLOUD BENCHMARK")
    print("#"*70)
    
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "INSERT_OPENROUTER_KEY_HERE")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    
    or_models = [
        "nvidia/nemotron-3-super:free",
        "minimax/minimax-m2.5:free",
        "qwen/qwen3-next-80b-a3b-instruct:free",
        "openai/gpt-oss-120b:free",
        "z-ai/glm-4.5-air:free",
        "mistralai/mistral-small-3.1-24b:free",
        "google/gemma-3-27b:free",
        "meta-llama/llama-3.2-3b-instruct:free",
        "nousresearch/hermes-3-405b-instruct:free"
    ]
    
    if or_models:
        print(f"✅ Testing user's explicit free endpoints: {len(or_models)} models")
        for or_model in or_models:
            print("⏳ Coasting for 2 seconds to respect free-tier rate limits...")
            time.sleep(2)
            res = run_inference(or_model, prompt=test_prompt, api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL, location="OPENROUTER")
            if res: results.append(res)
    
    print("\n" + "#"*70)
    print("2️⃣ INITIATING GROQ LPU CLOUD BENCHMARK")
    print("#"*70)
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "INSERT_GROQ_KEY_HERE")
    GROQ_MODEL = "llama-3.3-70b-versatile" 
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    
    res = run_inference(GROQ_MODEL, prompt=test_prompt, api_key=GROQ_API_KEY, base_url=GROQ_BASE_URL, location="GROQ LPU")
    if res: results.append(res)

    print("\n" + "="*60)
    print("🏆 FINAL CLOUD SCOREBOARD (Tokens/Second)")
    print("="*60)
    results.sort(key=lambda x: x["tps"], reverse=True)
    for i, r in enumerate(results):
        print(f"Score {i+1}. [{r['model'][:35]:<35}] -> {r['tps']:>6.2f} T/s ({r['latency']:>5.2f} sec completion)")
