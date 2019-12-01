#!flask/bin/python
from flask import Flask, jsonify,  request, abort,  make_response
from flask_cors import CORS
from ShoppingDAO import ShoppingDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')
CORS (app)

groceries = [
    {
        "id":"1",
        "item":"Fruit",
        "name":"oranges",
        "quantity":6,
        
    },
    {
        "id":"2",
        "item":"Tins",
        "name":"beans",
        "quantity":3,
        
    },
    {
        "id":"3",
        "item":"DryGroceries",
        "name":"pasta",
        "quantity":1,
        
    },
    {
        "id":"4",
        "item":"Sauces",
        "name":"pepper",
        "quantity":1,
        
    },
    {
        "id":"5",
        "item":"Meat",
        "name":"steak",
        "quantity":6,
        
    },
    {
        "id":"6",
        "item":"Vegetables",
        "name":"onions",
        "quantity":6,
        
    },
    {
        "id":"7",
        "item":"Meat",
        "name":"chicken",
        "quantity":5,
    },
    {
        "id":"8",
        "item":"Vegetables",
        "name":"potatoes",
        "quantity":10,
        
    },
    {
        "id":"9",
        "item":"Sauces",
        "name":"carbonara",
        "quantity":3,
    },
    {
         "id":"10",
        "item":"Fruit",
        "name":"apples",
        "quantity":6,
    },
]

@app.route('/groceries', methods=['GET'])
def get_AllGroceries():
    return jsonify( {'groceries':groceries})
# curl -i "http://localhost:5000/groceries/"

@app.route('/groceries/<string:id>', methods =['GET'])
def get_groceries(id):
    foundGroceries = list(filter(lambda t : t['id'] == id , groceries))
    if len(foundGroceries) == 0:
        return jsonify( { 'groceries' : '' }),204
    return jsonify( { 'groceries' : foundGroceries[0] })

@app.route('/groceries', methods=['POST'])
def create_groceries():
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    groceries={
        "id":  request.json['id'],
        "item": request.json['item'],
        "name":request.json['name'],
        "quantity":request.json['quantity']
    }
    groceries.append(groceries)
    return jsonify( {'groceries':groceries }),201

#curl -i "http://localhost:5000/groceries/test"

@app.route('/groceries/<string:id>', methods =['PUT'])
def update_groceries(id):
    foundGroceries=list(filter(lambda t : t['id'] ==id, groceries))
    if len(foundGroceries) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'item' in request.json and type(request.json['item']) != str:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) is not int:
        abort(400)
    
    foundGroceries[0]['item']  = request.json.get('item', foundGroceries[0]['item'])
    foundGroceries[0]['name'] =request.json.get('name', foundGroceries[0]['name'])
    foundGroceries[0]['quantity'] =request.json.get('quantity', foundGroceries[0]['quantity'])
    return jsonify( {'groceries':foundGroceries[0]})

#curl -i -H "Content-item:application/json" -X PUT -d "{\"quantity\":\"10\"}" http://localhost:5000/groceries/1

app.route('/groceries/<string:id>', methods =['DELETE'])
def delete_groceries(id):
    foundGroceries = list(filter (lambda t : t['id'] == id, groceries))
    if len(foundGroceries) == 0:
        abort(404)
    groceries.remove(foundGroceries[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)