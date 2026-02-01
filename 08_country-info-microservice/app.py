from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

REST_COUNTRIES_URL = "https://restcountries.com/v3.1/name/"
# No free public API for immigration rules, so we provide country info and a placeholder for immigration rules

@app.route("/country-info", methods=["GET"])
def country_info():
    country = request.args.get("country")
    if not country:
        return jsonify({"error": "Missing 'country' query parameter."}), 400
    try:
        resp = requests.get(REST_COUNTRIES_URL + country)
        resp.raise_for_status()
        data = resp.json()
        if not data or not isinstance(data, list):
            return jsonify({"error": "Country not found."}), 404
        country_data = data[0]
        result = {
            "name": country_data.get("name", {}).get("common"),
            "official_name": country_data.get("name", {}).get("official"),
            "region": country_data.get("region"),
            "subregion": country_data.get("subregion"),
            "capital": country_data.get("capital", [None])[0],
            "population": country_data.get("population"),
            "area": country_data.get("area"),
            "flag": country_data.get("flags", {}).get("png"),
            "iso_codes": {
                "alpha2": country_data.get("cca2"),
                "alpha3": country_data.get("cca3"),
                "numeric": country_data.get("ccn3")
            },
            "languages": list(country_data.get("languages", {}).values()) if country_data.get("languages") else [],
            "currencies": [
                {
                    "code": code,
                    "name": val.get("name"),
                    "symbol": val.get("symbol")
                } for code, val in (country_data.get("currencies") or {}).items()
            ],
            "immigration_rules": "No free public API for immigration rules. Please consult the official government website for up-to-date immigration requirements."
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007, debug=True)
