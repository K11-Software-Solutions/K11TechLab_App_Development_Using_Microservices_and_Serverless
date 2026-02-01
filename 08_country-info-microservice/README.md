# Country Immigration Microservice

This microservice provides country information using the REST Countries public API and a placeholder for immigration rules.

## How to Run

1. Install dependencies:
   
   pip install -r requirements.txt

2. Start the service:
   
   python app.py

The service will run on port 5007 by default.

## API Endpoint

- `GET /country-info?country=<country_name>`
  - Returns: country info and a placeholder for immigration rules
  - Example: `/country-info?country=France`

## Example Response

```
{
  "name": "France",
  "official_name": "French Republic",
  "region": "Europe",
  "subregion": "Western Europe",
  "capital": "Paris",
  "population": 67391582,
  "area": 551695.0,
  "flag": "https://flagcdn.com/w320/fr.png",
  "immigration_rules": "No free public API for immigration rules. Please consult the official government website for up-to-date immigration requirements."
}
```

## Notes
- Country data is fetched live from https://restcountries.com/
- Immigration rules are not available via a free public API; users are directed to official sources.
