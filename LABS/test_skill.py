from config import client, MODEL_NAME, TIMEOUT
import os

SKILL_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "SKILLS", "nexus-hardware.md")

def test_skill_injection():
    print("🧠 Reading Skill Document (Procedural Playbook)...")
    if not os.path.exists(SKILL_FILE):
        print(f"❌ Could not find {SKILL_FILE}")
        return
        
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        skill_context = f.read()
        
    system_prompt = (
        "You are the OpenCode Lead Developer. You have been injected with the following "
        "expert skill documentation. You must adhere strictly to its procedural rules.\n\n"
        f"--- SKILL DOCUMENT START ---\n{skill_context}\n--- SKILL DOCUMENT END ---"
    )
    
    # A terrifying, simulated messy Sionna OOM traceback
    user_prompt = """
CRITICAL FAILURE IN PIPELINE:
Traceback (most recent call last):
  File "simulate_ofdm.py", line 142, in <module>
    y = channel(x) # shape: (1024, 16, 256, 14, 72)
  File "/usr/local/lib/python3.10/dist-packages/sionna/channel/rayleigh.py", line 224, in call
    h = tf.complex(tf.random.normal(shape, dtype=tf.float64), tf.random.normal(shape, dtype=tf.float64))
tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[1024,16,256,14,72] and type double on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
    """

    print("🚀 Firing simulated OOM Error at the Agent...")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME, # Uses local standard to ensure baseline adherence testing
            messages=messages,
            temperature=0.1, # Low temp for strict adherence
            max_tokens=1000,
            timeout=TIMEOUT
        )
        output = response.choices[0].message.content
        print("\n" + "="*60)
        print("🤖 AGENT RESPONSE (Did it use the Skill?)")
        print("="*60)
        print(output)
        print("="*60 + "\n")
        
        # Eval Step
        if "complex64" in output and "512" in output and "AUTOTUNE" in output:
            print("🎯 EVAL PASSED: Agent successfully adhered to the 3-step Sionna VRAM Skill Playbook!")
        else:
            print("❌ EVAL FAILED: Agent hallucinated generic advice or ignored the procedural playbook.")
            
    except Exception as e:
        print(f"❌ API Error: {str(e)}")

if __name__ == "__main__":
    test_skill_injection()
