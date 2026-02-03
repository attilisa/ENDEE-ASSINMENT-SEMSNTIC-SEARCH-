import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    print("Health:", r.status_code, r.json())

def test_index():
    r = requests.post(f"{BASE_URL}/api/v1/index/create", json={"name": "papers"})
    print("Create Index:", r.status_code, r.json())

def test_search():
    payload = {
        "query": "attention mechanism",
        "top_k": 3
    }
    r = requests.post(f"{BASE_URL}/api/search/semantic", json=payload)
    print("Semantic Search:", r.status_code)
    print(r.json())

if __name__ == "__main__":
    time.sleep(1)
    test_health()
    test_index()
    test_search()
