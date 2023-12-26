#!/usr/bin/python3
"""
    This scripts starts the web flask application
    listens on 0.0.0.0
    port: 5000
    debug mode: False
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display the string Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display the string HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """display what comes after /c/<text>"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    """display what comes after /python/<text>"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays the number n only if it's int otherwise 404"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
