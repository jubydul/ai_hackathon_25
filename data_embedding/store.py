
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import pandas as pd

# Initialize Chroma
chroma_client = PersistentClient(path="../chroma_db")

# Create Chroma Collection
collection = chroma_client.get_or_create_collection(name="products")

# Load data
df = pd.read_csv("../dataset_preperation/products_cleaned.csv")
df["combined"] = df["title_left"] + " " + df["description_left"]

# Use SentenceTransformer embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

batch_size = 64
for i in range(0, len(df), batch_size):
    batch = df.iloc[i:i+batch_size]
    texts = batch["combined"].tolist()
    ids = batch["id_left"].astype(str).tolist()
    embeddings = model.encode(texts, show_progress_bar=False).tolist()
    metadata = batch[["title_left", "brand_left", "category_left"]].to_dict(orient="records")

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadata
    )