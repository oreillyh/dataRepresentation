#!flask/bin/python
from flask import Flask, jsonify, request, abort,  make_response, url_for, render_template, redirect #https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates Render template takes template and returns actual values
#from flask_cors import CORS
from ShoppingDAO import ShoppingDAO
from userinput import userinput

app = Flask(__name__,
            static_url_path='', 
            static_folder='.')
#CORS (app)

@app.route('/')
def hello_world():
    return 'Hello, Hugh!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != '' or request.form['password'] != '':
            # email and password passed in to app
            email = request.form['email']
            password = request.form['password']
            foundUser = userinput.checkUser(email, password)
            # create error
            if not foundUser:
                error = 'Invalid login'
            # redirects to main page on login   
            else:
                return redirect(url_for('groceries'))
        else:
            return error
    return render_template('login_style.html', error=error)#passes template as a keyword arg (ref Flask docs)

@app.route('/groceries', methods=['GET'])
def get_AllGroceries():
    results = ShoppingDAO.getAllGroceries()
    return jsonify(results)
# curl -i "http://127.0.0.1:5000/groceries"

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

#curl -i -H "Content-item:application/json" -X PUT -d "{"item\":\Tins\"name\":\"quantity\":\"10\"}" curl -i "http://127.0.0.1:5000/groceries/1"

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

@app.route('/nonfood', methods=['GET'])
def get_Allnonfood():
    results = ShoppingDAO.getAllnonfood()
    return jsonify(results)
# curl -i "http://127.0.0.1:5000/nonfood"

@app.route('/nonfood/<string:item>', methods =['GET'])
def get_nonfood(item):
    foundnonfood = ShoppingDAO.findnonfoodByItem(item)
    if not foundnonfood:
        abort(404)
    return jsonify(foundnonfood)

@app.route('/nonfood', methods=['POST'])
def create_nonfood():
       
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    nonfood={
        "id":  request.json['id'],
        "item": request.json['item'],
        "name":request.json['name'],
        "quantity":request.json['quantity']
    }
    values = (nonfood['item'], ['name'], ['quantity'])
    newid = ShoppingDAO.createnonfood(values)
    nonfood['id'] = newid
    return jsonify(nonfood)


@app.route('/nonfood/<string:id>', methods =['PUT'])
def update_nonfood(id):
    foundnonfood = ShoppingDAO.findnonfoodByItem()
    if len(foundnonfood) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'item' in request.json and type(request.json['item']) != str:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) is not int:
        abort(400)
    
    values = (foundnonfood['item'], ['name'], ['quantity'])
    ShoppingDAO.update(values)
    return jsonify(foundnonfood)

#curl -i -H "Content-item:application/json" -X PUT -d "{"item\":\Tins\"name\":\"quantity\":\"10\"}" curl -i "http://127.0.0.1:5000/nonfood/1"

app.route('/nonfood/<string:id>', methods =['DELETE'])
def delete_nonfood(id):
    deletenonfood = ShoppingDAO.delete(id)
    
    return  jsonify({'done':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)