#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """return string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """return string"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text="is cool"):
    """return string"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('index.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
