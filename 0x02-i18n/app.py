#!/usr/bin/env python3
'''app'''
from datetime import datetime
from flask import Flask, g, request, render_template
from flask_babel import Babel
from pytz import timezone, exceptions
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
    locale: str = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    elif request.headers:
        locale = request.headers.get('locale', None)
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> List:
    '''Retrieves requested user'''
    user_id = request.args.get('login_as', None)

    if user_id:
        id = int(user_id)
        return users[id]
    return None


@babel.timezoneselector
def get_timezone():
    '''Select appropriate timezone'''
    if 'timezone' in request.args:
        tzone = request.args['timezone']
    elif 'timezone' in g.user:
        tzone = guser.user['timezone']
    try:
        if timezone(tzone):
            return timezone(tzone).zone
    except exceptions.UnknownTimeZoneError:
        return None
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    '''Sets the user in global'''
    user = get_user()
    g.user = user
    
    time_fmt = '%b %d, %Y, %I:%M:%S %p'
    g.time = datetime.strftime(datetime.now(), time_fmt)


@app.route('/')
def index() -> str:
    '''View for the home route'''
    return render_template('index.html')
