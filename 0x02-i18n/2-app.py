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


@babel.localeselector
def get_locale():
    '''selects a language to use for
       that request'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''2-index.html'''
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
