"""
Semantic Search System using Endee Vector Database (Mock Implementation)
"""

from flask import Flask, request, jsonify
import numpy as np
from datetime import datetime

app = Flask(__name__)

# -------------------------------
# Mock Endee Vector Database
# -------------------------------
class EndeeVectorDB:
    def __init__(self):
        self.vectors = {}
        self.dimension = 384
        self.index_name = "papers"
        self.load_papers()

    def create_index(self, name="papers"):
        self.index_name = name
        return {
            "success": True,
            "index": name,
            "dimension": self.dimension,
            "timestamp": datetime.now().isoformat()
        }

    def upsert(self, vectors):
        for v in vectors:
            self.vectors[v["id"]] = {
                "vector": np.array(v["vector"]),
                "metadata": v["metadata"]
            }
        return {
            "success": True,
            "inserted": len(vectors),
            "total_vectors": len(self.vectors)
        }

    def cosine_similarity(self, a, b):
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query_vector, top_k=5):
        results = []
        for doc_id, doc in self.vectors.items():
            score = self.cosine_similarity(query_vector, doc["vector"])
            results.append({
                "id": doc_id,
                "score": round(float(score), 4),
                "metadata": doc["metadata"]
            })
        return sorted(results, key=lambda x: x["score"], reverse=True)[:top_k]

    def load_papers(self):
        papers = [
            {
                "id": "paper_1",
                "title": "Attention Is All You Need",
                "text": "Transformer model using self-attention.",
                "authors": "Vaswani et al.",
                "year": 2017
            },
            {
                "id": "paper_2",
                "title": "Multi-Head Attention",
                "text": "Parallel attention mechanisms.",
                "authors": "Vaswani et al.",
                "year": 2017
            },
            {
                "id": "paper_3",
                "title": "Vector Databases",
                "text": "High-dimensional semantic search.",
                "authors": "AI Research Collective",
                "year": 2025
            },
            {
                "id": "paper_4",
                "title": "Endee Vector Database",
                "text": "Efficient vector similarity search.",
                "authors": "Endee Labs",
                "year": 2026
            },
            {
                "id": "paper_5",
                "title": "Semantic Search Systems",
                "text": "Meaning-based information retrieval.",
                "authors": "IR Community",
                "year": 2024
            }
        ]

        for p in papers:
            vec = np.random.rand(self.dimension)
            vec = vec / np.linalg.norm(vec)
            self.upsert([{
                "id": p["id"],
                "vector": vec.tolist(),
                "metadata": p
            }])

        print(f"✅ Endee loaded {len(papers)} papers")

# Initialize DB
endee = EndeeVectorDB()

# -------------------------------
# API Endpoints
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Semantic Search using Endee Vector Database",
        "status": "Running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "total_vectors": len(endee.vectors),
        "dimension": endee.dimension,
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/v1/index/create", methods=["POST"])
def create_index():
    data = request.json or {}
    return jsonify(endee.create_index(data.get("name", "papers"))), 201

@app.route("/api/search/semantic", methods=["POST"])
def semantic_search():
    data = request.json or {}
    top_k = min(data.get("top_k", 5), len(endee.vectors))

    # Mock query embedding
    query_vector = np.random.rand(endee.dimension)
    query_vector = query_vector / np.linalg.norm(query_vector)

    results = endee.search(query_vector, top_k)

    return jsonify({
        "query": data.get("query", ""),
        "results": results,
        "result_count": len(results),
        "timestamp": datetime.now().isoformat()
    })

# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
