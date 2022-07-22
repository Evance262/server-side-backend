#!/usr/bin/env python3
'''Babel application'''
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''instantiating the babel object'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@app.route('/')
def index():
    '''1-index.html'''
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
