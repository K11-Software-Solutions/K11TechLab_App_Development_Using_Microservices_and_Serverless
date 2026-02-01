import requests
import json

def test_astronomy_info(output_file="test_astronomy_info_response.json"):
    url = "http://localhost:5006/astronomy-info"
    try:
        resp = requests.get(url)
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
    test_astronomy_info()
