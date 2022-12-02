#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display a message """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display a message HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_isfun(text=None):
    """ display a message with a text (parameter) """
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
