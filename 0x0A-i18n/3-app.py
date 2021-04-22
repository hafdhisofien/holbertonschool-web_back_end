#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    class config
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def welcome_holberton() -> str:
    """
    render of index
    """
    return render_template('0-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Get best supported language
    """
    return request.accept_languages.best_match(app.config.get['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
