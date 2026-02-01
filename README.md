<p align="center">
  <img src="artifacts/assets/k11_logo.png" alt="K11 Software Solutions Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
  <img src="artifacts/assets/Node.js_logo.png" alt="Node.js Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
  <img src="artifacts/assets/expressjs.png" alt="Express Logo" height="60" style="margin-right:20px;vertical-align:middle;"/>
</p>

# K11 Software Solutions Full Stack Microservices & Serverless Projects: Learning Path

This repository contains a curated set of microservices, REST APIs, and OpenAPI/Swagger demonstration projects. Each project is designed to teach a specific concept in modern API and microservice development.

## Project List (1–14)

1. **01_flask-hello-world-server** — Simple Flask REST API (hello world)
2. **02_list-universities-microservices** — University listing and website microservices
3. **03_weather_microservice** — Weather API microservice
4. **04_stock-price-microservice** — Stock price API microservice
5. **05_geocoding-microservice** — Geocoding API microservice
6. **06_attractions-microservice** — Tourist attractions API microservice
7. **07_astronomy-info-microservice** — Astronomy info API microservice
8. **08_country-info-microservice** — Country info API microservice
9. **09_research-papers-microservice** — Research papers API microservice
10. **10_graphql-city-state-microservice** — GraphQL API for city/state info
11. **11_swagger-example-microservice** — Swagger/OpenAPI demonstration microservice
12. **12_swagger-techtasks-microservice** — Technology tasks API with Swagger/OpenAPI
13. **13_openapi-demo** — Minimal Flask API with OpenAPI 3.0 spec
14. **14_openapi-crud-demo** — CRUD API with OpenAPI 3.0, pytest automation

---

## How to Use This Repository
- Start with project 01 for basic REST concepts
- Progress through each project to learn data handling, API documentation, and automation
- Use the README in each project for setup and usage instructions
- See `doc/pytest_automation.md` and `14_openapi-crud-demo/TESTING.md` for testing and automation guidance

# Product Price Comparison Application

The **Product Price Comparison Application** is a microservices-based project designed to demonstrate a multi-service architecture for comparing product prices across different dealers. It is organized as follows:

## Architecture Overview
- **Backend Microservices:**
	- `dealer_evaluation_backend/products_list` (Flask, Python): Serves product and dealer data from a local `products.json` file via REST endpoints.
	- `dealer_evaluation_backend/dealer_details` (Express, Node.js): Provides price data for products and dealers, reading from `utils/dealers.json`.
- **Frontend:**
	- `dealer_evaluation_frontend` (Flask, Python): Serves a static HTML interface (`html/index.html`) for users to interact with the application.

## Data Flow
1. The frontend presents a user interface for selecting products and viewing price comparisons.
2. It communicates with the backend microservices via HTTP requests:
	 - Fetches product and dealer lists from the products_list service.
	 - Retrieves price information from the dealer_details service.
3. All persistent data is stored in local JSON files within each service; there is no shared database.

## Endpoints
- **Products List Service (Flask):**
	- `/products`: Returns available products and dealers.
	- `/getdealers/<product>`: Returns dealers for a specific product.
- **Dealer Details Service (Express):**
	- `/price/:dealer/:product`: Returns the price for a given dealer and product.
	- `/allprice/:product`: Returns all prices for a given product.
- **Frontend (Flask):**
	- `/`: Serves the main HTML page.

## Running the Application
Each service is self-contained with its own `requirements.txt` or `package.json` and `Dockerfile`. To run locally:
1. Install dependencies for each service (Python: `pip install -r requirements.txt`, Node.js: `npm install`).
2. Start each backend and frontend service individually (Python: `python app.py`, Node.js: `node server.js`).
3. Access the frontend in your browser to use the application.

## Containerization
Each service can be built and run as a Docker container using the provided `Dockerfile` in each directory.

## Integration Points
- All cross-service communication is via HTTP endpoints.
- No direct database or message queue integration; all data is local to each service.

For more details, see the `Product_Price_Comparison_Application/` directory and the individual service READMEs.


## Recommended Tools
- Python (Flask)
- Node.js (Express, GraphQL)
- Swagger UI, Swagger Editor, SwaggerHub
- Pytest, pytest-cov, pytest-html
- GitHub Actions for CI/CD

---

This learning path is designed for hands-on mastery of microservices, REST APIs, OpenAPI/Swagger, and automation best practices.


## About k11 Software Solutions

**k11 Software Solutions** is a leading provider of modern, AI-powered test automation, DevOps, and quality engineering services. We help organizations accelerate digital transformation with robust, scalable, and intelligent automation solutions tailored for SaaS, web, and enterprise platforms.

- Website: [https://k11softwaresolutions.com](https://k11softwaresolutions.com)
- Contact: k11softwaresolutions@gmail.com

*Partner with us to future-proof your QA and automation strategy!*

## Follow Me
<p align="center">
    <a href="https://github.com/K11-Software-Solutions/" target="_blank">
        <img src="https://img.shields.io/badge/K11%20Tech%20Lab-FFFFFF?style=for-the-badge&logo=github&logoColor=black" alt="K11 Tech Lab"/>
    </a>
    <a href="https://k11softwaresolutions.com" target="_blank">
        <img src="https://img.shields.io/badge/k11softwaresolutions-00B386?style=for-the-badge&logo=google-chrome&logoColor=white" alt="k11softwaresolutions"/>
    </a>
</p>
