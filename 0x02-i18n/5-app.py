#!/usr/bin/env python3
'''5-app'''
from flask import Flask, g, request, render_template
from flask_babel import Babel
from typing import List

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''Flask app config contained in Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''Get best language match using the accept_langages header'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> List:
    '''Retrieves requested user'''
    user_id = request.args.get('login_as', None)

    if user_id and in users.keys():
        id = int(user_id)
        return users[id]
    return None


@app.before_request
def before_request():
    '''Sets the user in global'''
    user = get_user()
    g.user = user


@app.route('/')
def index() -> str:
    '''View for the home route'''
    return render_template('5-index.html')
