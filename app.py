from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "name": "Laptop",
        "brand": "HP",
        "price": 800,
        "quantity": 5,
        "barcode": "123456"
    }
]

@app.route('/')
def home():
    return "Inventory API is running"

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
            return jsonify({'message': 'Item deleted successfully'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)