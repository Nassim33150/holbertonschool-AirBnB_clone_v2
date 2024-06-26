#!/usr/bin/python3
""" This modules import Flask class """
from flask import Flask

"""Starts a Flask web application"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
