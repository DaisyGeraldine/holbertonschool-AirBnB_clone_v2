#!/usr/bin/python3
from flask import Flask

app = Flask(__name__) #new object

@app.route("/", strict_slashes=False) #decorator
def hello_hbnn():
    return "Hello HBNB"

if (__name__ == '__main___'):
    app.run(host="0.0.0.0", port=5000, debug=True)
