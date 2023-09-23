#!/usr/bin/python3
# starts a Flask web application

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    # display “Hello HBNB!”
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    # display “HBNB”
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # display “C ” followed by the value of the text variable
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
