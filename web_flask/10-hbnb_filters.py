#!/usr/bin/python3
"""
Module: 11. HBNB filters.
Script that starts a Flask web application
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def filters():
    """ Displays the list of all State objects
        present in DBStorage sorted by name (A->Z)
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Module the close session database """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
