#!flask/bin/python
from flask import Flask, jsonify,  request, abort, title_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

Drugs = [
    {
        "id":"1",
        "title":"Humira",
        "Manufacturer":"Abbvie",
        "RevenueB$":20.47,
        "Disease":"Autoimmune"
    },
    {
         "id":"2",
        "title":"Eliquis",
        "Manufacturer":"BMS/Pfizer",
        "RevenueB$":9.87,
        "Disease":"Cardio"
    },
    {
         "id":"3",
        "title":"Revlimid",
        "Manufacturer":"Celgene",
        "RevenueB$":9.69,
        "Disease":"Oncology"
    },
    {
         "id":"4",
        "title":"Opdivo",
        "Manufacturer":"BMS",
        "RevenueB$":7.57,
        "Disease":"Oncology"
    },
    {
         "id":"5",
        "title":"Amgen/Pfizer/Takeda",
        "Manufacturer":"Enbrel",
        "RevenueB$":7.45,
        "Disease":"Immunology"
    },
    {
         "id":"6",
        "title":"MSD",
        "Manufacturer":"Keytruda",
        "RevenueB$":7.17,
        "Disease":"Oncology"
    },
    {
         "id":"7",
        "title":"Herceptin",
        "Manufacturer":"Roche",
        "RevenueB$":7.05,
        "Disease":"Oncology"
    },
    {
         "id":"8",
        "title":"Avastin",
        "Manufacturer":"Roche",
        "RevenueB$":6.92,
        "Disease":"Oncology"
    },
    {
         "id":"9",
        "title":"Rituxan",
        "Manufacturer":"Roche",
        "RevenueB$":6.82,
        "Disease":"Oncology"
    },
    {
         "id":"10",
        "title":"Xarelto",
        "Manufacturer":"Bayer/J&J",
        "RevenueB$":6.58,
        "Disease":"Cardio"
    },
]

@app.route('/Drugs', methods=['GET'])
def get_drug():
    return return jsonify( {'Drugs':Drugs})
# curl -i http://localhost:5000/Drugs/

@app.route('/Drugs/<string:id>', methods =['GET'])
def get_drug(id):
    foundDrugs = list(filter(lambda t : t['id'] == id , Drugs))
    if len(foundDrugs) == 0:
        return jsonify( { 'drug' : '' }),204
    return jsonify( { 'drug' : foundDrugs[0] })

@app.route('/Drugs', methods=['POST'])
def create_drug():
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    drug={
        "id":  request.json['id'],
        "title": request.json['title'],
        "Manufacturer":request.json['Manufacturer'],
        "RevenueB$":request.json['RevenueB$'],
        "Disease":request.json["Cardio"]

    }
    Drugs.append(drug)
    return jsonify( {'drug':drug }),201

#curl -i http://localhost:5000/Drugs/test

@app.route('/Drugs/<string:id>', methods =['PUT'])
def update_car(id):
    foundDrugs=list(filter(lambda t : t['id'] ==id, Drugs))
    if len(foundDrugs) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'Manufacturer' in request.json and type(request.json['Manufacturer']) is not str:
        abort(400)
    if 'RevenueB$' in request.json and type(request.json['RevenueB$']) is not int:
        abort(400)
    if 'Disease' in request.json and type(request.json['Disease']) is not int:
        abort(400)
    foundDrugs[0]['title']  = request.json.get('title', foundDrugs[0]['title'])
    foundDrugs[0]['Manufacturer'] =request.json.get('Manufacturer', foundDrugs[0]['Manufacturer'])
    foundDrugs[0]['RevenueB$'] =request.json.get('RevenueB$', foundDrugs[0]['RevenueB$'])
    foundDrugs[0]['Disease'] =request.json.get('Disease', foundDrugs[0]['Disease'])
    return jsonify( {'drug':foundDrugs[0]})

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"RevenueB$\":\"10\"}" http://localhost:5000/Drugs/1

app.route('/drugs/<string:id>', methods =['DELETE'])
def delete_car(id):
    founddrugs = list(filter (lambda t : t['id'] == id, drugs))
    if len(founddrugs) == 0:
        abort(404)
    drugs.remove(founddrugs[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)