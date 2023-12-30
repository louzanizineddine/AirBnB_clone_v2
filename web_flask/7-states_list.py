#!/usr/bin/python3
"""
    This scripts starts the web flask application
    listens on 0.0.0.0
    port: 5000
    debug mode: False
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """render the list of cities on the template"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
