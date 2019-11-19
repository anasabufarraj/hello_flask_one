#!./venv/bin/python3.7
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj.
# ------------------------------------------------------------------------------
"""Learning Flask"""

from flask import Flask

APP = Flask(__name__)


@APP.route('/')
@APP.route('/index')
def home():
    """Returns home page contents."""
    return '<h1>Hello Earth!</h1>'


if __name__ == '__main__':
    APP.run()
