#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

# new object.
app = Flask(__name__)

# decorator
@app.route("/", strict_slashes=False)
def hello_hbnn():
    return "Hello HBNB"


if(__name__ == '__main___'):
    app.run(host="0.0.0.0", port=5000, debug=True)
