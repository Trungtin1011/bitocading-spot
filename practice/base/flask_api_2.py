from flask import Flask, jsonify, request
import json

app = Flask("Product Server")

products = [
    {"id": 143, "name": "Notebook", "price": 5.49},
    {"id": 144, "name": "Black Marker", "price": 1.99},
]


# Example request - http://localhost:5000/products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


# Example request - http://localhost:5000/products/144 - with method GET
@app.route("/products/<id>", methods=["GET"])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)


# Example request - http://localhost:5000/products - with method POST
@app.route("/products", methods=["POST"])
def add_product():
    products.append(request.get_json())
    return "", 201


# Example request - http://localhost:5000/products/144 - with method PUT
@app.route("/products/<id>", methods=["PUT"])
def update_product(id):
    id = int(id)
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return "", 204


# Example request - http://localhost:5000/products/144 - with method DELETE
@app.route("/products/<id>", methods=["DELETE"])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return "", 204


if __name__ == "__main__":
    app.run(debug=False)
# When no port is specified, starts at default port 5000

### Example POST:
# curl -X POST -H "Content-Type: application/json" \
#    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
#    http://localhost:5000/products
