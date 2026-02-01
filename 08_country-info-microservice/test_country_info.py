import requests
import json

def test_country_info(country):
    url = "http://127.0.0.1:5007/country-info"
    params = {"country": country}
    resp = requests.get(url, params=params)
    try:
        resp.raise_for_status()
        data = resp.json()
        # If the result is a list, try to select the correct country by name
        if isinstance(data, list):
            # Try to match the country name exactly (case-insensitive)
            match = next((item for item in data if item.get("name", {}).get("common", "").lower() == country.lower()), data[0])
        else:
            match = data
        print(json.dumps(match, indent=2, ensure_ascii=False))
        # Save result to a JSON file named after the country
        filename = f"result_{country.replace(' ', '_').lower()}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(match, f, indent=2, ensure_ascii=False)
        assert "iso_codes" in match
        assert "languages" in match
        assert "currencies" in match
        assert "capital" in match
        assert "population" in match
        assert "area" in match
        print(f"Test passed for {country}, result saved to {filename}")
    except Exception as e:
        print(f"Test failed for {country}: {e}")
        print(resp.text)

if __name__ == "__main__":
    # Test with a few countries
    # Use full official names for ambiguous countries
    for country in ["France", "Switzerland", "Republic of India", "United States of America"]:
        test_country_info(country)
