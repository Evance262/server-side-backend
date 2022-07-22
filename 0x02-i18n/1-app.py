#!/usr/bin/env python3
'''Babel application'''
from flask_babel import Babel
from flask import request

app = Flask(__name__)

babel = Babel(app)


@app.route('/')
def index():
    '''1-index.html'''
    return render_template("1-index.html")


class Config(object):
    '''instantiating the babel object'''
    LANGUAGES = ["en", "fr"]
    TIMEZONE = ["UTC"]


@babel.localeselector
def get_locale():
    return locale.setlocale(LANGUAGES, TIMEZONE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
