#!/usr/bin/python3
'''starts a Flask web application
'''
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


@app.route('/python/<text>', strict_slashes=False)
def python_route(text='cool'):
    # display “Python ”, followed by the value of the text variable
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
