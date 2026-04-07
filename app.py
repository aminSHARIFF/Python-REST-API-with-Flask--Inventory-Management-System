from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Laptop", "brand": "HP", "price": 800, "quantity": 5, "barcode": "123456"},
    {"id": 2, "name": "Water Bottle", "brand": "Sharif Store", "price": 2.99, "quantity": 100, "barcode": "789012"},
    {"id": 3, "name": "Notebook", "brand": "Sharif Store", "price": 1.50, "quantity": 200, "barcode": "345678"}
]

@app.route('/')
def home():
    return "Sharif Inventory System is live"

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<int:id>', methods=['GET'])
def get_item(id):
    for item in inventory:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = {
        'id': len(inventory) + 1,
        'name': data['name'],
        'brand': data['brand'],
        'price': data['price'],
        'quantity': data['quantity'],
        'barcode': data['barcode']
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:id>', methods=['PATCH'])
def update_item(id):
    for item in inventory:
        if item['id'] == id:
            data = request.get_json()
            item['name'] = data.get('name', item['name'])
            item['brand'] = data.get('brand', item['brand'])
            item['price'] = data.get('price', item['price'])
            item['quantity'] = data.get('quantity', item['quantity'])
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_item(id):
    for item in inventory:
        if item['id'] == id:
            inventory.remove(item)
            return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

def fetch_from_openfoodfacts(barcode):
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 1:
            product = data['product']
            return {
                'name': product.get('product_name', 'Unknown'),
                'brand': product.get('brands', 'Unknown'),
                'barcode': barcode
            }
        return None
    except:
        return None

@app.route('/lookup/<barcode>', methods=['GET'])
def lookup_product(barcode):
    product = fetch_from_openfoodfacts(barcode)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)