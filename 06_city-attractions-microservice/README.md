# City Attractions Microservice

This microservice fetches tourist attractions in a city using Wikipedia's GeoSearch API. It depends on the city-geocode-microservice for coordinates.

## How to Run

1. Install dependencies:
   
   pip install -r requirements.txt

2. Start the service:
   
   python app.py

The service will run on port 5005 by default.

## API Endpoint

- `GET /attractions?city=<city_name>`
  - Returns: `{ "city": ..., "attractions": [...] }`
  - Example: `/attractions?city=London`

## Example Response

```
{
  "city": "London",
  "attractions": [
    "Big Ben",
    "London Eye",
    "Buckingham Palace",
    ...
  ]
}
```

## Notes
- Requires the city-geocode-microservice to be running on port 5004.
- Uses Wikipedia's public API (subject to usage policy).
- Returns 400 if city parameter missing, 500 if errors occur.
