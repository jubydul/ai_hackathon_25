from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# Step 4: Define the search function
def search_products(query, k=5):
    # Step 1: Connect to the existing Chroma persistent database
    chroma_client = PersistentClient(path="./chroma_db")  # make sure path matches your persistence

    # Step 2: Load the existing collection
    collection = chroma_client.get_or_create_collection(name="products")

    # Step 3: Load embedding model
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    # 1. Encode the query into vector
    query_embedding = embedder.encode(query)

    # 2. Query from ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],  # must be a list
        n_results=k
    )

    # 3. Prepare results nicely
    hits = []
    for doc, meta, id_ in zip(results['documents'][0], results['metadatas'][0], results['ids'][0]):
        hits.append({
            "id": id_,
            "title": meta.get("title_left", ""),
            "brand": meta.get("brand_left", ""),
            #"description": meta.get("description", ""),
            "category": meta.get("category_left", ""),
            "raw_text": doc
        })
    
    return hits

# Sandisk Extreme microSDHC 64Gb Type 10" 10 acheter et offres sur Scubastore
#print(search_products("best budget samsung phone"))
