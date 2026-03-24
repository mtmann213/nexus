# Phase 2: The Librarian (RAG)
## Subject: Vector Embeddings and Semantic Retrieval

### 🎯 Learning Objectives
By the end of this phase, the trainee will be able to:
1. **Explain** the concept of a Vector Embedding and how it represents "meaning" mathematically.
2. **Calculate** semantic similarity using Cosine Similarity.
3. **Understand** the difference between keyword search and semantic search.
4. **Implement** a persistent Vector Database (ChromaDB) to store and retrieve technical knowledge.
5. **Analyze** distance scores to determine the reliability of a retrieved "memory."

---

### 📖 Technical Deep Dive

#### 1. Vector Embeddings (The Semantic Spectrum)
In AI, an **Embedding** is a process that turns text into a high-dimensional vector (a list of 768 or 1024 numbers).
* **The Analogy:** In RF, a Fourier Transform (FFT) takes a time-domain signal and represents it in the frequency domain. This allows you to identify a signal by its "spectral signature." An embedding does the same for text—it creates a "semantic signature" where concepts that are related sit in the same part of the mathematical spectrum.
* **Key Insight:** Words like "USRP" and "SDR" may share no letters, but their vectors will be physically close to each other in the 768-dimensional space.

#### 2. Cosine Similarity (Correlation)
To find out how related two pieces of text are, we measure the angle between their vectors.
* **The Analogy:** This is mathematically similar to a **Correlation Coefficient** or a **Matched Filter** in signal processing. We are looking for the "overlap" between two signals to see if one contains the information we need.
* **Results:** In our tests, we saw a **0.68** similarity for RF-related terms and a **0.40** similarity for unrelated terms (Pizza). That "Semantic Gap" is what allows the Librarian to filter out noise.

#### 3. Vector Databases (The Spatial Index)
A normal database (SQL) is like an alphabetical index. A **Vector Database** (like ChromaDB) is like a 3D map of a library.
* **The Strategy:** Instead of looking for a book by its title (exact match), the AI says, "Take me to the region of the map where people talk about GPU-accelerated simulations."
* **Persistence:** By using a `PersistentClient`, we ensure the AI's "long-term memory" survives even if the server is restarted.

---

### 📚 Glossary

| Term | Definition | RF Engineering Analogy |
| :--- | :--- | :--- |
| **Embedding** | A numerical representation of text in high-dimensional space. | An **FFT Signature** of a signal. |
| **Vector** | An array of numbers representing coordinates in semantic space. | An **IQ Sample** or a Coordinate. |
| **Cosine Similarity** | A measure of the angle between two vectors (0 to 1). | **Correlation** or Matched Filter output. |
| **Vector Database** | A specialized database for storing and querying embeddings. | A **Spectrum Map** or Signal Library. |
| **Distance Score** | The mathematical "length" between two vectors (Lower is better). | **Path Loss** or Signal Deviation. |

---

### ❓ Comprehension Questions
1. How does an embedding allow an AI to find a paper about "Antennas" if the user only searched for "Radiating elements"?
2. What is the "Semantic Gap," and why is it important for building a reliable agent?
3. Why can't we just use a standard SQL database for semantic search?
4. If a Distance Score in ChromaDB is 0.95, is that a "strong" match or a "weak" match? Why?
5. How does the "Librarian" (RAG) help solve the problem of a model's limited context window?

---

### 🧪 Lab Reference: `LABS/generate_embeddings.py` & `LABS/store_memories.py`

#### What to expect:
1. **`generate_embeddings.py`**: This script outputs the raw 768-dimensional coordinates for different sentences and calculates the **Cosine Similarity** between them. You will see a high score for related concepts and a low score for unrelated ones.
2. **`store_memories.py`**: This script creates a persistent database folder (`/nexus_db`). It stores documents and then searches them. You should see it successfully find the "Sionna" library when you search for "graphics card radio simulations," proving semantic retrieval works.

#### Generation Prompt (for the student):
> "Create a Python script using the `chromadb` and `openai` libraries. Use a local embedding model to turn three RF sentences into vectors and store them in a persistent collection named 'rf_knowledge'. Then, write a function to query that collection using a conceptual search like 'How do I run simulations on a GPU?' and display the best match and its distance score."

---

### ✅ Success Criteria
* **Proof of Work:** `store_memories.py` successfully retrieves the "Sionna" document when queried with the concept "graphics card," despite the words not matching.
