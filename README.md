Semantic Search System with Endee Vector Database
Project Overview

This project implements a Semantic Search system using a vector database inspired by Endee.
Instead of relying on keyword matching, the system retrieves documents based on semantic similarity, allowing more meaningful and context-aware search results.

The application is built using Python and Flask and exposes REST APIs for indexing and searching documents using cosine similarity over vector embeddings.

Note: Retrieval-Augmented Generation
This project focuses only on the retrieval layer to clearly demonstrate vector-based semantic search.

Features

Semantic (meaning-based) document search

Vector similarity search using cosine similarity

Endee-style vector database implementation

RESTful API built with Flask

Lightweight and easy to extend


Architecture
Client → Flask REST API → Endee Vector Database → Top-K Relevant Results


Installation
  Step 1: Clone the Repository
  git clone https://github.com/your-username/semantic-search-endee.git
  cd semantic-search-endee

Step 2: 
Create Virtual Environment (Optional but Recommended)
  python -m venv .venv
  source .venv/bin/activate   # On Windows: .venv\Scripts\activate

Step 3: 
  Install Dependencies
    pip install -r requirements.txt

Running the Application

Start the Flask server using:

python app.py


If successful, you will see:

Semantic Search API running on http://127.0.0.1:5000
Endee loaded 5 papers

How to Check the Working of the Use Case
1) Check Application Status

Open your browser or use curl:

http://127.0.0.1:5000/


Expected response:

{
  "project": "Semantic Search using Endee Vector Database",
  "status": "Running"
}

2) Health Check Endpoint
  GET http://127.0.0.1:5000/health


This confirms:

Vector database is loaded

Number of stored vectors

System health

3) Perform Semantic Search (Main Use Case)
Endpoint
POST /api/search/semantic

Sample Request
curl -X POST http://127.0.0.1:5000/api/search/semantic \
-H "Content-Type: application/json" \
-d '{
  "query": "attention mechanism in transformers",
  "top_k": 3
}'

Sample Response
{
  "query": "attention mechanism in transformers",
  "results": [
    {
    "id": "paper_1",
      "score": 0.91,
      "metadata": {
        "title": "Attention Is All You Need",
        "authors": "Vaswani et al.",
        "year": 2017
      }
    }
  ],
  "result_count": 3
}


        This confirms that the system successfully retrieves contextually relevant documents.

4️)Run Automated Test Script (Optional)
python test_complete.py


This script:

Tests the health endpoint

Creates an index

Executes a semantic search query


Conclusion

This project demonstrates a complete semantic search pipeline using vector similarity and an Endee-style vector database. It clearly showcases how modern AI search systems retrieve information based on meaning rather than keywords and serves as a strong foundation for advanced AI applications such as Semantic and recommendation systems.
