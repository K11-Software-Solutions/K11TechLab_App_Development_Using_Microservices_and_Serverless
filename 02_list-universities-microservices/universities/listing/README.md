# Universities Listing Microservice

A Python Flask microservice to list UK universities and search by name.

## Endpoints
- `/colleges` : Returns a list of all university names.
- `/colleges/<name>` : Returns universities matching the given name.

## How to Run
1. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Access at [http://localhost:5000/colleges](http://localhost:5000/colleges)

## Files
- `app.py`: Main Flask application.
- `UK_Universities.json`: Data source.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Containerization support.

---
