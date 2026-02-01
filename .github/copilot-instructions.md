# Copilot Instructions: IBM Full Stack Microservices & Serverless Projects

## Architecture Overview
- **Microservices Structure:**
  - Each top-level folder is a standalone microservice (Flask for Python, Express for Node.js), with its own `app.py` or `server.js`, `requirements.txt` or `package.json`, and `Dockerfile`.
  - The `Product_Price_Comparison_Application` contains a multi-service app:
    - `dealer_evaluation_backend/products_list`: Flask, serves product/dealer data from `products.json`.
    - `dealer_evaluation_backend/dealer_details`: Express, serves price data from `utils/dealers.json`.
    - `dealer_evaluation_frontend`: Flask, serves static HTML (`html/index.html`).
  - Standalone microservices: `01_flask-hello-world-server`, `03_weather_microservice`, `04_stock-price-microservice` (all Flask, Python).
  - Labs in `REST_API_AND_GraphQL/` include CRUD, GraphQL, and Swagger/OpenAPI examples.

## Developer Workflows
- **Python Services:**
  - Install: `pip install -r requirements.txt`
  - Run: `python app.py` (default ports: 5000, 5001, or as specified in README)
- **Node.js Services:**
  - Install: `npm install`
  - Run: `node server.js` (default port: 8080)
- **Swagger-Generated Servers:**
  - Install: `pip3 install -r requirements.txt`
  - Run: `python3 -m swagger_server` (port 8080)
  - Docker: `docker build -t swagger_server .` then `docker run -p 8080:8080 swagger_server`
- **Frontend:**
  - Run: `python app.py` (serves `html/index.html`)

## Patterns & Conventions
- **Service Boundaries:** Each microservice is self-contained; data is read from local JSON files (e.g., `products.json`, `dealers.json`, `UK_Universities.json`).
- **Endpoints:**
  - Flask: `/products`, `/getdealers/<product>`
  - Express: `/price/:dealer/:product`, `/allprice/:product`
  - Frontend: `/` (homepage)
- **Containerization:** Each service has a `Dockerfile` for container builds. No shared base images enforced.
- **Data Flow:** Frontend queries backend microservices via HTTP; backends read from local JSON files. No direct DB or message queue integration.
- **Swagger/OpenAPI:** Used for API documentation and server generation in some labs (see `swagger_server/`).

## Integration Points
- **Cross-Service Communication:** Always via HTTP endpoints. No shared state or direct DB connections between services.
- **Data Sources:** All persistent data is stored in local JSON files within each service.

## Key Files & Directories
- `Product_Price_Comparison_Application/`: Main multi-service app
- `REST_API_AND_GraphQL/`: Labs and generated servers
- `01_flask-hello-world-server/`, `03_weather_microservice/`, `04_stock-price-microservice/`: Standalone microservices

## Example: Adding a New Microservice
1. Create a new folder with `app.py` or `server.js`, `requirements.txt` or `package.json`, and `Dockerfile`.
2. Use a local JSON file for data, expose REST endpoints, and document in a local `README.md`.

---
For unclear or missing conventions, review the relevant `README.md` in each service folder. Please provide feedback if any section needs clarification or expansion.
