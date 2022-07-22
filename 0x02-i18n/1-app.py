#!/usr/bin/env python3
'''Babel application'''
from flask_babel import Babel
from flask import g, request

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
    '''selecting a language tlanslation to use'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''defaulting the timezone to UTC'''
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone.best_match(app.config['TIMEZONE'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
