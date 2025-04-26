# AI Engineering Hackathon 25

# High Level Architecture Design Flow for Intent-Aware Product Search System


                      +---------------------+
                      |    User Query        |
                      +---------------------+
                               |
                               v
                    +--------------------------+
                    |  Intent Detection (ZSL)   |
                    |  HuggingFace Transformers |
                    +--------------------------+
                               |
               ┌───────────────┴───────────────┐
               |                               |
        Search Product                  Other Intents
               |                               |
               v                               v
+----------------------------------+    +---------------------+
| Semantic Search via Vector DB    |    | (Optional) Routing   |
| SentenceTransformer Embedding    |    | Different Handlers   |
| Vector Database (ChromaDB)       |    +---------------------+
+----------------------------------+
               |
               v
+----------------------------------+
|   Top-k Matched Product Entries  |
|   title, brand, category         |
+----------------------------------+
               |
               v
+----------------------------------+
|        FastAPI REST API          |
|   POST /search                   |
|   Returns JSON: intent + items   |
+----------------------------------+
               |
               v
        +------------------+
        |    Client UI     |
        | (curl, browser,  |
        | Postman, etc.)   |
        +------------------+
