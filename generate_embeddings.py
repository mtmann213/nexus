import numpy as np
from openai import OpenAI

# Configuration (Note: Using your host IP from Phase 1)
BASE_URL = "http://172.18.176.1:1234/v1"
EMBED_MODEL = "text-embedding-nomic-embed-text-v1.5"

client = OpenAI(base_url=BASE_URL, api_key="lm-studio")

def get_embedding(text):
    """Turns text into a high-dimensional vector."""
    response = client.embeddings.create(input=[text], model=EMBED_MODEL)
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    """Calculates the mathematical 'closeness' of two vectors."""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

if __name__ == "__main__":
    # Test Sentences
    s1 = "The USRP is a software-defined radio for RF prototyping."
    s2 = "SDR hardware like Ettus products are used for radio experiments."
    s3 = "I like eating pepperoni pizza on Sundays."

    print(f"📡 Generating embeddings using {EMBED_MODEL}...")
    
    vec1 = get_embedding(s1)
    vec2 = get_embedding(s2)
    vec3 = get_embedding(s3)

    print(f"✅ Vector 1 Length (Dimensions): {len(vec1)}")
    print(f"📊 Similarity (S1 vs S2 - RF to RF): {cosine_similarity(vec1, vec2):.4f}")
    print(f"📊 Similarity (S1 vs S3 - RF to Pizza): {cosine_similarity(vec1, vec3):.4f}")

"""
Why this works:
1. Vectors: Each sentence becomes a list of numbers representing 'features'. 
2. Dot Product: This is the mathematical 'overlap' between two vectors.
3. Cosine Similarity: A score from 0 to 1. 
   - 1.0 = Identical meaning.
   - > 0.8 = Very similar (The 'Librarian' would show you this result).
   - < 0.5 = Unrelated (The 'Librarian' would ignore this).
"""
