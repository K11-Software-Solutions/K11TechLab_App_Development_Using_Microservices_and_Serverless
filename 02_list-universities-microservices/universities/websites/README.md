# Universities Websites Microservice

A Python Flask microservice to retrieve university websites by name.

## Endpoints
- `/websites/<name>` : Returns a list of website URLs for the given university name.

## How to Run
1. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Access at [http://localhost:5001/websites/<name>](http://localhost:5001/websites/<name>)

## Files
- `app.py`: Main Flask application.
- `UK_Universities.json`: Data source.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Containerization support.

---
