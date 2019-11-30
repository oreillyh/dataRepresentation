#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

groceries = [
    {
        "id":"1",
        "type":"Fruit",
        "name":"oranges",
        "quantity":6
        
    },
    {
        "id":"2",
        "type":"Tins",
        "name":"beans",
        "quantity":3
        
    },
    {
        "id":"3",
        "type":"DryGroceries",
        "name":"pasta",
        "quantity":1
        
    },
    {
        "id":"4",
        "type":"Sauces",
        "name":"pepper",
        "quantity":1
        
    },
    {
        "id":"5",
        "type":"Meat",
        "name":"steak",
        "quantity":7
        
    },
    {
        "id":"6",
        "type":"Vegetables",
        "name":"onions",
        "quantity":6
        
    },
    {
        "id":"7",
        "type":"Meat",
        "name":"chicken",
        "quantity":7
    },
    {
        "id":"8",
        "type":"Vegetables",
        "name":"potatoes",
        "quantity":10
        
    },
    {
        "id":"9",
        "type":"Sauces",
        "name":"carbonara",
        "quantity":6
        
    },
    {
        "id":"10",
        "type":"Fruit",
        "name":"apples",
        "quantity":6
    }
]

@app.route('/groceries', methods=['GET'])
def get_Groceries():
    return jsonify( {'grocery':groceries})
# curl -i http://localhost:5000/groceries/

@app.route('/groceries/<string:id>', methods =['GET'])
def get_Groceries(id):
    foundGroceries = list(filter(lambda t : t['id'] == id , groceries))
    if len(foundGroceries) == 0:
        return jsonify( { 'grocerY' : '' }),204
    return jsonify( { 'grocery' : foundGroceries[0] })

@app.route('/groceries', methods=['POST'])
def create_groceries():
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    groceries={
        "id":  request.json['id'],
        "type": request.json['type'],
        "name":request.json['name'],
        "quantity":request.json['quantity']
    }
    groceries.append(groceries)
    return jsonify( {'grocery':groceries }),201

#curl -i http://localhost:5000/groceries/test

@app.route('/groceries/<string:id>', methods =['PUT'])
def update_car(id):
    foundGroceries=list(filter(lambda t : t['id'] ==id, groceries))
    if len(foundGroceries) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'type' in request.json and type(request.json['type']) != str:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) is not int:
        abort(400)
    
    foundGroceries[0]['type']  = request.json.get('type', foundGroceries[0]['type'])
    foundGroceries[0]['name'] =request.json.get('name', foundGroceries[0]['name'])
    foundGroceries[0]['quantity'] =request.json.get('quantity', foundGroceries[0]['quantity'])
    return jsonify( {'grocery':foundGroceries[0]})

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"quantity\":\"10\"}" http://localhost:5000/groceries/1

app.route('/groceries/<string:id>', methods =['DELETE'])
def delete_car(id):
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