#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

# new object.
app = Flask(__name__)
app.url_map.strict_slashes = False


# decorator
@app.route("/")
def hello_hbnb():
    return "Hello HBNB"


if(__name__ == '__main___'):
    app.run(host="0.0.0.0", port=5000, debug=True)
