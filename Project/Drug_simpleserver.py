#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

@app.route('/Drug/test', methods=['GET'])
def get_drug():
    return 'GET'
# curl -i http://localhost:5000/Drug/test


if __name__ == '__main__' :
    app.run(debug= True)