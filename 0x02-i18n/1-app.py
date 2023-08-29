#!/usr/bin/env python3
'''1-app'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    '''Flask app config contained in Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    '''View for the home route'''
    return render_template('1-index.html')
