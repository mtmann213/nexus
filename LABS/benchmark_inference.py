import time
from openai import OpenAI

# Configuration
BASE_URL = "http://172.18.176.1:1234/v1"
MODEL_NAME = "qwen/qwen3.5-35b-a3b"  # Change this to test different models

client = OpenAI(base_url=BASE_URL, api_key="lm-studio")

def run_benchmark(prompt):
    print(f"🚀 Benchmarking model: {MODEL_NAME}")
    print(f"📝 Prompt: {prompt}\n")
    
    start_time = time.time()
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            stream=False # Change to True for real-time visualization
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Extract metrics
        content = response.choices[0].message.content
        total_tokens = response.usage.completion_tokens
        
        tokens_per_second = total_tokens / duration
        
        print("-" * 30)
        print(f"✅ Response: {content[:100]}...")
        print("-" * 30)
        print(f"⏱️ Time taken: {duration:.2f} seconds")
        print(f"🔢 Tokens generated: {total_tokens}")
        print(f"⚡ Speed: {tokens_per_second:.2f} tokens/sec")
        print("-" * 30)
        
        return tokens_per_second

    except Exception as e:
        print(f"❌ Error during benchmark: {e}")
        return None

if __name__ == "__main__":
    test_prompt = "Explain how a Phase Locked Loop (PLL) works in the context of RF signal synchronization."
    run_benchmark(test_prompt)

"""
Why this works:
This script uses the OpenAI Python SDK, which is the industry standard for interacting 
with LLM APIs. By pointing the 'base_url' to your local LM Studio instance, we 
treat your 3080 Ti exactly like a cloud-based server. 

Tokens/sec (t/s) is the key metric for 'inference throughput'. 
- < 5 t/s: Feels like a slow typist.
- 10-20 t/s: Natural reading speed.
- > 50 t/s: Near-instantaneous.
"""
