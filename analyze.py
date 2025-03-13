from transformers import pipeline
from sentence_transformers import SentenceTransformer
import numpy as np

sentiment_pipeline = pipeline("sentiment-analysis")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


EMAIL_CLASSES = []

def load_class_file():
    # open file in read mode, append each new line to EMAIL_CLASSES, stripping white space & new lines
    with open("classes.txt", "r") as file:
        for line in file:
            EMAIL_CLASSES.append(line.strip())

def get_email_classes():
    return EMAIL_CLASSES

def add_new_email_classes(new_classes: list[str]):
    # check if new classes already exist in EMAIL_CLASSES
    classes_to_add = [c for c in new_classes if c not in EMAIL_CLASSES]
    # if there are new classes to add, append to EMAIL_CLASSES and file
    if classes_to_add:
        EMAIL_CLASSES.extend(classes_to_add)
        with open("classes.txt", "a") as file:
            for c in classes_to_add:
                file.write(c + "\n")

def get_sentiment(text):
    response = sentiment_pipeline(text)
    return response

def compute_embeddings(embeddings = EMAIL_CLASSES):
    embeddings = model.encode(embeddings)
    return zip(EMAIL_CLASSES, embeddings)

def classify_email(text):
    # Encode the input text
    text_embedding = model.encode([text])[0]
    
    # Get embeddings for all classes
    class_embeddings = compute_embeddings()
    
    # Calculate distances and return results
    results = []
    for class_name, class_embedding in class_embeddings:
        # Compute cosine similarity between text and class embedding
        similarity = np.dot(text_embedding, class_embedding) / (np.linalg.norm(text_embedding) * np.linalg.norm(class_embedding))
        results.append({
            "class": class_name,
            "similarity": float(similarity)  # Convert tensor to float for JSON serialization
        })
    
    # Sort by similarity score descending
    results.sort(key=lambda x: x["similarity"], reverse=True)
    
    return results