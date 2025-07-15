import torch
import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample corpus
sentences = [
    "I love programming in Python",
    "Python is a great programming language",
    "I enjoy cooking Italian food",
    "Pasta is my favorite Italian dish",
    "Machine learning is fascinating",
    "I like to learn about AI",
    "The weather is nice today",
    "I enjoy going for walks in the park",
]

# Precompute embeddings
embeddings = model.encode(sentences)

def get_closest_match(query, corpus, embeddings):
    query_embedding = model.encode([query]).reshape(1, -1)
    similarities = cosine_similarity(query_embedding, embeddings)
    best_idx = np.argmax(similarities)
    return corpus[best_idx], similarities[0][best_idx]

# Streamlit UI
st.title("🧠 Semantic Search Engine")

user_query = st.text_input("🔍 Enter your query here:")

if user_query:
    best_match, similarity_score = get_closest_match(user_query, sentences, embeddings)
    st.success(f"✅ Best Match: **{best_match}**")
    st.info(f"🧮 Similarity Score: `{similarity_score:.3f}`")

    # Optionally show all matches
    st.subheader("📊 Similarity Breakdown")
    query_embedding = model.encode([user_query]).reshape(1, -1)
    similarities = cosine_similarity(query_embedding, embeddings).flatten()
    for i, sentence in enumerate(sentences):
        st.write(f"`{similarities[i]:.3f}` → {sentence}")
