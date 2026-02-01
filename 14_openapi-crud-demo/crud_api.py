from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data store for demo
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 500},
    {"id": 4, "name": "Monitor", "price": 300},
    {"id": 5, "name": "Keyboard", "price": 50},
    {"id": 6, "name": "Mouse", "price": 40},
    {"id": 7, "name": "Printer", "price": 150},
    {"id": 8, "name": "Webcam", "price": 80}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_id = max([p['id'] for p in products], default=0) + 1
    product = {"id": new_id, "name": data["name"], "price": data["price"]}
    products.append(product)
    return jsonify(product), 201

@app.route('/product/<int:pid>', methods=['GET'])
def get_product(pid):
    for product in products:
        if product["id"] == pid:
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/product/<int:pid>', methods=['DELETE'])
def delete_product(pid):
    global products
    products = [p for p in products if p["id"] != pid]
    return jsonify({"result": "Deleted"})

@app.route('/openapi.json', methods=['GET'])
def openapi_spec():
    # Serve OpenAPI 3.0 spec for this CRUD API
    import json
    with open('openapi.json') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(debug=True)
