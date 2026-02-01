# Weather Microservice

This microservice provides current weather information for a given city using the OpenWeatherMap API.

## Usage
- Start the Flask server: `python app.py`
- Make a GET request to `/weather?city=CityName`

## Example
```
GET /weather?city=London
Response:
{
  "city": "London",
  "temperature": 15.0,
  "description": "light rain"
}
```

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Add your OpenWeatherMap API key in `app.py`.
3. Run the server:
   ```
   python app.py
   ```

## Files
- app.py: Main Flask application
- requirements.txt: Python dependencies
