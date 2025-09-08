import chromadb
from sentence_transformers import SentenceTransformer

# Initialize Chroma client and collection
client = chromadb.Client()
collection = client.create_collection("pdf_texts")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def add_text_to_index(text: str):
    """
    Splits text into chunks and adds embeddings to Chroma.
    """
    chunks = text.split('\n')
    for i, chunk in enumerate(chunks):
        if chunk.strip():
            embedding = model.encode([chunk]).tolist()
            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"doc_{len(collection.get()['ids']) + i}"]
            )

def search_index(query: str, top_k=3):
    """
    Returns top_k most similar chunks for a query.
    """
    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )
    return results["documents"][0] if results["documents"] else []
