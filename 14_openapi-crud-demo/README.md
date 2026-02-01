# OpenAPI CRUD Demo Microservice

This project demonstrates a CRUD API for products using Flask, documented with OpenAPI 3.0.

## Features
- List, add, get, and delete products
- OpenAPI 3.0 spec served at `/openapi.json`
- Ready for visualization in Swagger UI, Swagger Editor, or SwaggerHub

## Endpoints
- `GET /products` — List all products
- `POST /product` — Add a new product (JSON: {"name": ..., "price": ...})
- `GET /product/<pid>` — Get a product by ID
- `DELETE /product/<pid>` — Delete a product by ID
- `GET /openapi.json` — Returns the OpenAPI 3.0 spec for this API

## How to Run
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the app:
   ```sh
   python crud_api.py
   ```
3. Access the API at [http://localhost:5000/products](http://localhost:5000/products)
4. Access the OpenAPI spec at [http://localhost:5000/openapi.json](http://localhost:5000/openapi.json)

## Visualize with Swagger Tools
- Open [Swagger Editor](https://editor.swagger.io/) and import `openapi.json` or `http://localhost:5000/openapi.json`
- Try out the endpoints interactively
- You can also use SwaggerHub, Redoc, Postman, Insomnia, etc.

## Example OpenAPI Spec
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "CRUD Products API",
    "version": "1.0.0"
  },
  "paths": {
    "/products": {"get": {"summary": "List all products"}},
    "/product": {"post": {"summary": "Add a new product"}},
    "/product/{pid}": {"get": {"summary": "Get a product by ID"}, "delete": {"summary": "Delete a product by ID"}}
  }
}
```

---
This project is a simple starting point for building CRUD APIs with OpenAPI documentation.
