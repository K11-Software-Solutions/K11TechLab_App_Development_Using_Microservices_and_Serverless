from flask import Flask, jsonify
import requests

app = Flask(__name__)

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = "DEMO_KEY"  # Replace with your own API key for higher rate limits

@app.route("/astronomy-info", methods=["GET"])
def get_astronomy_info():
    try:
        resp = requests.get(NASA_APOD_URL, params={"api_key": NASA_API_KEY})
        resp.raise_for_status()
        data = resp.json()
        result = {
            "title": data.get("title"),
            "date": data.get("date"),
            "explanation": data.get("explanation"),
            "image_url": data.get("url"),
            "media_type": data.get("media_type"),
            "copyright": data.get("copyright", "Public Domain/NASA")
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006, debug=True)
