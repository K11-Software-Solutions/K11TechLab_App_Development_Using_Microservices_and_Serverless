from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    """A simple hello world endpoint."""
    return jsonify({"message": "Hello, OpenAPI!"})

@app.route('/openapi.json', methods=['GET'])
def openapi_spec():
    """Serve OpenAPI 3.0 spec for this API."""
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "OpenAPI Demo API",
            "version": "1.0.0",
            "description": "A simple demo of OpenAPI with Flask."
        },
        "paths": {
            "/hello": {
                "get": {
                    "summary": "Returns a hello message.",
                    "responses": {
                        "200": {
                            "description": "A hello message.",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "message": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return jsonify(spec)

if __name__ == '__main__':
    app.run(debug=True)
