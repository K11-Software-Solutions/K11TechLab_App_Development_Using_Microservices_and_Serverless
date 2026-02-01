from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

@app.route("/papers", methods=["GET"])
def get_papers():
    topic = request.args.get("topic")
    if not topic:
        return jsonify({"error": "Missing 'topic' query parameter."}), 400
    params = {
        "query": topic,
        "limit": 5,
        "fields": "title,authors,year,abstract,url"
    }
    try:
        resp = requests.get(SEMANTIC_SCHOLAR_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        papers = [
            {
                "title": p.get("title"),
                "authors": [a.get("name") for a in p.get("authors", [])],
                "year": p.get("year"),
                "abstract": p.get("abstract"),
                "url": p.get("url")
            }
            for p in data.get("data", [])
        ]
        return jsonify({"topic": topic, "papers": papers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)
