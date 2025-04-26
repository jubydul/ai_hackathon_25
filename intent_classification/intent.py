from transformers import pipeline

classifier = pipeline("zero-shot-classification")
labels = ["search_product", "browse_category", "ask_brand", "generic_question"]

def detect_intent(query):
    result = classifier(query, labels)
    return result["labels"][0]

# print(detect_intent("laptop"))