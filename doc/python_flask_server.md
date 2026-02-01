# Python Flask Server Documentation

## Overview
A Python Flask server is a lightweight web application framework used to build web APIs and microservices. Flask is simple, flexible, and easy to use for rapid development.

## Key Features
- Minimal setup and easy to learn
- Supports RESTful request routing
- Can serve static and dynamic content
- Easily extensible with Flask extensions

## Basic Structure
A typical Flask server consists of:
- Importing Flask and initializing the app
- Defining routes using decorators
- Running the app

### Example
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

## Running a Flask Server
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Save your code in a file (e.g., `app.py`).
3. Run the server:
   ```bash
   python app.py
   ```
4. Access the server at [http://localhost:5000](http://localhost:5000)

## Common Flask Files
- `app.py`: Main application file
- `requirements.txt`: Lists dependencies
- `Dockerfile`: For containerization

## Useful Flask Extensions
- `flask-cors`: Enable Cross-Origin Resource Sharing
- `flask-restful`: Build REST APIs
- `flask-login`: User session management

## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
