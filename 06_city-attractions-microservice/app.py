from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEOCODE_URL = "http://localhost:5004/geocode"
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

@app.route("/attractions", methods=["GET"])
def get_attractions():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing 'city' query parameter."}), 400
    # Get city coordinates from geocode microservice
    try:
        geo_resp = requests.get(GEOCODE_URL, params={"city": city})
        if geo_resp.status_code != 200:
            return jsonify({"error": f"Geocode service error: {geo_resp.text}"}), geo_resp.status_code
        geo_data = geo_resp.json()
        lat = geo_data["latitude"]
        lon = geo_data["longitude"]
    except Exception as e:
        return jsonify({"error": f"Failed to get coordinates: {str(e)}"}), 500
    # Query Wikipedia for attractions near the coordinates
    try:
        params = {
            "action": "query",
            "list": "geosearch",
            "gscoord": f"{lat}|{lon}",
            "gsradius": 10000,  # 10km
            "gslimit": 10,
            "format": "json"
        }
        headers = {"User-Agent": "city-attractions-microservice/1.0 (contact: youremail@example.com)"}
        wiki_resp = requests.get(WIKIPEDIA_API_URL, params=params, headers=headers)
        wiki_resp.raise_for_status()
        data = wiki_resp.json()
        attractions = [item["title"] for item in data.get("query", {}).get("geosearch", [])]
        return jsonify({"city": city, "attractions": attractions})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch attractions: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
