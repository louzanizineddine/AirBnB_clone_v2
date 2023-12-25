#!/usr/bin/pyhton3
"""
    This scripts starts the web flask application
    listens on 0.0.0.0
    port: 5000
    debug mode: False
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display the string Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
