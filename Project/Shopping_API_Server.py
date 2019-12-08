#!flask/bin/python
from flask import Flask, jsonify,  request, abort,  make_response
from flask_cors import CORS
from ShoppingDAO import ShoppingDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='.')
CORS (app)


@app.route('/groceries', methods=['GET'])
def get_AllGroceries():
    results = ShoppingDAO.getAllGroceries()
    return jsonify(results)
# curl -i "http://localhost:5000/groceries/"

@app.route('/groceries/<string:item>', methods =['GET'])
def get_groceries(item):
    foundGroceries = ShoppingDAO.findGroceriesByItem(item)
    if not foundGroceries:
        abort(404)
    return jsonify(foundGroceries)

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
    values = (groceries['item'], ['name'], ['quantity'])
    newid = ShoppingDAO.createGroceries(values)
    groceries['id'] = newid
    return jsonify(groceries)

#curl -i "http://localhost:5000/groceries/test"

@app.route('/groceries/<string:id>', methods =['PUT'])
def update_groceries(id):
    foundGroceries = ShoppingDAO.findGroceriesByItem()
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
    
    values = (foundGroceries['item'], ['name'], ['quantity'])
    ShoppingDAO.update(values)
    return jsonify(foundGroceries)

#curl -i -H "Content-item:application/json" -X PUT -d "{\"quantity\":\"10\"}" http://localhost:5000/groceries/1

app.route('/groceries/<string:id>', methods =['DELETE'])
def delete_groceries(id):
    deleteGroceries = ShoppingDAO.delete(id)
    
    return  jsonify({'done':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)