from flask import Blueprint
from flask_restful import Api
from api.Mail import Mail

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Mail, '/mail')