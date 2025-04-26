# AI Engineering Hackathon 25

# High Level Architecture Design Flow


                      +---------------------+
                      |    User Query       |
                      +---------------------+
                               |
                               v
                    +--------------------------+
                    |  Intent Detection (ZSL)  |
                    |  HuggingFace Transformers|
                    +--------------------------+
                               |
               ┌───────────────┴───────────────┐
               |                               |
        "Search Product"                Other Intents
               |                               |
               v                               v
+----------------------------------+    +---------------------+
| Semantic Search via Vector DB    |    | (Optional) Routing  |
| - SentenceTransformer Embedding  |    | Different Handlers  |
| - Vector DB                      |    +---------------------+
+----------------------------------+
               |
               v
+----------------------------------+
|   Top-k Matched Product Entries  |
|   - title, brand, category       |
+----------------------------------+
               |
               v
+----------------------------------+
|        FastAPI REST API          |
|  - POST Search                  |
|  - Returns JSON: intent + items  |
+----------------------------------+
               |
               v
        +------------------+
        |    Client UI     |
        | (curl, browser,  |
        | Postman, etc.)   |
        +------------------+



