#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed.
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """
    find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user(request.args.get('login_as'))


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
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
