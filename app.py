#!./venv/bin/python3.7
# © Anas Abu Farraj
"""Learning Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
