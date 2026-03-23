import chromadb
from openai import OpenAI
import os

# 1. Setup our "Engine" (Inference/Embeddings)
BASE_URL = "http://172.18.176.1:1234/v1"
client = OpenAI(base_url=BASE_URL, api_key="lm-studio")

def get_embedding(text):
    """Generates a 768-dimensional vector for the given text."""
    response = client.embeddings.create(input=[text], model="text-embedding-nomic-embed-text-v1.5")
    return response.data[0].embedding

# 2. Setup our "Library" (Vector DB)
# PersistentClient ensures the data is saved in the 'nexus_db' folder
db_client = chromadb.PersistentClient(path="./nexus_db")
collection = db_client.get_or_create_collection(name="rf_knowledge")

def add_to_library(text, metadata_id):
    """Embeds text and saves it into the vector database."""
    print(f"📥 Adding to Library: {text}")
    vector = get_embedding(text)
    collection.add(
        embeddings=[vector],
        documents=[text],
        ids=[metadata_id]
    )

def query_library(query_text):
    """Searches the database for the semantically closest match."""
    print(f"\n🔍 Searching for: '{query_text}'")
    query_vector = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=1
    )
    return results

if __name__ == "__main__":
    # We check if we've already added the data so we don't duplicate it
    if collection.count() == 0:
        add_to_library("The USRP N210 is a high-performance SDR for signal processing.", "usrp_doc")
        add_to_library("Sionna is a GPU-accelerated library for link-level simulations.", "sionna_doc")
        add_to_library("A Phase Locked Loop (PLL) is used for frequency synthesis.", "pll_doc")
    else:
        print(f"📚 Library already contains {collection.count()} memories.")

    # MISSION: Search for a concept, not a word.
    # We use 'graphics card' (GPU) and 'radio simulations'.
    my_search = "How do I run radio simulations on my graphics card?"
    
    match = query_library(my_search)
    
    print("-" * 30)
    print(f"🤖 Librarian's Best Guess: {match['documents'][0][0]}")
    print(f"📊 Distance Score: {match['distances'][0][0]:.4f}")
    print("-" * 30)
    
    if "Sionna" in match['documents'][0][0]:
        print("🎯 SUCCESS: The Librarian connected 'graphics card' to 'GPU-accelerated'!")
    else:
        print("⚠️ The Librarian missed the connection. We might need a better threshold.")
