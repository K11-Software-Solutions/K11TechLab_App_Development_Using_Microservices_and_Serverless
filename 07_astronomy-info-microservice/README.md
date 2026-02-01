# Astronomy Info Microservice

This microservice provides dynamic astronomy information by fetching NASA's Astronomy Picture of the Day (APOD) with image, title, and explanation.

## How to Run

1. Install dependencies:
   
   pip install -r requirements.txt

2. Start the service:
   
   python app.py

The service will run on port 5006 by default.

## API Endpoint

- `GET /astronomy-info`
  - Returns: the latest NASA APOD image, title, explanation, and metadata

## Example Response

```
{
  "title": "A Beautiful Astronomy Image",
  "date": "2026-01-31",
  "explanation": "This is the NASA Astronomy Picture of the Day explanation...",
  "image_url": "https://apod.nasa.gov/apod/image/2401/example.jpg",
  "media_type": "image",
  "copyright": "Public Domain/NASA"
}
```

## Notes
- Data is fetched live from NASA's APOD API (https://api.nasa.gov/planetary/apod)
- Uses NASA's DEMO_KEY by default (replace with your own for higher rate limits)
