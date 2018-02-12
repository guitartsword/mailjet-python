"""Flask Email notification."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from settings import PUBLIC_KEY, SECRET_KEY, DATABASE_URL
from api import api_bp, api_db

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
APP.register_blueprint(api_bp)
CORS = CORS(APP)
api_db.init_app(APP)

with APP.app_context():
    api_db.create_all()

@APP.route('/')
def hello():
    """Simple Hello world."""
    return 'Hello World!'
