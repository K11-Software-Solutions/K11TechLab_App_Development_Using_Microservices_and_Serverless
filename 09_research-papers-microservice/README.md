# Research Papers Microservice

This microservice fetches published research papers based on a given topic using a public API (Semantic Scholar).

## Endpoint
- `/papers?topic=TOPIC` — Returns a list of research papers for the given topic.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start the service: `python app.py`
3. Query: `GET /papers?topic=machine+learning`