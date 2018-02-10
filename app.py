"""Flask Email notification."""
from flask import Flask
from settings import PUBLIC_KEY, SECRET_KEY
from api import api_bp
from flask_cors import CORS

APP = Flask(__name__)
APP.register_blueprint(api_bp)
CORS = CORS(APP)

@APP.route('/')
def hello():
    """Simple Hello world."""
    return 'Hello World!'
