import time
from config import client, MODEL_NAME

def run_benchmark(prompt):
    print(f"🚀 Benchmarking model: {MODEL_NAME}")
    print(f"📝 Prompt: {prompt}\n")
    
    start_time = time.time()
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            stream=False 
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
