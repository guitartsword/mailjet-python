"""Flask Email notification."""
from flask import Flask
from settings import PUBLIC_KEY, SECRET_KEY
from api import api_bp

APP = Flask(__name__)
APP.register_blueprint(api_bp)

@APP.route('/')
def hello():
    """Simple Hello world."""
    return 'Hello World!'
