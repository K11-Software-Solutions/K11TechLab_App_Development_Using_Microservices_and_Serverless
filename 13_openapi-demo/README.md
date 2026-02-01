# OpenAPI Demo Microservice

This project demonstrates a minimal Flask microservice documented with OpenAPI 3.0.

## Features
- Simple `/hello` endpoint returns a hello message
- OpenAPI 3.0 spec served at `/openapi.json` and in `openapi.yaml`
- Ready for visualization in Swagger UI, Swagger Editor, or SwaggerHub

## Endpoints
- `GET /hello` — Returns `{ "message": "Hello, OpenAPI!" }`
- `GET /openapi.json` — Returns the OpenAPI 3.0 spec for this API

## How to Run
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the app:
   ```sh
   python app.py
   ```
3. Access the API at [http://localhost:5000/hello](http://localhost:5000/hello)
4. Access the OpenAPI spec at [http://localhost:5000/openapi.json](http://localhost:5000/openapi.json)

## Visualize with Swagger Tools
- Open [Swagger Editor](https://editor.swagger.io/) and import `openapi.yaml` or `http://localhost:5000/openapi.json`
- Try out the `/hello` endpoint interactively
- You can also use SwaggerHub, Redoc, Postman, Insomnia, etc.

## Example OpenAPI Spec
```yaml
openapi: 3.0.0
info:
  title: OpenAPI Demo API
  version: 1.0.0
paths:
  /hello:
    get:
      summary: Returns a hello message.
      responses:
        '200':
          description: A hello message.
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
```

---
This project is a simple starting point for building and documenting APIs with OpenAPI.
