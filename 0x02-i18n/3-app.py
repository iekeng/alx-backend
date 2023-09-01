#!/usr/bin/env python3
'''3-app'''
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''View for the home route'''
    return render_template('3-index.html')
