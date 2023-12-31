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


@app.route("/states", strict_slashes=False)
def display_states():
    """render the list of cities on the template"""
    states = storage.all(State)
    return render_template("9-states.html", states=states, mode="states")


@app.route("/states/<id>", strict_slashes=False)
def display_cities(id):
    """render one state usiing the id on the template"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html",
                                   state=state, mode="state.id")
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
