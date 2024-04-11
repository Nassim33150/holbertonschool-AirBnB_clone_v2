#!/usr/bin/python3
""" This modules import Flask class """
from flask import Flask, render_template
from models import *
from models import storage

"""Starts a Flask web application"""
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ This function returns a template with all states """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ This function closes the session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
