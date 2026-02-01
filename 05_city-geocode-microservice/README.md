# City Geocode Microservice

This microservice provides the latitude and longitude for a given city name using the OpenStreetMap Nominatim API.

## How to Run

1. Install dependencies:
   
   pip install -r requirements.txt

2. Start the service:
   
   python app.py

The service will run on port 5004 by default.

## API Endpoint

- `GET /geocode?city=<city_name>`
  - Returns: `{ "city": ..., "latitude": ..., "longitude": ... }`
  - Example: `/geocode?city=London`

## Example Response

```
{
  "city": "London",
  "latitude": "51.5073219",
  "longitude": "-0.1276474"
}
```

## Notes
- Uses OpenStreetMap Nominatim API (subject to usage policy).
- Returns 404 if city not found, 400 if city parameter missing.
