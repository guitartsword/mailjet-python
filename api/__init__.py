from flask import Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from api.Mail import Mail, Notify, db as api_db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Mail, '/mail')
api.add_resource(Notify, '/notify')
