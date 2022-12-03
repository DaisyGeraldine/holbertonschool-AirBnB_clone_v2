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


@app.route('/states')
def states_list():
    """  list of all State objects present in DBStorage """
    dict_states = storage.all(State)
    return render_template('9-states.html', states=dict_states)


@app.route('/states/<id>')
def states_id_list(id):
    """  list of City objects linked to the State sorted by name """
    dict_states = storage.all(State)
    find_name = dict_states.get('State.{}'.format(id), None)
    dict_city = storage.all(City)
    return render_template('9-states.html', index=id,
                           cities=dict_city, states=find_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
