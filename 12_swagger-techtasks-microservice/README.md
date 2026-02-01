# About Swagger (OpenAPI)

Swagger (now known as OpenAPI) is a framework for designing, documenting, and testing RESTful APIs. It uses a standard specification (swagger_config.json in this project) to describe API endpoints, request/response formats, and more.

**Benefits:**
- Interactive documentation and testing
- Standardized API design
- Easy integration and code generation


# Swagger Tools

Swagger tools provide interactive visualization and testing for your API:

- **Swagger UI:**
  - Visualizes your API from a Swagger/OpenAPI config file.
  - Lets you try out endpoints directly in the browser.
  - Can be run locally or used via hosted services.

- **Swagger Editor:**
  - Online editor for designing and testing Swagger/OpenAPI specs.
  - Import your config (e.g., http://localhost:5000/swaggerfile_8) to view and interact with your API.
  - Available at https://editor.swagger.io/

**How to use with this project:**
1. Start the Flask app: `python app.py`
2. Open Swagger Editor (https://editor.swagger.io/)
3. Import the config from `http://localhost:5000/swaggerfile_8`
4. Explore and test the API interactively

You can also use other OpenAPI-compatible tools for visualization and testing.


# Other OpenAPI/Swagger Tools

In addition to Swagger UI and Swagger Editor, you can use these tools for working with OpenAPI specs:

- **Redoc:** Beautiful documentation generator for OpenAPI specs ([https://redocly.com/redoc/](https://redocly.com/redoc/))
- **Postman:** API testing and development platform with OpenAPI import ([https://www.postman.com/](https://www.postman.com/))
- **Insomnia:** API client for testing and designing APIs ([https://insomnia.rest/](https://insomnia.rest/))
- **OpenAPI Generator:** Generate client SDKs and server stubs in many languages ([https://openapi-generator.tech/](https://openapi-generator.tech/))
- **Stoplight Studio:** Visual OpenAPI designer ([https://stoplight.io/studio/](https://stoplight.io/studio/))
- **SwaggerHub:** Collaborative platform for API design and documentation ([https://swagger.io/tools/swaggerhub/](https://swagger.io/tools/swaggerhub/))

These tools help you visualize, test, design, and generate code for APIs described by OpenAPI/Swagger specs.

  
  **Usage Example:**
  1. Sign up or log in to SwaggerHub.
  2. Click "Create API" and choose OpenAPI 2.0 or 3.0.
  3. Paste your Swagger/OpenAPI config (e.g., from `swagger_config.json`).
  4. Edit, visualize, and test endpoints interactively.
  5. Share your API with collaborators or generate client/server code.
  
  *Example:*
  ```yaml
  openapi: 3.0.0
  info:
    title: Technology Tasks API
    version: 1.0.0
  paths:
    /tasks:
      get:
        summary: List all technology tasks
        responses:
          '200':
            description: Success
  ```
  Paste this YAML in SwaggerHub to visualize and test the endpoint.



# Swagger Technology Tasks Microservice

This project demonstrates a Flask REST API with Swagger (OpenAPI) documentation for managing technology-related tasks.

## Features
- List all technology tasks
- Add a new technology task
- Get a task by name
- Delete a task by name
- Swagger (OpenAPI) config available at `/swaggerfile_8`

## Endpoints
- `GET /tasks` — List all tasks
- `POST /task` — Add a new task (JSON: {"name": ..., "description": ...})
- `GET /task/<name>` — Get a task by name
- `DELETE /task/<name>` — Delete a task by name
- `GET /swaggerfile_8` — Download the Swagger config (swagger_config.json)

## Data
- Tasks are stored in `technology_tasks.json` (editable, persistent)

## How to Run
1. Install dependencies: `pip install flask flask-cors`
2. Start the app: `python app.py`
3. Access the API at `http://localhost:5000/`
4. Access the Swagger config at `http://localhost:5000/swaggerfile_8`

## Example Task
```
{
  "name": "Docker",
  "description": "Containerize a Flask app and run it locally."
}
```

## Swagger/OpenAPI
- The API is documented using a Swagger 2.0 config (`swagger_config.json`).
- You can use Swagger UI or other tools to visualize and test the API using this config.
