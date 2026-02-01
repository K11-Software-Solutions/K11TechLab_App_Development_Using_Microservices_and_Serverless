import requests
import json
import sys

def test_geocode(city="London", output_file="test_geocode_response.json"):
    url = "http://localhost:5004/geocode"
    params = {"city": city}
    resp = requests.get(url, params=params)
    try:
        resp.raise_for_status()
        data = resp.json()
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Response saved to {output_file}")
        return data
    except Exception as e:
        print(f"Test failed: {e}")
        return None

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        test_geocode()
    elif len(args) == 1:
        test_geocode(args[0], f"test_geocode_{args[0].lower()}.json")
    else:
        for i in range(0, len(args), 2):
            city = args[i]
            output = args[i+1] if i+1 < len(args) else f"test_geocode_{city.lower()}.json"
            test_geocode(city, output)
