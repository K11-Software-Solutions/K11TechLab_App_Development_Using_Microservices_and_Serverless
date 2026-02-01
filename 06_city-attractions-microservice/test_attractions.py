import requests
import json

def test_attractions(city="London", output_file="test_attractions_response.json"):
    url = "http://localhost:5005/attractions"
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

import sys

if __name__ == "__main__":
    # Allow running for multiple cities/output files from command line
    args = sys.argv[1:]
    if not args:
        test_attractions()
    elif len(args) == 1:
        test_attractions(args[0], f"test_attractions_{args[0].lower()}.json")
    else:
        for i in range(0, len(args), 2):
            city = args[i]
            output = args[i+1] if i+1 < len(args) else f"test_attractions_{city.lower()}.json"
            test_attractions(city, output)
