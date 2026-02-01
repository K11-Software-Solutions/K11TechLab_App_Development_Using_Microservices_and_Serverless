# Stock Price Microservice

A simple Flask microservice to fetch the latest market value for a given stock symbol using Yahoo Finance API (via RapidAPI).

## Usage
- Endpoint: `/price?symbol=XYZ`
- Returns: Latest price for the given symbol in JSON format.

## Setup
1. Get a free RapidAPI key from [RapidAPI Yahoo Finance](https://rapidapi.com/apidojo/api/yh-finance).
2. Set the environment variable `RAPIDAPI_KEY` with your key.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`

## Docker
```
docker build -t stock-price-microservice .
docker run -p 5000:5000 -e RAPIDAPI_KEY=your_key stock-price-microservice
```
