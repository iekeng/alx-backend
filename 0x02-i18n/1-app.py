from flask_babel import Babel
from flask import Flask
!  # /usr/bin/env python3
'''1-app'''


app = Flask(__name__)


class Config:
    '''Flask app config contained in Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
