#!flask/bin/python
from flask import Flask

@app.route('/')
def index():
    return "hello world"

if __name_=='__main__':
    app.run(debug=True)