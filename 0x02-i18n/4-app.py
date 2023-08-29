#!/usr/bin/env python3
'''4-app'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import Union, List


class Config:
    '''Flask app config contained in Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[List, str]:
    '''Get best language match using the accept_langages header'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''View for the home route'''
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    return render_template('4-index.html')
