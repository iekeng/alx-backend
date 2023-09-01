#!/usr/bin/env python3
'''4-app'''
from flask import ( 
    Flask, 
    render_template, 
    request
)
from flask_babel import (
    Babel, 
    gettext
)

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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''View for the home route'''
    home_title: str = gettext('home_title')
    home_header: str = gettext('home_header')
    return render_template('3-index.html')

@app.before_request
@app
def get_user():
