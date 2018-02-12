"""Flask Email notification."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from settings import PUBLIC_KEY, SECRET_KEY, DATABASE_URL
from api import api_bp, api_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.register_blueprint(api_bp)
    CORS(app)
    api_db.init_app(app)
    with app.app_context():
        api_db.create_all()

    @app.route('/')
    def hello():
        """Simple Hello world."""
        return 'Hello World!'
    return app

