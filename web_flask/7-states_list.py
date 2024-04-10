#!/usr/bin/python3
""" This modules import Flask class """
from flask import Flask, render_template
from models import storage

"""Starts a Flask web application"""
if __name__ == '__main__':
    app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
