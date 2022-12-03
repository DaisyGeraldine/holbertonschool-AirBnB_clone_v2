#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_close(self):
    """ tear down database """
    storage.close()


@app.route('/states_list')
def states_list():
    """ list of all State objects present in DBStorage sorted by name """
    dict_states = storage.all(State)
    return render_template('7-states_list.html', states=dict_states)


@app.route('/cities_by_states')
def cities_list():
    """ load all cities of a State """
    dict_states = storage.all(State)
    dict_city = storage.all(City)
    return render_template('8-cities_by_states.html', cities=dict_city, states=dict_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
