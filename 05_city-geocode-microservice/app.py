from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Free geocoding API endpoint (OpenStreetMap Nominatim)
GEOCODE_URL = "https://nominatim.openstreetmap.org/search"

@app.route("/geocode", methods=["GET"])
def geocode_city():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing 'city' query parameter."}), 400
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    try:
        resp = requests.get(GEOCODE_URL, params=params, headers={"User-Agent": "city-geocode-microservice"})
        resp.raise_for_status()
        data = resp.json()
        if not data:
            return jsonify({"error": "City not found."}), 404
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return jsonify({"city": city, "latitude": lat, "longitude": lon})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)
