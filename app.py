from fastapi import FastAPI
from pydantic import BaseModel
from intent_classification.intent import detect_intent
from query_search.search import search_products


app = FastAPI()

class Query(BaseModel):
    query: str

# API operations
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

@app.get("/info")
def info():
    return {'name': 'product-search', 'description': "Search API for AI Hackathon 2025."}

@app.post("/search")
def search_api(q: Query):
    intent = detect_intent(q.query)
    
    results = search_products(q.query, 5)
    
    output = [
        {
            "title": hit["title"],
            "brand": hit["brand"],
            "category": hit["category"]
        }
        for hit in results
    ]
    return {"intent": intent, "results": output}