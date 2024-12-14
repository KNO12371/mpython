from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (In-memory storage for testing purposes)
data = [
    {"id": 1, "name": "Item 1", "price": 100},
    {"id": 2, "name": "Item 2", "price": 200},
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Simple Backend Server!"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in data if i['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    if not new_item.get('name') or not new_item.get('price'):
        return jsonify({"error": "Invalid data"}), 400
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in data if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    updated_data = request.json
    item.update(updated_data)
    return jsonify(item)

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [i for i in data if i['id'] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
