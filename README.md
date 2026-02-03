# Semantic-Search-System-with-Endee-Vector-Database
This project implements a semantic search system using an Endee-style vector database. Documents and queries are represented as embeddings and matched using cosine similarity. The system retrieves contextually relevant results via a Flask REST API, focusing only on the retrieval layer .
# Semantic Search using Endee Vector Database (No RAG)

Project Overview
This project implements a **Semantic Search system** using a vector database inspired by **Endee**.
It retrieves documents based on **semantic similarity** rather than keyword matching.

> Note: Retrieval-Augmented Generation (RAG) is intentionally excluded.
> This project focuses on the **retrieval layer only**.

---

Features
- Vector-based semantic search
- Cosine similarity matching
- REST API using Flask
- Endee-style vector database implementation

---

Architecture
Client → Flask API → Endee Vector DB → Top-K Results

---

Installation

```bash
git clone https://github.com/your-username/semantic-search-endee.git
cd semantic-search-endee
pip install -r requirements.txt

