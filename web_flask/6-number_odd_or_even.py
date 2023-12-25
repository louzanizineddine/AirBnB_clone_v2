#!/usr/bin/pyhton3
"""
    This scripts starts the web flask application
    listens on 0.0.0.0
    port: 5000
    debug mode: False
"""

from flask import Flask
from flask import render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_number(n):
    """Displays the number template n only if it's int otherwise 404"""
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Displays the number parity even or odd"""
    if(n % 2 == 0):
        return render_template("6-number_odd_or_even.html", parity="even")
    return render_template("6-number_odd_or_even.html", parity="odd")
        


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
