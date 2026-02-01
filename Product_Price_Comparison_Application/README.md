# Product Price Comparison Application

This project is a microservices-based web application for comparing product prices from different dealers. It consists of three main services:

- **products_list (Flask, Python):** Serves product and dealer data from products.json
- **dealer_details (Express, Node.js):** Serves price data for products from dealers.json
- **dealer_evaluation_frontend (Flask, Python):** Serves the web frontend and communicates with the backend services

## Architecture

```
[Frontend (Flask)]
    |
    |--(HTTP GET /products)--------------------> [products_list (Flask)]
    |
    |--(HTTP GET /getdealers/<product>)-------> [products_list (Flask)]
    |
    |--(HTTP GET /allprice/:product)----------> [dealer_details (Express)]
    |
    |--(HTTP GET /price/:dealer/:product)-----> [dealer_details (Express)]
```

## Service Communication

- The **frontend** makes HTTP requests to the backend services:
  - `/products` and `/getdealers/<product>` to the products_list service (Python Flask)
  - `/allprice/:product` and `/price/:dealer/:product` to the dealer_details service (Node.js Express)
- The **backend services** read from their local JSON files and return JSON responses.
- All communication is via RESTful HTTP endpoints (no direct DB or message queue).

## How to Run
1. Start the backend services:
   - `cd dealer_evaluation_backend/products_list && python app.py`
   - `cd dealer_evaluation_backend/dealer_details && node server.js`
2. Start the frontend:
   - `cd dealer_evaluation_frontend && python app.py`
3. Open the frontend in your browser (default: http://localhost:5000)

## Example API Calls
- `GET /products` — List all products
- `GET /getdealers/<product>` — List dealers for a product
- `GET /allprice/:product` — Get all prices for a product
- `GET /price/:dealer/:product` — Get price for a product from a specific dealer

## Data Flow
- The frontend fetches product and dealer info from products_list
- It fetches price info from dealer_details
- All data is returned as JSON and rendered in the frontend

## Technology Stack
- Python (Flask)
- Node.js (Express)
- RESTful APIs
- JSON for data exchange

See each service's README for more details on endpoints and data formats.
