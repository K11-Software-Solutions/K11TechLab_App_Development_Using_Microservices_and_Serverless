import requests
import json

def test_papers(topic):
    url = "http://127.0.0.1:5010/papers"
    params = {"topic": topic}
    resp = requests.get(url, params=params)
    try:
        resp.raise_for_status()
        data = resp.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
        # Save result to a JSON file
        filename = f"result_{topic.replace(' ', '_').lower()}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        assert "papers" in data
        print(f"Test passed for {topic}, result saved to {filename}")
    except Exception as e:
        print(f"Test failed for {topic}: {e}")
        print(resp.text)

if __name__ == "__main__":
    for topic in ["machine learning", "quantum computing", "climate change"]:
        test_papers(topic)
