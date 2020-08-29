from flask import Flask, jsonify, request

app = Flask(__name__)


products = [
  {
    "name": "Laptop",
    "price": 2155
  },
  {
    "name": "Teclado",
    "price": 35
  },
  {
    "name": "Mouse",
    "price": 15
  }
]


@app.route('/products')
def index():
    return jsonify(products), 200


@app.route('/products/<int:index>')
def get_product(index):
    product = products[index] if len(products) > index else "404"

    return jsonify(product), 200


@app.route('/products', methods=['POST'])
def add_product():
    product = request.get_json()

    products.append(product)

    return jsonify(products), 201


@app.route('/products/<int:index>', methods=['PUT', 'PATCH'])
def update_product(index):
    product = request.get_json()

    products[index] = product

    return jsonify(products)


@app.route('/products/<int:index>', methods=['DELETE'])
def delete_product(index):
    products.pop(index)

    return jsonify(products), 200


app.run()
