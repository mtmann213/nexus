import os
import re
import time
import requests
from openai import OpenAI

try:
    from config import client as local_client, TIMEOUT
except ImportError:
    TIMEOUT = 300
    local_client = OpenAI(base_url="http://host.docker.internal:1234/v1", api_key="lm-studio")

AGENTS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "AGENTS.md")

def extract_all_local_models():
    """Extracts all models sequentially from the AGENTS.md tiers."""
    models = []
    if not os.path.exists(AGENTS_FILE): return models
    
    with open(AGENTS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    for i in range(1, 5):
        tier_block = content.split(f"## [Tier {i}]")
        if len(tier_block) > 1:
            block = tier_block[1].split("## [")[0]
            model_match = re.search(r"- \*\*Model:\*\* (.+)", block)
            if model_match: 
                models.append(model_match.group(1).strip())
                continue
            title_line = block.split("\n")[0]
            paren_matches = re.findall(r"\(([^)]+)\)", title_line)
            if paren_matches: 
                models.append(paren_matches[-1].strip())
    return models

def run_inference(model_id, is_local, prompt, api_key=None, base_url=None, location="LM STUDIO"):
    print(f"\n🚀 Booting [{model_id}] on {location}...")
    start_time = time.time()
    
    try:
        api_client = local_client if is_local else OpenAI(base_url=base_url, api_key=api_key or "ollama")
        
        response = api_client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=200,
            timeout=TIMEOUT,
            extra_headers={
                "HTTP-Referer": "https://github.com/project-nexus",
                "X-Title": "Project Nexus Hybrid Benchmarker"
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
    local_models = extract_all_local_models()
    print("="*70)
    print(f"🔍 Discovered {len(local_models)} active models targeted precisely from AGENTS.md!")
    print("="*70)
    
    test_prompt = "Write a comprehensive mathematical essay explaining exactly why running highly-quantized dense parameter models locally bypasses standard cloud transmission latency chokepoints."
    
    try:
        from tokenizers import Tokenizer
        print("🧮 Pulling generic HuggingFace `tokenizers` architecture...")
        tk = Tokenizer.from_pretrained("gpt2") 
        in_tokens = len(tk.encode(test_prompt).ids)
        print(f"📏 Calculated Outbound Payload: {in_tokens} physical tokens.")
    except Exception:
        print("⚠️ Core HF `tokenizers` API blocked or disabled.")
        in_tokens = len(test_prompt.split()) * 1.3
        print(f"📏 Estimated Outbound Payload: ~{int(in_tokens)} generic tokens.")

    print("\n" + "#"*70)
    print("1️⃣ INITIATING SEQUENTIAL LM STUDIO BENCHMARK")
    print("#"*70)
    
    results = []
    
    try:
        local_url = str(local_client.base_url).rstrip('/')
    except Exception:
        local_url = "http://host.docker.internal:1234/v1"
        
    for lm in local_models:
        res = run_inference(lm, is_local=True, prompt=test_prompt, base_url=local_url, location="LM STUDIO")
        if res: results.append(res)
        print("⏳ Letting VRAM context flush...")
        time.sleep(2) 
        
    print("\n" + "#"*70)
    print("2️⃣ INITIATING CLOUD API BENCHMARK (GROQ LPU)")
    print("#"*70)
    
    # Configuration for Groq Cloud benchmarking
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "INSERT_GROQ_KEY_HERE")
    GROQ_MODEL = "llama-3.3-70b-versatile" 
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    
    res = run_inference(GROQ_MODEL, is_local=False, prompt=test_prompt, api_key=GROQ_API_KEY, base_url=GROQ_BASE_URL, location="GROQ CLOUD")
    if res: results.append(res)

    print("\n" + "="*50)
    print("🏆 FINAL BENCHMARK SCOREBOARD (Tokens/Second)")
    print("="*50)
    results.sort(key=lambda x: x["tps"], reverse=True)
    for i, r in enumerate(results):
        print(f"Score {i+1}. [{r['model'][:30]:<30}] -> {r['tps']:>6.2f} T/s ({r['latency']:>5.2f} sec completion)")
